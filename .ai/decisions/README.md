# Decision records

Create a numbered Markdown record only for a choice that is important,
non-obvious, or costly to reverse.

Suggested name:

```text
0001-short-decision-title.md
```

Include:

- status
- known decision date, or `unknown`
- decision authority: user direction or agent implementation choice
- source or evidence when material
- context
- considered options that were actually considered
- outcome
- rationale
- consequences
- related tasks or commits

The record author is not necessarily the decision authority. Do not infer
either role, and do not invent a date, rationale, rejected option, or approval.
Supersede an accepted decision rather than silently rewriting its rationale.
