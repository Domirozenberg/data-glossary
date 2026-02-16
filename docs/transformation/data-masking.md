# Data Masking

## Overview
Data masking is the process of obscuring or replacing sensitive data with non-sensitive values so that data remains usable for development, testing, analytics, or sharing while reducing the risk of exposure. It can be applied statically (at rest) or dynamically (at query or access time).

## Definition
Data masking transforms sensitive values (e.g., PII, financial, or health data) into values that preserve format and optionally statistical properties but prevent identification or misuse. Types include static masking (replace in copy), dynamic masking (mask at read time via views or policies), and deterministic masking (same input always produces same mask for referential consistency).

## Key Concepts

- **Masking Techniques**: Substitution (e.g., fake names), shuffling (reorder within column), redaction (e.g., show last 4 digits), hashing, tokenization, or generalization (e.g., region instead of address)
- **Format Preservation**: Optional preservation of length and type (e.g., 16-digit card → 16-digit token) for testing and UI
- **Deterministic Masking**: Same plaintext yields same mask across tables for join consistency in non-production
- **Reversibility**: Irreversible (one-way) vs. reversible (with key) for tokenization; policy defines when each is allowed
- **Scope**: Per column, per environment (e.g., mask in dev/test, unmask in prod), or per role (RBAC + dynamic mask)
- **Regulatory Alignment**: Align with PCI-DSS, HIPAA, GDPR, or internal policy (e.g., what must be masked where)

## How It Works

Masking in pipelines:

1. **Classify Data**: Identify columns that contain PII or other sensitive data
2. **Choose Technique**: Select mask type per column (redact, substitute, hash, tokenize, etc.)
3. **Apply Mask**: In ETL—replace values in a dedicated copy; or at read—apply view/function or policy engine
4. **Preserve Referential Integrity (if needed)**: Use deterministic or consistent substitution so joins still work in masked copy
5. **Document and Audit**: Record what is masked, how, and where; log access to unmasked data
6. **Validate**: Ensure no unmasked sensitive data in shared/test environments; run checks in CI

Static: one-time or periodic job that produces masked dataset. Dynamic: database views, policy engines (e.g., Apache Ranger), or query proxies that rewrite results by role.

## Use Cases

- **Non-Production Environments**: Provide realistic but safe data for dev, test, and staging
- **Analytics and BI**: Allow analysts to use data without exposing PII (dynamic or pre-masked tables)
- **Sharing with Third Parties**: Mask or tokenize before sending to partners or cloud analytics
- **Compliance**: Meet “data minimization” and “purpose limitation” by masking where not needed
- **Support and Debugging**: Support teams see masked data; unmask only under controlled process

## Considerations

- **Utility vs. Privacy**: Strong masking reduces utility (e.g., no real names for testing); balance by use case
- **Performance**: Dynamic masking adds overhead per query; static masking is one-time cost
- **Key Management**: Reversible tokenization requires secure key storage and rotation
- **Consistency**: Deterministic masking must be consistent across pipelines and tables for joins
- **Re-identification Risk**: Poor masking (e.g., weak hashing or partial redaction) may still allow inference

## Best Practices

- **Classify and Document**: Maintain a data classification and document which columns are masked and how
- **Prefer Irreversible Where Possible**: Use one-way hash or redaction unless reversible tokenization is required
- **Test with Masked Data**: Validate pipelines and apps with masked data to catch dependency on plaintext
- **Principle of Least Privilege**: Unmask only for roles and environments that need it; audit access
- **Review Periodically**: Re-assess masking rules as schema and regulations change

## Related Topics

- [Data Anonymization](data-anonymization.md)
- [PII Handling](../governance/pii-handling.md)
- [Data Privacy](../governance/data-privacy.md)
- [Access Control](../governance/access-control.md)
- [GDPR Compliance](../governance/gdpr-compliance.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
