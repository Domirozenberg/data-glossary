# Supabase

## Overview
Supabase is an open-source Backend-as-a-Service (BaaS) platform built on PostgreSQL that
provides a complete backend stack — database, authentication, file storage, real-time
subscriptions, and serverless functions — through a single hosted service. It is widely
adopted as a Firebase alternative that keeps data in a standard relational database,
making it a strong fit for data-driven applications that need both application backend
services and direct SQL access.

## Definition
Supabase is a managed platform that wraps PostgreSQL with a suite of developer-facing
services: an auto-generated REST and GraphQL API, row-level security, real-time change
listeners, object storage, and Edge Functions. It can be used as a fully hosted cloud
service or self-hosted via Docker.

## Key Concepts

- **PostgreSQL Core**: Every Supabase project is a full PostgreSQL instance — any
  standard SQL, extension, index, or tool that works with Postgres works with Supabase.
- **Auto-generated API (PostgREST)**: Supabase automatically generates a RESTful API
  from your database schema using PostgREST, so tables and views are immediately
  queryable over HTTP without writing custom endpoints.
- **GraphQL (pg_graphql)**: A GraphQL API is generated from the schema using the
  `pg_graphql` PostgreSQL extension, enabling GraphQL queries alongside REST with no
  separate resolver layer.
- **Row Level Security (RLS)**: PostgreSQL's native RLS policies are used to control
  which rows each authenticated user can read or write, enforcing access control at the
  database level.
- **Auth**: Built-in authentication supporting email/password, magic links, OAuth
  providers (Google, GitHub, etc.), and phone/OTP, with JWTs issued per session and
  integrated with RLS policies.
- **Realtime**: A WebSocket-based service that streams database change events (inserts,
  updates, deletes) to connected clients in real time, powered by PostgreSQL's logical
  replication.
- **Storage**: S3-compatible object storage for files and media, with access policies
  tied to the Auth system.
- **Edge Functions**: Serverless functions deployed globally (built on Deno) for custom
  backend logic that cannot be expressed in SQL or RLS policies.
- **pgvector**: Native support for the `pgvector` PostgreSQL extension, enabling vector
  embeddings and similarity search directly in the database — commonly used for AI and
  semantic search use cases.

## How It Works

1. **Create a project**: A Supabase project provisions a dedicated PostgreSQL instance
   with all services pre-configured.
2. **Define schema**: Create tables, views, and functions using the SQL editor, Table
   Editor UI, or migrations managed in a local CLI project.
3. **Enable RLS**: Define row-level security policies to control per-user data access.
4. **Connect clients**: Use the Supabase client SDK (JavaScript, Python, Flutter, Swift,
   etc.) or any standard PostgreSQL driver to interact with the database.
5. **Use the auto-generated API**: Tables are immediately accessible via REST or GraphQL
   endpoints authenticated with JWTs.
6. **Subscribe to changes**: Clients subscribe to table change events over WebSockets for
   real-time updates.
7. **Deploy Edge Functions**: Write custom server-side logic in TypeScript/Deno and
   deploy globally for low-latency execution.

## Use Cases

- **Web and mobile applications**: A complete backend for apps that need auth, a
  relational database, and file storage without managing separate services.
- **Rapid prototyping**: Instant APIs from schema design allow teams to iterate quickly
  without building custom backend endpoints.
- **Real-time collaboration tools**: The Realtime service enables live-updating UIs such
  as dashboards, collaborative editors, or notification systems.
- **AI and vector search**: pgvector support makes Supabase a natural fit for storing
  embeddings and running semantic similarity queries alongside structured data.
- **Analytics backends**: Direct PostgreSQL access supports complex analytical queries,
  and Supabase integrates with BI tools that speak Postgres (e.g., Metabase, Grafana).
- **Firebase migration**: Teams migrating from Firebase to a relational, SQL-first
  platform use Supabase as a drop-in alternative with a familiar developer experience.

## Considerations

- **RLS complexity**: Row-level security is powerful but can become complex and hard to
  debug in applications with sophisticated permission models.
- **PostgreSQL constraints**: Supabase inherits PostgreSQL's scaling model — it scales
  vertically by default. Very high write throughput workloads may require connection
  pooling (Supabase provides PgBouncer) or a sharding strategy.
- **Vendor lock-in**: While Supabase is open-source and self-hostable, the hosted service
  adds proprietary orchestration. Migrating away from the managed platform requires
  exporting data and replicating the surrounding services.
- **Edge Functions cold starts**: Like other serverless platforms, Edge Functions can
  experience cold start latency for infrequently invoked functions.
- **Not a data warehouse**: Supabase is an OLTP (transactional) database optimised for
  application workloads, not large-scale analytical queries. Heavy analytics should be
  offloaded to a dedicated warehouse via ETL/ELT.

## Best Practices

- Enable Row Level Security on every table — disable it only on tables that are
  intentionally fully public, and document the reason.
- Use the Supabase CLI and migration files to manage schema changes as code, enabling
  version control and reproducible environments.
- Use connection pooling (PgBouncer) for applications with many short-lived connections,
  such as serverless functions.
- Keep Edge Functions thin — push business logic into PostgreSQL functions or views
  where possible to keep latency low and leverage the database's optimiser.
- Store vector embeddings with `pgvector` alongside the source data they describe to
  enable hybrid queries (semantic + structured filters) in a single SQL statement.
- Monitor query performance with `pg_stat_statements` and the Supabase dashboard to
  catch slow queries early.
- For analytical workloads, replicate data out of Supabase into a dedicated warehouse
  (e.g., BigQuery, Snowflake) rather than running heavy aggregations on the OLTP instance.

## Related Documentation

- [Supabase Documentation](https://supabase.com/docs) — Official docs, quickstart, and reference
- [Supabase GitHub](https://github.com/supabase/supabase) — Source code and community
- [PostgREST Documentation](https://postgrest.org/) — The REST API layer Supabase uses
- [pgvector](https://github.com/pgvector/pgvector) — Vector similarity search extension

## Related Topics

- [Relational Database (RDBMS)](../databases/relational-database.md)
- [Database as a Service (DBaaS)](../databases/database-as-a-service.md)
- [Row-Level Security / Access Control](../governance/access-control.md)
- [Vector Database](../databases/vector-database.md)
- [Embeddings](../databases/embeddings.md)
- [Real-time Analytics](../analytics/real-time-analytics.md)
- [ETL](../patterns/etl.md)
- [ELT](../patterns/elt.md)

---

**Category**: Tools & Products  
**Last Updated**: 2026
