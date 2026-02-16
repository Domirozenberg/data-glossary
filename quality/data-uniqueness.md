# Data Uniqueness

## Overview
Data uniqueness is the degree to which entities or records are represented once, without unintended duplication. Duplicate records distort counts, aggregates, and joins and can cause double-counting in reporting and analytics. Enforcing and measuring uniqueness is a core part of data quality and master data management.

## Definition
**Data uniqueness** means that each distinct real-world entity or logical record appears exactly once in a dataset (or within a defined scope), according to a chosen key or identity. Uniqueness is violated when the same entity appears multiple times (duplicates) or when the chosen key is not unique (key collision).

## Key Concepts

- **Business key and surrogate key**: Uniqueness is defined per *business key* (e.g., customer ID, order ID) or *surrogate key*; the same entity should have one row per key in the target grain.
- **Scope**: Uniqueness can be required per table, per partition (e.g., per day), or per system; scope affects how duplicates are defined and detected.
- **Deduplication**: The process of identifying and removing (or merging) duplicate records; see Data Deduplication.
- **Idempotency**: Pipelines that are idempotent (e.g., Idempotent Ingestion) avoid creating duplicates on retries or reruns.

## How It Works

Uniqueness is enforced and verified by:

1. **Key constraints**: Declare primary key or unique constraints in the database so the engine rejects duplicate keys at load time.
2. **Deduplication logic**: In the pipeline, identify duplicates (e.g., by business key), then keep one row (e.g., latest, best quality) and drop or merge others (Data Deduplication).
3. **Uniqueness checks**: After load or as a Data Quality Gate, count distinct keys and total rows; uniqueness holds when distinct key count equals row count (for the scope).
4. **Profiling and monitoring**: Data Profiling and Data Quality Monitoring report duplicate counts and sample duplicate keys; trends indicate ingestion or key definition issues.

Results feed Data Quality Metrics and Data Quality Gates; duplicates can block promotion or trigger alerts and deduplication jobs.

## Use Cases

- **Master data**: Customer, product, or other master entities should appear once per key in the golden record or data mart; uniqueness is enforced to avoid multiple records for the same entity.
- **Transactional and event data**: Depending on grain, events or transactions may be unique by (e.g., event_id, order_id); duplicates indicate replay, double-send, or bad keys.
- **Reporting and analytics**: Aggregations and joins assume one row per entity (or per grain); duplicates cause over-counting and wrong metrics.
- **Compliance and audit**: Some regulations require that individuals or transactions are not double-counted; uniqueness checks provide evidence.

## Considerations

- **Definition of “same”**: Uniqueness depends on the chosen key; different keys (e.g., email vs customer_id) can give different duplicate sets. Align with business on the canonical key.
- **Merge strategy**: When deduplicating, define which row to keep (latest, most complete, source priority) and whether to merge attributes; document in Data Governance.
- **Performance**: Uniqueness checks on large tables can be expensive; use indexes, sampling, or incremental checks where appropriate.

## Best Practices

- Define the business key and uniqueness scope per dataset; document in a data dictionary and align with Data Ownership.
- Enforce uniqueness in the pipeline (constraints, deduplication) and validate with Data Quality Gates before promoting data.
- Use Idempotent Ingestion and deterministic keys so that retries and backfills do not create duplicates.
- Monitor duplicate rates over time (Data Quality Monitoring); investigate and fix root causes (source, key definition, or pipeline logic).

## Related Topics

- Data Deduplication (identifying and removing duplicates)
- Idempotent Ingestion (avoiding duplicates on retry)
- Data Quality Metrics (measuring uniqueness)
- Data Quality Gates (enforcing uniqueness)
- Data Profiling (discovering duplicate keys)

## Further Reading

- Master data management (MDM) and golden record concepts
- Deterministic and idempotent pipeline design

---

**Category**: Data Quality & Validation  
**Last Updated**: 2025
