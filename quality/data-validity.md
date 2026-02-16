# Data Validity

## Overview
Data validity is the extent to which data conforms to defined syntax, format, and domain rules. Invalid data can cause load failures, incorrect parsing, and bad analytics. Validity is a foundational dimension of data quality and is usually checked at ingestion and transformation.

## Definition
**Data validity** means that values match the expected format, type, and domain rules. Valid data fits the schema (e.g., numeric field contains a number), obeys formats (e.g., date, email, code pattern), and falls within allowed sets or ranges (e.g., enum, min–max). Validity is about “well-formedness” and rule conformance, not necessarily semantic correctness (which is often covered under Data Accuracy).

## Key Concepts

- **Schema and type**: Data types (integer, string, timestamp, etc.) and nullability; invalid type or wrong type causes parse or load errors.
- **Format rules**: Patterns for strings (e.g., phone, email, ID format) and date/time formats; invalid format can break parsing or display.
- **Domain and enum**: Values must come from an allowed list (e.g., status codes, country codes) or fall within a range (e.g., age 0–120).
- **Validation rules**: Explicit business rules (e.g., “discount between 0 and 100,” “end date ≥ start date”) implemented as Data Validation Rules.

## How It Works

Validity is enforced and measured by:

1. **Schema validation**: At ingest or transform, validate types and nullability; reject or quarantine rows that violate the schema.
2. **Format and pattern checks**: Apply regex or format validators (e.g., ISO date, email) to string and datetime fields.
3. **Domain checks**: Compare values to allowed lists (lookup tables, enums) or ranges; flag or reject out-of-domain values.
4. **Rule engines**: Run declarative or code-based Data Validation Rules and collect pass/fail counts and samples of invalid rows.

Results feed Data Quality Metrics and Data Quality Gates; invalid data can be rejected, quarantined, or corrected (e.g., Data Cleansing) before promotion.

## Use Cases

- **Ingestion**: Validate incoming files or streams so that only valid records enter the pipeline; invalid records are logged, quarantined, or rejected.
- **API and integration**: Ensure payloads and responses conform to contracts (e.g., OpenAPI, schema registry); validity checks prevent bad data from propagating.
- **Downstream processing**: Transformations and joins assume valid types and formats; early validity checks reduce failures and rework.
- **Reporting and exports**: Valid formats and codes ensure correct display and compatibility with external systems (e.g., CSV, APIs).

## Considerations

- **Strict vs lenient**: Balance rejecting invalid data (strict) vs accepting and flagging (lenient); choose per use case and fix invalid data at source when possible.
- **Evolution**: As schemas and rules change (Schema Evolution), validity rules and Backward Compatibility need to be updated and communicated.
- **Performance**: Heavy validation can slow ingestion; use sampling, async checks, or tiered rules (critical fields first) where needed.

## Best Practices

- Define validity rules in a central place (e.g., schema registry, data contract) and align with Data Governance and ownership.
- Validate as early as possible (at ingestion or in the first transformation stage); use Data Quality Gates to block invalid data from promotion.
- Log and monitor invalid records (counts, samples, trends) via Data Quality Monitoring; use patterns to fix sources or rules.
- Prefer fixing invalid data at the source or in dedicated cleansing steps; document any automatic corrections (e.g., format normalization).

## Related Topics

- Data Validation Rules (defining and executing validity checks)
- Data Cleansing (correcting invalid or dirty data)
- Schema Evolution (managing schema and validity over time)
- Data Quality Metrics (measuring validity)
- Data Quality Gates (enforcing validity)

## Further Reading

- Schema validation (JSON Schema, Avro, Parquet) and format standards (e.g., ISO dates, RFCs for email)
- Data contract and API validation practices

---

**Category**: Data Quality & Validation  
**Last Updated**: 2025
