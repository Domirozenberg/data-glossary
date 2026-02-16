# Data Pipeline Glossary - Index

Quick navigation to all topics organized by category.

## Architecture & Design Patterns

### Core Architecture
- [Data Pipeline Architecture](./architecture/data-pipeline-architecture.md)
- [Lambda Architecture](./architecture/lambda-architecture.md)
- [Kappa Architecture](./architecture/kappa-architecture.md)
- [Data Mesh Architecture](./architecture/data-mesh-architecture.md)
- [Data Fabric Architecture](./architecture/data-fabric-architecture.md)
- [Medallion Architecture (Bronze/Silver/Gold)](./architecture/medallion-architecture.md)
- [Data Lake vs Data Warehouse](./architecture/data-lake-vs-data-warehouse.md)
- [Data Lakehouse](./architecture/data-lakehouse.md)
- [Data Hub Architecture](./architecture/data-hub-architecture.md)

### Processing Paradigms
- [Batch Processing](./architecture/batch-processing.md)
- [Stream Processing](./architecture/stream-processing.md)
- [Micro-batch Processing](./architecture/micro-batch-processing.md)
- [Event-driven Processing](./architecture/event-driven-processing.md)
- [Real-time vs Near-real-time Processing](./architecture/real-time-vs-near-real-time.md)

### Integration Patterns
- [ETL vs ELT](./patterns/etl-vs-elt.md)
- [ETLT (Extract, Transform, Load, Transform)](./patterns/etlt.md)
- [Change Data Capture (CDC)](./ingestion/change-data-capture.md)
- [Data Replication](./patterns/data-replication.md)
- [Data Synchronization](./patterns/data-synchronization.md)

## Data Ingestion

- [Change Data Capture (CDC)](ingestion/change-data-capture.md)
- [Batch Ingestion](./ingestion/batch-ingestion.md)
- [Streaming Ingestion](./ingestion/streaming-ingestion.md)
- [API-based Ingestion](./ingestion/api-based-ingestion.md)
- [File-based Ingestion](./ingestion/file-based-ingestion.md)
- [Database Replication](./ingestion/database-replication.md)
- [Log-based Ingestion](./ingestion/log-based-ingestion.md)
- [Webhook Ingestion](./ingestion/webhook-ingestion.md)
- [Push vs Pull Ingestion](./ingestion/push-vs-pull-ingestion.md)
- [Full Load vs Incremental Load](./ingestion/full-load-vs-incremental-load.md)
- [Upsert Patterns](./ingestion/upsert-patterns.md)
- [Idempotent Ingestion](./ingestion/idempotent-ingestion.md)
- [Exactly-once Semantics](./ingestion/exactly-once-semantics.md)
- [At-least-once Semantics](./ingestion/at-least-once-semantics.md)

## Data Storage

- [Object Storage](./storage/object-storage.md)
- [Columnar Storage](./storage/columnar-storage.md)
- [Row-based Storage](./storage/row-based-storage.md)
- [Hybrid Storage](./storage/hybrid-storage.md)
- [Data Partitioning](./storage/data-partitioning.md)
- [Data Bucketing](./storage/data-bucketing.md)
- [Data Clustering](./storage/data-clustering.md)
- [Data Indexing](./storage/data-indexing.md)
- [Hot vs Cold Storage](./storage/hot-vs-cold-storage.md)
- [Data Tiering](./storage/data-tiering.md)
- [Data Archiving](./storage/data-archiving.md)
- [Data Retention Policies](./storage/data-retention-policies.md)
- [Data Lifecycle Management](./storage/data-lifecycle-management.md)
- [Storage Compression](./storage/storage-compression.md)
- [Storage Encryption](./storage/storage-encryption.md)

## Database Types & Technologies

### Relational Databases
- [Relational Database (RDBMS)](./databases/relational-database.md)
- [ACID Properties](./databases/acid-properties.md)
- [SQL (Structured Query Language)](./databases/sql.md)
- [Normalization](./databases/normalization.md)
- [Foreign Keys and Relationships](./databases/foreign-keys-relationships.md)
- [Transactions](./databases/transactions.md)
- [Database Indexing](./databases/database-indexing.md)
- [Query Optimization](./databases/query-optimization.md)
- [Database Normalization Forms](./databases/database-normalization-forms.md)

