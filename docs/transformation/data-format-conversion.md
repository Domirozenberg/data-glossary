# Data Format Conversion

## Overview
Data format conversion is the process of changing data from one serialization or file format to another—e.g., CSV to Parquet, JSON to Avro, or XML to columnar—without changing the logical data. It is used to optimize storage, compatibility, and query performance across the pipeline.

## Definition
Format conversion reads records or files in a source format and writes them in a target format. The logical schema and values are preserved (subject to type and precision support in both formats); only the on-disk or wire representation changes. Conversion can be batch (file-to-file) or streaming (record-by-record).

## Key Concepts

- **Serialization Format**: How records are encoded (row vs. columnar, text vs. binary, schema-embedded vs. external)
- **Schema Handling**: Some formats embed schema (Avro, Parquet); others are schema-less or inferred (JSON, CSV)
- **Compression**: Often applied within the format (e.g., Parquet codecs); conversion may change compression
- **Splittability**: Whether the format supports parallel reads (e.g., Parquet) or not (e.g., single-file JSON)
- **Compatibility**: Target format must support the source types and semantics (e.g., nested types, decimals)
- **Idempotency**: Re-running conversion should produce the same output for same input

## How It Works

Conversion flow:

1. **Read Source**: Use format-specific reader (Spark, Pandas, Arrow, etc.) with optional schema
2. **Interpret Schema**: Infer or apply schema; resolve type mapping between formats
3. **Transform (Optional)**: Apply any schema or type adjustments during the pass
4. **Write Target**: Use format-specific writer with chosen options (compression, partitioning)
5. **Validate**: Check row count, sample records, or checksums to ensure correctness
6. **Clean Up**: Optionally remove or archive source files after verification

Considerations:
- **CSV → Parquet**: Often improves query performance and compression; specify delimiter, header, null representation
- **JSON → Parquet/Avro**: Flatten or preserve nested structure; align on date/number representation
- **Schema Evolution**: If source schema drifts, define how target schema is updated (merge, version, fail)

## Use Cases

- **Landing to Curated**: Convert raw CSV/JSON in landing zone to Parquet/Delta in silver/gold
- **Query Performance**: Columnar formats (Parquet, ORC) for analytical queries
- **Interoperability**: Convert to format required by downstream tool (e.g., Avro for Kafka, Parquet for Athena)
- **Storage Efficiency**: Move from verbose text to compressed binary to reduce cost
- **Streaming Sinks**: Convert from internal format to format required by sink (e.g., JSON for API)

## Considerations

- **Type Fidelity**: Not all types map cleanly (e.g., CSV has no native date type; JSON number precision)
- **Nested Data**: Nested and repeated structures differ across formats; flatten or normalize if needed
- **Performance**: Conversion is I/O and CPU bound; parallelism and compression matter
- **Schema Drift**: Evolving source schema requires a clear strategy for target schema and backfill

## Best Practices

- **Standardize on Few Formats**: Prefer one or two formats for analytics (e.g., Parquet/Delta) to simplify tooling
- **Document Mapping**: Record type and schema mapping between source and target formats
- **Validate After Conversion**: Row counts and spot checks; consider checksums for critical pipelines
- **Tune Compression**: Balance compression ratio and read/write speed (e.g., Snappy vs. Zstd)
- **Version Schema**: When format embeds schema, version it and document compatibility

## Related Topics

- [Data Type Conversion](data-type-conversion.md)
- [Schema Evolution](schema-evolution.md)
- [Parquet](../formats/parquet.md)
- [ETL/ELT](../patterns/etl-vs-elt.md)
- [Storage Compression](../storage/storage-compression.md)

---

**Category**: Data Transformation  
**Last Updated**: 2024
