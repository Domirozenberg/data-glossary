# Fact Tables

## Overview
Fact tables are the central tables in a dimensional model that store quantitative measures (metrics) and foreign keys linking to dimension tables. Each row typically represents an event or a snapshot at a defined grain (e.g., one row per sales line item, per day per product). Fact tables are the primary focus of analytical queries—filtering, grouping, and aggregating measures by dimensions.

## Definition
A fact table holds measurements from a business process. It contains foreign key columns that reference the primary keys of dimension tables and one or more measure (numeric) columns. The combination of dimension keys (and optionally degenerate dimensions) defines the grain of the fact table. Facts are usually additive (e.g., sales amount, quantity) or semi-additive (e.g., balance), and sometimes non-additive (e.g., ratio).

## Key Concepts

- **Measures**: Numeric values that are summed, averaged, or aggregated (e.g., revenue, quantity, count)
- **Foreign Keys**: References to dimension table primary keys (e.g., product_key, customer_key, date_key)
- **Grain**: The level of detail—what one row represents (e.g., one line item, one day per store)
- **Additive**: Measures that can be summed across dimensions (e.g., sales amount)
- **Semi-additive**: Measures that can be summed across some dimensions but not others (e.g., balance—sum across accounts, not across time)
- **Non-additive**: Measures that should not be summed (e.g., ratios, averages); store components and compute in query
- **Degenerate Dimensions**: Attributes that belong to the transaction but do not warrant a dimension table (e.g., order number, line number); stored as columns in the fact table
- **Fact Types**: Transaction (event-level), periodic snapshot (state at intervals), accumulating snapshot (process with milestones)

## How It Works

Fact table design:

1. **Choose Business Process**: Identify the process (e.g., sales, orders, inventory)
2. **Define Grain**: State precisely what one row represents (e.g., one row per order line per day)
3. **Identify Dimensions**: List dimensions that describe the process; add foreign key columns for each
4. **Identify Measures**: List numeric measures; classify as additive, semi-additive, or non-additive
5. **Identify Degenerate Dimensions**: Add transaction-level attributes that stay in the fact table
6. **Choose Fact Type**: Transaction (event), periodic snapshot, or accumulating snapshot
7. **Create Table**: Create fact table with keys and measures; establish relationships to dimensions
8. **Load**: Load from source (ETL/ELT); ensure grain is consistent and keys resolve to dimensions

Fact types:
- **Transaction**: One row per event (e.g., sale, click); most common
- **Periodic Snapshot**: One row per period per entity (e.g., daily balance per account); for state-over-time
- **Accumulating Snapshot**: One row per process instance with dates/measures at milestones (e.g., order: order date, ship date, delivery date); for pipeline analysis

## Use Cases

- **Sales and Revenue**: Revenue, quantity, discount by product, customer, time, channel
- **Operations**: Events, counts, durations by location, resource, time
- **Finance**: Amounts, balances by account, period, entity
- **Marketing**: Clicks, conversions, spend by campaign, segment, date
- **Inventory**: Quantities, movements by product, location, time

## Considerations

- **Grain Consistency**: All rows must be at the same grain; mixing grains corrupts aggregations
- **Key Management**: Use surrogate keys from dimensions; avoid storing volatile natural keys as sole link
- **Large Volume**: Fact tables grow quickly; partition by date and consider partitioning strategy
- **Null Keys**: Define policy for optional dimensions (e.g., unknown or N/A); use consistent surrogate key
- **Sparse Facts**: Many dimension combinations may have no row; that is normal; do not fill with zeros unless required

## Best Practices

- **Document Grain**: Write grain statement and validate with business and ETL
- **Partition by Time**: Partition fact tables by date/month for pruning and maintenance
- **Use Surrogate Keys**: Reference dimension surrogate keys for SCD and stability
- **Index Foreign Keys**: Support join performance; consider columnar storage and clustering
- **Monitor Row Count and Load**: Track growth and load duration; plan for archival or lifecycle

## Related Topics

- [Dimensional Modeling](dimensional-modeling.md)
- [Dimension Tables](dimension-tables.md)
- [Star Schema](star-schema.md)
- [Data Granularity](data-granularity.md)
- [Surrogate Keys](surrogate-keys.md)
- [Slowly Changing Dimensions (SCD)](slowly-changing-dimensions.md)

---

**Category**: Data Modeling  
**Last Updated**: 2024