### NoSQL Databases
- [NoSQL Database Overview](./databases/nosql-database.md)
- [Document Databases](./databases/document-databases.md)
- [Key-Value Stores](./databases/key-value-stores.md)
- [Column-Family Stores (Wide-Column)](./databases/column-family-stores.md)
- [NoSQL vs SQL Trade-offs](./databases/nosql-vs-sql-trade-offs.md)
- [Eventual Consistency](./databases/eventual-consistency.md)
- [CAP Theorem](./databases/cap-theorem.md)
- [BASE Properties](./databases/base-properties.md)

### Graph Databases
- [Graph Database](./databases/graph-database.md)
- [Nodes and Edges](./databases/nodes-and-edges.md)
- [Graph Traversal](./databases/graph-traversal.md)
- [Property Graphs](./databases/property-graphs.md)
- [RDF (Resource Description Framework)](./databases/rdf.md)
- [Graph Query Languages](./databases/graph-query-languages.md)
- [Graph Algorithms](./databases/graph-algorithms.md)
- [Use Cases for Graph Databases](./databases/use-cases-graph-databases.md)

### Vector Databases
- [Vector Database](./databases/vector-database.md)
- [Embeddings](./databases/embeddings.md)
- [Similarity Search](./databases/similarity-search.md)
- [Approximate Nearest Neighbor (ANN)](./databases/approximate-nearest-neighbor.md)
- [Vector Indexing](./databases/vector-indexing.md)
- [Semantic Search](./databases/semantic-search.md)
- [Use Cases for Vector Databases](./databases/use-cases-vector-databases.md)
- [Vector Database vs Traditional Database](./databases/vector-database-vs-traditional-database.md)

### Specialized Databases
- [Time-Series Databases](./databases/time-series-databases.md)
- [In-Memory Databases](./databases/in-memory-databases.md)
- [NewSQL Databases](./databases/newsql-databases.md)
- [Multi-Model Databases](./databases/multi-model-databases.md)
- [Distributed Databases](./databases/distributed-databases.md)
- [Blockchain Databases](./databases/blockchain-databases.md)
- [Spatial Databases](./databases/spatial-databases.md)
- [Search Databases](./databases/search-databases.md)

### Database Concepts
- [Database Sharding](./databases/database-sharding.md)
- [Database Replication](./databases/database-replication.md)
- [Master-Slave Replication](./databases/master-slave-replication.md)
- [Master-Master Replication](./databases/master-master-replication.md)
- [Database Clustering](./databases/database-clustering.md)
- [Database Partitioning](./databases/database-partitioning.md)
- [Horizontal vs Vertical Scaling](./databases/horizontal-vs-vertical-scaling.md)
- [Database Backup and Recovery](./databases/database-backup-recovery.md)
- [Database Migration](./databases/database-migration.md)
- [Database Versioning](./databases/database-versioning.md)

### Database Selection
- [Choosing the Right Database](./databases/choosing-right-database.md)
- [Database Performance Considerations](./databases/database-performance-considerations.md)
- [Database Scalability Patterns](./databases/database-scalability-patterns.md)
- [Polyglot Persistence](./databases/polyglot-persistence.md)
- [Database as a Service (DBaaS)](./databases/database-as-a-service.md)

## Data Transformation

- [Data Cleansing](./transformation/data-cleansing.md)
- [Data Normalization](./transformation/data-normalization.md)
- [Data Denormalization](./transformation/data-denormalization.md)
- [Data Aggregation](./transformation/data-aggregation.md)
- [Data Enrichment](./transformation/data-enrichment.md)
- [Data Joining](./transformation/data-joining.md)
- [Data Filtering](./transformation/data-filtering.md)
- [Data Pivoting/Unpivoting](./transformation/data-pivoting-unpivoting.md)
- [Schema Evolution](./transformation/schema-evolution.md)
- [Schema Drift Handling](./transformation/schema-drift-handling.md)
- [Data Type Conversion](./transformation/data-type-conversion.md)
- [Data Format Conversion](./transformation/data-format-conversion.md)
- [Data Deduplication](./transformation/data-deduplication.md)
- [Data Masking](./transformation/data-masking.md)
- [Data Anonymization](./transformation/data-anonymization.md)
- [Data Standardization](./transformation/data-standardization.md)

## Data Modeling

