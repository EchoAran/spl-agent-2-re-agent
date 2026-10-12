
let pages = [];
let active = null;
const nav = document.getElementById('nav');
const content = document.getElementById('content');
const meta = document.getElementById('meta');
const links = document.getElementById('links');
const search = document.getElementById('search');

async function init() {
  pages = await fetch('../index/search-index.json').then(r => r.json());
  renderNav(pages);
  renderPage(pages[0]);
}

function renderNav(items) {
  nav.innerHTML = items.map(p => `<div class="nav-item ${active === p.page_id ? 'active' : ''}" data-id="${p.page_id}"><div>${escapeHtml(p.title)}</div><div class="kind">${p.entity_kind}</div></div>`).join('');
  nav.querySelectorAll('.nav-item').forEach(el => el.addEventListener('click', () => renderPage(pages.find(p => p.page_id === el.dataset.id))));
}

async function renderPage(pageSummary) {
  if (!pageSummary) return;
  active = pageSummary.page_id;
  renderNav(filterPages(search.value));
  const fileName = pageSummary.page_id.replace(/[^0-9A-Za-z_]+/g, '_').replace(/^_+|_+$/g, '') || 'root';
  const page = await fetch(`../pages/${fileName}.json`).then(r => r.json());
  meta.innerHTML = `<span class="pill">${page.entity_kind}</span>${page.tags.map(t => `<span class="pill">${escapeHtml(t)}</span>`).join('')}`;
  content.innerHTML = markdownLite(page.body_markdown);
  links.innerHTML = `<h2>Links</h2><div class="link-list">
    ${(page.outgoing_links || []).map(l => `<div>→ ${escapeHtml(l.relation)}: ${escapeHtml(l.label || l.target_page_id)}</div>`).join('')}
    ${(page.incoming_links || []).map(l => `<div>← ${escapeHtml(l.relation)}: ${escapeHtml(l.label || l.source_page_id)}</div>`).join('')}
  </div>`;
}

function filterPages(q) {
  q = (q || '').toLowerCase();
  if (!q) return pages;
  return pages.filter(p => [p.title, p.summary, p.qualified_name, p.entity_kind, (p.tags || []).join(' ')].join(' ').toLowerCase().includes(q));
}

search.addEventListener('input', () => renderNav(filterPages(search.value)));

function markdownLite(text) {
  const blocks = [];
  let escaped = escapeHtml(text).replace(/```spl\n([\s\S]*?)```/g, (_, code) => {
    const id = `@@CODE_${blocks.length}@@`;
    blocks.push(`<pre><code>${code}</code></pre>`);
    return id;
  });
  escaped = escaped
    .replace(/^# (.*)$/gm, '<h1>$1</h1>')
    .replace(/^## (.*)$/gm, '<h2>$1</h2>')
    .replace(/^### (.*)$/gm, '<h3>$1</h3>')
    .replace(/^- (.*)$/gm, '<li>$1</li>')
    .replace(/\n\n/g, '<br/><br/>')
    .replace(/\[\[([^\]]+)\]\]/g, '<strong>$1</strong>');
  blocks.forEach((block, idx) => {
    escaped = escaped.replace(`@@CODE_${idx}@@`, block);
  });
  return escaped;
}

function escapeHtml(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

init();
