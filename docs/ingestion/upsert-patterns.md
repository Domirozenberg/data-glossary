# Upsert Patterns

## Overview
Upsert (Update or Insert) is a data loading pattern that inserts new records or updates existing records based on a key. It is essential for incremental loads where you need to handle both new and updated data efficiently without creating duplicates.

## Definition
Upsert is a database operation that updates an existing record if it exists (based on a key) or inserts a new record if it doesn't exist. It combines the logic of both UPDATE and INSERT operations into a single atomic operation, ensuring data consistency.

## Key Concepts

- **Key-based Matching**: Uses a key to identify existing records
- **Update Existing**: Updates records that already exist
- **Insert New**: Inserts records that don't exist
- **Atomic Operation**: Single operation ensures consistency
- **Idempotency**: Can be safely retried
- **Conflict Resolution**: Handles conflicts when records exist
- **Performance**: More efficient than separate insert/update logic

## How It Works

Upsert operations:

1. **Key Identification**: Identify key fields for matching
2. **Existence Check**: Check if record exists (implicit or explicit)
3. **Update Path**: If exists, update existing record
4. **Insert Path**: If not exists, insert new record
5. **Atomic Execution**: Execute as single atomic operation
6. **Conflict Handling**: Handle any conflicts that arise

Implementation approaches:
- **MERGE Statement**: SQL MERGE statement
- **ON CONFLICT**: PostgreSQL ON CONFLICT clause
- **REPLACE INTO**: MySQL REPLACE INTO
- **Application Logic**: Application-level upsert logic

## Use Cases

- **Incremental Loads**: Loading incremental data updates
- **Change Data Capture**: Applying CDC changes
- **Data Synchronization**: Keeping systems synchronized
- **Idempotent Operations**: Ensuring operations can be retried
- **Master Data Management**: Maintaining master data
- **Real-time Updates**: Applying real-time data updates

## Considerations

- **Key Selection**: Choosing appropriate keys for matching
- **Performance**: Upsert performance on large datasets
- **Conflict Resolution**: Handling conflicts in concurrent scenarios
- **Partial Updates**: Deciding what to update vs insert
- **Null Handling**: Handling null values in keys
- **Index Impact**: Impact on indexes during upserts

## Best Practices

- **Choose Appropriate Keys**: Use unique, stable keys
- **Optimize Performance**: Index key columns
- **Handle Conflicts**: Plan for conflict resolution
- **Batch Upserts**: Batch upserts for better performance
- **Monitor Performance**: Track upsert performance
- **Test Thoroughly**: Test upsert logic with various scenarios
- **Document Logic**: Document upsert rules and keys

## Related Topics

- [Incremental Load](full-load-vs-incremental-load.md)
- [Change Data Capture (CDC)](change-data-capture.md)
- [Data Synchronization](../patterns/data-synchronization.md)
- [Idempotent Ingestion](idempotent-ingestion.md)
- Database Operations

---

**Category**: Data Ingestion  
**Last Updated**: 2024
