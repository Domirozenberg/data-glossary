# Naming Convention

## Overview
Naming conventions are standardized rules for how identifiers — variables, functions,
classes, files, and database objects — are formatted in code and data systems. Consistent
naming conventions improve code readability, reduce cognitive load, and make codebases
easier to navigate and maintain across teams.

## Definition
A naming convention is a set of agreed-upon rules that govern the casing, structure, and
vocabulary of identifiers in a programming language or data system. Different conventions
are suited to different contexts: languages, frameworks, and data layers each have their
own established norms.

## Key Concepts

- **PascalCase** (also called UpperCamelCase): Every word starts with a capital letter,
  with no separators — `CustomerOrder`, `DataPipeline`, `UserProfile`. Commonly used for
  class names, types, and constructors in languages like Java, C#, and Python.
- **camelCase** (lowerCamelCase): First word is lowercase, subsequent words are
  capitalized — `customerOrder`, `dataPipeline`, `userId`. Widely used for variables and
  functions in JavaScript, Java, and Go.
- **snake_case**: Words are lowercase and separated by underscores — `customer_order`,
  `data_pipeline`, `user_id`. The dominant convention in Python (PEP 8) and SQL
  identifiers.
- **SCREAMING_SNAKE_CASE** (UPPER_SNAKE_CASE): All uppercase with underscores —
  `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`. Used for constants and environment variables
  across many languages.
- **kebab-case**: Words are lowercase and separated by hyphens — `customer-order`,
  `data-pipeline`. Common in URLs, HTML attributes, CSS class names, and CLI flags.
- **Hungarian Notation**: Prefixes encode the type or scope of a variable — `strName`,
  `iCount`, `bIsActive`. Once common in Windows/C++ development; largely discouraged
  in modern practice in favour of expressive names and strong typing.

## How It Works

Naming conventions are applied by choosing the appropriate style for the context:

| Context | Recommended Convention | Example |
|---|---|---|
| Python variables & functions | `snake_case` | `get_user_by_id()` |
| Python classes | `PascalCase` | `UserRepository` |
| JavaScript / TypeScript variables | `camelCase` | `fetchUserData` |
| JavaScript / TypeScript classes | `PascalCase` | `DataPipeline` |
| SQL columns & tables | `snake_case` | `order_placed_at` |
| Constants (most languages) | `SCREAMING_SNAKE_CASE` | `MAX_BATCH_SIZE` |
| CSS classes / HTML attributes | `kebab-case` | `data-user-id` |
| File names (scripts, configs) | `kebab-case` or `snake_case` | `load_events.py` |
| REST API endpoints | `kebab-case` | `/api/user-orders` |

Teams codify these rules in a style guide and enforce them through linters:
- **Python**: `flake8`, `pylint`, `ruff` (enforces PEP 8)
- **JavaScript / TypeScript**: ESLint with style rules
- **SQL**: SQLFluff
- **Go**: `gofmt` (enforces conventions automatically)

## Use Cases

- **Team consistency**: Prevents a mix of `getUserId`, `get_user_id`, and `GetUserId` for
  the same concept across the same codebase.
- **Cross-language projects**: Data pipelines often span Python, SQL, and YAML — defining
  which convention applies to each layer avoids confusion.
- **Code reviews**: Naming conventions give reviewers a concrete standard to reference,
  removing subjective debate.
- **Onboarding**: New engineers can infer intent and context from a name without reading
  every implementation detail.
- **Tooling compatibility**: Some systems (e.g., certain databases, cloud services) are
  case-insensitive or reserve certain characters, making a consistent convention
  essential for portability.

## Considerations

- **Language norms take precedence**: Following the idiomatic convention of a language
  (e.g., `snake_case` in Python, `camelCase` in JavaScript) is more important than
  enforcing a single house style across all languages.
- **Abbreviations**: Shortened names (`usr`, `val`, `tmp`) save keystrokes but reduce
  clarity. Prefer full words unless the abbreviation is universally understood in the
  domain (e.g., `id`, `url`, `api`).
- **Acronyms**: Treat acronyms consistently — either always uppercase (`userID`, `parseURL`)
  or capitalise only the first letter (`UserId`, `ParseUrl`). Mixing both causes confusion.
- **Length**: Names should be as short as possible while remaining unambiguous. Avoid
  single-letter names outside of loop indices (`i`, `j`) or well-known mathematical
  contexts.
- **Consistency over perfection**: A consistently applied imperfect convention is better
  than an inconsistently applied perfect one.

## Best Practices

- Follow the idiomatic convention of the language or framework you are working in.
- Enforce conventions with automated linters rather than relying solely on manual review.
- Document your team's choices — especially for edge cases like acronyms and abbreviations
  — in a shared style guide or `CONTRIBUTING.md`.
- Avoid mixing conventions within the same scope — don't name one variable `userId` and
  another `user_name` in the same function.
- Use `SCREAMING_SNAKE_CASE` exclusively for true constants that never change at runtime.
- Avoid Hungarian notation — modern IDEs and type systems make type-encoding prefixes
  redundant and they clutter names.
- When in doubt, favour the longer, more descriptive name — future readers will thank you.

## Related Topics

- [Data Dictionary](data-dictionary.md)
- [Data Stewardship](data-stewardship.md)
- [Metadata Management](metadata-management.md)
- [Version Control](../version-control/index.md)

---

**Category**: Governance  
**Last Updated**: 2026
