# LLM Wiki

> Single-file code knowledge wiki compiled from repository SPL artifacts, cards, and graphs.

## Build Summary

- Root path: `C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo`
- Root package SPL: `spl/commerce_ops_demo/__package__.spl`
- Packages: 2
- Files: 9
- Classes: 13
- Methods/functions: 43
- Wiki pages: 77

## Table of Contents

- [Repository Wiki](#home-root) `home`
- [commerce_ops_demo](#package-commerce-ops-demo) `package`
- [commerce_ops_demo.commerce_ops](#package-commerce-ops-demo-commerce-ops) `package`
- [commerce_ops_demo.commerce_ops](#file-commerce-ops-init-py) `file`
- [commerce_ops_demo.commerce_ops.catalog](#file-commerce-ops-catalog-py) `file`
- [commerce_ops_demo.commerce_ops.cli](#file-commerce-ops-cli-py) `file`
- [commerce_ops_demo.commerce_ops.models](#file-commerce-ops-models-py) `file`
- [commerce_ops_demo.commerce_ops.notifications](#file-commerce-ops-notifications-py) `file`
- [commerce_ops_demo.commerce_ops.payments](#file-commerce-ops-payments-py) `file`
- [commerce_ops_demo.commerce_ops.pricing](#file-commerce-ops-pricing-py) `file`
- [commerce_ops_demo.commerce_ops.repository](#file-commerce-ops-repository-py) `file`
- [commerce_ops_demo.commerce_ops.services](#file-commerce-ops-services-py) `file`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog](#class-commerce-ops-demo-commerce-ops-catalog-productcatalog) `class`
- [commerce_ops_demo.commerce_ops.models.CartItem](#class-commerce-ops-demo-commerce-ops-models-cartitem) `class`
- [commerce_ops_demo.commerce_ops.models.Customer](#class-commerce-ops-demo-commerce-ops-models-customer) `class`
- [commerce_ops_demo.commerce_ops.models.Order](#class-commerce-ops-demo-commerce-ops-models-order) `class`
- [commerce_ops_demo.commerce_ops.models.Product](#class-commerce-ops-demo-commerce-ops-models-product) `class`
- [commerce_ops_demo.commerce_ops.notifications.NotificationService](#class-commerce-ops-demo-commerce-ops-notifications-notificationservice) `class`
- [commerce_ops_demo.commerce_ops.payments.PaymentError](#class-commerce-ops-demo-commerce-ops-payments-paymenterror) `class`
- [commerce_ops_demo.commerce_ops.payments.PaymentGateway](#class-commerce-ops-demo-commerce-ops-payments-paymentgateway) `class`
- [commerce_ops_demo.commerce_ops.payments.PaymentReceipt](#class-commerce-ops-demo-commerce-ops-payments-paymentreceipt) `class`
- [commerce_ops_demo.commerce_ops.pricing.PriceQuote](#class-commerce-ops-demo-commerce-ops-pricing-pricequote) `class`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy](#class-commerce-ops-demo-commerce-ops-pricing-pricingpolicy) `class`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository](#class-commerce-ops-demo-commerce-ops-repository-orderrepository) `class`
- [commerce_ops_demo.commerce_ops.services.OrderService](#class-commerce-ops-demo-commerce-ops-services-orderservice) `class`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__](#method-commerce-ops-demo-commerce-ops-catalog-productcatalog-init) `method`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get](#method-commerce-ops-demo-commerce-ops-catalog-productcatalog-get) `method`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available](#method-commerce-ops-demo-commerce-ops-catalog-productcatalog-list-available) `method`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items](#method-commerce-ops-demo-commerce-ops-catalog-productcatalog-release-items) `method`
- [commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items](#method-commerce-ops-demo-commerce-ops-catalog-productcatalog-reserve-items) `method`
- [commerce_ops_demo.commerce_ops.catalog.normalize_sku](#method-commerce-ops-demo-commerce-ops-catalog-normalize-sku) `function`
- [commerce_ops_demo.commerce_ops.cli.build_demo_service](#method-commerce-ops-demo-commerce-ops-cli-build-demo-service) `function`
- [commerce_ops_demo.commerce_ops.cli.main](#method-commerce-ops-demo-commerce-ops-cli-main) `function`
- [commerce_ops_demo.commerce_ops.cli.parse_cart](#method-commerce-ops-demo-commerce-ops-cli-parse-cart) `function`
- [commerce_ops_demo.commerce_ops.cli.run_checkout_demo](#method-commerce-ops-demo-commerce-ops-cli-run-checkout-demo) `function`
- [commerce_ops_demo.commerce_ops.models.CartItem.validate](#method-commerce-ops-demo-commerce-ops-models-cartitem-validate) `method`
- [commerce_ops_demo.commerce_ops.models.Customer.can_spend](#method-commerce-ops-demo-commerce-ops-models-customer-can-spend) `method`
- [commerce_ops_demo.commerce_ops.models.Customer.credit](#method-commerce-ops-demo-commerce-ops-models-customer-credit) `method`
- [commerce_ops_demo.commerce_ops.models.Customer.debit](#method-commerce-ops-demo-commerce-ops-models-customer-debit) `method`
- [commerce_ops_demo.commerce_ops.models.Order.add_event](#method-commerce-ops-demo-commerce-ops-models-order-add-event) `method`
- [commerce_ops_demo.commerce_ops.models.Order.mark_cancelled](#method-commerce-ops-demo-commerce-ops-models-order-mark-cancelled) `method`
- [commerce_ops_demo.commerce_ops.models.Order.mark_paid](#method-commerce-ops-demo-commerce-ops-models-order-mark-paid) `method`
- [commerce_ops_demo.commerce_ops.models.Product.release](#method-commerce-ops-demo-commerce-ops-models-product-release) `method`
- [commerce_ops_demo.commerce_ops.models.Product.reserve](#method-commerce-ops-demo-commerce-ops-models-product-reserve) `method`
- [commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__](#method-commerce-ops-demo-commerce-ops-notifications-notificationservice-init) `method`
- [commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert](#method-commerce-ops-demo-commerce-ops-notifications-notificationservice-send-low-stock-alert) `method`
- [commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt](#method-commerce-ops-demo-commerce-ops-notifications-notificationservice-send-receipt) `method`
- [commerce_ops_demo.commerce_ops.notifications.format_currency](#method-commerce-ops-demo-commerce-ops-notifications-format-currency) `function`
- [commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__](#method-commerce-ops-demo-commerce-ops-payments-paymentgateway-init) `method`
- [commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize](#method-commerce-ops-demo-commerce-ops-payments-paymentgateway-authorize) `method`
- [commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund](#method-commerce-ops-demo-commerce-ops-payments-paymentgateway-refund) `method`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__](#method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-init) `method`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon](#method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-apply-coupon) `method`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal](#method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-calculate-subtotal) `method`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax](#method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-calculate-tax) `method`
- [commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote](#method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-quote) `method`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__](#method-commerce-ops-demo-commerce-ops-repository-orderrepository-init) `method`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository.get](#method-commerce-ops-demo-commerce-ops-repository-orderrepository-get) `method`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer](#method-commerce-ops-demo-commerce-ops-repository-orderrepository-list-by-customer) `method`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid](#method-commerce-ops-demo-commerce-ops-repository-orderrepository-mark-paid) `method`
- [commerce_ops_demo.commerce_ops.repository.OrderRepository.save](#method-commerce-ops-demo-commerce-ops-repository-orderrepository-save) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService.__init__](#method-commerce-ops-demo-commerce-ops-services-orderservice-init) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService._build_order](#method-commerce-ops-demo-commerce-ops-services-orderservice-build-order) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService._charge](#method-commerce-ops-demo-commerce-ops-services-orderservice-charge) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService._notify_customer](#method-commerce-ops-demo-commerce-ops-services-orderservice-notify-customer) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService.cancel_order](#method-commerce-ops-demo-commerce-ops-services-orderservice-cancel-order) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService.checkout](#method-commerce-ops-demo-commerce-ops-services-orderservice-checkout) `method`
- [commerce_ops_demo.commerce_ops.services.OrderService.customer_history](#method-commerce-ops-demo-commerce-ops-services-orderservice-customer-history) `method`
- [Workflow from commerce_ops_demo.commerce_ops.cli.build_demo_service](#workflow-commerce-ops-demo-commerce-ops-cli-build-demo-service) `workflow`
- [Workflow from commerce_ops_demo.commerce_ops.cli.main](#workflow-commerce-ops-demo-commerce-ops-cli-main) `workflow`
- [Workflow from commerce_ops_demo.commerce_ops.cli.parse_cart](#workflow-commerce-ops-demo-commerce-ops-cli-parse-cart) `workflow`
- [Workflow from commerce_ops_demo.commerce_ops.cli.run_checkout_demo](#workflow-commerce-ops-demo-commerce-ops-cli-run-checkout-demo) `workflow`
- [Authentication](#topic-authentication) `topic`
- [Configuration](#topic-configuration) `topic`
- [External Integration](#topic-external-integration) `topic`
- [Persistence](#topic-persistence) `topic`
- [Validation](#topic-validation) `topic`

---

<a id="home-root"></a>

## Repository Wiki

- Page ID: `home:root`
- Type: `navigation` / `home`
- Qualified name: `Repository Wiki`
- Tags: `home`, `overview`

### Summary

Compiled code repository LLM Wiki.

### Wiki Content

# Repository Wiki

- Root SPL: `spl/commerce_ops_demo/__package__.spl`
- Packages: 2
- Files: 9
- Classes: 13
- Methods/functions: 43

This wiki is compiled from SPL artifacts, cards, and repository graphs.

### Source Evidence

- `manifest.json`

### Symbols

- `evidence: missing; confidence: not_available; source: static_analysis`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---

<a id="package-commerce-ops-demo"></a>

## commerce_ops_demo

- Page ID: `package:commerce_ops_demo`
- Type: `entity` / `package`
- Qualified name: `commerce_ops_demo`
- Package: `commerce_ops_demo`
- Tags: `Container package for a commerce operations demo subsystem`, `package`

### Summary

Provide a repository-level container for a demo commerce operations subsystem.

### SPL Content

```spl
[DEFINE_AGENT: "A package that groups related modules into a subsystem with public surface, internal structure, dependency direction, and repository role" commerce_ops_demo]

[DEFINE_PERSONA:]
    ROLE: "Container package for a commerce operations demo subsystem"
    LAYER: "repository root container"
    ABSTRACTION_LEVEL: "Package-level; describes subsystem responsibility without expanding file, class, or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, extend, test, or integrate this package"
    INTEREST: "Package purpose, public APIs, internal subsystems, dependency direction, workflows, boundaries, and repository role"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a repository-level container for a demo commerce operations subsystem."
    PublicSurface: "evidence: missing; confidence: not_available; source: static_analysis"
    InternalSubsystems: "Subpackage: commerce_ops — self-contained commerce operations subsystem with checkout and order management orchestration, domain models, in-memory adapters, and a CLI demo"
    PackageMechanism: "Acts as a container; all functionality and public surface are provided by the commerce_ops subpackage; this package adds no additional coordination or APIs."
    DependencyDirection: "No incoming or outgoing package edges observed at this level; functionality and dependency flow are delegated to the commerce_ops child package."
    RepositoryRole: "Top-level package grouping the commerce_ops demo subsystem for checkout, order management, and customer interactions."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> package_name </REF>: text "commerce_ops_demo"
    <REF> package_path </REF>: text "commerce_ops_demo"
    <REF> source_directory </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo"

    <!-- Purpose and architecture -->
    <REF> purpose </REF>: text "Provide a repository-level container for a demo commerce operations subsystem."
    <REF> role </REF>: text "Container package for a commerce operations demo subsystem"
    <REF> repository_role </REF>: text "Top-level package grouping the commerce_ops demo subsystem for checkout, order management, and customer interactions."

    <!-- Public surface -->
    <REF> public_api </REF>: List [text] []
    <REF> entrypoints </REF>: List [text] []

    <!-- Internal structure -->
    <REF> files </REF>: List [text] []
    <REF> subpackages </REF>: List [text] ["commerce_ops: Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo."]
    <REF> subsystem_groups </REF>: List [text] ["Subpackage: commerce_ops — self-contained commerce operations subsystem with checkout and order management orchestration, domain models, in-memory adapters, and a CLI demo"]
    <REF> package_mechanism </REF>: text "Acts as a container; all functionality and public surface are provided by the commerce_ops subpackage; this package adds no additional coordination or APIs."

    <!-- Dependencies -->
    <REF> dependencies </REF>: List [text] []
    <REF> dependency_direction </REF>: text "No incoming or outgoing package edges observed at this level; functionality and dependency flow are delegated to the commerce_ops child package."

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] []
    <REF> outputs </REF>: List [text] []
    <REF> key_workflows </REF>: List [text] ["Delegates workflows such as checkout, cancellation, customer history, and CLI demo to the commerce_ops subpackage"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] []
    <REF> errors </REF>: List [text] []
    <REF> architectural_assumptions </REF>: List [text] ["All operational logic and public surface reside in the commerce_ops subpackage", "This package does not re-export symbols from child packages", "External integrations should import from the commerce_ops subpackage for functionality"]

    <!-- Traceability -->
    <REF> file_refs </REF>: List [text] []
    <REF> subpackage_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/__package__.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines package-level reverse-engineering information.
     It should let a developer understand what subsystem this package represents, what it exposes, how its files and subpackages cooperate, and how it fits into the repository.
     Do NOT expand file internals.
     Do NOT expand class or method details.
     Use file_refs and subpackage_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    PackageLevelOnly: "Describe the package as a subsystem; do not expand individual files, classes, or methods" LOG "package_over_expansion"
    BoundaryAccuracy: "Distinguish what the package owns from what it delegates to sibling, child, parent, or external packages" LOG "package_boundary_error"
    DependencyDirection: "Preserve intended dependency direction and architectural layer" LOG "package_dependency_error"
    WorkflowSummary: "Describe workflows only at package level without expanding implementation steps" LOG "package_workflow_over_detail"
    Traceability: "Refer to file-level and subpackage-level SPL artifacts by reference instead of inlining them" LOG "subsystem_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `package:commerce_ops_demo`
- Entity kind: `package`
- Package: `commerce_ops_demo`

## Wiki Summary

# commerce_ops_demo

Provide a repository-level container for a demo commerce operations subsystem.

## Architecture Role
Container package for a commerce operations demo subsystem

## Public API
- evidence: missing; confidence: not_available; source: static_analysis

## Child Files
- evidence: missing; confidence: not_available; source: static_analysis

## Child Packages
- commerce_ops: Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo.

## Dependency Direction
No incoming or outgoing package edges observed at this level; functionality and dependency flow are delegated to the commerce_ops child package.

## Key Workflows
- Delegates workflows such as checkout, cancellation, customer history, and CLI demo to the commerce_ops subpackage

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/__package__.spl</SPL>

### Outgoing Links

- `contains_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/__package__.spl`

### Symbols

- `evidence: missing; confidence: not_available; source: static_analysis`

### Graph References

- `package_dependency:commerce_ops_demo`

---

<a id="package-commerce-ops-demo-commerce-ops"></a>

## commerce_ops_demo.commerce_ops

- Page ID: `package:commerce_ops_demo.commerce_ops`
- Type: `entity` / `package`
- Qualified name: `commerce_ops_demo.commerce_ops`
- Package: `commerce_ops_demo.commerce_ops`
- Tags: `package`, `subsystem; checkout and order management orchestration with domain models and in-memory adapters`

### Summary

Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo.

### SPL Content

```spl
[DEFINE_AGENT: "A package that groups related modules into a subsystem with public surface, internal structure, dependency direction, and repository role" commerce_ops]

[DEFINE_PERSONA:]
    ROLE: "subsystem; checkout and order management orchestration with domain models and in-memory adapters"
    LAYER: "application service and domain subsystem with in-memory adapters"
    ABSTRACTION_LEVEL: "Package-level; describes subsystem responsibility without expanding file, class, or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, extend, test, or integrate this package"
    INTEREST: "Package purpose, public APIs, internal subsystems, dependency direction, workflows, boundaries, and repository role"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo."
    PublicSurface: "CartItem; Customer; Order; Product; OrderService"
    InternalSubsystems: "Public surface: __init__.py re-exports CartItem, Customer, Order, Product, OrderService; Application service: services.py OrderService orchestrates checkout, cancellation, and history; Domain models: models.py core entities and validation (Product, Customer, Order, CartItem); Catalog and SKU utilities: catalog.py product index, reservation/release, normalize_sku; Pricing policy and quotes: pricing.py PricingPolicy and PriceQuote; Payments gateway and types: payments.py PaymentGateway, PaymentReceipt, PaymentError; Order repository (in-memory): repository.py OrderRepository; Notifications and currency formatting: notifications.py NotificationService, format_currency; CLI demo and wiring: cli.py build_demo_service, parse_cart, run_checkout_demo, main"
    PackageMechanism: "OrderService coordinates checkout, cancellation, and history by invoking ProductCatalog for inventory, PricingPolicy for quotes, PaymentGateway for authorization/refunds, OrderRepository for persistence, and NotificationService for receipts and alerts. Domain models encapsulate validation and state transitions. __init__.py defines the package-level surface via re-exports. cli.py wires demo components and executes a sample flow."
    DependencyDirection: "No incoming package edges observed. Internal flow: CLI -> OrderService; OrderService -> {catalog, pricing, payments, repository, notifications}; these depend on domain models. Outgoing edges target Python standard library utilities (dataclasses, datetime, typing, uuid)."
    RepositoryRole: "Demo commerce operations subsystem offering domain models, service orchestration, pricing, payments, catalog, repository, and notifications with a CLI example."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> package_name </REF>: text "commerce_ops"
    <REF> package_path </REF>: text "commerce_ops_demo.commerce_ops"
    <REF> source_directory </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops"

    <!-- Purpose and architecture -->
    <REF> purpose </REF>: text "Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo."
    <REF> role </REF>: text "subsystem; checkout and order management orchestration with domain models and in-memory adapters"
    <REF> repository_role </REF>: text "Demo commerce operations subsystem offering domain models, service orchestration, pricing, payments, catalog, repository, and notifications with a CLI example."

    <!-- Public surface -->
    <REF> public_api </REF>: List [text] ["CartItem", "Customer", "Order", "Product", "OrderService"]
    <REF> entrypoints </REF>: List [text] ["cli.main", "OrderService", "OrderService.checkout", "OrderService.cancel_order", "OrderService.customer_history"]

    <!-- Internal structure -->
    <REF> files </REF>: List [text] ["__init__.py: Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules.", "catalog.py: Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings.", "cli.py: Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary.", "models.py: Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers.", "notifications.py: Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts.", "payments.py: Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures.", "pricing.py: Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals.", "repository.py: Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model.", "services.py: Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications."]
    <REF> subpackages </REF>: List [text] []
    <REF> subsystem_groups </REF>: List [text] ["Public surface: __init__.py re-exports CartItem, Customer, Order, Product, OrderService", "Application service: services.py OrderService orchestrates checkout, cancellation, and history", "Domain models: models.py core entities and validation (Product, Customer, Order, CartItem)", "Catalog and SKU utilities: catalog.py product index, reservation/release, normalize_sku", "Pricing policy and quotes: pricing.py PricingPolicy and PriceQuote", "Payments gateway and types: payments.py PaymentGateway, PaymentReceipt, PaymentError", "Order repository (in-memory): repository.py OrderRepository", "Notifications and currency formatting: notifications.py NotificationService, format_currency", "CLI demo and wiring: cli.py build_demo_service, parse_cart, run_checkout_demo, main"]
    <REF> package_mechanism </REF>: text "OrderService coordinates checkout, cancellation, and history by invoking ProductCatalog for inventory, PricingPolicy for quotes, PaymentGateway for authorization/refunds, OrderRepository for persistence, and NotificationService for receipts and alerts. Domain models encapsulate validation and state transitions. __init__.py defines the package-level surface via re-exports. cli.py wires demo components and executes a sample flow."

    <!-- Dependencies -->
    <REF> dependencies </REF>: List [text] ["Python stdlib: dataclasses", "Python stdlib: datetime", "Python stdlib: typing", "Python stdlib: uuid"]
    <REF> dependency_direction </REF>: text "No incoming package edges observed. Internal flow: CLI -> OrderService; OrderService -> {catalog, pricing, payments, repository, notifications}; these depend on domain models. Outgoing edges target Python standard library utilities (dataclasses, datetime, typing, uuid)."

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["Customer instances for checkout and history", "Cart items (List[CartItem]) for checkout", "Raw cart item strings 'sku:qty' via CLI parse_cart", "Product list for ProductCatalog construction", "Coupon code for PricingPolicy.quote", "PricingPolicy configuration: tax_rate_bps and coupons mapping", "Order identifiers for repository operations and cancellation"]
    <REF> outputs </REF>: List [text] ["Persisted and updated Order entities via OrderRepository", "PaymentReceipt from PaymentGateway.authorize", "PriceQuote from PricingPolicy.quote", "Composed receipt and low-stock alert messages recorded by NotificationService", "Reserved/released inventory state in Product entities", "CLI demo: printed checkout summary"]
    <REF> key_workflows </REF>: List [text] ["Checkout: reserve items in ProductCatalog, compute quote via PricingPolicy.quote, authorize payment via PaymentGateway.authorize, mark order paid and persist via OrderRepository.save, send receipt and possible low-stock alerts via NotificationService; release reserved items on failure.", "Cancel order: retrieve order from OrderRepository.get, release reserved items via ProductCatalog.release_items, mark order cancelled, then save.", "Customer history: list orders for a customer via OrderRepository.list_by_customer (used by OrderService.customer_history).", "CLI demo: build_demo_service to assemble ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, NotificationService, and OrderService; parse raw items and run a sample checkout and summary print."]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Inventory reservation and release via Product.reserve and Product.release", "Customer balance debit/credit via Customer.debit and Customer.credit", "In-memory order persistence mutations in OrderRepository", "Recording sent messages in NotificationService.sent_messages", "PaymentGateway counters for authorized and refunded totals", "Order state transitions and event log appends", "CLI stdout printing"]
    <REF> errors </REF>: List [text] ["ValueError from domain validations: Product.reserve/release, Customer.debit/credit, Order.mark_paid/mark_cancelled, CartItem.validate", "PaymentError for invalid amounts or wrapped Customer.debit/credit failures in PaymentGateway operations", "KeyError on missing entries in ProductCatalog.get and OrderRepository.get", "ValueError and AttributeError from PricingPolicy initialization and quote helpers (coupon normalization, subtotal, tax calculation)", "Exceptions from NotificationService formatting and attribute access when customer/order/product data is missing", "CLI parse_cart errors converting qty or splitting 'sku:qty' strings; propagation of constructor errors during demo wiring", "Propagation of exceptions across OrderService orchestration; compensating releases on checkout failure"]
    <REF> architectural_assumptions </REF>: List [text] ["In-memory adapters (catalog, repository, notifications) with no external datastore", "Synchronous orchestration within a single process", "Package-level public surface is defined by __init__.py re-exports", "OrderService expects collaborators implementing the methods used in checkout, cancellation, and history", "Currency handled in integer cents; coupons normalized to uppercase", "SKU normalization is uppercase after trimming", "No external I/O beyond stdout in CLI; no network or persistence integrations in evidence"]

    <!-- Traceability -->
    <REF> file_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/__init__.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/cli.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/__file__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/__file__.spl</SPL>"]
    <REF> subpackage_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines package-level reverse-engineering information.
     It should let a developer understand what subsystem this package represents, what it exposes, how its files and subpackages cooperate, and how it fits into the repository.
     Do NOT expand file internals.
     Do NOT expand class or method details.
     Use file_refs and subpackage_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    PackageLevelOnly: "Describe the package as a subsystem; do not expand individual files, classes, or methods" LOG "package_over_expansion"
    BoundaryAccuracy: "Distinguish what the package owns from what it delegates to sibling, child, parent, or external packages" LOG "package_boundary_error"
    DependencyDirection: "Preserve intended dependency direction and architectural layer" LOG "package_dependency_error"
    WorkflowSummary: "Describe workflows only at package level without expanding implementation steps" LOG "package_workflow_over_detail"
    Traceability: "Refer to file-level and subpackage-level SPL artifacts by reference instead of inlining them" LOG "subsystem_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `package:commerce_ops_demo.commerce_ops`
- Entity kind: `package`
- Package: `commerce_ops_demo.commerce_ops`

## Wiki Summary

# commerce_ops_demo.commerce_ops

Provide a self-contained commerce operations subsystem for checkout, order management, and customer interactions, exposing a package-level surface for core domain models and an OrderService orchestrator with a CLI demo.

## Architecture Role
subsystem; checkout and order management orchestration with domain models and in-memory adapters

## Public API
- CartItem
- Customer
- Order
- Product
- OrderService

## Child Files
- __init__.py: Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules.
- catalog.py: Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings.
- cli.py: Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary.
- models.py: Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers.
- notifications.py: Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts.
- payments.py: Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures.
- pricing.py: Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals.
- repository.py: Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model.
- services.py: Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications.

## Child Packages
- evidence: missing; confidence: not_available; source: static_analysis

## Dependency Direction
No incoming package edges observed. Internal flow: CLI -> OrderService; OrderService -> {catalog, pricing, payments, repository, notifications}; these depend on domain models. Outgoing edges target Python standard library utilities (dataclasses, datetime, typing, uuid).

## Key Workflows
- Checkout: reserve items in ProductCatalog, compute quote via PricingPolicy.quote, authorize payment via PaymentGateway.authorize, mark order paid and persist via OrderRepository.save, send receipt and possible low-stock alerts via NotificationService; release reserved items on failure.
- Cancel order: retrieve order from OrderRepository.get, release reserved items via ProductCatalog.release_items, mark order cancelled, then save.
- Customer history: list orders for a customer via OrderRepository.list_by_customer (used by OrderService.customer_history).
- CLI demo: build_demo_service to assemble ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, NotificationService, and OrderService; parse raw items and run a sample checkout and summary print.

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/__init__.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/cli.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/__file__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/__file__.spl</SPL>

### Outgoing Links

- `contains_file` -> `file:commerce_ops/__init__.py`
- `contains_file` -> `file:commerce_ops/catalog.py`
- `contains_file` -> `file:commerce_ops/cli.py`
- `contains_file` -> `file:commerce_ops/models.py`
- `contains_file` -> `file:commerce_ops/notifications.py`
- `contains_file` -> `file:commerce_ops/payments.py`
- `contains_file` -> `file:commerce_ops/pricing.py`
- `contains_file` -> `file:commerce_ops/repository.py`
- `contains_file` -> `file:commerce_ops/services.py`

### Referenced By

- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.cli.main`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `owned_by_package` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `contains_package` <- `package:commerce_ops_demo`
- `topic_mentions` <- `topic:external-integration`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/__package__.spl`

### Symbols

- `evidence: missing; confidence: not_available; source: static_analysis`

### Graph References

- `package_dependency:commerce_ops_demo.commerce_ops`

---

<a id="file-commerce-ops-init-py"></a>

## commerce_ops_demo.commerce_ops

- Page ID: `file:commerce_ops/__init__.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/__init__.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/__init__.py`
- Tags: `file`, `python`, `re-export module`

### Summary

Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" __init__.py]

[DEFINE_PERSONA:]
    ROLE: "re-export module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules."
    PublicSurface: "CartItem; Customer; Order; OrderService; Product"
    InternalOrganization: "['Provides two re-export blocks: one importing domain model symbols from commerce_ops.models and one importing OrderService from commerce_ops.services. No additional classes, functions, or module state are defined.']"
    ModuleMechanism: "On import, binds CartItem, Customer, Order, Product, and OrderService into the package namespace by importing them from their submodules, enabling consumers to import these names directly from commerce_ops."
    DependencyBoundary: "external dependency commerce_ops.models; external dependency commerce_ops.services"
    ErrorBoundary: "evidence: missing; confidence: not_available; source: static_analysis"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "__init__.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\__init__.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules."
    <REF> role </REF>: text "re-export module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["CartItem", "Customer", "Order", "OrderService", "Product"]
    <REF> entrypoints </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["Re-exports: CartItem, Customer, Order, Product from commerce_ops.models", "Re-exports: OrderService from commerce_ops.services"]
    <REF> internal_structure </REF>: text "['Provides two re-export blocks: one importing domain model symbols from commerce_ops.models and one importing OrderService from commerce_ops.services. No additional classes, functions, or module state are defined.']"
    <REF> module_mechanism </REF>: text "On import, binds CartItem, Customer, Order, Product, and OrderService into the package namespace by importing them from their submodules, enabling consumers to import these names directly from commerce_ops."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency commerce_ops.models", "external dependency commerce_ops.services"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] ["__all__"]

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> outputs </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> key_paths </REF>: List [text] ["Importing commerce_ops initializes the package namespace by re-exporting CartItem, Customer, Order, Product, and OrderService from submodules."]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> errors </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> initialization_order </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] []
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/__init__.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/__init__.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops

Define the package-level public surface for commerce_ops by re-exporting core domain models and the order service from submodules.

## Exports
- CartItem
- Customer
- Order
- OrderService
- Product

## Components
- Re-exports: CartItem, Customer, Order, Product from commerce_ops.models
- Re-exports: OrderService from commerce_ops.services

## Internal Structure
- Provides two re-export blocks: one importing domain model symbols from commerce_ops.models and one importing OrderService from commerce_ops.services. No additional classes, functions, or module state are defined.

## Imports
- external dependency commerce_ops.models
- external dependency commerce_ops.services

## Source Evidence
- evidence: missing; confidence: not_available; source: static_analysis

### Referenced By

- `contains_file` <- `package:commerce_ops_demo.commerce_ops`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/__init__.py/__file__.spl`

### Symbols

- `evidence: missing; confidence: not_available; source: static_analysis`

### Graph References

- `file_dependency:commerce_ops/__init__.py`

---

<a id="file-commerce-ops-catalog-py"></a>

## commerce_ops_demo.commerce_ops.catalog

- Page ID: `file:commerce_ops/catalog.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/catalog.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `file`, `python`, `repository, coordinator`

### Summary

Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" catalog.py]

[DEFINE_PERSONA:]
    ROLE: "repository, coordinator"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings."
    PublicSurface: "ProductCatalog; normalize_sku"
    InternalOrganization: "['The module centers on ProductCatalog, which builds and owns a mapping from normalized SKU to Product. Catalog methods use normalize_sku for consistent lookups, expose listing of available products, and coordinate multi-item reservation and release by invoking Product.reserve and Product.release. The normalize_sku function provides the SKU normalization used by ProductCatalog.']"
    ModuleMechanism: "At import and construction time, ProductCatalog normalizes provided Product SKUs to populate an internal map. Callers construct ProductCatalog and invoke reserve_items or release_items to mutate inventory via Product methods, with compensating releases on reservation errors. normalize_sku enforces SKU input quality by trimming and uppercasing values and raising ValueError when empty."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.models; external dependency typing"
    ErrorBoundary: "__init__: exceptions propagated from normalize_sku, unhashable keys, missing product.sku attribute, or non-iterable products argument; get: KeyError when normalized SKU not present; reserve_items: any exception during item.validate, get, or Product.reserve triggers compensating releases via Product.release and then re-raises; release_items: exceptions propagated from get or Product.release; AttributeError when items lack sku or qty or the retrieved object lacks release; TypeError when items is not iterable; normalize_sku: AttributeError: object has no attribute 'strip'; normalize_sku: AttributeError: object has no attribute 'upper'; normalize_sku: The stripped value does not support upper(); normalize_sku: ValueError: sku is required; normalize_sku: invalid when not value or not value.strip(); normalize_sku: not value or not value.strip(); normalize_sku: raise ValueError('sku is required'); normalize_sku: value is truthy and does not support strip()"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "catalog.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.catalog"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\catalog.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings."
    <REF> role </REF>: text "repository, coordinator"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["ProductCatalog", "normalize_sku"]
    <REF> entrypoints </REF>: List [text] ["ProductCatalog", "ProductCatalog.reserve_items", "ProductCatalog.release_items"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["ProductCatalog: in-memory catalog repository and coordinator for Product retrieval, availability listing, and reservation/release orchestration with compensation on failure.", "normalize_sku: validation/normalization helper that trims and uppercases SKU strings."]
    <REF> internal_structure </REF>: text "['The module centers on ProductCatalog, which builds and owns a mapping from normalized SKU to Product. Catalog methods use normalize_sku for consistent lookups, expose listing of available products, and coordinate multi-item reservation and release by invoking Product.reserve and Product.release. The normalize_sku function provides the SKU normalization used by ProductCatalog.']"
    <REF> module_mechanism </REF>: text "At import and construction time, ProductCatalog normalizes provided Product SKUs to populate an internal map. Callers construct ProductCatalog and invoke reserve_items or release_items to mutate inventory via Product methods, with compensating releases on reservation errors. normalize_sku enforces SKU input quality by trimming and uppercasing values and raising ValueError when empty."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.models", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["products: iterable of Product for ProductCatalog construction", "items: iterable of CartItem for ProductCatalog.reserve_items", "items: iterable of CartItem for ProductCatalog.release_items", "value (string): SKU input to normalize for normalize_sku"]
    <REF> outputs </REF>: List [text] ["Product from ProductCatalog.get", "List[Product] with positive stock, optionally filtered by tag and sorted by SKU from ProductCatalog.list_available", "List[Product] successfully reserved from ProductCatalog.reserve_items", "None from ProductCatalog.release_items", "normalized_sku (string) from normalize_sku", "Inventory/reservation state mutations on Product via Product.reserve/Product.release"]
    <REF> key_paths </REF>: List [text] ["Construction builds a normalized-SKU map of Product instances using normalize_sku", "Lookup path: ProductCatalog.get normalizes SKU then retrieves Product or raises KeyError", "Availability path: ProductCatalog.list_available filters positive stock (optional tag) and sorts by SKU", "Reservation path: ProductCatalog.reserve_items validates items, retrieves Products, reserves quantities, and compensates by releasing prior reservations on error", "Release path: ProductCatalog.release_items retrieves Products and releases specified quantities"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates internal product index during ProductCatalog construction", "Mutates Product inventory/reservations via Product.reserve in reserve_items", "Mutates Product inventory/reservations via Product.release in release_items"]
    <REF> errors </REF>: List [text] ["__init__: exceptions propagated from normalize_sku, unhashable keys, missing product.sku attribute, or non-iterable products argument", "get: KeyError when normalized SKU not present", "reserve_items: any exception during item.validate, get, or Product.reserve triggers compensating releases via Product.release and then re-raises", "release_items: exceptions propagated from get or Product.release; AttributeError when items lack sku or qty or the retrieved object lacks release; TypeError when items is not iterable", "normalize_sku: AttributeError: object has no attribute 'strip'", "normalize_sku: AttributeError: object has no attribute 'upper'", "normalize_sku: The stripped value does not support upper()", "normalize_sku: ValueError: sku is required", "normalize_sku: invalid when not value or not value.strip()", "normalize_sku: not value or not value.strip()", "normalize_sku: raise ValueError('sku is required')", "normalize_sku: value is truthy and does not support strip()"]
    <REF> initialization_order </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/normalize_sku.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/catalog.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog

Provide a product catalog module that maintains a normalized-SKU index for Product lookups and exposes catalog operations for listing available products and coordinating reservation/release of quantities. Also exposes a utility to normalize SKU strings.

## Exports
- ProductCatalog
- normalize_sku

## Components
- ProductCatalog: in-memory catalog repository and coordinator for Product retrieval, availability listing, and reservation/release orchestration with compensation on failure.
- normalize_sku: validation/normalization helper that trims and uppercases SKU strings.

## Internal Structure
- The module centers on ProductCatalog, which builds and owns a mapping from normalized SKU to Product. Catalog methods use normalize_sku for consistent lookups, expose listing of available products, and coordinate multi-item reservation and release by invoking Product.reserve and Product.release. The normalize_sku function provides the SKU normalization used by ProductCatalog.

## Imports
- external dependency __future__
- external dependency commerce_ops.models
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/normalize_sku.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.catalog.normalize_sku`

### Graph References

- `file_dependency:commerce_ops/catalog.py`

---

<a id="file-commerce-ops-cli-py"></a>

## commerce_ops_demo.commerce_ops.cli

- Page ID: `file:commerce_ops/cli.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/cli.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `entrypoint (CLI demo utility)`, `file`, `python`

### Summary

Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" cli.py]

[DEFINE_PERSONA:]
    ROLE: "entrypoint (CLI demo utility)"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary."
    PublicSurface: "build_demo_service; main; parse_cart; run_checkout_demo"
    InternalOrganization: "['main calls run_checkout_demo; run_checkout_demo builds the service via build_demo_service and parses items via parse_cart, then calls OrderService.checkout and OrderService.customer_history, formats a summary, and returns it; main prints the returned value.']"
    ModuleMechanism: "When invoked via main, the module composes sample data and in-memory dependencies, executes a checkout workflow through OrderService, and surfaces the result via stdout. The exported helpers (parse_cart, build_demo_service, run_checkout_demo) allow programmatic use of the same flow."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.catalog; external dependency commerce_ops.models; external dependency commerce_ops.notifications; external dependency commerce_ops.payments; external dependency commerce_ops.pricing; external dependency commerce_ops.repository; external dependency commerce_ops.services; external dependency typing"
    ErrorBoundary: "Exception: Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> propagates.; The constructor for <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> raises during instantiation.; ValueError: Invalid literal for int() with base 10.; ValueError: Not enough values to unpack (expected 2).; qty_text cannot be converted to an integer via int(qty_text).; raw is not a string-like object and does not support split(':', 1).; raw.split(':', 1) does not produce exactly two parts for unpacking.; Exception: Underlying constructor exception is not handled and propagates to the caller.; If any constructor call (<SPL>commerce_ops_demo.commerce_ops.models.Product</SPL>, <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog</SPL>, <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy</SPL>, <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway</SPL>, <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository</SPL>, <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService</SPL>, or <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL>) raises an error; AttributeError: order.order_id or order.status not available.; Exception: Checkout operation error.; Exception: Customer history retrieval error.; Exception: Invalid cart items.; Exception: Service initialization error.; If <SPL>commerce_ops_demo.commerce_ops.cli.build_demo_service</SPL> fails to create the service instance.; If <SPL>commerce_ops_demo.commerce_ops.cli.parse_cart</SPL>(raw_items) raises due to invalid or malformed input.; If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.checkout</SPL>(...) fails due to validation, inventory, or coupon issues.; If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.customer_history</SPL>(customer.customer_id) fails or customer_id is invalid.; If order lacks order_id or status attributes when formatting the summary string."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "cli.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.cli"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\cli.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary."
    <REF> role </REF>: text "entrypoint (CLI demo utility)"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["build_demo_service", "main", "parse_cart", "run_checkout_demo"]
    <REF> entrypoints </REF>: List [text] ["main"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["build_demo_service: construct a demo OrderService from ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, and NotificationService", "parse_cart: convert raw 'sku:qty' strings into a List[CartItem]", "run_checkout_demo: orchestrate customer creation, parse cart, perform checkout, fetch history, and format a summary string", "main: invoke run_checkout_demo with sample items and 'SAVE10', then print the result"]
    <REF> internal_structure </REF>: text "['main calls run_checkout_demo; run_checkout_demo builds the service via build_demo_service and parses items via parse_cart, then calls OrderService.checkout and OrderService.customer_history, formats a summary, and returns it; main prints the returned value.']"
    <REF> module_mechanism </REF>: text "When invoked via main, the module composes sample data and in-memory dependencies, executes a checkout workflow through OrderService, and surfaces the result via stdout. The exported helpers (parse_cart, build_demo_service, run_checkout_demo) allow programmatic use of the same flow."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.catalog", "external dependency commerce_ops.models", "external dependency commerce_ops.notifications", "external dependency commerce_ops.payments", "external dependency commerce_ops.pricing", "external dependency commerce_ops.repository", "external dependency commerce_ops.services", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["parse_cart.raw_items (List[str])", "run_checkout_demo.raw_items (List[str])", "run_checkout_demo.coupon (str, optional)"]
    <REF> outputs </REF>: List [text] ["parse_cart -> List[CartItem]", "build_demo_service -> OrderService", "run_checkout_demo -> formatted summary string 'created={order_id}; status={status}; history_count={count}'", "main -> prints the checkout result to stdout"]
    <REF> key_paths </REF>: List [text] ["main -> run_checkout_demo", "run_checkout_demo -> build_demo_service", "run_checkout_demo -> parse_cart", "run_checkout_demo -> OrderService.checkout(...)", "run_checkout_demo -> OrderService.customer_history(...)", "run_checkout_demo -> format 'created={order_id}; status={status}; history_count={count}'", "main -> print(result)"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["stdout printing in main"]
    <REF> errors </REF>: List [text] ["Exception: Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> propagates.", "The constructor for <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> raises during instantiation.", "ValueError: Invalid literal for int() with base 10.", "ValueError: Not enough values to unpack (expected 2).", "qty_text cannot be converted to an integer via int(qty_text).", "raw is not a string-like object and does not support split(':', 1).", "raw.split(':', 1) does not produce exactly two parts for unpacking.", "Exception: Underlying constructor exception is not handled and propagates to the caller.", "If any constructor call (<SPL>commerce_ops_demo.commerce_ops.models.Product</SPL>, <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog</SPL>, <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy</SPL>, <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway</SPL>, <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository</SPL>, <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService</SPL>, or <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL>) raises an error", "AttributeError: order.order_id or order.status not available.", "Exception: Checkout operation error.", "Exception: Customer history retrieval error.", "Exception: Invalid cart items.", "Exception: Service initialization error.", "If <SPL>commerce_ops_demo.commerce_ops.cli.build_demo_service</SPL> fails to create the service instance.", "If <SPL>commerce_ops_demo.commerce_ops.cli.parse_cart</SPL>(raw_items) raises due to invalid or malformed input.", "If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.checkout</SPL>(...) fails due to validation, inventory, or coupon issues.", "If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.customer_history</SPL>(customer.customer_id) fails or customer_id is invalid.", "If order lacks order_id or status attributes when formatting the summary string."]
    <REF> initialization_order </REF>: List [text] ["main() -> run_checkout_demo(raw_items, coupon='SAVE10' in this demo)", "run_checkout_demo: build_demo_service() to construct OrderService and dependencies", "run_checkout_demo: parse_cart(raw_items)", "run_checkout_demo: OrderService.checkout(customer, items, coupon)", "run_checkout_demo: OrderService.customer_history(customer.customer_id)", "run_checkout_demo: format summary string and return", "main: print(result)"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] []
    <REF> function_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/cli.py/parse_cart.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/cli.py/build_demo_service.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/cli.py/run_checkout_demo.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/cli.py/main.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/cli.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.cli

Provide a small CLI/demo module that constructs a demo OrderService, parses 'sku:qty' cart items, performs a sample checkout, and prints a summary.

## Exports
- build_demo_service
- main
- parse_cart
- run_checkout_demo

## Components
- build_demo_service: construct a demo OrderService from ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, and NotificationService
- parse_cart: convert raw 'sku:qty' strings into a List[CartItem]
- run_checkout_demo: orchestrate customer creation, parse cart, perform checkout, fetch history, and format a summary string
- main: invoke run_checkout_demo with sample items and 'SAVE10', then print the result

## Internal Structure
- main calls run_checkout_demo; run_checkout_demo builds the service via build_demo_service and parses items via parse_cart, then calls OrderService.checkout and OrderService.customer_history, formats a summary, and returns it; main prints the returned value.

## Imports
- external dependency __future__
- external dependency commerce_ops.catalog
- external dependency commerce_ops.models
- external dependency commerce_ops.notifications
- external dependency commerce_ops.payments
- external dependency commerce_ops.pricing
- external dependency commerce_ops.repository
- external dependency commerce_ops.services
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/cli.py/parse_cart.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/cli.py/build_demo_service.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/cli.py/run_checkout_demo.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/cli.py/main.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.cli.main`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.cli.main`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/cli.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.parse_cart`
- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `commerce_ops_demo.commerce_ops.cli.main`

### Graph References

- `file_dependency:commerce_ops/cli.py`

---

<a id="file-commerce-ops-models-py"></a>

## commerce_ops_demo.commerce_ops.models

- Page ID: `file:commerce_ops/models.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/models.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `file`, `model module`, `python`

### Summary

Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" models.py]

[DEFINE_PERSONA:]
    ROLE: "model module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers."
    PublicSurface: "CartItem; Customer; Order; Product"
    InternalOrganization: "['The module groups four dataclass-based domain types. Each class encapsulates its own state and validation. Internal collaboration occurs within classes only (e.g., Customer.debit calls Customer.can_spend; Order status methods call Order.add_event). There are no cross-class calls within this file. Methods mutate instance fields and may raise ValueError; Order uses datetime.now(timezone.utc) for timestamps.']"
    ModuleMechanism: "On import, it defines dataclass-based models without side effects. At runtime, consumers construct these models and invoke their public methods. Methods validate inputs; on success they mutate in-memory state and, for Order, append timestamped events; on invalid inputs they raise ValueError. The module’s public surface is the set of exported classes."
    DependencyBoundary: "external dependency __future__; external dependency dataclasses; external dependency datetime; external dependency typing"
    ErrorBoundary: "ValueError: qty must be positive (Product.reserve, Product.release); ValueError: not enough stock for {self.sku} (Product.reserve); ValueError: customer has insufficient balance (Customer.debit); ValueError: amount must be positive (Customer.credit); TypeError: invalid amount comparisons during validation in Customer.credit; ValueError: sku is required (CartItem.validate); ValueError: qty must be positive (CartItem.validate); ValueError: only created orders can be marked paid (Order.mark_paid); ValueError: paid orders cannot be cancelled here (Order.mark_cancelled); AttributeError: events does not support append (Order.add_event); NameError: datetime or timezone is not defined (Order.add_event)"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "models.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.models"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\models.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers."
    <REF> role </REF>: text "model module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["CartItem", "Customer", "Order", "Product"]
    <REF> entrypoints </REF>: List [text] ["Product.reserve", "Product.release", "Customer.debit", "Customer.credit", "Customer.can_spend", "Order.mark_paid", "Order.mark_cancelled", "Order.add_event", "CartItem.validate"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["Product: entity; stock reservation and release with validation", "Customer: entity; balance management with debit/credit and spend checks", "Order: entity; status transitions (paid/cancelled) and timestamped event log", "CartItem: value object; SKU and quantity validation"]
    <REF> internal_structure </REF>: text "['The module groups four dataclass-based domain types. Each class encapsulates its own state and validation. Internal collaboration occurs within classes only (e.g., Customer.debit calls Customer.can_spend; Order status methods call Order.add_event). There are no cross-class calls within this file. Methods mutate instance fields and may raise ValueError; Order uses datetime.now(timezone.utc) for timestamps.']"
    <REF> module_mechanism </REF>: text "On import, it defines dataclass-based models without side effects. At runtime, consumers construct these models and invoke their public methods. Methods validate inputs; on success they mutate in-memory state and, for Order, append timestamped events; on invalid inputs they raise ValueError. The module’s public surface is the set of exported classes."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency dataclasses", "external dependency datetime", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["Product.reserve(qty: int)", "Product.release(qty: int)", "Customer.can_spend(amount_cents)", "Customer.debit(amount_cents)", "Customer.credit(amount_cents)", "CartItem(sku, qty)", "CartItem.validate()", "Order.mark_paid(payment_id)", "Order.mark_cancelled(reason)", "Order.add_event(kind, detail)", "Order(order_id, customer_id, items, total_cents, status, events, created_at)"]
    <REF> outputs </REF>: List [text] ["Product: mutates stock; reserve/release return None", "Customer.can_spend: returns bool indicating spend eligibility", "Customer.debit: mutates balance_cents; returns None", "Customer.credit: mutates balance_cents; returns None", "Order: mutates status; appends event entries with timestamps; methods return None", "CartItem.validate: returns None on success; signals failures via exceptions"]
    <REF> key_paths </REF>: List [text] ["Customer.debit -> Customer.can_spend", "Order.mark_paid -> Order.add_event", "Order.mark_cancelled -> Order.add_event", "ProductCatalog.reserve_items -> Product.reserve", "ProductCatalog.release_items -> Product.release", "PaymentGateway.authorize -> Customer.debit", "PaymentGateway.refund -> Customer.credit", "OrderRepository.mark_paid -> Order.mark_paid", "OrderService._build_order -> Order", "OrderService._build_order -> Order.add_event", "OrderService.checkout -> Order.mark_paid", "cli.parse_cart -> CartItem", "cli.build_demo_service -> Product"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates instance state: Product.stock", "Mutates instance state: Customer.balance_cents", "Mutates instance state: Order.status", "Appends to Order.events with timestamped entries", "Raises ValueError on validation failures", "Reads current time via datetime.now(timezone.utc) for event timestamps"]
    <REF> errors </REF>: List [text] ["ValueError: qty must be positive (Product.reserve, Product.release)", "ValueError: not enough stock for {self.sku} (Product.reserve)", "ValueError: customer has insufficient balance (Customer.debit)", "ValueError: amount must be positive (Customer.credit)", "TypeError: invalid amount comparisons during validation in Customer.credit", "ValueError: sku is required (CartItem.validate)", "ValueError: qty must be positive (CartItem.validate)", "ValueError: only created orders can be marked paid (Order.mark_paid)", "ValueError: paid orders cannot be cancelled here (Order.mark_cancelled)", "AttributeError: events does not support append (Order.add_event)", "NameError: datetime or timezone is not defined (Order.add_event)"]
    <REF> initialization_order </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/CartItem/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/models.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models

Provide dataclass-backed domain models for commerce operations: Product inventory control, Customer balance management, Order status transitions with event logging, and CartItem validation. Expose validated, stateful operations used by catalog, payments, repository, services, and CLI layers.

## Exports
- CartItem
- Customer
- Order
- Product

## Components
- Product: entity; stock reservation and release with validation
- Customer: entity; balance management with debit/credit and spend checks
- Order: entity; status transitions (paid/cancelled) and timestamped event log
- CartItem: value object; SKU and quantity validation

## Internal Structure
- The module groups four dataclass-based domain types. Each class encapsulates its own state and validation. Internal collaboration occurs within classes only (e.g., Customer.debit calls Customer.can_spend; Order status methods call Order.add_event). There are no cross-class calls within this file. Methods mutate instance fields and may raise ValueError; Order uses datetime.now(timezone.utc) for timestamps.

## Imports
- external dependency __future__
- external dependency dataclasses
- external dependency datetime
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/CartItem/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/__class__.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.models.Order`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Product`
- `commerce_ops_demo.commerce_ops.models.Customer`
- `commerce_ops_demo.commerce_ops.models.CartItem`
- `commerce_ops_demo.commerce_ops.models.Order`

### Graph References

- `file_dependency:commerce_ops/models.py`

---

<a id="file-commerce-ops-notifications-py"></a>

## commerce_ops_demo.commerce_ops.notifications

- Page ID: `file:commerce_ops/notifications.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/notifications.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `file`, `python`, `service module`

### Summary

Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" notifications.py]

[DEFINE_PERSONA:]
    ROLE: "service module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts."
    PublicSurface: "NotificationService; format_currency"
    InternalOrganization: "['The module exposes a service class and a small utility. NotificationService composes messages for downstream consumers and records them in an instance-level accumulator. When building receipts, it calls the module-level format_currency helper. The file maintains no module-level state and relies on callers (e.g., OrderService, CLI) to invoke the service.']"
    ModuleMechanism: "At import, the module defines a service class and a formatter function. At runtime, external modules construct NotificationService and invoke its methods; send_receipt uses format_currency to build totals and appends composed messages to the instance accumulator. No external I/O is performed by this module."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.models; external dependency typing"
    ErrorBoundary: "<SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.; Exception: Propagated exception from format_currency when formatting the total.; AttributeError: Raised when expected attributes are missing on customer or order.; customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.; self.sent_messages is missing or not list-like, causing append to fail.; A product lacks the 'sku' attribute when formatting the alert string; A product lacks the 'stock' attribute when evaluating the threshold condition; TypeError: Object is not iterable.; TypeError: Unsupported comparison between product.stock and threshold.; products is None or not iterable when entering the loop; ValueError: currency value cannot be negative; cents < 0; cents > 0; raise ValueError('currency value cannot be negative')"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "notifications.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.notifications"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\notifications.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts."
    <REF> role </REF>: text "service module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["NotificationService", "format_currency"]
    <REF> entrypoints </REF>: List [text] ["NotificationService", "format_currency"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["NotificationService: service class that composes receipt and low-stock alert messages and accumulates them in an in-memory sent_messages list; delegates total formatting to format_currency.", "format_currency(cents) -> str: utility function formatting non-negative cent amounts into dollar strings; raises ValueError for negative input."]
    <REF> internal_structure </REF>: text "['The module exposes a service class and a small utility. NotificationService composes messages for downstream consumers and records them in an instance-level accumulator. When building receipts, it calls the module-level format_currency helper. The file maintains no module-level state and relies on callers (e.g., OrderService, CLI) to invoke the service.']"
    <REF> module_mechanism </REF>: text "At import, the module defines a service class and a formatter function. At runtime, external modules construct NotificationService and invoke its methods; send_receipt uses format_currency to build totals and appends composed messages to the instance accumulator. No external I/O is performed by this module."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.models", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["NotificationService.send_receipt(customer, order)", "NotificationService.send_low_stock_alert(products, threshold=2)", "format_currency(cents)"]
    <REF> outputs </REF>: List [text] ["send_receipt: receipt message string recorded in self.sent_messages", "send_low_stock_alert: list of low-stock alert strings recorded in self.sent_messages", "format_currency: formatted currency string like '$12.34'", "NotificationService: maintains an in-memory accumulator of composed messages (sent_messages)"]
    <REF> key_paths </REF>: List [text] ["NotificationService.send_receipt -> format_currency", "commerce_ops_demo.commerce_ops.services.OrderService._notify_customer -> NotificationService.send_receipt", "commerce_ops_demo.commerce_ops.services.OrderService._notify_customer -> NotificationService.send_low_stock_alert", "commerce_ops_demo.commerce_ops.cli.build_demo_service -> NotificationService"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Appends composed messages to NotificationService.sent_messages (in-memory state)", "Maintains an in-memory log of composed messages across calls via NotificationService.sent_messages"]
    <REF> errors </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.", "Exception: Propagated exception from format_currency when formatting the total.", "AttributeError: Raised when expected attributes are missing on customer or order.", "customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.", "self.sent_messages is missing or not list-like, causing append to fail.", "A product lacks the 'sku' attribute when formatting the alert string", "A product lacks the 'stock' attribute when evaluating the threshold condition", "TypeError: Object is not iterable.", "TypeError: Unsupported comparison between product.stock and threshold.", "products is None or not iterable when entering the loop", "ValueError: currency value cannot be negative", "cents < 0", "cents > 0", "raise ValueError('currency value cannot be negative')"]
    <REF> initialization_order </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/format_currency.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/notifications.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications

Provide a notification service that composes and records order-related messages (receipts and low-stock alerts) and a helper to format currency amounts used in receipts.

## Exports
- NotificationService
- format_currency

## Components
- NotificationService: service class that composes receipt and low-stock alert messages and accumulates them in an in-memory sent_messages list; delegates total formatting to format_currency.
- format_currency(cents) -> str: utility function formatting non-negative cent amounts into dollar strings; raises ValueError for negative input.

## Internal Structure
- The module exposes a service class and a small utility. NotificationService composes messages for downstream consumers and records them in an instance-level accumulator. When building receipts, it calls the module-level format_currency helper. The file maintains no module-level state and relies on callers (e.g., OrderService, CLI) to invoke the service.

## Imports
- external dependency __future__
- external dependency commerce_ops.models
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/format_currency.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `contains_symbol` -> `method:commerce_ops_demo.commerce_ops.notifications.format_currency`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `commerce_ops_demo.commerce_ops.notifications.format_currency`

### Graph References

- `file_dependency:commerce_ops/notifications.py`

---

<a id="file-commerce-ops-payments-py"></a>

## commerce_ops_demo.commerce_ops.payments

- Page ID: `file:commerce_ops/payments.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/payments.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `file`, `python`, `service module`

### Summary

Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" payments.py]

[DEFINE_PERSONA:]
    ROLE: "service module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures."
    PublicSurface: "PaymentError; PaymentGateway; PaymentReceipt"
    InternalOrganization: "['The module centers on PaymentGateway, which coordinates payment authorization and refunds by delegating balance changes to Customer, constructing PaymentReceipt records, and signaling failures via PaymentError. PaymentReceipt carries structured result data, and PaymentError defines the boundary for payment-related exceptions.']"
    ModuleMechanism: "Consumers import PaymentGateway, instantiate it with an optional provider label, and call authorize or refund. Internally, the gateway validates amounts, interacts with Customer.debit/credit, uses uuid4/str to tag receipts, returns PaymentReceipt on authorization, and accumulates authorized/refunded totals on the instance. Other modules (e.g., CLI builder and OrderService._charge) rely on these operations."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.models; external dependency dataclasses; external dependency uuid"
    ErrorBoundary: "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'amount must be positive' when amount_cents <= 0 in authorize; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: wraps ValueError from <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> during authorize; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'receipt amount must be positive' when receipt.amount_cents <= 0 in refund"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "payments.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.payments"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\payments.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures."
    <REF> role </REF>: text "service module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["PaymentError", "PaymentGateway", "PaymentReceipt"]
    <REF> entrypoints </REF>: List [text] ["PaymentGateway.__init__", "PaymentGateway.authorize", "PaymentGateway.refund"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["PaymentGateway: service class exposing authorize(customer, amount_cents) -> PaymentReceipt and refund(customer, receipt) -> None; tracks authorized_total_cents and refunded_total_cents", "PaymentReceipt: dataclass value object carrying payment_id, amount_cents, provider", "PaymentError: domain-specific exception type for payment operations"]
    <REF> internal_structure </REF>: text "['The module centers on PaymentGateway, which coordinates payment authorization and refunds by delegating balance changes to Customer, constructing PaymentReceipt records, and signaling failures via PaymentError. PaymentReceipt carries structured result data, and PaymentError defines the boundary for payment-related exceptions.']"
    <REF> module_mechanism </REF>: text "Consumers import PaymentGateway, instantiate it with an optional provider label, and call authorize or refund. Internally, the gateway validates amounts, interacts with Customer.debit/credit, uses uuid4/str to tag receipts, returns PaymentReceipt on authorization, and accumulates authorized/refunded totals on the instance. Other modules (e.g., CLI builder and OrderService._charge) rely on these operations."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.models", "external dependency dataclasses", "external dependency uuid"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["PaymentGateway.__init__(provider='internal-wallet')", "authorize(customer, amount_cents)", "refund(customer, receipt)"]
    <REF> outputs </REF>: List [text] ["authorize: returns <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>", "authorize: increments authorized_total_cents", "authorize: debits customer via <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>", "refund: increments refunded_total_cents", "refund: credits customer via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>", "refund: no return value"]
    <REF> key_paths </REF>: List [text] ["authorize -> validate positive amount -> <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> -> create receipt id via uuid4/str -> return <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>", "refund -> validate positive receipt amount -> <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL> -> update refunded_total_cents -> no return", "Used by: commerce_ops_demo.commerce_ops.services.OrderService._charge -> PaymentGateway.authorize; CLI builder constructs/uses PaymentGateway"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates authorized_total_cents on successful authorization", "Mutates refunded_total_cents on successful refund", "Debits customer balance via <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>", "Credits customer balance via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>"]
    <REF> errors </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'amount must be positive' when amount_cents <= 0 in authorize", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: wraps ValueError from <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> during authorize", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'receipt amount must be positive' when receipt.amount_cents <= 0 in refund"]
    <REF> initialization_order </REF>: List [text] []

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentError/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentReceipt/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/payments.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments

Provide a payment service API (PaymentGateway) with authorization and refund operations, a structured receipt type (PaymentReceipt), and a domain-specific error (PaymentError) for payment failures.

## Exports
- PaymentError
- PaymentGateway
- PaymentReceipt

## Components
- PaymentGateway: service class exposing authorize(customer, amount_cents) -> PaymentReceipt and refund(customer, receipt) -> None; tracks authorized_total_cents and refunded_total_cents
- PaymentReceipt: dataclass value object carrying payment_id, amount_cents, provider
- PaymentError: domain-specific exception type for payment operations

## Internal Structure
- The module centers on PaymentGateway, which coordinates payment authorization and refunds by delegating balance changes to Customer, constructing PaymentReceipt records, and signaling failures via PaymentError. PaymentReceipt carries structured result data, and PaymentError defines the boundary for payment-related exceptions.

## Imports
- external dependency __future__
- external dependency commerce_ops.models
- external dependency dataclasses
- external dependency uuid

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentError/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentReceipt/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__class__.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:authentication`
- `topic_mentions` <- `topic:external-integration`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentError`
- `commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway`

### Graph References

- `file_dependency:commerce_ops/payments.py`

---

<a id="file-commerce-ops-pricing-py"></a>

## commerce_ops_demo.commerce_ops.pricing

- Page ID: `file:commerce_ops/pricing.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/pricing.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `file`, `python`, `service module`

### Summary

Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" pricing.py]

[DEFINE_PERSONA:]
    ROLE: "service module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals."
    PublicSurface: "PriceQuote; PricingPolicy"
    InternalOrganization: "['The module defines a value object (PriceQuote) and a policy service (PricingPolicy). PricingPolicy holds policy configuration (tax_rate_bps and a coupon code map) set on construction, and exposes quote as the primary operation. quote coordinates internal helpers: calculate_subtotal derives a subtotal from items/products, apply_coupon computes and caps a discount from the configured mapping and customer context, calculate_tax computes tax from the taxable amount, and quote assembles the result into a PriceQuote.']"
    ModuleMechanism: "Consumers construct PricingPolicy with a tax rate and coupons mapping; the initializer validates and normalizes configuration. At runtime, clients call quote with customer, cart items, price lookup, and an optional coupon. The module computes subtotal, discount, and tax, then returns a PriceQuote. Other parts of the system (e.g., services) depend on this module as the pricing provider."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.models; external dependency dataclasses; external dependency typing"
    ErrorBoundary: "ValueError: tax rate cannot be negative (initialization).; AttributeError: coupons does not provide an .items() method (initialization).; AttributeError: coupon code lacks .upper() during coupon key normalization (initialization).; ValueError: total must be positive (quote).; ValueError: qty must be positive (calculate_subtotal).; ValueError: price_cents must be positive (calculate_subtotal).; AttributeError: item missing required attributes or sku lacks upper() (calculate_subtotal).; KeyError: SKU not found in price lookup (calculate_subtotal).; TypeError: Non-numeric qty or price causes arithmetic failure (calculate_subtotal).; ValueError: coupon is not supported (apply_coupon).; AttributeError or TypeError: coupon.upper() unavailable or failed (apply_coupon).; ValueError: taxable amount cannot be negative (calculate_tax).; TypeError: Non-numeric taxable_cents or tax_rate_bps (calculate_tax)."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "pricing.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.pricing"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\pricing.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals."
    <REF> role </REF>: text "service module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["PriceQuote", "PricingPolicy"]
    <REF> entrypoints </REF>: List [text] ["PricingPolicy.__init__", "PricingPolicy.quote"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["PriceQuote: dataclass value object holding subtotal_cents, discount_cents, tax_cents, total_cents, coupon", "PricingPolicy: service encapsulating pricing rules and quote orchestration", "PricingPolicy helpers: calculate_subtotal, apply_coupon, calculate_tax"]
    <REF> internal_structure </REF>: text "['The module defines a value object (PriceQuote) and a policy service (PricingPolicy). PricingPolicy holds policy configuration (tax_rate_bps and a coupon code map) set on construction, and exposes quote as the primary operation. quote coordinates internal helpers: calculate_subtotal derives a subtotal from items/products, apply_coupon computes and caps a discount from the configured mapping and customer context, calculate_tax computes tax from the taxable amount, and quote assembles the result into a PriceQuote.']"
    <REF> module_mechanism </REF>: text "Consumers construct PricingPolicy with a tax rate and coupons mapping; the initializer validates and normalizes configuration. At runtime, clients call quote with customer, cart items, price lookup, and an optional coupon. The module computes subtotal, discount, and tax, then returns a PriceQuote. Other parts of the system (e.g., services) depend on this module as the pricing provider."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.models", "external dependency dataclasses", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["tax_rate_bps (int) for PricingPolicy.__init__", "coupons mapping[str,int] for PricingPolicy.__init__", "customer (commerce_ops.models.Customer) for quote/apply_coupon", "items (List[commerce_ops.models.CartItem]) for quote/calculate_subtotal", "products price map (Dict[str, commerce_ops.models.Product]) for quote/calculate_subtotal", "coupon code (str or None) for quote/apply_coupon"]
    <REF> outputs </REF>: List [text] ["PriceQuote from PricingPolicy.quote", "subtotal_cents (int)", "discount_cents (int)", "tax_cents (int)", "total_cents (int) encapsulated in PriceQuote"]
    <REF> key_paths </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService.checkout -> PricingPolicy.quote -> calculate_subtotal -> apply_coupon -> calculate_tax -> PriceQuote", "commerce_ops_demo.commerce_ops.cli.build_demo_service -> PricingPolicy.__init__", "PricingPolicy.quote constructs PriceQuote"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Stores tax_rate_bps on the PricingPolicy instance during __init__", "Normalizes coupon keys to uppercase and stores the mapping during __init__", "Constructs PriceQuote objects when quoting", "No external I/O, network, or persistence effects in evidence"]
    <REF> errors </REF>: List [text] ["ValueError: tax rate cannot be negative (initialization).", "AttributeError: coupons does not provide an .items() method (initialization).", "AttributeError: coupon code lacks .upper() during coupon key normalization (initialization).", "ValueError: total must be positive (quote).", "ValueError: qty must be positive (calculate_subtotal).", "ValueError: price_cents must be positive (calculate_subtotal).", "AttributeError: item missing required attributes or sku lacks upper() (calculate_subtotal).", "KeyError: SKU not found in price lookup (calculate_subtotal).", "TypeError: Non-numeric qty or price causes arithmetic failure (calculate_subtotal).", "ValueError: coupon is not supported (apply_coupon).", "AttributeError or TypeError: coupon.upper() unavailable or failed (apply_coupon).", "ValueError: taxable amount cannot be negative (calculate_tax).", "TypeError: Non-numeric taxable_cents or tax_rate_bps (calculate_tax)."]
    <REF> initialization_order </REF>: List [text] ["Instantiate PricingPolicy (__init__) to validate tax_rate_bps and normalize coupons before calling quote", "Coupons normalization and policy state setup occur during __init__"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PriceQuote/__class__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/pricing.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing

Provide a pricing policy service that computes shopping cart price quotes and a simple PriceQuote data object for returning computed totals.

## Exports
- PriceQuote
- PricingPolicy

## Components
- PriceQuote: dataclass value object holding subtotal_cents, discount_cents, tax_cents, total_cents, coupon
- PricingPolicy: service encapsulating pricing rules and quote orchestration
- PricingPolicy helpers: calculate_subtotal, apply_coupon, calculate_tax

## Internal Structure
- The module defines a value object (PriceQuote) and a policy service (PricingPolicy). PricingPolicy holds policy configuration (tax_rate_bps and a coupon code map) set on construction, and exposes quote as the primary operation. quote coordinates internal helpers: calculate_subtotal derives a subtotal from items/products, apply_coupon computes and caps a discount from the configured mapping and customer context, calculate_tax computes tax from the taxable amount, and quote assembles the result into a PriceQuote.

## Imports
- external dependency __future__
- external dependency commerce_ops.models
- external dependency dataclasses
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PriceQuote/__class__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__class__.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy`

### Graph References

- `file_dependency:commerce_ops/pricing.py`

---

<a id="file-commerce-ops-repository-py"></a>

## commerce_ops_demo.commerce_ops.repository

- Page ID: `file:commerce_ops/repository.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/repository.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `file`, `python`, `repository module; in-memory data access adapter for the Order domain`

### Summary

Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" repository.py]

[DEFINE_PERSONA:]
    ROLE: "repository module; in-memory data access adapter for the Order domain"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model."
    PublicSurface: "OrderRepository"
    InternalOrganization: "['The module exports OrderRepository as its primary component. The repository maintains an internal mapping keyed by order_id initialized at construction. Operational methods manipulate this mapping. mark_paid orchestrates a small workflow: get the order, delegate to Order.mark_paid, then persist with save; internal edges show mark_paid calls get and save.']"
    ModuleMechanism: "Consumers (e.g., CLI demo builder and service layer) instantiate OrderRepository and invoke its public methods. The module depends on typing for annotations and on the Order model for domain behavior during mark_paid. It raises validation and lookup errors across the module boundary and provides an in-memory data source for higher-level services."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.models; external dependency typing"
    ErrorBoundary: "ValueError: order_id is required (save) when order.order_id is falsy; KeyError: order {order_id} not found (get) when the id is absent; AttributeError: Encountered an order without a customer_id attribute while filtering (list_by_customer); AttributeError: The orders collection does not implement values() (list_by_customer); <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid (mark_paid); <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order (mark_paid); <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order (mark_paid); AttributeError: Attempting to call mark_paid on a None order value (mark_paid); Retrieved order is None, causing a failure on mark_paid invocation (mark_paid)"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "repository.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.repository"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\repository.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model."
    <REF> role </REF>: text "repository module; in-memory data access adapter for the Order domain"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["OrderRepository"]
    <REF> entrypoints </REF>: List [text] ["OrderRepository", "OrderRepository.save", "OrderRepository.get", "OrderRepository.list_by_customer", "OrderRepository.mark_paid"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["Class OrderRepository: in-memory repository keyed by order_id; constructor initializes empty orders mapping; provides save(order), get(order_id), list_by_customer(customer_id), and mark_paid(order_id, payment_id) that retrieves, invokes Order.mark_paid, then persists via save"]
    <REF> internal_structure </REF>: text "['The module exports OrderRepository as its primary component. The repository maintains an internal mapping keyed by order_id initialized at construction. Operational methods manipulate this mapping. mark_paid orchestrates a small workflow: get the order, delegate to Order.mark_paid, then persist with save; internal edges show mark_paid calls get and save.']"
    <REF> module_mechanism </REF>: text "Consumers (e.g., CLI demo builder and service layer) instantiate OrderRepository and invoke its public methods. The module depends on typing for annotations and on the Order model for domain behavior during mark_paid. It raises validation and lookup errors across the module boundary and provides an in-memory data source for higher-level services."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.models", "external dependency typing"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["OrderRepository.__init__() constructs an empty repository", "OrderRepository.save(order: Order)", "OrderRepository.get(order_id)", "OrderRepository.list_by_customer(customer_id)", "OrderRepository.mark_paid(order_id, payment_id)"]
    <REF> outputs </REF>: List [text] ["save mutates repository state; no return value", "get returns Order for the given order_id", "list_by_customer returns List[Order] filtered by customer_id", "mark_paid returns the updated Order after persisting"]
    <REF> key_paths </REF>: List [text] ["cli.build_demo_service -> OrderRepository (instantiation)", "services.OrderService.checkout -> OrderRepository.save", "services.OrderService.customer_history -> OrderRepository.list_by_customer", "services.OrderService.cancel_order -> OrderRepository.get -> OrderRepository.save", "OrderRepository.mark_paid -> OrderRepository.get -> Order.mark_paid -> OrderRepository.save"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates internal orders mapping on save and mark_paid", "Overwrites existing entries on duplicate order_id in save", "Persists domain changes during mark_paid by delegating to Order.mark_paid and re-saving", "Raises exceptions on validation and lookup failures"]
    <REF> errors </REF>: List [text] ["ValueError: order_id is required (save) when order.order_id is falsy", "KeyError: order {order_id} not found (get) when the id is absent", "AttributeError: Encountered an order without a customer_id attribute while filtering (list_by_customer)", "AttributeError: The orders collection does not implement values() (list_by_customer)", "<SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid (mark_paid)", "<SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order (mark_paid)", "<SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order (mark_paid)", "AttributeError: Attempting to call mark_paid on a None order value (mark_paid)", "Retrieved order is None, causing a failure on mark_paid invocation (mark_paid)"]
    <REF> initialization_order </REF>: List [text] ["Instantiate OrderRepository before OrderService methods invoke repository operations (constructed via cli.build_demo_service)"]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/repository.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository

Provide an in-memory repository for Order entities used by service-layer operations, supporting save, retrieval, customer-scoped listing, and a mark-paid workflow that coordinates with the Order domain model.

## Exports
- OrderRepository

## Components
- Class OrderRepository: in-memory repository keyed by order_id; constructor initializes empty orders mapping; provides save(order), get(order_id), list_by_customer(customer_id), and mark_paid(order_id, payment_id) that retrieves, invokes Order.mark_paid, then persists via save

## Internal Structure
- The module exports OrderRepository as its primary component. The repository maintains an internal mapping keyed by order_id initialized at construction. Operational methods manipulate this mapping. mark_paid orchestrates a small workflow: get the order, delegate to Order.mark_paid, then persist with save; internal edges show mark_paid calls get and save.

## Imports
- external dependency __future__
- external dependency commerce_ops.models
- external dependency typing

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__class__.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:external-integration`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository`

### Graph References

- `file_dependency:commerce_ops/repository.py`

---

<a id="file-commerce-ops-services-py"></a>

## commerce_ops_demo.commerce_ops.services

- Page ID: `file:commerce_ops/services.py`
- Type: `entity` / `file`
- Qualified name: `commerce_ops/services.py`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `file`, `python`, `service module`

### Summary

Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications.

### SPL Content

```spl
[DEFINE_AGENT: "A source file that defines a module with purpose, exports, internal organization, dependencies, and runtime role" services.py]

[DEFINE_PERSONA:]
    ROLE: "service module"
    LANGUAGE: "python"
    ABSTRACTION_LEVEL: "File-level; describes module responsibility and organization without expanding class or method internals"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, maintain, test, or integrate this file"
    INTEREST: "File purpose, exports, imports, contained components, runtime role, dependencies, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications."
    PublicSurface: "OrderService"
    InternalOrganization: "['A single class-centric module. Consumers instantiate OrderService with required collaborators and invoke its public methods. Public methods delegate to internal helper methods and coordinate calls across catalog, pricing, payments, repository, and notifications. No additional top-level functions or module-level state are defined.']"
    ModuleMechanism: "The module contributes a single orchestration class. At runtime, clients construct OrderService with injected dependencies. checkout uses internal helpers to build an Order (uuid4), reserve or release inventory, obtain a price quote, authorize payment, persist the order, and send notifications. cancel_order retrieves and updates an order, releases inventory, and persists changes. customer_history queries the repository and formats results. Dependency flow is inbound via constructor and outbound to domain and infrastructure collaborators during method calls."
    DependencyBoundary: "external dependency __future__; external dependency commerce_ops.catalog; external dependency commerce_ops.models; external dependency commerce_ops.notifications; external dependency commerce_ops.payments; external dependency commerce_ops.pricing; external dependency commerce_ops.repository; external dependency typing; external dependency uuid"
    ErrorBoundary: "Propagates exceptions from ProductCatalog reserve/release; Propagates exceptions from PricingPolicy.quote; Propagates exceptions from PaymentGateway.authorize; Propagates exceptions from OrderRepository.get/save/list_by_customer; Propagates exceptions from NotificationService sending methods; Attribute errors if injected dependencies are missing or lack required methods; If checkout fails after reservation, items are released and the original error is re-raised; Type errors if iterable inputs (items, orders) are invalid; Order retrieval may return None leading to attribute access errors during cancellation"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> file_name </REF>: text "services.py"
    <REF> module_name </REF>: text "commerce_ops_demo.commerce_ops.services"
    <REF> source_path </REF>: text "C:\Users\杨天宇\资料\逆向工程\工程\Code_SPL\Code_SPL\sample_repos\commerce_ops_demo\commerce_ops\services.py"
    <REF> language </REF>: text "python"

    <!-- Purpose and role -->
    <REF> purpose </REF>: text "Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications."
    <REF> role </REF>: text "service module"

    <!-- Public surface -->
    <REF> exports </REF>: List [text] ["OrderService"]
    <REF> entrypoints </REF>: List [text] ["OrderService", "OrderService.__init__", "OrderService.checkout", "OrderService.cancel_order", "OrderService.customer_history"]

    <!-- Internal organization -->
    <REF> components </REF>: List [text] ["OrderService: service orchestrator for checkout, cancellation, and customer history; collaborates with ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, NotificationService, and Order model.", "OrderService private helpers: _build_order, _charge, _notify_customer (invoked by checkout)."]
    <REF> internal_structure </REF>: text "['A single class-centric module. Consumers instantiate OrderService with required collaborators and invoke its public methods. Public methods delegate to internal helper methods and coordinate calls across catalog, pricing, payments, repository, and notifications. No additional top-level functions or module-level state are defined.']"
    <REF> module_mechanism </REF>: text "The module contributes a single orchestration class. At runtime, clients construct OrderService with injected dependencies. checkout uses internal helpers to build an Order (uuid4), reserve or release inventory, obtain a price quote, authorize payment, persist the order, and send notifications. cancel_order retrieves and updates an order, releases inventory, and persists changes. customer_history queries the repository and formats results. Dependency flow is inbound via constructor and outbound to domain and infrastructure collaborators during method calls."

    <!-- Dependencies and data -->
    <REF> imports </REF>: List [text] ["external dependency __future__", "external dependency commerce_ops.catalog", "external dependency commerce_ops.models", "external dependency commerce_ops.notifications", "external dependency commerce_ops.payments", "external dependency commerce_ops.pricing", "external dependency commerce_ops.repository", "external dependency typing", "external dependency uuid"]
    <REF> internal_imports </REF>: List [text] []
    <REF> globals </REF>: List [text] []

    <!-- Behavior -->
    <REF> inputs </REF>: List [text] ["OrderService.__init__(catalog: ProductCatalog, pricing: PricingPolicy, payments: PaymentGateway, repository: OrderRepository, notifications: NotificationService)", "OrderService.checkout(customer: Customer, items: List[CartItem], coupon: str = '')", "OrderService.cancel_order(order_id, reason)", "OrderService.customer_history(customer_id)"]
    <REF> outputs </REF>: List [text] ["checkout returns Order (paid and persisted)", "cancel_order returns Order (cancelled and persisted)", "customer_history returns List[dict] with order_id, status, total as string"]
    <REF> key_paths </REF>: List [text] ["checkout: reserve items in ProductCatalog -> obtain PriceQuote from PricingPolicy -> authorize via PaymentGateway -> mark Order paid -> persist via OrderRepository -> notify customer and low-stock alerts via NotificationService; release items on failure path.", "cancel_order: retrieve via OrderRepository.get -> mark order cancelled -> release items via ProductCatalog.release_items -> persist via OrderRepository.save.", "customer_history: list orders via OrderRepository.list_by_customer and format string fields.", "order construction: internal _build_order uses uuid4 and Order model, adding initial event."]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.last_receipt during charge", "Reserves and releases inventory in catalog", "Charges payment through external gateway", "Persists orders to repository", "Sends customer receipt notifications", "Triggers low-stock alerts", "Marks order as paid"]
    <REF> errors </REF>: List [text] ["Propagates exceptions from ProductCatalog reserve/release", "Propagates exceptions from PricingPolicy.quote", "Propagates exceptions from PaymentGateway.authorize", "Propagates exceptions from OrderRepository.get/save/list_by_customer", "Propagates exceptions from NotificationService sending methods", "Attribute errors if injected dependencies are missing or lack required methods", "If checkout fails after reservation, items are released and the original error is re-raised", "Type errors if iterable inputs (items, orders) are invalid", "Order retrieval may return None leading to attribute access errors during cancellation"]
    <REF> initialization_order </REF>: List [text] ["Instantiate OrderService with ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, and NotificationService before invoking checkout, cancel_order, or customer_history."]

    <!-- Traceability -->
    <REF> class_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__class__.spl</SPL>"]
    <REF> function_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines file-level reverse-engineering information.
     It should let a developer understand what the file does, what it exposes, how its components cooperate, and where to inspect lower-level details.
     Do NOT expand class internals.
     Do NOT expand method or function COMMAND flows.
     Use class_refs and function_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    FileLevelOnly: "Describe the file as a module; do not expand class internals or function steps" LOG "file_over_expansion"
    ExportBoundary: "Clearly distinguish exported surface from internal components" LOG "file_export_error"
    DependencyAccuracy: "Mention dependencies only when they affect the module responsibility, runtime role, or boundary" LOG "file_dependency_error"
    InitializationAccuracy: "Include initialization order only when it affects runtime behavior" LOG "file_initialization_error"
    Traceability: "Refer to class-level and function-level SPL artifacts by reference instead of inlining them" LOG "component_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `file:commerce_ops/services.py`
- Entity kind: `file`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services

Expose an application-level service that coordinates checkout, order cancellation, and customer order history by orchestrating catalog, pricing, payments, order persistence, and customer notifications.

## Exports
- OrderService

## Components
- OrderService: service orchestrator for checkout, cancellation, and customer history; collaborates with ProductCatalog, PricingPolicy, PaymentGateway, OrderRepository, NotificationService, and Order model.
- OrderService private helpers: _build_order, _charge, _notify_customer (invoked by checkout).

## Internal Structure
- A single class-centric module. Consumers instantiate OrderService with required collaborators and invoke its public methods. Public methods delegate to internal helper methods and coordinate calls across catalog, pricing, payments, repository, and notifications. No additional top-level functions or module-level state are defined.

## Imports
- external dependency __future__
- external dependency commerce_ops.catalog
- external dependency commerce_ops.models
- external dependency commerce_ops.notifications
- external dependency commerce_ops.payments
- external dependency commerce_ops.pricing
- external dependency commerce_ops.repository
- external dependency typing
- external dependency uuid

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__class__.spl</SPL>

### Outgoing Links

- `contains_symbol` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`

### Referenced By

- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `owned_by_file` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `contains_file` <- `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` <- `topic:authentication`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/__file__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService`

### Graph References

- `file_dependency:commerce_ops/services.py`

---

<a id="class-commerce-ops-demo-commerce-ops-catalog-productcatalog"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog

- Page ID: `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `class`, `repository, coordinator`

### Summary

Maintain a normalized-SKU index of Product objects for lookups and expose catalog operations, including listing available items and coordinating reservation/release of quantities for cart items with failure compensation.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" ProductCatalog]

[DEFINE_PERSONA:]
    ROLE: "repository, coordinator"
    DOMAIN: "Commerce operations: product catalog, SKU lookup, and inventory reservation/release"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Maintain a normalized-SKU index of Product objects for lookups and expose catalog operations, including listing available items and coordinating reservation/release of quantities for cart items with failure compensation."
    Responsibility: "Primary: own an in-memory mapping from normalized SKU to Product and provide reliable retrieval by SKU. Secondary: expose available products (filter by tag, sorted) and orchestrate reservation/release across multiple items with compensating release on errors."
    PublicBehavior: "Construction: __init__(products) builds a mapping from normalized SKU to Product.; Lookup: get(sku) -> Product; normalizes SKU and raises KeyError when not found.; Catalog listing: list_available(tag) -> List[Product] with positive stock, optional tag filter, sorted by product.sku ascending.; Reservation: reserve_items(items) -> List[Product]; validates items, retrieves products, reserves quantities, and compensates by releasing prior reservations on error.; Release: release_items(items) -> None; retrieves products and releases the specified quantities."
    InternalMechanism: "On construction, normalize each Product.sku via <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> and index into an internal dictionary. Lookups normalize input SKUs and read from that index, raising a KeyError if the key is absent. Catalog listing iterates current products, filters to positive stock (and tag when provided), and sorts by product.sku. For reservations, iterate items, validate each, fetch the Product with get, and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL>; if any error occurs, iterate previously reserved pairs and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with original quantities, then re-raise. Releases iterate items, fetch each Product, and call <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL>."
    StateModel: "self.products: Dict[str, Product] — normalized SKU index owned by the class (writes in __init__; reads in get and list_available)."
    Collaboration: "commerce_ops_demo.commerce_ops.catalog.normalize_sku; commerce_ops_demo.commerce_ops.models.Product.reserve; commerce_ops_demo.commerce_ops.models.Product.release; external.item.validate; external.sorted"
    ErrorBoundary: "__init__: exceptions propagated from <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>, unhashable keys, missing product.sku attribute, or non-iterable products argument.; get: KeyError when the normalized SKU is not present in self.products.; reserve_items: any exception during item.validate, get, or Product.reserve triggers compensating releases via <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> and then re-raises.; release_items: exceptions propagated from get or Product.release; AttributeError when items lack sku or qty or the retrieved object lacks release; TypeError when items is not iterable."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "ProductCatalog"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.catalog.ProductCatalog"
    <REF> source_file </REF>: text "commerce_ops/catalog.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Maintain a normalized-SKU index of Product objects for lookups and expose catalog operations, including listing available items and coordinating reservation/release of quantities for cart items with failure compensation."
    <REF> responsibility </REF>: text "Primary: own an in-memory mapping from normalized SKU to Product and provide reliable retrieval by SKU. Secondary: expose available products (filter by tag, sorted) and orchestrate reservation/release across multiple items with compensating release on errors."
    <REF> role </REF>: text "repository, coordinator"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["Construction: __init__(products) builds a mapping from normalized SKU to Product.", "Lookup: get(sku) -> Product; normalizes SKU and raises KeyError when not found.", "Catalog listing: list_available(tag) -> List[Product] with positive stock, optional tag filter, sorted by product.sku ascending.", "Reservation: reserve_items(items) -> List[Product]; validates items, retrieves products, reserves quantities, and compensates by releasing prior reservations on error.", "Release: release_items(items) -> None; retrieves products and releases the specified quantities."]
    <REF> entrypoints </REF>: List [text] ["__init__", "reserve_items", "release_items"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "On construction, normalize each Product.sku via <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> and index into an internal dictionary. Lookups normalize input SKUs and read from that index, raising a KeyError if the key is absent. Catalog listing iterates current products, filters to positive stock (and tag when provided), and sorts by product.sku. For reservations, iterate items, validate each, fetch the Product with get, and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL>; if any error occurs, iterate previously reserved pairs and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with original quantities, then re-raise. Releases iterate items, fetch each Product, and call <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL>."
    <REF> internal_structure </REF>: List [text] ["State index: self.products mapping normalized SKU -> Product (written in __init__, read by get and listing).", "Normalization dependency: <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> used in construction and lookup.", "Orchestration methods: reserve_items (validate items, get, reserve, compensate on error) and release_items (get, release).", "Shared helper: get is a high fan-in method used by reserve_items and release_items.", "No private methods or decorators."]
    <REF> lifecycle </REF>: List [text] ["Creation: constructed with an iterable of Product and builds the normalized SKU index.", "Usage: get and list_available read from the index for retrieval and listing.", "Operational: reserve_items and release_items coordinate product state changes via Product.reserve/Product.release.", "Error handling: reservation path performs compensating releases on failure and re-raises the original exception."]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["self.products: Dict[str, Product] — normalized SKU index owned by the class (writes in __init__; reads in get and list_available)."]
    <REF> inputs </REF>: List [text] ["products: Iterable[Product] (constructor).", "sku: str (get).", "items: List[CartItem] with sku and qty (reserve_items).", "items: List[CartItem] with sku and qty (release_items).", "tag: str (optional filter in list_available)."]
    <REF> outputs </REF>: List [text] ["Product (from get).", "List[Product] filtered to positive stock, sorted by SKU (from list_available).", "List[Product] that were successfully reserved (from reserve_items).", "None (from release_items).", "Product inventory/reservation state is mutated via Product.reserve/Product.release."]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["commerce_ops_demo.commerce_ops.catalog.normalize_sku", "commerce_ops_demo.commerce_ops.models.Product.reserve", "commerce_ops_demo.commerce_ops.models.Product.release", "external.item.validate", "external.sorted"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService.checkout", "commerce_ops_demo.commerce_ops.services.OrderService.cancel_order"]
    <REF> key_interactions </REF>: List [text] ["Calls <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> to build and query the SKU index.", "Delegates inventory changes to <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL> and <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL>.", "Exposed to OrderService: checkout uses reserve_items and release_items; cancel_order uses release_items.", "Raises KeyError in get when a normalized SKU is absent."]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.products during construction.", "Mutates Product inventory/reservations via Product.reserve in reserve_items.", "Mutates Product inventory/reservations via Product.release in release_items."]
    <REF> errors </REF>: List [text] ["__init__: exceptions propagated from <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>, unhashable keys, missing product.sku attribute, or non-iterable products argument.", "get: KeyError when the normalized SKU is not present in self.products.", "reserve_items: any exception during item.validate, get, or Product.reserve triggers compensating releases via <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> and then re-raises.", "release_items: exceptions propagated from get or Product.release; AttributeError when items lack sku or qty or the retrieved object lacks release; TypeError when items is not iterable."]
    <REF> invariants </REF>: List [text] ["Catalog keys are normalized via <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>.", "get requires the normalized SKU to exist in the index; otherwise a KeyError is raised.", "reserve_items performs compensating releases for all previously reserved products if any step fails, then re-raises the original error.", "list_available returns only products with positive stock and sorts results by product.sku ascending.", "Cart items provided to reservation/release expose sku and qty and are iterable."]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/get.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/list_available.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/reserve_items.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/release_items.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog

Maintain a normalized-SKU index of Product objects for lookups and expose catalog operations, including listing available items and coordinating reservation/release of quantities for cart items with failure compensation.

## Role and Responsibilities
Primary: own an in-memory mapping from normalized SKU to Product and provide reliable retrieval by SKU. Secondary: expose available products (filter by tag, sorted) and orchestrate reservation/release across multiple items with compensating release on errors.

## Public Surface
- Construction: __init__(products) builds a mapping from normalized SKU to Product.
- Lookup: get(sku) -> Product; normalizes SKU and raises KeyError when not found.
- Catalog listing: list_available(tag) -> List[Product] with positive stock, optional tag filter, sorted by product.sku ascending.
- Reservation: reserve_items(items) -> List[Product]; validates items, retrieves products, reserves quantities, and compensates by releasing prior reservations on error.
- Release: release_items(items) -> None; retrieves products and releases the specified quantities.

## State Model
- self.products: Dict[str, Product] — normalized SKU index owned by the class (writes in __init__; reads in get and list_available).

## Internal Mechanism
On construction, normalize each Product.sku via <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> and index into an internal dictionary. Lookups normalize input SKUs and read from that index, raising a KeyError if the key is absent. Catalog listing iterates current products, filters to positive stock (and tag when provided), and sorts by product.sku. For reservations, iterate items, validate each, fetch the Product with get, and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL>; if any error occurs, iterate previously reserved pairs and invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with original quantities, then re-raise. Releases iterate items, fetch each Product, and call <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL>.

## Related Classes
- {"source_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "target_class_id": "commerce_ops_demo.commerce_ops.models.Product", "relation_type": "uses", "evidence": "product.reserve(item.qty)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "target_class_id": "commerce_ops_demo.commerce_ops.models.Product", "relation_type": "uses", "evidence": "product.release(item.qty)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "target_class_id": "commerce_ops_demo.commerce_ops.models.Product", "relation_type": "uses", "evidence": "product.release(item.qty)", "direction": "this -> target", "confidence": "high"}

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/get.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/list_available.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/reserve_items.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/release_items.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Product`

### Referenced By

- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/catalog.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`

---

<a id="class-commerce-ops-demo-commerce-ops-models-cartitem"></a>

## commerce_ops_demo.commerce_ops.models.CartItem

- Page ID: `class:commerce_ops_demo.commerce_ops.models.CartItem`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.models.CartItem`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `class`, `value object`

### Summary

Represent a single cart line item with SKU and quantity and provide a simple validity check for these attributes.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" CartItem]

[DEFINE_PERSONA:]
    ROLE: "value object"
    DOMAIN: "E-commerce cart and order modeling"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent a single cart line item with SKU and quantity and provide a simple validity check for these attributes."
    Responsibility: "Hold SKU and quantity as domain data and validate that both are present and logically valid."
    PublicBehavior: "Dataclass constructor with fields: sku, qty; validate()"
    InternalMechanism: "A dataclass carrying sku and qty; validation ensures sku is provided and qty is greater than zero, signaling problems by raising ValueError."
    StateModel: "sku: domain data (read by validate); qty: domain data (read by validate)"
    Collaboration: "dataclass (decorator); ValueError (exception used to signal validation failures)"
    ErrorBoundary: "ValueError: sku is required; ValueError: qty must be positive"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "CartItem"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.models.CartItem"
    <REF> source_file </REF>: text "commerce_ops/models.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent a single cart line item with SKU and quantity and provide a simple validity check for these attributes."
    <REF> responsibility </REF>: text "Hold SKU and quantity as domain data and validate that both are present and logically valid."
    <REF> role </REF>: text "value object"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["Dataclass constructor with fields: sku, qty", "validate()"]
    <REF> entrypoints </REF>: List [text] ["Dataclass constructor: CartItem(sku, qty)", "validate()"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "A dataclass carrying sku and qty; validation ensures sku is provided and qty is greater than zero, signaling problems by raising ValueError."
    <REF> internal_structure </REF>: List [text] ["Dataclass structure providing auto-generated initialization for sku and qty", "Single public validator method: validate()"]
    <REF> lifecycle </REF>: List [text] ["Created via dataclass constructor with sku and qty", "Optional: call validate() to assert correctness before further use", "No disposal steps indicated"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["sku: domain data (read by validate)", "qty: domain data (read by validate)"]
    <REF> inputs </REF>: List [text] ["sku (provided at construction)", "qty (provided at construction)"]
    <REF> outputs </REF>: List [text] ["Validation outcome via exceptions; validate() returns None on success"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["dataclass (decorator)", "ValueError (exception used to signal validation failures)"]
    <REF> used_by </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> key_interactions </REF>: List [text] ["Raises ValueError when validation fails"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["No I/O or external state mutation; validation only"]
    <REF> errors </REF>: List [text] ["ValueError: sku is required", "ValueError: qty must be positive"]
    <REF> invariants </REF>: List [text] ["sku must be truthy", "qty must be greater than 0"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/models.py/CartItem/validate.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.models.CartItem`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.CartItem

Represent a single cart line item with SKU and quantity and provide a simple validity check for these attributes.

## Role and Responsibilities
Hold SKU and quantity as domain data and validate that both are present and logically valid.

## Public Surface
- Dataclass constructor with fields: sku, qty
- validate()

## State Model
- sku: domain data (read by validate)
- qty: domain data (read by validate)

## Internal Mechanism
A dataclass carrying sku and qty; validation ensures sku is provided and qty is greater than zero, signaling problems by raising ValueError.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/CartItem/validate.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- `contains_symbol` <- `file:commerce_ops/models.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/CartItem/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.CartItem`
- `commerce_ops_demo.commerce_ops.models.CartItem.validate`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.models.CartItem`

---

<a id="class-commerce-ops-demo-commerce-ops-models-customer"></a>

## commerce_ops_demo.commerce_ops.models.Customer

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Customer`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Customer`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `class`, `entity`

### Summary

Represent a customer account with a cents-based balance, providing validated debit and credit operations and a spend check used by payment flows.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" Customer]

[DEFINE_PERSONA:]
    ROLE: "entity"
    DOMAIN: "Commerce operations / payments"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent a customer account with a cents-based balance, providing validated debit and credit operations and a spend check used by payment flows."
    Responsibility: "Primary: maintain and validate the customer's balance_cents, enabling spend checks and performing debit/credit under rules. Secondary: carry identity and profile attributes such as customer_id, email, and tier."
    PublicBehavior: "dataclass construction: Customer(customer_id, email, balance_cents, tier); can_spend(amount_cents) -> bool; debit(amount_cents) -> None (mutates balance); credit(amount_cents) -> None (mutates balance)"
    InternalMechanism: "Maintains a cents-denominated balance and enforces validation rules: spend checks confirm amount_cents > 0 and sufficient balance; debit invokes the spend check before decrementing; credit requires a positive amount before incrementing. No external I/O is performed."
    StateModel: "customer_id: customer identifier (domain attribute); email: contact attribute (domain attribute); tier: classification attribute (domain attribute); balance_cents: mutable account balance in cents; read by can_spend; decremented by debit; incremented by credit"
    Collaboration: "external.ValueError"
    ErrorBoundary: "ValueError('customer has insufficient balance') from debit when not <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents); ValueError('amount must be positive') from credit when amount_cents <= 0; TypeError from invalid amount comparisons during validation in credit; Exceptions from <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL> propagate (none specified in evidence)"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "Customer"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.models.Customer"
    <REF> source_file </REF>: text "commerce_ops/models.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent a customer account with a cents-based balance, providing validated debit and credit operations and a spend check used by payment flows."
    <REF> responsibility </REF>: text "Primary: maintain and validate the customer's balance_cents, enabling spend checks and performing debit/credit under rules. Secondary: carry identity and profile attributes such as customer_id, email, and tier."
    <REF> role </REF>: text "entity"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["dataclass construction: Customer(customer_id, email, balance_cents, tier)", "can_spend(amount_cents) -> bool", "debit(amount_cents) -> None (mutates balance)", "credit(amount_cents) -> None (mutates balance)"]
    <REF> entrypoints </REF>: List [text] ["debit(amount_cents)", "credit(amount_cents)", "can_spend(amount_cents)"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Maintains a cents-denominated balance and enforces validation rules: spend checks confirm amount_cents > 0 and sufficient balance; debit invokes the spend check before decrementing; credit requires a positive amount before incrementing. No external I/O is performed."
    <REF> internal_structure </REF>: List [text] ["Validation helper: can_spend(amount_cents) reads balance_cents", "Mutation operation: debit(amount_cents) decrements balance_cents after validation", "Mutation operation: credit(amount_cents) increments balance_cents with positive-amount check"]
    <REF> lifecycle </REF>: List [text] ["Construct via dataclass with customer_id, email, balance_cents, tier", "Use debit and credit to mutate monetary state", "No explicit teardown or disposal behavior"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["customer_id: customer identifier (domain attribute)", "email: contact attribute (domain attribute)", "tier: classification attribute (domain attribute)", "balance_cents: mutable account balance in cents; read by can_spend; decremented by debit; incremented by credit"]
    <REF> inputs </REF>: List [text] ["amount_cents (int) to can_spend", "amount_cents (int) to debit", "amount_cents (int) to credit", "constructor inputs: customer_id, email, balance_cents, tier"]
    <REF> outputs </REF>: List [text] ["can_spend returns bool indicating spend eligibility", "debit returns None and reduces balance_cents", "credit returns None and increases balance_cents", "updated balance_cents persisted in instance state"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["external.ValueError"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize", "commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund"]
    <REF> key_interactions </REF>: List [text] ["debit -> <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL> for validation", "commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize -> debit", "commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund -> credit", "debit and credit raise ValueError on invalid operations"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.balance_cents", "Raises ValueError on insufficient balance or non-positive credit", "TypeError may propagate if amount_cents is not comparable to integers"]
    <REF> errors </REF>: List [text] ["ValueError('customer has insufficient balance') from debit when not <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents)", "ValueError('amount must be positive') from credit when amount_cents <= 0", "TypeError from invalid amount comparisons during validation in credit", "Exceptions from <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL> propagate (none specified in evidence)"]
    <REF> invariants </REF>: List [text] ["All debit and credit operations require amount_cents > 0", "Debits only occur when balance_cents >= amount_cents", "balance_cents remains non-negative when using provided operations"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/can_spend.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/debit.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/credit.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Customer`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Customer

Represent a customer account with a cents-based balance, providing validated debit and credit operations and a spend check used by payment flows.

## Role and Responsibilities
Primary: maintain and validate the customer's balance_cents, enabling spend checks and performing debit/credit under rules. Secondary: carry identity and profile attributes such as customer_id, email, and tier.

## Public Surface
- dataclass construction: Customer(customer_id, email, balance_cents, tier)
- can_spend(amount_cents) -> bool
- debit(amount_cents) -> None (mutates balance)
- credit(amount_cents) -> None (mutates balance)

## State Model
- customer_id: customer identifier (domain attribute)
- email: contact attribute (domain attribute)
- tier: classification attribute (domain attribute)
- balance_cents: mutable account balance in cents; read by can_spend; decremented by debit; incremented by credit

## Internal Mechanism
Maintains a cents-denominated balance and enforces validation rules: spend checks confirm amount_cents > 0 and sufficient balance; debit invokes the spend check before decrementing; credit requires a positive amount before incrementing. No external I/O is performed.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/can_spend.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/debit.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Customer/credit.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Customer.credit`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `uses` <- `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `uses` <- `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `contains_symbol` <- `file:commerce_ops/models.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Customer/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Customer`
- `commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `commerce_ops_demo.commerce_ops.models.Customer.debit`
- `commerce_ops_demo.commerce_ops.models.Customer.credit`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.models.Customer`

---

<a id="class-commerce-ops-demo-commerce-ops-models-order"></a>

## commerce_ops_demo.commerce_ops.models.Order

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Order`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Order`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `class`, `entity`

### Summary

Represent an order with core fields, enforce simple status transitions (to paid or cancelled) with validation, and record a timestamped event log for significant changes.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" Order]

[DEFINE_PERSONA:]
    ROLE: "entity"
    DOMAIN: "Commerce operations order domain"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent an order with core fields, enforce simple status transitions (to paid or cancelled) with validation, and record a timestamped event log for significant changes."
    Responsibility: "Primary: maintain order state and guard-valid transitions (pay, cancel). Secondary: append timestamped event entries describing changes."
    PublicBehavior: "mark_paid(payment_id); mark_cancelled(reason); add_event(kind, detail); dataclass-based construction with fields: order_id, customer_id, items, total_cents, status, events, created_at"
    InternalMechanism: "State transition methods read and mutate the status field under guard rules and delegate event logging to add_event; add_event appends an event dict with a UTC ISO timestamp using datetime.now(timezone.utc)."
    StateModel: "order_id: domain data identifier; customer_id: domain data identifier; items: domain data collection; total_cents: domain monetary amount; status: runtime state with guarded transitions; events: event log list mutated by add_event; created_at: creation timestamp"
    Collaboration: "datetime.now(timezone.utc) for UTC ISO timestamps; dataclasses.dataclass for field-based initialization"
    ErrorBoundary: "ValueError: only created orders can be marked paid (when status != 'created'); ValueError: paid orders cannot be cancelled here (when status == 'paid'); AttributeError: events does not support append; NameError: datetime or timezone is not defined for timestamp creation"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "Order"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.models.Order"
    <REF> source_file </REF>: text "commerce_ops/models.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent an order with core fields, enforce simple status transitions (to paid or cancelled) with validation, and record a timestamped event log for significant changes."
    <REF> responsibility </REF>: text "Primary: maintain order state and guard-valid transitions (pay, cancel). Secondary: append timestamped event entries describing changes."
    <REF> role </REF>: text "entity"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["mark_paid(payment_id)", "mark_cancelled(reason)", "add_event(kind, detail)", "dataclass-based construction with fields: order_id, customer_id, items, total_cents, status, events, created_at"]
    <REF> entrypoints </REF>: List [text] ["mark_paid", "mark_cancelled", "add_event"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "State transition methods read and mutate the status field under guard rules and delegate event logging to add_event; add_event appends an event dict with a UTC ISO timestamp using datetime.now(timezone.utc)."
    <REF> internal_structure </REF>: List [text] ["State transitions: mark_paid, mark_cancelled (validate status and update, then record events)", "Event logging helper: add_event (append {kind, detail, timestamp} to events)", "Validation and error guards: raise ValueError when rules are violated"]
    <REF> lifecycle </REF>: List [text] ["Constructed via dataclass with provided fields", "Used by callers to transition status to paid or cancelled", "Events accumulate over the order lifetime to reflect changes"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["order_id: domain data identifier", "customer_id: domain data identifier", "items: domain data collection", "total_cents: domain monetary amount", "status: runtime state with guarded transitions", "events: event log list mutated by add_event", "created_at: creation timestamp"]
    <REF> inputs </REF>: List [text] ["payment_id (mark_paid)", "reason (mark_cancelled)", "kind, detail (add_event)", "current status read during validation in state transition methods"]
    <REF> outputs </REF>: List [text] ["status updated to 'paid' when paid", "status updated to 'cancelled' when cancelled", "events list appended with {kind, detail, timestamp} entries", "no direct return values from provided methods"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["datetime.now(timezone.utc) for UTC ISO timestamps", "dataclasses.dataclass for field-based initialization"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid", "commerce_ops_demo.commerce_ops.services.OrderService._build_order", "commerce_ops_demo.commerce_ops.services.OrderService.checkout"]
    <REF> key_interactions </REF>: List [text] ["Order.mark_paid is invoked by repository and service layers to finalize payment and log a 'paid' event", "Order.mark_cancelled updates status and logs a 'cancelled' event when not paid", "Order.add_event is called internally by transitions and by OrderService to record events", "add_event obtains timestamps via datetime and mutates the events list"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.status", "Mutates self.events by appending event dicts with timestamps", "Reads current time for timestamps"]
    <REF> errors </REF>: List [text] ["ValueError: only created orders can be marked paid (when status != 'created')", "ValueError: paid orders cannot be cancelled here (when status == 'paid')", "AttributeError: events does not support append", "NameError: datetime or timezone is not defined for timestamp creation"]
    <REF> invariants </REF>: List [text] ["Only orders in status 'created' may transition to 'paid'", "Paid orders must not be cancelled through mark_cancelled", "events must be a list-like that supports append", "Event timestamps are recorded in UTC ISO format"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_paid.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_cancelled.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/add_event.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Order`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Order

Represent an order with core fields, enforce simple status transitions (to paid or cancelled) with validation, and record a timestamped event log for significant changes.

## Role and Responsibilities
Primary: maintain order state and guard-valid transitions (pay, cancel). Secondary: append timestamped event entries describing changes.

## Public Surface
- mark_paid(payment_id)
- mark_cancelled(reason)
- add_event(kind, detail)
- dataclass-based construction with fields: order_id, customer_id, items, total_cents, status, events, created_at

## State Model
- order_id: domain data identifier
- customer_id: domain data identifier
- items: domain data collection
- total_cents: domain monetary amount
- status: runtime state with guarded transitions
- events: event log list mutated by add_event
- created_at: creation timestamp

## Internal Mechanism
State transition methods read and mutate the status field under guard rules and delegate event logging to add_event; add_event appends an event dict with a UTC ISO timestamp using datetime.now(timezone.utc).

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_paid.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_cancelled.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Order/add_event.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`

### Referenced By

- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `uses` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/models.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Order/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Order`
- `commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `commerce_ops_demo.commerce_ops.models.Order.add_event`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.models.Order`

---

<a id="class-commerce-ops-demo-commerce-ops-models-product"></a>

## commerce_ops_demo.commerce_ops.models.Product

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Product`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Product`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `class`, `entity`

### Summary

Represent a product and manage available inventory by providing validated reservation and release operations on stock.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" Product]

[DEFINE_PERSONA:]
    ROLE: "entity"
    DOMAIN: "E-commerce inventory and catalog model"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent a product and manage available inventory by providing validated reservation and release operations on stock."
    Responsibility: "Primary: enforce and apply stock changes with input validation and error signaling. Secondary: hold product attributes (sku, name, price_cents, tags)."
    PublicBehavior: "reserve(qty: int) -> None; release(qty: int) -> None"
    InternalMechanism: "A dataclass holds product data fields while stock operations validate inputs and mutate the stock field. Methods raise ValueError on invalid quantities or insufficient stock. External callers (ProductCatalog) invoke these operations to coordinate inventory changes."
    StateModel: "sku: product identifier (read by methods); name: product name (declared); price_cents: price in cents (declared); tags: label collection (declared); stock: available quantity (read and written by methods)"
    Collaboration: "dataclasses.dataclass (decorator); ValueError (exception type raised for validation failures)"
    ErrorBoundary: "ValueError: qty must be positive (reserve, release); ValueError: not enough stock for {self.sku} (reserve)"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "Product"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.models.Product"
    <REF> source_file </REF>: text "commerce_ops/models.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent a product and manage available inventory by providing validated reservation and release operations on stock."
    <REF> responsibility </REF>: text "Primary: enforce and apply stock changes with input validation and error signaling. Secondary: hold product attributes (sku, name, price_cents, tags)."
    <REF> role </REF>: text "entity"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["reserve(qty: int) -> None", "release(qty: int) -> None"]
    <REF> entrypoints </REF>: List [text] ["reserve(qty: int)", "release(qty: int)"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "A dataclass holds product data fields while stock operations validate inputs and mutate the stock field. Methods raise ValueError on invalid quantities or insufficient stock. External callers (ProductCatalog) invoke these operations to coordinate inventory changes."
    <REF> internal_structure </REF>: List [text] ["Domain data fields: sku, name, price_cents, tags", "Inventory field: stock (mutable; read/write)", "No private helpers; validation and mutation occur within public methods", "Decorator: dataclass"]
    <REF> lifecycle </REF>: List [text] ["Instantiated with product attributes and initial stock via dataclass construction", "Stock evolves through reserve and release calls", "No explicit teardown or disposal behavior"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["sku: product identifier (read by methods)", "name: product name (declared)", "price_cents: price in cents (declared)", "tags: label collection (declared)", "stock: available quantity (read and written by methods)"]
    <REF> inputs </REF>: List [text] ["qty (int) for reserve", "qty (int) for release", "Initial construction fields: sku, name, price_cents, stock, tags"]
    <REF> outputs </REF>: List [text] ["Updated stock via in-place mutation", "No return values from reserve or release"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["dataclasses.dataclass (decorator)", "ValueError (exception type raised for validation failures)"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items", "commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items"]
    <REF> key_interactions </REF>: List [text] ["Called by ProductCatalog to reserve or release product units", "Raises ValueError to signal invalid quantity or insufficient stock"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates in-memory state: self.stock"]
    <REF> errors </REF>: List [text] ["ValueError: qty must be positive (reserve, release)", "ValueError: not enough stock for {self.sku} (reserve)"]
    <REF> invariants </REF>: List [text] ["Reservation requires qty > 0 and qty <= current stock", "Release requires qty > 0", "Stock is not reduced below zero by reserve due to validation", "Only reserve and release modify stock in this class"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/reserve.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/release.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.models.Product`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Product

Represent a product and manage available inventory by providing validated reservation and release operations on stock.

## Role and Responsibilities
Primary: enforce and apply stock changes with input validation and error signaling. Secondary: hold product attributes (sku, name, price_cents, tags).

## Public Surface
- reserve(qty: int) -> None
- release(qty: int) -> None

## State Model
- sku: product identifier (read by methods)
- name: product name (declared)
- price_cents: price in cents (declared)
- tags: label collection (declared)
- stock: available quantity (read and written by methods)

## Internal Mechanism
A dataclass holds product data fields while stock operations validate inputs and mutate the stock field. Methods raise ValueError on invalid quantities or insufficient stock. External callers (ProductCatalog) invoke these operations to coordinate inventory changes.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/reserve.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/models.py/Product/release.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `uses` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `uses` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `uses` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `contains_symbol` <- `file:commerce_ops/models.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Product/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Product`
- `commerce_ops_demo.commerce_ops.models.Product.reserve`
- `commerce_ops_demo.commerce_ops.models.Product.release`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.models.Product`

---

<a id="class-commerce-ops-demo-commerce-ops-notifications-notificationservice"></a>

## commerce_ops_demo.commerce_ops.notifications.NotificationService

- Page ID: `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.notifications.NotificationService`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `class`, `service`

### Summary

Compose and record notification messages such as order receipts and low-stock alerts, accumulating them in an internal list for later use; invoked by OrderService._notify_customer.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" NotificationService]

[DEFINE_PERSONA:]
    ROLE: "service"
    DOMAIN: "commerce operations - notifications"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Compose and record notification messages such as order receipts and low-stock alerts, accumulating them in an internal list for later use; invoked by OrderService._notify_customer."
    Responsibility: "Primary: generate and accumulate notification messages in sent_messages. Secondary: delegate currency formatting to a helper function for receipt totals."
    PublicBehavior: "__init__(): initialize internal accumulator sent_messages; send_receipt(customer, order) -> str: compose a receipt message and record it; send_low_stock_alert(products, threshold=2) -> List[str]: generate alerts for low inventory and record them"
    InternalMechanism: "Builds message strings from provided domain objects, delegates currency formatting to format_currency for totals, appends each composed message to an internal sent_messages list, and returns the message or list of messages. No external I/O is performed."
    StateModel: "sent_messages: List[str] (accumulator; initialized in constructor; appended by public methods)"
    Collaboration: "commerce_ops_demo.commerce_ops.notifications.format_currency"
    ErrorBoundary: "<SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.; Exception: Propagated exception from format_currency when formatting the total.; AttributeError: Raised when expected attributes are missing on customer or order.; customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.; self.sent_messages is missing or not list-like, causing append to fail.; A product lacks the 'sku' attribute when formatting the alert string; A product lacks the 'stock' attribute when evaluating the threshold condition; TypeError: Object is not iterable.; TypeError: Unsupported comparison between product.stock and threshold.; products is None or not iterable when entering the loop"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "NotificationService"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.notifications.NotificationService"
    <REF> source_file </REF>: text "commerce_ops/notifications.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Compose and record notification messages such as order receipts and low-stock alerts, accumulating them in an internal list for later use; invoked by OrderService._notify_customer."
    <REF> responsibility </REF>: text "Primary: generate and accumulate notification messages in sent_messages. Secondary: delegate currency formatting to a helper function for receipt totals."
    <REF> role </REF>: text "service"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["__init__(): initialize internal accumulator sent_messages", "send_receipt(customer, order) -> str: compose a receipt message and record it", "send_low_stock_alert(products, threshold=2) -> List[str]: generate alerts for low inventory and record them"]
    <REF> entrypoints </REF>: List [text] ["__init__", "send_receipt", "send_low_stock_alert"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Builds message strings from provided domain objects, delegates currency formatting to format_currency for totals, appends each composed message to an internal sent_messages list, and returns the message or list of messages. No external I/O is performed."
    <REF> internal_structure </REF>: List [text] ["State: sent_messages (List[str]) as an accumulator for all composed notifications", "No private helpers; public methods directly compose and append messages", "Delegation: uses format_currency to format monetary amounts in receipt messages"]
    <REF> lifecycle </REF>: List [text] ["Creation: __init__ sets up sent_messages", "Usage: each call to a public method composes messages and appends them to sent_messages", "Retention: accumulated messages persist on the instance for its lifetime"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["sent_messages: List[str] (accumulator; initialized in constructor; appended by public methods)"]
    <REF> inputs </REF>: List [text] ["customer.email (send_receipt)", "order.order_id (send_receipt)", "order.total_cents (send_receipt, formatted via format_currency)", "products iterable of Product objects (send_low_stock_alert)", "product.sku (send_low_stock_alert)", "product.stock comparable to threshold (send_low_stock_alert)", "threshold: int with default 2 (send_low_stock_alert)"]
    <REF> outputs </REF>: List [text] ["receipt message string (from send_receipt)", "list of low-stock alert strings (from send_low_stock_alert)", "mutated sent_messages containing all composed messages"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["commerce_ops_demo.commerce_ops.notifications.format_currency"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService._notify_customer"]
    <REF> key_interactions </REF>: List [text] ["Incoming: OrderService._notify_customer -> send_receipt", "Incoming: OrderService._notify_customer -> send_low_stock_alert", "Outgoing: send_receipt -> format_currency for total formatting", "State effect: both public methods -> self.sent_messages.append for accumulation"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Appends composed messages to self.sent_messages", "Maintains an in-memory log of messages across calls via sent_messages"]
    <REF> errors </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.", "Exception: Propagated exception from format_currency when formatting the total.", "AttributeError: Raised when expected attributes are missing on customer or order.", "customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.", "self.sent_messages is missing or not list-like, causing append to fail.", "A product lacks the 'sku' attribute when formatting the alert string", "A product lacks the 'stock' attribute when evaluating the threshold condition", "TypeError: Object is not iterable.", "TypeError: Unsupported comparison between product.stock and threshold.", "products is None or not iterable when entering the loop"]
    <REF> invariants </REF>: List [text] ["sent_messages exists on the instance and supports append operations", "send_receipt assumes customer has email and order has order_id and total_cents acceptable to format_currency", "send_low_stock_alert assumes each product provides sku and stock, and stock is comparable to threshold", "Methods operate in-memory without external I/O; side effects are confined to sent_messages"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_receipt.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_low_stock_alert.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications.NotificationService

Compose and record notification messages such as order receipts and low-stock alerts, accumulating them in an internal list for later use; invoked by OrderService._notify_customer.

## Role and Responsibilities
Primary: generate and accumulate notification messages in sent_messages. Secondary: delegate currency formatting to a helper function for receipt totals.

## Public Surface
- __init__(): initialize internal accumulator sent_messages
- send_receipt(customer, order) -> str: compose a receipt message and record it
- send_low_stock_alert(products, threshold=2) -> List[str]: generate alerts for low inventory and record them

## State Model
- sent_messages: List[str] (accumulator; initialized in constructor; appended by public methods)

## Internal Mechanism
Builds message strings from provided domain objects, delegates currency formatting to format_currency for totals, appends each composed message to an internal sent_messages list, and returns the message or list of messages. No external I/O is performed.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_receipt.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_low_stock_alert.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/notifications.py`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.notifications.NotificationService`

---

<a id="class-commerce-ops-demo-commerce-ops-payments-paymenterror"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentError

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentError`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `class`, `value object`

### Summary

Provide a domain-specific runtime exception for payment operations so payment-related failures can be conveyed and categorized.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" PaymentError]

[DEFINE_PERSONA:]
    ROLE: "value object"
    DOMAIN: "payments"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide a domain-specific runtime exception for payment operations so payment-related failures can be conveyed and categorized."
    Responsibility: "Expose a named error type for payment logic, enabling callers to raise and catch payment-specific failures distinctly from other runtime errors."
    PublicBehavior: "Exception type subclassing RuntimeError for payment failures"
    InternalMechanism: "Inherits behavior from RuntimeError and serves as a semantic marker without adding state or methods."
    StateModel: "evidence: missing; confidence: not_available; source: static_analysis"
    Collaboration: "RuntimeError (inherits)"
    ErrorBoundary: "Raised to signal payment-related failures"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "PaymentError"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.payments.PaymentError"
    <REF> source_file </REF>: text "commerce_ops/payments.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Provide a domain-specific runtime exception for payment operations so payment-related failures can be conveyed and categorized."
    <REF> responsibility </REF>: text "Expose a named error type for payment logic, enabling callers to raise and catch payment-specific failures distinctly from other runtime errors."
    <REF> role </REF>: text "value object"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["Exception type subclassing RuntimeError for payment failures"]
    <REF> entrypoints </REF>: List [text] []

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Inherits behavior from RuntimeError and serves as a semantic marker without adding state or methods."
    <REF> internal_structure </REF>: List [text] ["No additional fields or methods beyond RuntimeError"]
    <REF> lifecycle </REF>: List [text] ["Instantiated and raised as a payment-specific RuntimeError", "Propagates up the call stack until caught by handlers for PaymentError or RuntimeError"]

    <!-- State and data -->
    <REF> state </REF>: List [text] []
    <REF> inputs </REF>: List [text] []
    <REF> outputs </REF>: List [text] []

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["RuntimeError (inherits)"]
    <REF> used_by </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> key_interactions </REF>: List [text] ["Inherits from RuntimeError to integrate with Python exception hierarchy"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] []
    <REF> errors </REF>: List [text] ["Raised to signal payment-related failures"]
    <REF> invariants </REF>: List [text] []

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentError

Provide a domain-specific runtime exception for payment operations so payment-related failures can be conveyed and categorized.

## Role and Responsibilities
Expose a named error type for payment logic, enabling callers to raise and catch payment-specific failures distinctly from other runtime errors.

## Public Surface
- Exception type subclassing RuntimeError for payment failures

## State Model
- evidence: missing; confidence: not_available; source: static_analysis

## Internal Mechanism
Inherits behavior from RuntimeError and serves as a semantic marker without adding state or methods.

## Related Classes
- {"source_class_id": "commerce_ops_demo.commerce_ops.payments.PaymentError", "target_class_id": "RuntimeError", "relation_type": "inherits_from", "evidence": "RuntimeError", "direction": "this -> target", "confidence": "medium"}

## Source Evidence
- evidence: missing; confidence: not_available; source: static_analysis

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `calls` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `contains_symbol` <- `file:commerce_ops/payments.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentError/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentError`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.payments.PaymentError`

---

<a id="class-commerce-ops-demo-commerce-ops-payments-paymentgateway"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentGateway

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `class`, `service`

### Summary

Provide payment authorization and refund operations with provider tagging, delegating balance changes to customer accounts, producing payment receipts, and tracking authorized and refunded totals.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" PaymentGateway]

[DEFINE_PERSONA:]
    ROLE: "service"
    DOMAIN: "Commerce payments"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide payment authorization and refund operations with provider tagging, delegating balance changes to customer accounts, producing payment receipts, and tracking authorized and refunded totals."
    Responsibility: "Primary: authorize payments, debit the customer, return a receipt, and accumulate authorized_total_cents. Secondary: process refunds by crediting the customer and accumulating refunded_total_cents while enforcing positive amounts and signaling failures via PaymentError."
    PublicBehavior: "__init__(provider='internal-wallet'); authorize(customer, amount_cents) -> PaymentReceipt; refund(customer, receipt) -> None"
    InternalMechanism: "Maintains a provider identifier and running counters for authorized and refunded amounts. For authorization, validates a positive amount, debits the customer, increments authorized_total_cents, and constructs a PaymentReceipt with a generated UUID and the provider. For refunds, validates a positive receipt amount, credits the customer, and increments refunded_total_cents. Validation failures and debit errors are communicated via PaymentError."
    StateModel: "provider: configuration string set during __init__; authorized_total_cents: running total of authorized amounts in cents; refunded_total_cents: running total of refunded amounts in cents"
    Collaboration: "<SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>; <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>; external.uuid4; external.str"
    ErrorBoundary: "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'amount must be positive' when amount_cents <= 0 in authorize; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: wraps ValueError from <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> during authorize; <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'receipt amount must be positive' when receipt.amount_cents <= 0 in refund"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "PaymentGateway"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.payments.PaymentGateway"
    <REF> source_file </REF>: text "commerce_ops/payments.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Provide payment authorization and refund operations with provider tagging, delegating balance changes to customer accounts, producing payment receipts, and tracking authorized and refunded totals."
    <REF> responsibility </REF>: text "Primary: authorize payments, debit the customer, return a receipt, and accumulate authorized_total_cents. Secondary: process refunds by crediting the customer and accumulating refunded_total_cents while enforcing positive amounts and signaling failures via PaymentError."
    <REF> role </REF>: text "service"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["__init__(provider='internal-wallet')", "authorize(customer, amount_cents) -> PaymentReceipt", "refund(customer, receipt) -> None"]
    <REF> entrypoints </REF>: List [text] ["__init__", "authorize", "refund"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Maintains a provider identifier and running counters for authorized and refunded amounts. For authorization, validates a positive amount, debits the customer, increments authorized_total_cents, and constructs a PaymentReceipt with a generated UUID and the provider. For refunds, validates a positive receipt amount, credits the customer, and increments refunded_total_cents. Validation failures and debit errors are communicated via PaymentError."
    <REF> internal_structure </REF>: List [text] ["Configuration: provider identifier stored at initialization and included in receipts", "Accumulators: authorized_total_cents and refunded_total_cents updated on successful operations", "Delegation to customer account methods: <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> and <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>", "Receipt construction: <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> with external.uuid4 and provider", "Validation and error signaling via <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>"]
    <REF> lifecycle </REF>: List [text] ["Construction sets provider and initializes authorized_total_cents and refunded_total_cents to 0", "During use, authorize and refund update running totals across the instance lifetime"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["provider: configuration string set during __init__", "authorized_total_cents: running total of authorized amounts in cents", "refunded_total_cents: running total of refunded amounts in cents"]
    <REF> inputs </REF>: List [text] ["constructor: provider (defaults to 'internal-wallet')", "authorize: customer and amount_cents (> 0)", "refund: customer and receipt with receipt.amount_cents (> 0)"]
    <REF> outputs </REF>: List [text] ["authorize: returns <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> containing id, amount_cents, and provider", "authorize: increments authorized_total_cents", "authorize: debits customer via <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>", "refund: increments refunded_total_cents", "refund: credits customer via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>", "refund: no return value"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>", "<SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>", "external.uuid4", "external.str"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService._charge"]
    <REF> key_interactions </REF>: List [text] ["authorize calls <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> to reduce customer funds", "refund calls <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL> to restore customer funds", "authorize constructs <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> with provider and a UUID from external.uuid4", "Validation and error translation via <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates authorized_total_cents on successful authorization", "Mutates refunded_total_cents on successful refund", "Debits customer balance via <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>", "Credits customer balance via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>"]
    <REF> errors </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'amount must be positive' when amount_cents <= 0 in authorize", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: wraps ValueError from <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> during authorize", "<SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: 'receipt amount must be positive' when receipt.amount_cents <= 0 in refund"]
    <REF> invariants </REF>: List [text] ["authorize requires amount_cents > 0", "refund requires receipt.amount_cents > 0", "authorized_total_cents increases by amount_cents on successful authorization", "refunded_total_cents increases by receipt.amount_cents on successful refund"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/authorize.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/refund.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentGateway

Provide payment authorization and refund operations with provider tagging, delegating balance changes to customer accounts, producing payment receipts, and tracking authorized and refunded totals.

## Role and Responsibilities
Primary: authorize payments, debit the customer, return a receipt, and accumulate authorized_total_cents. Secondary: process refunds by crediting the customer and accumulating refunded_total_cents while enforcing positive amounts and signaling failures via PaymentError.

## Public Surface
- __init__(provider='internal-wallet')
- authorize(customer, amount_cents) -> PaymentReceipt
- refund(customer, receipt) -> None

## State Model
- provider: configuration string set during __init__
- authorized_total_cents: running total of authorized amounts in cents
- refunded_total_cents: running total of refunded amounts in cents

## Internal Mechanism
Maintains a provider identifier and running counters for authorized and refunded amounts. For authorization, validates a positive amount, debits the customer, increments authorized_total_cents, and constructs a PaymentReceipt with a generated UUID and the provider. For refunds, validates a positive receipt amount, credits the customer, and increments refunded_total_cents. Validation failures and debit errors are communicated via PaymentError.

## Related Classes
- {"source_class_id": "commerce_ops_demo.commerce_ops.payments.PaymentGateway", "target_class_id": "commerce_ops_demo.commerce_ops.models.Customer", "relation_type": "uses", "evidence": "customer.debit(amount_cents)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.payments.PaymentGateway", "target_class_id": "commerce_ops_demo.commerce_ops.models.Customer", "relation_type": "uses", "evidence": "customer.credit(receipt.amount_cents)", "direction": "this -> target", "confidence": "high"}

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/authorize.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/refund.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Customer`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/payments.py`
- `topic_mentions` <- `topic:authentication`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.payments.PaymentGateway`

---

<a id="class-commerce-ops-demo-commerce-ops-payments-paymentreceipt"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentReceipt

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `class`, `value object`

### Summary

Represent structured payment receipt data with fields identifying the payment and its amount and provider.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" PaymentReceipt]

[DEFINE_PERSONA:]
    ROLE: "value object"
    DOMAIN: "commerce operations / payments"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent structured payment receipt data with fields identifying the payment and its amount and provider."
    Responsibility: "Encapsulate and transport payment receipt information as a simple structured data record."
    PublicBehavior: "dataclass-generated constructor for fields: payment_id, amount_cents, provider; public attributes: payment_id, amount_cents, provider"
    InternalMechanism: "Uses the dataclass decorator to generate initialization and attribute handling, storing receipt data without additional behavior."
    StateModel: "payment_id: domain data; amount_cents: domain data; provider: domain data"
    Collaboration: "evidence: missing; confidence: not_available; source: static_analysis"
    ErrorBoundary: "evidence: missing; confidence: not_available; source: static_analysis"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "PaymentReceipt"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.payments.PaymentReceipt"
    <REF> source_file </REF>: text "commerce_ops/payments.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent structured payment receipt data with fields identifying the payment and its amount and provider."
    <REF> responsibility </REF>: text "Encapsulate and transport payment receipt information as a simple structured data record."
    <REF> role </REF>: text "value object"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["dataclass-generated constructor for fields: payment_id, amount_cents, provider", "public attributes: payment_id, amount_cents, provider"]
    <REF> entrypoints </REF>: List [text] ["dataclass-generated constructor for fields: payment_id, amount_cents, provider"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Uses the dataclass decorator to generate initialization and attribute handling, storing receipt data without additional behavior."
    <REF> internal_structure </REF>: List [text] ["No user-defined methods within class scope", "Dataclass decorator provides boilerplate initialization and representation"]
    <REF> lifecycle </REF>: List [text] ["Creation via dataclass-generated constructor with receipt fields", "Used as a data carrier; no explicit reset or disposal behavior in evidence"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["payment_id: domain data", "amount_cents: domain data", "provider: domain data"]
    <REF> inputs </REF>: List [text] ["payment_id", "amount_cents", "provider"]
    <REF> outputs </REF>: List [text] ["Structured receipt data via attributes: payment_id, amount_cents, provider"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] []
    <REF> used_by </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> key_interactions </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] []
    <REF> errors </REF>: List [text] []
    <REF> invariants </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentReceipt

Represent structured payment receipt data with fields identifying the payment and its amount and provider.

## Role and Responsibilities
Encapsulate and transport payment receipt information as a simple structured data record.

## Public Surface
- dataclass-generated constructor for fields: payment_id, amount_cents, provider
- public attributes: payment_id, amount_cents, provider

## State Model
- payment_id: domain data
- amount_cents: domain data
- provider: domain data

## Internal Mechanism
Uses the dataclass decorator to generate initialization and attribute handling, storing receipt data without additional behavior.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- evidence: missing; confidence: not_available; source: static_analysis

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `contains_symbol` <- `file:commerce_ops/payments.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentReceipt/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

---

<a id="class-commerce-ops-demo-commerce-ops-pricing-pricequote"></a>

## commerce_ops_demo.commerce_ops.pricing.PriceQuote

- Page ID: `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `class`, `value object`

### Summary

Represent a price quote as a simple dataclass with fields for subtotal_cents, discount_cents, tax_cents, total_cents, and coupon.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" PriceQuote]

[DEFINE_PERSONA:]
    ROLE: "value object"
    DOMAIN: "commerce_ops_demo.commerce_ops.pricing"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Represent a price quote as a simple dataclass with fields for subtotal_cents, discount_cents, tax_cents, total_cents, and coupon."
    Responsibility: "Hold and convey computed price components and final total as structured data."
    PublicBehavior: "Dataclass-generated constructor to set: subtotal_cents, discount_cents, tax_cents, total_cents, coupon; Public attributes: subtotal_cents, discount_cents, tax_cents, total_cents, coupon"
    InternalMechanism: "The @dataclass decorator provides initialization and attribute storage; the class defines no custom methods or internal logic."
    StateModel: "subtotal_cents (domain data); discount_cents (domain data); tax_cents (domain data); total_cents (domain data); coupon (domain data)"
    Collaboration: "evidence: missing; confidence: not_available; source: static_analysis"
    ErrorBoundary: "No error-handling behavior in evidence"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "PriceQuote"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.pricing.PriceQuote"
    <REF> source_file </REF>: text "commerce_ops/pricing.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Represent a price quote as a simple dataclass with fields for subtotal_cents, discount_cents, tax_cents, total_cents, and coupon."
    <REF> responsibility </REF>: text "Hold and convey computed price components and final total as structured data."
    <REF> role </REF>: text "value object"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["Dataclass-generated constructor to set: subtotal_cents, discount_cents, tax_cents, total_cents, coupon", "Public attributes: subtotal_cents, discount_cents, tax_cents, total_cents, coupon"]
    <REF> entrypoints </REF>: List [text] ["Constructor (__init__)"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "The @dataclass decorator provides initialization and attribute storage; the class defines no custom methods or internal logic."
    <REF> internal_structure </REF>: List [text] ["No inheritance and no private helpers", "No internal call graph edges; pure data holder"]
    <REF> lifecycle </REF>: List [text] ["Created with pricing values; persists as an in-memory data record", "No explicit initialization beyond construction; no disposal/reset behavior in evidence"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["subtotal_cents (domain data)", "discount_cents (domain data)", "tax_cents (domain data)", "total_cents (domain data)", "coupon (domain data)"]
    <REF> inputs </REF>: List [text] ["subtotal_cents", "discount_cents", "tax_cents", "total_cents", "coupon"]
    <REF> outputs </REF>: List [text] ["Exposes pricing attributes via direct attribute access: subtotal_cents, discount_cents, tax_cents, total_cents, coupon"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] []
    <REF> used_by </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]
    <REF> key_interactions </REF>: List [text] ["No incoming or outgoing edges in class scope graph; no observed collaborations"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["None observed in class scope graph; data-only container"]
    <REF> errors </REF>: List [text] ["No error-handling behavior in evidence"]
    <REF> invariants </REF>: List [text] ["evidence: missing; confidence: not_available; source: static_analysis"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] []
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PriceQuote

Represent a price quote as a simple dataclass with fields for subtotal_cents, discount_cents, tax_cents, total_cents, and coupon.

## Role and Responsibilities
Hold and convey computed price components and final total as structured data.

## Public Surface
- Dataclass-generated constructor to set: subtotal_cents, discount_cents, tax_cents, total_cents, coupon
- Public attributes: subtotal_cents, discount_cents, tax_cents, total_cents, coupon

## State Model
- subtotal_cents (domain data)
- discount_cents (domain data)
- tax_cents (domain data)
- total_cents (domain data)
- coupon (domain data)

## Internal Mechanism
The @dataclass decorator provides initialization and attribute storage; the class defines no custom methods or internal logic.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- evidence: missing; confidence: not_available; source: static_analysis

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `contains_symbol` <- `file:commerce_ops/pricing.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PriceQuote/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PriceQuote`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.pricing.PriceQuote`

---

<a id="class-commerce-ops-demo-commerce-ops-pricing-pricingpolicy"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy

- Page ID: `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `class`, `service`

### Summary

Encapsulate pricing rules for shopping carts by computing a price quote that combines item subtotal, coupon-based discounts, and tax using configured policy state.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" PricingPolicy]

[DEFINE_PERSONA:]
    ROLE: "service"
    DOMAIN: "Commerce operations: pricing and quoting"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Encapsulate pricing rules for shopping carts by computing a price quote that combines item subtotal, coupon-based discounts, and tax using configured policy state."
    Responsibility: "Primary: Provide a price quoting capability that orchestrates subtotal calculation, coupon discounting, and tax computation into a final result. Secondary: Maintain pricing policy configuration (tax_rate_bps and coupons mapping) and expose reusable helpers for subtotal, coupon, and tax calculations with validation."
    PublicBehavior: "__init__(tax_rate_bps: int, coupons: mapping[str,int]): validate non-negative tax rate; normalize and store coupons with uppercase keys.; quote(customer, items, products, coupon): produce a PriceQuote by subtotaling items, applying coupon rules (code normalization, VIP bonus, cap), clamping taxable, computing tax, and validating positive total.; calculate_subtotal(items, products): compute subtotal in cents from product price lookup and item quantities with required validations.; apply_coupon(customer, subtotal_cents, coupon): resolve discount from coupons mapping with uppercased code, add VIP bonus when applicable, and cap discount to subtotal.; calculate_tax(taxable_cents): compute tax in cents using self.tax_rate_bps basis points with integer floor division."
    InternalMechanism: "The class holds configuration state for tax and supported coupons. Callers construct an instance with these settings, then use quote to coordinate subtotal, coupon application, and tax. quote delegates to calculate_subtotal, apply_coupon, and calculate_tax, enforces non-negative taxable amounts and positive totals, and constructs a <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>."
    StateModel: "tax_rate_bps (int): configuration for tax rate in basis points; written in __init__; read by calculate_tax.; coupons (mapping[str,int]): configuration of uppercase coupon codes to discount cents; written in __init__; read by apply_coupon."
    Collaboration: "<SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>; external.ValueError; external.max; external.min; external.coupon.upper; external.item.sku.upper; external.code.upper"
    ErrorBoundary: "ValueError: tax rate cannot be negative (initialization).; AttributeError: coupons does not provide an .items() method (initialization).; AttributeError: coupon code lacks .upper() during coupon key normalization (initialization).; ValueError: total must be positive (quote).; ValueError: qty must be positive (calculate_subtotal).; ValueError: price_cents must be positive (calculate_subtotal).; AttributeError: item missing required attributes or sku lacks upper() (calculate_subtotal).; KeyError: SKU not found in price lookup (calculate_subtotal).; TypeError: Non-numeric qty or price causes arithmetic failure (calculate_subtotal).; ValueError: coupon is not supported (apply_coupon).; AttributeError or TypeError: coupon.upper() unavailable or failed (apply_coupon).; ValueError: taxable amount cannot be negative (calculate_tax).; TypeError: Non-numeric taxable_cents or tax_rate_bps (calculate_tax)."
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "PricingPolicy"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.pricing.PricingPolicy"
    <REF> source_file </REF>: text "commerce_ops/pricing.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Encapsulate pricing rules for shopping carts by computing a price quote that combines item subtotal, coupon-based discounts, and tax using configured policy state."
    <REF> responsibility </REF>: text "Primary: Provide a price quoting capability that orchestrates subtotal calculation, coupon discounting, and tax computation into a final result. Secondary: Maintain pricing policy configuration (tax_rate_bps and coupons mapping) and expose reusable helpers for subtotal, coupon, and tax calculations with validation."
    <REF> role </REF>: text "service"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["__init__(tax_rate_bps: int, coupons: mapping[str,int]): validate non-negative tax rate; normalize and store coupons with uppercase keys.", "quote(customer, items, products, coupon): produce a PriceQuote by subtotaling items, applying coupon rules (code normalization, VIP bonus, cap), clamping taxable, computing tax, and validating positive total.", "calculate_subtotal(items, products): compute subtotal in cents from product price lookup and item quantities with required validations.", "apply_coupon(customer, subtotal_cents, coupon): resolve discount from coupons mapping with uppercased code, add VIP bonus when applicable, and cap discount to subtotal.", "calculate_tax(taxable_cents): compute tax in cents using self.tax_rate_bps basis points with integer floor division."]
    <REF> entrypoints </REF>: List [text] ["quote", "__init__"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "The class holds configuration state for tax and supported coupons. Callers construct an instance with these settings, then use quote to coordinate subtotal, coupon application, and tax. quote delegates to calculate_subtotal, apply_coupon, and calculate_tax, enforces non-negative taxable amounts and positive totals, and constructs a <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>."
    <REF> internal_structure </REF>: List [text] ["Quote orchestration entry: coordinates subtotal, coupon discounting, tax computation, and builds <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>.", "Subtotal computation helper: validates items and products and sums price_cents * qty.", "Coupon handling helper: normalizes coupon code to uppercase, looks up in self.coupons, adds VIP bonus when applicable, caps discount to subtotal.", "Tax calculation helper: reads self.tax_rate_bps and computes integer tax from a non-negative taxable amount.", "Configuration state: self.tax_rate_bps and self.coupons set during initialization."]
    <REF> lifecycle </REF>: List [text] ["Creation: __init__ validates tax_rate_bps >= 0 and normalizes coupon keys to uppercase before storing state.", "Usage: quote is invoked with customer, items, products, and an optional coupon to obtain a PriceQuote.", "No explicit reset or disposal behavior is defined."]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["tax_rate_bps (int): configuration for tax rate in basis points; written in __init__; read by calculate_tax.", "coupons (mapping[str,int]): configuration of uppercase coupon codes to discount cents; written in __init__; read by apply_coupon."]
    <REF> inputs </REF>: List [text] ["tax_rate_bps (int)", "coupons (mapping[str,int])", "customer (Customer)", "items (List[CartItem])", "products (List[Product])", "coupon (str)", "taxable_cents (int)"]
    <REF> outputs </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL> from quote", "subtotal_cents (int)", "discount_cents (int)", "tax_cents (int)", "total_cents (int) encapsulated in PriceQuote"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["<SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>", "external.ValueError", "external.max", "external.min", "external.coupon.upper", "external.item.sku.upper", "external.code.upper"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService.checkout"]
    <REF> key_interactions </REF>: List [text] ["quote -> calculate_subtotal", "quote -> apply_coupon", "quote -> calculate_tax", "quote -> <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>", "commerce_ops_demo.commerce_ops.services.OrderService.checkout -> quote", "apply_coupon reads self.coupons", "calculate_tax reads self.tax_rate_bps"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Sets self.tax_rate_bps during construction.", "Normalizes and stores coupons mapping with uppercase keys during construction.", "Constructs <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL> when quoting."]
    <REF> errors </REF>: List [text] ["ValueError: tax rate cannot be negative (initialization).", "AttributeError: coupons does not provide an .items() method (initialization).", "AttributeError: coupon code lacks .upper() during coupon key normalization (initialization).", "ValueError: total must be positive (quote).", "ValueError: qty must be positive (calculate_subtotal).", "ValueError: price_cents must be positive (calculate_subtotal).", "AttributeError: item missing required attributes or sku lacks upper() (calculate_subtotal).", "KeyError: SKU not found in price lookup (calculate_subtotal).", "TypeError: Non-numeric qty or price causes arithmetic failure (calculate_subtotal).", "ValueError: coupon is not supported (apply_coupon).", "AttributeError or TypeError: coupon.upper() unavailable or failed (apply_coupon).", "ValueError: taxable amount cannot be negative (calculate_tax).", "TypeError: Non-numeric taxable_cents or tax_rate_bps (calculate_tax)."]
    <REF> invariants </REF>: List [text] ["self.tax_rate_bps >= 0.", "Coupon codes are normalized to uppercase in self.coupons.", "Subtotal uses only items with qty > 0 and products with price_cents > 0.", "Accepted coupon must exist in self.coupons.", "Applied discount is capped to subtotal.", "Taxable amount provided to tax calculation is >= 0.", "Final total in a quote is > 0."]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/quote.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_subtotal.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/apply_coupon.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_tax.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy

Encapsulate pricing rules for shopping carts by computing a price quote that combines item subtotal, coupon-based discounts, and tax using configured policy state.

## Role and Responsibilities
Primary: Provide a price quoting capability that orchestrates subtotal calculation, coupon discounting, and tax computation into a final result. Secondary: Maintain pricing policy configuration (tax_rate_bps and coupons mapping) and expose reusable helpers for subtotal, coupon, and tax calculations with validation.

## Public Surface
- __init__(tax_rate_bps: int, coupons: mapping[str,int]): validate non-negative tax rate; normalize and store coupons with uppercase keys.
- quote(customer, items, products, coupon): produce a PriceQuote by subtotaling items, applying coupon rules (code normalization, VIP bonus, cap), clamping taxable, computing tax, and validating positive total.
- calculate_subtotal(items, products): compute subtotal in cents from product price lookup and item quantities with required validations.
- apply_coupon(customer, subtotal_cents, coupon): resolve discount from coupons mapping with uppercased code, add VIP bonus when applicable, and cap discount to subtotal.
- calculate_tax(taxable_cents): compute tax in cents using self.tax_rate_bps basis points with integer floor division.

## State Model
- tax_rate_bps (int): configuration for tax rate in basis points; written in __init__; read by calculate_tax.
- coupons (mapping[str,int]): configuration of uppercase coupon codes to discount cents; written in __init__; read by apply_coupon.

## Internal Mechanism
The class holds configuration state for tax and supported coupons. Callers construct an instance with these settings, then use quote to coordinate subtotal, coupon application, and tax. quote delegates to calculate_subtotal, apply_coupon, and calculate_tax, enforces non-negative taxable amounts and positive totals, and constructs a <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL>.

## Related Classes
- evidence: missing; confidence: not_available; source: static_analysis

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/quote.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_subtotal.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/apply_coupon.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_tax.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/pricing.py`
- `topic_mentions` <- `topic:configuration`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`

---

<a id="class-commerce-ops-demo-commerce-ops-repository-orderrepository"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository

- Page ID: `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `class`, `repository`

### Summary

Provide an in-memory repository for Order entities keyed by order_id, enabling save, retrieval, customer-based listing, and a paid-marking workflow used by service-layer operations.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" OrderRepository]

[DEFINE_PERSONA:]
    ROLE: "repository"
    DOMAIN: "Commerce operations / order management"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Provide an in-memory repository for Order entities keyed by order_id, enabling save, retrieval, customer-based listing, and a paid-marking workflow used by service-layer operations."
    Responsibility: "Primary: manage storage and retrieval of Order entities in an internal mapping keyed by order_id. Secondary: support filtered queries by customer_id and coordinate the mark-paid update by invoking the Order domain method and persisting the change."
    PublicBehavior: "Constructor: __init__() initializes an empty orders mapping; save(order): validate order.order_id is truthy and store in the internal mapping under that key; get(order_id): return the stored Order for the given id or raise KeyError; list_by_customer(customer_id): return a new list of orders whose customer_id matches; mark_paid(order_id, payment_id): retrieve Order, invoke domain mark_paid, persist via save, and return the updated entity"
    InternalMechanism: "Maintains a per-instance dictionary mapping order_id to Order. Operations read and write this mapping: save validates a truthy order_id before inserting/updating; get indexes by key and raises KeyError when absent; list_by_customer filters values() by customer_id into a new list; mark_paid orchestrates get, delegates to Order.mark_paid(payment_id), then persists with save."
    StateModel: "orders: Dict[str, Order] (runtime in-memory store; writes in __init__ and save; reads in save/get/list_by_customer)"
    Collaboration: "commerce_ops_demo.commerce_ops.models.Order (used by mark_paid); external.ValueError (thrown by save on missing order_id); external.KeyError (thrown by get when order_id not found)"
    ErrorBoundary: "ValueError: order_id is required (save) when order.order_id is falsy; KeyError: order {order_id} not found (get) when the id is absent; AttributeError: Encountered an order without a customer_id attribute while filtering (list_by_customer); AttributeError: The orders collection does not implement values() (list_by_customer); <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid (mark_paid); <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order (mark_paid); <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order (mark_paid); AttributeError: Attempting to call mark_paid on a None order value (mark_paid); Retrieved order is None, causing a failure on mark_paid invocation (mark_paid)"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "OrderRepository"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.repository.OrderRepository"
    <REF> source_file </REF>: text "commerce_ops/repository.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Provide an in-memory repository for Order entities keyed by order_id, enabling save, retrieval, customer-based listing, and a paid-marking workflow used by service-layer operations."
    <REF> responsibility </REF>: text "Primary: manage storage and retrieval of Order entities in an internal mapping keyed by order_id. Secondary: support filtered queries by customer_id and coordinate the mark-paid update by invoking the Order domain method and persisting the change."
    <REF> role </REF>: text "repository"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["Constructor: __init__() initializes an empty orders mapping", "save(order): validate order.order_id is truthy and store in the internal mapping under that key", "get(order_id): return the stored Order for the given id or raise KeyError", "list_by_customer(customer_id): return a new list of orders whose customer_id matches", "mark_paid(order_id, payment_id): retrieve Order, invoke domain mark_paid, persist via save, and return the updated entity"]
    <REF> entrypoints </REF>: List [text] ["__init__", "save", "get", "list_by_customer", "mark_paid"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Maintains a per-instance dictionary mapping order_id to Order. Operations read and write this mapping: save validates a truthy order_id before inserting/updating; get indexes by key and raises KeyError when absent; list_by_customer filters values() by customer_id into a new list; mark_paid orchestrates get, delegates to Order.mark_paid(payment_id), then persists with save."
    <REF> internal_structure </REF>: List [text] ["In-memory orders mapping keyed by order_id (state store)", "Shared helpers with high fan-in: save (write path), get (read path)", "Orchestration method: mark_paid -> get + Order.mark_paid + save", "Filtering operation: list_by_customer iterates self.orders.values() to build a new list"]
    <REF> lifecycle </REF>: List [text] ["Creation: __init__ sets self.orders to an empty mapping", "Usage: save adds/updates orders; get retrieves by order_id; list_by_customer queries by customer_id", "Update workflow: mark_paid updates the domain entity then persists via save", "State persists within the repository instance across calls until overwritten on save"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["orders: Dict[str, Order] (runtime in-memory store; writes in __init__ and save; reads in save/get/list_by_customer)"]
    <REF> inputs </REF>: List [text] ["order (Order) with a truthy order_id for save", "order_id (str) for get and mark_paid", "customer_id (str) for list_by_customer", "payment_id (str) for mark_paid"]
    <REF> outputs </REF>: List [text] ["get returns Order for the given order_id", "list_by_customer returns List[Order] filtered by customer_id", "mark_paid returns the updated Order after persisting", "save returns no value and mutates repository state"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["commerce_ops_demo.commerce_ops.models.Order (used by mark_paid)", "external.ValueError (thrown by save on missing order_id)", "external.KeyError (thrown by get when order_id not found)"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.services.OrderService.checkout -> save", "commerce_ops_demo.commerce_ops.services.OrderService.cancel_order -> get, save", "commerce_ops_demo.commerce_ops.services.OrderService.customer_history -> list_by_customer"]
    <REF> key_interactions </REF>: List [text] ["Service layer uses repository to persist and query orders across checkout, cancellation, and history features", "Repository invokes commerce_ops_demo.commerce_ops.models.Order.mark_paid during the mark-paid workflow", "Repository enforces validation and existence via ValueError and KeyError on invalid operations"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.orders mapping", "Overwrites existing entries on duplicate order_id in save", "Persists domain changes during mark_paid by calling save", "Raises exceptions on validation and lookup failures"]
    <REF> errors </REF>: List [text] ["ValueError: order_id is required (save) when order.order_id is falsy", "KeyError: order {order_id} not found (get) when the id is absent", "AttributeError: Encountered an order without a customer_id attribute while filtering (list_by_customer)", "AttributeError: The orders collection does not implement values() (list_by_customer)", "<SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid (mark_paid)", "<SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order (mark_paid)", "<SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order (mark_paid)", "AttributeError: Attempting to call mark_paid on a None order value (mark_paid)", "Retrieved order is None, causing a failure on mark_paid invocation (mark_paid)"]
    <REF> invariants </REF>: List [text] ["orders mapping is keyed by order.order_id", "save requires a truthy order.order_id and writes to orders[order.order_id]", "get requires order_id to exist in the internal mapping", "list_by_customer relies on orders having Order objects with a customer_id attribute", "After mark_paid, the updated Order is persisted via save"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/save.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/get.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/list_by_customer.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/mark_paid.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository

Provide an in-memory repository for Order entities keyed by order_id, enabling save, retrieval, customer-based listing, and a paid-marking workflow used by service-layer operations.

## Role and Responsibilities
Primary: manage storage and retrieval of Order entities in an internal mapping keyed by order_id. Secondary: support filtered queries by customer_id and coordinate the mark-paid update by invoking the Order domain method and persisting the change.

## Public Surface
- Constructor: __init__() initializes an empty orders mapping
- save(order): validate order.order_id is truthy and store in the internal mapping under that key
- get(order_id): return the stored Order for the given id or raise KeyError
- list_by_customer(customer_id): return a new list of orders whose customer_id matches
- mark_paid(order_id, payment_id): retrieve Order, invoke domain mark_paid, persist via save, and return the updated entity

## State Model
- orders: Dict[str, Order] (runtime in-memory store; writes in __init__ and save; reads in save/get/list_by_customer)

## Internal Mechanism
Maintains a per-instance dictionary mapping order_id to Order. Operations read and write this mapping: save validates a truthy order_id before inserting/updating; get indexes by key and raises KeyError when absent; list_by_customer filters values() by customer_id into a new list; mark_paid orchestrates get, delegates to Order.mark_paid(payment_id), then persists with save.

## Related Classes
- {"source_class_id": "commerce_ops_demo.commerce_ops.repository.OrderRepository", "target_class_id": "commerce_ops_demo.commerce_ops.models.Order", "relation_type": "uses", "evidence": "order.mark_paid(payment_id)", "direction": "this -> target", "confidence": "high"}

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/save.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/get.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/list_by_customer.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/mark_paid.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Order`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `uses` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `contains_symbol` <- `file:commerce_ops/repository.py`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.repository.OrderRepository`

---

<a id="class-commerce-ops-demo-commerce-ops-services-orderservice"></a>

## commerce_ops_demo.commerce_ops.services.OrderService

- Page ID: `class:commerce_ops_demo.commerce_ops.services.OrderService`
- Type: `entity` / `class`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `class`, `service`

### Summary

Coordinate checkout, cancellation, and customer order history by orchestrating catalog, pricing, payments, persistence, and notifications.

### SPL Content

```spl
[DEFINE_AGENT: "A class that represents a cohesive abstraction with responsibility, state, behavior, and collaboration boundaries" OrderService]

[DEFINE_PERSONA:]
    ROLE: "service"
    DOMAIN: "E-commerce order processing and checkout orchestration"
    ABSTRACTION_LEVEL: "Class-level; describes what the class does and how it works at a summarized level without expanding method command flows"
[END_PERSONA]

[DEFINE_AUDIENCE:]
    KNOWLEDGE: "Developers who need to understand, reuse, test, extend, or modify this class"
    INTEREST: "Class purpose, responsibility, public behavior, state, dependencies, control role, side effects, and errors"
[END_AUDIENCE]

[DEFINE_CONCEPTS:]
    Purpose: "Coordinate checkout, cancellation, and customer order history by orchestrating catalog, pricing, payments, persistence, and notifications."
    Responsibility: "Primary: End-to-end checkout orchestration. Secondary: Order cancellation and customer order history summarization."
    PublicBehavior: "__init__(catalog, pricing, payments, repository, notifications); checkout(customer, items, coupon='') -> Order; cancel_order(order_id, reason) -> Order; customer_history(customer_id) -> List[dict]"
    InternalMechanism: "Acts as an orchestrator across injected services: reserves inventory via a catalog, requests a price quote, constructs an Order via an internal builder, authorizes payment while storing the last receipt, marks the order paid, persists it, and sends customer and stock notifications. On post-reservation failures during checkout, it releases inventory and lets the error propagate. Cancellation retrieves and updates an order, releases items, and saves. Customer history delegates to the repository and returns a simplified projection."
    StateModel: "catalog: dependency (ProductCatalog); pricing: dependency (PricingPolicy); payments: dependency (PaymentGateway); repository: dependency (OrderRepository); notifications: dependency (NotificationService); last_receipt: runtime state (last payment receipt)"
    Collaboration: "commerce_ops_demo.commerce_ops.catalog.ProductCatalog; commerce_ops_demo.commerce_ops.pricing.PricingPolicy; commerce_ops_demo.commerce_ops.payments.PaymentGateway; commerce_ops_demo.commerce_ops.repository.OrderRepository; commerce_ops_demo.commerce_ops.notifications.NotificationService; commerce_ops_demo.commerce_ops.models.Order"
    ErrorBoundary: "Propagates exceptions from ProductCatalog reserve/release; Propagates exceptions from PricingPolicy.quote; Propagates exceptions from PaymentGateway.authorize; Propagates exceptions from OrderRepository.get/save/list_by_customer; Propagates exceptions from NotificationService sending methods; Attribute errors if injected dependencies are missing or lack required methods; If checkout fails after reservation, items are released and the original error is re-raised; Type errors if iterable inputs (items, orders) are invalid; Order retrieval may return None leading to attribute access errors during cancellation"
[END_CONCEPTS]

[DEFINE_VARIABLES:]
    <!-- Identity -->
    <REF> class_name </REF>: text "OrderService"
    <REF> qualified_name </REF>: text "commerce_ops_demo.commerce_ops.services.OrderService"
    <REF> source_file </REF>: text "commerce_ops/services.py"

    <!-- Purpose and responsibility -->
    <REF> purpose </REF>: text "Coordinate checkout, cancellation, and customer order history by orchestrating catalog, pricing, payments, persistence, and notifications."
    <REF> responsibility </REF>: text "Primary: End-to-end checkout orchestration. Secondary: Order cancellation and customer order history summarization."
    <REF> role </REF>: text "service"

    <!-- Public surface -->
    <REF> public_surface </REF>: List [text] ["__init__(catalog, pricing, payments, repository, notifications)", "checkout(customer, items, coupon='') -> Order", "cancel_order(order_id, reason) -> Order", "customer_history(customer_id) -> List[dict]"]
    <REF> entrypoints </REF>: List [text] ["__init__", "checkout", "cancel_order", "customer_history"]

    <!-- Internal mechanism -->
    <REF> mechanism </REF>: text "Acts as an orchestrator across injected services: reserves inventory via a catalog, requests a price quote, constructs an Order via an internal builder, authorizes payment while storing the last receipt, marks the order paid, persists it, and sends customer and stock notifications. On post-reservation failures during checkout, it releases inventory and lets the error propagate. Cancellation retrieves and updates an order, releases items, and saves. Customer history delegates to the repository and returns a simplified projection."
    <REF> internal_structure </REF>: List [text] ["Public orchestrator: checkout(...) coordinates inventory, pricing, payment, persistence, and notifications", "Private helper: _build_order(...) constructs Order and records a quoted event", "Private helper: _charge(...) authorizes payment and updates last_receipt", "Private helper: _notify_customer(...) sends receipt and low-stock alerts", "Public maintenance: cancel_order(...) releases items and persists cancellation", "Public query: customer_history(...) lists orders as summary dicts"]
    <REF> lifecycle </REF>: List [text] ["Constructed with catalog, pricing, payments, repository, notifications; initializes last_receipt=None", "Used per checkout/cancel/query invocation; no persistent sessions maintained", "No explicit teardown or disposal behavior in evidence"]

    <!-- State and data -->
    <REF> state </REF>: List [text] ["catalog: dependency (ProductCatalog)", "pricing: dependency (PricingPolicy)", "payments: dependency (PaymentGateway)", "repository: dependency (OrderRepository)", "notifications: dependency (NotificationService)", "last_receipt: runtime state (last payment receipt)"]
    <REF> inputs </REF>: List [text] ["constructor: catalog, pricing, payments, repository, notifications", "checkout: customer, items, coupon", "cancel_order: order_id, reason", "customer_history: customer_id"]
    <REF> outputs </REF>: List [text] ["checkout returns Order (paid and persisted)", "cancel_order returns Order (cancelled and persisted)", "customer_history returns List[dict] with order_id, status, total as string"]

    <!-- Collaboration -->
    <REF> dependencies </REF>: List [text] ["commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "commerce_ops_demo.commerce_ops.pricing.PricingPolicy", "commerce_ops_demo.commerce_ops.payments.PaymentGateway", "commerce_ops_demo.commerce_ops.repository.OrderRepository", "commerce_ops_demo.commerce_ops.notifications.NotificationService", "commerce_ops_demo.commerce_ops.models.Order"]
    <REF> used_by </REF>: List [text] ["commerce_ops_demo.commerce_ops.cli.run_checkout_demo"]
    <REF> key_interactions </REF>: List [text] ["Reserve and release inventory via ProductCatalog", "Quote pricing via PricingPolicy", "Construct orders and add events via Order", "Authorize payments via PaymentGateway and store last_receipt", "Mark orders paid via Order.mark_paid", "Persist orders via OrderRepository.save and fetch via get/list_by_customer", "Send receipt and low-stock alerts via NotificationService"]

    <!-- Effects and risks -->
    <REF> side_effects </REF>: List [text] ["Mutates self.last_receipt during charge", "Reserves and releases inventory in catalog", "Charges payment through external gateway", "Persists orders to repository", "Sends customer receipt notifications", "Triggers low-stock alerts", "Marks order as paid"]
    <REF> errors </REF>: List [text] ["Propagates exceptions from ProductCatalog reserve/release", "Propagates exceptions from PricingPolicy.quote", "Propagates exceptions from PaymentGateway.authorize", "Propagates exceptions from OrderRepository.get/save/list_by_customer", "Propagates exceptions from NotificationService sending methods", "Attribute errors if injected dependencies are missing or lack required methods", "If checkout fails after reservation, items are released and the original error is re-raised", "Type errors if iterable inputs (items, orders) are invalid", "Order retrieval may return None leading to attribute access errors during cancellation"]
    <REF> invariants </REF>: List [text] ["Dependencies catalog, pricing, payments, repository, notifications must be set before use", "Inventory reserved during checkout is released on any subsequent failure", "Order is marked paid only after successful payment authorization", "last_receipt reflects the most recent payment authorization in this instance", "Order changes are persisted via the repository for checkout and cancellation"]

    <!-- Traceability -->
    <REF> method_refs </REF>: List [text] ["<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__init__.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/checkout.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/cancel_order.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/customer_history.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_build_order.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_charge.spl</SPL>", "<SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_notify_customer.spl</SPL>"]
[END_VARIABLES]

<!-- This section defines class-level reverse-engineering information.
     It should let a developer understand what the class does, why it exists, how it works at a summarized level, and where to inspect method-level details.
     Do NOT expand method COMMAND flows.
     Do NOT restate every method implementation.
     Use method_refs only for traceability. -->

[DEFINE_CONSTRAINTS:]
    ClassLevelOnly: "Describe the class-level abstraction; do not expand individual method command flows" LOG "class_over_expansion"
    MechanismSummary: "Explain how the class works only at a summarized class level" LOG "class_mechanism_over_detail"
    ResponsibilityBoundary: "Distinguish what this class owns from what it delegates to dependencies" LOG "class_boundary_error"
    StateAccuracy: "Only include state actually owned, read, mutated, cached, or exposed by this class" LOG "class_state_error"
    Traceability: "Refer to method-level SPL artifacts by reference instead of inlining method-level details" LOG "method_detail_leakage"
[END_CONSTRAINTS]

[END_AGENT]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `class:commerce_ops_demo.commerce_ops.services.OrderService`
- Entity kind: `class`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService

Coordinate checkout, cancellation, and customer order history by orchestrating catalog, pricing, payments, persistence, and notifications.

## Role and Responsibilities
Primary: End-to-end checkout orchestration. Secondary: Order cancellation and customer order history summarization.

## Public Surface
- __init__(catalog, pricing, payments, repository, notifications)
- checkout(customer, items, coupon='') -> Order
- cancel_order(order_id, reason) -> Order
- customer_history(customer_id) -> List[dict]

## State Model
- catalog: dependency (ProductCatalog)
- pricing: dependency (PricingPolicy)
- payments: dependency (PaymentGateway)
- repository: dependency (OrderRepository)
- notifications: dependency (NotificationService)
- last_receipt: runtime state (last payment receipt)

## Internal Mechanism
Acts as an orchestrator across injected services: reserves inventory via a catalog, requests a price quote, constructs an Order via an internal builder, authorizes payment while storing the last receipt, marks the order paid, persists it, and sends customer and stock notifications. On post-reservation failures during checkout, it releases inventory and lets the error propagate. Cancellation retrieves and updates an order, releases items, and saves. Customer history delegates to the repository and returns a simplified projection.

## Related Classes
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "relation_type": "uses", "evidence": "self.catalog.reserve_items(items)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.pricing.PricingPolicy", "relation_type": "uses", "evidence": "self.pricing.quote(customer, items, reserved_products, coupon)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.models.Order", "relation_type": "uses", "evidence": "order.mark_paid(receipt.payment_id)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.repository.OrderRepository", "relation_type": "uses", "evidence": "self.repository.save(order)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "relation_type": "uses", "evidence": "self.catalog.release_items(items)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.repository.OrderRepository", "relation_type": "uses", "evidence": "self.repository.get(order_id)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.catalog.ProductCatalog", "relation_type": "uses", "evidence": "self.catalog.release_items(order.items)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.repository.OrderRepository", "relation_type": "uses", "evidence": "self.repository.save(order)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.repository.OrderRepository", "relation_type": "uses", "evidence": "self.repository.list_by_customer(customer_id)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.models.Order", "relation_type": "uses", "evidence": "order.add_event(\"quoted\", f\"subtotal={quote.subtotal_cents}; discount={quote.discount_cents}; tax={quote.tax_cents}\")", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.payments.PaymentGateway", "relation_type": "uses", "evidence": "self.payments.authorize(customer, quote.total_cents)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.notifications.NotificationService", "relation_type": "uses", "evidence": "self.notifications.send_receipt(customer, order)", "direction": "this -> target", "confidence": "high"}
- {"source_class_id": "commerce_ops_demo.commerce_ops.services.OrderService", "target_class_id": "commerce_ops_demo.commerce_ops.notifications.NotificationService", "relation_type": "uses", "evidence": "self.notifications.send_low_stock_alert(products)", "direction": "this -> target", "confidence": "high"}

## Source Evidence
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__init__.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/checkout.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/cancel_order.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/customer_history.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_build_order.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_charge.spl</SPL>
- <SPL>spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_notify_customer.spl</SPL>

### Outgoing Links

- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `contains_method` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `uses` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `uses` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `uses` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `uses` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `uses` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `uses` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `uses` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `uses` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `uses` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `uses` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `uses` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `uses` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `owned_by_class` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `contains_symbol` <- `file:commerce_ops/services.py`
- `topic_mentions` <- `topic:authentication`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__class__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService`
- `commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- `commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`

### Graph References

- `class_scope:commerce_ops_demo.commerce_ops.services.OrderService`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-productcatalog-init"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Initializes the instance by creating a dictionary mapping normalized SKUs to the provided Product objects from the input iterable.

### SPL Content

```spl
[DEFINE_WORKER: "Initializes the instance by creating a dictionary mapping normalized SKUs to the provided Product objects from the input iterable." __init__]
    [INPUTS]
        <REF> products </REF>: Iterable[Product] "Iterable of Product objects to populate the instance mapping."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.products </REF>: Dict[str, Product] "Instance dictionary mapping normalized SKU strings to Product objects, populated from the input."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Initialize self.products to an empty dictionary RESULT self.products]
            [COMMAND Iterate over products; for each product, compute key = <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) and assign self.products[key] = product RESULT self.products populated with entries for each product; later products with the same normalized key overwrite earlier ones]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: If multiple products resolve to the same normalized SKU]
        [SEQUENTIAL_BLOCK]
            [COMMAND Assign the later product to the existing key in self.products RESULT The later product overwrites the earlier entry for that key]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: products is not iterable when the for-loop begins]
        [LOG "Failed to iterate over products: object is not iterable"]
        [THROW TypeError "The provided products argument is not iterable."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: An element in products lacks a sku attribute]
        [LOG "Product missing 'sku' attribute during normalization"]
        [THROW AttributeError "Encountered a product without a sku attribute."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) raises an exception]
        [LOG "Error from <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL> during key normalization"]
        [THROW Exception "Exception propagated from <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) returns a non-hashable key]
        [LOG "Non-hashable normalized SKU used as dict key"]
        [THROW TypeError "Unhashable key cannot be used in dict assignment."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__

Initializes the instance by creating a dictionary mapping normalized SKUs to the provided Product objects from the input iterable.

## Inputs
- products (Iterable[Product]): Iterable of Product objects to populate the instance mapping.

## Outputs
- self.products (Dict[str, Product]): Instance dictionary mapping normalized SKU strings to Product objects, populated from the input.

## Main Effect
Iterate over products; for each product, compute key = <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) and assign self.products[key] = product

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.normalize_sku

## Side Effects
- mutates self.products
- mutates self.products[normalize_sku(product.sku)]
- self.products (Dict[str, Product]): Instance dictionary mapping normalized SKU strings to Product objects, populated from the input.

## Errors
- <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) raises an exception
- <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>(product.sku) returns a non-hashable key
- An element in products lacks a sku attribute
- AttributeError: Encountered a product without a sku attribute.
- Exception: Exception propagated from <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>.
- TypeError: The provided products argument is not iterable.
- TypeError: Unhashable key cannot be used in dict assignment.
- products is not iterable when the for-loop begins
- products must contain normalize_sku(product.sku)

## Validation Rules
- products must contain normalize_sku(product.sku)

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-productcatalog-get"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Retrieve a Product by normalizing the provided SKU and returning the mapped item from the products dictionary, raising KeyError if absent.

### SPL Content

```spl
[DEFINE_WORKER: "Retrieve a Product by normalizing the provided SKU and returning the mapped item from the products dictionary, raising KeyError if absent." get]
    [INPUTS]
        <REF> sku </REF>: string "The raw SKU string to be looked up."
        <REF> self.products </REF>: Mapping[str, Product] "Internal mapping from normalized SKU to Product used for lookup."
    [END_INPUTS]

    [OUTPUTS]
        <REF> product </REF>: Product "The Product associated with the normalized SKU."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Normalize the input SKU using <SPL>commerce_ops_demo.commerce_ops.catalog.normalize_sku</SPL>. RESULT normalized]
            [COMMAND Retrieve the product from self.products using the key normalized. RESULT product]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: If normalized is not present as a key in self.products.]
        [LOG "No product found for normalized SKU; raising KeyError."]
        [THROW KeyError "Raised with message 'unknown sku {normalized}' when the normalized SKU is absent from the products mapping."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get

Retrieve a Product by normalizing the provided SKU and returning the mapped item from the products dictionary, raising KeyError if absent.

## Inputs
- sku (string): The raw SKU string to be looked up.
- self.products (Mapping[str, Product]): Internal mapping from normalized SKU to Product used for lookup.

## Outputs
- product (Product): The Product associated with the normalized SKU.

## Main Effect
Retrieve the product from self.products using the key normalized.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.normalize_sku
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- If normalized is not present as a key in self.products.
- KeyError: Raised with message 'unknown sku {normalized}' when the normalized SKU is absent from the products mapping.
- invalid when normalized not in self.products
- raise KeyError(f"unknown sku {normalized}")

## Validation Rules
- invalid when normalized not in self.products

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/get.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-productcatalog-list-available"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Return products with positive stock, optionally filtered by a provided tag, sorted by SKU in ascending order.

### SPL Content

```spl
[DEFINE_WORKER: "Return products with positive stock, optionally filtered by a provided tag, sorted by SKU in ascending order." list_available]
    [INPUTS]
        <REF> tag </REF>: str "Optional tag used to filter products; if empty, no tag-based filtering is applied."
        <REF> self.products </REF>: Dict[Any, Product] "Internal mapping of products from which values are read and filtered."
    [END_INPUTS]

    [OUTPUTS]
        <REF> available_products </REF>: List[Product] "List of in-stock products, optionally filtered by tag, sorted by product.sku ascending."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Collect products with stock > 0 from self.products.values() RESULT values]
            [COMMAND If tag is non-empty, filter values to products where tag is in product.tags RESULT values]
            [COMMAND Sort values by product.sku in ascending order and produce final list RESULT available_products]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: tag is a non-empty string]
        [SEQUENTIAL_BLOCK]
            [COMMAND Filter current values to include only products whose tags contain the given tag RESULT values]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [ALTERNATIVE_FLOW: tag is an empty string]
        [SEQUENTIAL_BLOCK]
            [COMMAND Skip tag-based filtering and retain the current values RESULT values]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available

Return products with positive stock, optionally filtered by a provided tag, sorted by SKU in ascending order.

## Inputs
- tag (str): Optional tag used to filter products; if empty, no tag-based filtering is applied.
- self.products (Dict[Any, Product]): Internal mapping of products from which values are read and filtered.

## Outputs
- available_products (List[Product]): List of in-stock products, optionally filtered by tag, sorted by product.sku ascending.

## Main Effect
Sort values by product.sku in ascending order and produce final list

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `topic_mentions` <- `topic:configuration`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/list_available.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-productcatalog-release-items"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Iterates over provided cart items, fetching each product by SKU and invoking its release with the item quantity to update product state.

### SPL Content

```spl
[DEFINE_WORKER: "Iterates over provided cart items, fetching each product by SKU and invoking its release with the item quantity to update product state." release_items]
    [INPUTS]
        <REF> self </REF>: ProductCatalog "Catalog instance providing get(sku) to retrieve products and orchestrate releases."
        <REF> items </REF>: List[CartItem] "Iterable of CartItem objects, each with sku and qty to release."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return </REF>: None "This method returns None."
        <REF> side_effects </REF>: SideEffect "For each item, calls Product.release with the specified quantity, potentially mutating product inventory/reservation state."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND For each item in items, retrieve the corresponding product via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> using item.sku. RESULT product_for_item]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with item.qty to release the quantity for the retrieved product. RESULT product_state_updated]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: items is empty]
        [SEQUENTIAL_BLOCK]
            [COMMAND Detect that there are no items to process and perform no operations. RESULT no_action]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: items is not iterable and the for-loop cannot begin iteration]
        [LOG "Iteration over items failed due to a non-iterable input."]
        [THROW TypeError "Raised by Python when attempting to iterate over a non-iterable items argument."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: An element in items lacks sku or qty (e.g., item.sku or item.qty is missing)]
        [LOG "Access to item.sku or item.qty failed during loop processing."]
        [THROW AttributeError "Raised when item does not provide the expected attributes sku or qty."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> returns None or a non-product object lacking release]
        [LOG "Product retrieval returned an unexpected value, causing release invocation to fail."]
        [THROW AttributeError "Raised when the retrieved product is None or lacks a release method."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> or <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> raises an underlying domain/runtime exception]
        [LOG "Dependency call failed while fetching product or releasing quantity."]
        [THROW Exception "Propagated exception from get or release indicating retrieval or release failure."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items

Iterates over provided cart items, fetching each product by SKU and invoking its release with the item quantity to update product state.

## Inputs
- self (ProductCatalog): Catalog instance providing get(sku) to retrieve products and orchestrate releases.
- items (List[CartItem]): Iterable of CartItem objects, each with sku and qty to release.

## Outputs
- return (None): This method returns None.
- side_effects (SideEffect): For each item, calls Product.release with the specified quantity, potentially mutating product inventory/reservation state.

## Main Effect
Invoke <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with item.qty to release the quantity for the retrieved product.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get
- commerce_ops_demo.commerce_ops.models.Product.release
- commerce_ops_demo.commerce_ops.services.OrderService.cancel_order
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> or <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> raises an underlying domain/runtime exception
- <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> returns None or a non-product object lacking release
- An element in items lacks sku or qty (e.g., item.sku or item.qty is missing)
- AttributeError: Raised when item does not provide the expected attributes sku or qty.
- AttributeError: Raised when the retrieved product is None or lacks a release method.
- Exception: Propagated exception from get or release indicating retrieval or release failure.
- TypeError: Raised by Python when attempting to iterate over a non-iterable items argument.
- items is not iterable and the for-loop cannot begin iteration

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/release_items.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-productcatalog-reserve-items"></a>

## commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Validate each cart item, fetch its product, reserve requested quantities, accumulate reserved products, and return them; on any error, release previously reserved quantities and re-raise the exception.

### SPL Content

```spl
[DEFINE_WORKER: "Validate each cart item, fetch its product, reserve requested quantities, accumulate reserved products, and return them; on any error, release previously reserved quantities and re-raise the exception." reserve_items]
    [INPUTS]
        <REF> self </REF>: ProductCatalog "Catalog instance used to fetch products and manage reservations."
        <REF> items </REF>: List[CartItem] "List of cart items containing sku and qty to validate and reserve."
    [END_INPUTS]

    [OUTPUTS]
        <REF> reserved </REF>: List[Product] "Products for which the requested quantities were successfully reserved."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Initialize an empty list to track products that have been reserved. RESULT reserved initialized to []]
            [COMMAND For each item in items: validate the item; fetch its Product via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL> using item.sku; reserve the requested quantity via <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL> with item.qty; append the Product to the reserved list. RESULT reserved populated with Product objects corresponding to successfully reserved items]
            [COMMAND Return the list of reserved Product objects. RESULT reserved]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: Any Exception occurs during item validation, product retrieval via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL>, or reservation via <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL>.]
        [LOG "Exception information"]
        [THROW Exception "Before re-raising, release any previously reserved quantities by iterating zip(reserved, items) and calling <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with the original item.qty; then re-raise the original exception."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items

Validate each cart item, fetch its product, reserve requested quantities, accumulate reserved products, and return them; on any error, release previously reserved quantities and re-raise the exception.

## Inputs
- self (ProductCatalog): Catalog instance used to fetch products and manage reservations.
- items (List[CartItem]): List of cart items containing sku and qty to validate and reserve.

## Outputs
- reserved (List[Product]): Products for which the requested quantities were successfully reserved.

## Main Effect
Return the list of reserved Product objects.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get
- commerce_ops_demo.commerce_ops.models.Product.release
- commerce_ops_demo.commerce_ops.models.Product.reserve
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- reserved.append(product)

## Errors
- Any Exception occurs during item validation, product retrieval via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get</SPL>, or reservation via <SPL>commerce_ops_demo.commerce_ops.models.Product.reserve</SPL>.
- Exception: Before re-raising, release any previously reserved quantities by iterating zip(reserved, items) and calling <SPL>commerce_ops_demo.commerce_ops.models.Product.release</SPL> with the original item.qty; then re-raise the original exception.
- raise

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:external-integration`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/ProductCatalog/reserve_items.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`

---

<a id="method-commerce-ops-demo-commerce-ops-catalog-normalize-sku"></a>

## commerce_ops_demo.commerce_ops.catalog.normalize_sku

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`
- Tags: `method`, `public`

### Summary

Validates that a SKU string is present and returns it trimmed of whitespace and uppercased.

### SPL Content

```spl
[DEFINE_WORKER: "Validates that a SKU string is present and returns it trimmed of whitespace and uppercased." normalize_sku]
    [INPUTS]
        <REF> value </REF>: string "SKU input string to normalize."
    [END_INPUTS]

    [OUTPUTS]
        <REF> normalized_sku </REF>: string "Uppercased SKU string with leading and trailing whitespace removed."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Check that value is provided and not whitespace-only after trimming. RESULT validation_passed]
            [COMMAND Strip leading and trailing whitespace from value and convert to uppercase. RESULT normalized_sku]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: not value or not value.strip()]
        [LOG "Input validation failed: sku is required"]
        [THROW ValueError "sku is required"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: value is truthy and does not support strip()]
        [LOG "Attribute error during validation: input lacks strip method"]
        [THROW AttributeError "object has no attribute 'strip'"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: The stripped value does not support upper()]
        [LOG "Normalization failed: upper() not supported on resulting type"]
        [THROW AttributeError "object has no attribute 'upper'"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/catalog.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.catalog.normalize_sku

Validates that a SKU string is present and returns it trimmed of whitespace and uppercased.

## Inputs
- value (string): SKU input string to normalize.

## Outputs
- normalized_sku (string): Uppercased SKU string with leading and trailing whitespace removed.

## Main Effect
Strip leading and trailing whitespace from value and convert to uppercase.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- AttributeError: object has no attribute 'strip'
- AttributeError: object has no attribute 'upper'
- The stripped value does not support upper()
- ValueError: sku is required
- invalid when not value or not value.strip()
- not value or not value.strip()
- raise ValueError("sku is required")
- value is truthy and does not support strip()

## Validation Rules
- invalid when not value or not value.strip()

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/catalog.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `contains_symbol` <- `file:commerce_ops/catalog.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/catalog.py/normalize_sku.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.normalize_sku`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.catalog.normalize_sku`

---

<a id="method-commerce-ops-demo-commerce-ops-cli-build-demo-service"></a>

## commerce_ops_demo.commerce_ops.cli.build_demo_service

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `method`, `public`

### Summary

Constructs and returns a demo OrderService preconfigured with a sample catalog, pricing, and in-memory dependencies.

### SPL Content

```spl
[DEFINE_WORKER: "Constructs and returns a demo OrderService preconfigured with a sample catalog, pricing, and in-memory dependencies." build_demo_service]
    [INPUTS]
    [END_INPUTS]

    [OUTPUTS]
        <REF> order_service </REF>: OrderService "A configured demo OrderService instance built from a catalog of sample products, a pricing policy, a payment gateway, an order repository, and a notification service."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Construct Product('BOOK-1', 'Clean Architecture', 3500, 4, ['book']), Product('MUG-1', 'SPL Mug', 1800, 3, ['gift']), and Product('TEE-1', 'Compiler Tee', 2500, 1, ['gift']) via <SPL>commerce_ops_demo.commerce_ops.models.Product</SPL> and aggregate them into a list RESULT product_list]
            [COMMAND Create a product catalog from product_list via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog</SPL> RESULT catalog]
            [COMMAND Create a pricing policy with base 825 and discounts {'SAVE10': 1000, 'VIP5': 500} via <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy</SPL> RESULT pricing]
            [COMMAND Instantiate a payment gateway via <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway</SPL> RESULT payments]
            [COMMAND Instantiate an order repository via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository</SPL> RESULT repository]
            [COMMAND Instantiate a notification service via <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService</SPL> RESULT notifications]
            [COMMAND Construct an order service from catalog, pricing, payments, repository, and notifications via <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL> RESULT order_service]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: If any constructor call (<SPL>commerce_ops_demo.commerce_ops.models.Product</SPL>, <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog</SPL>, <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy</SPL>, <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway</SPL>, <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository</SPL>, <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService</SPL>, or <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL>) raises an error]
        [LOG "Constructor failure while building demo service; propagating exception"]
        [THROW Exception "Underlying constructor exception is not handled and propagates to the caller."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.cli.build_demo_service

Constructs and returns a demo OrderService preconfigured with a sample catalog, pricing, and in-memory dependencies.

## Inputs
- evidence: missing; confidence: not_available; source: static_analysis

## Outputs
- order_service (OrderService): A configured demo OrderService instance built from a catalog of sample products, a pricing policy, a payment gateway, an order repository, and a notification service.

## Main Effect
Construct an order service from catalog, pricing, payments, repository, and notifications via <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL>

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog
- commerce_ops_demo.commerce_ops.models.Product
- commerce_ops_demo.commerce_ops.notifications.NotificationService
- commerce_ops_demo.commerce_ops.payments.PaymentGateway
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy
- commerce_ops_demo.commerce_ops.repository.OrderRepository
- commerce_ops_demo.commerce_ops.services.OrderService
- commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Side Effects
- ProductCatalog(
        [
            Product("BOOK-1", "Clean Architecture", 3500, 4, ["book"]),
            Product("MUG-1", "SPL Mug", 1800, 3, ["gift"]),
            Product("TEE-1", "Compiler Tee", 2500, 1, ["gift"]),
        ]
    )
- order_service (OrderService): A configured demo OrderService instance built from a catalog of sample products, a pricing policy, a payment gateway, an order repository, and a notification service.

## Errors
- Exception: Underlying constructor exception is not handled and propagates to the caller.
- If any constructor call (<SPL>commerce_ops_demo.commerce_ops.models.Product</SPL>, <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog</SPL>, <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy</SPL>, <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway</SPL>, <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository</SPL>, <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService</SPL>, or <SPL>commerce_ops_demo.commerce_ops.services.OrderService</SPL>) raises an error

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/cli.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `calls` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `calls` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `calls` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `calls` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `calls` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `calls` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `contains_symbol` <- `file:commerce_ops/cli.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:configuration`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/cli.py/build_demo_service.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.build_demo_service`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.cli.build_demo_service`

---

<a id="method-commerce-ops-demo-commerce-ops-cli-main"></a>

## commerce_ops_demo.commerce_ops.cli.main

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.main`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.main`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `method`, `public`

### Summary

Calls <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> with fixed sample items and the 'SAVE10' code, then prints the returned value.

### SPL Content

```spl
[DEFINE_WORKER: "Calls <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> with fixed sample items and the 'SAVE10' code, then prints the returned value." main]
    [INPUTS]
    [END_INPUTS]

    [OUTPUTS]
        <REF> stdout </REF>: stdout "Printed representation of the value returned by <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> when invoked with the sample inputs."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> with list ['BOOK-1:1', 'MUG-1:2'] and discount code 'SAVE10'. RESULT checkout_result]
            [COMMAND Print checkout_result to standard output. RESULT stdout contains the textual representation of checkout_result]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.main`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.cli.main

Calls <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> with fixed sample items and the 'SAVE10' code, then prints the returned value.

## Inputs
- evidence: missing; confidence: not_available; source: static_analysis

## Outputs
- stdout (stdout): Printed representation of the value returned by <SPL>commerce_ops_demo.commerce_ops.cli.run_checkout_demo</SPL> when invoked with the sample inputs.

## Main Effect
Print checkout_result to standard output.

## Calls and Callers
- commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/cli.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `contains_symbol` <- `file:commerce_ops/cli.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/cli.py/main.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.main`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.cli.main`

---

<a id="method-commerce-ops-demo-commerce-ops-cli-parse-cart"></a>

## commerce_ops_demo.commerce_ops.cli.parse_cart

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.parse_cart`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `method`, `public`

### Summary

Parse a list of 'sku:qty' strings into CartItem objects by splitting on the first colon, stripping the SKU, converting quantity to int, and returning the list.

### SPL Content

```spl
[DEFINE_WORKER: "Parse a list of 'sku:qty' strings into CartItem objects by splitting on the first colon, stripping the SKU, converting quantity to int, and returning the list." parse_cart]
    [INPUTS]
        <REF> raw_items </REF>: List[str] "Iterable of strings in the format 'sku:qty' to parse into CartItem objects."
    [END_INPUTS]

    [OUTPUTS]
        <REF> items </REF>: List[CartItem] "List of CartItem objects constructed from the parsed input strings."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Initialize an empty list to collect parsed items. RESULT items]
            [COMMAND Iterate over raw_items; for each raw, split on ':' with maxsplit=1 and unpack into sku and qty_text. RESULT sku and qty_text for current element]
            [COMMAND Construct <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> with sku.strip() and int(qty_text) and append it to items. RESULT items updated with a new CartItem]
            [COMMAND Return the accumulated items list. RESULT List[CartItem]]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: raw.split(':', 1) does not produce exactly two parts for unpacking.]
        [LOG "Failed to unpack 'sku' and 'qty_text' from raw; expected 'sku:qty' format."]
        [THROW ValueError "Not enough values to unpack (expected 2)."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: qty_text cannot be converted to an integer via int(qty_text).]
        [LOG "Invalid quantity; int conversion failed for qty_text."]
        [THROW ValueError "Invalid literal for int() with base 10."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: raw is not a string-like object and does not support split(':', 1).]
        [LOG "raw element lacks a compatible split method."]
        [THROW AttributeError or TypeError "Object has no attribute 'split' or split invocation is not applicable."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: The constructor for <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> raises during instantiation.]
        [LOG "CartItem construction failed and is propagated."]
        [THROW Exception "Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> propagates."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.cli.parse_cart

Parse a list of 'sku:qty' strings into CartItem objects by splitting on the first colon, stripping the SKU, converting quantity to int, and returning the list.

## Inputs
- raw_items (List[str]): Iterable of strings in the format 'sku:qty' to parse into CartItem objects.

## Outputs
- items (List[CartItem]): List of CartItem objects constructed from the parsed input strings.

## Main Effect
Return the accumulated items list.

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.CartItem
- commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Side Effects
- items.append(CartItem(sku.strip(), int(qty_text)))

## Errors
- Exception: Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> propagates.
- The constructor for <SPL>commerce_ops_demo.commerce_ops.models.CartItem</SPL> raises during instantiation.
- ValueError: Invalid literal for int() with base 10.
- ValueError: Not enough values to unpack (expected 2).
- qty_text cannot be converted to an integer via int(qty_text).
- raw is not a string-like object and does not support split(':', 1).
- raw.split(':', 1) does not produce exactly two parts for unpacking.

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/cli.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `contains_symbol` <- `file:commerce_ops/cli.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/cli.py/parse_cart.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.parse_cart`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.cli.parse_cart`

---

<a id="method-commerce-ops-demo-commerce-ops-cli-run-checkout-demo"></a>

## commerce_ops_demo.commerce_ops.cli.run_checkout_demo

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `method`, `public`

### Summary

Builds a demo order service, constructs a fixed customer, parses raw item strings, performs checkout with an optional coupon, retrieves the customer’s order history, and returns a formatted summary string.

### SPL Content

```spl
[DEFINE_WORKER: "Builds a demo order service, constructs a fixed customer, parses raw item strings, performs checkout with an optional coupon, retrieves the customer’s order history, and returns a formatted summary string." run_checkout_demo]
    [INPUTS]
        <REF> raw_items </REF>: List[str] "List of raw item strings to parse into cart items."
        <REF> coupon </REF>: str "Optional coupon code applied during checkout; empty string when none."
    [END_INPUTS]

    [OUTPUTS]
        <REF> summary </REF>: str "Formatted summary string: 'created={order_id}; status={status}; history_count={count}'."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.cli.build_demo_service</SPL> to construct the order service instance. RESULT service]
            [COMMAND Instantiate <SPL>commerce_ops_demo.commerce_ops.models.Customer</SPL> with id 'cust-100', email 'reader@example.com', balance 20000, and tier 'vip'. RESULT customer]
            [COMMAND Parse raw cart items via <SPL>commerce_ops_demo.commerce_ops.cli.parse_cart</SPL>(raw_items). RESULT items]
            [COMMAND Perform checkout via <SPL>commerce_ops_demo.commerce_ops.services.OrderService.checkout</SPL>(customer, items, coupon). RESULT order]
            [COMMAND Fetch customer order history via <SPL>commerce_ops_demo.commerce_ops.services.OrderService.customer_history</SPL>(customer.customer_id). RESULT history]
            [COMMAND Format the return message as "created={order.order_id}; status={order.status}; history_count={len(history)}". RESULT summary]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: If <SPL>commerce_ops_demo.commerce_ops.cli.build_demo_service</SPL> fails to create the service instance.]
        [LOG "Failed to initialize demo order service."]
        [THROW Exception "Service initialization error."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: If <SPL>commerce_ops_demo.commerce_ops.cli.parse_cart</SPL>(raw_items) raises due to invalid or malformed input.]
        [LOG "Failed to parse raw_items into cart items."]
        [THROW Exception "Invalid cart items."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.checkout</SPL>(...) fails due to validation, inventory, or coupon issues.]
        [LOG "Checkout failed for given customer/items/coupon."]
        [THROW Exception "Checkout operation error."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.customer_history</SPL>(customer.customer_id) fails or customer_id is invalid.]
        [LOG "Retrieving customer history failed."]
        [THROW Exception "Customer history retrieval error."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: If order lacks order_id or status attributes when formatting the summary string.]
        [LOG "Order object missing expected attributes."]
        [THROW AttributeError "order.order_id or order.status not available."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.cli.run_checkout_demo

Builds a demo order service, constructs a fixed customer, parses raw item strings, performs checkout with an optional coupon, retrieves the customer’s order history, and returns a formatted summary string.

## Inputs
- raw_items (List[str]): List of raw item strings to parse into cart items.
- coupon (str): Optional coupon code applied during checkout; empty string when none.

## Outputs
- summary (str): Formatted summary string: 'created={order_id}; status={status}; history_count={count}'.

## Main Effect
Format the return message as "created={order.order_id}; status={order.status}; history_count={len(history)}".

## Calls and Callers
- commerce_ops_demo.commerce_ops.cli.build_demo_service
- commerce_ops_demo.commerce_ops.cli.parse_cart
- commerce_ops_demo.commerce_ops.models.Customer
- commerce_ops_demo.commerce_ops.services.OrderService.checkout
- commerce_ops_demo.commerce_ops.services.OrderService.customer_history
- commerce_ops_demo.commerce_ops.cli.main

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- AttributeError: order.order_id or order.status not available.
- Exception: Checkout operation error.
- Exception: Customer history retrieval error.
- Exception: Invalid cart items.
- Exception: Service initialization error.
- If <SPL>commerce_ops_demo.commerce_ops.cli.build_demo_service</SPL> fails to create the service instance.
- If <SPL>commerce_ops_demo.commerce_ops.cli.parse_cart</SPL>(raw_items) raises due to invalid or malformed input.
- If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.checkout</SPL>(...) fails due to validation, inventory, or coupon issues.
- If <SPL>commerce_ops_demo.commerce_ops.services.OrderService.customer_history</SPL>(customer.customer_id) fails or customer_id is invalid.
- If order lacks order_id or status attributes when formatting the summary string.

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/cli.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `calls` -> `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `calls` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `calls` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `calls` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.cli.main`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.main`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `contains_symbol` <- `file:commerce_ops/cli.py`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:configuration`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/cli.py/run_checkout_demo.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

---

<a id="method-commerce-ops-demo-commerce-ops-models-cartitem-validate"></a>

## commerce_ops_demo.commerce_ops.models.CartItem.validate

- Page ID: `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.CartItem.validate`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Validates that the instance has a truthy sku and a positive qty, raising ValueError if either check fails.

### SPL Content

```spl
[DEFINE_WORKER: "Validates that the instance has a truthy sku and a positive qty, raising ValueError if either check fails." validate]
    [INPUTS]
        <REF> self </REF>: object "Instance whose attributes are validated."
        <REF> self.sku </REF>: any "SKU value; must be truthy to pass validation."
        <REF> self.qty </REF>: number "Quantity value; must be greater than 0."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return </REF>: None "Returns None if both validations pass without raising an exception."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Check that self.sku is truthy to proceed with validation. RESULT sku_valid]
            [COMMAND Check that self.qty is greater than 0. RESULT qty_valid]
            [COMMAND Complete method execution without returning a value. RESULT None]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: not self.sku]
        [LOG "sku is required"]
        [THROW ValueError "Raised when sku is missing or falsy."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: self.qty <= 0]
        [LOG "qty must be positive"]
        [THROW ValueError "Raised when qty is non-positive."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.CartItem.validate

Validates that the instance has a truthy sku and a positive qty, raising ValueError if either check fails.

## Inputs
- self (object): Instance whose attributes are validated.
- self.sku (any): SKU value; must be truthy to pass validation.
- self.qty (number): Quantity value; must be greater than 0.

## Outputs
- return (None): Returns None if both validations pass without raising an exception.

## Main Effect
Complete method execution without returning a value.

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- ValueError: Raised when qty is non-positive.
- ValueError: Raised when sku is missing or falsy.
- invalid when not self.sku
- not self.sku
- raise ValueError("qty must be positive")
- raise ValueError("sku is required")
- self.qty <= 0
- self.qty > 0

## Validation Rules
- invalid when not self.sku
- self.qty > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/CartItem/validate.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.CartItem.validate`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.CartItem.validate`

---

<a id="method-commerce-ops-demo-commerce-ops-models-customer-can-spend"></a>

## commerce_ops_demo.commerce_ops.models.Customer.can_spend

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Returns True if the requested amount in cents is positive and does not exceed the current balance; otherwise returns False.

### SPL Content

```spl
[DEFINE_WORKER: "Returns True if the requested amount in cents is positive and does not exceed the current balance; otherwise returns False." can_spend]
    [INPUTS]
        <REF> amount_cents </REF>: int "Requested spend amount in cents."
        <REF> self.balance_cents </REF>: int "Current balance in cents read from instance state."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return_value </REF>: bool "True if amount_cents > 0 and balance_cents >= amount_cents; otherwise False."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Evaluate amount_cents > 0 and, if True, check self.balance_cents >= amount_cents using short-circuit AND semantics. RESULT is_spendable]
            [COMMAND Return the computed boolean result. RESULT return_value]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Customer.can_spend

Returns True if the requested amount in cents is positive and does not exceed the current balance; otherwise returns False.

## Inputs
- amount_cents (int): Requested spend amount in cents.
- self.balance_cents (int): Current balance in cents read from instance state.

## Outputs
- return_value (bool): True if amount_cents > 0 and balance_cents >= amount_cents; otherwise False.

## Main Effect
Return the computed boolean result.

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Customer.debit

## Side Effects
- return_value (bool): True if amount_cents > 0 and balance_cents >= amount_cents; otherwise False.

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Customer`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:external-integration`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Customer/can_spend.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Customer.can_spend`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Customer.can_spend`

---

<a id="method-commerce-ops-demo-commerce-ops-models-customer-credit"></a>

## commerce_ops_demo.commerce_ops.models.Customer.credit

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Customer.credit`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Credits a positive amount (in cents) to the balance by incrementing self.balance_cents and rejects non-positive values.

### SPL Content

```spl
[DEFINE_WORKER: "Credits a positive amount (in cents) to the balance by incrementing self.balance_cents and rejects non-positive values." credit]
    [INPUTS]
        <REF> amount_cents </REF>: int "Amount to credit, in cents; must be > 0."
        <REF> self.balance_cents </REF>: int "Current balance in cents read and incremented."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.balance_cents </REF>: int "Updated balance in cents after adding amount_cents."
        <REF> return </REF>: None "No return value."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Increment self.balance_cents by amount_cents RESULT self.balance_cents]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: amount_cents <= 0]
        [LOG "Exception information"]
        [THROW ValueError "Raised with message 'amount must be positive' when the amount is not greater than 0."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: amount_cents is None or non-numeric, making the '<=' comparison invalid]
        [LOG "Exception information"]
        [THROW TypeError "Implicitly raised by the comparison when amount_cents cannot be compared to 0."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Customer.credit

Credits a positive amount (in cents) to the balance by incrementing self.balance_cents and rejects non-positive values.

## Inputs
- amount_cents (int): Amount to credit, in cents; must be > 0.
- self.balance_cents (int): Current balance in cents read and incremented.

## Outputs
- self.balance_cents (int): Updated balance in cents after adding amount_cents.
- return (None): No return value.

## Main Effect
Increment self.balance_cents by amount_cents

## Calls and Callers
- commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund

## Side Effects
- mutates self.balance_cents
- self.balance_cents (int): Updated balance in cents after adding amount_cents.

## Errors
- TypeError: Implicitly raised by the comparison when amount_cents cannot be compared to 0.
- ValueError: Raised with message 'amount must be positive' when the amount is not greater than 0.
- amount_cents <= 0
- amount_cents > 0
- amount_cents is None or non-numeric, making the '<=' comparison invalid
- raise ValueError("amount must be positive")

## Validation Rules
- amount_cents > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Customer`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Customer/credit.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Customer.credit`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Customer.credit`

---

<a id="method-commerce-ops-demo-commerce-ops-models-customer-debit"></a>

## commerce_ops_demo.commerce_ops.models.Customer.debit

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Customer.debit`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Debits the customer's balance by amount_cents after verifying via <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>, otherwise raises ValueError for insufficient balance.

### SPL Content

```spl
[DEFINE_WORKER: "Debits the customer's balance by amount_cents after verifying via <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>, otherwise raises ValueError for insufficient balance." debit]
    [INPUTS]
        <REF> amount_cents </REF>: int "Amount in cents to deduct from the customer's balance."
        <REF> self.balance_cents </REF>: int (state) "Current stored balance in cents used to compute the new balance."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return </REF>: None "No return value on success."
        <REF> self.balance_cents </REF>: int (state) "Decremented by amount_cents when the debit succeeds."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents) to verify available balance RESULT is_allowed]
            [COMMAND Subtract amount_cents from self.balance_cents RESULT updated self.balance_cents]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: not <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents)]
        [LOG "customer has insufficient balance"]
        [THROW ValueError "Raised when the customer has insufficient balance."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: Exception raised by <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents)]
        [LOG "Propagate exception from can_spend"]
        [THROW Exception "Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL> propagates."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Customer.debit

Debits the customer's balance by amount_cents after verifying via <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>, otherwise raises ValueError for insufficient balance.

## Inputs
- amount_cents (int): Amount in cents to deduct from the customer's balance.

## Outputs
- return (None): No return value on success.

## Main Effect
Subtract amount_cents from self.balance_cents

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Customer.can_spend
- commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize

## Side Effects
- mutates self.balance_cents

## Errors
- Exception raised by <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents)
- Exception: Any exception raised by <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL> propagates.
- ValueError: Raised when the customer has insufficient balance.
- invalid when not self.can_spend(amount_cents)
- not <SPL>commerce_ops_demo.commerce_ops.models.Customer.can_spend</SPL>(amount_cents)
- raise ValueError("customer has insufficient balance")

## Validation Rules
- invalid when not self.can_spend(amount_cents)

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `calls` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Customer`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Customer/debit.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Customer.debit`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Customer.debit`

---

<a id="method-commerce-ops-demo-commerce-ops-models-order-add-event"></a>

## commerce_ops_demo.commerce_ops.models.Order.add_event

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Order.add_event`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Appends a new event dictionary with kind, detail, and a current UTC ISO timestamp to the instance's events list.

### SPL Content

```spl
[DEFINE_WORKER: "Appends a new event dictionary with kind, detail, and a current UTC ISO timestamp to the instance's events list." add_event]
    [INPUTS]
        <REF> kind </REF>: str "Event type identifier to record in the new event."
        <REF> detail </REF>: str "Event detail message or description."
        <REF> self.events </REF>: list "Existing events list on the instance that will be mutated via append."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return </REF>: None "No direct return value."
        <REF> self.events </REF>: list "Mutated by appending a new event dictionary containing kind, detail, and a UTC ISO timestamp."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Generate a UTC timestamp string using datetime.now(timezone.utc).isoformat(). RESULT timestamp string in ISO 8601 format]
            [COMMAND Construct an event dictionary with keys kind, detail, and timestamp. RESULT event dict with provided kind/detail and generated timestamp]
            [COMMAND Append the constructed event dictionary to self.events. RESULT self.events updated with the new event entry]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.events is None or lacks an append method (not a list-like).]
        [LOG "Cannot append event; self.events is not appendable."]
        [THROW AttributeError "self.events does not support append."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: datetime or timezone is not imported/defined when generating the timestamp.]
        [LOG "Time source unavailable: datetime or timezone is undefined."]
        [THROW NameError "datetime or timezone is not defined."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Order.add_event

Appends a new event dictionary with kind, detail, and a current UTC ISO timestamp to the instance's events list.

## Inputs
- kind (str): Event type identifier to record in the new event.
- detail (str): Event detail message or description.
- self.events (list): Existing events list on the instance that will be mutated via append.

## Outputs
- return (None): No direct return value.
- self.events (list): Mutated by appending a new event dictionary containing kind, detail, and a UTC ISO timestamp.

## Main Effect
Append the constructed event dictionary to self.events.

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Order.mark_cancelled
- commerce_ops_demo.commerce_ops.models.Order.mark_paid
- commerce_ops_demo.commerce_ops.services.OrderService._build_order

## Side Effects
- mutates self.events
- mutates self.events via append
- self.events (list): Mutated by appending a new event dictionary containing kind, detail, and a UTC ISO timestamp.
- self.events.append(
            {
                "kind": kind,
                "detail": detail,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        )

## Errors
- AttributeError: self.events does not support append.
- NameError: datetime or timezone is not defined.
- datetime or timezone is not imported/defined when generating the timestamp.
- self.events is None or lacks an append method (not a list-like).

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `calls` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Order`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Order/add_event.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Order.add_event`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Order.add_event`

---

<a id="method-commerce-ops-demo-commerce-ops-models-order-mark-cancelled"></a>

## commerce_ops_demo.commerce_ops.models.Order.mark_cancelled

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Cancels the order by setting its status to 'cancelled' and records the cancellation reason unless the order is paid, in which case it raises an error.

### SPL Content

```spl
[DEFINE_WORKER: "Cancels the order by setting its status to 'cancelled' and records the cancellation reason unless the order is paid, in which case it raises an error." mark_cancelled]
    [INPUTS]
        <REF> self </REF>: Order "Order instance whose status is read and updated, and which exposes add_event."
        <REF> reason </REF>: string "Human-readable explanation for the cancellation; passed to the event log."
        <REF> self.status </REF>: string "Current order status evaluated to guard against cancelling paid orders."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.status </REF>: state_write "Updated to 'cancelled' when the guard condition does not trigger."
        <REF> event </REF>: side_effect "Adds a 'cancelled' event with the provided reason via <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL>."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Set self.status to 'cancelled' RESULT status set to 'cancelled']
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> with arguments ('cancelled', reason) RESULT cancellation event recorded]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.status == 'paid']
        [LOG "paid orders cannot be cancelled here"]
        [THROW ValueError "paid orders cannot be cancelled here"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Order.mark_cancelled

Cancels the order by setting its status to 'cancelled' and records the cancellation reason unless the order is paid, in which case it raises an error.

## Inputs
- self (Order): Order instance whose status is read and updated, and which exposes add_event.
- reason (string): Human-readable explanation for the cancellation; passed to the event log.
- self.status (string): Current order status evaluated to guard against cancelling paid orders.

## Outputs
- self.status (state_write): Updated to 'cancelled' when the guard condition does not trigger.
- event (side_effect): Adds a 'cancelled' event with the provided reason via <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL>.

## Main Effect
Call <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> with arguments ('cancelled', reason)

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Order.add_event

## Side Effects
- mutates self.status
- self.status (state_write): Updated to 'cancelled' when the guard condition does not trigger.

## Errors
- ValueError: paid orders cannot be cancelled here
- invalid when self.status == "paid"
- raise ValueError("paid orders cannot be cancelled here")
- self.status == 'paid'

## Validation Rules
- invalid when self.status == "paid"

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Order`
- `topic_mentions` <- `topic:configuration`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_cancelled.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`

---

<a id="method-commerce-ops-demo-commerce-ops-models-order-mark-paid"></a>

## commerce_ops_demo.commerce_ops.models.Order.mark_paid

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Marks the order as paid by setting status to 'paid' and recording a 'paid' event with the provided payment_id when the current status is 'created'.

### SPL Content

```spl
[DEFINE_WORKER: "Marks the order as paid by setting status to 'paid' and recording a 'paid' event with the provided payment_id when the current status is 'created'." mark_paid]
    [INPUTS]
        <REF> payment_id </REF>: string "Identifier for the payment used to record the 'paid' event."
        <REF> self.status </REF>: string "Current order status; must be 'created' for the operation to proceed."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.status </REF>: string "Updated to 'paid' when the operation succeeds."
        <REF> event_record </REF>: side_effect "Calls <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> to record a 'paid' event with the given payment_id."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Verify the current status is exactly 'created'. RESULT Precondition satisfied; proceed with marking as paid.]
            [COMMAND Assign the literal 'paid' to self.status. RESULT Order status updated to 'paid'.]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> with event='paid' and the provided payment_id. RESULT 'paid' event recorded for the order with the payment identifier.]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.status != 'created']
        [LOG "Raising ValueError: only created orders can be marked paid"]
        [THROW ValueError "only created orders can be marked paid"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Order.mark_paid

Marks the order as paid by setting status to 'paid' and recording a 'paid' event with the provided payment_id when the current status is 'created'.

## Inputs
- payment_id (string): Identifier for the payment used to record the 'paid' event.
- self.status (string): Current order status; must be 'created' for the operation to proceed.

## Outputs
- self.status (string): Updated to 'paid' when the operation succeeds.
- event_record (side_effect): Calls <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> to record a 'paid' event with the given payment_id.

## Main Effect
Invoke <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> with event='paid' and the provided payment_id.

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Order.add_event
- commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- mutates self.status
- self.status (string): Updated to 'paid' when the operation succeeds.

## Errors
- ValueError: only created orders can be marked paid
- invalid when self.status != "created"
- raise ValueError("only created orders can be marked paid")
- self.status != 'created'

## Validation Rules
- invalid when self.status != "created"

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `calls` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Order`
- `topic_mentions` <- `topic:configuration`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Order/mark_paid.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Order.mark_paid`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Order.mark_paid`

---

<a id="method-commerce-ops-demo-commerce-ops-models-product-release"></a>

## commerce_ops_demo.commerce_ops.models.Product.release

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Product.release`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Product.release`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Increases the object's stock by the given quantity after validating the quantity is positive.

### SPL Content

```spl
[DEFINE_WORKER: "Increases the object's stock by the given quantity after validating the quantity is positive." release]
    [INPUTS]
        <REF> qty </REF>: int "Quantity to add; must be greater than 0."
        <REF> self.stock </REF>: int "Current stock value prior to update."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.stock </REF>: int "Updated stock after adding qty."
        <REF> return </REF>: None "No return value."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that qty is greater than 0 RESULT validation_passed]
            [COMMAND Add qty to self.stock RESULT updated_stock]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: qty <= 0]
        [LOG "Invalid quantity: qty must be positive"]
        [THROW ValueError "Raised when qty is not positive with message 'qty must be positive'."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Product.release`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Product.release

Increases the object's stock by the given quantity after validating the quantity is positive.

## Inputs
- qty (int): Quantity to add; must be greater than 0.
- self.stock (int): Current stock value prior to update.

## Outputs
- self.stock (int): Updated stock after adding qty.
- return (None): No return value.

## Main Effect
Add qty to self.stock

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items

## Side Effects
- mutates self.stock
- self.stock (int): Updated stock after adding qty.

## Errors
- ValueError: Raised when qty is not positive with message 'qty must be positive'.
- qty <= 0
- qty > 0
- raise ValueError("qty must be positive")

## Validation Rules
- qty > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Product`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Product/release.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Product.release`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Product.release`

---

<a id="method-commerce-ops-demo-commerce-ops-models-product-reserve"></a>

## commerce_ops_demo.commerce_ops.models.Product.reserve

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.models.Product.reserve`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`
- Tags: `method`, `public`

### Summary

Reserve a positive quantity from available stock by validating constraints and decrementing the stock value.

### SPL Content

```spl
[DEFINE_WORKER: "Reserve a positive quantity from available stock by validating constraints and decrementing the stock value." reserve]
    [INPUTS]
        <REF> qty </REF>: int "Requested quantity to reserve; must be > 0 and <= current stock."
        <REF> self.stock </REF>: int "Current available stock level read for validation and decremented on success."
        <REF> self.sku </REF>: str "SKU identifier used in error message when stock is insufficient."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.stock </REF>: int "Updated stock after reservation; reduced by qty when validation passes."
        <REF> return </REF>: None "No return value."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Verify that qty is positive (qty > 0). RESULT qty_validated]
            [COMMAND Verify that qty does not exceed available stock (qty <= self.stock). RESULT sufficiency_confirmed]
            [COMMAND Subtract qty from self.stock to reserve the items. RESULT self.stock updated]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: qty <= 0]
        [LOG "Quantity must be positive; reservation aborted."]
        [THROW ValueError "qty must be positive"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: qty > self.stock]
        [LOG "Insufficient stock for requested reservation; reservation aborted."]
        [THROW ValueError "not enough stock for {self.sku}"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/models.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.models.Product.reserve

Reserve a positive quantity from available stock by validating constraints and decrementing the stock value.

## Inputs
- qty (int): Requested quantity to reserve; must be > 0 and <= current stock.
- self.stock (int): Current available stock level read for validation and decremented on success.
- self.sku (str): SKU identifier used in error message when stock is insufficient.

## Outputs
- self.stock (int): Updated stock after reservation; reduced by qty when validation passes.
- return (None): No return value.

## Main Effect
Subtract qty from self.stock to reserve the items.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items

## Side Effects
- mutates self.stock
- self.stock (int): Updated stock after reservation; reduced by qty when validation passes.

## Errors
- ValueError: not enough stock for {self.sku}
- ValueError: qty must be positive
- invalid when qty > self.stock
- qty <= 0
- qty > 0
- qty > self.stock
- raise ValueError("qty must be positive")
- raise ValueError(f"not enough stock for {self.sku}")

## Validation Rules
- invalid when qty > self.stock
- qty > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `owned_by_file` -> `file:commerce_ops/models.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.models.Product`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/models.py/Product/reserve.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.models.Product.reserve`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.models.Product.reserve`

---

<a id="method-commerce-ops-demo-commerce-ops-notifications-notificationservice-init"></a>

## commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `method`, `public`

### Summary

Summarize method __init__ from static structure

### SPL Content

```spl
[DEFINE_WORKER: "Summarize method __init__ from static structure" __init__]
    [INPUTS]
        <REF> parameters </REF>: text "Function or method signature parameters"
    [END_INPUTS]

    [OUTPUTS]
        <REF> result </REF>: text "Return value or side effects inferred from static structure"
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Use static evidence and resolved calls (no resolved internal callees) to understand behavior RESULT result]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__

Summarize method __init__ from static structure

## Inputs
- parameters (text): Function or method signature parameters

## Outputs
- result (text): Return value or side effects inferred from static structure

## Main Effect
Use static evidence and resolved calls (no resolved internal callees) to understand behavior

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- mutates self.sent_messages

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `owned_by_file` -> `file:commerce_ops/notifications.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.notifications.NotificationService.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-notifications-notificationservice-send-low-stock-alert"></a>

## commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `method`, `public`

### Summary

Generates low-stock alert messages for products with stock less than or equal to a threshold (default 2), appends them to self.sent_messages, and returns the messages.

### SPL Content

```spl
[DEFINE_WORKER: "Generates low-stock alert messages for products with stock less than or equal to a threshold (default 2), appends them to self.sent_messages, and returns the messages." send_low_stock_alert]
    [INPUTS]
        <REF> products </REF>: List[Product] "Iterable of Product objects; each product is expected to have 'stock' and 'sku' attributes."
        <REF> threshold </REF>: int "Stock threshold; products with stock <= threshold are considered low. Defaults to 2."
    [END_INPUTS]

    [OUTPUTS]
        <REF> alerts </REF>: List[str] "List of alert message strings created for products whose stock <= threshold, returned in iteration order."
        <REF> self.sent_messages </REF>: side_effect "Each generated alert message is appended to self.sent_messages."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Initialize an empty collection to accumulate alert messages. RESULT alerts (empty list)]
            [COMMAND Iterate over products; for each product with product.stock <= threshold, format the alert string: "Low stock for {product.sku}: {product.stock}". RESULT alert (string) for each qualifying product]
            [COMMAND Append each created alert to self.sent_messages. RESULT self.sent_messages updated with new alert entries]
            [COMMAND Append each created alert to the alerts collection. RESULT alerts updated with new alert entries]
            [COMMAND Return the collected alerts. RESULT alerts (List[str])]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: product.stock > threshold during iteration]
        [SEQUENTIAL_BLOCK]
            [COMMAND Skip alert creation and do not append anything. RESULT No change to alerts or self.sent_messages for this product]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: products is None or not iterable when entering the loop]
        [LOG "Failed to iterate over 'products'."]
        [THROW TypeError "Object is not iterable."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: A product lacks the 'stock' attribute when evaluating the threshold condition]
        [LOG "Product missing 'stock' attribute during low-stock check."]
        [THROW AttributeError "Missing 'stock' attribute on product."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: product.stock cannot be compared to threshold (e.g., incompatible type)]
        [LOG "Type comparison failed between product.stock and threshold."]
        [THROW TypeError "Unsupported comparison between product.stock and threshold."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: A product lacks the 'sku' attribute when formatting the alert string]
        [LOG "Product missing 'sku' attribute during alert formatting."]
        [THROW AttributeError "Missing 'sku' attribute on product."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: self.sent_messages is missing or does not support append]
        [LOG "Cannot append alert to self.sent_messages."]
        [THROW AttributeError "Attribute 'sent_messages' missing or not appendable."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert

Generates low-stock alert messages for products with stock less than or equal to a threshold (default 2), appends them to self.sent_messages, and returns the messages.

## Inputs
- products (List[Product]): Iterable of Product objects; each product is expected to have 'stock' and 'sku' attributes.
- threshold (int): Stock threshold; products with stock <= threshold are considered low. Defaults to 2.

## Outputs
- alerts (List[str]): List of alert message strings created for products whose stock <= threshold, returned in iteration order.
- self.sent_messages (side_effect): Each generated alert message is appended to self.sent_messages.

## Main Effect
Return the collected alerts.

## Calls and Callers
- commerce_ops_demo.commerce_ops.services.OrderService._notify_customer

## Side Effects
- alerts.append(alert)
- mutates self.sent_messages
- mutates self.sent_messages via append
- self.sent_messages (side_effect): Each generated alert message is appended to self.sent_messages.
- self.sent_messages.append(alert)

## Errors
- A product lacks the 'sku' attribute when formatting the alert string
- A product lacks the 'stock' attribute when evaluating the threshold condition
- AttributeError: Attribute 'sent_messages' missing or not appendable.
- AttributeError: Missing 'sku' attribute on product.
- AttributeError: Missing 'stock' attribute on product.
- TypeError: Object is not iterable.
- TypeError: Unsupported comparison between product.stock and threshold.
- product.stock cannot be compared to threshold (e.g., incompatible type)
- products is None or not iterable when entering the loop
- self.sent_messages is missing or does not support append

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `owned_by_file` -> `file:commerce_ops/notifications.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_low_stock_alert.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`

---

<a id="method-commerce-ops-demo-commerce-ops-notifications-notificationservice-send-receipt"></a>

## commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `method`, `public`

### Summary

Compose a receipt message for a customer's order, append it to sent_messages, and return the message string.

### SPL Content

```spl
[DEFINE_WORKER: "Compose a receipt message for a customer's order, append it to sent_messages, and return the message string." send_receipt]
    [INPUTS]
        <REF> self </REF>: object "Object instance that must provide a sent_messages list-like attribute to append the message."
        <REF> customer </REF>: Customer "Customer object providing email used in the receipt message."
        <REF> order </REF>: Order "Order object providing order_id and total_cents used to compose and format the receipt."
    [END_INPUTS]

    [OUTPUTS]
        <REF> message </REF>: str "The composed receipt message string that is returned."
        <REF> self.sent_messages </REF>: List[str] "Updated list after appending the composed receipt message."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Construct receipt message string using customer.email, order.order_id, and <SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL>(order.total_cents). RESULT message]
            [COMMAND Append message to self.sent_messages. RESULT self.sent_messages]
            [COMMAND Return the composed message. RESULT message]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.]
        [LOG "Attribute access failed while composing the receipt message."]
        [THROW AttributeError "Raised when expected attributes are missing on customer or order."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.]
        [LOG "Formatting total_cents failed during receipt message construction."]
        [THROW Exception "Propagated exception from format_currency when formatting the total."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: self.sent_messages is missing or not list-like, causing append to fail.]
        [LOG "Failed to append the message to self.sent_messages."]
        [THROW AttributeError or TypeError "Raised when sent_messages attribute is absent or does not support append."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt

Compose a receipt message for a customer's order, append it to sent_messages, and return the message string.

## Inputs
- self (object): Object instance that must provide a sent_messages list-like attribute to append the message.
- customer (Customer): Customer object providing email used in the receipt message.
- order (Order): Order object providing order_id and total_cents used to compose and format the receipt.

## Outputs
- message (str): The composed receipt message string that is returned.
- self.sent_messages (List[str]): Updated list after appending the composed receipt message.

## Main Effect
Return the composed message.

## Calls and Callers
- commerce_ops_demo.commerce_ops.notifications.format_currency
- commerce_ops_demo.commerce_ops.services.OrderService._notify_customer

## Side Effects
- mutates self.sent_messages
- mutates self.sent_messages via append
- self.sent_messages (List[str]): Updated list after appending the composed receipt message.
- self.sent_messages.append(message)

## Errors
- <SPL>commerce_ops_demo.commerce_ops.notifications.format_currency</SPL> raises due to invalid order.total_cents or internal formatting error.
- AttributeError: Raised when expected attributes are missing on customer or order.
- Exception: Propagated exception from format_currency when formatting the total.
- customer or order lacks required attributes (email, order_id, total_cents) or is None, causing attribute access during message construction to fail.
- self.sent_messages is missing or not list-like, causing append to fail.

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`
- `owned_by_file` -> `file:commerce_ops/notifications.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.notifications.NotificationService`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/NotificationService/send_receipt.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`

---

<a id="method-commerce-ops-demo-commerce-ops-notifications-format-currency"></a>

## commerce_ops_demo.commerce_ops.notifications.format_currency

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- Type: `entity` / `function`
- Qualified name: `commerce_ops_demo.commerce_ops.notifications.format_currency`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`
- Tags: `method`, `public`

### Summary

Formats a non-negative cent amount into a dollar string with two decimal places, raising ValueError for negative input.

### SPL Content

```spl
[DEFINE_WORKER: "Formats a non-negative cent amount into a dollar string with two decimal places, raising ValueError for negative input." format_currency]
    [INPUTS]
        <REF> cents </REF>: int "Amount in cents to format; must be non-negative."
    [END_INPUTS]

    [OUTPUTS]
        <REF> formatted_currency </REF>: str "Dollar-formatted string with two decimal places (e.g., '$12.34')."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Divide cents by 100 to compute the dollar amount as a float. RESULT dollar_value]
            [COMMAND Format the dollar amount with two decimal places and prefix with '$'. RESULT formatted_currency]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: cents < 0]
        [LOG "Exception information"]
        [THROW ValueError "currency value cannot be negative"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- Entity kind: `function`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/notifications.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.notifications.format_currency

Formats a non-negative cent amount into a dollar string with two decimal places, raising ValueError for negative input.

## Inputs
- cents (int): Amount in cents to format; must be non-negative.

## Outputs
- formatted_currency (str): Dollar-formatted string with two decimal places (e.g., '$12.34').

## Main Effect
Format the dollar amount with two decimal places and prefix with '$'.

## Calls and Callers
- commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- ValueError: currency value cannot be negative
- cents < 0
- cents > 0
- raise ValueError("currency value cannot be negative")

## Validation Rules
- cents > 0

### Outgoing Links

- `owned_by_file` -> `file:commerce_ops/notifications.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `contains_symbol` <- `file:commerce_ops/notifications.py`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/notifications.py/format_currency.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.notifications.format_currency`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.notifications.format_currency`

---

<a id="method-commerce-ops-demo-commerce-ops-payments-paymentgateway-init"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `method`, `public`

### Summary

Initialize the instance by setting the payment provider and zeroing authorized and refunded totals.

### SPL Content

```spl
[DEFINE_WORKER: "Initialize the instance by setting the payment provider and zeroing authorized and refunded totals." __init__]
    [INPUTS]
        <REF> self </REF>: object "The instance being initialized."
        <REF> provider </REF>: str "Payment provider identifier; defaults to 'internal-wallet'."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.provider </REF>: str "Instance attribute set to the provided provider value."
        <REF> self.authorized_total_cents </REF>: int "Instance attribute initialized to 0 representing total authorized amount in cents."
        <REF> self.refunded_total_cents </REF>: int "Instance attribute initialized to 0 representing total refunded amount in cents."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Assign provider to instance attribute RESULT self.provider]
            [COMMAND Initialize authorized_total_cents to 0 RESULT self.authorized_total_cents]
            [COMMAND Initialize refunded_total_cents to 0 RESULT self.refunded_total_cents]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__

Initialize the instance by setting the payment provider and zeroing authorized and refunded totals.

## Inputs
- self (object): The instance being initialized.
- provider (str): Payment provider identifier; defaults to 'internal-wallet'.

## Outputs
- self.provider (str): Instance attribute set to the provided provider value.
- self.authorized_total_cents (int): Instance attribute initialized to 0 representing total authorized amount in cents.
- self.refunded_total_cents (int): Instance attribute initialized to 0 representing total refunded amount in cents.

## Main Effect
Initialize refunded_total_cents to 0

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- mutates self.authorized_total_cents
- mutates self.provider
- mutates self.refunded_total_cents
- self.authorized_total_cents (int): Instance attribute initialized to 0 representing total authorized amount in cents.
- self.provider (str): Instance attribute set to the provided provider value.
- self.refunded_total_cents (int): Instance attribute initialized to 0 representing total refunded amount in cents.

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `owned_by_file` -> `file:commerce_ops/payments.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `topic_mentions` <- `topic:authentication`
- `topic_mentions` <- `topic:configuration`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-payments-paymentgateway-authorize"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `method`, `public`

### Summary

Authorize a payment by validating the amount, debiting the customer, updating the authorized total, and returning a new payment receipt.

### SPL Content

```spl
[DEFINE_WORKER: "Authorize a payment by validating the amount, debiting the customer, updating the authorized total, and returning a new payment receipt." authorize]
    [INPUTS]
        <REF> customer </REF>: Customer "Customer account to be debited; must support <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>."
        <REF> amount_cents </REF>: int "Positive amount in cents to authorize."
        <REF> self.provider </REF>: Provider "Provider identifier read from instance state and included in <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>."
    [END_INPUTS]

    [OUTPUTS]
        <REF> receipt </REF>: PaymentReceipt "A new <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> constructed with a generated UUID string, amount_cents, and self.provider."
        <REF> self.authorized_total_cents </REF>: int "Instance state incremented by amount_cents."
        <REF> customer_balance </REF>: mutation "Side effect: customer.debit(amount_cents) invoked to reduce available funds on the customer."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that amount_cents is greater than 0. RESULT validated_amount]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> on customer with amount_cents. RESULT debited_customer]
            [COMMAND Add amount_cents to self.authorized_total_cents. RESULT updated_authorized_total_cents]
            [COMMAND Generate a new UUID string via uuid4() and construct <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> with (id, amount_cents, self.provider); return it. RESULT receipt]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: amount_cents <= 0]
        [LOG "Invalid authorization amount: non-positive value."]
        [THROW <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL> "Raised with message 'amount must be positive' when the amount is not greater than zero."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> raises ValueError]
        [LOG "Customer debit failed with ValueError; rewrapping in PaymentError."]
        [THROW <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL> "Re-raised as PaymentError with the original ValueError message."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize

Authorize a payment by validating the amount, debiting the customer, updating the authorized total, and returning a new payment receipt.

## Inputs
- customer (Customer): Customer account to be debited; must support <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL>.
- amount_cents (int): Positive amount in cents to authorize.
- self.provider (Provider): Provider identifier read from instance state and included in <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL>.

## Outputs
- receipt (PaymentReceipt): A new <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> constructed with a generated UUID string, amount_cents, and self.provider.
- self.authorized_total_cents (int): Instance state incremented by amount_cents.
- customer_balance (mutation): Side effect: customer.debit(amount_cents) invoked to reduce available funds on the customer.

## Main Effect
Generate a new UUID string via uuid4() and construct <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> with (id, amount_cents, self.provider); return it.

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Customer.debit
- commerce_ops_demo.commerce_ops.payments.PaymentError
- commerce_ops_demo.commerce_ops.payments.PaymentReceipt
- commerce_ops_demo.commerce_ops.services.OrderService._charge

## Side Effects
- customer_balance (mutation): Side effect: customer.debit(amount_cents) invoked to reduce available funds on the customer.
- mutates self.authorized_total_cents
- receipt (PaymentReceipt): A new <SPL>commerce_ops_demo.commerce_ops.payments.PaymentReceipt</SPL> constructed with a generated UUID string, amount_cents, and self.provider.
- self.authorized_total_cents (int): Instance state incremented by amount_cents.

## Errors
- <SPL>commerce_ops_demo.commerce_ops.models.Customer.debit</SPL> raises ValueError
- <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: Raised with message 'amount must be positive' when the amount is not greater than zero.
- <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: Re-raised as PaymentError with the original ValueError message.
- amount_cents <= 0
- amount_cents > 0
- raise PaymentError("amount must be positive")
- raise PaymentError(str(exc)) from exc

## Validation Rules
- amount_cents > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `owned_by_file` -> `file:commerce_ops/payments.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `calls` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- `calls` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:authentication`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/authorize.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`

---

<a id="method-commerce-ops-demo-commerce-ops-payments-paymentgateway-refund"></a>

## commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`
- Tags: `method`, `public`

### Summary

Validates a positive receipt amount, credits the customer by that amount, and increments the instance's refunded total.

### SPL Content

```spl
[DEFINE_WORKER: "Validates a positive receipt amount, credits the customer by that amount, and increments the instance's refunded total." refund]
    [INPUTS]
        <REF> self </REF>: object "Instance with refunded_total_cents attribute to update."
        <REF> customer </REF>: Customer "Customer to credit via credit(amount_cents)."
        <REF> receipt </REF>: PaymentReceipt "Payment receipt providing amount_cents to refund."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return </REF>: None "No return value."
        <REF> customer </REF>: state_mutation "Credited by receipt.amount_cents via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>."
        <REF> self.refunded_total_cents </REF>: int "Incremented by receipt.amount_cents."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that receipt.amount_cents is greater than 0 RESULT Proceed with refund processing when amount_cents > 0]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL> on customer with receipt.amount_cents RESULT Customer is credited by receipt.amount_cents]
            [COMMAND Increment self.refunded_total_cents by receipt.amount_cents RESULT self.refunded_total_cents updated to include the refunded amount]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: receipt.amount_cents <= 0]
        [LOG "Exception information"]
        [THROW <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL> "Raised with message 'receipt amount must be positive' to enforce a positive refund amount."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/payments.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund

Validates a positive receipt amount, credits the customer by that amount, and increments the instance's refunded total.

## Inputs
- self (object): Instance with refunded_total_cents attribute to update.
- customer (Customer): Customer to credit via credit(amount_cents).
- receipt (PaymentReceipt): Payment receipt providing amount_cents to refund.

## Outputs
- return (None): No return value.
- customer (state_mutation): Credited by receipt.amount_cents via <SPL>commerce_ops_demo.commerce_ops.models.Customer.credit</SPL>.
- self.refunded_total_cents (int): Incremented by receipt.amount_cents.

## Main Effect
Increment self.refunded_total_cents by receipt.amount_cents

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Customer.credit
- commerce_ops_demo.commerce_ops.payments.PaymentError

## Side Effects
- mutates self.refunded_total_cents
- self.refunded_total_cents (int): Incremented by receipt.amount_cents.

## Errors
- <SPL>commerce_ops_demo.commerce_ops.payments.PaymentError</SPL>: Raised with message 'receipt amount must be positive' to enforce a positive refund amount.
- raise PaymentError("receipt amount must be positive")
- receipt.amount_cents <= 0
- receipt.amount_cents > 0

## Validation Rules
- receipt.amount_cents > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `owned_by_file` -> `file:commerce_ops/payments.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `calls` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentError`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/payments.py/PaymentGateway/refund.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`

---

<a id="method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-init"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `method`, `public`

### Summary

Initialize the instance by validating that tax_rate_bps is non-negative and storing tax_rate_bps and a coupons dict with uppercase keys.

### SPL Content

```spl
[DEFINE_WORKER: "Initialize the instance by validating that tax_rate_bps is non-negative and storing tax_rate_bps and a coupons dict with uppercase keys." __init__]
    [INPUTS]
        <REF> tax_rate_bps </REF>: int "Tax rate in basis points; must be >= 0."
        <REF> coupons </REF>: Dict[str, int] "Mapping of coupon code strings to integer values; codes will be normalized to uppercase."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.tax_rate_bps </REF>: int attribute "Instance attribute set to the provided tax_rate_bps."
        <REF> self.coupons </REF>: dict[str, int] attribute "New dictionary with coupon codes uppercased as keys and original values; later entries overwrite earlier ones if uppercase keys collide."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that tax_rate_bps is not negative (tax_rate_bps >= 0). RESULT validated_tax_rate]
            [COMMAND Assign the validated tax_rate_bps to the instance attribute. RESULT self.tax_rate_bps set]
            [COMMAND Construct a new dict by iterating coupons.items() and mapping each code.upper() to its value; values are preserved by reference and later keys overwrite earlier ones if uppercase-normalized keys collide. RESULT normalized_coupons]
            [COMMAND Assign the normalized coupon mapping to the instance attribute. RESULT self.coupons set]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: tax_rate_bps < 0]
        [LOG "tax rate cannot be negative"]
        [THROW ValueError "Raised when a negative tax_rate_bps is provided."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: coupons does not provide an .items() method (non-mapping or None)]
        [LOG "coupons must be mapping-like; .items() is required"]
        [THROW AttributeError "Attempted to call .items() on a non-mapping coupons argument."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: a coupon code from coupons.items() is not a string (lacks .upper())]
        [LOG "coupon code must be string-like to support .upper()"]
        [THROW AttributeError "Non-string coupon code encountered during key normalization with .upper()."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__

Initialize the instance by validating that tax_rate_bps is non-negative and storing tax_rate_bps and a coupons dict with uppercase keys.

## Inputs
- tax_rate_bps (int): Tax rate in basis points; must be >= 0.
- coupons (Dict[str, int]): Mapping of coupon code strings to integer values; codes will be normalized to uppercase.

## Outputs
- evidence: missing; confidence: not_available; source: static_analysis

## Main Effect
Assign the normalized coupon mapping to the instance attribute.

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- mutates self.coupons
- mutates self.tax_rate_bps

## Errors
- AttributeError: Attempted to call .items() on a non-mapping coupons argument.
- AttributeError: Non-string coupon code encountered during key normalization with .upper().
- ValueError: Raised when a negative tax_rate_bps is provided.
- a coupon code from coupons.items() is not a string (lacks .upper())
- coupons does not provide an .items() method (non-mapping or None)
- raise ValueError("tax rate cannot be negative")
- tax_rate_bps < 0
- tax_rate_bps > 0

## Validation Rules
- tax_rate_bps > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `owned_by_file` -> `file:commerce_ops/pricing.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-apply-coupon"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `method`, `public`

### Summary

Computes the discount in cents from a coupon code, adds a 500-cent VIP bonus when applicable, and returns the discount capped to the subtotal.

### SPL Content

```spl
[DEFINE_WORKER: "Computes the discount in cents from a coupon code, adds a 500-cent VIP bonus when applicable, and returns the discount capped to the subtotal." apply_coupon]
    [INPUTS]
        <REF> self </REF>: object "Instance providing the coupons mapping used for lookup."
        <REF> self.coupons </REF>: mapping[str, int] "Mapping of uppercase coupon codes to discount amounts in cents."
        <REF> customer </REF>: Customer "Customer whose tier may trigger a VIP bonus."
        <REF> subtotal_cents </REF>: int "Subtotal amount in cents used to cap the discount."
        <REF> coupon </REF>: str "Coupon code string; empty or falsy means no discount."
    [END_INPUTS]

    [OUTPUTS]
        <REF> applied_discount_cents </REF>: int "Final discount in cents to apply, 0 if no coupon, includes VIP bonus when applicable and is capped to the subtotal."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Convert coupon to uppercase string RESULT code]
            [COMMAND Verify code exists in self.coupons RESULT valid_code]
            [COMMAND Retrieve base discount in cents from self.coupons[code] RESULT discount]
            [COMMAND If customer.tier == 'vip', add 500 to discount; otherwise leave unchanged RESULT discount]
            [COMMAND Return the minimum of discount and subtotal_cents RESULT applied_discount_cents]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: coupon is empty or falsy]
        [SEQUENTIAL_BLOCK]
            [COMMAND Return 0 (no coupon provided) RESULT applied_discount_cents = 0]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [ALTERNATIVE_FLOW: customer.tier == 'vip']
        [SEQUENTIAL_BLOCK]
            [COMMAND Increase discount by 500 before capping RESULT discount]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: Uppercased code not present in self.coupons]
        [LOG "coupon is not supported"]
        [THROW ValueError "coupon is not supported"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: coupon is truthy but lacks a callable upper() method during normalization]
        [LOG "Failed to uppercase coupon"]
        [THROW AttributeError "coupon.upper() is unavailable or not callable"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: upper() call on coupon fails due to incompatible type]
        [LOG "Type error during coupon normalization"]
        [THROW TypeError "upper() call failed on coupon"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon

Computes the discount in cents from a coupon code, adds a 500-cent VIP bonus when applicable, and returns the discount capped to the subtotal.

## Inputs
- self (object): Instance providing the coupons mapping used for lookup.
- self.coupons (mapping[str, int]): Mapping of uppercase coupon codes to discount amounts in cents.
- customer (Customer): Customer whose tier may trigger a VIP bonus.
- subtotal_cents (int): Subtotal amount in cents used to cap the discount.
- coupon (str): Coupon code string; empty or falsy means no discount.

## Outputs
- applied_discount_cents (int): Final discount in cents to apply, 0 if no coupon, includes VIP bonus when applicable and is capped to the subtotal.

## Main Effect
Return the minimum of discount and subtotal_cents

## Calls and Callers
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- AttributeError: coupon.upper() is unavailable or not callable
- TypeError: upper() call failed on coupon
- Uppercased code not present in self.coupons
- ValueError: coupon is not supported
- coupon is truthy but lacks a callable upper() method during normalization
- invalid when code not in self.coupons
- raise ValueError("coupon is not supported")
- upper() call on coupon fails due to incompatible type

## Validation Rules
- invalid when code not in self.coupons

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `owned_by_file` -> `file:commerce_ops/pricing.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/apply_coupon.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`

---

<a id="method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-calculate-subtotal"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `method`, `public`

### Summary

Compute the cart subtotal in cents by mapping product SKUs to prices, validating quantities and prices, and summing price * quantity for each item.

### SPL Content

```spl
[DEFINE_WORKER: "Compute the cart subtotal in cents by mapping product SKUs to prices, validating quantities and prices, and summing price * quantity for each item." calculate_subtotal]
    [INPUTS]
        <REF> self </REF>: object "Instance of the containing class; not used in the computation."
        <REF> items </REF>: List[CartItem] "Iterable of cart items, each with sku and qty to be validated and priced."
        <REF> products </REF>: List[Product] "Iterable of products, each with sku and price_cents used to build a price lookup."
    [END_INPUTS]

    [OUTPUTS]
        <REF> subtotal </REF>: int "Total price in cents calculated as the sum of price_cents * qty for all valid items."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Build a dict mapping each product.sku to product.price_cents from products RESULT price_by_sku]
            [COMMAND Initialize subtotal accumulator to 0 RESULT subtotal]
            [COMMAND Iterate over items; for each item validate item.qty > 0, lookup price = price_by_sku[item.sku.upper()], validate price > 0, and add price * item.qty to subtotal RESULT subtotal]
            [COMMAND Return the accumulated subtotal RESULT subtotal]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: During iteration, item.qty <= 0]
        [LOG "Invalid quantity encountered for an item"]
        [THROW ValueError "qty must be positive"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: During iteration, fetched price <= 0]
        [LOG "Invalid product price encountered"]
        [THROW ValueError "price_cents must be positive"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: During lookup, item.sku.upper() key is not present in price_by_sku]
        [LOG "SKU not found in product price mapping"]
        [THROW KeyError "SKU not found in price_by_sku when using item.sku.upper()"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: During iteration, item lacks required attributes or item.sku is not a string supporting upper()]
        [LOG "Item has missing or invalid attributes (sku or qty)"]
        [THROW AttributeError "Missing attribute (sku or qty) or sku does not support upper()"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: During comparison or multiplication, qty or price is non-numeric]
        [LOG "Type mismatch when validating or accumulating subtotal"]
        [THROW TypeError "Non-numeric qty or price caused comparison or arithmetic to fail"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal

Compute the cart subtotal in cents by mapping product SKUs to prices, validating quantities and prices, and summing price * quantity for each item.

## Inputs
- self (object): Instance of the containing class; not used in the computation.
- items (List[CartItem]): Iterable of cart items, each with sku and qty to be validated and priced.
- products (List[Product]): Iterable of products, each with sku and price_cents used to build a price lookup.

## Outputs
- subtotal (int): Total price in cents calculated as the sum of price_cents * qty for all valid items.

## Main Effect
Return the accumulated subtotal

## Calls and Callers
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- AttributeError: Missing attribute (sku or qty) or sku does not support upper()
- During comparison or multiplication, qty or price is non-numeric
- During iteration, fetched price <= 0
- During iteration, item lacks required attributes or item.sku is not a string supporting upper()
- During iteration, item.qty <= 0
- During lookup, item.sku.upper() key is not present in price_by_sku
- KeyError: SKU not found in price_by_sku when using item.sku.upper()
- TypeError: Non-numeric qty or price caused comparison or arithmetic to fail
- ValueError: price_cents must be positive
- ValueError: qty must be positive
- item.qty > 0
- item.sku.upper() > 0
- raise ValueError("price_cents must be positive")
- raise ValueError("qty must be positive")

## Validation Rules
- item.qty > 0
- item.sku.upper() > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `owned_by_file` -> `file:commerce_ops/pricing.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_subtotal.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`

---

<a id="method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-calculate-tax"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `method`, `public`

### Summary

Computes tax in cents from a non-negative taxable amount using self.tax_rate_bps (basis points) with integer floor division by 10000.

### SPL Content

```spl
[DEFINE_WORKER: "Computes tax in cents from a non-negative taxable amount using self.tax_rate_bps (basis points) with integer floor division by 10000." calculate_tax]
    [INPUTS]
        <REF> taxable_cents </REF>: int "Taxable amount in cents; must be >= 0."
        <REF> self.tax_rate_bps </REF>: int "Tax rate in basis points (hundredths of a percent) read from instance state."
    [END_INPUTS]

    [OUTPUTS]
        <REF> tax_cents </REF>: int "Computed tax in cents using (taxable_cents * self.tax_rate_bps) // 10000; fractional part is truncated."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that taxable_cents is not negative; continue if taxable_cents >= 0. RESULT validation_passed]
            [COMMAND Compute tax as (taxable_cents * self.tax_rate_bps) // 10000 using integer floor division. RESULT tax_cents]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: taxable_cents < 0]
        [LOG "Negative taxable amount encountered; raising ValueError."]
        [THROW ValueError "taxable amount cannot be negative"]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: Non-numeric or non-comparable inputs during comparison or arithmetic (e.g., taxable_cents or self.tax_rate_bps is not an int).]
        [LOG "Type error during comparison or arithmetic while computing tax."]
        [THROW TypeError "Raised by Python when comparing or multiplying non-numeric or incompatible types."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax

Computes tax in cents from a non-negative taxable amount using self.tax_rate_bps (basis points) with integer floor division by 10000.

## Inputs
- taxable_cents (int): Taxable amount in cents; must be >= 0.
- self.tax_rate_bps (int): Tax rate in basis points (hundredths of a percent) read from instance state.

## Outputs
- tax_cents (int): Computed tax in cents using (taxable_cents * self.tax_rate_bps) // 10000; fractional part is truncated.

## Main Effect
Compute tax as (taxable_cents * self.tax_rate_bps) // 10000 using integer floor division.

## Calls and Callers
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote

## Side Effects
- tax_cents (int): Computed tax in cents using (taxable_cents * self.tax_rate_bps) // 10000; fractional part is truncated.

## Errors
- Non-numeric or non-comparable inputs during comparison or arithmetic (e.g., taxable_cents or self.tax_rate_bps is not an int).
- TypeError: Raised by Python when comparing or multiplying non-numeric or incompatible types.
- ValueError: taxable amount cannot be negative
- raise ValueError("taxable amount cannot be negative")
- taxable_cents < 0
- taxable_cents > 0

## Validation Rules
- taxable_cents > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `owned_by_file` -> `file:commerce_ops/pricing.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/calculate_tax.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`

---

<a id="method-commerce-ops-demo-commerce-ops-pricing-pricingpolicy-quote"></a>

## commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`
- Tags: `method`, `public`

### Summary

Computes a customer's cart price quote by calculating subtotal, applying a coupon, clamping taxable to non-negative, computing tax, validating total is positive, and returning a PriceQuote with an uppercased coupon code.

### SPL Content

```spl
[DEFINE_WORKER: "Computes a customer's cart price quote by calculating subtotal, applying a coupon, clamping taxable to non-negative, computing tax, validating total is positive, and returning a PriceQuote with an uppercased coupon code." quote]
    [INPUTS]
        <REF> self </REF>: PricingPolicy "Instance providing pricing calculations for subtotal, coupon application, and tax."
        <REF> customer </REF>: Customer "Customer for whom discounts may apply."
        <REF> items </REF>: List[CartItem] "Shopping cart items to be priced."
        <REF> products </REF>: List[Product] "Product catalog data used to compute item prices."
        <REF> coupon </REF>: str "Optional coupon code used to compute a discount; defaults to empty string."
    [END_INPUTS]

    [OUTPUTS]
        <REF> price_quote </REF>: PriceQuote "Price breakdown including subtotal, discount, tax, total, and the coupon code uppercased."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal</SPL> with items and products to compute subtotal RESULT subtotal]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon</SPL> with customer, subtotal, and coupon to compute discount RESULT discount]
            [COMMAND Compute taxable as max(subtotal - discount, 0) to clamp negative taxable amounts to zero RESULT taxable]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax</SPL> with taxable to compute tax RESULT tax]
            [COMMAND Compute total as taxable + tax RESULT total]
            [COMMAND Validate that total > 0 RESULT validated_total]
            [COMMAND Construct <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL> with (subtotal, discount, tax, total, coupon.upper()) RESULT price_quote]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: discount >= subtotal (i.e., subtotal - discount <= 0), so taxable is clamped to 0]
        [SEQUENTIAL_BLOCK]
            [COMMAND Set taxable to 0 via max(subtotal - discount, 0) RESULT taxable]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax</SPL> with taxable (0) to compute tax RESULT tax]
            [COMMAND Compute total as taxable + tax (total = tax) RESULT total]
            [COMMAND Construct <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL> with (subtotal, discount, tax, total, coupon.upper()) RESULT price_quote]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: total <= 0 after computing total]
        [LOG "No log"]
        [THROW ValueError "total must be positive"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/pricing.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote

Computes a customer's cart price quote by calculating subtotal, applying a coupon, clamping taxable to non-negative, computing tax, validating total is positive, and returning a PriceQuote with an uppercased coupon code.

## Inputs
- self (PricingPolicy): Instance providing pricing calculations for subtotal, coupon application, and tax.
- customer (Customer): Customer for whom discounts may apply.
- items (List[CartItem]): Shopping cart items to be priced.
- products (List[Product]): Product catalog data used to compute item prices.
- coupon (str): Optional coupon code used to compute a discount; defaults to empty string.

## Outputs
- price_quote (PriceQuote): Price breakdown including subtotal, discount, tax, total, and the coupon code uppercased.

## Main Effect
Construct <SPL>commerce_ops_demo.commerce_ops.pricing.PriceQuote</SPL> with (subtotal, discount, tax, total, coupon.upper())

## Calls and Callers
- commerce_ops_demo.commerce_ops.pricing.PriceQuote
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- ValueError: total must be positive
- raise ValueError("total must be positive")
- total <= 0 after computing total
- total > 0

## Validation Rules
- total > 0

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `owned_by_file` -> `file:commerce_ops/pricing.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `calls` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `calls` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `calls` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/pricing.py/PricingPolicy/quote.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`

---

<a id="method-commerce-ops-demo-commerce-ops-repository-orderrepository-init"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `method`, `public`

### Summary

Initialize the instance by creating an empty orders mapping.

### SPL Content

```spl
[DEFINE_WORKER: "Initialize the instance by creating an empty orders mapping." __init__]
    [INPUTS]
        <REF> self </REF>: object "The instance being initialized."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.orders </REF>: Dict[str, Order] "Instance attribute initialized to an empty dictionary."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Initialize the orders attribute as an empty dictionary on the instance. RESULT self.orders]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__

Initialize the instance by creating an empty orders mapping.

## Inputs
- self (object): The instance being initialized.

## Outputs
- self.orders (Dict[str, Order]): Instance attribute initialized to an empty dictionary.

## Main Effect
Initialize the orders attribute as an empty dictionary on the instance.

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- mutates self.orders
- self.orders (Dict[str, Order]): Instance attribute initialized to an empty dictionary.

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `owned_by_file` -> `file:commerce_ops/repository.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-repository-orderrepository-get"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository.get

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `method`, `public`

### Summary

Returns the Order associated with the given order_id from self.orders, raising KeyError if the id is absent.

### SPL Content

```spl
[DEFINE_WORKER: "Returns the Order associated with the given order_id from self.orders, raising KeyError if the id is absent." get]
    [INPUTS]
        <REF> order_id </REF>: str "Identifier of the order to retrieve."
        <REF> self.orders </REF>: Mapping[str, Order] "Internal mapping of orders keyed by order_id."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order </REF>: Order "The order object corresponding to the provided order_id."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Check that order_id exists in self.orders RESULT validated_presence]
            [COMMAND Retrieve the order via self.orders[order_id] RESULT order]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: order_id not in self.orders]
        [LOG "Exception information"]
        [THROW KeyError "order {order_id} not found"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository.get

Returns the Order associated with the given order_id from self.orders, raising KeyError if the id is absent.

## Inputs
- order_id (str): Identifier of the order to retrieve.
- self.orders (Mapping[str, Order]): Internal mapping of orders keyed by order_id.

## Outputs
- order (Order): The order object corresponding to the provided order_id.

## Main Effect
Retrieve the order via self.orders[order_id]

## Calls and Callers
- commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid
- commerce_ops_demo.commerce_ops.services.OrderService.cancel_order

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- KeyError: order {order_id} not found
- invalid when order_id not in self.orders
- order_id not in self.orders
- raise KeyError(f"order {order_id} not found")

## Validation Rules
- invalid when order_id not in self.orders

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `owned_by_file` -> `file:commerce_ops/repository.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/get.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository.get`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`

---

<a id="method-commerce-ops-demo-commerce-ops-repository-orderrepository-list-by-customer"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `method`, `public`

### Summary

Returns a new list of orders from the internal collection whose customer_id equals the provided customer_id.

### SPL Content

```spl
[DEFINE_WORKER: "Returns a new list of orders from the internal collection whose customer_id equals the provided customer_id." list_by_customer]
    [INPUTS]
        <REF> customer_id </REF>: str "Target customer identifier used to filter orders."
        <REF> self.orders </REF>: Mapping[Any, Order] "Internal mapping of orders; its values() are iterated to access order objects."
    [END_INPUTS]

    [OUTPUTS]
        <REF> orders_by_customer </REF>: List[Order] "New list containing orders whose order.customer_id equals the provided customer_id."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Access the internal orders collection values for iteration RESULT all_orders_iterable]
            [COMMAND Filter orders where each order.customer_id equals the input customer_id RESULT matching_orders_sequence]
            [COMMAND Construct a list from the filtered orders RESULT orders_by_customer]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [ALTERNATIVE_FLOW: No orders have a customer_id equal to the provided customer_id]
        [SEQUENTIAL_BLOCK]
            [COMMAND Iterate through orders, find no matches, and produce an empty list RESULT orders_by_customer (empty)]
        [END_SEQUENTIAL_BLOCK]
    [END_ALTERNATIVE_FLOW]

    [EXCEPTION_FLOW: The orders container does not support attribute values()]
        [LOG "AttributeError when accessing self.orders.values()"]
        [THROW AttributeError "The orders collection does not implement a values() method."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: An order object is missing the customer_id attribute during filtering]
        [LOG "AttributeError when reading order.customer_id"]
        [THROW AttributeError "Encountered an order without a customer_id attribute while filtering."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer

Returns a new list of orders from the internal collection whose customer_id equals the provided customer_id.

## Inputs
- customer_id (str): Target customer identifier used to filter orders.
- self.orders (Mapping[Any, Order]): Internal mapping of orders; its values() are iterated to access order objects.

## Outputs
- orders_by_customer (List[Order]): New list containing orders whose order.customer_id equals the provided customer_id.

## Main Effect
Construct a list from the filtered orders

## Calls and Callers
- commerce_ops_demo.commerce_ops.services.OrderService.customer_history

## Side Effects
- orders_by_customer (List[Order]): New list containing orders whose order.customer_id equals the provided customer_id.

## Errors
- An order object is missing the customer_id attribute during filtering
- AttributeError: Encountered an order without a customer_id attribute while filtering.
- AttributeError: The orders collection does not implement a values() method.
- The orders container does not support attribute values()

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `owned_by_file` -> `file:commerce_ops/repository.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/list_by_customer.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`

---

<a id="method-commerce-ops-demo-commerce-ops-repository-orderrepository-mark-paid"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `method`, `public`

### Summary

Retrieve an order by ID, mark it as paid with the given payment ID, persist it, and return the updated order.

### SPL Content

```spl
[DEFINE_WORKER: "Retrieve an order by ID, mark it as paid with the given payment ID, persist it, and return the updated order." mark_paid]
    [INPUTS]
        <REF> order_id </REF>: str "Identifier of the order to update."
        <REF> payment_id </REF>: str "Identifier of the payment used to mark the order as paid."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order </REF>: Order "The updated Order entity after being marked as paid and saved."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Fetch the order by ID via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> using order_id RESULT order]
            [COMMAND Mark the retrieved order as paid using payment_id via <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> RESULT order]
            [COMMAND Persist the updated order via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> RESULT saved]
            [COMMAND Return the updated order RESULT order]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order]
        [LOG "Failed to retrieve order for the provided order_id."]
        [THROW Exception "Error propagated from <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL>."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: Retrieved order is None, causing a failure on mark_paid invocation]
        [LOG "Retrieved order is None; cannot mark it as paid."]
        [THROW AttributeError "Attempting to call mark_paid on a None order value."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid]
        [LOG "Error occurred while marking the order as paid."]
        [THROW Exception "Error propagated from <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL>."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order]
        [LOG "Failed to persist the updated order."]
        [THROW Exception "Error propagated from <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL>."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid

Retrieve an order by ID, mark it as paid with the given payment ID, persist it, and return the updated order.

## Inputs
- order_id (str): Identifier of the order to update.
- payment_id (str): Identifier of the payment used to mark the order as paid.

## Outputs
- order (Order): The updated Order entity after being marked as paid and saved.

## Main Effect
Return the updated order

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Order.mark_paid
- commerce_ops_demo.commerce_ops.repository.OrderRepository.get
- commerce_ops_demo.commerce_ops.repository.OrderRepository.save

## Side Effects
- self.save(order)

## Errors
- <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> raises an error while marking the order as paid
- <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> raises an error while retrieving the order
- <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> raises an error while saving the updated order
- AttributeError: Attempting to call mark_paid on a None order value.
- Exception: Error propagated from <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL>.
- Exception: Error propagated from <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL>.
- Exception: Error propagated from <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL>.
- Retrieved order is None, causing a failure on mark_paid invocation

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `owned_by_file` -> `file:commerce_ops/repository.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/mark_paid.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`

---

<a id="method-commerce-ops-demo-commerce-ops-repository-orderrepository-save"></a>

## commerce_ops_demo.commerce_ops.repository.OrderRepository.save

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`
- Tags: `method`, `public`

### Summary

Validates the order has a truthy order_id and stores the order in the instance's orders mapping under that key.

### SPL Content

```spl
[DEFINE_WORKER: "Validates the order has a truthy order_id and stores the order in the instance's orders mapping under that key." save]
    [INPUTS]
        <REF> order </REF>: Order "Order object to be saved; must expose a truthy order_id used as the storage key."
        <REF> self.orders </REF>: MutableMapping "Instance mapping of orders keyed by order_id that will be updated."
    [END_INPUTS]

    [OUTPUTS]
        <REF> return_value </REF>: NoneType "No value is returned."
        <REF> orders_updated </REF>: state_mutation "self.orders[order.order_id] is set to the provided order (overwrites existing entry if the key already exists)."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Validate that order.order_id is truthy RESULT validation_passed]
            [COMMAND Assign the order into self.orders keyed by order.order_id RESULT orders_updated]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: order.order_id is falsy (e.g., None, '', 0)]
        [LOG "order_id is required"]
        [THROW ValueError "order_id is required"]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/repository.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.repository.OrderRepository.save

Validates the order has a truthy order_id and stores the order in the instance's orders mapping under that key.

## Inputs
- order (Order): Order object to be saved; must expose a truthy order_id used as the storage key.
- self.orders (MutableMapping): Instance mapping of orders keyed by order_id that will be updated.

## Outputs
- return_value (NoneType): No value is returned.
- orders_updated (state_mutation): self.orders[order.order_id] is set to the provided order (overwrites existing entry if the key already exists).

## Main Effect
Assign the order into self.orders keyed by order.order_id

## Calls and Callers
- commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid
- commerce_ops_demo.commerce_ops.services.OrderService.cancel_order
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- mutates self.orders
- mutates self.orders[order.order_id]
- orders_updated (state_mutation): self.orders[order.order_id] is set to the provided order (overwrites existing entry if the key already exists).

## Errors
- ValueError: order_id is required
- invalid when not order.order_id
- order.order_id is falsy (e.g., None, '', 0)
- orders must contain order.order_id
- raise ValueError("order_id is required")

## Validation Rules
- invalid when not order.order_id
- orders must contain order.order_id

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `owned_by_file` -> `file:commerce_ops/repository.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `calls` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` <- `topic:persistence`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/repository.py/OrderRepository/save.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.repository.OrderRepository.save`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-init"></a>

## commerce_ops_demo.commerce_ops.services.OrderService.__init__

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `public`

### Summary

Constructs the instance by storing injected services on the object and initializing last_receipt to None.

### SPL Content

```spl
[DEFINE_WORKER: "Constructs the instance by storing injected services on the object and initializing last_receipt to None." __init__]
    [INPUTS]
        <REF> catalog </REF>: ProductCatalog "Product catalog dependency to be stored on the instance."
        <REF> pricing </REF>: PricingPolicy "Pricing policy dependency to be stored on the instance."
        <REF> payments </REF>: PaymentGateway "Payment gateway dependency to be stored on the instance."
        <REF> repository </REF>: OrderRepository "Order repository dependency to be stored on the instance."
        <REF> notifications </REF>: NotificationService "Notification service dependency to be stored on the instance."
    [END_INPUTS]

    [OUTPUTS]
        <REF> self.catalog </REF>: ProductCatalog "Instance attribute set to the provided catalog reference."
        <REF> self.pricing </REF>: PricingPolicy "Instance attribute set to the provided pricing reference."
        <REF> self.payments </REF>: PaymentGateway "Instance attribute set to the provided payments reference."
        <REF> self.repository </REF>: OrderRepository "Instance attribute set to the provided repository reference."
        <REF> self.notifications </REF>: NotificationService "Instance attribute set to the provided notifications reference."
        <REF> self.last_receipt </REF>: PaymentReceipt | None "Initialized to None to indicate no receipt is present at construction time."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Assign constructor dependencies to instance attributes RESULT self.catalog, self.pricing, self.payments, self.repository, self.notifications]
            [COMMAND Initialize last_receipt attribute to None RESULT self.last_receipt = None]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.__init__`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService.__init__

Constructs the instance by storing injected services on the object and initializing last_receipt to None.

## Inputs
- catalog (ProductCatalog): Product catalog dependency to be stored on the instance.
- pricing (PricingPolicy): Pricing policy dependency to be stored on the instance.
- payments (PaymentGateway): Payment gateway dependency to be stored on the instance.
- repository (OrderRepository): Order repository dependency to be stored on the instance.
- notifications (NotificationService): Notification service dependency to be stored on the instance.

## Outputs
- self.catalog (ProductCatalog): Instance attribute set to the provided catalog reference.
- self.pricing (PricingPolicy): Instance attribute set to the provided pricing reference.
- self.payments (PaymentGateway): Instance attribute set to the provided payments reference.
- self.repository (OrderRepository): Instance attribute set to the provided repository reference.
- self.notifications (NotificationService): Instance attribute set to the provided notifications reference.

## Main Effect
Initialize last_receipt attribute to None

## Calls and Callers
- evidence: missing; confidence: not_available; source: static_analysis

## Side Effects
- mutates self.catalog
- mutates self.last_receipt
- mutates self.notifications
- mutates self.payments
- mutates self.pricing
- mutates self.repository
- self.catalog (ProductCatalog): Instance attribute set to the provided catalog reference.
- self.notifications (NotificationService): Instance attribute set to the provided notifications reference.
- self.payments (PaymentGateway): Instance attribute set to the provided payments reference.
- self.pricing (PricingPolicy): Instance attribute set to the provided pricing reference.
- self.repository (OrderRepository): Instance attribute set to the provided repository reference.

## Errors
- evidence: missing; confidence: not_available; source: static_analysis

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`

### Referenced By

- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/__init__.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService.__init__`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService.__init__`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-build-order"></a>

## commerce_ops_demo.commerce_ops.services.OrderService._build_order

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `private`

### Summary

Constructs a new Order from the given customer, items, and quote, assigns a UUID, records a 'quoted' event with price breakdown, and returns the Order.

### SPL Content

```spl
[DEFINE_WORKER: "Constructs a new Order from the given customer, items, and quote, assigns a UUID, records a 'quoted' event with price breakdown, and returns the Order." _build_order]
    [INPUTS]
        <REF> self </REF>: object "Instance context for method execution."
        <REF> customer </REF>: Customer "Customer providing customer_id used in the order."
        <REF> items </REF>: List[CartItem] "Cart items; copied into the order via list(items)."
        <REF> quote </REF>: PriceQuote "Pricing details providing total_cents and breakdown fields used for the event message."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order </REF>: Order "Newly constructed Order with UUID string id, customer_id, a copied items list, total_cents, and a recorded 'quoted' event."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Construct <SPL>commerce_ops_demo.commerce_ops.models.Order</SPL> using str(uuid4()) for id, customer.customer_id, a list(items) copy, and quote.total_cents RESULT order]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> on order with event 'quoted' and message 'subtotal={quote.subtotal_cents}; discount={quote.discount_cents}; tax={quote.tax_cents}' RESULT event_recorded]
            [COMMAND Return the constructed order RESULT order]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: customer is None or lacks attribute customer.customer_id when accessed]
        [LOG "Customer is missing customer_id."]
        [THROW AttributeError "customer must have a customer_id attribute."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: items is None or not iterable when list(items) is evaluated]
        [LOG "Items is not iterable or is None."]
        [THROW TypeError "items must be an iterable of CartItem."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: quote is None or lacks expected attributes (total_cents, subtotal_cents, discount_cents, tax_cents)]
        [LOG "Quote missing required pricing fields."]
        [THROW AttributeError "quote must provide total_cents, subtotal_cents, discount_cents, and tax_cents."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.models.Order</SPL> constructor rejects provided arguments]
        [LOG "Order construction failed due to invalid argument types or values."]
        [THROW ValueError "Invalid arguments for constructing Order."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: Calling <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> fails]
        [LOG "Failed to add 'quoted' event to order."]
        [THROW Exception "add_event raised an error."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService._build_order

Constructs a new Order from the given customer, items, and quote, assigns a UUID, records a 'quoted' event with price breakdown, and returns the Order.

## Inputs
- self (object): Instance context for method execution.
- customer (Customer): Customer providing customer_id used in the order.
- items (List[CartItem]): Cart items; copied into the order via list(items).
- quote (PriceQuote): Pricing details providing total_cents and breakdown fields used for the event message.

## Outputs
- order (Order): Newly constructed Order with UUID string id, customer_id, a copied items list, total_cents, and a recorded 'quoted' event.

## Main Effect
Return the constructed order

## Calls and Callers
- commerce_ops_demo.commerce_ops.models.Order
- commerce_ops_demo.commerce_ops.models.Order.add_event
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- <SPL>commerce_ops_demo.commerce_ops.models.Order</SPL> constructor rejects provided arguments
- AttributeError: customer must have a customer_id attribute.
- AttributeError: quote must provide total_cents, subtotal_cents, discount_cents, and tax_cents.
- Calling <SPL>commerce_ops_demo.commerce_ops.models.Order.add_event</SPL> fails
- Exception: add_event raised an error.
- TypeError: items must be an iterable of CartItem.
- ValueError: Invalid arguments for constructing Order.
- customer is None or lacks attribute customer.customer_id when accessed
- items is None or not iterable when list(items) is evaluated
- quote is None or lacks expected attributes (total_cents, subtotal_cents, discount_cents, tax_cents)

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_build_order.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService._build_order`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService._build_order`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-charge"></a>

## commerce_ops_demo.commerce_ops.services.OrderService._charge

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService._charge`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `private`

### Summary

Authorize a payment for the customer's quoted amount via the payment gateway, store the resulting receipt in state, and return it.

### SPL Content

```spl
[DEFINE_WORKER: "Authorize a payment for the customer's quoted amount via the payment gateway, store the resulting receipt in state, and return it." _charge]
    [INPUTS]
        <REF> customer </REF>: Customer "Customer to be charged; passed to the payment gateway."
        <REF> quote </REF>: PriceQuote "Quote containing total_cents; quote.total_cents is used as the amount to authorize."
        <REF> self.payments </REF>: PaymentGateway "Instance payment gateway used to authorize charges; expected to implement authorize(customer, amount_cents)."
    [END_INPUTS]

    [OUTPUTS]
        <REF> receipt </REF>: PaymentReceipt "Payment receipt returned from the authorization call."
        <REF> self.last_receipt </REF>: PaymentReceipt "Instance state updated to reference the same receipt object."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize</SPL> via self.payments with (customer, quote.total_cents) RESULT receipt]
            [COMMAND Assign receipt to self.last_receipt RESULT self.last_receipt]
            [COMMAND Return receipt RESULT receipt]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.payments is None or does not provide authorize]
        [LOG "Payment gateway unavailable or missing authorize()"]
        [THROW AttributeError "Raised when self.payments is not set or lacks an authorize method."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: quote is None or quote.total_cents attribute access fails]
        [LOG "Invalid quote or missing total_cents"]
        [THROW AttributeError "Raised when quote is missing or does not have total_cents."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize</SPL> raises due to invalid inputs or gateway failure]
        [LOG "Authorization failed during payment processing"]
        [THROW Exception "Propagated exception from the payment gateway authorization call."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService._charge

Authorize a payment for the customer's quoted amount via the payment gateway, store the resulting receipt in state, and return it.

## Inputs
- customer (Customer): Customer to be charged; passed to the payment gateway.
- quote (PriceQuote): Quote containing total_cents; quote.total_cents is used as the amount to authorize.
- self.payments (PaymentGateway): Instance payment gateway used to authorize charges; expected to implement authorize(customer, amount_cents).

## Outputs
- receipt (PaymentReceipt): Payment receipt returned from the authorization call.
- self.last_receipt (PaymentReceipt): Instance state updated to reference the same receipt object.

## Main Effect
Return receipt

## Calls and Callers
- commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- mutates self.last_receipt
- self.last_receipt (PaymentReceipt): Instance state updated to reference the same receipt object.

## Errors
- <SPL>commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize</SPL> raises due to invalid inputs or gateway failure
- AttributeError: Raised when quote is missing or does not have total_cents.
- AttributeError: Raised when self.payments is not set or lacks an authorize method.
- Exception: Propagated exception from the payment gateway authorization call.
- quote is None or quote.total_cents attribute access fails
- self.payments is None or does not provide authorize

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:authentication`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_charge.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService._charge`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService._charge`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-notify-customer"></a>

## commerce_ops_demo.commerce_ops.services.OrderService._notify_customer

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `private`

### Summary

Send a purchase receipt to the customer and trigger a low-stock alert for the provided products using the instance's notifications service.

### SPL Content

```spl
[DEFINE_WORKER: "Send a purchase receipt to the customer and trigger a low-stock alert for the provided products using the instance's notifications service." _notify_customer]
    [INPUTS]
        <REF> self </REF>: object "Instance reference; must provide a notifications service at self.notifications."
        <REF> self.notifications </REF>: NotificationService "Service used to send notifications; expected to implement send_receipt and send_low_stock_alert."
        <REF> customer </REF>: Customer "Customer entity used for sending the receipt."
        <REF> order </REF>: Order "Order entity whose details are included in the receipt."
        <REF> products </REF>: Any "Collection of product items evaluated for low-stock alerting."
    [END_INPUTS]

    [OUTPUTS]
        <REF> receipt_sent </REF>: side_effect "Receipt notification sent via <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt</SPL>."
        <REF> low_stock_alert_sent </REF>: side_effect "Low-stock alert triggered via <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL>."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt</SPL> on self.notifications with (customer, order). RESULT receipt_sent]
            [COMMAND Invoke <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL> on self.notifications with (products). RESULT low_stock_alert_sent]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.notifications is None or lacks send_receipt/send_low_stock_alert methods.]
        [LOG "Notification service missing or incompatible on self.notifications."]
        [THROW AttributeError "notifications service is not available or does not implement required methods."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt</SPL> or <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL> raises an exception during execution.]
        [LOG "Underlying notification call failed; propagating error."]
        [THROW Exception "Error raised by the notification service while sending messages."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService._notify_customer

Send a purchase receipt to the customer and trigger a low-stock alert for the provided products using the instance's notifications service.

## Inputs
- self (object): Instance reference; must provide a notifications service at self.notifications.
- self.notifications (NotificationService): Service used to send notifications; expected to implement send_receipt and send_low_stock_alert.
- customer (Customer): Customer entity used for sending the receipt.
- order (Order): Order entity whose details are included in the receipt.
- products (Any): Collection of product items evaluated for low-stock alerting.

## Outputs
- receipt_sent (side_effect): Receipt notification sent via <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt</SPL>.
- low_stock_alert_sent (side_effect): Low-stock alert triggered via <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL>.

## Main Effect
Invoke <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL> on self.notifications with (products).

## Calls and Callers
- commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert
- commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt
- commerce_ops_demo.commerce_ops.services.OrderService.checkout

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt</SPL> or <SPL>commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert</SPL> raises an exception during execution.
- AttributeError: notifications service is not available or does not implement required methods.
- Exception: Error raised by the notification service while sending messages.
- self.notifications is None or lacks send_receipt/send_low_stock_alert methods.

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- `calls` -> `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_low_stock_alert`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.notifications.NotificationService.send_receipt`
- `calls` <- `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/_notify_customer.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-cancel-order"></a>

## commerce_ops_demo.commerce_ops.services.OrderService.cancel_order

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `public`

### Summary

Cancels an order by ID with a reason, releases its items back to the catalog, saves the updated order, and returns it.

### SPL Content

```spl
[DEFINE_WORKER: "Cancels an order by ID with a reason, releases its items back to the catalog, saves the updated order, and returns it." cancel_order]
    [INPUTS]
        <REF> order_id </REF>: str "Unique identifier of the order to cancel."
        <REF> reason </REF>: str "Human-readable reason for cancelling the order."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order </REF>: Order "The updated Order entity marked as cancelled and persisted."
        <REF> inventory_released </REF>: None "Side effect: order items released back to catalog inventory."
        <REF> repository_saved </REF>: None "Side effect: updated order persisted via repository."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Fetch order by ID via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL>(order_id) RESULT order]
            [COMMAND Mark the order as cancelled with the provided reason using order.mark_cancelled(reason) RESULT cancelled_order]
            [COMMAND Release the order's items back to the catalog via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL>(order.items) RESULT inventory_released]
            [COMMAND Persist the updated order via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL>(order) RESULT repository_saved]
            [COMMAND Return the updated order RESULT order]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: self.repository is None or <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> is not available]
        [LOG "Repository unavailable or missing get() when fetching order."]
        [THROW AttributeError "Failed to access repository.get to retrieve the order."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: Fetched order is None after <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL>(order_id)]
        [LOG "Order not found for the given order_id; subsequent operations will fail."]
        [THROW AttributeError "order is None; calling order.mark_cancelled(reason) would raise an AttributeError."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: self.catalog is None or <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL> is not available]
        [LOG "Catalog unavailable or missing release_items() when releasing items."]
        [THROW AttributeError "Failed to access catalog.release_items to release order items."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: self.repository is None or <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> is not available]
        [LOG "Repository unavailable or missing save() when persisting the order."]
        [THROW AttributeError "Failed to access repository.save to persist the updated order."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService.cancel_order

Cancels an order by ID with a reason, releases its items back to the catalog, saves the updated order, and returns it.

## Inputs
- order_id (str): Unique identifier of the order to cancel.
- reason (str): Human-readable reason for cancelling the order.

## Outputs
- order (Order): The updated Order entity marked as cancelled and persisted.
- inventory_released (None): Side effect: order items released back to catalog inventory.
- repository_saved (None): Side effect: updated order persisted via repository.

## Main Effect
Return the updated order

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items
- commerce_ops_demo.commerce_ops.repository.OrderRepository.get
- commerce_ops_demo.commerce_ops.repository.OrderRepository.save

## Side Effects
- self.catalog.release_items(order.items)
- self.repository.save(order)

## Errors
- AttributeError: Failed to access catalog.release_items to release order items.
- AttributeError: Failed to access repository.get to retrieve the order.
- AttributeError: Failed to access repository.save to persist the updated order.
- AttributeError: order is None; calling order.mark_cancelled(reason) would raise an AttributeError.
- Fetched order is None after <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL>(order_id)
- self.catalog is None or <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL> is not available
- self.repository is None or <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.get</SPL> is not available
- self.repository is None or <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> is not available

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/cancel_order.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-checkout"></a>

## commerce_ops_demo.commerce_ops.services.OrderService.checkout

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `public`

### Summary

Reserve cart items, quote pricing, build and charge an order, mark it paid, persist and notify the customer, then return the order; on any failure after reservation, release items and propagate the error.

### SPL Content

```spl
[DEFINE_WORKER: "Reserve cart items, quote pricing, build and charge an order, mark it paid, persist and notify the customer, then return the order; on any failure after reservation, release items and propagate the error." checkout]
    [INPUTS]
        <REF> customer </REF>: Customer "Customer placing the order; used for pricing, charging, and notification."
        <REF> items </REF>: List[CartItem] "Cart items to purchase; used for reservation and pricing."
        <REF> coupon </REF>: str "Optional coupon code applied during pricing; defaults to empty string."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order </REF>: Order "Final paid order object that has been saved and returned."
        <REF> inventory_reserved </REF>: side_effect "Items reserved via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items</SPL>; on failure, reservations are released via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL>."
        <REF> payment_charged </REF>: side_effect "Payment processed via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._charge</SPL> and applied to the order using <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL>."
        <REF> order_persisted </REF>: side_effect "Order persisted via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL>."
        <REF> customer_notified </REF>: side_effect "Customer notified of the order via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._notify_customer</SPL>."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items</SPL> with items to reserve inventory. RESULT reserved_products]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote</SPL> with customer, items, reserved_products, and coupon to compute a pricing quote. RESULT quote]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.services.OrderService._build_order</SPL> with customer, items, and quote to construct the order. RESULT order]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.services.OrderService._charge</SPL> with customer and quote to process payment. RESULT receipt]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL> on order with receipt.payment_id to mark the order as paid. RESULT order_paid]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL> with order to persist it. RESULT order_saved]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.services.OrderService._notify_customer</SPL> with customer, order, and reserved_products to send a notification. RESULT customer_notified]
            [COMMAND Return the completed order. RESULT order]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: If any exception occurs after reserving items during quoting, building the order, charging payment, marking as paid, saving, or notifying.]
        [LOG "Release item reservations by calling <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL> with items, then re-raise the original exception."]
        [THROW Exception "Original exception is propagated to the caller."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService.checkout

Reserve cart items, quote pricing, build and charge an order, mark it paid, persist and notify the customer, then return the order; on any failure after reservation, release items and propagate the error.

## Inputs
- customer (Customer): Customer placing the order; used for pricing, charging, and notification.
- items (List[CartItem]): Cart items to purchase; used for reservation and pricing.
- coupon (str): Optional coupon code applied during pricing; defaults to empty string.

## Outputs
- order (Order): Final paid order object that has been saved and returned.
- inventory_reserved (side_effect): Items reserved via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items</SPL>; on failure, reservations are released via <SPL>commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items</SPL>.
- payment_charged (side_effect): Payment processed via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._charge</SPL> and applied to the order using <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL>.
- order_persisted (side_effect): Order persisted via <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.save</SPL>.
- customer_notified (side_effect): Customer notified of the order via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._notify_customer</SPL>.

## Main Effect
Return the completed order.

## Calls and Callers
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items
- commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items
- commerce_ops_demo.commerce_ops.models.Order.mark_paid
- commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote
- commerce_ops_demo.commerce_ops.repository.OrderRepository.save
- commerce_ops_demo.commerce_ops.services.OrderService._build_order
- commerce_ops_demo.commerce_ops.services.OrderService._charge
- commerce_ops_demo.commerce_ops.services.OrderService._notify_customer
- commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Side Effects
- customer_notified (side_effect): Customer notified of the order via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._notify_customer</SPL>.
- payment_charged (side_effect): Payment processed via <SPL>commerce_ops_demo.commerce_ops.services.OrderService._charge</SPL> and applied to the order using <SPL>commerce_ops_demo.commerce_ops.models.Order.mark_paid</SPL>.
- self.catalog.release_items(items)
- self.catalog.reserve_items(items)
- self.repository.save(order)

## Errors
- Exception: Original exception is propagated to the caller.
- If any exception occurs after reserving items during quoting, building the order, charging payment, marking as paid, saving, or notifying.
- raise

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `calls` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `calls` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `calls` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `calls` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `calls` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `calls` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Referenced By

- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.release_items`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._notify_customer`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` <- `workflow:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` <- `topic:validation`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/checkout.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService.checkout`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService.checkout`

---

<a id="method-commerce-ops-demo-commerce-ops-services-orderservice-customer-history"></a>

## commerce_ops_demo.commerce_ops.services.OrderService.customer_history

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- Type: `entity` / `method`
- Qualified name: `commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`
- Tags: `method`, `public`

### Summary

Fetches a customer's orders from the repository and returns a list of dictionaries containing order_id, status, and total_cents converted to a string.

### SPL Content

```spl
[DEFINE_WORKER: "Fetches a customer's orders from the repository and returns a list of dictionaries containing order_id, status, and total_cents converted to a string." customer_history]
    [INPUTS]
        <REF> customer_id </REF>: str "Identifier of the customer whose orders are requested."
        <REF> self.repository </REF>: OrderRepository "Repository used to retrieve orders for the given customer."
    [END_INPUTS]

    [OUTPUTS]
        <REF> order_summaries </REF>: List[Dict[str, str]] "List of order summary dictionaries with keys order_id, status, and total (as a string)."
    [END_OUTPUTS]

    [MAIN_FLOW]
        [SEQUENTIAL_BLOCK]
            [COMMAND Call <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer</SPL> with customer_id to retrieve the customer's orders. RESULT orders]
            [COMMAND Construct a list of dictionaries from orders, each with order_id, status, and total as str(order.total_cents). RESULT order_summaries]
        [END_SEQUENTIAL_BLOCK]
    [END_MAIN_FLOW]

    [EXCEPTION_FLOW: <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer</SPL> raises an exception.]
        [LOG "Repository error occurred while fetching orders for the customer."]
        [THROW Exception "Propagates any exception raised by the repository call."]
    [END_EXCEPTION_FLOW]

    [EXCEPTION_FLOW: orders is None or otherwise non-iterable, causing the list comprehension to fail.]
        [LOG "Failed to iterate over the repository result when building order summaries."]
        [THROW TypeError "Raised when attempting to iterate over a None or non-iterable orders result."]
    [END_EXCEPTION_FLOW]

[END_WORKER]
```

### Wiki Navigation And Context

## Wiki Navigation

- Page ID: `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- Entity kind: `method`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/services.py`

## Wiki Summary

# commerce_ops_demo.commerce_ops.services.OrderService.customer_history

Fetches a customer's orders from the repository and returns a list of dictionaries containing order_id, status, and total_cents converted to a string.

## Inputs
- customer_id (str): Identifier of the customer whose orders are requested.
- self.repository (OrderRepository): Repository used to retrieve orders for the given customer.

## Outputs
- evidence: missing; confidence: not_available; source: static_analysis

## Main Effect
Construct a list of dictionaries from orders, each with order_id, status, and total as str(order.total_cents).

## Calls and Callers
- commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer
- commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Side Effects
- evidence: missing; confidence: not_available; source: static_analysis

## Errors
- <SPL>commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer</SPL> raises an exception.
- Exception: Propagates any exception raised by the repository call.
- TypeError: Raised when attempting to iterate over a None or non-iterable orders result.
- orders is None or otherwise non-iterable, causing the list comprehension to fail.

## Validation Rules
- evidence: missing; confidence: not_available; source: static_analysis

### Outgoing Links

- `owned_by_class` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `owned_by_file` -> `file:commerce_ops/services.py`
- `owned_by_package` -> `package:commerce_ops_demo.commerce_ops`
- `calls` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `called_by` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

### Referenced By

- `calls` <- `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `called_by` <- `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `contains_method` <- `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `topic_mentions` <- `topic:persistence`

### Source Evidence

- `spl/commerce_ops_demo/commerce_ops/services.py/OrderService/customer_history.spl`

### Symbols

- `commerce_ops_demo.commerce_ops.services.OrderService.customer_history`

### Graph References

- `call_graph:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`

---

<a id="workflow-commerce-ops-demo-commerce-ops-cli-build-demo-service"></a>

## Workflow from commerce_ops_demo.commerce_ops.cli.build_demo_service

- Page ID: `workflow:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- Type: `workflow` / `workflow`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `workflow`

### Summary

Call path starting from commerce_ops_demo.commerce_ops.cli.build_demo_service.

### Wiki Content

# Workflow from commerce_ops_demo.commerce_ops.cli.build_demo_service

## Path

1. [[commerce_ops_demo.commerce_ops.cli.build_demo_service]]
2. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog]]
3. [[commerce_ops_demo.commerce_ops.models.Product]]

## Evidence

- source: static_call_graph
- confidence: high_or_medium_edges_preferred

### Outgoing Links

- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Product`

### Source Evidence

- `graphs/repository_call_graph.json`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.models.Product`

### Graph References

- `workflow:commerce_ops_demo.commerce_ops.cli.build_demo_service`

---

<a id="workflow-commerce-ops-demo-commerce-ops-cli-main"></a>

## Workflow from commerce_ops_demo.commerce_ops.cli.main

- Page ID: `workflow:commerce_ops_demo.commerce_ops.cli.main`
- Type: `workflow` / `workflow`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.main`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `workflow`

### Summary

Call path starting from commerce_ops_demo.commerce_ops.cli.main.

### Wiki Content

# Workflow from commerce_ops_demo.commerce_ops.cli.main

## Path

1. [[commerce_ops_demo.commerce_ops.cli.main]]
2. [[commerce_ops_demo.commerce_ops.cli.run_checkout_demo]]
3. [[commerce_ops_demo.commerce_ops.cli.build_demo_service]]
4. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog]]
5. [[commerce_ops_demo.commerce_ops.models.Product]]
6. [[commerce_ops_demo.commerce_ops.models.Customer]]
7. [[commerce_ops_demo.commerce_ops.cli.parse_cart]]
8. [[commerce_ops_demo.commerce_ops.models.CartItem]]
9. [[commerce_ops_demo.commerce_ops.services.OrderService.checkout]]
10. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items]]
11. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get]]
12. [[commerce_ops_demo.commerce_ops.catalog.normalize_sku]]
13. [[commerce_ops_demo.commerce_ops.models.Product.reserve]]
14. [[commerce_ops_demo.commerce_ops.models.Product.release]]
15. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote]]
16. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal]]
17. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon]]
18. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax]]
19. [[commerce_ops_demo.commerce_ops.pricing.PriceQuote]]
20. [[commerce_ops_demo.commerce_ops.services.OrderService._build_order]]
21. [[commerce_ops_demo.commerce_ops.models.Order]]
22. [[commerce_ops_demo.commerce_ops.models.Order.add_event]]
23. [[commerce_ops_demo.commerce_ops.services.OrderService._charge]]
24. [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize]]
25. [[commerce_ops_demo.commerce_ops.payments.PaymentError]]
26. [[commerce_ops_demo.commerce_ops.models.Customer.debit]]
27. [[commerce_ops_demo.commerce_ops.models.Customer.can_spend]]
28. [[commerce_ops_demo.commerce_ops.payments.PaymentReceipt]]

## Evidence

- source: static_call_graph
- confidence: high_or_medium_edges_preferred

### Outgoing Links

- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.main`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

### Source Evidence

- `graphs/repository_call_graph.json`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.main`
- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.models.Product`
- `commerce_ops_demo.commerce_ops.models.Customer`
- `commerce_ops_demo.commerce_ops.cli.parse_cart`
- `commerce_ops_demo.commerce_ops.models.CartItem`
- `commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `commerce_ops_demo.commerce_ops.models.Product.reserve`
- `commerce_ops_demo.commerce_ops.models.Product.release`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `commerce_ops_demo.commerce_ops.models.Order`
- `commerce_ops_demo.commerce_ops.models.Order.add_event`
- `commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `commerce_ops_demo.commerce_ops.payments.PaymentError`
- `commerce_ops_demo.commerce_ops.models.Customer.debit`
- `commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

### Graph References

- `workflow:commerce_ops_demo.commerce_ops.cli.main`

---

<a id="workflow-commerce-ops-demo-commerce-ops-cli-parse-cart"></a>

## Workflow from commerce_ops_demo.commerce_ops.cli.parse_cart

- Page ID: `workflow:commerce_ops_demo.commerce_ops.cli.parse_cart`
- Type: `workflow` / `workflow`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.parse_cart`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `workflow`

### Summary

Call path starting from commerce_ops_demo.commerce_ops.cli.parse_cart.

### Wiki Content

# Workflow from commerce_ops_demo.commerce_ops.cli.parse_cart

## Path

1. [[commerce_ops_demo.commerce_ops.cli.parse_cart]]
2. [[commerce_ops_demo.commerce_ops.models.CartItem]]

## Evidence

- source: static_call_graph
- confidence: high_or_medium_edges_preferred

### Outgoing Links

- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`

### Source Evidence

- `graphs/repository_call_graph.json`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.parse_cart`
- `commerce_ops_demo.commerce_ops.models.CartItem`

### Graph References

- `workflow:commerce_ops_demo.commerce_ops.cli.parse_cart`

---

<a id="workflow-commerce-ops-demo-commerce-ops-cli-run-checkout-demo"></a>

## Workflow from commerce_ops_demo.commerce_ops.cli.run_checkout_demo

- Page ID: `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- Type: `workflow` / `workflow`
- Qualified name: `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- Package: `commerce_ops_demo.commerce_ops`
- File: `commerce_ops/cli.py`
- Tags: `workflow`

### Summary

Call path starting from commerce_ops_demo.commerce_ops.cli.run_checkout_demo.

### Wiki Content

# Workflow from commerce_ops_demo.commerce_ops.cli.run_checkout_demo

## Path

1. [[commerce_ops_demo.commerce_ops.cli.run_checkout_demo]]
2. [[commerce_ops_demo.commerce_ops.cli.build_demo_service]]
3. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog]]
4. [[commerce_ops_demo.commerce_ops.models.Product]]
5. [[commerce_ops_demo.commerce_ops.models.Customer]]
6. [[commerce_ops_demo.commerce_ops.cli.parse_cart]]
7. [[commerce_ops_demo.commerce_ops.models.CartItem]]
8. [[commerce_ops_demo.commerce_ops.services.OrderService.checkout]]
9. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items]]
10. [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get]]
11. [[commerce_ops_demo.commerce_ops.catalog.normalize_sku]]
12. [[commerce_ops_demo.commerce_ops.models.Product.reserve]]
13. [[commerce_ops_demo.commerce_ops.models.Product.release]]
14. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote]]
15. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal]]
16. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon]]
17. [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax]]
18. [[commerce_ops_demo.commerce_ops.pricing.PriceQuote]]
19. [[commerce_ops_demo.commerce_ops.services.OrderService._build_order]]
20. [[commerce_ops_demo.commerce_ops.models.Order]]
21. [[commerce_ops_demo.commerce_ops.models.Order.add_event]]
22. [[commerce_ops_demo.commerce_ops.services.OrderService._charge]]
23. [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize]]
24. [[commerce_ops_demo.commerce_ops.payments.PaymentError]]
25. [[commerce_ops_demo.commerce_ops.models.Customer.debit]]
26. [[commerce_ops_demo.commerce_ops.models.Customer.can_spend]]
27. [[commerce_ops_demo.commerce_ops.payments.PaymentReceipt]]

## Evidence

- source: static_call_graph
- confidence: high_or_medium_edges_preferred

### Outgoing Links

- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.cli.parse_cart`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.models.Order`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Order.add_event`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentError`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `workflow_step` -> `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `workflow_step` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

### Source Evidence

- `graphs/repository_call_graph.json`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.models.Product`
- `commerce_ops_demo.commerce_ops.models.Customer`
- `commerce_ops_demo.commerce_ops.cli.parse_cart`
- `commerce_ops_demo.commerce_ops.models.CartItem`
- `commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `commerce_ops_demo.commerce_ops.models.Product.reserve`
- `commerce_ops_demo.commerce_ops.models.Product.release`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `commerce_ops_demo.commerce_ops.pricing.PriceQuote`
- `commerce_ops_demo.commerce_ops.services.OrderService._build_order`
- `commerce_ops_demo.commerce_ops.models.Order`
- `commerce_ops_demo.commerce_ops.models.Order.add_event`
- `commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `commerce_ops_demo.commerce_ops.payments.PaymentError`
- `commerce_ops_demo.commerce_ops.models.Customer.debit`
- `commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `commerce_ops_demo.commerce_ops.payments.PaymentReceipt`

### Graph References

- `workflow:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`

---

<a id="topic-authentication"></a>

## Authentication

- Page ID: `topic:authentication`
- Type: `topic` / `topic`
- Qualified name: `Authentication`
- Tags: `topic`

### Summary

Entities related to Authentication.

### Wiki Content

# Authentication

- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__]]
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize]]
- [[commerce_ops_demo.commerce_ops.services.OrderService._charge]]
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway]]
- [[commerce_ops_demo.commerce_ops.services.OrderService]]
- [[commerce_ops/services.py]]
- [[commerce_ops/payments.py]]

### Outgoing Links

- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `topic_mentions` -> `file:commerce_ops/services.py`
- `topic_mentions` -> `file:commerce_ops/payments.py`

### Source Evidence

- `artifacts/*_cards`

### Symbols

- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `commerce_ops_demo.commerce_ops.services.OrderService._charge`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway`
- `commerce_ops_demo.commerce_ops.services.OrderService`
- `commerce_ops/services.py`
- `commerce_ops/payments.py`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---

<a id="topic-configuration"></a>

## Configuration

- Page ID: `topic:configuration`
- Type: `topic` / `topic`
- Qualified name: `Configuration`
- Tags: `topic`

### Summary

Entities related to Configuration.

### Wiki Content

# Configuration

- [[commerce_ops_demo.commerce_ops.cli.run_checkout_demo]]
- [[commerce_ops_demo.commerce_ops.cli.build_demo_service]]
- [[commerce_ops_demo.commerce_ops.models.Order.mark_paid]]
- [[commerce_ops_demo.commerce_ops.models.Order.mark_cancelled]]
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available]]
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy]]

### Outgoing Links

- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.pricing.PricingPolicy`

### Source Evidence

- `artifacts/*_cards`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.list_available`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.__init__`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---

<a id="topic-external-integration"></a>

## External Integration

- Page ID: `topic:external-integration`
- Type: `topic` / `topic`
- Qualified name: `External Integration`
- Tags: `topic`

### Summary

Entities related to External Integration.

### Wiki Content

# External Integration

- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items]]
- [[commerce_ops_demo.commerce_ops.models.Customer.can_spend]]
- [[commerce_ops/payments.py]]
- [[commerce_ops/repository.py]]
- [[commerce_ops_demo.commerce_ops]]

### Outgoing Links

- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `topic_mentions` -> `file:commerce_ops/payments.py`
- `topic_mentions` -> `file:commerce_ops/repository.py`
- `topic_mentions` -> `package:commerce_ops_demo.commerce_ops`

### Source Evidence

- `artifacts/*_cards`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `commerce_ops_demo.commerce_ops.models.Customer.can_spend`
- `commerce_ops/payments.py`
- `commerce_ops/repository.py`
- `commerce_ops_demo.commerce_ops`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---

<a id="topic-persistence"></a>

## Persistence

- Page ID: `topic:persistence`
- Type: `topic` / `topic`
- Qualified name: `Persistence`
- Tags: `topic`

### Summary

Entities related to Persistence.

### Wiki Content

# Persistence

- [[commerce_ops_demo.commerce_ops.cli.main]]
- [[commerce_ops_demo.commerce_ops.cli.build_demo_service]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.save]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.get]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid]]
- [[commerce_ops_demo.commerce_ops.services.OrderService.cancel_order]]
- [[commerce_ops_demo.commerce_ops.services.OrderService.customer_history]]
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository]]
- [[commerce_ops_demo.commerce_ops.services.OrderService]]
- [[commerce_ops/catalog.py]]
- [[commerce_ops/cli.py]]
- [[commerce_ops/models.py]]
- [[commerce_ops/services.py]]
- [[commerce_ops/repository.py]]
- [[commerce_ops_demo.commerce_ops]]
- [[commerce_ops_demo]]

### Outgoing Links

- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `topic_mentions` -> `file:commerce_ops/catalog.py`
- `topic_mentions` -> `file:commerce_ops/cli.py`
- `topic_mentions` -> `file:commerce_ops/models.py`
- `topic_mentions` -> `file:commerce_ops/services.py`
- `topic_mentions` -> `file:commerce_ops/repository.py`
- `topic_mentions` -> `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` -> `package:commerce_ops_demo`

### Source Evidence

- `artifacts/*_cards`

### Symbols

- `commerce_ops_demo.commerce_ops.cli.main`
- `commerce_ops_demo.commerce_ops.cli.build_demo_service`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.__init__`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.list_by_customer`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.mark_paid`
- `commerce_ops_demo.commerce_ops.services.OrderService.cancel_order`
- `commerce_ops_demo.commerce_ops.services.OrderService.customer_history`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository`
- `commerce_ops_demo.commerce_ops.services.OrderService`
- `commerce_ops/catalog.py`
- `commerce_ops/cli.py`
- `commerce_ops/models.py`
- `commerce_ops/services.py`
- `commerce_ops/repository.py`
- `commerce_ops_demo.commerce_ops`
- `commerce_ops_demo`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---

<a id="topic-validation"></a>

## Validation

- Page ID: `topic:validation`
- Type: `topic` / `topic`
- Qualified name: `Validation`
- Tags: `topic`

### Summary

Entities related to Validation.

### Wiki Content

# Validation

## Validation Rules

- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__]]
  - products must contain normalize_sku(product.sku
- [[commerce_ops_demo.commerce_ops.catalog.normalize_sku]]
  - invalid when not value or not value.strip(
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get]]
  - invalid when normalized not in self.products
- [[commerce_ops_demo.commerce_ops.models.Product.reserve]]
  - invalid when qty > self.stock
  - qty > 0
- [[commerce_ops_demo.commerce_ops.models.Customer.debit]]
  - invalid when not self.can_spend(amount_cents
- [[commerce_ops_demo.commerce_ops.models.Order.mark_paid]]
  - invalid when self.status != "created
- [[commerce_ops_demo.commerce_ops.models.CartItem.validate]]
  - invalid when not self.sku
  - self.qty > 0
- [[commerce_ops_demo.commerce_ops.models.Order.mark_cancelled]]
  - invalid when self.status == "paid
- [[commerce_ops_demo.commerce_ops.models.Customer.credit]]
  - amount_cents > 0
- [[commerce_ops_demo.commerce_ops.notifications.format_currency]]
  - cents > 0
- [[commerce_ops_demo.commerce_ops.models.Product.release]]
  - qty > 0
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize]]
  - amount_cents > 0
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote]]
  - total > 0
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax]]
  - taxable_cents > 0
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon]]
  - invalid when code not in self.coupons
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.save]]
  - invalid when not order.order_id
  - orders must contain order.order_id
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund]]
  - receipt.amount_cents > 0
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.get]]
  - invalid when order_id not in self.orders
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__]]
  - tax_rate_bps > 0
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal]]
  - item.qty > 0
  - item.sku.upper( > 0

## Related Entities

- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__]]
- [[commerce_ops_demo.commerce_ops.catalog.normalize_sku]]
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items]]
- [[commerce_ops_demo.commerce_ops.cli.main]]
- [[commerce_ops_demo.commerce_ops.cli.run_checkout_demo]]
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get]]
- [[commerce_ops_demo.commerce_ops.models.CartItem.validate]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.save]]
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund]]
- [[commerce_ops_demo.commerce_ops.services.OrderService.checkout]]
- [[commerce_ops_demo.commerce_ops.catalog.ProductCatalog]]
- [[commerce_ops_demo.commerce_ops.models.Product]]
- [[commerce_ops_demo.commerce_ops.models.CartItem]]
- [[commerce_ops_demo.commerce_ops.models.Customer]]
- [[commerce_ops_demo.commerce_ops.services.OrderService]]
- [[commerce_ops/catalog.py]]
- [[commerce_ops/cli.py]]
- [[commerce_ops/models.py]]
- [[commerce_ops/services.py]]
- [[commerce_ops_demo.commerce_ops]]
- [[commerce_ops_demo.commerce_ops.models.Product.reserve]]
- [[commerce_ops_demo.commerce_ops.models.Customer.debit]]
- [[commerce_ops_demo.commerce_ops.models.Order.mark_paid]]
- [[commerce_ops_demo.commerce_ops.models.Order.mark_cancelled]]
- [[commerce_ops_demo.commerce_ops.models.Customer.credit]]
- [[commerce_ops_demo.commerce_ops.notifications.format_currency]]
- [[commerce_ops_demo.commerce_ops.models.Product.release]]
- [[commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon]]
- [[commerce_ops_demo.commerce_ops.repository.OrderRepository.get]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__]]
- [[commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal]]

