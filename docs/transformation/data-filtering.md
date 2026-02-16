# Data Filtering

## Overview
Data filtering is the process of retaining only rows (or columns) that meet specified conditions and excluding the rest. It is used to focus on relevant subsets, meet compliance or retention rules, and reduce data volume for downstream processing and storage.

## Definition
Filtering applies predicates (conditions) to a dataset and keeps only rows where the predicate evaluates to true. Common operations include equality, range, membership (IN), pattern match (LIKE, regex), and null checks. Column filtering (projection) selects a subset of columns; row filtering selects a subset of rows.

## Key Concepts

- **Predicate**: Boolean expression (e.g., status = 'active', date >= '2024-01-01')
- **Pushdown**: Applying filters as early as possible (in storage or engine) to reduce I/O
- **Partition Pruning**: Skipping partitions that cannot contain matching rows
- **Selectivity**: Proportion of rows that pass; affects performance and cost
- **Determinism**: Same input and predicate should yield same result for reproducibility
- **Null Handling**: Define whether null compares as true, false, or unknown (SQL: typically unknown/false)

## How It Works

Filtering in pipelines:

1. **Define Criteria**: Specify conditions (e.g., date range, status, exclusion list)
2. **Apply Filter**: Execute WHERE-like logic in SQL, DataFrame API, or config
3. **Optimize**: Use partition pruning and predicate pushdown when available
4. **Validate**: Spot-check row counts and sample rows to ensure logic is correct
5. **Document**: Record filter logic and any business rules (e.g., exclusions for compliance)

Best practices:
- **Push Down**: Filter in the source query or reader when possible
- **Partition Alignment**: Filter on partition columns to skip entire files/partitions
- **Parameterize**: Use parameters for date ranges and lists to avoid hardcoding

## Use Cases

- **Compliance and Retention**: Retain only data within retention window or allowed regions
- **Focus Subsets**: Limit to active customers, certain products, or test data exclusion
- **PII Reduction**: Drop or restrict columns/rows containing sensitive data before sharing
- **Cost and Performance**: Reduce volume before expensive joins or transfers
- **Environment Separation**: Filter by environment or tenant for dev/test/prod

## Considerations

- **Information Loss**: Filtered-out data is unavailable unless re-read from source
- **Logic Errors**: Incorrect predicates can drop valid or keep invalid data
- **Performance**: Complex predicates or non-partition columns can limit pushdown
- **Auditability**: Document why rows were excluded for compliance and debugging

## Best Practices

- **Document Rules**: Maintain a clear record of filter logic and business justification
- **Reuse Definitions**: Centralize filter logic (e.g., shared views or config) for consistency
- **Test Edge Cases**: Empty result, all pass, boundary values, nulls
- **Monitor Volume**: Alert on large changes in filtered row counts
- **Prefer Pushdown**: Design pipelines so engines can push filters to storage

## Related Topics

- [Data Cleansing](data-cleansing.md)
- [Data Retention Policies](../storage/data-retention-policies.md)
- [Data Masking](../governance/data-masking.md)
- [Data Partitioning](../storage/data-partitioning.md)
- [ETL/ELT](../patterns/etl-vs-elt.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