- [Dimensional Modeling](./modeling/dimensional-modeling.md)
- [Star Schema](./modeling/star-schema.md)
- [Snowflake Schema](./modeling/snowflake-schema.md)
- [Fact Tables](./modeling/fact-tables.md)
- [Dimension Tables](./modeling/dimension-tables.md)
- [Normalized vs Denormalized Models](./modeling/normalized-vs-nonnormalized.md)
- [Data Vault Modeling](./modeling/data-vault-modeling.md)
- [Graph Modeling](./modeling/graph-modeling.md)
- [Anchor Modeling](./modeling/anchor-modeling.md)
- [Slowly Changing Dimensions (SCD)](./modeling/slowly-changing-dimensions.md)
- [Surrogate Keys](./modeling/surrogate-keys.md)
- [Natural Keys](./modeling/natural-keys.md)
- [Composite Keys](./modeling/composite-keys.md)
- [Data Granularity](./modeling/data-granularity.md)
- [Data Aggregation Levels](./modeling/data-aggregation-levels.md)

## Data Quality & Validation

- [Data Completeness](quality/data-completeness.md)
- [Data Accuracy](quality/data-accuracy.md)
- [Data Consistency](quality/data-consistency.md)
- [Data Validity](quality/data-validity.md)
- [Data Timeliness](quality/data-timeliness.md)
- [Data Uniqueness](quality/data-uniqueness.md)
- [Data Integrity](quality/data-integrity.md)
- [Data Profiling](./quality/data-profiling.md)
- [Data Validation Rules](quality/data-validation-rules.md)
- [Data Quality Metrics](quality/data-quality-metrics.md)
- [Data Quality Monitoring](quality/data-quality-monitoring.md)
- [Anomaly Detection](quality/anomaly-detection.md)
- [Data Quality Scoring](quality/data-quality-scoring.md)
- [Data Quality Gates](quality/data-quality-gates.md)

## Data Orchestration

- [Pipeline Orchestration](./orchestration/pipeline-orchestration.md)
- [Workflow Scheduling](orchestration/workflow-scheduling.md)
- [Dependency Management](orchestration/dependency-management.md)
- [Task Dependencies](orchestration/task-dependencies.md)
- [Pipeline Triggers](orchestration/pipeline-triggers.md)
- [Error Handling](orchestration/error-handling.md)
- [Retry Strategies](orchestration/retry-strategies.md)
- [Circuit Breakers](orchestration/circuit-breakers.md)
- [Sequential Execution](orchestration/sequential-execution.md)
- [Parallel Execution](orchestration/parallel-execution.md)
- [Conditional Execution](orchestration/conditional-execution.md)
- [Loop Patterns](orchestration/loop-patterns.md)
- [Fan-out/Fan-in Patterns](orchestration/fan-out-fan-in-patterns.md)
- [Pipeline Chaining](orchestration/pipeline-chaining.md)

## Data Formats & Serialization

- [JSON](formats/json.md)
- [Avro](formats/avro.md)
- [Parquet](./formats/parquet.md)
- [ORC](formats/orc.md)
- [CSV](formats/csv.md)
- [XML](formats/xml.md)
- [Protocol Buffers](formats/protocol-buffers.md)
- [Delta Format](formats/delta-format.md)
- [Schema Evolution](./transformation/schema-evolution.md)
- [Backward Compatibility](formats/backward-compatibility.md)
- [Forward Compatibility](formats/forward-compatibility.md)
- [Schema Registry](formats/schema-registry.md)
- [Data Compression](formats/data-compression.md)
- [Data Encoding](formats/data-encoding.md)

## Data Governance

- [Data Catalog](./governance/data-catalog.md)
- [Data Lineage](governance/data-lineage.md)
- [Data Dictionary](governance/data-dictionary.md)
- [Metadata Management](governance/metadata-management.md)
- [Data Classification](governance/data-classification.md)
- [Data Ownership](governance/data-ownership.md)
- [Data Stewardship](governance/data-stewardship.md)
- [Data Privacy](governance/data-privacy.md)
- [Data Encryption (at rest, in transit)](governance/data-encryption-at-rest-in-transit.md)
- [Access Control](governance/access-control.md)
- [Data Masking](governance/data-masking.md)
- [PII Handling](governance/pii-handling.md)
- [GDPR Compliance](governance/gdpr-compliance.md)
- [Data Retention Policies](./storage/data-retention-policies.md)
- [Audit Logging](governance/audit-logging.md)

## Data Observability

- [Data Observability](./observability/data-observability.md)
- [Data Monitoring](observability/data-monitoring.md)
- [Data Logging](observability/data-logging.md)
- [Data Metrics](observability/data-metrics.md)
- [Data Tracing](observability/data-tracing.md)
- [Data Alerting](observability/data-alerting.md)
- [Data Health Checks](observability/data-health-checks.md)
- [Pipeline Performance Monitoring](observability/pipeline-performance-monitoring.md)

## Advanced Concepts

