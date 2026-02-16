# Data Type Conversion

## Overview
Data type conversion (casting or coercion) is the process of changing values from one data type to another—e.g., string to number, timestamp to date, or decimal to integer. It is essential for consistent processing, joining datasets, and meeting the expectations of downstream systems and analytics.

## Definition
Type conversion transforms the representation and semantics of data so that it fits a target type. It can be explicit (invoked by the developer via cast functions) or implicit (performed by the engine according to rules). Conversions may be lossless (e.g., int to bigint) or lossy (e.g., float to int, or truncation).

## Key Concepts

- **Cast vs. Coerce**: Explicit cast (e.g., CAST(x AS INT)) vs. implicit conversion by the engine
- **Lossy vs. Lossless**: Some conversions drop precision (e.g., timestamp to date) or range (overflow)
- **Format and Locale**: String-to-date/number conversion depends on format and locale
- **Null and Invalid**: Define behavior when source is null or not convertible (null, error, or default)
- **Type Promotion**: Automatic widening (e.g., int to long) in expressions
- **Semantic Equivalence**: Same value in different types (e.g., "123" and 123)

## How It Works

Conversion in pipelines:

1. **Identify Source and Target Types**: Per column or expression (e.g., string → integer, string → timestamp)
2. **Choose Conversion Method**: Use engine cast (SQL CAST, DataFrame cast) or custom UDF/expression
3. **Handle Format (if string)**: For string-to-date/number, specify format or use locale-aware parsing
4. **Handle Failures**: Invalid input—fail row/job, return null, or use default per policy
5. **Validate**: Spot-check and monitor for overflow, truncation, or unexpected nulls
6. **Document**: Record conversion rules and any lossy behavior

Common conversions:
- **Numeric**: String → int/long/decimal; float → decimal (precision); int → float (possible precision loss)
- **Temporal**: String → date/timestamp (with format); timestamp → date (truncate time); timezone handling
- **Boolean**: String/int to boolean (e.g., "true"/1 → true)
- **Binary**: String (hex/base64) to binary and back

## Use Cases

- **Ingestion**: Normalize types from CSV, JSON, or APIs (often string-heavy) to warehouse types
- **Joining**: Align key types (e.g., string ID to bigint) across tables
- **Analytics**: Ensure numeric and date types for aggregations and time-based filters
- **API and Exports**: Convert internal types to string or ISO formats for external systems
- **Data Quality**: Standardize types before validation and deduplication

## Considerations

- **Precision and Overflow**: Integer and decimal overflow; float rounding
- **Timezone**: Timestamp conversion and storage (UTC vs. local) must be explicit
- **Locale**: Number and date string parsing varies by locale
- **Null and Empty**: Distinguish null, empty string, and "null" string; define consistent behavior
- **Performance**: Bulk conversion is usually efficient; per-row UDFs can be costly

## Best Practices

- **Be Explicit**: Prefer explicit CAST with target type rather than relying on implicit coercion
- **Centralize Format Strings**: Use shared constants or config for date/number formats
- **Handle Invalid Data**: Define policy (fail, null, or default) and log or metric invalid count
- **Document Lossy Conversions**: Record truncation or precision loss (e.g., timestamp → date)
- **Test Boundaries**: Test null, empty, overflow, and invalid strings in type conversion tests

## Related Topics

- [Data Format Conversion](data-format-conversion.md)
- [Data Standardization](data-standardization.md)
- [Schema Evolution](schema-evolution.md)
- [Data Cleansing](data-cleansing.md)
- [Data Validation Rules](../quality/data-validation-rules.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
