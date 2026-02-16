# Star Schema

## Overview
Star schema is a dimensional modeling pattern that structures data into a central fact table surrounded by dimension tables, with each dimension connected directly to the fact table. The layout resembles a star: one fact table in the center and dimension tables as points. It is the most common and query-friendly structure for analytical data warehouses and data marts.

## Definition
A star schema consists of one or more fact tables (holding measures and foreign keys) and multiple dimension tables (holding descriptive attributes). Each dimension table has a single primary key that is referenced by the fact table; dimensions are not normalized further in the star, so each dimension is a flat or lightly normalized table. The design prioritizes simple joins and fast analytical queries.

## Key Concepts

- **Fact Table**: Central table with measures (e.g., sales amount, quantity) and foreign keys to dimensions
- **Dimension Tables**: One per business dimension (product, customer, time, store); descriptive attributes only
- **Single-Level Dimensions**: Dimensions are denormalized (no dimension-to-dimension joins in the star)
- **Grain**: The level of detail of the fact table (e.g., one row per line item, per day, per store)
- **Surrogate Keys**: Fact table typically references dimension surrogate keys for stability and SCD support
- **Query Simplicity**: Most queries join fact to one or more dimensions with simple equality joins

## How It Works

Star schema design:

1. **Identify Business Process**: Choose the process to model (e.g., sales, orders, shipments)
2. **Define Grain**: State exactly what one row in the fact table represents
3. **Identify Dimensions**: List the dimensions that describe the process (who, what, when, where)
4. **Design Fact Table**: Create fact table with measure columns and foreign keys to each dimension
5. **Design Dimension Tables**: One table per dimension with surrogate key, natural key, and attributes
6. **Establish Relationships**: Fact table references dimension primary keys; no direct dimension-to-dimension links in the star
7. **Load and Maintain**: Populate dimensions (with SCD logic if needed) and load facts

Characteristics:
- **Denormalized Dimensions**: Redundant attributes in dimensions (e.g., category name in product dimension) to avoid extra joins
- **Few Joins**: Typical query joins fact to N dimensions with N simple joins
- **Optimized for Reads**: Not normalized for update efficiency; optimized for aggregation and filtering

## Use Cases

- **Data Warehousing**: Core schema pattern for enterprise data warehouses
- **Data Marts**: Subject-area marts (sales, marketing, finance) often use star schema
- **Business Intelligence**: BI tools and SQL analysts work naturally with star schema
- **Reporting and Dashboards**: Pre-aggregated or detail-level reporting on facts by dimensions
- **OLAP**: Many OLAP cubes are built on top of or sourced from star schemas

## Considerations

- **Redundancy**: Denormalized dimensions use more storage and can become inconsistent if not maintained
- **Dimension Size**: Very wide or frequently changing dimensions need SCD strategy
- **Multiple Facts**: Multiple business processes may require multiple fact tables (constellation) or shared dimensions
- **Grain**: Changing grain later can require schema and ETL changes

## Best Practices

- **Define Grain Explicitly**: Document what one fact row represents; validate with business
- **Use Surrogate Keys in Facts**: Reference dimension surrogate keys for SCD and stability
- **Keep Dimensions Flat in the Star**: Avoid normalizing dimensions into sub-dimensions in the same star (use snowflake only if needed)
- **Name Consistently**: Use clear naming (e.g., dim_product, fact_sales) and consistent key names
- **Document and Version**: Maintain a data dictionary and version the schema

## Related Topics

- [Dimensional Modeling](dimensional-modeling.md)
- [Snowflake Schema](snowflake-schema.md)
- [Fact Tables](fact-tables.md)
- [Dimension Tables](dimension-tables.md)
- [Slowly Changing Dimensions (SCD)](slowly-changing-dimensions.md)
- [Surrogate Keys](surrogate-keys.md)

---

**Category**: Data Modeling  
**Last Updated**: 2024
