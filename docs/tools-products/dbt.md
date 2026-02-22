# DBT (Data Build Tool)

## Overview
DBT (Data Build Tool) is an open-source command-line tool that enables data analysts and engineers to transform data in warehouses using SQL and Jinja. It applies software engineering best practices—version control, testing, and documentation—to data transformation workflows, making it a core component of the modern [ELT](../patterns/elt.md) stack.

## Definition
DBT is a transformation framework that compiles SQL and Jinja templates into executable SQL, runs queries against a data warehouse, and manages dependencies between models. It supports incremental updates, testing, and documentation generation, enabling teams to build reliable, maintainable data pipelines.

## Key Concepts

- **Models**: SQL-based transformations defined as `.sql` files
- **Jinja Templating**: Dynamic SQL generation with Jinja2
- **DAG Dependencies**: Automatic dependency graph from model references
- **Incremental Models**: Run only new or changed data
- **Tests**: Built-in and custom tests for data quality
- **Documentation**: Auto-generated docs from schema and descriptions
- **Seeds**: CSV files loaded into the warehouse
- **Snapshots**: Slowly changing dimension tracking

## How It Works

1. **Define Models**: Write SQL in `.sql` files
2. **Reference Dependencies**: Use `ref()` to link models
3. **Compile**: DBT compiles Jinja + SQL into SQL
4. **Run**: Execute against warehouse (Snowflake, BigQuery, etc.)
5. **Test**: Run tests on data quality
6. **Document**: Generate docs from schema and descriptions

DBT does not run transformations itself—it orchestrates SQL execution against your warehouse. It works with [Airflow](airflow.md) and other orchestration tools for scheduling.

## Use Cases

- **Analytics Engineering**: Building data marts and reporting layers
- **ELT Pipelines**: Transform data after loading into warehouse
- **Data Quality**: Built-in tests and custom assertions
- **Documentation**: Auto-generated data lineage and docs
- **Version Control**: SQL transformations as code

## Considerations

- **Warehouse-Centric**: Requires a supported warehouse (Snowflake, BigQuery, etc.)
- **SQL Only**: No support for non-SQL transformations
- **Orchestration**: Often paired with Airflow for scheduling
- **Learning Curve**: Jinja for advanced use cases

## Best Practices

- **Use Incremental Models**: For large tables, use incremental models
- **Add Tests**: Document and test columns and relationships
- **Modularize**: Keep models small and focused
- **Document**: Add descriptions to models and columns

## Related Documentation

- [DBT Documentation](https://docs.getdbt.com/) — Official docs, quickstart, and reference
- [DBT Cloud](https://www.getdbt.com/product/dbt-cloud) — Managed DBT platform
- [DBT GitHub](https://github.com/dbt-labs/dbt-core) — Source code and releases

## Related Topics

- [ELT](../patterns/elt.md)
- [ETL vs ELT](../patterns/etl-vs-elt.md)
- [Data Transformation](../transformation/data-cleansing.md)
- [Dimensional Modeling](../modeling/dimensional-modeling.md)
- [Schema Evolution](../transformation/schema-evolution.md)
- [Data Testing](../advanced/data-testing.md)
- [Data Lineage](../governance/data-lineage.md)
- [Data Quality Metrics](../quality/data-quality-metrics.md)
- [Airflow](airflow.md)

---

**Category**: Tools & Products  
**Last Updated**: 2025
