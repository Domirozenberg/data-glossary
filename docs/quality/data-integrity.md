# Data Integrity

## Overview
Data integrity is the preservation of correctness and consistency of data over its lifecycle. It covers both physical integrity (storage and transmission without corruption) and logical integrity (rules, relationships, and constraints). Integrity is foundational to trust in data and is supported by database constraints, pipeline design, and governance.

## Definition
**Data integrity** is the assurance that data remains accurate, consistent, and reliable from creation through storage, processing, and use. It includes: no unintended modification or corruption (physical), and conformance to business and referential rules (logical). When integrity is maintained, data can be trusted for reporting, analytics, and operations.

## Key Concepts

- **Physical integrity**: Data is not corrupted in storage or in transit; achieved via checksums, replication, backup, and safe storage (e.g., Database Backup and Recovery, Storage Encryption).
- **Logical integrity**: Data obeys constraints and rules: entity integrity (primary keys unique and non-null), referential integrity (foreign keys reference existing rows), and domain/constraint rules (values in range, formats valid).
- **Transactional integrity**: ACID properties (e.g., in relational systems) ensure that multi-step updates either fully commit or fully roll back, avoiding partial or inconsistent state.
- **Integrity constraints**: Database or application-level rules (unique, not null, check, foreign key) that prevent invalid or inconsistent data from being stored.

## How It Works

Integrity is maintained and verified by:

1. **Database constraints**: Define primary keys, unique constraints, foreign keys, and check constraints so the database rejects or prevents invalid writes.
2. **Pipeline validation**: In ETL or ingestion, validate referential integrity (e.g., parent row exists), key uniqueness, and business rules before or after load; use Data Quality Gates to block bad data.
3. **Checksums and reconciliation**: Use hashes or checksums to detect corruption in files or rows; reconcile source and target after replication or ETL (see Data Consistency).
4. **Backup and recovery**: Regular backups and tested recovery (Database Backup and Recovery, Disaster Recovery) protect against loss and support point-in-time restoration.

Monitoring (Data Quality Monitoring, Data Observability) and audits (Audit Logging) help detect integrity violations and track who changed what.

## Use Cases

- **Transactional systems**: Banks, orders, and inventory rely on ACID and referential integrity to prevent double-spend, orphan records, and inconsistent state.
- **Data warehouses and lakes**: Integrity checks after load (e.g., row counts, key uniqueness, referential checks) ensure that replicated or transformed data is correct and consistent.
- **Compliance and audit**: Regulations often require evidence that data has not been altered inappropriately; integrity controls and Audit Logging support compliance.
- **Data sharing and APIs**: Contracts and schemas (e.g., Schema Registry) help consumers trust that data conforms to expected structure and relationships.

## Considerations

- **Performance**: Heavy constraints and checks can slow writes and pipelines; balance strictness with throughput and use batch or async checks where appropriate.
- **Distributed and eventual consistency**: In distributed systems, strict integrity may be relaxed to eventual consistency; define what guarantees are required and where.
- **Human and process errors**: Integrity controls reduce technical errors; access control (Access Control), stewardship (Data Stewardship), and change management reduce human errors.

## Best Practices

- Enforce integrity as close to the source as possible (database constraints, validated ingestion); add pipeline-level checks for replicated and transformed data.
- Document constraints and rules in a data dictionary or contract; align with Data Governance and Data Ownership.
- Use transactions and idempotent design (Idempotent Ingestion) so that retries and backfills do not leave data in a half-updated or duplicate state.
- Monitor integrity metrics (e.g., constraint violations, reconciliation failures) and protect data at rest and in transit (Data Encryption, Backup and Recovery).

## Related Topics

- [ACID Properties](../databases/acid-properties.md) (transactional integrity in databases)
- [Data Consistency](data-consistency.md) (logical agreement across data)
- [Data Quality Gates](data-quality-gates.md) (enforcing integrity before promotion)
- [Database Backup and Recovery](../databases/database-backup-recovery.md) (physical protection)
- Referential integrity and Foreign Keys and Relationships

## Further Reading

- Database integrity constraints and normal forms
- DAMA-DMBOK and similar frameworks on data integrity and quality

---

**Category**: Data Quality & Validation  
**Last Updated**: 2025
