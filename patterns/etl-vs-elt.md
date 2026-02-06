# ETL vs ELT

## Overview
ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) are two fundamental data integration patterns that differ in where and when data transformation occurs. The choice between them significantly impacts architecture, performance, and flexibility.

## Definition

**ETL (Extract, Transform, Load)**: A pattern where data is extracted from sources, transformed in a separate processing engine, then loaded into the destination system. Transformation happens before loading.

**ELT (Extract, Load, Transform)**: A pattern where data is extracted from sources, loaded into the destination system in its raw form, then transformed within the destination system. Transformation happens after loading.

## Key Concepts

- **Transformation Location**: Where data transformation occurs (separate engine vs destination)
- **Data Movement**: Amount of data moved between systems
- **Processing Power**: Where computational resources are applied
- **Schema-on-Write vs Schema-on-Read**: When data structure is defined
- **Flexibility**: Ability to change transformations without re-ingestion
- **Cost Model**: Where compute costs are incurred

## How It Works

### ETL Pattern
1. **Extract**: Pull data from source systems
2. **Transform**: Process data in a separate transformation engine (dedicated ETL tool, Spark, etc.)
   - Data cleansing, validation, aggregation
   - Schema mapping and restructuring
   - Business rule application
3. **Load**: Write transformed data to destination

### ELT Pattern
1. **Extract**: Pull data from source systems
2. **Load**: Write raw data directly to destination (data lake, data warehouse)
3. **Transform**: Process data using destination system's compute (SQL, Spark on data lake, etc.)
   - Transformations defined as queries or views
   - Multiple transformation layers possible
   - Transformations can be changed without re-ingestion

## Use Cases

### ETL is suitable for:
- **Structured Data Warehouses**: When destination has fixed schemas
- **Complex Transformations**: When transformation logic is complex and benefits from dedicated tools
- **Data Quality Requirements**: When strict validation must happen before storage
- **Legacy Systems**: When destination systems lack transformation capabilities
- **Regulatory Compliance**: When transformed data must be stored in specific formats

### ELT is suitable for:
- **Data Lakes**: When storing raw data for exploration
- **Cloud Data Warehouses**: When destination has powerful compute (Snowflake, BigQuery, Redshift)
- **Agile Analytics**: When transformation requirements change frequently
- **Multiple Use Cases**: When same raw data serves different analytical needs
- **Cost Optimization**: When leveraging destination system's scalable compute

## Considerations

- **Transformation Complexity**: ETL tools may offer better visual interfaces for complex logic
- **Data Volume**: ELT can be more efficient for large datasets (transform where data lives)
- **Destination Capabilities**: ELT requires destination to support transformation
- **Latency**: ETL may add latency; ELT can transform on-demand
- **Cost**: ETL uses separate compute; ELT uses destination compute
- **Flexibility**: ELT allows re-transformation without re-ingestion
- **Data Governance**: ETL provides more control over what gets stored

## Best Practices

- **Choose ETL when**: You need strict data quality gates, have complex transformation logic, or destination lacks compute
- **Choose ELT when**: You have powerful destination systems, need flexibility, or want to preserve raw data
- **Hybrid Approach**: Use ETL for critical transformations, ELT for exploratory analytics
- **Consider Data Volume**: Large datasets often benefit from ELT (transform where data lives)
- **Plan for Schema Evolution**: ELT provides more flexibility for changing requirements
- **Optimize Transformation Location**: Balance between transformation complexity and destination capabilities
- **Monitor Costs**: Track compute costs in both patterns

## Related Topics

- Data Lake vs Data Warehouse
- Batch Processing
- Data Transformation
- Schema-on-Read vs Schema-on-Write
- Medallion Architecture

---

**Category**: Patterns  
**Last Updated**: 2024
