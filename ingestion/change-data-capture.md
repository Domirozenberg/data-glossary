# Change Data Capture (CDC)

## Overview
Change Data Capture is a technique for identifying and capturing changes made to data in source systems, then delivering those changes in real-time or near-real-time to downstream systems. CDC enables efficient incremental data synchronization without full table scans.

## Definition
Change Data Capture is a process that monitors and captures insert, update, and delete operations on source data, extracting only the changed records along with metadata about the change type and timing. This allows downstream systems to stay synchronized with source systems efficiently.

## Key Concepts

- **Change Detection**: Methods to identify what data has changed
- **Change Logs**: Transaction logs or change tables that record modifications
- **Incremental Processing**: Processing only changed data rather than full datasets
- **Change Types**: Insert, Update, Delete operations
- **Change Metadata**: Timestamps, sequence numbers, or transaction IDs
- **Low Latency**: Near real-time propagation of changes

## How It Works

CDC operates by monitoring source system change logs or transaction logs:

1. **Log-based CDC**: Reads database transaction logs (redo logs, WAL) to detect changes
2. **Trigger-based CDC**: Uses database triggers to capture changes into change tables
3. **Timestamp-based CDC**: Compares record timestamps to identify modifications
4. **Diff-based CDC**: Compares current state with previous snapshots

The captured changes are then streamed or batched to downstream systems, which apply the changes to maintain synchronization. CDC typically includes metadata such as:
- Operation type (INSERT, UPDATE, DELETE)
- Change timestamp
- Before/after values (for updates)
- Transaction sequence information

## Use Cases

- **Real-time Data Replication**: Keeping databases synchronized across systems
- **Event Sourcing**: Capturing all changes as a sequence of events
- **Data Warehouse Updates**: Incrementally updating analytical systems
- **Microservices Synchronization**: Keeping distributed data stores in sync
- **Audit Trails**: Maintaining complete change history
- **Multi-region Replication**: Synchronizing data across geographic locations

## Considerations

- **Source System Impact**: Log-based CDC has minimal impact; trigger-based may affect performance
- **Latency Requirements**: Real-time vs batch CDC trade-offs
- **Change Volume**: High-change tables may generate significant CDC traffic
- **Schema Changes**: Handling source schema evolution
- **Data Consistency**: Ensuring transactional consistency across systems
- **Initial Load**: First-time synchronization may require full load before CDC
- **Conflict Resolution**: Handling conflicts in distributed scenarios

## Best Practices

- Use log-based CDC when available for minimal source system impact
- Implement change filtering to reduce unnecessary data movement
- Handle schema changes gracefully with versioning
- Monitor CDC lag to ensure timely synchronization
- Plan for initial full load before enabling incremental CDC
- Implement idempotent change application for reliability
- Consider change ordering and transaction boundaries
- Archive or purge old change logs to manage storage

## Related Topics

- Data Replication
- Stream Processing
- Incremental Load
- Event-driven Processing
- Data Synchronization

---

**Category**: Ingestion  
**Last Updated**: 2024
