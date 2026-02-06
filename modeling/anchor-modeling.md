# Anchor Modeling

## Overview
Anchor modeling is a database modeling technique that structures data around "anchors" (entities), "attributes" (one table per attribute for an anchor), and "ties" (relationships between anchors). It emphasizes information preservation, schema evolution, and query flexibility by avoiding destructive schema changes and storing each attribute in its own historized table.

## Definition
In anchor modeling, the model consists of: (1) **Anchors**—one table per entity, containing only a surrogate key; (2) **Attributes**—separate tables for each attribute of an anchor, each with anchor key, value, and often temporal columns for history; (3) **Ties**—tables that represent relationships between two or more anchors, with optional temporal columns. This structure allows adding new attributes or relationships without altering existing tables and preserves full history by default.

## Key Concepts

- **Anchor**: Entity; represented by a table with a single surrogate key column (e.g., anchor_id)
- **Attribute**: One table per attribute; columns typically include anchor key, value, and metadata (e.g., changed_at); supports temporal tracking
- **Tie**: Relationship between anchors; table with foreign keys to the participating anchors and optional temporal columns
- **Information Preservation**: No destructive changes; new attributes and ties add new tables, not new columns on existing tables
- **Schema Evolution**: New business concepts map to new anchors, attributes, or ties without migrating existing data
- **Temporal by Default**: Attribute and tie tables can store history via timestamps or validity periods
- **6NF-Oriented**: Design tends toward sixth normal form (no non-key attributes depend on a proper subset of a key)

## How It Works

Anchor modeling design:

1. **Identify Anchors**: List core entities (e.g., Customer, Product, Order)
2. **Create Anchor Tables**: One table per anchor with surrogate key only
3. **Identify Attributes**: For each anchor, list attributes; create one attribute table per attribute with (anchor key, value, [temporal columns])
4. **Identify Ties**: List relationships between anchors; create tie tables with keys to anchors and optional temporal columns
5. **Load Data**: Insert into anchors (get surrogate keys), then populate attribute and tie tables; use same anchor key across attribute tables to "reconstruct" an entity
6. **Query**: Join anchor to attribute tables (and ties) to build current or point-in-time view; views or marts often wrap this for consumption
7. **Evolve**: Add new attribute or tie by adding new table; no ALTER on existing tables

Characteristics:
- **Many Tables**: More tables than star or normalized 3NF; one table per attribute and per tie
- **Joins to Reconstruct**: Current state or history of an entity requires joining anchor to all its attribute tables
- **No Attribute Drops**: "Removing" an attribute is done by ceasing to populate it or by soft delete, not by dropping a column
- **Audit and History**: Temporal columns on attributes and ties support "as-of" and full history queries

## Use Cases

- **Highly Changing Schemas**: Domains where new attributes and relationships are added frequently
- **Historical and Audit Requirements**: Need for full history and point-in-time querying without complex SCD
- **Integration Hubs**: Multiple sources contributing different attributes to the same anchor over time
- **Regulatory and Compliance**: Requirement to never lose or overwrite historical data
- **Research and Exploration**: Schema that evolves as understanding of the domain grows

## Considerations

- **Query Complexity**: Reconstructing an entity or relationship requires many joins; views or materialized layers help
- **Table Proliferation**: Many small tables; operational and naming discipline required
- **Tool Support**: Some BI tools expect fewer, wider tables; semantic layer or views needed
- **Learning Curve**: Different from star and 3NF; team needs to understand anchors, attributes, and ties
- **Performance**: Join-heavy queries; indexing and materialized views or marts may be needed for performance

## Best Practices

- **Name Consistently**: Clear naming for anchors (e.g., anchor_customer), attributes (e.g., attr_customer_name), ties (e.g., tie_customer_order)
- **Use Views or Marts**: Provide star-like or flattened views for reporting and analytics
- **Document Model**: Maintain diagram and dictionary of anchors, attributes, and ties
- **Temporal Strategy**: Decide which attributes and ties are historized and how (e.g., changed_at vs. valid_from/valid_to)
- **Key Management**: Surrogate keys for anchors; consistent generation and assignment in ETL

## Related Topics

- Data Vault Modeling
- Dimensional Modeling
- Schema Evolution
- Normalization
- Surrogate Keys
- Data Historization

---

**Category**: Data Modeling  
**Last Updated**: 2024
