# Data Standardization

## Overview
Data standardization is the process of transforming data into consistent formats, units, codes, and naming so that it can be reliably combined, compared, and used across sources and consumers. It is a foundation for data quality, integration, and analytics.

## Definition
Standardization applies rules so that equivalent concepts are represented the same way: same units (e.g., meters, UTC), same codes (e.g., country ISO, status enums), same formats (e.g., YYYY-MM-DD, phone E.164), and consistent naming (e.g., column and value conventions). It does not change the meaning of data, only its representation.

## Key Concepts

- **Format Standardization**: Dates, numbers, phone numbers, and identifiers in a single canonical form
- **Unit Standardization**: Convert to base or agreed units (e.g., currency to USD, length to meters)
- **Code Standardization**: Map to standard vocabularies (e.g., ISO country, industry codes, internal enums)
- **Naming Conventions**: Consistent column names (snake_case, domain prefixes) and value labels
- **Canonical Model**: Target schema and value set that all sources are mapped to
- **Documentation**: Standards are documented and versioned so pipelines and consumers align

## How It Works

Standardization in pipelines:

1. **Define Standards**: Publish canonical formats, units, code lists, and naming (e.g., in data dictionary or schema registry)
2. **Map Sources**: For each source, define mapping from source values to canonical (e.g., “M”/“Male” → “MALE”)
3. **Apply Transformations**: In ETL/ELT, apply format parsing, unit conversion, and code lookup
4. **Handle Exceptions**: Define behavior for unknown or invalid values (reject, default, or flag)
5. **Validate Output**: Check that output conforms to standards (format checks, code list membership)
6. **Version and Communicate**: When standards change, version them and update pipelines and consumers
7. **Monitor**: Track conformance rates and exception volumes

Common operations:
- **Dates**: Parse various formats → ISO date or timestamp (UTC)
- **Phones**: Normalize to E.164 or national format
- **Addresses**: Normalize casing, abbreviations (St, Ave), and optional validation
- **Categories**: Map synonyms and variants to standard enum or code
- **Units**: Convert weight, length, currency to standard (with audit of conversion rates)

## Use Cases

- **Data Integration**: Align multiple sources (e.g., CRM, ERP, web) to a single model for reporting
- **Analytics**: Consistent dimensions and measures for dashboards and KPIs
- **Master Data**: Single representation for customer, product, or location across systems
- **Regulatory and Reporting**: Meet required formats and codes (e.g., XBRL, regulatory codes)
- **APIs and Exchanges**: Publish or consume data in agreed standards (e.g., ISO, HL7)

## Considerations

- **Information Loss**: Mapping to codes or ranges can lose nuance (e.g., free text → category)
- **Ambiguity**: Some source values map to multiple standards; define rules and document exceptions
- **Change Management**: Changing a standard affects all pipelines and consumers; version and communicate
- **Performance**: Large lookup tables or complex parsing can add latency; cache and optimize
- **Ownership**: Clear ownership of standard definitions and approval for new codes or formats

## Best Practices

- **Centralize Standards**: Maintain a single source of truth for code lists, units, and formats (data dictionary or registry)
- **Document Mappings**: Keep mapping tables (source value → standard) versioned and auditable
- **Validate Early**: Validate conformance as close to source as practical to catch issues early
- **Handle Unknowns Explicitly**: Define and log unknown or invalid values; do not silently default without policy
- **Review and Update**: Periodically review standards with domain owners and update mappings as sources evolve

## Related Topics

- [Data Normalization](data-normalization.md)
- [Data Cleansing](data-cleansing.md)
- [Data Quality](../quality/data-quality-metrics.md)
- [Data Type Conversion](data-type-conversion.md)
- [Metadata Management](../governance/metadata-management.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
