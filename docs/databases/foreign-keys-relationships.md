# Foreign Keys and Relationships

## Overview
Foreign keys and relationships are fundamental concepts in relational databases that establish connections between tables. They enforce referential integrity, ensuring that relationships between data remain consistent and valid.

## Definition
A foreign key is a column or set of columns in one table that references the primary key of another table. It establishes a relationship between tables and enforces referential integrity, ensuring that referenced data exists and maintaining data consistency across related tables.

## Key Concepts

- **Foreign Key**: Column referencing another table's primary key
- **Referential Integrity**: Ensuring referenced data exists
- **Primary Key**: Unique identifier in referenced table
- **Relationship Types**: One-to-one, one-to-many, many-to-many
- **Cascade Operations**: Cascading updates and deletes
- **Constraints**: Foreign key constraints enforce integrity
- **Joins**: Foreign keys enable efficient joins

## How It Works

Foreign keys and relationships:

1. **Primary Key Definition**: Define primary key in parent table
2. **Foreign Key Definition**: Define foreign key in child table
3. **Constraint Creation**: Create foreign key constraint
4. **Integrity Enforcement**: Database enforces referential integrity
5. **Relationship Queries**: Use relationships in queries (joins)
6. **Cascade Rules**: Define cascade behavior for updates/deletes

Relationship types:
- **One-to-One**: One record relates to one record
- **One-to-Many**: One record relates to many records
- **Many-to-Many**: Many records relate to many records (via junction table)

## Use Cases

- **Data Integrity**: Maintaining data integrity
- **Relational Design**: Designing relational databases
- **Data Consistency**: Ensuring data consistency
- **Efficient Joins**: Enabling efficient joins
- **Data Modeling**: Modeling relationships between entities

## Considerations

- **Performance**: Foreign keys can impact performance
- **Cascade Behavior**: Planning cascade operations
- **Orphaned Records**: Preventing orphaned records
- **Index Performance**: Foreign keys should be indexed
- **Constraint Overhead**: Constraint checking overhead

## Best Practices

- **Index Foreign Keys**: Index foreign key columns
- **Plan Cascade Rules**: Plan update/delete cascade behavior
- **Document Relationships**: Document table relationships
- **Test Integrity**: Test referential integrity
- **Monitor Performance**: Monitor foreign key performance
- **Use Appropriately**: Use foreign keys appropriately

## Related Topics

- [Relational Database](relational-database.md)
- Primary Keys
- Referential Integrity
- Database Relationships
- Joins

---

**Category**: Database Types & Technologies  
**Last Updated**: 2024
