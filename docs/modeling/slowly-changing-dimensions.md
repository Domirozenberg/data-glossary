# Slowly Changing Dimensions (SCD)

## Overview
Slowly changing dimensions (SCD) are techniques for handling changes to dimension attribute values over time so that historical facts remain correctly associated with the dimension state that was valid when the fact occurred. Different SCD types trade off between simplicity, storage, and ability to track and report on history.

## Definition
SCD refers to a set of strategies (Type 1 through Type 6 and hybrids) for updating dimension tables when source attributes change. The choice determines whether the dimension keeps only current state (Type 1), keeps full history with new rows (Type 2), keeps limited history with additional columns (Type 3), or combines approaches. The goal is to preserve correct relationship between facts and dimension context over time.

## Key Concepts

- **Type 1 (Overwrite)**: Update the dimension row in place; no history; simplest
- **Type 2 (New Row)**: Add a new dimension row with new surrogate key; keep old row; facts keep pointing to old key for historical accuracy; use effective/end dates and current flag
- **Type 3 (New Column)**: Add columns for "previous" value (e.g., previous_region); limited to one or few changes per attribute
- **Type 4 (History Table)**: Current state in main dimension; full history in separate history table
- **Type 5 (Type 1 + Type 2 Hybrid)**: Some attributes Type 1 (current only), others Type 2 (history); or use mini-dimension for volatile attributes
- **Type 6 (Hybrid 1+2+3)**: Combine current value, previous value, and full history (rarely used)
- **Surrogate Key**: Essential for Type 2; new row gets new surrogate key so fact table references remain stable
- **Effective/End Date**: In Type 2, columns that define the period during which the row was current
- **Current Flag**: Boolean or indicator for "current" row in Type 2 for easy filtering

## How It Works

**Type 1**: On attribute change, UPDATE dimension row. No history; all facts see new value. Used for corrections or when history is not needed.

**Type 2**: On attribute change, INSERT new dimension row with new surrogate key; set effective date, set end date (or current flag) on old row. ETL must assign new surrogate key and keep natural key for matching. Facts that referenced the old surrogate key continue to show historical context; new facts use new key. Queries for "current" use current flag or max effective date.

**Type 3**: Add column(s) for previous value. On change, UPDATE current value and copy current to previous. Only one level of history; used for "current and prior" reporting (e.g., current and previous region).

**Implementation (Type 2 typical)**:
1. Match incoming dimension row by natural key (and optionally source)
2. Compare attributes; if changed, close current row (set end_date, current_flag = false) and insert new row with new surrogate key, effective_date, current_flag = true
3. If new natural key, insert new row
4. Fact table always stores surrogate key; no change to fact rows when dimension is updated

## Use Cases

- **Customer/Product Attributes**: Name, segment, region, status changes over time; report "sales when customer was in segment A"
- **Organizational Hierarchy**: Employee or cost center changes; report by structure at point in time
- **Compliance and Audit**: Need to know what attribute value was at transaction time
- **Trend Analysis**: Compare behavior before/after attribute change (e.g., before/after region change)
- **Type 1**: When history is irrelevant (e.g., typo correction, current state only)

## Considerations

- **Storage**: Type 2 increases dimension row count over time; archive or limit history if needed
- **ETL Complexity**: Type 2 requires careful key generation, effective/end date logic, and fact key resolution
- **Query Complexity**: "Current" vs. "as-of" queries; BI tools must understand current flag or date range
- **Multiple Attributes**: When many attributes change at different times, Type 2 can create many rows per natural key; consider mini-dimensions or Type 4
- **Performance**: Large Type 2 dimensions need indexing on natural key, effective/end date, and current flag

## Best Practices

- **Choose Type per Dimension (or Attribute)**: Not all dimensions need Type 2; use Type 1 where history is not required
- **Consistent Surrogate Key Handling**: Fact table always references dimension surrogate key; never update fact table when dimension gets new row
- **Document SCD Type**: Document which dimensions use which type and how "current" is defined
- **Test Changes**: Test ETL with attribute changes to ensure new row created (Type 2) and facts unchanged
- **Archive Strategy**: Plan for very large Type 2 dimensions (e.g., archive old rows, or limit retention)

## Related Topics

- [Dimension Tables](dimension-tables.md)
- [Fact Tables](fact-tables.md)
- [Surrogate Keys](surrogate-keys.md)
- [Dimensional Modeling](dimensional-modeling.md)
- [Star Schema](star-schema.md)
- [Data Historization](slowly-changing-dimensions.md)

---

**Category**: Data Modeling  
**Last Updated**: 2024
