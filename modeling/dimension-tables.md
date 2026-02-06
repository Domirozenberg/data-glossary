# Dimension Tables

## Overview
Dimension tables hold the descriptive attributes used to filter, group, and label the measures in fact tables. They represent the "who, what, when, where" of the business process—customers, products, dates, locations, and other contextual attributes. Dimension tables are joined to fact tables via keys and provide the context that makes fact data interpretable for reporting and analytics.

## Definition
A dimension table contains a primary key (often a surrogate key), one or more natural key columns from the source, and attribute columns that describe the entity. Rows represent unique members of the dimension (e.g., one product, one customer, one date). Fact tables reference dimension primary keys; dimension attributes are used in WHERE, GROUP BY, and SELECT to slice and describe the facts.

## Key Concepts

- **Primary Key**: Unique identifier for each dimension row (typically surrogate key for stability and SCD)
- **Natural Key**: Business identifier from source (e.g., product_sku, customer_id); used for ETL matching and audit
- **Attributes**: Descriptive columns (name, category, region, type, etc.) used in reporting and filtering
- **Hierarchies**: Attributes that form levels (e.g., product → category → department); may be flattened in star or normalized in snowflake
- **Slowly Changing Dimensions (SCD)**: Strategy for keeping history when dimension attributes change (Type 1, 2, 3, etc.)
- **Role-Playing Dimensions**: Same dimension table used multiple times in a fact table with different roles (e.g., order date, ship date both reference date dimension)
- **Junk Dimensions**: Group of low-cardinality flags or codes into one dimension to avoid fact table clutter
- **Conformed Dimensions**: Dimensions shared across fact tables or marts for consistent analysis

## How It Works

Dimension table design:

1. **Identify Dimension**: Define the business entity (product, customer, date, store, etc.)
2. **Identify Attributes**: List descriptive attributes from business and source systems
3. **Choose Keys**: Define surrogate key (e.g., product_key) and natural key(s) (e.g., product_sku, source_system_id)
4. **Define SCD Strategy**: Decide how to handle changes (overwrite, new row, new column, or hybrid)
5. **Create Table**: Create dimension table with key and attributes; add SCD columns if Type 2 (effective date, end date, current flag)
6. **Load and Maintain**: Initial load and incremental updates; match on natural key and apply SCD rules
7. **Conform if Shared**: If dimension is used across marts, define and publish conformed definition and keys

Characteristics:
- **Wider, Fewer Rows**: Typically more columns than fact tables; fewer rows (all distinct members)
- **Slower Changing**: Updated less frequently than fact tables; changes governed by SCD
- **Heavily Used in Joins**: Almost every analytical query joins facts to one or more dimensions

## Use Cases

- **Filtering**: "Sales where region = West and product category = Electronics"
- **Grouping and Labeling**: "Revenue by customer segment and month"
- **Slicing and Dicing**: Pivot and drill by dimension attributes in BI tools
- **Consistent Context**: Same customer, product, or calendar definition across reports and marts
- **Historical Analysis**: SCD Type 2 allows "what did we know then?" analysis by effective date

## Considerations

- **Attribute Bloat**: Too many or rarely used attributes add storage and complexity; consider role-playing or junk dimensions
- **SCD Complexity**: Type 2 and hybrid strategies require careful ETL and key handling in facts
- **Conformance**: Shared dimensions must agree on definition and keys across fact tables and marts
- **Large Dimensions**: Very large dimensions (e.g., customer) need efficient lookups and possibly mini-dimensions for hot attributes
- **Multiple Sources**: Same dimension from multiple sources may require integration and survivorship rules

## Best Practices

- **Use Surrogate Keys**: Surrogate key as primary key; natural key for ETL and deduplication
- **Document Attributes**: Maintain data dictionary with source, definition, and SCD behavior
- **Conform Shared Dimensions**: One definition and key for dimensions used across marts
- **Design for SCD Up Front**: Choose SCD type per dimension and add required columns (effective/end date, current flag) from the start
- **Name Clearly**: Consistent prefix (e.g., dim_) and key naming (e.g., product_key, product_sk)

## Related Topics

- Dimensional Modeling
- Fact Tables
- Star Schema
- Slowly Changing Dimensions (SCD)
- Surrogate Keys
- Natural Keys
- Conformed Dimensions

---

**Category**: Data Modeling  
**Last Updated**: 2024
