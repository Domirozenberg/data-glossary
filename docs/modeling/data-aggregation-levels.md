# Data Aggregation Levels

## Overview
Data aggregation levels are the different levels of summarization at which data can be viewed or stored—e.g., transaction, daily, weekly, monthly, or by geography (store, region, country). They define the "roll-up" and "drill-down" paths for reporting and analytics and determine what questions can be answered without accessing finer-grained data.

## Definition
An aggregation level is a specific combination of dimensions and time/context at which measures are summed, counted, or otherwise aggregated. For example, "sales by product by month" is one level; "sales by product by store by day" is a finer level. Levels form a hierarchy (e.g., day → week → month → quarter → year) or a set of dimensions (e.g., product, category, department). Data may be stored at one or more levels (detail vs. pre-aggregated) for query performance and clarity.

## Key Concepts

- **Roll-Up**: Aggregating from finer to coarser level (e.g., daily → monthly, product → category)
- **Drill-Down**: Disaggregating or querying at finer level (e.g., monthly → daily, region → store)
- **Level Hierarchy**: Ordered set of levels (e.g., day, week, month, quarter, year) or (store, district, region, country)
- **Pre-Aggregation**: Storing data at multiple levels (e.g., detail fact + summary tables or materialized views) for faster queries
- **Additivity**: Measures that can be summed across a level (e.g., revenue) vs. semi-additive (e.g., balance) or non-additive (e.g., ratio)
- **Consistency**: Same measure aggregated at different levels should be consistent (e.g., sum of daily = monthly total)
- **Dimension Hierarchy**: Levels often align to dimension hierarchies (e.g., date → month → year, product → category → department)

## How It Works

Aggregation levels in practice:

1. **Define Hierarchies**: Identify time hierarchy (day → month → quarter → year) and dimension hierarchies (e.g., product → category → department, store → region → country)
2. **Define Stored Levels**: Decide what is stored—detail only, or detail + selected aggregation levels (e.g., daily + monthly summary)
3. **Build Aggregates**: Create summary tables, materialized views, or cubes at chosen levels; refresh with detail data
4. **Expose to Users**: Present levels in semantic layer, BI folder, or catalog so users choose "Sales by Month" vs. "Sales by Day"
5. **Roll-Up and Drill-Down**: BI tools or SQL group by and filter at different levels; ensure dimension attributes support hierarchy (e.g., month, year on date dimension)
6. **Validate**: Reconcile aggregated levels to detail (sum of daily = monthly, etc.) and monitor for drift

Characteristics:
- **Detail as Source of Truth**: Finest grain is authoritative; coarser levels are derived and should match when aggregated
- **Performance vs. Flexibility**: Pre-aggregated levels speed up common reports; detail supports ad-hoc drill-down
- **Semantic Layer**: Many BI tools define levels and hierarchies in a semantic layer and generate SQL accordingly

## Use Cases

- **Reporting**: Standard reports at month, quarter, or year; ad-hoc at day or transaction where needed
- **Dashboards**: KPIs at summary level (e.g., company monthly); drill to region, product, or week
- **OLAP**: Cubes and multidimensional analysis with explicit levels and hierarchies
- **Performance**: Pre-aggregate at month or quarter to avoid scanning detail for routine reporting
- **Governance**: Define "official" levels for published metrics (e.g., revenue at month level for external reporting)
- **Data Marts**: Mart may be built at one primary level (e.g., monthly) with optional detail view

## Considerations

- **Storage**: Storing multiple levels increases storage and ETL; balance with query patterns
- **Freshness**: Summary levels must be refreshed when detail changes; incremental aggregation reduces cost
- **Semi-Additive Measures**: Balance and inventory cannot be summed across time; define correct aggregation (e.g., last value, average) per level
- **Non-Additive**: Ratios and averages must be computed from components at each level, not summed
- **Hierarchy Consistency**: Dimension must have consistent hierarchy (e.g., every product in one category) for clean roll-up
- **Multiple Hierarchies**: Same dimension may have multiple hierarchies (e.g., date: calendar vs. fiscal); document and support both if needed

## Best Practices

- **Document Levels and Hierarchies**: Maintain data dictionary with levels, hierarchies, and which tables/views support each level
- **Single Definition of Roll-Up**: Define aggregation logic once (e.g., in view or semantic model) to avoid inconsistent numbers
- **Reconcile to Detail**: Periodically validate that aggregated levels match sum/count of detail
- **Choose Pre-Aggregation Wisely**: Pre-aggregate only levels that are queried often and expensive at detail
- **Expose in Semantic Layer**: Let BI and analysts select level in tool rather than writing custom SQL per level

## Related Topics

- [Data Granularity](data-granularity.md)
- [Data Aggregation](../transformation/data-aggregation.md)
- [Dimensional Modeling](dimensional-modeling.md)
- [Fact Tables](fact-tables.md)
- [OLAP](../analytics/oltp-vs-olap.md)
- [Roll-up and Drill-down](../analytics/roll-up-and-drill-down.md)

---

**Category**: Data Modeling  
**Last Updated**: 2024
