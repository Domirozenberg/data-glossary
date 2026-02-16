# Data Joining

## Overview
Data joining is the process of combining rows from two or more datasets based on a common key or condition. It is a core transformation in ETL/ELT pipelines, enabling unified views from multiple sources and supporting analytics and reporting.

## Definition
A join associates rows from a left and right (or multiple) dataset where a join condition is satisfied. Common types include inner join (only matching rows), left/right outer join (all from one side plus matches), full outer join (all from both sides), and cross join (Cartesian product). The result is a single dataset with columns from all inputs.

## Key Concepts

- **Join Key**: Column(s) used to match rows (e.g., customer_id, order_id)
- **Join Type**: Inner, left, right, full outer, cross, semi, anti
- **Cardinality**: One-to-one, one-to-many, many-to-many—affects row count and duplicates
- **Null Handling**: How nulls in keys are treated (e.g., not equal to each other)
- **Skew**: Uneven key distribution can cause performance issues in distributed systems
- **Deduplication**: Pre-deduping inputs to avoid unintended row multiplication

## How It Works

Join execution (conceptually):

1. **Choose Join Type**: Select inner, left, right, or full outer based on business need
2. **Define Keys**: Specify join columns (or expressions) for each side
3. **Execute**: Engine matches rows; for each left row, find matching right row(s) and emit combined row(s)
4. **Handle Multiplicity**: One-to-many or many-to-many can multiply rows; filter or aggregate if needed
5. **Project Columns**: Select and optionally rename output columns

In distributed systems:
- **Broadcast Join**: Small table sent to all workers; good when one side is small
- **Sort-Merge / Hash Join**: Both sides partitioned by key; scalable for large tables
- **Skew Handling**: Salting or splitting hot keys to balance work

## Use Cases

- **Data Integration**: Combining transactional and master data
- **Enrichment**: Attaching reference or dimension data to fact data
- **Deduplication**: Matching and merging duplicate records across sources
- **Change Data Capture**: Joining CDC stream with dimension table for current state
- **Reporting**: Building star-schema-style datasets from normalized sources

## Considerations

- **Correctness**: Wrong key or type can cause silent duplicates or drops (e.g., nulls)
- **Performance**: Large joins dominate runtime; partition pruning and key design matter
- **Data Quality**: Dirty or inconsistent keys cause wrong or missing matches
- **Schema**: Column name clashes require aliasing or selection

## Best Practices

- **Validate Keys**: Ensure join keys are deduped and typed consistently
- **Document Cardinality**: State expected one-to-one vs. one-to-many
- **Test with Edge Cases**: Empty inputs, null keys, all unmatched
- **Monitor Row Counts**: Compare pre- and post-join counts to catch anomalies
- **Prefer Small Dimension Broadcasts**: When one side is small, use broadcast for simplicity

## Related Topics

- [Data Enrichment](data-enrichment.md)
- [ETL/ELT](../patterns/etl-vs-elt.md)
- [Data Cleansing](data-cleansing.md)
- [Dimensional Modeling](../modeling/dimensional-modeling.md)
- [Data Deduplication](data-deduplication.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
