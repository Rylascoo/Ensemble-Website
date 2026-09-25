# Kymaean website

Source for **[www.kymaean.com](https://www.kymaean.com)**, the public website of Kymaean.

## Status

The site is a single teaser page: the Kymaean name standing on a dark stage, under the release
line **In Rehearsal**. Nothing about the product is disclosed until the app ships. See
[`docs/LAUNCH.md`](docs/LAUNCH.md) for the launch site that replaces it.

## Where things live

| Place | Owns |
|---|---|
| This repository | Website design, implementation and website-specific history |
| [`Rylascoo/Ensemble-Project`](https://github.com/Rylascoo/Ensemble-Project) | The product: architecture, app design, implementation, tests |
| Google Drive, `Ensemble Project` | Canonical visual and creative masters |

Product facts on the website come from `Ensemble-Project`; they are never re-authored here.

## Layout

```
site/            the Cloudflare Worker (the only thing that deploys)
  public/        static files served as-is
  wrangler.jsonc Worker configuration
brand/           master logo files (SVG) and brand usage notes
docs/            design system, launch plan, decision log
tools/site.mjs   stamps asset hashes and checks the site (no dependencies)
tools/card.html  template for the social sharing image
```

## Working on the site

```sh
node tools/site.mjs stamp   # after changing any file in site/public: refresh ?v= hashes + CSP
node tools/site.mjs check   # verify links, hashes, CSP, size budget, retired terms
cd site && npx wrangler dev # local preview at http://localhost:8787
```

Anything referenced as `/assets/...?v=<hash>` is cached by browsers for a year, so never edit an
asset without running `stamp`. CI runs `check` on every push and pull request.

## Deployment

Cloudflare Workers Builds watches this repository (Worker `kymaean-site`, root directory `site/`).

- A push to **`main`** deploys to production (`www.kymaean.com`).
- A push to **any other branch** uploads a preview version; its URL appears on the pull request.

Work happens on a branch and merges to `main` only after the preview has been reviewed and the
Director has approved the change. The bare domain `kymaean.com` redirects to `www` through a
Cloudflare redirect rule; mail DNS records are not managed here and must not be touched.

## History

Everything before the 2026-09-24 renovation is preserved in Git:

- `archive/pre-renovation-2026-09-24`: the repository exactly as it was (commit `43801c0b`).
- `archive/branch/<name>`: the exact tip of every retired branch, with its status in the tag message.
- `archive/...` (127 older tags): earlier checkpoints, kept unchanged.

All content in this repository is © Kymaean, all rights reserved, except the Josefin Sans font,
which is licensed under the SIL Open Font License (see `site/public/assets/fonts/`).
