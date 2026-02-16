# Data Vault Modeling

## Overview
Data Vault Modeling is a data modeling methodology designed for building scalable, flexible, and auditable data warehouses. It separates business keys from structural relationships and descriptive attributes, enabling parallel loading, historical tracking, and easy adaptation to changing business requirements. Data Vault is particularly well-suited for enterprise data warehousing where data sources change frequently, auditability is critical, and scalability is essential.

## Definition
Data Vault Modeling is a hybrid data modeling approach that combines the best of third normal form (3NF) and dimensional modeling. It structures data into three core table types: Hubs (business keys), Links (relationships), and Satellites (descriptive attributes). This design enables parallel data loading, complete historical tracking, and separation of concerns between business keys, relationships, and attributes, making it highly adaptable to changing source systems and business requirements.

## Key Concepts

- **Hubs**: Tables that store unique business keys and metadata about when records were first loaded
- **Links**: Tables that represent relationships between business keys (many-to-many relationships)
- **Satellites**: Tables that store descriptive attributes and historical changes for hubs or links
- **Business Keys**: Natural keys from source systems that uniquely identify business entities
- **Hash Keys**: Surrogate keys generated from business keys using hash functions for performance
- **Load Date Timestamps**: Metadata tracking when records were loaded into the data warehouse
- **Record Source**: Metadata tracking the source system from which data originated
- **Point-in-Time (PIT) Tables**: Pre-joined tables that simplify querying historical data
- **Bridge Tables**: Pre-aggregated tables that improve query performance for common patterns
- **Raw Vault**: Initial layer storing data as-is from source systems
- **Business Vault**: Layer with business rules and transformations applied
- **Information Marts**: Presentation layer optimized for specific business needs

## How It Works

Data Vault Modeling follows a three-layer architecture:

1. **Hub Creation**: Extract unique business keys from source systems and store them in Hub tables
2. **Link Creation**: Identify relationships between business entities and create Link tables
3. **Satellite Creation**: Extract descriptive attributes and store them in Satellite tables with history
4. **Parallel Loading**: Load hubs, links, and satellites independently and in parallel
5. **Historical Tracking**: Satellites automatically track all changes over time with load timestamps
6. **Information Marts**: Build dimensional models or other structures on top of the Data Vault

Key characteristics:
- **Separation of Concerns**: Business keys, relationships, and attributes are stored separately
- **Parallel Processing**: Hubs, links, and satellites can be loaded independently
- **Historical Preservation**: All changes are preserved with timestamps, enabling point-in-time queries
- **Source System Independence**: Changes in source systems don't require restructuring the vault
- **Scalability**: New sources can be added by creating new satellites without modifying existing structures
- **Auditability**: Complete lineage from source to target with load dates and record sources

Data Vault structure example:
- **Customer Hub**: Contains customer business keys (customer_id)
- **Product Hub**: Contains product business keys (product_id)
- **Order Link**: Links customers to products (many-to-many relationship)
- **Customer Satellite**: Contains customer attributes (name, address) with history
- **Product Satellite**: Contains product attributes (description, price) with history
- **Order Satellite**: Contains order attributes (quantity, order_date) with history

## Use Cases

- **Enterprise Data Warehousing**: Building large-scale data warehouses that integrate multiple source systems
- **Historical Data Tracking**: Scenarios requiring complete audit trails and historical data preservation
- **Rapid Source System Changes**: Environments where source systems change frequently
- **Parallel Data Loading**: Situations requiring high-performance, parallel ETL processes
- **Regulatory Compliance**: Industries requiring complete data lineage and auditability (finance, healthcare)
- **Multi-Source Integration**: Integrating data from many disparate source systems
- **Agile Data Warehousing**: Projects requiring iterative development and easy schema evolution
- **Data Lakehouse Architecture**: Foundation layer for modern data lakehouse implementations
- **Real-time Data Warehousing**: Supporting real-time or near-real-time data loading patterns
- **Master Data Management**: Managing master data with complete history and lineage

## Considerations

- **Complexity**: More complex than star schema, requiring understanding of three table types
- **Query Performance**: Raw queries against Data Vault can be slower; requires PIT and bridge tables
- **Storage Requirements**: Historical tracking increases storage needs compared to current-state models
- **Learning Curve**: Team needs training on Data Vault concepts and best practices
- **Query Complexity**: End-user queries require joining multiple tables; information marts help
- **Initial Setup**: More upfront design work compared to simpler dimensional models
- **Tool Support**: Requires ETL tools and practices that support parallel loading patterns
- **Documentation**: Needs thorough documentation of business keys, relationships, and transformations
- **Performance Tuning**: Requires careful design of PIT and bridge tables for query optimization
- **Data Quality**: Business key quality is critical; poor keys can cause data quality issues

## Best Practices

- **Identify Business Keys First**: Start by identifying unique business keys from source systems
- **Use Hash Keys**: Implement hash keys for performance, especially for large datasets
- **Separate Concerns**: Keep hubs, links, and satellites separate; don't mix concerns
- **Track Metadata**: Always include load date timestamps and record source in all tables
- **Build Information Marts**: Create dimensional models or other structures on top of Data Vault for end users
- **Design for Parallel Loading**: Structure ETL processes to load hubs, links, and satellites independently
- **Document Business Keys**: Maintain clear documentation of business key definitions and sources
- **Handle Slowly Changing Dimensions**: Use satellites to track all changes over time
- **Create PIT Tables**: Build point-in-time tables for common query patterns
- **Implement Data Quality Checks**: Validate business keys and relationships during loading
- **Plan for Growth**: Design with scalability in mind; new sources should add satellites, not restructure
- **Use Consistent Naming**: Follow consistent naming conventions for hubs, links, and satellites
- **Version Control**: Track changes to Data Vault structure and business rules
- **Performance Optimization**: Monitor and optimize PIT and bridge tables based on query patterns

## Related Topics

- [Dimensional Modeling](dimensional-modeling.md)
- [Star Schema](star-schema.md)
- [Snowflake Schema](snowflake-schema.md)
- [Fact Tables](fact-tables.md)
- [Dimension Tables](dimension-tables.md)
- [Slowly Changing Dimensions (SCD)](slowly-changing-dimensions.md)
- [Data Warehousing](../architecture/data-lake-vs-data-warehouse.md)
- [Data Lakehouse](../architecture/data-lakehouse.md)
- [Master Data Management](../governance/data-stewardship.md)
- [Data Lineage](../governance/data-lineage.md)
- [ETL vs ELT](../patterns/etl-vs-elt.md)
- Data Modeling

## Further Reading

- Data Vault 2.0 methodology and best practices
- Hub, Link, and Satellite design patterns
- Point-in-Time and Bridge table optimization techniques
- Agile data warehousing with Data Vault
- Data Vault automation and code generation

---

**Category**: Data Modeling  
**Last Updated**: 2026
