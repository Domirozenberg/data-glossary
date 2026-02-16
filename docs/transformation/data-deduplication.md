# Data Deduplication

## Overview
Data deduplication is the process of identifying and removing (or merging) duplicate records so that each logical entity or event is represented once in the dataset. It is essential for correct analytics, consistent joins, and compliance with exactly-once or idempotent semantics.

## Definition
Deduplication determines which rows are duplicates—typically by a key or set of columns—and keeps one representative row (or merges attributes) according to a strategy (e.g., first, last, or aggregate). It can be applied in batch (full or incremental) or in streaming (within a window or per key).

## Key Concepts

- **Deduplication Key**: Column(s) that define uniqueness (e.g., order_id, event_id, or composite)
- **Strategy**: How to choose the row to keep—first, last, max timestamp, or merge (e.g., take non-null values)
- **Scope**: Full dataset vs. incremental (only new data) vs. windowed (streaming)
- **Idempotency**: Re-running ingestion or transformation yields same result; dedup is central to this
- **Ordering**: When using “last” or “first,” define sort order (e.g., event_time, processed_at)
- **Fuzzy Duplicates**: Near-duplicates (e.g., slight text differences) may require matching logic beyond key equality

## How It Works

Deduplication typically:

1. **Define Key**: Choose business or technical key(s) that uniquely identify a record
2. **Define Order (if applicable)**: Choose column(s) to order by when selecting first/last
3. **Scope Data**: Full table, incremental partition, or streaming window
4. **Partition by Key**: Group rows by key (in SQL: GROUP BY key; in Spark: dropDuplicates or window)
5. **Select Representative**: Apply strategy (e.g., MAX(timestamp) for “latest,” or FIRST() for “first seen”)
6. **Write Result**: Replace or upsert into target; ensure downstream sees at most one row per key
7. **Validate**: Check duplicate count before/after and monitor key distribution

Streaming: use event-time (or processing-time) windows and deduplicate per key within window; handle late data per watermark policy.

## Use Cases

- **Idempotent Ingestion**: Replaying the same file or stream should not double-count records
- **CDC and Replication**: Remove duplicate apply events or multiple updates per key
- **Event Pipelines**: One row per event_id (or per entity+time bucket) for analytics
- **Master Data**: Single canonical record per entity (e.g., customer, product) from multiple sources
- **Reporting**: Correct KPIs (e.g., order count, DAU) by removing duplicate transactions or events

## Considerations

- **Key Design**: Weak or non-unique keys lead to over-dedup (losing valid rows) or under-dedup (keeping duplicates)
- **Ordering**: “Last” requires stable ordering (e.g., timestamp); out-of-order data complicates streaming
- **Performance**: Dedup over large datasets or high-cardinality keys is expensive; partition and tune
- **Auditability**: Sometimes need to retain “duplicate” rows for audit; consider separate duplicate log or archive

## Best Practices

- **Use Business or Stable Keys**: Prefer immutable business keys (order_id) or stable surrogates
- **Document Strategy**: Clearly state “keep latest by event_time” or “keep first by received_at”
- **Test with Duplicates**: Include duplicate key scenarios in tests; verify row count and which row is kept
- **Monitor Duplicate Rates**: Alert on sudden increase in duplicates (may indicate upstream issue)
- **Align with Exactly-Once**: Design dedup with exactly-once semantics in mind for streaming and replay

## Related Topics

- [Data Cleansing](data-cleansing.md)
- [Idempotent Ingestion](../ingestion/idempotent-ingestion.md)
- [Exactly-once Semantics](../ingestion/exactly-once-semantics.md)
- [Change Data Capture (CDC)](../ingestion/change-data-capture.md)
- [Data Joining](data-joining.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
