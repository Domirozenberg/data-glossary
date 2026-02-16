# At-least-once Semantics

## Overview
At-least-once semantics is a delivery guarantee that ensures each record is processed at least once, but may be processed multiple times in case of failures or retries. It is simpler to implement than exactly-once and is often sufficient when downstream systems can handle duplicates.

## Definition
At-least-once semantics guarantees that each data record will be processed at least once, but may be processed multiple times. It prioritizes not losing data over avoiding duplicates, making it suitable when duplicates can be handled downstream.

## Key Concepts

- **No Loss**: Guarantees no records are lost
- **Possible Duplicates**: Records may be processed multiple times
- **Retry Logic**: Retries on failure may cause duplicates
- **Simpler Implementation**: Simpler than exactly-once
- **Downstream Handling**: Requires downstream to handle duplicates
- **Idempotency**: Downstream should be idempotent
- **Performance**: Generally better performance than exactly-once

## How It Works

At-least-once semantics:

1. **Record Delivery**: Records delivered to processing system
2. **Processing**: Records processed
3. **Acknowledgment**: Acknowledgment sent after processing
4. **Failure Handling**: On failure, records may be redelivered
5. **Retry**: Retry logic may reprocess records
6. **Duplicates**: Duplicates may occur from retries
7. **Downstream Deduplication**: Downstream handles duplicates

Characteristics:
- **Guaranteed Delivery**: Ensures delivery even with failures
- **Retry on Failure**: Automatically retries on failures
- **No Duplicate Prevention**: Doesn't prevent duplicates
- **Simpler**: Simpler than exactly-once implementation

## Use Cases

- **High Throughput**: When throughput is priority
- **Tolerant Systems**: When duplicates are acceptable
- **Idempotent Downstream**: When downstream can handle duplicates
- **Simpler Implementation**: When simplicity is priority
- **Non-critical Data**: When exact-once not required
- **Analytics**: Many analytics can handle duplicates
- **Logging**: Log aggregation systems

## Considerations

- **Duplicate Handling**: Must handle duplicates downstream
- **Idempotency**: Downstream operations should be idempotent
- **Data Quality**: May require deduplication logic
- **Accuracy**: May impact accuracy of counts/aggregations
- **Storage**: Duplicates increase storage requirements

## Best Practices

- **Make Downstream Idempotent**: Ensure downstream handles duplicates
- **Implement Deduplication**: Add deduplication where needed
- **Monitor Duplicates**: Track duplicate rates
- **Document Behavior**: Document at-least-once guarantees
- **Test Scenarios**: Test failure and retry scenarios
- **Optimize Performance**: Leverage performance benefits

## Related Topics

- [Exactly-once Semantics](exactly-once-semantics.md)
- [Idempotent Ingestion](idempotent-ingestion.md)
- [Retry Strategies](../orchestration/retry-strategies.md)
- [Error Handling](../orchestration/error-handling.md)
- Deduplication
- [Fault Tolerance](../advanced/fault-tolerance.md)

---

**Category**: Data Ingestion  
**Last Updated**: 2024
