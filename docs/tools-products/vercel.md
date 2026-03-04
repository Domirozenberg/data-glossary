# Vercel

## Overview
Vercel is a cloud platform for deploying and hosting frontend applications and serverless
functions, optimised for frameworks like Next.js (which Vercel created). It provides a
global edge network, zero-configuration deployments from Git, and serverless compute
that scales automatically, making it a popular choice for modern web applications that
consume data APIs and need fast, globally distributed delivery.

## Definition
Vercel is a Platform-as-a-Service (PaaS) that builds and deploys web projects directly
from a Git repository. It serves static assets and server-rendered pages from a global
Content Delivery Network (CDN), and executes backend logic through serverless and edge
functions without requiring any server management.

## Key Concepts

- **Git-based Deployments**: Every push to a Git branch triggers an automatic build and
  deployment. Pull requests get their own isolated preview URL, enabling pre-merge review
  of both code and UI.
- **Edge Network**: Static assets and cached responses are served from Vercel's global
  CDN, minimising latency by serving content from the node closest to the end user.
- **Serverless Functions**: Backend logic is packaged as stateless functions that run
  on-demand in the cloud (Node.js, Python, Go, Ruby). They scale to zero when idle and
  scale horizontally under load with no configuration.
- **Edge Functions**: A lighter-weight alternative to serverless functions that run in
  Vercel's edge runtime (V8 isolates) rather than full Node.js containers — sub-millisecond
  cold starts, globally distributed, but with a restricted runtime (no full Node.js APIs).
- **Next.js Integration**: Vercel is the reference hosting platform for Next.js and
  natively supports its features — App Router, Server Components, incremental static
  regeneration (ISR), and streaming — without additional configuration.
- **Preview Deployments**: Every branch and pull request is deployed to a unique,
  shareable URL. Stakeholders can review changes before they reach production.
- **Environment Variables**: Secrets and configuration values are managed per-environment
  (development, preview, production) and injected at build time or runtime.
- **Analytics & Web Vitals**: Built-in Real User Monitoring (RUM) tracks Core Web Vitals
  (LCP, CLS, FID) in production, providing performance data per page and per deployment.
- **Vercel KV / Postgres / Blob**: Managed data primitives — a Redis-compatible key-value
  store, a serverless Postgres database (powered by Neon), and object storage — available
  directly from the Vercel dashboard, integrated with the deployment environment.

## How It Works

1. **Connect a repository**: Link a GitHub, GitLab, or Bitbucket repository to a Vercel
   project.
2. **Configure the build**: Vercel auto-detects the framework and sets the build command
   and output directory. Override these in `vercel.json` if needed.
3. **Push code**: On every push, Vercel runs the build, uploads static assets to the
   CDN, and deploys serverless functions to the edge.
4. **Serve traffic**: Incoming requests are routed to the nearest CDN node for static
   assets or to the serverless/edge function runtime for dynamic responses.
5. **Preview and promote**: Preview URLs let teams verify changes before merging. Merging
   to the production branch (e.g., `main`) promotes the deployment to the production URL.
6. **Monitor**: The Vercel dashboard shows deployment logs, function invocation metrics,
   and web vitals in real time.

## Use Cases

- **Frontend hosting**: Deploying React, Next.js, Vue, Svelte, or static site generator
  projects with zero-configuration, globally distributed delivery.
- **Full-stack web applications**: Pairing Vercel's serverless functions with a backend
  database (e.g., Supabase, PlanetScale, Neon) to build complete applications without
  managing servers.
- **Data dashboards**: Serving analytics dashboards or reporting UIs that fetch data
  from a warehouse or API at request time or on a revalidation schedule.
- **API layer**: Using serverless functions as a lightweight API layer that proxies,
  transforms, or aggregates data from upstream services before delivering it to the
  client.
- **A/B testing and personalisation**: Edge Functions can rewrite, redirect, or
  personalise responses at the edge before a request reaches the origin, with minimal
  latency impact.
- **CI/CD for frontend**: Preview deployments make Vercel a de-facto CI/CD platform for
  frontend teams, replacing manual staging environment management.

## Considerations

- **Vendor lock-in**: Advanced features like ISR, Edge Middleware, and the Vercel data
  primitives are tightly coupled to the Vercel platform. Migrating to another host may
  require rearchitecting these features.
- **Stateless functions**: Serverless and edge functions are stateless and short-lived.
  Long-running jobs, persistent connections (e.g., WebSockets), or heavy computation
  should be handled by a dedicated backend service rather than Vercel functions.
- **Cold starts**: Serverless functions (not Edge Functions) can experience cold start
  latency after periods of inactivity, affecting response times for infrequently called
  endpoints.
- **Execution limits**: Serverless functions have maximum execution time limits (up to
  300 seconds on Pro/Enterprise plans). ETL-style workloads or large data processing
  should be offloaded to a dedicated pipeline tool.
- **Cost at scale**: Vercel's pricing is based on bandwidth, function invocations, and
  build minutes. High-traffic applications or those with many serverless function calls
  can incur significant costs compared to self-hosted alternatives.
- **Not a data platform**: Vercel does not replace dedicated data infrastructure. It is
  a delivery and compute layer; analytical workloads, data storage, and processing belong
  in purpose-built data tools.

## Best Practices

- Use **Edge Functions** for latency-sensitive logic (auth checks, redirects,
  personalisation) and **Serverless Functions** for heavier, Node.js-dependent backend
  work.
- Store secrets in Vercel's environment variable management rather than committing them
  to the repository.
- Use preview deployments as a mandatory step in the review process — reviewers should
  verify the deployed preview, not just the code diff.
- Leverage **Incremental Static Regeneration (ISR)** for pages that display data updated
  on a schedule (e.g., dashboards, reports) to avoid full server-side rendering on every
  request.
- Set appropriate cache headers and use `stale-while-revalidate` strategies to maximise
  CDN hit rates and minimise function invocations.
- Keep serverless functions small and focused. If a function is growing large, consider
  whether it belongs in a dedicated backend service.
- Monitor Core Web Vitals in the Vercel Analytics dashboard and treat regressions as
  deployment blockers.

## Related Documentation

- [Vercel Documentation](https://vercel.com/docs) — Official docs, quickstart, and reference
- [Next.js Documentation](https://nextjs.org/docs) — Framework documentation
- [Vercel Edge Functions](https://vercel.com/docs/functions/edge-functions) — Edge runtime reference
- [Vercel GitHub](https://github.com/vercel/vercel) — Source code and CLI

## Related Topics

- [Supabase](supabase.md)
- [Database as a Service (DBaaS)](../databases/database-as-a-service.md)
- [Real-time Analytics](../analytics/real-time-analytics.md)
- [Caching Strategies](../advanced/caching-strategies.md)
- [ETL](../patterns/etl.md)
- [API-based Ingestion](../ingestion/api-based-ingestion.md)

---

**Category**: Tools & Products  
**Last Updated**: 2026