### Outgoing Links

- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.main`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.CartItem.validate`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.models.Product`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.models.CartItem`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.models.Customer`
- `topic_mentions` -> `class:commerce_ops_demo.commerce_ops.services.OrderService`
- `topic_mentions` -> `file:commerce_ops/catalog.py`
- `topic_mentions` -> `file:commerce_ops/cli.py`
- `topic_mentions` -> `file:commerce_ops/models.py`
- `topic_mentions` -> `file:commerce_ops/services.py`
- `topic_mentions` -> `package:commerce_ops_demo.commerce_ops`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Product.reserve`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Customer.debit`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Customer.credit`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.notifications.format_currency`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.models.Product.release`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `topic_mentions` -> `method:commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`

### Source Evidence

- `artifacts/*_cards`

### Symbols

- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.__init__`
- `commerce_ops_demo.commerce_ops.catalog.normalize_sku`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.reserve_items`
- `commerce_ops_demo.commerce_ops.cli.main`
- `commerce_ops_demo.commerce_ops.cli.run_checkout_demo`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog.get`
- `commerce_ops_demo.commerce_ops.models.CartItem.validate`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.save`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.refund`
- `commerce_ops_demo.commerce_ops.services.OrderService.checkout`
- `commerce_ops_demo.commerce_ops.catalog.ProductCatalog`
- `commerce_ops_demo.commerce_ops.models.Product`
- `commerce_ops_demo.commerce_ops.models.CartItem`
- `commerce_ops_demo.commerce_ops.models.Customer`
- `commerce_ops_demo.commerce_ops.services.OrderService`
- `commerce_ops/catalog.py`
- `commerce_ops/cli.py`
- `commerce_ops/models.py`
- `commerce_ops/services.py`
- `commerce_ops_demo.commerce_ops`
- `commerce_ops_demo.commerce_ops.models.Product.reserve`
- `commerce_ops_demo.commerce_ops.models.Customer.debit`
- `commerce_ops_demo.commerce_ops.models.Order.mark_paid`
- `commerce_ops_demo.commerce_ops.models.Order.mark_cancelled`
- `commerce_ops_demo.commerce_ops.models.Customer.credit`
- `commerce_ops_demo.commerce_ops.notifications.format_currency`
- `commerce_ops_demo.commerce_ops.models.Product.release`
- `commerce_ops_demo.commerce_ops.payments.PaymentGateway.authorize`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.quote`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_tax`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.apply_coupon`
- `commerce_ops_demo.commerce_ops.repository.OrderRepository.get`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.__init__`
- `commerce_ops_demo.commerce_ops.pricing.PricingPolicy.calculate_subtotal`

### Graph References

- `evidence: missing; confidence: not_available; source: static_analysis`

---
