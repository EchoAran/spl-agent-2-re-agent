const messages = document.getElementById("messages");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const startBtn = document.getElementById("startBtn");
const sessionInfo = document.getElementById("sessionInfo");
const runBtn = document.getElementById("runBtn");
const pauseBtn = document.getElementById("pauseBtn");
const resumeBtn = document.getElementById("resumeBtn");
const repoUrlInput = document.getElementById("repoUrlInput");
const projectNameInput = document.getElementById("projectNameInput");

let ws = null;
let sessionId = null;
let interviewerId = null;
let sessionStatus = "idle";
const SESSION_CACHE_KEY = "multi_agent_interview_current_session";
const renderedMessageIds = new Set();

function addMessage({ role, agentName, text, roundIndex }) {
  const key = `${role}|${agentName}|${text}|${roundIndex}`;
  if (renderedMessageIds.has(key)) {
    return;
  }
  renderedMessageIds.add(key);
  const div = document.createElement("div");
  div.className = `msg ${role === "user" ? "user" : "agent"}`;
  const meta = document.createElement("div");
  meta.className = "meta";
  meta.textContent = role === "user" ? "用户" : `${agentName}`;
  const body = document.createElement("div");
  body.textContent = text;
  div.append(meta, body);
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function updateSessionInfo(reason) {
  if (!sessionId) {
    sessionInfo.textContent = "未创建会话";
    return;
  }
  const suffix = reason ? `，原因：${reason}` : "";
  sessionInfo.textContent = `会话：${sessionId}，状态：${sessionStatus}${suffix}`;
}

async function createSession() {
  const githubRepoUrl = repoUrlInput.value.trim();
  if (!githubRepoUrl) {
    throw new Error("请先填写 GitHub 仓库 URL");
  }
  const projectName = projectNameInput.value.trim();
  const payload = {
    github_repo_url: githubRepoUrl,
    project_name: projectName || null,
  };
  const response = await fetch("/api/sessions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(text);
  }
  return response.json();
}

function persistSessionCache() {
  if (!sessionId) {
    return;
  }
  localStorage.setItem(
    SESSION_CACHE_KEY,
    JSON.stringify({
      sessionId,
      interviewerId,
    }),
  );
}

function clearSessionCache() {
  localStorage.removeItem(SESSION_CACHE_KEY);
}

async function loadSessionSnapshot(id) {
  const response = await fetch(`/api/sessions/${id}/messages`);
  if (!response.ok) {
    throw new Error(await response.text());
  }
  return response.json();
}

function connectWebSocket(id) {
  if (ws) {
    ws.close();
  }
  const protocol = location.protocol === "https:" ? "wss" : "ws";
  ws = new WebSocket(`${protocol}://${location.host}/ws/${id}`);
  ws.onmessage = (event) => {
    const payload = JSON.parse(event.data);
    if (payload.type === "session_status") {
      sessionStatus = payload.status || "unknown";
      updateSessionInfo(payload.reason);
      if (sessionStatus === "completed") {
        addMessage({
          role: "system",
          agentName: "系统",
          text: `访谈已结束。${payload.reason || ""}`,
          roundIndex: 0,
        });
        clearSessionCache();
      }
      return;
    }
    if (payload.type === "message") {
      const message = payload.message;
      addMessage({
        role: message.agent_id === interviewerId ? "interviewer" : "agent",
        agentName: message.agent_name,
        text: message.text,
        roundIndex: message.round_index,
      });
      return;
    }
    if (payload.type === "error") {
      addMessage({ role: "system", agentName: "系统", text: payload.text, roundIndex: 0 });
    }
  };
}

startBtn.addEventListener("click", async () => {
  try {
    renderedMessageIds.clear();
    messages.innerHTML = "";
    const data = await createSession();
    sessionId = data.session_id;
    interviewerId = data.interviewer_agent_id;
    sessionStatus = data.status || "running";
    persistSessionCache();
    connectWebSocket(sessionId);
    updateSessionInfo();
    addMessage({
      role: "system",
      agentName: "系统",
      text: "会话已建立，系统将自动开始访谈。你可以随时插话。",
      roundIndex: 0,
    });
  } catch (error) {
    addMessage({
      role: "system",
      agentName: "系统",
      text: `创建会话失败：${error.message}`,
      roundIndex: 0,
    });
  }
});

runBtn.addEventListener("click", () => {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    return;
  }
  ws.send(JSON.stringify({ type: "start" }));
});

pauseBtn.addEventListener("click", () => {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    return;
  }
  ws.send(JSON.stringify({ type: "pause" }));
});

resumeBtn.addEventListener("click", () => {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    return;
  }
  ws.send(JSON.stringify({ type: "resume" }));
});

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = userInput.value.trim();
  if (!text || !ws || ws.readyState !== WebSocket.OPEN) {
    return;
  }
  addMessage({ role: "user", agentName: "用户", text, roundIndex: 0 });
  ws.send(JSON.stringify({ type: "user_message", text }));
  userInput.value = "";
});

async function restoreSessionIfExists() {
  const raw = localStorage.getItem(SESSION_CACHE_KEY);
  if (!raw) {
    return;
  }
  try {
    const cached = JSON.parse(raw);
    if (!cached.sessionId) {
      clearSessionCache();
      return;
    }
    const snapshot = await loadSessionSnapshot(cached.sessionId);
    sessionId = snapshot.session_id;
    interviewerId = snapshot.interviewer_agent_id || cached.interviewerId || "interviewer";
    sessionStatus = snapshot.status || "unknown";
    renderedMessageIds.clear();
    messages.innerHTML = "";
    snapshot.messages.forEach((message) => {
      addMessage({
        role: message.agent_id === interviewerId ? "interviewer" : "agent",
        agentName: message.agent_name,
        text: message.text,
        roundIndex: message.round_index,
      });
    });
    updateSessionInfo(snapshot.reason);
    connectWebSocket(sessionId);
  } catch (error) {
    clearSessionCache();
  }
}

restoreSessionIfExists();