### Performance Optimization
- [Data Partitioning](./storage/data-partitioning.md) Strategies
- [Query Optimization](./databases/query-optimization.md)
- [Caching Strategies](advanced/caching-strategies.md)
- [Materialized Views](advanced/materialized-views.md)
- [Incremental Processing](advanced/incremental-processing.md)
- [Parallel Processing](advanced/parallel-processing.md)
- [Resource Management](advanced/resource-management.md)

### Scalability & Reliability
- [Horizontal Scaling](advanced/horizontal-scaling.md)
- [Vertical Scaling](advanced/vertical-scaling.md)
- [Auto-scaling](advanced/auto-scaling.md)
- [Fault Tolerance](advanced/fault-tolerance.md)
- [Disaster Recovery](advanced/disaster-recovery.md)
- [High Availability](advanced/high-availability.md)
- [Data Replication](./patterns/data-replication.md) Strategies

### Modern Techniques
- [Data Versioning](./advanced/data-versioning.md)
- [Feature Stores](./advanced/feature-stores.md)
- [Data Contracts](advanced/data-contracts.md)
- [Data Testing](advanced/data-testing.md)
- [Data Observability](./observability/data-observability.md) Platforms
- [Reverse ETL](advanced/reverse-etl.md)
- [Data Activation](advanced/data-activation.md)

## AI & Machine Learning

### ML Pipeline Concepts
- [Machine Learning Pipelines](ai-ml/machine-learning-pipelines.md)
- [MLOps (Machine Learning Operations)](./ai-ml/mlops.md)
- [Model Training Pipelines](./ai-ml/model-training-pipelines.md)
- [Model Inference Pipelines](ai-ml/model-inference-pipelines.md)
- [Model Serving](ai-ml/model-serving.md)
- [Model Deployment](ai-ml/model-deployment.md)
- [Model Versioning](ai-ml/model-versioning.md)
- [Model Registry](ai-ml/model-registry.md)
- [Model Monitoring](ai-ml/model-monitoring.md)
- [Model Drift Detection](ai-ml/model-drift-detection.md)

### Feature Engineering
- [Feature Engineering](./ai-ml/feature-engineering.md)
- [Feature Selection](ai-ml/feature-selection.md)
- [Feature Transformation](ai-ml/feature-transformation.md)
- [Feature Scaling](ai-ml/feature-scaling.md)
- [Feature Encoding](ai-ml/feature-encoding.md)
- [Feature Stores](./ai-ml/feature-stores.md)
- [Online vs Offline Features](ai-ml/online-vs-offline-features.md)
- [Feature Pipelines](ai-ml/feature-pipelines.md)
- [Feature Validation](ai-ml/feature-validation.md)

### Data for ML
- [Training Data Preparation](ai-ml/training-data-preparation.md)
- [Data Labeling](ai-ml/data-labeling.md)
- [Data Augmentation](ai-ml/data-augmentation.md)
- [Train/Validation/Test Splits](ai-ml/train-validation-test-splits.md)
- [Data Sampling for ML](ai-ml/data-sampling-for-ml.md)
- [Imbalanced Data Handling](ai-ml/imbalanced-data-handling.md)
- [Data Quality for ML](ai-ml/data-quality-for-ml.md)
- [ML Data Lineage](ai-ml/ml-data-lineage.md)

### AI Integration
- [AI-powered Data Processing](ai-ml/ai-powered-data-processing.md)
- [Automated Data Quality](ai-ml/automated-data-quality.md)
- [AI-assisted Data Discovery](ai-ml/ai-assisted-data-discovery.md)
- [Natural Language Processing in Pipelines](ai-ml/natural-language-processing-in-pipelines.md)
- [Computer Vision Data Pipelines](ai-ml/computer-vision-data-pipelines.md)
- [LLM Integration in Data Pipelines](ai-ml/llm-integration-in-data-pipelines.md)
- [Generative AI for Data](ai-ml/generative-ai-for-data.md)
- [Model Context Protocol (MCP)](./ai-ml/mcp.md)

## Conversational Analytics

### Conversational Interfaces
- [Conversational Analytics](./conversational-analytics/conversational-analytics.md)
- [Natural Language Querying](./conversational-analytics/natural-language-querying.md)
- [Chat-based Data Exploration](conversational-analytics/chat-based-data-exploration.md)
- [Voice-enabled Analytics](conversational-analytics/voice-enabled-analytics.md)
- [AI-powered Data Q&A](conversational-analytics/ai-powered-data-qa.md)
- [Semantic Search](./databases/semantic-search.md) in Data
- [LLM-based Data Discovery](./conversational-analytics/LLM-based-data-discovery.md)
- [Conversational BI](conversational-analytics/conversational-bi.md)

