# Apache Airflow

## Overview
Apache Airflow is an open-source platform for programmatically authoring, scheduling, and monitoring workflows. It is widely used for data pipeline orchestration, enabling teams to define complex DAGs (Directed Acyclic Graphs) of tasks, manage dependencies, retry on failure, and monitor execution. Airflow is commonly paired with [DBT](dbt.md) for transformation workflows.

## Definition
Airflow is a workflow orchestration platform that allows users to define tasks and their dependencies as Python code. DAGs define the structure; tasks define the work. A scheduler runs tasks in order based on dependencies, and the web UI provides monitoring and manual triggering.

## Key Concepts

- **DAG (Directed Acyclic Graph)**: Workflow definition with tasks and dependencies
- **Operators**: Reusable task types (Bash, Python, SQL, etc.)
- **Tasks**: Instances of operators within a DAG
- **Task Dependencies**: Define execution order via `>>` and `<<`
- **Scheduler**: Runs tasks based on schedule and dependencies
- **Executors**: How tasks run (Local, Celery, Kubernetes)
- **XCom**: Cross-task communication
- **Hooks**: Connections to external systems

## How It Works

1. **Define DAG**: Create Python file with DAG definition
2. **Add Tasks**: Use operators for each step
3. **Set Dependencies**: Define task order with `>>` and `<<`
4. **Schedule**: Set cron or interval for runs
5. **Scheduler**: Runs tasks when dependencies are met
6. **Monitor**: Use web UI for status, logs, retries

Airflow handles [workflow scheduling](../orchestration/workflow-scheduling.md), [task dependencies](../orchestration/task-dependencies.md), [retry strategies](../orchestration/retry-strategies.md), and [error handling](../orchestration/error-handling.md).

## Use Cases

- **ETL/ELT Orchestration**: Coordinate extract, load, transform steps
- **Data Pipeline Scheduling**: Run batch jobs on schedule
- **DBT Runs**: Trigger DBT models via BashOperator or DBT operator
- **Multi-System Workflows**: Coordinate across databases, APIs, cloud services
- **Data Quality Checks**: Run validation after loads

## Considerations

- **Python-Centric**: DAGs are Python; learning curve for non-Python users
- **Scalability**: Requires Celery or Kubernetes for large workloads
- **Database**: Uses metadata DB for state; can become bottleneck
- **Complexity**: Overkill for simple cron jobs

## Best Practices

- **Idempotent Tasks**: Design tasks to be safely retried
- **Resource Pools**: Use pools to limit concurrent tasks
- **Sensible Retries**: Configure retries with backoff
- **Monitoring**: Set up alerts for failures

## Related Documentation

- [Apache Airflow Documentation](https://airflow.apache.org/docs/) — Official docs and guides
- [Airflow GitHub](https://github.com/apache/airflow) — Source code and releases
- [Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html) — Getting started tutorial

## Related Topics

- [Pipeline Orchestration](../orchestration/pipeline-orchestration.md)
- [Workflow Scheduling](../orchestration/workflow-scheduling.md)
- [Task Dependencies](../orchestration/task-dependencies.md)
- [Error Handling](../orchestration/error-handling.md)
- [Retry Strategies](../orchestration/retry-strategies.md)
- [Batch Processing](../architecture/batch-processing.md)
- [DBT](dbt.md)

---

**Category**: Tools & Products  
**Last Updated**: 2025
