# Schema Drift Handling

## Overview
Schema drift is the unplanned or evolving change in structure, types, or semantics of data over time (new columns, removed columns, type changes, or source-specific variations). Handling schema drift is the set of practices and mechanisms used to detect, accommodate, and govern these changes in pipelines without breaking downstream consumers.

## Definition
Schema drift handling encompasses detecting when incoming data no longer matches the expected schema, deciding how to treat new, missing, or changed attributes (add, ignore, fail, or version), and updating pipeline and consumer contracts so that processing remains correct and observable.

## Key Concepts

- **Schema Drift**: Change in columns, types, or constraints in source or derived data
- **Detection**: Comparing actual data (or metadata) to an expected or registered schema
- **Backward/Forward Compatibility**: Old consumers with new data vs. new consumers with old data
- **Schema Registry**: Central store for schema versions and compatibility rules
- **Graceful Degradation**: Pipeline behavior when drift is detected (fail, warn, merge, or ignore)
- **Lineage**: Tracking which schema version was used for each output partition or table

## How It Works

Typical approach:

1. **Capture Expected Schema**: Define or infer schema (from registry, DDL, or sample) and version it
2. **Validate Incoming Data**: Compare read data (or file/stream metadata) to expected schema
3. **Apply Policy**: On drift—fail job, log and continue, add new columns with default/null, or promote to new schema version
4. **Update Contracts**: Bump schema version, update registry, and communicate to consumers
5. **Backfill or Migrate**: If needed, reprocess historical data with new schema or provide compatibility layer
6. **Monitor**: Alert on drift events and track schema version over time

Techniques:
- **Schema-on-read**: Resolve schema at read time (e.g., Parquet/Avro metadata or external registry)
- **Merge schema**: Allow new columns; fill with null for older partitions
- **Strict vs. flexible**: Strict mode fails on unknown/missing columns; flexible adds/ignores

## Use Cases

- **Multi-source Ingestion**: Different sources or versions emit different columns
- **Agile Sources**: Application schemas change frequently; pipelines must adapt
- **Data Lake/Lakehouse**: Files from different times or jobs may have different schemas
- **Streaming**: Late or out-of-order schema changes in event streams
- **Compliance**: Document and audit schema evolution for regulated data

## Considerations

- **Breaking Changes**: Renames, type changes, or removals can break consumers
- **Performance**: Schema validation and merge add overhead
- **Complexity**: Many sources and versions increase testing and ops burden
- **Semantics**: Structural compatibility does not guarantee semantic compatibility (e.g., unit or encoding change)

## Best Practices

- **Version All Schemas**: Use a schema registry or versioned DDL and reference version in pipeline metadata
- **Define Compatibility Rules**: Decide what is allowed (e.g., add optional column only) and enforce in CI or at deploy
- **Test with Drift**: Include “new column” and “missing column” scenarios in tests
- **Document Policy**: Document how pipeline behaves on drift (fail vs. merge vs. ignore) and who is notified
- **Gradual Rollout**: When changing schema, support both old and new formats during transition

## Related Topics

- [Schema Evolution](schema-evolution.md)
- [Data Type Conversion](data-type-conversion.md)
- [Data Format Conversion](data-format-conversion.md)
- [Data Contracts](../advanced/data-contracts.md)
- [Metadata Management](../governance/metadata-management.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
