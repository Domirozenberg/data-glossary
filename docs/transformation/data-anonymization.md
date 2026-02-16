# Data Anonymization

## Overview
Data anonymization is the process of removing or altering identifying information so that individuals cannot be readily identified from the data, while preserving utility for analysis, research, or testing. It supports privacy compliance and ethical data use when full identification is not required.

## Definition
Anonymization modifies or removes direct identifiers (e.g., name, email, ID) and often reduces quasi-identifiers (e.g., age, zip, job) through generalization, suppression, or perturbation so that re-identification risk is acceptably low. The result is “anonymous” in a legal or policy sense when identification is not reasonably likely. It differs from masking (which may be reversible or format-only) in that the goal is irreversible de-identification.

## Key Concepts

- **Direct Identifiers**: Attributes that directly identify a person (name, SSN, email); typically removed or strongly altered
- **Quasi-identifiers**: Attributes that can identify when combined (age + zip + gender); generalized or perturbed
- **k-Anonymity**: Each quasi-identifier combination appears for at least k individuals (group size)
- **Generalization**: Replace specific value with range or category (e.g., age 25 → “20–30”, zip → region)
- **Suppression**: Remove or withhold values that are too identifying (e.g., rare combinations)
- **Perturbation**: Add noise or swap values to reduce linkability while preserving distribution (e.g., for analytics)
- **Re-identification Risk**: Residual risk that data can be linked back to individuals; assessed and documented

## How It Works

Anonymization process:

1. **Identify Identifiers**: Classify direct and quasi-identifiers in the dataset
2. **Assess Risk**: Consider linkability to other datasets and background knowledge
3. **Choose Techniques**: Remove/suppress direct IDs; generalize or perturb quasi-identifiers to meet policy (e.g., k-anonymity, differential privacy)
4. **Apply Transformations**: Run suppression, generalization, or perturbation (batch or in pipeline)
5. **Assess Utility**: Check that analytics and reporting still meet requirements
6. **Document and Review**: Record techniques, parameters, and residual risk; periodic re-assessment
7. **Govern Access**: Treat anonymized data as sensitive; restrict access and sharing per policy

Techniques:
- **Removal**: Drop identifier columns
- **Generalization**: Replace with ranges or categories (e.g., date → year)
- **Noise Addition**: Add random noise to numeric or date (e.g., ±N days)
- **Swapping**: Swap values across records within a group (e.g., same gender/region)
- **Synthetic Data**: Replace with synthetic data that preserves statistics but not real individuals

## Use Cases

- **Research and Analytics**: Share or publish datasets without exposing individuals
- **Regulatory Compliance**: Meet GDPR, HIPAA, or other requirements for “anonymous” data
- **Third-Party Sharing**: Provide data to partners or vendors without PII
- **Testing and ML**: Train or test on data that does not identify real users
- **Public or Open Data**: Release datasets for transparency or research with low re-identification risk

## Considerations

- **Utility vs. Privacy**: Strong anonymization can reduce analytical value; balance by use case and risk
- **Re-identification**: Sophisticated linkage or background knowledge can sometimes re-identify; document and limit risk
- **Context**: “Anonymous” is context-dependent (e.g., same data may be low risk internally but higher when published)
- **Regulatory Definitions**: Legal definitions of “anonymous” and “personal data” vary; align with legal/compliance
- **Irreversibility**: True anonymization should not be reversible; avoid storing mapping to original identities

## Best Practices

- **Document Methodology**: Record which attributes were anonymized, how, and residual risk assessment
- **Involve Legal/Privacy**: Align with privacy and legal on definition of “anonymous” and acceptable risk
- **Test Utility**: Validate that key analyses still work on anonymized data
- **Limit Linkability**: Avoid releasing multiple anonymized datasets that can be joined to re-identify
- **Review Periodically**: Re-assess re-identification risk as new data or techniques become available

## Related Topics

- [Data Masking](../governance/data-masking.md)
- [Data Privacy](../governance/data-privacy.md)
- [PII Handling](../governance/pii-handling.md)
- [GDPR Compliance](../governance/gdpr-compliance.md)
- [Data Classification](../governance/data-classification.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
