# Data Pivoting/Unpivoting

## Overview
Pivoting and unpivoting are complementary transformations that change the shape of data between long (narrow) and wide formats. Pivoting turns unique values in a column into separate columns; unpivoting turns columns into rows, producing a long-format table.

## Definition
- **Pivoting (long → wide)**: Rows are grouped by one or more keys; values from a specified column become new column names, and a value column is aggregated (or chosen) to fill the new columns. Example: one row per product with columns for each month’s sales.
- **Unpivoting (wide → long)**: Selected columns are “melted” into a pair of columns: one for the original column name (or category), one for the value. Example: columns Jan, Feb, Mar become rows with month and sales value.

## Key Concepts

- **Long Format**: Many rows per entity, one column for “category” and one for “value” (tidy data)
- **Wide Format**: Fewer rows, many columns (e.g., one column per time period or category)
- **Aggregation in Pivot**: When multiple source rows map to one cell, an aggregate (SUM, MAX, etc.) is required
- **Idempotency**: Unpivot then pivot (with same aggregation) can recreate wide form; pivot then unpivot recreates long form
- **Schema Stability**: Pivoted schemas change when new values appear in the pivot column (e.g., new months)

## How It Works

**Pivot:**
1. Choose grouping columns (e.g., product_id, region)
2. Choose the column whose values become new column names (e.g., month)
3. Choose the value column and aggregate (e.g., SUM(sales))
4. Engine groups by keys, then spreads values into columns per pivot value

**Unpivot:**
1. Choose key columns that stay as rows (e.g., id, name)
2. Choose columns to “melt” into name/value pairs (e.g., Jan, Feb, Mar)
3. Name the new columns (e.g., period, amount)
4. Engine produces one row per key + column combination with the value

SQL: PIVOT/UNPIVOT (dialect-specific) or GROUP BY + CASE/MAX for pivot; UNION or native UNPIVOT for unpivot. DataFrames: pivot / pivot_table and melt / wide_to_long.

## Use Cases

- **Reporting**: Pivot for human-readable tables (e.g., months as columns); unpivot for loading into tools that expect long data
- **Time Series**: Switch between one-row-per-period (long) and one-row-per-entity-with-period-columns (wide)
- **ML and Stats**: Many algorithms or libraries expect long (tidy) format; pivot for presentation
- **APIs and Exports**: Match expected wide or long shape for downstream systems
- **Comparison Views**: Pivot to put two metrics side by side (e.g., actual vs. forecast by month)

## Considerations

- **Cardinality**: High cardinality in the pivot column creates many columns and sparse data
- **Schema Evolution**: New pivot values (e.g., new month) change wide schema; may require pipeline or schema updates
- **Nulls**: Missing combinations appear as null in pivot; define fill or default if needed
- **Performance**: Large pivots (many groups and many pivot values) can be memory- or CPU-intensive

## Best Practices

- **Prefer Long for Storage and Processing**: Easier to add new categories without schema change
- **Pivot for Presentation**: Use pivot when generating reports or feeding tools that need wide form
- **Document Pivot Values**: If wide, document which columns are pivot-derived and how they’re created
- **Handle New Values**: Decide how new pivot values are added (backfill, schema change, or dynamic columns)
- **Test Round-trip**: Unpivot then pivot (or vice versa) to validate logic

## Related Topics

- Data Format Conversion
- Data Aggregation
- Schema Evolution
- ETL/ELT
- Data Type Conversion

---

**Category**: Data Transformation  
**Last Updated**: 2024
