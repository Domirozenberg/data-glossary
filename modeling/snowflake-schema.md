# Snowflake Schema

## Overview
Snowflake schema is a dimensional modeling pattern that normalizes dimension tables so that hierarchical or repeated attributes are stored in separate tables, reducing redundancy. The fact table still sits at the center, but dimensions are "snowflaked" into multiple related tables, forming a shape that can resemble a snowflake when diagrammed.

## Definition
A snowflake schema extends the star schema by normalizing dimension tables. Instead of one flat dimension table (e.g., product with category name and department name), the snowflake has a product dimension that references a category dimension, which may reference a department dimension. The fact table still references the primary dimension (e.g., product key), but attribute hierarchies are broken out into separate tables to eliminate redundancy and enforce consistency.

## Key Concepts

- **Normalized Dimensions**: Dimension attributes are split into multiple tables by hierarchy or grouping
- **Dimension Hierarchies**: Parent-child relationships between dimension tables (e.g., product → category → department)
- **Reduced Redundancy**: Each attribute value (e.g., category name) stored once; dimensions reference other dimensions
- **Referential Integrity**: Strong normalization supports consistent lookup and smaller dimension storage
- **More Joins**: Queries that need hierarchy levels require additional joins through the snowflaked dimensions
- **Grain Unchanged**: Fact table grain is the same as in star schema; only dimension structure differs

## How It Works

Snowflake schema design:

1. **Start from Star**: Begin with a star schema (fact + dimensions)
2. **Identify Hierarchies**: Find attributes in dimensions that form hierarchies or repeated groupings (e.g., category, region, calendar levels)
3. **Extract Sub-dimensions**: Create separate tables for each level (e.g., dim_category, dim_department)
4. **Replace Attributes with Keys**: In the main dimension (e.g., dim_product), replace category name with category_key pointing to dim_category
5. **Preserve Fact Links**: Fact table still references the primary dimension (e.g., product_key); no change to fact grain
6. **Load and Maintain**: Load hierarchy tables first, then dimensions, then facts; maintain referential integrity

Characteristics:
- **Normalized**: Conforms to normalization rules; good for consistency and storage when hierarchies are large
- **More Tables**: More dimension tables and more joins than star
- **Query Complexity**: Reporting across hierarchy levels requires joining through the snowflake
- **ETL Complexity**: More tables to load and keep in sync

## Use Cases

- **Large Hierarchies**: When dimension attributes have deep or wide hierarchies (e.g., organizational structure, product taxonomies)
- **Shared Lookups**: When the same lookup (e.g., calendar, geography) is used across many dimensions and should be stored once
- **Storage and Consistency**: When minimizing redundancy and enforcing single source of truth for attributes is important
- **Regulatory or Governance**: When normalized structures are required for audit or compliance
- **Mixed Workloads**: When some queries benefit from normalized dimensions and storage savings matter

## Considerations

- **Join Cost**: More joins can hurt query performance compared to a flat star
- **Complexity**: More tables and relationships to document and maintain
- **BI Tool Support**: Some tools assume star schema; snowflake may need views or semantic layer to present a flatter model
- **When to Use**: Often star is preferred for simplicity and performance unless redundancy or consistency demands snowflake

## Best Practices

- **Snowflake Only Where It Pays**: Use for large, shared hierarchies; keep simple dimensions as star
- **Document Hierarchy**: Clearly document dimension hierarchy and join paths for report authors
- **Consider Views**: Provide star-like views (flattened) for common reporting if the physical model is snowflake
- **Consistent Naming**: Use clear names (e.g., dim_product, dim_category) and key naming (product_key, category_key)
- **Maintain Referential Integrity**: Enforce FKs and validate during ETL

## Related Topics

- Dimensional Modeling
- Star Schema
- Fact Tables
- Dimension Tables
- Data Normalization
- Data Denormalization

---

**Category**: Data Modeling  
**Last Updated**: 2024
