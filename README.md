# Brand Genome Template

**Your brand as code: one repo that holds strategy, story, voice, facts, identity and prompts, so every person and every AI agent makes content the same way.**

> A **brand genome** is a brand written as a spec that people and AI tools generate from. This template is the structure Youssef Jalloul uses for every brand he builds: his own (YJ), Ikraa, and the ventures that follow. It's empty, so you can fill it with yours.

Click **Use this template** to start your own.

## Why brand as code

- **AI agents need a source of truth.** Point Claude, ChatGPT or any agent at `AGENTS.md` and `brand.json`, and they write and design on brand.
- **Facts stay true.** Every number lives in one register with a source and a status. Nothing else gets published.
- **Marketing gets reviewed like code.** Briefs are issues, drafts are pull requests, the brand owner approves, and a check runs on every change.
- **Search engines and AI assistants read it.** Structured, consistent facts are what AI search tools quote.

## The structure

```
├── README.md · AGENTS.md · CLAUDE.md · brand.json · llms.txt
├── 00-genome/          lean strategy · blue ocean (ERRC) · positioning · audiences · flaming corner
├── 01-story-universe/  hero · villain · guide · supporting cast · world · story arc
├── 02-voice/           voice and tone · approved messages
├── 03-facts/           facts register (ready · framed · needs-source · conflict)
├── 04-identity/        logo · colour · type · imagery · motion
├── 05-characters/      mascots or a comic cast (optional)
├── 06-design-system/   tokens · coding-agent guide
├── 07-content-kits/    per channel: specs · formats · hooks
├── 08-prompts/         copy · images · characters · voice
├── 09-governance/      approval workflow · decisions log
├── 10-library/         approved campaigns and results
└── scripts/brand_check.py   runs on every pull request
```

## Set up a new brand in 10 minutes

1. **Use this template** → name the repo `brand`, ideally in its own organisation (`<brand>-brand`), private.
2. Fill `brand.json` first: every top-level key is required (the brand check enforces it).
3. Fill `03-facts/facts.md`. Anything without a source stays `needs-source`.
4. Add the owner to `.github/CODEOWNERS` and protect `main`: require a pull request, Code Owner review and the "Brand check" status.
5. Fill the numbered folders in order. Each folder's README says what goes there.

## The frameworks inside

| Framework | Where | Credit |
| --- | --- | --- |
| Lean Strategy and Lean Canvas | `00-genome` | Youssef Jalloul's Lean Strategy; Lean Canvas by Ash Maurya |
| Blue Ocean strategy canvas and Four Actions (ERRC) | `00-genome` | W. Chan Kim and Renée Mauborgne |
| Messaging house and Schwartz's five awareness levels | `00-genome` | Eugene Schwartz |
| Flaming Corner launch playbook | `00-genome` | Youssef Jalloul |
| StoryBrand story arc | `01-story-universe` | Donald Miller |

## The one rule every brand genome carries

Always positive. Villains are problems or models, never people, nationalities, cultures or groups. People are shown confident and curious, never frowning or upset. No invented facts, results or testimonials.

## Licence

MIT. Use it for any brand, commercial or not.

## About the author

**Youssef Jalloul** is an AI entrepreneur and venture builder based in Sydney and Dubai, and the Founder and CEO of Inova AI Solutions. Over 20+ years he has built and exited multiple companies and created or implemented 200+ AI agents and proofs of concept. [youssefjalloul.com](https://youssefjalloul.com) · [LinkedIn](https://www.linkedin.com/in/youssef-jalloul/)