### AI-Assisted Exploration
- [AI-powered Data Cataloging](./governance/data-catalog.md)
- [Intelligent Data Recommendations](conversational-analytics/intelligent-data-recommendations.md)
- [Automated Insight Generation](conversational-analytics/automated-insight-generation.md)
- [Natural Language to SQL](./ai-ml/natural-language-to-sql.md)
- [Query Understanding](conversational-analytics/query-understanding.md)
- [Context-aware Data Queries](conversational-analytics/context-aware-data-queries.md)
- [Multi-modal Data Interaction](conversational-analytics/multi-modal-data-interaction.md)

## Analytics & Business Intelligence

### Analytics Concepts
- [Business Intelligence (BI)](./analytics/business-intelligence.md)
- [Analytics Pipelines](analytics/analytics-pipelines.md)
- [Reporting Pipelines](analytics/reporting-pipelines.md)
- [Dashboard Creation](analytics/dashboard-creation.md)
- [Ad-hoc Analytics](analytics/ad-hoc-analytics.md)
- [Self-service Analytics](analytics/self-service-analytics.md)
- [Embedded Analytics](analytics/embedded-analytics.md)
- [Real-time Analytics](analytics/real-time-analytics.md)
- [Predictive Analytics](analytics/predictive-analytics.md)
- [Prescriptive Analytics](analytics/prescriptive-analytics.md)

### Analytical Processing
- [OLAP (Online Analytical Processing)](./analytics/olap.md)
- [OLTP vs OLAP](analytics/oltp-vs-olap.md)
- [Multidimensional Analysis](analytics/multidimensional-analysis.md)
- [Data Cubes](analytics/data-cubes.md)
- [Roll-up and Drill-down](analytics/roll-up-and-drill-down.md)
- [Slice and Dice](analytics/slice-and-dice.md)
- [Pivot Operations](analytics/pivot-operations.md)
- [Time-series Analysis](analytics/time-series-analysis.md)
- [Cohort Analysis](analytics/cohort-analysis.md)

### Query & Reporting
- [SQL Analytics](analytics/sql-analytics.md)
- [Query Engines](analytics/query-engines.md)
- [Query Optimization](./databases/query-optimization.md) for Analytics
- [Materialized Views](advanced/materialized-views.md) for Analytics
- [Report Generation](analytics/report-generation.md)
- [Scheduled Reporting](analytics/scheduled-reporting.md)
- [Report Distribution](analytics/report-distribution.md)
- [Interactive Dashboards](analytics/interactive-dashboards.md)
- [Data Visualization](analytics/data-visualization.md)
- [Metrics and KPIs](analytics/metrics-and-kpis.md)

### Analytics Delivery
- [Data Marts](analytics/data-marts.md)
- [Analytical Databases](analytics/analytical-databases.md)
- [Columnar Analytics](analytics/columnar-analytics.md)
- [In-memory Analytics](analytics/in-memory-analytics.md)
- [Streaming Analytics](analytics/streaming-analytics.md)
- [Event Analytics](analytics/event-analytics.md)
- [User Analytics](analytics/user-analytics.md)
- [Product Analytics](analytics/product-analytics.md)

## Cross-Cutting Topics

- [Data Pipeline Best Practices](./cross-cutting/data-pipeline-best-practices.md)
- [Data Pipeline Anti-patterns](cross-cutting/data-pipeline-anti-patterns.md)
- [Data Pipeline Testing Strategies](cross-cutting/data-pipeline-testing-strategies.md)
- [Data Pipeline Documentation](cross-cutting/data-pipeline-documentation.md)
- [Data Pipeline Cost Optimization](cross-cutting/data-pipeline-cost-optimization.md)
- [Data Pipeline Migration Strategies](cross-cutting/data-pipeline-migration-strategies.md)
- [MkDocs](./cross-cutting/mkdocs.md)

## Version Control & Git

- [Git and GitHub](./version-control/git-and-github.md)
- [Git Repository and Workflow](./version-control/git-repository-and-workflow.md)
- [Git Clone and Remotes](./version-control/git-clone-and-remotes.md)
- [Git Commit and Status](./version-control/git-commit-and-status.md)
- [Git Push and Pull](./version-control/git-push-and-pull.md)
- [Git Branches](./version-control/git-branches.md)
- [Git Merge](./version-control/git-merge.md)
- [GitHub Pull Requests](./version-control/github-pull-requests.md)

---

*Note: Topics in bold are completed. Others are placeholders for future content.*
