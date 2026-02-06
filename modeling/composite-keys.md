# Composite Keys

## Overview
A composite key is a primary or unique key that consists of two or more columns. It is used when a single column does not uniquely identify a row—for example, order_id + line_number for order lines, or tenant_id + user_id in multi-tenant models. Composite keys appear in both normalized and dimensional modeling (e.g., fact table grain, degenerate dimensions, or bridge tables).

## Definition
A composite key is a key made of multiple columns. The combination of values in those columns must be unique (and typically non-null) for each row. It can serve as the primary key of a table or as a unique constraint. In dimensional modeling, the grain of a fact table is often expressed as a combination of dimensions (and possibly degenerate dimensions) that together form a composite unique identifier for each fact row.

## Key Concepts

- **Multi-Column Uniqueness**: No single column is unique; the set of columns together is unique
- **Order of Columns**: Column order can matter for indexing and partitioning (e.g., leading columns in composite index)
- **Null Handling**: Typically all key columns must be non-null; null in any part can break uniqueness semantics
- **Grain Definition**: In facts, the set of dimension keys (and degenerate dimensions) that define grain is a logical composite key
- **Natural vs. Surrogate**: Composite key can be natural (business identifiers) or surrogate (e.g., multiple surrogate keys in a fact table together identify grain)
- **Join and Lookup**: Matching on composite key requires equality on all columns (or use composite surrogate)

## How It Works

Composite key usage:

1. **Identify Uniqueness**: Determine which set of columns must be unique (e.g., order_id + line_number, date_key + product_key + store_key for fact grain)
2. **Define Constraint**: Create PRIMARY KEY or UNIQUE constraint on (col1, col2, ...); ensure columns are NOT NULL or define policy for nulls
3. **Indexing**: Create index on composite key columns; order columns by selectivity or query pattern (e.g., date first for time-range queries)
4. **Joins**: When joining on composite key, use ON a.col1 = b.col1 AND a.col2 = b.col2 ...
5. **ETL**: When loading, check for duplicates on composite key; use upsert or merge keyed by composite
6. **Fact Grain**: In dimensional model, fact table grain is defined by the combination of dimension foreign keys (and degenerate dimensions); this is the logical composite key of the fact

Examples:
- **Order line**: (order_id, line_number) — natural composite key
- **Fact sales**: (date_key, product_key, store_key, customer_key) — grain; may also have surrogate fact_key as single-column PK for convenience
- **Bridge table**: (product_key, category_key) for many-to-many — composite key of relationship table
- **Multi-tenant**: (tenant_id, entity_id) — composite to scope uniqueness per tenant

## Use Cases

- **Fact Table Grain**: Define what one row represents (e.g., one row per product per store per day); composite of dimension keys
- **Order and Line Items**: Order ID + line number for order lines; header and detail in one or separate tables
- **Many-to-Many**: Bridge or association tables with composite key (e.g., student_id + course_id)
- **Multi-Tenancy**: tenant_id + id to scope uniqueness and partitioning per tenant
- **Time-Series or Snapshot**: (entity_id, date) or (entity_id, period_id) for periodic snapshots
- **Degenerate Dimension**: Transaction number + line number stored in fact table as part of grain (no separate dimension)

## Considerations

- **Complexity**: More columns in key mean more complex joins, constraints, and ETL logic
- **Index Size**: Composite indexes are larger; choose column order for common query patterns
- **Partitioning**: Some systems partition by leading columns of key; design for pruning
- **Surrogate Over Composite**: Sometimes a single surrogate key is added as PK even when composite defines grain (e.g., for joins and tools that expect single-column PK)
- **Nulls**: Define whether null is allowed in any key column; usually not for primary key

## Best Practices

- **Document Grain**: For facts, write explicit grain statement and list the columns that form the composite key
- **Minimal Key**: Use the smallest set of columns that guarantees uniqueness
- **Index Order**: Order composite index by selectivity and filter usage (e.g., high-filter columns first)
- **Consistent Order**: Use same column order in constraint, index, and join for predictability
- **Validate in ETL**: Enforce uniqueness on load; reject or handle duplicates per business rules

## Related Topics

- Surrogate Keys
- Natural Keys
- Fact Tables
- Data Granularity
- Dimensional Modeling
- Grain Definition

---

**Category**: Data Modeling  
**Last Updated**: 2024
