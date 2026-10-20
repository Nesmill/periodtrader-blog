# Period Trader blog content

Posts served at https://periodtrader.com/blog. The site reads this repo at runtime
(raw.githubusercontent.com), so a push publishes a post with no site redeploy
(live within ~10 minutes: GitHub raw cache + site edge cache).

- `index.json` — list of published posts (newest first). Only `tools/blog.py publish` edits it.
- `posts/<slug>/meta.json`, `en.md`, `es.md` — one post. Spanish is a full edition in tuteo.
- `tools/blog.py` — `plan` (picks today's category), `check <slug>` (editorial/safety gates),
  `publish <slug>` (index + commit + push + live verification).

Schedule: Monday market news, Wednesday strategy research, Friday product update
(when a new release shipped) or tutorial. Written by the Hermes cron job
"PeriodTrader blog autopost" using the `periodtrader-blog-autopost` skill.

Markdown subset: `##`/`###` headings, paragraphs, lists, `>` quotes, fenced code,
`---`, pipe tables, **bold**, *italic*, `code`, [links](https://...). Raw HTML is
rejected by `check` and shown as text by the site.

To unpublish a post: remove its entry from `index.json` and push.
