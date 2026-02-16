# Data Accuracy

## Overview
Data accuracy is the extent to which data correctly represents the real-world entities or events it is intended to model. Inaccurate data undermines trust in reports, models, and decisions. Measuring and improving accuracy is a central concern in data quality and governance.

## Definition
**Data accuracy** is the degree to which data values match the true state of the world (or an authoritative source). Unlike completeness (presence of data) or format validity (syntax), accuracy is about *correctness*: whether a stored value is right for the thing it describes.

## Key Concepts

- **Authoritative source**: A system or dataset accepted as the “truth” (e.g., system of record); accuracy is often checked by comparing to this source.
- **Correctness rules**: Business rules that define valid value ranges, relationships, or formats (e.g., age between 0 and 120, revenue ≥ 0).
- **Cross-field consistency**: Values across columns or tables must agree (e.g., end date after start date, sum of line items equals total).
- **Temporal accuracy**: Data reflects the state at the intended point in time and is not stale or overwritten incorrectly.

## How It Works

Accuracy is evaluated by:

1. **Comparison to source of truth**: Reconcile pipeline or warehouse data against the authoritative system (e.g., row counts, key fields, checksums).
2. **Business-rule checks**: Apply validation rules (format, range, referential integrity) and flag or reject violations.
3. **Statistical and anomaly checks**: Use distributions, outlier detection, or ML-based checks to find values that are implausible or inconsistent with history.
4. **Sampling and audits**: Periodically compare samples to reality (e.g., manual verification, external data) to estimate error rates.

Results are expressed as pass/fail rates, error counts, or accuracy scores; monitoring and gates can block promotion or alert when accuracy drops.

## Use Cases

- **Financial and regulatory reporting**: Incorrect figures can cause compliance failures or wrong business decisions; accuracy checks are mandatory in many domains.
- **Customer and product data**: Wrong addresses, prices, or attributes affect operations and analytics; accuracy is often validated against master data.
- **ML and analytics**: Inaccurate labels or features degrade model performance; data quality for ML often includes accuracy and consistency checks.
- **Data migration and integration**: After ETL or replication, accuracy checks confirm that data was transformed and loaded correctly.

## Considerations

- **Source of truth may be imperfect**: The “authoritative” system can have errors; treat accuracy as relative to that source unless you have a higher standard (e.g., manual audit).
- **Cost of checks**: Full reconciliation can be expensive; balance coverage (all rows vs samples) and frequency with risk and cost.
- **Defining “correct”**: Some attributes have no single truth (e.g., categorizations); agree with stakeholders on how accuracy is defined and measured.

## Best Practices

- Document accuracy rules and sources of truth in a data dictionary or contract; align with data ownership and stewardship.
- Automate accuracy checks where possible (e.g., in pipelines or as Data Quality Gates); combine with Data Quality Monitoring and alerting.
- Prioritize high-impact fields (e.g., revenue, identifiers) and critical pipelines; use sampling or profiling to extend coverage.
- Correct inaccuracies at the source or in early pipeline stages when feasible; log and review corrections for patterns.

## Related Topics

- [Data Validity](data-validity.md)(syntax and format correctness)
- [Data Consistency](data-consistency.md)(agreement across systems and fields)
- [Data Quality Metrics](data-quality-metrics.md)(measuring accuracy)
- [Data Profiling](data-profiling.md)(discovering accuracy issues)
- [Data Quality Gates](data-quality-gates.md)(enforcing accuracy before use)

## Further Reading

- Data quality dimensions (accuracy, completeness, consistency, etc.) in DAMA-DMBOK and similar frameworks
- Techniques for record linkage and deduplication when reconciling across sources

---

**Category**: Data Quality & Validation  
**Last Updated**: 2025
