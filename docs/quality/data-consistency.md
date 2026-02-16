# Data Consistency

## Overview
Data consistency means that data is coherent and agrees across systems, tables, time periods, and fields according to defined rules. Inconsistent data leads to conflicting reports, failed joins, and loss of trust. Consistency is a core dimension of data quality and is especially important in integrated and replicated environments.

## Definition
**Data consistency** is the degree to which data conforms to logical and business rules across the dataset and across systems. It includes: same entities having the same attributes in different places (e.g., no conflicting duplicates), relationships holding (e.g., foreign keys, sums matching), and values aligning with expected rules (e.g., status transitions, date order).

## Key Concepts

- **Cross-system consistency**: The same business entity (e.g., customer, order) has aligned attributes in different systems or tables; discrepancies indicate sync or transformation issues.
- **Referential integrity**: Foreign keys reference existing rows; no orphaned child rows or broken links.
- **Semantic consistency**: Values and codes mean the same thing everywhere (e.g., one code set for “country,” consistent units and currencies).
- **Temporal consistency**: Snapshots and history are coherent (e.g., no end date before start date, no future-dated records unless intended).

## How It Works

Consistency is checked by:

1. **Reconciliation**: Compare key fields and aggregates between source and target (e.g., after replication or ETL) or between redundant tables.
2. **Referential-integrity checks**: Validate that every foreign key points to an existing primary key and that required relationships are present.
3. **Business-rule validation**: Enforce rules such as “status can only move forward,” “total = sum of parts,” or “codes from allowed list.”
4. **Cross-table and cross-partition checks**: Ensure that derived or aggregated data matches underlying detail and that partitions (e.g., by date) do not overlap or conflict.

Results feed into Data Quality Monitoring and Data Quality Gates; failures can block promotion or trigger alerts and remediation.

## Use Cases

- **Data replication and sync**: After CDC, ETL, or Data Synchronization, consistency checks confirm that the replica or warehouse matches the source (or defined rules).
- **Master data and golden records**: When merging or curating master data, consistency ensures one version of the truth across systems.
- **Reporting and analytics**: Inconsistent definitions or duplicate/conflicting records cause wrong totals and broken dashboards; consistency checks protect downstream consumers.
- **Regulatory and audit**: Many controls require evidence that data is consistent across systems and over time.

## Considerations

- **Eventual consistency**: In distributed or async systems, consistency may be eventual; define when and how consistency is evaluated (e.g., after a sync window).
- **Rule complexity**: Some rules are expensive (e.g., full cross-table checks); prioritize and run heavy checks on schedule or samples.
- **Conflicting sources**: When two systems disagree, define which is authoritative and how conflicts are resolved (e.g., Data Stewardship, Data Ownership).

## Best Practices

- Define consistency rules and owners; document in a data dictionary or contract and align with Data Governance.
- Automate checks in pipelines (e.g., post-load reconciliation, referential-integrity tests) and in Data Quality Gates.
- Use idempotent and well-ordered pipelines (e.g., Idempotent Ingestion) to reduce inconsistent intermediate states.
- Monitor consistency over time; investigate and fix root causes (source, transformation, or sync logic) rather than only correcting data.

## Related Topics

- [Data Replication](../patterns/data-replication.md) (keeping copies consistent)
- [Data Synchronization](../patterns/data-synchronization.md) (aligning data across systems)
- [Data Integrity](data-integrity.md)(logical and physical correctness)
- [Data Quality Metrics](data-quality-metrics.md)(measuring consistency)
- [Data Quality Gates](data-quality-gates.md)(enforcing consistency)

## Further Reading

- ACID and eventual consistency in databases and distributed systems
- Data quality frameworks (e.g., DAMA-DMBOK) and consistency as a dimension

---

**Category**: Data Quality & Validation  
**Last Updated**: 2025
