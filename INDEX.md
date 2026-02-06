# Data Pipeline Glossary - Index

Quick navigation to all topics organized by category.

## Architecture & Design Patterns

### Core Architecture
- [[[[Data Pipeline Architecture](architecture/data-pipeline-architecture.md)](./architecture/data-pipeline-architecture.md)](./architecture/data-pipeline-architecture.md)](./architecture/data-pipeline-architecture.md)
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
- [[[[ETL vs ELT](patterns/etl-vs-elt.md)](./patterns/etl-vs-elt.md)](./patterns/etl-vs-elt.md)](./patterns/etl-vs-elt.md)
- ETLT (Extract, Transform, Load, Transform)
- Change Data Capture (CDC)
- [Data Replication](./patterns/data-replication.md)
- [Data Synchronization](./patterns/data-synchronization.md)

## Data Ingestion

- [Change Data Capture (CDC)](ingestion/change-data-capture.md)
- [Batch Ingestion](./ingestion/batch-ingestion.md)
- [Streaming Ingestion](./ingestion/streaming-ingestion.md)
- [API-based Ingestion](./ingestion/api-based-ingestion.md)
- [File-based Ingestion](./ingestion/file-based-ingestion.md)
- [[[[Database Replication](./databases/database-replication.md)](./ingestion/database-replication.md)](./ingestion/database-replication.md)](./ingestion/database-replication.md)
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
- Relational Database (RDBMS)
- [ACID Properties](./databases/acid-properties.md)
- SQL (Structured Query Language)
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
- Column-Family Stores (Wide-Column)
- [NoSQL vs SQL Trade-offs](./databases/nosql-vs-sql-trade-offs.md)
- [Eventual Consistency](./databases/eventual-consistency.md)
- [CAP Theorem](./databases/cap-theorem.md)
- [BASE Properties](./databases/base-properties.md)

### Graph Databases
- [Graph Database](./databases/graph-database.md)
- [Nodes and Edges](./databases/nodes-and-edges.md)
- [Graph Traversal](./databases/graph-traversal.md)
- [Property Graphs](./databases/property-graphs.md)
- RDF (Resource Description Framework)
- [Graph Query Languages](./databases/graph-query-languages.md)
- [Graph Algorithms](./databases/graph-algorithms.md)
- [Use Cases for Graph Databases](./databases/use-cases-graph-databases.md)

### Vector Databases
- [Vector Database](./databases/vector-database.md)
- [Embeddings](./databases/embeddings.md)
- [Similarity Search](./databases/similarity-search.md)
- Approximate Nearest Neighbor (ANN)
- [Vector Indexing](./databases/vector-indexing.md)
- [Semantic Search](./databases/semantic-search.md)
- [Use Cases for Vector Databases](./databases/use-cases-vector-databases.md)
- [Vector Database](./databases/vector-database.md) vs Traditional Database

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
- [[[[Database Replication](./databases/database-replication.md)](./ingestion/database-replication.md)](./ingestion/database-replication.md)](./ingestion/database-replication.md)
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
- Database as a Service (DBaaS)

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

- Data Completeness
- Data Accuracy
- Data Consistency
- Data Validity
- Data Timeliness
- Data Uniqueness
- Data Integrity
- [Data Profiling](./quality/data-profiling.md)
- Data Validation Rules
- Data Quality Metrics
- Data Quality Monitoring
- Anomaly Detection
- Data Quality Scoring
- Data Quality Gates

## Data Orchestration

- [Pipeline Orchestration](./orchestration/pipeline-orchestration.md)
- Workflow Scheduling
- Dependency Management
- Task Dependencies
- Pipeline Triggers
- Error Handling
- Retry Strategies
- Circuit Breakers
- Sequential Execution
- Parallel Execution
- Conditional Execution
- Loop Patterns
- Fan-out/Fan-in Patterns
- Pipeline Chaining

## Data Formats & Serialization

- JSON
- Avro
- [Parquet](./formats/parquet.md)
- ORC
- CSV
- XML
- Protocol Buffers
- Delta Format
- [Schema Evolution](./transformation/schema-evolution.md)
- Backward Compatibility
- Forward Compatibility
- Schema Registry
- Data Compression
- Data Encoding

## Data Governance

- [Data Catalog](./governance/data-catalog.md)
- Data Lineage
- Data Dictionary
- Metadata Management
- Data Classification
- Data Ownership
- Data Stewardship
- Data Privacy
- Data Encryption (at rest, in transit)
- Access Control
- Data Masking
- PII Handling
- GDPR Compliance
- [Data Retention Policies](./storage/data-retention-policies.md)
- Audit Logging

