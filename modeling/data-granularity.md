# Data Granularity

## Overview
Data granularity is the level of detail (or resolution) at which data is stored and represented—e.g., one row per transaction, per day per product, or per month per account. Choosing the right granularity is critical for correctness of aggregations, storage, and the types of questions the data can answer.

## Definition
Granularity defines what one row in a dataset represents. For a fact table, it is the combination of dimensions (and any degenerate dimensions) that uniquely identify each row—e.g., "one row per sales line item" (transaction grain) or "one row per product per store per day" (daily snapshot grain). For event or time-series data, granularity might be per event, per minute, or per hour. Finer granularity means more detail and more rows; coarser granularity means more aggregation and fewer rows.

## Key Concepts

- **Grain Statement**: Explicit definition: "One row per [dimension values] per [optional time/context]"
- **Fact Grain**: In dimensional modeling, the grain of the fact table is the level of detail of the measures (e.g., line-level vs. order-level vs. daily rollup)
- **Finer vs. Coarser**: Finer = more detail, more rows (e.g., event-level). Coarser = more summarized, fewer rows (e.g., monthly).
- **Aggregation Level**: The level at which measures are additive (e.g., sum sales at line level to get order total; sum daily to get monthly)
- **Loss of Detail**: Once data is stored at a coarser grain, finer detail cannot be recovered without going back to source
- **Multiple Grains**: A warehouse may have multiple fact tables or partitions at different grains (e.g., detail facts and summary facts)

## How It Works

Granularity in design and use:

1. **Define Grain Up Front**: For each fact table or analytical dataset, write a grain statement (e.g., "one row per order line per order per day")
2. **Validate with Business**: Confirm that the grain supports required reporting (e.g., can we get daily sales by product? If grain is line-level, yes; if grain is monthly only, no.)
3. **Design Keys**: Dimension keys and degenerate dimensions in the fact table must match the grain (one set of key values per row)
4. **Load at Grain**: ETL must produce exactly one row per grain combination; deduplicate or aggregate source data to match
5. **Query and Aggregate**: Users aggregate measures at or above the defined grain; drilling below grain requires a finer-grained table or source
6. **Document**: Document grain in data dictionary and in pipeline metadata so consumers know what one row means

Examples:
- **Transaction grain**: One row per sale line item — finest level; can aggregate to order, day, product, etc.
- **Daily snapshot**: One row per product per store per day — can aggregate to week, month, product, store
- **Monthly snapshot**: One row per account per month — cannot get daily or transaction detail from this table alone
- **Event grain**: One row per click or per log event — can aggregate by time window, user, page, etc.

## Use Cases

- **Reporting**: Grain determines whether you can report "by day," "by product," "by store," or only at higher levels
- **Storage and Performance**: Coarser grain reduces row count and storage; finer grain supports more flexible analysis but costs more
- **Incremental Processing**: Process and partition by grain (e.g., one partition per day) for efficient refresh
- **Data Marts**: Marts may be at summary grain (e.g., monthly) for performance while detail is in another mart or layer
- **Compliance**: Retention or anonymization may be defined at a certain grain (e.g., drop event-level after 90 days, keep monthly)

## Considerations

- **Cannot Disaggregate**: Data at daily grain cannot be split into hourly; plan grain to support minimum required detail
- **Mixed Grain**: Avoid mixing grains in the same table; each table should have one clear grain
- **Source Alignment**: Grain must be achievable from source (e.g., if source has only daily totals, you cannot build transaction grain without another source)
- **Sparsity**: Some grain combinations may have no data (e.g., no sale for product X in store Y on date Z); that is normal; do not fill with zeros unless required
- **Change Over Time**: Changing grain usually requires new table or migration and backfill

## Best Practices

- **Write Grain Statement**: Document "One row per X, Y, Z" for every fact table and key dataset
- **Validate Queries**: Check that required reports are possible at chosen grain
- **Single Grain per Table**: Do not mix grains in one table; use separate tables or partitions for different grains
- **Partition by Grain**: When grain includes time, partition by date/period for pruning and lifecycle
- **Communicate to Consumers**: Make grain visible in catalog and documentation so users know what they are querying

## Related Topics

- Fact Tables
- Data Aggregation
- Data Aggregation Levels
- Dimensional Modeling
- Star Schema
- Composite Keys

---

**Category**: Data Modeling  
**Last Updated**: 2024
