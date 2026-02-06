# ELT (Extract, Load, Transform)

## Overview
ELT (Extract, Load, Transform) is a data integration pattern where data is extracted from sources, loaded into the destination system in its raw form, and then transformed within the destination system. This approach leverages the processing power of modern data platforms and provides more flexibility than traditional ETL.

## Definition
ELT is a three-phase data integration process: Extract (retrieving data from sources), Load (loading raw data into destination), and Transform (transforming data using destination system's compute). Unlike ETL, transformation happens after loading, using the destination system's processing capabilities.

## Key Concepts

- **Extract**: Reading data from source systems
- **Load**: Loading raw data into destination (data lake, warehouse)
- **Transform**: Transforming data within destination system
- **Schema-on-Read**: Schema applied when reading/querying
- **Destination Compute**: Uses destination system's processing power
- **Raw Data Preservation**: Raw data preserved for reprocessing
- **Flexibility**: Transformations can be changed without re-ingestion
- **Cloud Data Warehouses**: Leverages powerful cloud data platforms

## How It Works

ELT process follows these steps:

1. **Extract Phase**:
   - Connect to source systems
   - Extract data (full or incremental)
   - Minimal or no transformation
   - Preserve original data format

2. **Load Phase**:
   - Load raw data into destination
   - Store in native or optimized formats
   - Maintain data as-is
   - Fast loading with minimal processing

3. **Transform Phase**:
   - Transform data using destination compute (SQL, Spark, etc.)
   - Apply business logic and transformations
   - Create views or materialized tables
   - Multiple transformation layers possible

## Use Cases

- **Data Lakes**: Loading data into data lakes
- **Cloud Data Warehouses**: Leveraging cloud warehouse compute
- **Agile Analytics**: When transformation requirements change frequently
- **Exploratory Analytics**: Preserving raw data for exploration
- **Multiple Use Cases**: Same raw data serving different analytical needs
- **Cost Optimization**: Leveraging destination system's scalable compute
- **Modern Data Stack**: Building modern data platforms

## Considerations

- **Destination Capabilities**: Requires destination with transformation capabilities
- **Compute Costs**: Transformation uses destination compute resources
- **Data Volume**: Loading large volumes of raw data
- **Transformation Complexity**: Complex transformations in SQL/query language
- **Latency**: Transformation happens on-demand or in separate jobs
- **Storage Costs**: Storing raw data increases storage requirements

## Best Practices

- **Leverage Destination Compute**: Use destination system's optimization
- **Optimize Storage Formats**: Use efficient formats (Parquet, Delta)
- **Design Transformation Layers**: Plan transformation layers (Bronze/Silver/Gold)
- **Version Transformations**: Track transformation logic versions
- **Monitor Costs**: Track compute and storage costs
- **Preserve Raw Data**: Never delete raw data
- **Optimize Queries**: Optimize transformation queries
- **Document Transformations**: Document transformation logic

## Related Topics

- ETL (Extract, Transform, Load)
- Data Lake
- Data Lakehouse
- Schema-on-Read
- Data Transformation
- Medallion Architecture

---

**Category**: Patterns  
**Last Updated**: 2024