## Data Observability

- [Data Observability](./observability/data-observability.md)
- Data Monitoring
- Data Logging
- Data Metrics
- Data Tracing
- Data Alerting
- Data Health Checks
- Pipeline Performance Monitoring

## Advanced Concepts

### Performance Optimization
- [Data Partitioning](./storage/data-partitioning.md) Strategies
- [Query Optimization](./databases/query-optimization.md)
- Caching Strategies
- Materialized Views
- Incremental Processing
- Parallel Processing
- Resource Management

### Scalability & Reliability
- Horizontal Scaling
- Vertical Scaling
- Auto-scaling
- Fault Tolerance
- Disaster Recovery
- High Availability
- [Data Replication](./patterns/data-replication.md) Strategies

### Modern Techniques
- [Data Versioning](./advanced/data-versioning.md)
- Feature Stores
- Data Contracts
- Data Testing
- [Data Observability](./observability/data-observability.md) Platforms
- Reverse ETL
- Data Activation

## AI & Machine Learning

### ML Pipeline Concepts
- Machine Learning Pipelines
- MLOps (Machine Learning Operations)
- [Model Training Pipelines](./ai-ml/model-training-pipelines.md)
- Model Inference Pipelines
- Model Serving
- Model Deployment
- Model Versioning
- Model Registry
- Model Monitoring
- Model Drift Detection

### Feature Engineering
- [Feature Engineering](./ai-ml/feature-engineering.md)
- Feature Selection
- Feature Transformation
- Feature Scaling
- Feature Encoding
- Feature Stores
- Online vs Offline Features
- Feature Pipelines
- Feature Validation

### Data for ML
- Training Data Preparation
- Data Labeling
- Data Augmentation
- Train/Validation/Test Splits
- Data Sampling for ML
- Imbalanced Data Handling
- Data Quality for ML
- ML Data Lineage

### AI Integration
- AI-powered Data Processing
- Automated Data Quality
- AI-assisted Data Discovery
- Natural Language Processing in Pipelines
- Computer Vision Data Pipelines
- LLM Integration in Data Pipelines
- Generative AI for Data
- [Model Context Protocol (MCP)](./ai-ml/mcp.md)

## Conversational Analytics

### Conversational Interfaces
- [Conversational Analytics](./conversational-analytics/conversational-analytics.md)
- [Natural Language Querying](./conversational-analytics/natural-language-querying.md)
- Chat-based Data Exploration
- Voice-enabled Analytics
- AI-powered Data Q&A
- [Semantic Search](./databases/semantic-search.md) in Data
- [[[LLM-based Data Discovery](conversational-analytics/LLM-based-data-discovery.md)](./conversational-analytics/LLM-based-data-discovery.md)](./conversational-analytics/LLM-based-data-discovery.md)
- Conversational BI

### AI-Assisted Exploration
- AI-powered Data Cataloging
- Intelligent Data Recommendations
- Automated Insight Generation
- [[[Natural Language to SQL](ai-ml/natural-language-to-sql.md)](./ai-ml/natural-language-to-sql.md)](./ai-ml/natural-language-to-sql.md)
- Query Understanding
- Context-aware Data Queries
- Multi-modal Data Interaction

## Analytics & Business Intelligence

### Analytics Concepts
- Business Intelligence (BI)
- Analytics Pipelines
- Reporting Pipelines
- Dashboard Creation
- Ad-hoc Analytics
- Self-service Analytics
- Embedded Analytics
- Real-time Analytics
- Predictive Analytics
- Prescriptive Analytics

### Analytical Processing
- OLAP (Online Analytical Processing)
- OLTP vs OLAP
- Multidimensional Analysis
- Data Cubes
- Roll-up and Drill-down
- Slice and Dice
- Pivot Operations
- Time-series Analysis
- Cohort Analysis

### Query & Reporting
- SQL Analytics
- Query Engines
- [Query Optimization](./databases/query-optimization.md) for Analytics
- Materialized Views for Analytics
- Report Generation
- Scheduled Reporting
- Report Distribution
- Interactive Dashboards
- Data Visualization
- Metrics and KPIs

### Analytics Delivery
- Data Marts
- Analytical Databases
- Columnar Analytics
- In-memory Analytics
- Streaming Analytics
- Event Analytics
- User Analytics
- Product Analytics

## Cross-Cutting Topics

- [Data Pipeline Best Practices](./cross-cutting/data-pipeline-best-practices.md)
- Data Pipeline Anti-patterns
- Data Pipeline Testing Strategies
- Data Pipeline Documentation
- Data Pipeline Cost Optimization
- Data Pipeline Migration Strategies

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
