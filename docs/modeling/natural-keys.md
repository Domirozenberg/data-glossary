# Natural Keys

## Overview
A natural key is a business or domain identifier that uniquely identifies an entity in the source system or in the real world (e.g., product SKU, customer ID, order number). In data warehousing and dimensional modeling, natural keys are retained as attributes for matching, deduplication, and audit, while surrogate keys are typically used as primary and foreign keys for stability and SCD support.

## Definition
A natural key is one or more attributes that uniquely identify an entity from the business perspective. It comes from the source system or domain (e.g., social security number, email, product code, composite of order_id + line_number). In the warehouse, the natural key is stored in dimension tables for ETL lookup and reconciliation but is usually not the primary key; the primary key is a surrogate key. In some operational or normalized models, the natural key may serve as the primary key.

## Key Concepts

- **Business Meaning**: Has semantic meaning (e.g., employee badge number, account number)
- **Source System Origin**: Defined by and may be owned by source system(s)
- **Uniqueness in Context**: Uniquely identifies entity within a given scope (system, domain, or globally)
- **Stability**: May change (e.g., key reassigned, format changed) or be reused in source; affects warehouse design
- **Matching and Deduplication**: Used to match incoming records to existing dimension rows and to deduplicate across sources
- **Audit and Lineage**: Used to trace warehouse rows back to source system records
- **Composite Natural Key**: Multiple columns together form the key (e.g., tenant_id + user_id)

## How It Works

Natural key in the warehouse:

1. **Identify in Source**: Determine which attribute(s) uniquely identify the entity in source and in business terms
2. **Store in Dimension**: Keep natural key as a column (or set of columns) in the dimension table; often indexed for lookup
3. **ETL Matching**: When loading dimensions, match incoming rows by natural key (and optionally source system) to decide insert vs. update (or SCD new row)
4. **Fact Load**: When loading facts, resolve dimension surrogate key by looking up dimension on natural key (and effective date if SCD Type 2); store surrogate in fact, not natural key, for join
5. **Reconciliation**: Use natural key to reconcile warehouse data to source and to support data quality checks
6. **Multi-Source**: When same entity comes from multiple sources with different natural keys, implement a mapping or master entity with one surrogate and multiple natural key attributes (e.g., source_system_id + source_natural_key)

Considerations:
- **Unstable Keys**: If source reuses or changes natural keys, warehouse must still maintain one surrogate per logical entity; use history or versioning
- **Composite Keys**: Store all parts of composite natural key; use same composite in lookup logic
- **Null and Unknown**: Define how "unknown" or "not applicable" dimension members are represented (e.g., reserved surrogate key with natural key null or 'Unknown')

## Use Cases

- **Dimension ETL**: Match incoming dimension data to existing rows by natural key to apply SCD and assign surrogate
- **Fact ETL**: Resolve dimension surrogate key from fact’s natural key (e.g., product_sku → product_key)
- **Deduplication**: Identify duplicate entities across sources using natural key (after standardization)
- **Reconciliation**: Compare warehouse counts and values to source by natural key
- **Data Quality**: Validate that natural key exists in dimension and that there are no duplicate natural keys (within same effective period)
- **Operational Reporting**: When reporting back to source system, natural key links report row to source record

## Considerations

- **Not Always Stable**: Source may change format, reassign, or reuse keys; warehouse design should not depend on natural key immutability for joins
- **Multi-Source Conflict**: Different sources may use different identifiers for same entity; need master data or mapping
- **Privacy and Compliance**: Natural keys may be PII (e.g., email, SSN); handle per policy (masking, access control)
- **Performance**: Lookup by natural key in large dimensions should be indexed; consider caching in ETL
- **Uniqueness Scope**: Uniqueness may be per source system or per tenant; define scope clearly

## Best Practices

- **Keep in Dimension**: Always store natural key in dimension for matching and audit; do not drop after surrogate assignment
- **Index for Lookup**: Index dimension on natural key (and effective date if Type 2) for fast ETL lookup
- **Document Source**: Document which source(s) and column(s) define the natural key
- **Handle Multi-Source**: If multiple natural keys map to one entity, store all (e.g., source_id + natural_key) or maintain mapping table
- **Use Surrogate for Joins**: Use surrogate key in fact table and in all warehouse-to-warehouse joins; use natural key for source integration and audit

## Related Topics

- [Surrogate Keys](surrogate-keys.md)
- [Composite Keys](composite-keys.md)
- [Dimension Tables](dimension-tables.md)
- [Slowly Changing Dimensions (SCD)](slowly-changing-dimensions.md)
- [Data Deduplication](../transformation/data-deduplication.md)
- [ETL/ELT](../patterns/etl-vs-elt.md)

---

**Category**: Data Modeling  
**Last Updated**: 2024
