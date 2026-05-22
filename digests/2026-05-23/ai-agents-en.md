# OpenClaw Ecosystem Digest 2026-05-23

> Issues: 500 | PRs: 500 | Projects covered: 13 | Generated: 2026-05-22 16:02 UTC

- [OpenClaw](https://github.com/openclaw/openclaw)
- [NanoBot](https://github.com/HKUDS/nanobot)
- [Hermes Agent](https://github.com/nousresearch/hermes-agent)
- [PicoClaw](https://github.com/sipeed/picoclaw)
- [NanoClaw](https://github.com/qwibitai/nanoclaw)
- [NullClaw](https://github.com/nullclaw/nullclaw)
- [IronClaw](https://github.com/nearai/ironclaw)
- [LobsterAI](https://github.com/netease-youdao/LobsterAI)
- [TinyClaw](https://github.com/TinyAGI/tinyagi)
- [Moltis](https://github.com/moltis-org/moltis)
- [CoPaw](https://github.com/agentscope-ai/CoPaw)
- [ZeptoClaw](https://github.com/qhkm/zeptoclaw)
- [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

---

## OpenClaw Deep Dive

# OpenClaw Project Digest — 2026-05-23

## 1. Today's Overview

OpenClaw shows **extremely high activity** with 500 issues and 500 PRs updated in the last 24 hours, indicating a mature project under heavy development with substantial community engagement. The 428:72 open-to-closed issue ratio and 422:78 open-to-merged PR ratio suggest a growing backlog that may strain maintainer capacity. A single release (v2026.5.20) shipped recently with security-hardening changes to skill execution. The top issues reveal deep architectural concerns around session state reliability, multi-channel message delivery, and security boundaries—consistent with a production AI agent platform serving diverse deployment scenarios.

---

## 2. Releases

### [v2026.5.20](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20) — openclaw 2026.5.20

| Change | Impact |
|--------|--------|
| **Exec approvals: removed legacy `cat SKILL.md && printf ... && <skill-wrapper>` allowlist compatibility path** | **BREAKING**: Skill files must now be loaded exclusively via the `read` tool; only the real skill executable receives auto-allow. Any external skill relying on the old shell-pipe pattern will fail execution. |
| **Discord: voice sessions follow configured Discord users into voice channels** | Enhancement for voice integration; enables persistent voice session mobility. |

**Migration Note**: Operators with custom skills using the deprecated `cat SKILL.md` pattern must migrate to the `read` tool pattern before this release. No automated migration path is documented.

---

## 3. Project Progress

### Closed PRs Today (Selected)

| PR | Description | Significance |
|----|-------------|------------|
| [#85391](https://github.com/openclaw/openclaw/pull/85391) | fix(update): detect nested macOS gateway ancestry | Prevents in-band `openclaw update` from stopping its own managing LaunchAgent on macOS |
| [#85036](https://github.com/openclaw/openclaw/pull/85036) | Openclaw original v2026.5.18 (Vietnamese localization) | Large localization PR for Vietnamese Control UI; closed, possibly superseded |
| [#85120](https://github.com/openclaw/openclaw/issues/85120) | [Bug] in-band `openclaw update` on macOS LaunchAgent can stop gateway | Related issue closed with #85391 fix |

### Notable Open PRs Advancing

| PR | Stage | What It Fixes/Adds |
|----|-------|------------------|
| [#85436](https://github.com/openclaw/openclaw/pull/85436) | Needs proof | iMessage catchup cursor deadlock fix — critical for Apple messaging reliability |
| [#85104](https://github.com/openclaw/openclaw/pull/85104) | Ready for maintainer | Auto fast mode cutoff (`fast: auto` with configurable `fast_seconds`) |
| [#84894](https://github.com/openclaw/openclaw/pull/84894) | Needs proof | Codex empty result after exec stdout turns — fixes silent output failures |
| [#84268](https://github.com/openclaw/openclaw/pull/84268) | Waiting on author | Codex chat history reload for message-tool replies — UI state persistence |
| [#85367](https://github.com/openclaw/openclaw/pull/85367) | Waiting on author | **Workboard dashboard plugin** — new Kanban-style persistent task surface |

---

## 4. Community Hot Topics

### Most Discussed Issues (by comment count)

| # | Issue | Comments | Rating | Core Need |
|---|-------|----------|--------|-----------|
| [#48788](https://github.com/openclaw/openclaw/issues/48788) | Centralized filename encoding utility for multi-encoding Content-Disposition | 17 | 🌊 off-meta tidepool | **Cross-cultural reliability**: Chinese (GB18030), Japanese (Shift-JIS), Korean (EUC-KR) filename handling across all channel adapters |
| [#48183](https://github.com/openclaw/openclaw/issues/48183) | Feishu monitor state cleanup incomplete — memory leak in httpServers Map | 17 | 🦞 diamond lobster | **Production stability**: Proper async resource lifecycle management in enterprise messaging |
| [#50090](https://github.com/openclaw/openclaw/issues/50090) | Community Skill Development & ClawHub | 14 | 🌊 off-meta tidepool | **Ecosystem growth**: Driftnet's abandoned skills highlight need for sustainable community governance |
| [#29387](https://github.com/openclaw/openclaw/issues/29387) | Bootstrap files in agentDir silently ignored | 13 | 🦞 diamond lobster | **Config predictability**: Per-agent isolation vs. shared workspace confusion |
| [#53628](https://github.com/openclaw/openclaw/issues/53628) | `${XDG_CONFIG_HOME}` not processed when installing skill | 12 | 🦞 diamond lobster | **Standards compliance**: XDG Base Directory spec adherence for containerized deployments |

**Underlying Pattern**: Enterprise users (Feishu, Docker, multi-user setups) are hitting friction where OpenClaw's assumptions about single-user, standard environments conflict with production deployment patterns.

---

## 5. Bugs & Stability

### P1 (Critical) Issues — Active Today

| Issue | Symptom | Fix PR? | Risk |
|-------|---------|---------|------|
| [#84516](https://github.com/openclaw/openclaw/issues/84516) | Codex app-server: replies truncated at ~1000-1100 chars silently | No | **Silent data loss** — users receive incomplete responses without error indication |
| [#29387](https://github.com/openclaw/openclaw/issues/29387) | agentDir bootstrap files ignored, only workspace loaded | No | Security/session state: agents run with wrong identity context |
| [#51396](https://github.com/openclaw/openclaw/issues/51396) | `clearUnboundScopes` strips operator scopes for token-auth clients | Linked PR open | **Auth regression**: backend integrations broken in 2026.3.13 |
| [#51593](https://github.com/openclaw/openclaw/issues/51593) | HTTP 400 "tool call id exec:26 is duplicated" — moonshot/kimi-k2.5 in WhatsApp groups | No | **Crash in group contexts** — specific model + channel combination |
| [#57019](https://github.com/openclaw/openclaw/issues/57019) | Session write lock race: async release deletes newly-acquired lock | No | **Data corruption** — concurrent session access |
| [#85126](https://github.com/openclaw/openclaw/issues/85126) | Control UI auto-selects wrong `authProfileOverride` (deepseek vs. minimax) | No | **Misrouted API costs/permissions** |

### P2 (High) Regressions

| Issue | First Seen | Status |
|-------|-----------|--------|
| [#43747](https://github.com/openclaw/openclaw/issues/43747) | Memory management chaos — inconsistent embedding storage across users | 2026-03-12 | No fix PR |
| [#48920](https://github.com/openclaw/openclaw/issues/48920) | Live docs ahead of release (`IsolatedSessions` documented but not shipped) | 2026-03-17 | Docs/Release process failure |
| [#51429](https://github.com/openclaw/openclaw/issues/51429) | Hardcoded path `/Users/wangtao` merged to production | 2026-03-21 | **Embarrassing QA gap** — developer artifact in release |

---

## 6. Feature Requests & Roadmap Signals

| Issue | Request | Predicted Priority | Rationale |
|-------|---------|-------------------|-----------|
| [#50090](https://github.com/openclaw/openclaw/issues/50090) | ClawHub skill ecosystem governance | **High** | Critical for platform differentiation vs. closed alternatives; "Driftnet has been abandoned" signals urgency |
| [#50199](https://github.com/openclaw/openclaw/issues/50199) | Skill priority configuration | Medium | Natural complement to #50090; overlapping skills create UX confusion |
| [#52640](https://github.com/openclaw/openclaw/issues/52640) | Persistent task-status surface for long-running channel turns | Medium | Discord-first, then generic; addresses "agent went silent" user anxiety |
| [#48874](https://github.com/openclaw/openclaw/issues/48874) | Multi-Session Architecture: Shared LLM + Isolated Sessions + Public KB | **High** | Resource optimization + tenant isolation; enterprise blocker |
| [#45758](https://github.com/openclaw/openclaw/issues/45758) | YAML config format support | Low | DevOps ergonomics; JSON5 is functional |
| [#85367](https://github.com/openclaw/openclaw/pull/85367) | Workboard dashboard plugin (PR) | **Likely v2026.6.x** | Large PR in progress; Kanban is frequently requested task visualization |

**Next Version Signals**: Auto fast mode (#85104), Workboard plugin (#85367), and iOS Realtime-2 Talk Mode (#85131) appear closest to merge-ready for v2026.6.x.

---

## 7. User Feedback Summary

### Pain Points (Explicit)

| Theme | Evidence | Severity |
|-------|----------|----------|
| **Silent failures** | #84516 (truncation), #49876 (cron hallucinates instead of failing), #50165 (subagents appear done before finished) | 🔴 Critical — erodes trust |
| **Session state fragility** | #47975, #48573, #48003, #57019 — zombie agents, lock races, steer mode broken | 🔴 Critical — core reliability |
| **Multi-channel delivery gaps** | #54531 (replies lost to wrong channel), #53486 (Feishu cards as plain text), #52972 (wrong reminder confirmation) | 🟡 High — UX inconsistency |
| **Enterprise deployment friction** | #53628 (XDG_CONFIG_HOME), #56263 (chmod 0o600 breaks multi-user), #44599 (whitespace in paths) | 🟡 High — blocks adoption |
| **Developer artifact in production** | #51429 (`/Users/wangtao`) | 🟡 Process failure |

### Use Cases Emerging
- **Headless/automated operations**: Cron sessions, CLI tool_use bridging (#80046)
- **Multi-tenant/containerized**: Permission configs, XDG compliance, proxy exemptions
- **Real-time voice**: iOS Realtime-2, Discord voice session following
- **Regulated environments**: Security reviews on gh-issues skill (#45740), auth scope hardening

---

## 8. Backlog Watch

### Issues Needing Maintainer Decision (stuck >60 days, high impact)

| Issue | Age | Blocker | Why It Matters |
|-------|-----|---------|---------------|
| [#29387](https://github.com/openclaw/openclaw/issues/29387) | ~85 days | Product decision + security review | Fundamental config architecture: per-agent vs. shared workspace |
| [#50090](https://github.com/openclaw/openclaw/issues/50090) | ~65 days | Product decision + security review | Platform ecosystem viability |
| [#45740](https://github.com/openclaw/openclaw/issues/45740) | ~70 days | Security review | Prompt injection vulnerability in gh-issues skill |
| [#45608](https://github.com/openclaw/openclaw/issues/45608) | ~70 days | Product decision | Memory flush consistency — data loss prevention |
| [#59413](https://github.com/openclaw/openclaw/issues/59413) | ~51 days | Product decision | Model fallback for proxy/pool providers — cost optimization |

### PRs Waiting on Author (risk of staleness)

| PR | Age | Risk |
|----|-----|------|
| [#82918](https://github.com/openclaw/openclaw/pull/82918) | ~6 days | curl\|bash stdin guard — security fix languishing |
| [#84268](https://github.com/openclaw/openclaw/pull/84268) | ~3 days | Codex chat history — user-visible data loss |
| [#85131](https://github.com/openclaw/openclaw/pull/85131) | ~1 day | iOS Realtime-2 — large PR, needs review bandwidth |

---

**Project Health Assessment**: ⚠️ **Strained but functional**. High velocity (1000 items/day) with strong community contribution, but maintainer bandwidth appears insufficient for the decision backlog. Critical stability issues (session state, silent truncation) need urgent attention before feature expansion. The v2026.5.20 security change shows proactive hardening, yet process gaps (hardcoded paths, docs ahead of releases) indicate QA/review pressure.

---

## Cross-Ecosystem Comparison

# Cross-Project Comparison Report: Personal AI Agent Open-Source Ecosystem
*Date: 2026-05-23 | Based on 10 active projects*

---

## 1. Ecosystem Overview

The personal AI assistant / agent open-source ecosystem is experiencing **unprecedented velocity** with over 1,200 GitHub items updated across tracked projects in 24 hours, yet showing **severe maintainer bandwidth constraints** everywhere. The field has bifurcated between **mature production platforms** (OpenClaw, ZeroClaw, IronClaw) wrestling with enterprise reliability and **emerging specialized tools** (NanoBot, PicoClaw, Moltis) carving out focused use cases. A critical inflection point is visible: projects are pivoting from "single-user chatbot" architectures toward **multi-tenant, multi-interface agent orchestration platforms** with TUI, voice, and subagent capabilities, while struggling with foundational issues like session state durability and silent data loss that threaten production adoption.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Release Status | Merge/Close Rate | Health Assessment |
|:---|:---:|:---:|:---|:---|
| **OpenClaw** | 500 | 500 | v2026.5.20 (security hardening) | 14% issues closed, 16% PRs merged | ⚠️ **Strained** — 1000 items/day, decision backlog growing |
| **NanoBot** | 7 | 17 | None | 71% merge/close rate | ✅ **Healthy** — responsive maintainers, focused scope |
| **Hermes Agent** | 50 | 50 | v0.14.0 (2026-05-21) | 10% PRs merged, 12% issues closed | ⚠️ **Concerning** — 4 P1 bugs unaddressed, review bottleneck |
| **PicoClaw** | 6 | 22 | v0.2.8-nightly | 41% PRs merged | 🟡 **Stable** — active maintenance, stale-issue cleanup masking unresolved bugs |
| **NanoClaw** | 6 new | 18 | None | 44% PRs merged | 🔴 **Fragile** — Apple Container cascade failure, no release despite major merges |
| **NullClaw** | 0 | 3 updated | None | 0% today | 🟡 **Dormant** — 3 PRs stalled 2-7 weeks, zero community engagement |
| **IronClaw** | 26 | 50 | None | 42% PRs merged | 🟡 **Pre-release churn** — Reborn migration, disciplined but unstable |
| **LobsterAI** | 1 active | 21 | **v2026.5.22** (today) | 57% PRs merged | ✅ **Shipping** — strong velocity, security backlog risk |
| **Moltis** | 4 | 7 | None (20260518.01 current) | 57% PRs merged | ✅ **Responsive** — same-day critical fixes, small focused team |
| **CoPaw (QwenPaw)** | 23 | 20 | None (v1.1.8.post1) | 45% PRs merged | ⚠️ **Triage pressure** — critical data loss bug unresolved |
| **ZeroClaw** | 18 | 23 | None | 9% PRs merged | 🟡 **Architectural expansion** — TUI pivot, 95% PR backlog |
| **TinyClaw** | — | — | — | — | ❌ **Inactive** — no activity |
| **ZeptoClaw** | — | — | — | — | ❌ **Inactive** — no activity |

---

## 3. OpenClaw's Position

### Advantages vs. Peers

| Dimension | OpenClaw | Peer Comparison |
|:---|:---|:---|
| **Scale** | 1000 items/day — 20-50× higher absolute volume than any peer | ZeroClaw (41 items) is closest; NanoBot (24) and Moltis (11) are order of magnitude smaller |
| **Channel diversity** | 15+ channel adapters (Discord, Feishu, iMessage, Telegram, WhatsApp, etc.) | Hermes (11-language i18n, Matrix, Tlon), ZeroClaw (WhatsApp, Slack, Telegram, Lark), NanoClaw (Signal, Telegram) — OpenClaw maintains breadth lead |
| **Enterprise penetration** | Feishu, multi-tenant architecture, XDG compliance debates | IronClaw targets enterprise via NEAR ecosystem; CoPaw has WeChat/DingTalk China focus |
| **Security hardening** | v2026.5.20 exec approval breaking change — proactive | LobsterAI has security PRs stalled 6 weeks; Moltis just added vault encryption disable |

### Technical Approach Differences

| Aspect | OpenClaw | Alternatives |
|:---|:---|:---|
| **Architecture** | Monolithic with plugin skills; heavy session state management | IronClaw: Rust-based "Reborn" microkernel with TurnCoordinator; ZeroClaw: TUI+web dual interface; PicoClaw: request-scoped context policies per turn |
| **State model** | Persistent workspace + agentDir with known fragility (#29387, #57019) | NanoBot: WebSocket-gateway-as-service; Hermes: cloud sync requested; LobsterAI: SQLite subagent persistence with lazy backfill |
| **Skill ecosystem** | ClawHub centralized (drifting — #50090) | NanoBot: CLI Apps ecosystem emerging; Hermes: 81 official skills currently broken (#30482); NanoClaw: Composio MCP integration |
| **Deployment target** | Desktop + server hybrid, macOS LaunchAgent, Docker | Moltis: Docker-native telephony; NullClaw: POSIX/threaded runtime; IronClaw: cloud-hosted with local bridge gap (#2117) |

### Community Size Reality

OpenClaw's **absolute contributor volume is unmatched**, but **engagement quality is strained**: 428:72 open-to-closed issue ratio indicates ~86% of issues remain unresolved vs. NanoBot's healthier flow. The project has **graduated from "benevolent dictator" to "infrastructure at scale"** without proportional maintainer growth — a pattern also seen in Hermes (90% open PR rate) and ZeroClaw (95%).

---

## 4. Shared Technical Focus Areas

| Requirement | Projects | Specific Evidence | Urgency |
|:---|:---|:---|:---:|
| **Session state reliability / durability** | OpenClaw, NanoClaw, LobsterAI, CoPaw, PicoClaw | OpenClaw #57019 (lock race), #29387 (bootstrap ignored); NanoClaw #2586 (transcript rotation); LobsterAI #2036 (no real-time persistence events); CoPaw #4620 (history loss); PicoClaw #2795 (compression over-aggressive) | 🔴 Critical |
| **Multi-channel message delivery** | OpenClaw, Hermes, ZeroClaw, CoPaw, NanoClaw | OpenClaw #54531 (wrong channel), #53486 (Feishu cards plain text); Hermes #30411 (Telegram routing); ZeroClaw #6847 (WhatsApp QR), #6844 (Slack token); CoPaw #4521 (WeChat false success); NanoClaw #2585 (Telegram grammy) | 🔴 Critical |
| **Docker/containerized deployment polish** | OpenClaw, Hermes, Moltis, PicoClaw | OpenClaw #53628 (XDG_CONFIG_HOME), #56263 (chmod multi-user); Hermes #18482 (HOME permissions), #16703 (DooD); Moltis #1035/#1040 (sandbox mounts); PicoClaw #2812 (root Dockerfile) | 🟡 High |
| **Provider abstraction / rapid model support** | NanoBot, Hermes, CoPaw, IronClaw, ZeroClaw | NanoBot #3940 (Ollama image gen), #3954 (OpenAI/Codex); Hermes #26847 (xAI tier), #30449 (DeepSeek reasoning); CoPaw #4474 (GPT-5.5), #4625 (MiniMax XML); IronClaw Google Extensions; ZeroClaw #6549 (Claude Code vision) | 🟡 High |
| **Subagent / multi-agent orchestration** | LobsterAI, IronClaw, ZeroClaw, OpenClaw | LobsterAI v2026.5.22 (subagent sidebar + persistence); IronClaw #3875 (blocking spawn bug); ZeroClaw #5890 (multi-agent UX RFC); OpenClaw #50165 (subagents appear done before finished) | 🟡 High |
| **Real-time voice / multimodal** | OpenClaw, Moltis, NanoClaw, NanoBot | OpenClaw Discord voice session following; Moltis #1034 (Twilio speech), #1041 (MP3 voice); NanoClaw #2532 (Veo 3.1 video); NanoBot #3946 (Ollama image gen) | 🟢 Emerging |
| **TUI / alternative interfaces** | Hermes, ZeroClaw, OpenClaw | Hermes v0.14.0 TUI paste bugs (#24860, #30083); ZeroClaw 6 TUI issues (#6821-6827); OpenClaw Control UI auto-select bugs | 🟢 Emerging |

---

## 5. Differentiation Analysis

| Project | Core Differentiator | Target User | Architecture Signature | Risk Profile |
|:---|:---|:---|:---|:---|
| **OpenClaw** | Universal channel adapter + skill ecosystem | Power users, small teams, multi-platform operators | Node/TS monolith, workspace-centric | Maintainer bandwidth; session state debt |
| **NanoBot** | Lean, fast, local-first (Ollama) | Individual developers, privacy-conscious | Python, gateway-as-service, WebUI | WebSocket reliability; scaling beyond personal |
| **Hermes Agent** | Urbit/Tlon integration, plugin hooks | Decentralization advocates, self-hosters | Python, diverse adapters, Kanban dashboard | Skills ecosystem broken; review bottleneck |
| **PicoClaw** | Per-turn context control, embedded/edge friendly | Cost-optimizers, multi-agent scenarios | Go, request-scoped policies, message bus | Stale issue masking; multi-agent immaturity |
| **NanoClaw** | Apple Container native, Signal focus, marketing skills | macOS users, SMB automation | Node/bun, microVM containers, MCP integrations | Apple Container cascade failure; branch decay |
| **IronClaw** | NEAR blockchain integration, Rust performance, "Reborn" enterprise architecture | Web3/NEAR ecosystem, enterprise | Rust, TurnCoordinator kernel, tenant isolation | Pre-release instability; cloud-local file gap |
| **LobsterAI** | Subagent persistence + cowork engine, China-market polish | Teams, enterprise, deep research workflows | Electron/Tauri, SQLite, OpenClaw gateway dependency | Security PR staleness; gateway event coupling |
| **Moltis** | Telephony-first (Twilio), Docker-native sandbox | Voice agents, containerized deployments | Rust, sandbox isolation, vault encryption | Small community; narrow use case |
| **CoPaw (QwenPaw)** | China ecosystem integration (WeChat, DingTalk, Qwen), desktop pet | Chinese market, casual desktop users | Python, Tauri migration, plugin marketplace | Data loss critical bug; model compatibility lag |
| **ZeroClaw** | Multi-interface (web + TUI + headless), ACP protocol | Power users, developers, server operators | Rust, Unix socket RPC, MemoryStrategy trait | Configuration fragility; Windows inequality |

---

## 6. Community Momentum & Maturity

### Tier 1: Rapid Iteration (Shipping Velocity)

| Project | Signal | Risk |
|:---|:---|:---|
| **LobsterAI** | 10 PRs → release in 24h; subagent feature hardened | Security backlog (#1534, #1535) |
| **NanoBot** | 71% merge rate; image gen 0→3 providers in 48h | Gateway-as-service reliability |
| **Moltis** | Same-day critical fixes; zero stale items | Scale limitations |

### Tier 2: Heavy Development / Pre-Stabilization

| Project | Signal | Risk |
|:---|:---|:---|
| **IronClaw** | 76 items/day, Reborn migration, WebUI v2 beta | 12-day E2E failure unresolved; not production-ready |
| **ZeroClaw** | 41 items/day, TUI pivot, multi-agent RFC | 95% PR open rate; 3 S1 channel bugs |
| **CoPaw** | 43 items/day, active contributor onboarding | Critical data loss (#4620) eroding trust |

### Tier 3: Mature but Strained

| Project | Signal | Risk |
|:---|:---|:---|
| **OpenClaw** | 1000 items/day, security hardening releases | Decision backlog, silent failures, session state |
| **Hermes** | v0.14.0 shipped, 11-language i18n, diverse adapters | 4 P1 bugs unaddressed; skills ecosystem broken |

### Tier 4: Stabilization / Maintenance Mode

| Project | Signal | Risk |
|:---|:---|:---|
| **PicoClaw** | Nightly builds, stale-issue cleanup | Unresolved bugs masked by closures; multi-agent architecture needs design |
| **NanoClaw** | Major merges without release; Apple Container decay | macOS user exodus; process gaps |

### Tier 5: Stalled / Dormant

| Project | Signal | Risk |
|:---|:---|:---|
| **NullClaw** | 3 PRs stalled 2-7 weeks, zero issues | Project may be abandoned or insular |
| **TinyClaw, ZeptoClaw** | No activity | Effectively inactive |

---

## 7. Trend Signals

| Trend | Evidence | Value for AI Agent Developers |
|:---|:---|:---|
| **From chatbot to agent orchestration platform** | Subagent features in LobsterAI, IronClaw, ZeroClaw; multi-agent UX RFC #5890; OpenClaw subagent pain points | Design for **hierarchical agent graphs** with persistence and observability at every level, not single-turn interactions |
| **Multi-interface as table stakes** | TUI surge (ZeroClaw 6 issues, Hermes TUI, OpenClaw Control UI); voice (Moltis Twilio, OpenClaw Discord); desktop native (CoPaw Tauri, LobsterAI Electron) | Plan **interface-agnostic core** with RPC/ACP bridges; web-only is insufficient for power users |
| **Local-first and provider diversification** | NanoBot Ollama image gen; NanoClaw Codex + Claude Code dual support; IronClaw NEAR AI Cloud; Moltis NEAR AI | **Abstract provider interface early**; users demand model agility (GPT-5.5, MiniMax XML, DeepSeek thinking formats all breaking assumptions) |
| **Enterprise deployment friction as adoption blocker** | Docker path issues across 4+ projects; XDG compliance; multi-user permissions; proxy configuration (NO_PROXY); env var vs. config file tension | **Treat containerization and 12-factor compliance as first-class**, not afterthought; single-user desktop assumptions fail at scale |
| **Silent failures eroding trust** | OpenClaw truncation (#84516), cron hallucination (#49876); CoPaw history loss (#4620); ZeroClaw vision routing (#6841); Hermes config migration (#17182) | **Build observable failure modes** — every silent fallback, every "appears done before finished" is a trust catastrophe; event streaming (#2036) is infrastructure, not feature |
| **Skill/plugin ecosystem governance crisis** | OpenClaw ClawHub drift (#50090, "Driftnet abandoned"); Hermes 81 skills broken (#30482); NanoBot CLI Apps emerging; CoPaw MCP marketplace | **Centralized marketplaces decay without curation investment**; consider federated or MCP-standard approaches over bespoke ecosystems |
| **Real-time persistence as reliability foundation** | LobsterAI #2036 (agent:turn events); OpenClaw session lock races; PicoClaw per-message timestamps | **Event-sourced agent state** with crash recovery is becoming baseline expectation, not advanced feature |

---

*Report compiled from 13 project digests covering 2026-05-22/23 GitHub activity. Health assessments reflect maintainer capacity, bug severity, and delivery velocity, not code quality in isolation.*

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot Project Digest — 2026-05-23

## 1. Today's Overview

NanoBot showed **strong development velocity** with 17 PRs and 7 issues updated in the last 24 hours, yielding a **71% merge/close rate** (12 closed, 5 open). No new releases were published. Activity concentrated heavily on **WebUI polish** (locale completeness, sidebar UX, performance), **provider ecosystem expansion** (Ollama image generation, OpenAI/Codex image generation, Manifest router), and **critical API compatibility fixes** for Anthropic and Moonshot. The project demonstrates healthy maintainer responsiveness with same-day turnaround on multiple PRs, though a growing backlog of open feature PRs suggests capacity constraints for larger architectural contributions.

---

## 2. Releases

**None** — No new releases published today.

---

## 3. Project Progress

### Merged/Closed PRs (12 items)

| PR | Author | Summary | Impact |
|:---|:---|:---|:---|
| [#3964](https://github.com/HKUDS/nanobot/pull/3964) | yu-xin-c | Filled WebUI locale keys for `es`, `fr`, `id`, `ko`, `vi` | Internationalization completeness |
| [#3928](https://github.com/HKUDS/nanobot/pull/3928) | Hinotoi-agent | **Security fix**: Validated redirect targets in `web_fetch` to close SSRF vulnerability | Critical security hardening |
| [#3962](https://github.com/HKUDS/nanobot/pull/3962) | yu-xin-c | Filled `zh-TW` and `ja` WebUI locale keys | East Asian i18n coverage |
| [#3961](https://github.com/HKUDS/nanobot/pull/3961) | Yuxin-Lou | Deduplicated Responses API replay item IDs for Codex compatibility | Prevents conversation resume failures |
| [#3929](https://github.com/HKUDS/nanobot/pull/3929) | HaisamAbbas | Unified image provider HTTP handling + Gemini base URL documentation | Code health, maintainability |
| [#3946](https://github.com/HKUDS/nanobot/pull/3946) | HaisamAbbas | **Native Ollama image generation support** | Major local AI capability expansion |
| [#3954](https://github.com/HKUDS/nanobot/pull/3954) | ZegWe | **OpenAI and Codex image generation provider support** | Enterprise/proprietary provider coverage |
| [#3960](https://github.com/HKUDS/nanobot/pull/3960) | chengyongru | Removed deprecated `patch` mode from `apply_patch`, kept `edits`-only | Tooling simplification, reduced maintenance burden |
| [#3957](https://github.com/HKUDS/nanobot/pull/3957) | Re-bin | Fixed misleading file edit counters in WebUI | UX accuracy |
| [#3940](https://github.com/HKUDS/nanobot/pull/3940) | agbocsardi | Dropped redundant `reasoning_effort` for Kimi thinking models | Moonshot API compatibility |
| [#3953](https://github.com/HKUDS/nanobot/pull/3953) | Re-bin | Improved sidebar performance with batched rendering | Scalability for long chat histories |
| [#3951](https://github.com/HKUDS/nanobot/pull/3951) | Re-bin | Refined collapsible sidebar with persistent rail | Desktop UX polish |

**Key advancement**: Image generation went from **0 to 3 providers** in 48 hours (Ollama, OpenAI, Codex), indicating a strategic push toward visual capabilities.

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|:---|:---|:---|
| [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI conversation closes after first response | **6 comments**, closed | Most discussed issue. Reveals **WebSocket reliability problems** in gateway-as-service deployments. Root cause likely in connection lifecycle management. Fix merged but pattern suggests broader WebUI state management fragility. |
| [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill list` shows disabled skills | **4 comments**, open | Configuration system not respecting `disabledSkills` array. Indicates **skill registry filtering gap** between config parsing and runtime enumeration. |
| [#3028](https://github.com/HKUDS/nanobot/issues/3028) Heartbeat creates duplicate scheduled tasks | **3 comments**, open | **Architectural bug** in cron/heartbeat system: heartbeat triggers create nested timers instead of using context-aware scheduling. Affects v0.15; user reports duplicate greetings. Suggests scheduler needs redesign for idempotency. |

**Underlying needs**: Users want **predictable, stateful agent behavior** (conversations that persist, skills that respect config, heartbeats that don't spam). The project is gaining production users with expectations of reliability.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR |
|:---|:---|:---|:---|
| 🔴 **Critical** | [#3928](https://github.com/HKUDS/nanobot/pull/3928) SSRF via unvalidated redirects in `web_fetch` | **Fixed** | #3928 (merged) |
| 🔴 **Critical** | [#3956](https://github.com/HKUDS/nanobot/issues/3956) Anthropic API 400 error on tool results with list content (image reads) | **Fixed** | Implied in #3961 or related |
| 🟡 **High** | [#3939](https://github.com/HKUDS/nanobot/issues/3939) Moonshot rejects Kimi models with conflicting `thinking` + `reasoning_effort` | **Fixed** | [#3940](https://github.com/HKUDS/nanobot/pull/3940) (merged) |
| 🟡 **High** | [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI conversation closes after first response | **Fixed** | Closed, fix in unspecified PR |
| 🟢 **Medium** | [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill list` ignores `disabledSkills` | **Open** | None yet |
| 🟢 **Medium** | [#3028](https://github.com/HKUDS/nanobot/issues/3028) Heartbeat duplicate task creation | **Open** | None yet; needs scheduler refactor |

**Stability assessment**: Two critical security/API compatibility issues resolved within 24 hours. Two medium bugs remain open with clear reproduction steps but no assigned fix PRs.

---

## 6. Feature Requests & Roadmap Signals

| Request | Issue/PR | Likelihood in Next Release | Rationale |
|:---|:---|:---|:---|
| **Ollama image generation** | [#3941](https://github.com/HKUDS/nanobot/issues/3941) → [#3946](https://github.com/HKUDS/nanobot/pull/3946) | ✅ **Shipped** | Merged same day as request |
| **OpenAI/Codex image generation** | [#3954](https://github.com/HKUDS/nanobot/pull/3954) | ✅ **Shipped** | Proactive provider expansion |
| **Weather skill → example** (modularization) | [#3958](https://github.com/HKUDS/nanobot/issues/3958) | 🔶 **High** | Aligns with "lean and mean" project philosophy; trivial implementation |
| **CLI Apps ecosystem** (`nanobot` as app platform) | [#3963](https://github.com/HKUDS/nanobot/pull/3963) | 🔶 **High** | Large PR open, MVP architecture complete |
| **`nanobot doctor` diagnostics** | [#3776](https://github.com/HKUDS/nanobot/pull/3776) | 🔶 **Moderate-High** | 10-check health command; mature but unmerged for 8 days |
| **BM25-lite skill router** (~60% prompt reduction) | [#3865](https://github.com/HKUDS/nanobot/pull/3865) | 🔶 **Moderate** | Performance win, but architectural review needed |
| **Manifest LLM router** | [#3568](https://github.com/HKUDS/nanobot/pull/3568) | 🔶 **Moderate** | Open since April 30; gateway provider pattern |
| **MECE long-term memory** (deduplication, consolidation) | [#3952](https://github.com/HKUDS/nanobot/pull/3952) | 🔶 **Moderate** | Complex memory system refactor; addresses real bloat |

**Predicted next release focus**: Image generation stabilization, CLI Apps MVP, and memory system improvements.

---

## 7. User Feedback Summary

### Pain Points
| Theme | Evidence | Severity |
|:---|:---|:---|
| **WebUI reliability** | [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebSocket drops; gateway-as-service instability | High |
| **Configuration not respected** | [#3959](https://github.com/HKUDS/nanobot/issues/3959) disabled skills still appear; config schema gaps | Medium |
| **API provider fragility** | [#3939](https://github.com/HKUDS/nanobot/issues/3939), [#3956](https://github.com/HKUDS/nanobot/issues/3956) Vendor-specific parameter conflicts | Medium |
| **Scheduler/task duplication** | [#3028](https://github.com/HKUDS/nanobot/issues/3028) Heartbeat spam; poor cron hygiene | Medium |

### Positive Signals
- **Local-first AI**: Strong demand for Ollama integration (#3941) satisfied rapidly
- **Visual capabilities**: Image generation expansion shows project responsiveness to multimodal trends
- **Internationalization**: Active locale maintenance (5 languages in 2 days) indicates global user base

### Use Case Evolution
Users are moving from **personal assistant** to **production agent platform** (gateway-as-service, CLI Apps ecosystem, diagnostic tools). This shifts quality expectations from "works on my machine" to "enterprise reliable."

---

## 8. Backlog Watch

| Item | Age | Risk | Needs |
|:---|:---|:---|:---|
| [#3568](https://github.com/HKUDS/nanobot/pull/3568) Manifest LLM router | 23 days | Stale provider PR | Maintainer review; rebase likely needed |
| [#3865](https://github.com/HKUDS/nanobot/pull/3865) BM25-lite skill router | 7 days | Architectural uncertainty | Performance benchmarking; system prompt compatibility review |
| [#3776](https://github.com/HKUDS/nanobot/pull/3776) `nanobot doctor` | 9 days | Near-ready, unmerged | Final UX review; merge conflict check |
| [#3952](https://github.com/HKUDS/nanobot/pull/3952) MECE memory enhancement | 2 days | Complex, high-impact | Careful review of prompt changes; migration path for existing `MEMORY.md` |

**Maintainer attention recommended**: The 23-day-old Manifest PR risks bit-rot. The `nanobot doctor` and BM25 PRs are user-visible improvements with clear value propositions that should be prioritized for merge or explicit rejection to maintain contributor momentum.

---

*Digest generated from HKUDS/nanobot GitHub activity for 2026-05-22/23. All links: https://github.com/HKUDS/nanobot*

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent Project Digest — 2026-05-23

## 1. Today's Overview

Hermes Agent shows **high community velocity** with 50 issues and 50 PRs active in the last 24 hours, though the **merge/close rate remains low** (5 PRs merged/closed, 6 issues closed), suggesting a bottleneck in maintainer review capacity. The project is in a **stabilization phase** for v0.14.0 with no new releases, focusing on bug fixes for recently shipped features including TUI, Kanban dashboard, and provider integrations. Critical P1 bugs in skills installation, config migration, and Telegram gateway indicate **release-quality concerns** that are actively being patched. The contributor base is diverse with 11-language i18n work and multiple new platform adapters in flight, signaling healthy ecosystem growth despite review backlog.

---

## 2. Releases

**No new releases** — v0.14.0 remains the current version (released 2026-05-21 per commit `ba9964ff0`). The absence of a hotfix release despite multiple P1 bugs suggests maintainers may be batching fixes or awaiting validation.

---

## 3. Project Progress

### Merged/Closed PRs Today (5 total)

| PR | Author | Summary | Significance |
|:---|:---|:---|:---|
| [#30495](https://github.com/NousResearch/hermes-agent/pull/30495) | [ilonagaja509-glitch](https://github.com/ilonagaja509-glitch) | Emoji scanner fix: allow ZWJ in grapheme clusters | Fixes broken emoji rendering; regression from over-aggressive unicode filtering |
| [#30496](https://github.com/NousResearch/hermes-agent/pull/30496) | [ilonagaja509-glitch](https://github.com/ilonagaja509-glitch) | Gateway progress deduplication on pre-truncation key | Eliminates false dedup for distinct commands with shared long prefixes |
| [#30325](https://github.com/NousResearch/hermes-agent/pull/30325) | [andrew54068](https://github.com/andrew54068) | Clear Docusaurus broken-link warnings after locale fix | Unblocks docs site CI; infrastructure quality |

### Notable Open PRs Advancing

| PR | Author | Feature | Status |
|:---|:---|:---|:---|
| [#30504](https://github.com/NousResearch/hermes-agent/pull/30504) | [ilonagaja509-glitch](https://github.com/ilonagaja509-glitch) | Bundle `anthropic`, `bedrock`, `azure-identity` extras in Docker image | Addresses [#30394](https://github.com/NousResearch/hermes-agent/issues/30394) — critical for air-gapped deployments |
| [#27648](https://github.com/NousResearch/hermes-agent/pull/27648) | [EduardoSolanas](https://github.com/EduardoSolanas) | Fallback provider management UI in dashboard | Major UX improvement for model reliability |
| [#26300](https://github.com/NousResearch/hermes-agent/pull/26300) | [wca4a](https://github.com/wca4a) | Expand Tlon adapter (OpenClaw-style group/channel reads) | Deepens Urbit ecosystem integration |
| [#30111](https://github.com/NousResearch/hermes-agent/pull/30111) | [ambient-gregory](https://github.com/ambient-gregory) | Add Ambient as verified inference provider | Cryptographic proof-of-execution — unique positioning |
| [#30492](https://github.com/NousResearch/hermes-agent/pull/30492) | [Syz87](https://github.com/Syz87) | 11-language i18n complete (zh, ja, ko, de, fr, es, pt, ru, ar, hi, it) | Massive internationalization effort across 17 files |
| [#30493](https://github.com/NousResearch/hermes-agent/pull/30493) | [kshitijk4poor](https://github.com/kshitijk4poor) | `register_transcription_provider()` plugin hook | Completes STT plugin parity with TTS |
| [#4043](https://github.com/NousResearch/hermes-agent/pull/4043) | [sprmn24](https://github.com/sprmn24) | ntfy platform adapter (self-hosted push notifications) | Pairs with community feature request [#13866](https://github.com/NousResearch/hermes-agent/issues/13866) |

---

## 4. Community Hot Topics

### Most Active Issues by Engagement

| Issue | Comments | 👍 | Core Tension |
|:---|:---|:---|:---|
| [#26847](https://github.com/NousResearch/hermes-agent/issues/26847) — xAI OAuth 403 for standard SuperGrok subscribers | 15 | 1 | **Provider-tier enforcement mismatch**: xAI backend blocks $30/month users despite docs claiming all tiers work; business model vs. documentation accuracy |
| [#2706](https://github.com/NousResearch/hermes-agent/issues/2706) — Response truncated due to output length limit | 11 | 0 | **Closed** — Fundamental streaming architecture: rollback-on-truncation vs. progressive delivery |
| [#29125](https://github.com/NousResearch/hermes-agent/issues/29125) — Hermes does not work through Claude CLI | 9 | 3 | **Provider abstraction leakage**: Anthropic's native CLI conflicts with Hermes's token management; users expect seamless "Claude as a backend" |
| [#18482](https://github.com/NousResearch/hermes-agent/issues/18482) — Cannot create home directory: Permission denied | 6 | 0 | **Docker UX friction**: Custom HOME paths fail silently; documentation gap for containerized deployments |
| [#28844](https://github.com/NousResearch/hermes-agent/issues/28844) — Kanban schema migration ordering bug | 5 | 0 | **Database reliability**: Index created before column exists = permanent initialization failure; migration system needs transaction safety |

### Underlying Needs Analysis

- **Provider reliability expectations**: Users treat Hermes as a universal router but hit tier/compat issues (xAI, Claude CLI, Kimi, DeepSeek) — suggests need for provider health checks and graceful degradation
- **Self-hosting operational maturity**: Docker, Matrix, and config migration bugs cluster around "deploy and forget" use cases
- **TUI/dashboard polish**: Multiple paste/scrolling/visual bugs indicate v0.14.0's new interface needs stabilization sprint

---

## 5. Bugs & Stability

### P1 (Critical — Data Loss or Core Function Broken)

| Issue | Description | Fix PR? |
|:---|:---|:---|
| [#30482](https://github.com/NousResearch/hermes-agent/issues/30482) | **Skills installation completely broken**: All 81 official skills have empty `repo` field in index | **None** — needs immediate hotfix |
| [#27988](https://github.com/NousResearch/hermes-agent/issues/27988) | Codex adapter maps `final_answer` to `finish_reason=incomplete` on Azure Foundry | **None** |
| [#30411](https://github.com/NousResearch/hermes-agent/issues/30411) | Telegram DM auto-topic-rename and tool-call routing broken | **None** |
| [#17182](https://github.com/NousResearch/hermes-agent/issues/17182) | Config migration resets `terminal.cwd` and clears all `auxiliary.*.model` fields | **None** |

### P2 (High — Major Feature Impaired)

| Issue | Description | Fix PR? |
|:---|:---|:---|
| [#16703](https://github.com/NousResearch/hermes-agent/issues/16703) | Docker-out-of-Docker code execution fails (`docker version` check) | **None** |
| [#4587](https://github.com/NousResearch/hermes-agent/issues/4587) | Multi-profile gateway kills other profiles' processes (profile-blind operations) | **None** |
| [#7069](https://github.com/NousResearch/hermes-agent/issues/7069) | Infinite retry loop on local LLM prefill timeout | **None** |
| [#24860](https://github.com/NousResearch/hermes-agent/issues/24860) | Dashboard Chat: Ctrl+V paste broken, image paste unsupported | **None** |
| [#30083](https://github.com/NousResearch/hermes-agent/issues/30083) | Ask tool prompt in new TUI rejects pasted text | **None** |
| [#30417](https://github.com/NousResearch/hermes-agent/issues/30417) | Dispatcher: deterministic spawn-crash loop, SQLite I/O latches, orphaned child promotion | **None** |
| [#26886](https://github.com/NousResearch/hermes-agent/issues/26886) | `hermes mcp add` corrupts empty args `[]` to `[""]` | **None** |
| [#30218](https://github.com/NousResearch/hermes-agent/issues/30218) | OSC 11 color response leaks into CLI input over SSH | **None** |
| [#30399](https://github.com/NousResearch/hermes-agent/issues/30399) | Matrix gateway unusable from Docker (missing `mautrix[encryption]`) | **None** |
| [#30449](https://github.com/NousResearch/hermes-agent/issues/30449) | DeepSeek `reasoning_content`/`reasoning_effort` never reach OpenAI-compatible SSE | **None** |

### P3 (Medium — Workaround Exists)

| Issue | Description | Fix PR? |
|:---|:---|:---|
| [#26847](https://github.com/NousResearch/hermes-agent/issues/26847) | xAI OAuth tier enforcement (SuperGrok vs. Heavy) | **None** |
| [#29125](https://github.com/NousResearch/hermes-agent/issues/29125) | Claude CLI integration failure | **None** |
| [#28844](https://github.com/NousResearch/hermes-agent/issues/28844) | Kanban DB corruption from migration ordering | **None** |

**Stability Assessment**: ⚠️ **Concerning** — 4 P1 bugs with no linked PRs, 10 P2 bugs unaddressed. The skills installation breakage (#30482) is particularly severe as it blocks all new skill adoption.

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Request | Likelihood in Next Version | Rationale |
|:---|:---|:---|:---|
| [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) | Cloud sync for all configs across devices | Medium | High 👍 (6), but requires infrastructure; may pair with existing auth work |
| [#13866](https://github.com/NousResearch/hermes-agent/issues/13866) / [#4043](https://github.com/NousResearch/hermes-agent/pull/4043) | ntfy native messaging provider | **High** | PR already open, matches self-hosting trend |
| [#30437](https://github.com/NousResearch/hermes-agent/issues/30437) | Kanban assignee dropdown from profiles | Medium | Small UI change, fits current Kanban focus |
| [#30428](https://github.com/NousResearch/hermes-agent/issues/30428) | "Gene Network Self-Evolution System" (璇玑×Hermès fusion) | Low | Highly speculative, no implementation path |
| [#30480](https://github.com/NousResearch/hermes-agent/issues/30480) | TLS fingerprint spoofing for third-party API proxies | Medium | China-market need, but may conflict with security principles |
| [#30493](https://github.com/NousResearch/hermes-agent/pull/30493) | `register_transcription_provider()` plugin hook | **High** | PR open, completes existing plugin architecture |

**Emerging Themes**: Self-hosted/edge deployment (ntfy, Docker hardening, TLS fingerprinting), plugin ecosystem maturation (STT/TTS/provider hooks), and operational reliability (cloud sync, multi-profile safety).

---

## 7. User Feedback Summary

### Pain Points (Explicit)

| Theme | Evidence | Severity |
|:---|:---|:---|
| **Configuration fragility** | [#17182](https://github.com/NousResearch/hermes-agent/issues/17182) migration resets, [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) no sync, [#4587](https://github.com/NousResearch/hermes-agent/issues/4587) multi-profile unsafe | 🔴 High |
| **Provider integration gaps** | [#26847](https://github.com/NousResearch/hermes-agent/issues/26847) xAI, [#29125](https://github.com/NousResearch/hermes-agent/issues/29125) Claude CLI, [#30449](https://github.com/NousResearch/hermes-agent/issues/30449) DeepSeek reasoning, [#30494](https://github.com/NousResearch/hermes-agent/issues/30494) Kimi temperature | 🔴 High |
| **Docker deployment friction** | [#18482](https://github.com/NousResearch/hermes-agent/issues/18482) permissions, [#16703](https://github.com/NousResearch/hermes-agent/issues/16703) DooD, [#30399](https://github.com/NousResearch/hermes-agent/issues/30399) Matrix missing deps, [#30504](https://github.com/NousResearch/hermes-agent/pull/30504) lazy-install fails air-gapped | 🟡 Medium-High |
| **TUI/dashboard polish** | [#24860](https://github.com/NousResearch/hermes-agent/issues/24860) paste broken, [#30083](https://github.com/NousResearch/hermes-agent/issues/30083) Ask paste, [#30218](https://github.com/NousResearch/hermes-agent/issues/30218) OSC leak, [#30503](https://github.com/NousResearch/hermes-agent/issues/30503) truncated header | 🟡 Medium |
| **Skills ecosystem broken** | [#30482](https://github.com/NousResearch/hermes-agent/issues/30482) all official skills uninstallable | 🔴 Critical |

### Satisfaction Signals

- Strong engagement with experimental features (Tlon adapter, Ambient provider, 11-language i18n)
- Active self-hosting community (ntfy, Matrix, Docker optimizations)
- Plugin architecture adoption (image gen, TTS, STT hooks)

---

## 8. Backlog Watch

### Long-Unanswered Critical Items Needing Maintainer Attention

| Issue/PR | Age | Problem | Action Needed |
|:---|:---|:---|:---|
| [#7069](https://github.com/NousResearch/hermes-agent/issues/7069) | ~6 weeks | Infinite retry loop on local LLM prefill — breaks local/self-hosted core use case | Assign to streaming/reliability owner; timeout architecture review |
| [#4587](https://github.com/NousResearch/hermes-agent/issues/4587) | ~7 weeks | Multi-profile gateway safety — **data integrity risk** as users scale deployments | Design review for profile-scoped process management |
| [#16703](https://github.com/NousResearch/hermes-agent/issues/16703) | ~4 weeks | Docker-out-of-Docker code execution — **security-sensitive** container escape pattern | Security review; document supported topologies |
| [#12845](https://github.com/NousResearch/hermes-agent/issues/12845) | ~5 weeks | Signal document attachments silently dropped | Assign to messaging platform owner |
| [#13866](https://github.com/NousResearch/hermes-agent/issues/13866) | ~4 weeks | ntfy provider request — **PR [#4043](https://github.com/NousResearch/hermes-agent/pull/4043) ready since March** | Merge or provide review feedback |

### Review Bottleneck Indicators

- 45/50 PRs remain open (90% open rate)
- Multiple PRs by [ilonagaja509-glitch](https://github.com/ilonagaja509-glitch) (5 today alone) suggest dedicated contributor but potential maintainer bandwidth constraints
- [EduardoSolanas](https://github.com/EduardoSolanas)'s fallback management PR ([#27648](https://github.com/NousResearch/hermes-agent/pull/27648)) open since May 17 without merge despite clear user value

---

*Digest generated from GitHub activity 2026-05-22 to 2026-05-23. All links: https://github.com/NousResearch/hermes-agent*

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-05-23

## 1. Today's Overview

PicoClaw shows **moderate-to-high development velocity** with 22 PRs and 6 issues updated in the last 24 hours, though the majority of issue activity was **closure of stale items** rather than new bug reports. The project released a new nightly build (`v0.2.8-nightly.20260522.5bbebb5f`), indicating active iteration toward a patch release. Dependency maintenance dominates open PRs (9 from Dependabot), while core development focuses on message bus reliability, session timestamp accuracy, and Telegram channel robustness. The 13:9 open-to-closed PR ratio suggests a healthy but slightly backlogged review queue. Notably, all 6 issues updated today were **closed**, suggesting an active stale-issue cleanup effort.

---

## 2. Releases

| Version | Type | Notes |
|---------|------|-------|
| [`v0.2.8-nightly.20260522.5bbebb5f`](https://github.com/sipeed/picoclaw/compare/v0.2.8...main) | Nightly Build | Automated build from `main`; **unstable, use with caution**. Compares against `v0.2.8` baseline. |

**No stable release today.** The nightly suggests ongoing work toward `v0.2.9` or beyond, with accumulated changes since `v0.2.8` including session timestamps, request-scoped context policies, and message bus improvements.

---

## 3. Project Progress

### Merged/Closed PRs (9 items)

| PR | Author | Summary | Significance |
|----|--------|---------|------------|
| [#2921](https://github.com/sipeed/picoclaw/pull/2921) | dependabot[bot] | Bump `gronx` 1.19.7 → 1.20.0 | Cron scheduling library update |
| [#2923](https://github.com/sipeed/picoclaw/pull/2923) | dependabot[bot] | Bump `line-bot-sdk-go` 8.19.0 → 8.20.0 | LINE channel support |
| [#2914](https://github.com/sipeed/picoclaw/pull/2914) | lxowalle | **feat: add request-scoped context policies** | Major: `turn_profile` controls history, system context, skills, tools per turn |
| [#2812](https://github.com/sipeed/picoclaw/pull/2812) | moltenbot000 | Root Dockerfile for development | DevEx improvement (AI-augmented contribution) |
| [#2779](https://github.com/sipeed/picoclaw/pull/2779) | bogdanovich | Telegram topic group trigger overrides | Channel-specific behavior control |
| [#2778](https://github.com/sipeed/picoclaw/pull/2778) | bogdanovich | `working_summary` tool feedback style | UX: compact progress indicators in chat |
| [#2777](https://github.com/sipeed/picoclaw/pull/2777) | bogdanovich | Suppress feedback for scheduled cron turns | Stability: prevents ghost messages from background jobs |
| [#2776](https://github.com/sipeed/picoclaw/pull/2776) | bogdanovich | Stop typing for topic replies | Telegram polish |
| [#2772](https://github.com/sipeed/picoclaw/pull/2772) | bogdanovich | Preserve Telegram forum topic for `message` tool | Bug fix for multi-topic routing |

**Key advancement:** Request-scoped context policies ([#2914](https://github.com/sipeed/picoclaw/pull/2914)) enable fine-grained control over agent context per turn—critical for cost optimization and multi-agent scenarios.

---

## 4. Community Hot Topics

### Most Active Issues (by comment count)

| Issue | Comments | Status | Core Concern |
|-------|----------|--------|--------------|
| [#629](https://github.com/sipeed/picoclaw/issues/629) | **15** | ✅ CLOSED | LLM call retry logic failure under HTTP 500 errors |
| [#2775](https://github.com/sipeed/picoclaw/issues/2775) | 4 | ✅ CLOSED | Multi-agent identity confusion: child agents inherit root `AGENT.md` |
| [#2702](https://github.com/sipeed/picoclaw/issues/2702) | 4 | ✅ CLOSED | Multi-user channels lack sender attribution in history |

### Underlying Needs Analysis

- **Resilience engineering** (#629): Long-running tasks need robust retry with exponential backoff—currently ad-hoc
- **Multi-agent architecture maturity** (#2775): The `AGENT.md` inheritance model breaks role separation; users need **per-agent persona isolation**
- **Multi-tenancy in group channels** (#2702): Discord/Telegram group use cases require sender-aware session management, not flat chat history

> **Signal:** These closures without linked fix PRs suggest they were **stale-cleaned**, not resolved. Risk of recurrence.

---

## 5. Bugs & Stability

| Severity | Issue/PR | Description | Fix Status |
|----------|----------|-------------|------------|
| 🔴 **High** | [#629](https://github.com/sipeed/picoclaw/issues/629) | LLM calls fail without retry, tasks hang | CLOSED stale; **no confirmed fix** |
| 🟡 **Medium** | [#2798](https://github.com/sipeed/picoclaw/issues/2798) | PDF stream corruption in Telegram bot | CLOSED stale; **reproducible**, OpenClaw works fine |
| 🟡 **Medium** | [#2702](https://github.com/sipeed/picoclaw/issues/2702) | Conversation history lacks sender labels in groups | CLOSED stale; PR [#2788](https://github.com/sipeed/picoclaw/pull/2788) addresses timestamps partially |
| 🟡 **Medium** | [#2795](https://github.com/sipeed/picoclaw/issues/2795) | Only last user message visible in history (session compression over-aggressive) | CLOSED stale; **no fix PR** |
| 🟢 **Low** | [#2787](https://github.com/sipeed/picoclaw/issues/2787) | Missing per-message timestamps | **PR [#2788](https://github.com/sipeed/picoclaw/pull/2788) OPEN** — fix in progress |

### Infrastructure Concerns

- **Message bus backpressure** ([#2906](https://github.com/sipeed/picoclaw/pull/2906), OPEN): Goroutine accumulation under load could cause memory leaks or deadlock
- **PDF handling fragility** (#2798): Suggests stream parsing differences vs. upstream OpenClaw

---

## 6. Feature Requests & Roadmap Signals

| Feature | Source | Likelihood in Next Version |
|---------|--------|---------------------------|
| **Per-message timestamps in sessions** | PR [#2788](https://github.com/sipeed/picoclaw/pull/2788) | 🔥 **High** — actively developed |
| **Media attachments in `message` tool** | PR [#2856](https://github.com/sipeed/picoclaw/pull/2856) | 🔥 **High** — rich delivery for Telegram |
| **Frontmatter tool policy filters (`allow`/`deny`)** | PR [#2838](https://github.com/sipeed/picoclaw/pull/2838) | 🟡 Medium — security/ops feature |
| **Message bus backpressure + health visibility** | PR [#2906](https://github.com/sipeed/picoclaw/pull/2906) | 🟡 Medium — reliability hardening |
| **Unified providers documentation** | PR [#2662](https://github.com/sipeed/picoclaw/pull/2662) | 🟢 Lower — docs debt |
| **Request-scoped context policies** | PR [#2914](https://github.com/sipeed/picoclaw/pull/2914) | ✅ **Shipped** in nightly |

**Predicted `v0.2.9` focus:** Session UX improvements, Telegram channel parity, and runtime stability (backpressure).

---

## 7. User Feedback Summary

### Pain Points

| Theme | Evidence | Severity |
|-------|----------|----------|
| **Task hangs on LLM failures** | #629 (15 comments, v0.1.2 still affected) | Critical for production use |
| **Broken multi-agent identity** | #2775 — child agents "think they're the root" | Architecture-level |
| **History visibility degraded by compression** | #2795 — users see truncated history | UX regression |
| **Telegram-specific fragility** | #2798 (PDFs), #2776, #2772, #2779 | Channel maintenance burden |
| **Missing temporal fidelity** | #2787 — all messages show same timestamp | UI accuracy |

### Use Case Signals

- **Discord/Teams multi-user deployments** need sender-aware sessions (#2702)
- **Scheduled/automated workflows** need silent operation (#2777 — cron feedback suppression)
- **Document-heavy workflows** (PDF analysis) breaking in Telegram specifically

> **Satisfaction note:** Rapid closure of stale issues may improve backlog hygiene but risks **perception of dismissiveness** for legitimate bugs without fixes.

---

## 8. Backlog Watch

### PRs Needing Maintainer Attention (>10 days open, high value)

| PR | Age | Blocker | Action Needed |
|----|-----|---------|---------------|
| [#2662](https://github.com/sipeed/picoclaw/pull/2662) | ~1 month | Docs restructure, low conflict risk | Review/merge for contributor retention |
| [#2838](https://github.com/sipeed/picoclaw/pull/2838) | ~2 weeks | Security-relevant (tool policy filtering) | Security review, merge for `v0.2.9` |
| [#2856](https://github.com/sipeed/picoclaw/pull/2856) | ~2 weeks | Feature-complete, needs review | Media delivery is user-requested |
| [#2788](https://github.com/sipeed/picoclaw/pull/2788) | ~2 weeks | Addresses #2787 | Straightforward schema addition |

### Issues Reopened Risk

| Issue | Risk | Recommendation |
|-------|------|----------------|
| #629 | **High** — no fix verified, production hang | Reopen or link to retry implementation PR |
| #2798 | **Medium** — reproducible PDF bug, competitor works | Reopen with `needs-investigation` label |
| #2795 | **Medium** — clear regression in session UX | Verify if compression logic changed in `v0.2.8` |

---

**Project Health Score: 🟡 B+** — Strong development velocity, active maintenance, but stale-issue closure strategy may mask unresolved reliability issues. Dependency automation is excellent; core architecture (multi-agent, session model) needs deliberate design attention.

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw Project Digest — 2026-05-23

## 1. Today's Overview

NanoClaw shows **elevated but concentrated activity** with 18 PRs updated in the last 24 hours (8 merged/closed, 10 open) and 6 new issues, all from a single contributor cluster around Signal authentication and Apple Container stability. Notably, **no new releases** were cut despite significant bug accumulation in the Apple Container skill path. The project appears to be in a **stabilization phase** with heavy focus on platform-specific reliability (macOS/Signal) and provider diversification (Codex, Telegram), though the burst of issues from `snymanpaul` suggests the Apple Container feature is currently **broken in production** for new users.

---

## 2. Releases

**None** — No new releases published.

---

## 3. Project Progress

### Merged/Closed PRs (8 items)

| PR | Author | Summary | Significance |
|:---|:---|:---|:---|
| [#1781](https://github.com/nanocoai/nanoclaw/pull/1781) | shakhruz | Composio MCP for managed Gmail/Calendar OAuth | **Infrastructure** — Reduces OAuth friction for Google integrations; fallback preserves backward compatibility |
| [#1780](https://github.com/nanocoai/nanoclaw/pull/1780) | shakhruz | 5 marketing container skills (client-profile, design-avatar, telegram-ads, olx-research, olx-ad-generator) | **Ecosystem expansion** — Vertical-specific skill bundles for marketing workflows |
| [#1757](https://github.com/nanocoai/nanoclaw/pull/1757) | shakhruz | `send_file` MCP tool for file delivery to chat | **UX** — Enables rich media responses from container agents |
| [#1756](https://github.com/nanocoai/nanoclaw/pull/1756) | shakhruz | Include message ID in XML format for agent context | **Bug fix** — Fixes `react_to_message` MCP tool broken reference |
| [#1749](https://github.com/nanocoai/nanoclaw/pull/1749) | shakhruz | Check all agent-runner source files for cache staleness | **Reliability** — Eliminates silent stale-code bugs in container launches |
| [#1747](https://github.com/nanocoai/nanoclaw/pull/1747) | shakhruz | Todoist MCP integration | **Productivity integration** |
| [#1737](https://github.com/nanocoai/nanoclaw/pull/1737) | shakhruz | Google Calendar MCP integration | **Productivity integration** |
| [#1735](https://github.com/nanocoai/nanoclaw/pull/1735) | shakhruz | Apple Container credential proxy, env loading, launchd PATH fixes | **Platform fix** — End-to-end Apple Container repair (now regressed per new issues) |

**Key advancement:** The closed PR cluster from `shakhruz` (dated April 10–15, merged May 22) represents a **major integration push** — Composio OAuth, 5 marketing skills, and core messaging fixes all landed simultaneously, suggesting a coordinated release effort that was **not accompanied by a version tag**.

---

## 4. Community Hot Topics

### Most Active Discussions

| Item | Activity | Analysis |
|:---|:---|:---|
| [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) — Apple Container branch out of sync | 0 comments, 0 👍 | **Critical structural issue** — The `skill/apple-container` branch is fundamentally incompatible with mainline (Node→bun migration, stale APIs). This is a **process failure**: feature branches aren't being rebased or CI-tested against main. |
| [#2585](https://github.com/nanocoai/nanoclaw/pull/2585) — Telegram channel support via grammy | 0 comments, 0 👍 | **High-interest feature** — New channel addition (text/media/commands/typing indicators). Fills a major gap in messaging platform coverage. |
| [#2532](https://github.com/nanocoai/nanoclaw/pull/2532) — Edna Veo 3.1 video generation | Updated May 18→21 | **Multimedia AI push** — Google's Veo 3.1 video generation + Slack delivery. Signals ambition beyond text-based agents. |

**Underlying needs:** 
- **Platform parity**: Users want macOS-native container deployment (Apple Container) but it's decaying
- **Channel diversity**: Telegram, WhatsApp, Signal all being actively worked, suggesting user demand for omnichannel presence
- **Media richness**: Video generation (Veo 3.1) and file sending indicate shift toward multimodal agents

---

## 5. Bugs & Stability

| Severity | Issue | Fix PR? | Details |
|:---|:---|:---|:---|
| 🔴 **Critical** | [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) — Apple Container branch completely broken | No | `/convert-to-apple-container` skill fails immediately. Branch references non-existent APIs, wrong runtime. **Blocks all macOS container users.** |
| 🔴 **Critical** | [#2589](https://github.com/nanocoai/nanoclaw/issues/2589) — `host.docker.internal` unresolvable in Apple Container | No | Networking broken for OneCLI proxy in microVMs. No `--add-host` workaround available. |
| 🟡 **High** | [#2583](https://github.com/nanocoai/nanoclaw/issues/2583) — `restartService` silently no-ops | No | `launchctl kickstart -k` fails when plist unloaded. Service appears restarted but isn't. **Operational hazard.** |
| 🟡 **High** | [#2582](https://github.com/nanocoai/nanoclaw/issues/2582) — `signal-auth listAccounts` deadlock | No | `spawnSync` with no timeout blocks forever when signal-cli daemon holds lock. Setup wizard hangs. |
| 🟡 **High** | [#2581](https://github.com/nanocoai/nanoclaw/issues/2581) — signal-cli 0.13+ JSON field mismatch | **[#2584](https://github.com/nanocoai/nanoclaw/pull/2584)** | `account` → `number` field rename causes false "no linked account" detection. **Fix PR open and ready.** |
| 🟢 **Medium** | [#2587](https://github.com/nanocoai/nanoclaw/issues/2587) — Stale `npm run build` in Apple Container Dockerfile | No | Agent-runner migrated to bun, Dockerfile still references npm. Build fails. |

**Stability assessment:** The Signal+Apple Container subsystem is experiencing **cascading failure**. Six issues from one contributor (`snymanpaul`) in 48 hours suggests either:
1. A new user hitting every broken path on macOS, or
2. A recent mainline change that broke the feature branch

The April fix ([#1735](https://github.com/nanocoai/nanoclaw/pull/1735)) was insufficient or regressed.

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Release |
|:---|:---|:---|
| **Codex as first-class provider** | [#2580](https://github.com/nanocoai/nanoclaw/pull/2580), [#2474](https://github.com/nanocoai/nanoclaw/pull/2474), [#2361](https://github.com/nanocoai/nanoclaw/pull/2361), [#2337](https://github.com/nanocoai/nanoclaw/pull/2337) | **High** — 4 open PRs forming complete Codex integration: setup picker, credentials, provider contracts, skill catalog parity |
| **Telegram channel** | [#2585](https://github.com/nanocoai/nanoclaw/pull/2585) | **High** — PR open with tests, clean implementation |
| **Video generation (Veo 3.1)** | [#2532](https://github.com/nanocoai/nanoclaw/pull/2532) | **Medium** — Large PR, multimedia infrastructure |
| **AI-coding CLI abstraction** | [#2474](https://github.com/nanocoai/nanoclaw/pull/2474) | **Medium** — Registry framework for Claude Code/Codex/Aider/Gemini CLI |
| **Transcript rotation** | [#2586](https://github.com/nanocoai/nanoclaw/pull/2586) | **Medium** — Performance fix for long-lived sessions |

**Prediction:** Next release will likely be **provider-agnostic** (Codex + Claude Code dual support) with Telegram channel, if Apple Container blockers are resolved.

---

## 7. User Feedback Summary

### Pain Points (from issue analysis)

| Pain Point | Evidence | Severity |
|:---|:---|:---|
| **macOS setup completely broken** | 4 Apple Container issues, all critical path | 🔴 Blocking |
| **Signal authentication fragile** | 3 issues: deadlock, JSON compatibility, restart failure | 🟡 High friction |
| **Stale documentation/branch maintenance** | [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) — branch "substantially out of sync" | 🟡 Trust erosion |
| **Silent failures** | [#2583](https://github.com/nanocoai/nanoclaw/issues/2583) restart no-ops without error | 🟡 Operational risk |
| **Long session transcript bloat** | [#2586](https://github.com/nanocoai/nanoclaw/pull/2586) — "days of history plus base64 image blocks" | 🟢 Performance |

### Satisfaction Indicators
- Active skill ecosystem growth (5 marketing skills, Todoist, Calendar, Composio)
- Rapid bug identification (same contributor filing detailed issues)
- Strong test coverage in new PRs (Telegram grammy implementation)

### Dissatisfaction Indicators
- **No release despite major merges** — users may be running from main with known bugs
- Feature branch decay suggests **resource constraints** or **process gaps** in maintenance

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed |
|:---|:---|:---|:---|
| [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) — Apple Container branch out of sync | 1 day | 🔴 **Urgent** — Blocks macOS users | Maintainer decision: archive branch, merge to main, or fast-follow fix |
| [#2584](https://github.com/nanocoai/nanoclaw/pull/2584) — signal-cli 0.13 field fix | 1 day, open | 🟡 Ready to merge | Trivial fix, should be merged immediately |
| [#2523](https://github.com/nanocoai/nanoclaw/pull/2523) — chat-sdk-bridge transformOutboundText | 6 days, open | 🟡 Follows guidelines, unmerged | Review queue backlog |
| [#2361](https://github.com/nanocoai/nanoclaw/pull/2361) — Codex provider contracts | 14 days, open | 🟡 Part of Codex epic | Needs coordination with [#2580](https://github.com/nanocoai/nanoclaw/pull/2580), [#2474](https://github.com/nanocoai/nanoclaw/pull/2474) |
| [#2337](https://github.com/nanocoai/nanoclaw/pull/2337) — Skill catalog for non-Claude providers | 16 days, open | 🟡 Blocked on provider abstraction | Depends on [#2474](https://github.com/nanocoai/nanoclaw/pull/2474) architecture |

**Maintainer attention needed:** The Apple Container subsystem requires **immediate triage** — either a hotfix release or deprecation warning. The Signal authentication stack needs a compatibility test matrix for signal-cli versions. The 4-PR Codex epic needs a merge coordination strategy to avoid partial states.

---

*Digest generated from GitHub activity data. All links reference `github.com/nanocoai/nanoclaw`.*

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw Project Digest — 2026-05-23

## 1. Today's Overview

NullClaw shows **minimal day-of activity** with zero issues updated and no releases published on 2026-05-23. However, **three open pull requests received recent updates** (two touched on 2026-05-22, one on 2026-05-21), indicating **sustained but slow-burn development** rather than daily velocity. The project appears to be in a **stabilization phase** with a focus on reliability fixes (transport error handling, thread scheduling) and infrastructure expansion (cron subsystem). No active open issues suggests either effective issue triage or potentially **low community engagement** on the bug-reporting side. Overall project health reads as **moderate—technically active but not shipping frequently**.

---

## 2. Releases

**No new releases.** The project has no published releases in the tracked period.

---

## 3. Project Progress

**No PRs merged or closed today.** All three recently-updated PRs remain open:

| PR | Status | Last Activity | Focus |
|---|---|---|---|
| [#891](https://github.com/nullclaw/nullclaw/pull/891) | Open, updated 2026-05-22 | Transport-layer error fidelity in OpenAI-compatible provider health probes |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) | Open, updated 2026-05-22 | POSIX thread sleep using `nanosleep` instead of cooperative yield |
| [#783](https://github.com/nullclaw/nullclaw/pull/783) | Open, updated 2026-05-21 | Cron subagent engine with run history, JSON output, security hardening |

**Technical momentum exists but delivery is stalled**—all three PRs have been open for 1–7 weeks without merge. The `nanosleep` and curl probe fixes appear **merge-ready** (narrow scope, single-author, well-specified), while the cron feature PR likely requires **extended review** due to surface area.

---

## 4. Community Hot Topics

**No community hot topics detected.** Zero issues, zero comments, zero reactions across all tracked items.

| Metric | Value |
|---|---|
| Total comments on open PRs | 0 (undefined in data) |
| Total 👍 reactions | 0 |
| Active discussions | None |

**Underlying need assessment:** The absence of engagement suggests either (a) **low adoption** of NullClaw as a user-facing project, (b) **insular development** with discussions happening outside GitHub, or (c) **early-stage maturity** where users haven't yet accumulated operational friction to report. The cron PR (#783) by `yanggf8` is the only **community-contributed** item (non-`vernonstinebaker`), indicating limited external contributor pool.

---

## 5. Bugs & Stability

**No new bugs reported today.** However, **two open PRs address known stability issues**:

| Severity | PR | Issue | Fix Status |
|---|---|---|---|
| **High** | [#891](https://github.com/nullclaw/nullclaw/pull/891) | Health probes collapsing curl transport failures into generic errors, masking DNS/timeout/TLS/read/write failures | **Fix proposed, unmerged** |
| **Medium-High** | [#878](https://github.com/nullclaw/nullclaw/pull/878) | `std_compat.thread.sleep()` using cooperative yield instead of actual OS thread suspension under POSIX, causing CPU burn and scheduling unpredictability in NullClaw's managed runtime | **Fix proposed, unmerged** |

**Risk:** Both fixes are **unmerged after 3+ weeks** (#878) and **1+ weeks** (#891). The thread sleep bug is particularly concerning for production deployments—cooperative yielding under `std.Io.Threaded` implies **busy-waiting behavior** that wastes CPU and breaks latency expectations.

---

## 6. Feature Requests & Roadmap Signals

**Primary feature in flight:** [PR #783](https://github.com/nullclaw/nullclaw/pull/783) — Cron subagent engine

| Component | Signal for Roadmap |
|---|---|
| DB-backed scheduler with `cron_runs` history | Production operability |
| `cron_run_queue` worker with atomic state machine | Reliability at scale |
| Skill/agent/shell job types | Multi-modal execution |
| Per-job timezone offsets | Enterprise/global use case |
| JSON CLI output (`--json` flags) | Automation/CI integration |
| Security hardening | Compliance readiness |

**Prediction:** If merged, cron functionality positions NullClaw as a **job orchestration layer** for AI agents, not just a runtime. The JSON output pattern suggests **API-first/CLI-automation** philosophy. Next version likely to include this if review bandwidth allows.

**No explicit user feature requests** were captured in issues.

---

## 7. User Feedback Summary

**No direct user feedback available** (zero issues, zero discussions, zero comments).

**Inferred pain points from PR analysis:**

| Inferred Pain Point | Evidence | Severity |
|---|---|---|
| **Observability gaps in provider health checks** | #891 explicitly preserves curl error taxonomy | Operators can't diagnose why AI providers fail |
| **Resource efficiency in managed runtime** | #882 switches to `nanosleep` for actual suspension | CPU waste, battery drain, cloud cost inflation |
| **Need for scheduled agent execution** | #783's extensive cron subsystem | Users want "set and forget" agent workflows |
| **Automation-unfriendly CLI output** | #783 adds `--json` throughout | Current output requires text parsing |

**Satisfaction/dissatisfaction:** Unable to assess directly. The **absence of issues** could indicate satisfaction or disengagement.

---

## 8. Backlog Watch

| PR/Issue | Age | Risk | Action Needed |
|---|---|---|---|
| [#783](https://github.com/nullclaw/nullclaw/pull/783) Cron subagent | ~7 weeks open | **Bit rot**, merge conflicts, contributor fatigue | Maintainer review; possibly split into smaller PRs |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) nanosleep fix | ~3 weeks open | **Production impact**, low risk to merge | Merge or request changes |
| [#891](https://github.com/nullclaw/nullclaw/pull/891) curl probe errors | ~2 weeks open | **Diagnostic blindness** for operators | Merge or request changes |

**Critical observation:** All three PRs are **single-author updates with zero reviewer engagement** (no comments). This suggests **maintainer bandwidth constraint** or **unclear ownership** of review duties. The project would benefit from:
- Explicit CODEOWNERS for provider/compat/cron subsystems
- Stale bot or review SLA to prevent PR decay
- Issue templates to capture user feedback that currently isn't surfacing

---

*Digest generated from github.com/nullclaw/nullclaw data as of 2026-05-23.*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw Project Digest — 2026-05-23

## 1. Today's Overview

IronClaw shows **extremely high development velocity** with 76 total items updated in 24 hours (26 issues, 50 PRs), indicating an active push toward the major "Reborn" architectural migration. The project is in a **heavy integration phase**: 21 PRs were merged/closed while 29 remain open, with substantial parallel workstreams on subagent spawning, Google Extensions (OAuth + Calendar + Gmail), WebUI v2, and product auth lifecycle. No new releases were cut, consistent with pre-stabilization work on a large platform overhaul. The volume of draft PRs and phased implementation plans suggests disciplined engineering but also indicates the codebase is not yet production-stable for Reborn features.

---

## 2. Releases

**No new releases** (0).

---

## 3. Project Progress

### Merged/Closed PRs Today (21 total; key items highlighted)

| PR | Author | Summary | Significance |
|:---|:---|:---|:---|
| [#3861](https://github.com/nearai/ironclaw/pull/3861) | serrrfirat | Reborn skill activation selector | Enables explicit `/skill` command context selection for Reborn extensions |
| [#3761](https://github.com/nearai/ironclaw/pull/3761) | serrrfirat | Event stream manager slice | Transport-neutral product streaming with redaction, replay, and multi-tenancy isolation |

### Closed Issues Today (7 total; key items)

| Issue | Author | Resolution |
|:---|:---|:---|
| [#3013](https://github.com/nearai/ironclaw/issues/3013) | serrrfirat | **TurnCoordinator kernel service** — host-layer turn admission and one-active-run enforcement for Reborn cutover |
| [#3623](https://github.com/nearai/ironclaw/issues/3623) | serrrfirat | `BeforeInboundPolicy` seam for WebUI beta message policy checking |
| [#3611](https://github.com/nearai/ironclaw/issues/3611) | serrrfirat | Minimal native WebChat v2 routes (create thread, send message, get timeline) |
| [#3626](https://github.com/nearai/ironclaw/issues/3626) | serrrfirat | WebUI caller/thread scope binding to canonical `TurnScope` |
| [#3625](https://github.com/nearai/ironclaw/issues/3625) | serrrfirat | WebUI idempotency and accepted-message ledger |
| [#3610](https://github.com/nearai/ironclaw/issues/3610) | serrrfirat | Preserved typed filesystem errors in `ProcessError` |
| [#3039](https://github.com/nearai/ironclaw/issues/3039) | serrrfirat | Final integration PR reviewer checklist (tracking item, not blocking) |

**Key advancement**: The WebUI Beta critical path (issues #3607 and children) is nearly complete — idempotency, turn scope binding, native routes, and policy seams are all closed. This unblocks WebChat v2 beta readiness.

---

## 4. Community Hot Topics

### Most Active by Engagement

| Rank | Item | Comments | Analysis |
|:---|:---|:---:|:---|
| 1 | [#3013](https://github.com/nearai/ironclaw/issues/3013) TurnCoordinator (CLOSED) | 8 | **Core architecture decision** — Host-layer turn coordination was the #1 Reborn cutover blocker; resolution required deep consensus on thread/turn admission semantics |
| 2 | [#3031](https://github.com/nearai/ironclaw/issues/3031) Reborn product surface migration EPIC | 7 | **Meta-tracking issue** for preserving legacy behavior during Reborn migration; high comment count reflects cross-cutting coordination needs across modules M1-M4 |
| 3 | [#3702](https://github.com/nearai/ironclaw/issues/3702) Binary-E2E test framework plan | 4 | **Quality infrastructure** — 88 Rust test files need Reborn parity; community concern about test coverage gaps in critical path |
| 4 | [#3623](https://github.com/nearai/ironclaw/issues/3623) BeforeInboundPolicy (CLOSED) | 3 | WebUI beta security seam — comments reflect careful scoping to avoid pulling in non-beta features from parent issue #3280 |

### Underlying Needs

- **Architectural clarity on Reborn boundaries**: Repeated "splits from #3280" and "separate from #3094" patterns show maintainers aggressively scoping issues to prevent scope creep
- **Test confidence**: #3702's existence and activity signal that E2E coverage is a perceived risk before Reborn can ship
- **WebUI v2 as user-visible milestone**: Multiple closed issues converge on a demonstrable beta surface, suggesting near-term user validation is prioritized

---

## 5. Bugs & Stability

| Severity | Item | Status | Details | Fix PR? |
|:---|:---|:---|:---|:---:|
| 🔴 **High** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E failed | OPEN | `v2-engine` E2E suite failing since 2026-05-10; recurring, not flaky | **No** — needs investigation |
| 🟡 **Medium** | [#3875](https://github.com/nearai/ironclaw/issues/3875) Blocking spawn parent recovery gap | OPEN | Subagent `builtin.spawn_subagent` with `mode=blocking` leaves parent hung after child completion; real integration gap found during draft PR #3872 | In progress via [#3872](https://github.com/nearai/ironclaw/pull/3872) |
| 🟡 **Medium** | [#3871](https://github.com/nearai/ironclaw/issues/3871) `executor.rs` decomposition | OPEN | File exceeds architecture size guidelines; subagent additions worsened | No — tracking only, non-blocking |

**Assessment**: The nightly E2E failure is the most concerning stability signal — 12 days without resolution suggests either resource constraints or the failure is entangled with Reborn migration churn. The subagent blocking spawn issue is actively being worked and was caught in draft phase, indicating review processes are functional.

---

## 6. Feature Requests & Roadmap Signals

### In-Flight Major Features (PRs open today)

| Feature | PRs | Likelihood in Next Release |
|:---|:---|:---:|
| **Google Extensions** (OAuth + Calendar + Gmail) | [#3893](https://github.com/nearai/ironclaw/pull/3893), [#3894](https://github.com/nearai/ironclaw/pull/3894), [#3895](https://github.com/nearai/ironclaw/pull/3895), [#3896](https://github.com/nearai/ironclaw/pull/3896), [#3897](https://github.com/nearai/ironclaw/pull/3897), [#3898](https://github.com/nearai/ironclaw/pull/3898) | High — phased design doc exists, all phases opened same day |
| **Subagent Spawn** | [#3868](https://github.com/nearai/ironclaw/pull/3868), [#3869](https://github.com/nearai/ironclaw/pull/3869), [#3870](https://github.com/nearai/ironclaw/pull/3870), [#3872](https://github.com/nearai/ironclaw/pull/3872) | Medium — design approved (#3798), but blocking bug #3875 needs resolution |
| **Product Auth Lifecycle** (OAuth, token refresh, credential recovery) | [#3865](https://github.com/nearai/ironclaw/pull/3865), [#3881](https://github.com/nearai/ironclaw/issues/3881)-[#3884](https://github.com/nearai/ironclaw/issues/3884) | High — 5 sequential steps filed, coordinated with WebUI beta |
| **Reborn Budgets** | [#3899](https://github.com/nearai/ironclaw/pull/3899) | Medium — addresses all #3841 follow-ups, cost tracking foundation |
| **Trigger Loop (Cron)** | [#3873](https://github.com/nearai/ironclaw/issues/3873) | Lower — V1 proposal, no PR yet, synthetic inbound message design |

### User-Requested / Ecosystem Features

| Item | Source | Signal |
|:---|:---|:---|
| [#2117](https://github.com/nearai/ironclaw/issues/2117) ironclaw-bridge (local file/MCP bridge for cloud) | henrypark133, 👍: 1 | **Infrastructure gap** — cloud-hosted users need local file access; blocked on tunnel system redesign |
| [#2394](https://github.com/nearai/ironclaw/pull/2394) WeCom channel | hanakannzashi | Enterprise China market need; large scope, high risk, long-running |
| [#3857](https://github.com/nearai/ironclaw/issues/3857) Slack ProductAdapter MVP | serrrfirat | Third-party integration expansion; "Lane 10" suggests prioritized sequence |
| [#3892](https://github.com/nearai/ironclaw/pull/3892) NEAR ecosystem summary skill | imrohitom (new contributor) | Ecosystem-specific skill; community contribution pattern |

---

## 7. User Feedback Summary

### Pain Points

| Issue | Evidence | User Impact |
|:---|:---|:---|
| Cloud-local file gap | [#2117](https://github.com/nearai/ironclaw/issues/2117) | Cannot use local Obsidian vaults, project directories with cloud-hosted IronClaw |
| nightly E2E failures | [#3447](https://github.com/nearai/ironclaw/issues/3447) | Regression detection degraded; confidence in `v2-engine` stability eroding |
| Auth/credential UX complexity | [#3881](https://github.com/nearai/ironclaw/issues/3881)-[#3884](https://github.com/nearai/ironclaw/issues/3884) sequence | Token setup, refresh, recovery, and cleanup currently leak backend details or require manual steps |

### Satisfaction Signals

- **WebUI Beta progress**: Rapid closure of #3611, #3625, #3626, #3623 suggests user-facing surface is approaching usable state
- **Explicit skill activation (#3861)**: User control over skill context is a UX win
- **Multi-tenancy isolation (#3890)**: Enterprise/community hosting confidence improving

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed |
|:---|:---:|:---|:---|
| [#2117](https://github.com/nearai/ironclaw/issues/2117) ironclaw-bridge | ~6 weeks | **User-visible capability gap** | Design review for tunnel system replacement; no PR linked |
| [#2394](https://github.com/nearai/ironclaw/pull/2394) WeCom channel | ~6 weeks | Large scope, high risk, may bit-rot against Reborn migration | Decision: rebase on Reborn or defer to post-migration |
| [#3031](https://github.com/nearai/ironclaw/issues/3031) Reborn product surface migration EPIC | ~4 weeks | **Meta-coordination risk** | Active but needs periodic consolidation; 7 comments suggest healthy but could become bottleneck |
| [#3280](https://github.com/nearai/ironclaw/issues/3280) ProductWorkflow and InboundTurnService facade | ~2.5 weeks | **Blocking multiple children** | Partially unblocked by #3623 split, but core facade still open |
| [#3094](https://github.com/nearai/ironclaw/issues/3094) Approval/auth interaction services | ~3.5 weeks | Split into #3889, #3891; original may be stale | Close or redirect to children |

**Maintainer Attention Recommended**: 
- **#2117** (bridge) — longest-running user request with clear use case, no engineering response visible
- **#2394** (WeCom) — risk of contributor burnout if Reborn migration forces repeated rebases without decision

---

*Digest generated from 76 GitHub items (26 issues, 50 PRs) updated 2026-05-22 to 2026-05-23.*

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI Project Digest — 2026-05-23

## 1. Today's Overview

LobsterAI shows **high development velocity** with 21 PRs updated in the last 24 hours (12 merged/closed, 9 open) and a fresh release cut today. The project is in an **active shipping phase**, with the core team aggressively landing subagent infrastructure improvements, UI polish, and model configuration enhancements. Notably, 10 PRs were merged/closed on 2026-05-22 alone, suggesting a coordinated release push for v2026.5.22. However, community contribution remains limited—most activity is from core maintainers (`fisherdaddy`, `btc69m979y-dotcom`) and dependabot, with several community PRs from April still stalled. The single active issue signals a specific architectural need around OpenClaw gateway event broadcasting for real-time persistence.

---

## 2. Releases

### [LobsterAI 2026.5.22](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.5.22)

| Aspect | Details |
|--------|---------|
| **Release Date** | 2026-05-22 |
| **Type** | Feature + Stability |

**What's Changed:**
- **feat: Subagent session sidebar display and detail view** ([#2011](https://github.com/netease-youdao/LobsterAI/pull/2011)) — New dedicated sidebar for subagent sessions with standalone detail view
- **feat: Model custom params + thinking block display** ([#2019](https://github.com/netease-youdao/LobsterAI/pull/2019)) — Users can now configure custom model parameters; reasoning/thinking blocks are visibly rendered
- **feat(cowork): ...** *(truncated in source)*

**Breaking Changes / Migration:** None explicitly noted. Subagent sessions are automatically backfilled on first access (lazy migration).

**Stability Notes:** This release bundles 10+ PRs fixing subagent sync bugs, duplicate tracking, missing tool results, and sidebar state issues—suggesting the subagent feature graduated from experimental to production-ready.

---

## 3. Project Progress

### Merged/Closed PRs (2026-05-22)

| PR | Author | Area | Summary |
|----|--------|------|---------|
| [#2038](https://github.com/netease-youdao/LobsterAI/pull/2038) | fisherdaddy | Release | **v2026.5.19 release rollup** — subagent UX, artifacts preview, cowork engine stability, model config flexibility |
| [#2037](https://github.com/netease-youdao/LobsterAI/pull/2037) | fisherdaddy | IM | Optimize IM-related copywriting |
| [#2035](https://github.com/netease-youdao/LobsterAI/pull/2035) | fisherdaddy | Docs | Fix Qwen coding plan for Qwen 3.6 Plus |
| [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034) | btc69m979y-dotcom | Main | **Persist subagent session messages to local DB** — SQLite `subagent_messages` table, lazy backfill, instant subsequent loads |
| [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | btc69m979y-dotcom | Renderer/Main/Cowork | **Fix subagent session bugs** — sync missing tool results, sidebar highlight state, empty/error handling, spawn error detection |
| [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | fisherdaddy | Docs/Main/OpenClaw | Fix model switch error with custom models |
| [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | fisherdaddy | Renderer/Main/OpenClaw | Fix browser config invalid |
| [#2030](https://github.com/netease-youdao/LobsterAI/pull/2030) | btc69m979y-dotcom | Renderer/Main/Cowork | **Refactor: subagent reuses main conversation rendering pipeline** — extracted `ConversationTurnsView`, full `CoworkMessage` format |
| [#2029](https://github.com/netease-youdou/LobsterAI/pull/2029) | btc69m979y-dotcom | Renderer/Main | Fix subagent sidebar style, duplicate tracking (toolCallId as unique key), missing tool results |
| [#2028](https://github.com/netease-youdao/LobsterAI/pull/2028) | fisherdaddy | Renderer/IM | UI update |
| [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) | btc69m979y-dotcom | Renderer/Cowork | Subagent page sidebar toggle, draggable header, Mac window controls padding fix |

**Key Advancements:**
- **Subagent architecture hardened**: From simple ReactMarkdown rendering to full conversation pipeline reuse, with local persistence and robust error handling
- **Cross-platform polish**: Mac window controls overlap fixed, draggable headers added
- **Model flexibility**: Custom parameters + thinking block display, Qwen 3.6 Plus support fixed

---

## 4. Community Hot Topics

### Most Active Discussion

| Item | Activity | Analysis |
|------|----------|----------|
| [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) — OpenClaw gateway `agent:turn`/`agent:loop` events | 1 comment, open | **Architectural bottleneck for real-time persistence**: Author `woxinsj` identifies that without per-turn broadcast events from the gateway, the system cannot reliably persist agent execution state to disk in real-time. This suggests the current polling or end-of-session persistence model is insufficient for production reliability. |

**Underlying Need:** The project needs **event-driven observability** at the agent loop level. This is foundational for:
- Crash recovery (resume interrupted long-running agents)
- Audit logging/compliance
- Real-time collaboration (multi-user agent observation)
- Debugging complex multi-step agent workflows

**Community PRs with Lingering Interest:**
| PR | Author | Status | Blocker |
|----|--------|--------|---------|
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) — Compact theme color circle selector | leedalei | Open since Apr 7, updated today | No maintainer review; UI-only, low risk |
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) — Local session usage stats panel | MaoQianTu | Open since Apr 7, updated today | No maintainer review; depends on `coworkStore.ts` |
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) — API proxy log security fix | kayo5994 | Open since Apr 7, updated today | **Security-critical**, no review |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) — KV store IPC key whitelist | kayo5994 | Open since Apr 7, updated today | **Security-critical**, no review |

---

## 5. Bugs & Stability

| Severity | Issue/PR | Description | Fix Status |
|----------|----------|-------------|------------|
| 🔴 **High** | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | No real-time persistence events from OpenClaw gateway; data loss risk on crash | **No fix PR** — architectural discussion needed |
| 🟡 **Medium** | [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033), [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | Subagent sync missing tool results, duplicate tracking, spawn errors | **Fixed in v2026.5.22** |
| 🟡 **Medium** | [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | Model switch errors with custom models | **Fixed** |
| 🟡 **Medium** | [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | Browser config invalid | **Fixed** |
| 🟢 **Low** | [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) | Mac window controls overlapping back button | **Fixed** |

**Regression Risk:** The rapid subagent refactoring (5 PRs in one day) suggests the feature was recently promoted from prototype. The lazy backfill persistence (#2034) is a pragmatic choice but may edge-case on corrupted sessions.

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Version |
|--------|--------|---------------------------|
| **OpenClaw gateway event streaming** (`agent:turn`/`agent:loop`) | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | **High** — blocker for production hardening |
| **Real-time collaboration / multi-user agent observation** | Implied by #2036 | Medium — depends on event infrastructure |
| **Enhanced usage analytics dashboard** | [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | Medium — community PR exists, needs review |
| **Theme customization polish** | [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | Low — nice-to-have, stalled |
| **Security hardening (log sanitization, IPC sandboxing)** | [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534), [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | **Should be high** — but no maintainer engagement |

**Predicted v2026.5.29 focus:** OpenClaw event system expansion, cowork engine stability, security PRs (if prioritized).

---

## 7. User Feedback Summary

**Pain Points:**
- **Data durability anxiety**: Users need confidence that long-running agent sessions survive crashes (#2036 explicitly calls this out)
- **Subagent observability**: Early subagent UX was "simple ReactMarkdown" — users likely struggled to debug/tool-call trace; now resolved with full conversation pipeline reuse
- **Model configuration rigidity**: Prior to custom params, users couldn't tune temperature/top-p/etc per model; now unblocked

**Use Cases Emerging:**
- **Deep research / multi-hop agents**: Subagent persistence + sidebar implies users run extended agent workflows needing history review
- **Team/shared agent environments**: The cowork engine + IM integration suggests enterprise/team use cases

**Satisfaction Signals:** Rapid iteration on subagent (5 PRs → release in 24h) indicates strong internal dogfooding and user demand.

---

## 8. Backlog Watch

| PR/Issue | Age | Risk | Action Needed |
|----------|-----|------|---------------|
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) — API proxy credential leak | ~6 weeks | 🔴 **Security vulnerability** — API keys in logs | **Urgent maintainer review & merge** |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) — KV store IPC sandbox escape | ~6 weeks | 🔴 **Security vulnerability** — renderer can access sensitive keys | **Urgent maintainer review & merge** |
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) — Usage stats panel | ~6 weeks | 🟡 Feature stagnation | Review or close with feedback |
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) — Theme selector | ~6 weeks | 🟢 Low priority | Review or close |
| [#1766](https://github.com/netease-youdao/LobsterAI/pull/1766)-[#1763](https://github.com/netease-youdao/LobsterAI/pull/1763), [#1277](https://github.com/netease-youdao/LobsterAI/pull/1277) — Dependabot major version bumps | ~4-6 weeks | 🟡 Dependency drift (Vite 5→8, React 18→19, Electron 40→42) | Evaluate breaking changes, merge or pin |

**Maintainer Attention Required:** The two security PRs by `kayo5994` (#1534, #1535) are the highest-risk backlog items. Their staleness despite being updated today (dependabot-style rebase?) suggests automated updates without human triage. The major version dependency bumps also need decision — Electron 42 and React 19 are significant jumps that could break the renderer/main IPC boundary.

---

*Digest generated from GitHub activity 2026-05-22. Project health: Strong shipping velocity, security backlog needs attention.*

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis Project Digest — 2026-05-23

## 1. Today's Overview

Moltis shows **strong maintainer velocity** with 4 PRs merged/closed against 3 open, indicating active development but also some unfinished work carrying over. The project is in a **stability-focused phase**, with today's merged fixes addressing Docker sandbox reliability, Twilio telephony parsing, and vault encryption flexibility. No new releases were cut, suggesting the team is accumulating fixes before a version bump. Community activity is moderate with 4 issues touched, though comment engagement remains low (maximum 5 comments on any item). The open PRs for Docker media file handling and MP3 voice generation indicate ongoing polish for containerized deployments and audio pipeline compatibility.

---

## 2. Releases

**No new releases** — version 20260518.01 remains current.

---

## 3. Project Progress

### Merged/Closed PRs (4 items)

| PR | Author | Summary | Impact |
|:---|:---|:---|:---|
| [#1035](https://github.com/moltis-org/moltis/pull/1035) | penso | **fix(sandbox): auto-detect docker host data mounts** | Resolves container path resolution for both sandbox exec and browser profiles; closes the underlying cause of [#977](https://github.com/moltis-org/moltis/issues/977) |
| [#1034](https://github.com/moltis-org/moltis/pull/1034) | penso | **fix(telephony): dispatch Twilio gather speech** | Fixes speech recognition in phone calls where agent greeted but didn't respond; closes [#1032](https://github.com/moltis-org/moltis/issues/1032) |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) | penso | **Allow disabling vault encryption at rest** | Adds operational flexibility for simpler deployments; includes safe migration path with decryption before disable |
| [#1039](https://github.com/moltis-org/moltis/pull/1039) | dependabot[bot] | **chore(deps): bump openssl 0.10.79 → 0.10.80** | Routine security/maintenance dependency update |

**Key advancement**: Docker sandbox reliability improved significantly with two coordinated fixes (#1035 merged, #1040 pending) addressing file system visibility in containerized environments.

---

## 4. Community Hot Topics

| Item | Engagement | Analysis |
|:---|:---|:---|
| [#977](https://github.com/moltis-org/moltis/issues/977) — Browser sandbox fails in Docker | **5 comments, closed** | Most discussed item; reveals **containerization as primary deployment pattern** for users. Resolution validates community investment in Docker workflows |
| [#1040](https://github.com/moltis-org/moltis/pull/1040) — Fix sandbox media file reads in Docker | Open, 0 comments | **Critical follow-up** to #1035; addresses `send_image`/`send_document` specifically. Silent engagement suggests users are watching rather than actively reviewing |

**Underlying need**: The Docker user segment is growing and encountering edge cases in sandbox isolation. Users need **seamless file I/O** between host, Moltis container, and sandbox containers without manual mount configuration.

---

## 5. Bugs & Stability

| Severity | Issue/PR | Status | Details | Fix Available |
|:---|:---|:---|:---|:---|
| **High** | [#1032](https://github.com/moltis-org/moltis/issues/1032) — Phone call: agent greets but never responds | **CLOSED** | Twilio `SpeechResult`/`Digits` parsing failed; broke entire voice interaction flow | ✅ [#1034](https://github.com/moltis-org/moltis/pull/1034) merged |
| **High** | [#1037](https://github.com/moltis-org/moltis/issues/1037) — `send_image`/`send_document` fail in Docker | **OPEN** | Media file path resolution broken in Docker; blocks multimodal workflows in containers | 🔄 [#1040](https://github.com/moltis-org/moltis/pull/1040) open, targets same root cause |
| **Medium** | [#977](https://github.com/moltis-org/moltis/issues/977) — Browser sandbox fails in Docker | **CLOSED** | `/data/browse` creation failed; blocked web automation in containers | ✅ [#1035](https://github.com/moltis-org/moltis/pull/1035) merged |

**Pattern**: All high-severity bugs this cycle involve **Docker-specific path/container edge cases**. The team is responsive (2/3 resolved within 24h of PR creation).

---

## 6. Feature Requests & Roadmap Signals

| Item | Type | Likelihood in Next Version | Rationale |
|:---|:---|:---|:---|
| [#1036](https://github.com/moltis-org/moltis/issues/1036) — Arbitrary inbound file attachments in web UI | Enhancement | **High** | Filed by active contributor (IlyaBizyaev), pairs with #1037/#1040 media handling work; natural extension of current file pipeline improvements |
| [#1031](https://github.com/moltis-org/moltis/pull/1031) — NEAR AI Cloud provider | New provider | **Medium-High** | Community contribution, OpenAI-compatible, TEE-aware positioning aligns with AI infrastructure trends; needs review bandwidth |
| [#1041](https://github.com/moltis-org/moltis/pull/1041) — MP3 for chat voice generation | Format compatibility | **High** | Small, targeted fix with regression tests; blocks OpenAI-compatible servers like Speaches |

**Predicted next release focus**: Container reliability (Docker media I/O), voice/chat audio format standardization, and expanded model provider ecosystem.

---

## 7. User Feedback Summary

### Pain Points
- **Docker deployment friction**: 3 of 4 issues/PRs involve containerized environment problems. Users expect "it just works" in Docker but hit mount visibility and path translation issues.
- **Voice interaction reliability**: Phone/Twilio users experienced complete conversation breakdown (#1032) — high-visibility failure mode for telephony use case.
- **Media handling gaps**: Image/document sending broken in Docker (#1037); web UI lacks arbitrary file upload (#1036).

### Use Cases Emerging
- **Self-hosted containerized deployments** (Proxmox/LXC/Docker stack)
- **Telephony/voice agents** via Twilio integration
- **Multimodal agents** with image/document I/O

### Satisfaction Signal
Rapid maintainer response (penso authored 4/7 PRs, merged 3 fixes within 24h) suggests healthy project stewardship. Low 👍 counts indicate small but engaged user base rather than mass adoption.

---

## 8. Backlog Watch

| Item | Age | Risk | Needs |
|:---|:---|:---|:---|
| [#1031](https://github.com/moltis-org/moltis/pull/1031) — NEAR AI Cloud provider | 2 days | **Contributor fatigue** | Maintainer review; external contribution may stall without feedback |
| [#1040](https://github.com/moltis-org/moltis/pull/1040) — Fix sandbox media file reads | 1 day | **User blocker** | Review and merge to resolve open #1037; pairs with already-merged #1035 |
| [#1041](https://github.com/moltis-org/moltis/pull/1041) — MP3 for chat voice | 1 day | **Compatibility fix** | Review; small, tested change with clear regression coverage |

**No long-stale items** in today's data — all open PRs are ≤2 days old. Project maintains healthy triage velocity.

---

*Digest generated from github.com/moltis-org/moltis activity for 2026-05-22/23.*

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw Project Digest — 2026-05-23

## 1. Today's Overview

CoPaw (QwenPaw) shows **high community activity** with 23 issues and 20 PRs updated in the last 24 hours, indicating an active development cycle despite no new release. The project is experiencing **significant bug triage pressure** with 16 open/active issues versus 7 closed, and a healthy merge rate with 9 PRs merged/closed against 11 still open. Notably, **first-time contributors are actively participating** (4 PRs marked), suggesting growing community engagement. The focus areas today center on **channel reliability** (WeChat, DingTalk), **model provider compatibility** (Gemini, MiniMax, DeepSeek, GPT-5.5), and **desktop experience improvements**. The maintainers appear responsive with same-day fixes for critical channel bugs, though the persistent chat history data loss issue (#4620) remains unresolved and is drawing significant community concern.

---

## 2. Releases

**No new releases** — Version v1.1.8.post1 remains the current release. No migration notes required.

---

## 3. Project Progress

### Merged/Closed PRs Today (9 items)

| PR | Author | Description | Significance |
|:---|:---|:---|:---|
| [#4395](https://github.com/agentscope-ai/QwenPaw/pull/4395) | aqilaziz | Security: unit tests for tool guard utilities | Test coverage expansion for security module |
| [#4600](https://github.com/agentscope-ai/QwenPaw/pull/4600) | hongxicheng | **Fix DingTalk Chinese filename encoding** | Resolves #4586 — URL percent-encoding bug for CJK filenames |
| [#4627](https://github.com/agentscope-ai/QwenPaw/pull/4627) | hongxicheng | **Fix WeChat token invalidation cross-request interference** | Critical reliability fix; improves #4618 with per-request meta flags instead of instance-level state |
| [#4626](https://github.com/agentscope-ai/QwenPaw/pull/4626) | Osier-Yi | Fix pet stuck in "Done" state on consecutive conversations | UI state machine fix for qwenpaw-pet |
| [#4623](https://github.com/agentscope-ai/QwenPaw/pull/4623) | zhaozhuang521 | Style: skill market page UI refresh | Console visual polish |
| [#4618](https://github.com/agentscope-ai/QwenPaw/pull/4618) | hongxicheng | Fix WeChat: skip sends when context_token invalid | Foundation for #4627 improvement |
| [#4621](https://github.com/agentscope-ai/QwenPaw/pull/4621) | qbc2016 | **Fix Gemini/Gemma max_tokens → max_output_tokens mapping** | Resolves #4605 — pydantic ValidationError crash |
| [#4434](https://github.com/agentscope-ai/QwenPaw/pull/4434) | weixizi | Feat: cron "clear context before run" option | Resolves #4432 — automated task isolation |
| [#4597](https://github.com/agentscope-ai/QwenPaw/pull/4597) | hongxicheng | **Fix WeChat API-initiated message failure reporting** | Resolves #4521 — false success responses for WeChat sends |

**Key advancements:** Channel reliability improved significantly with **3 WeChat-related fixes** and **1 DingTalk fix** merged. Model compatibility expanded with Gemini parameter mapping corrected. Cron job infrastructure gained context isolation capability.

---

## 4. Community Hot Topics

### Most Active Issues (by comment count)

| Rank | Issue | Comments | Status | Underlying Need |
|:---|:---|:---:|:---|:---|
| 1 | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) Chat history disappeared | **12** | 🔴 OPEN | **Data integrity crisis** — users losing conversation history, fundamental trust issue |
| 2 | [#4051](https://github.com/agentscope-ai/QwenPaw/issues/4051) DeepSeek think content parsing | 10 | ✅ CLOSED | Model output format compatibility (`<thinking>` tags) |
| 3 | [#4474](https://github.com/agentscope-ai/QwenPaw/issues/4474) ChatGPT-5.5 support | 8 | 🔴 OPEN | **Model provider agility** — users expect rapid new model support |
| 4 | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) NO_PROXY env var ignored | 6 | 🔴 OPEN | Enterprise proxy configuration reliability |

### Most Active PRs

| PR | Comments/Status | Significance |
|:---|:---|:---|
| [#4615](https://github.com/agentscope-ai/QwenPaw/pull/4615) Fix ACP orphan process | Under review, first-time contributor | External agent lifecycle management — addresses #4611 |

**Analysis:** The [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) chat history bug represents the **highest community anxiety** with 12 comments and explicit "critical bug" labeling. The pattern of model compatibility issues (DeepSeek, GPT-5.5, Gemini, MiniMax) suggests the provider abstraction layer needs proactive testing against new model releases rather than reactive fixes.

---

## 5. Bugs & Stability

| Severity | Issue | Description | Fix PR? | Risk Assessment |
|:---|:---|:---|:---:|:---|
| 🔴 **Critical** | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) | Chat history intermittently disappears — data loss | ❌ No | **User data loss** — highest priority; affects v1.1.8.post1; "existed for a long time" suggests systemic issue |
| 🟡 High | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) | NO_PROXY environment variable ignored | ❌ No | Enterprise/corporate users blocked; proxy configuration is infrastructure-critical |
| 🟡 High | [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625) | MiniMax-M2.5 returns XML thinking format, breaks compatibility | ❌ No | Model provider regression; "急盼修复" (urgent fix requested) |
| 🟡 High | [#4556](https://github.com/agentscope-ai/QwenPaw/issues/4556) | Voice transcription ignores Whisper config, uses browser Speech API | ❌ No | Configuration system integrity failure |
| 🟢 Medium | [#4616](https://github.com/agentscope-ai/QwenPaw/issues/4616) | Dream awakening task error, WeChat channel misconfiguration | ❌ No | Task system error propagation; false channel dependency |
| 🟢 Medium | [#4619](https://github.com/agentscope-ai/QwenPaw/issues/4619) | Web UI visual inconsistencies (alignment, icons) | ❌ No | Polish/UX debt |
| 🟢 Medium | [#4631](https://github.com/agentscope-ai/QwenPaw/issues/4631) | Desktop shows Python icon instead of app icon | ❌ No | Branding issue in Tauri desktop build |

**Fixed today:** #4605 (Gemini crash), #4521/#4612 (WeChat send failures), #4586 (DingTalk encoding), #3707 (MiniMax multimodal flag)

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Feature | Predicted Priority | Rationale |
|:---|:---|:---|:---|
| [#4632](https://github.com/agentscope-ai/QwenPaw/issues/4632) | **Multi-line text write tool** for agent framework | 🔥 High | Blocker for skill development, code persistence, config editing — fundamental capability gap |
| [#4613](https://github.com/agentscope-ai/QwenPaw/issues/4613) | Plugin agent hook support (`register_agent_hook`) | High | Ecosystem enablement; author has production LightRAG plugin blocked |
| [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624) | Per-model LLM retry/concurrency limits | High | Production multi-model deployments; quota optimization |
| [#4634](https://github.com/agentscope-ai/QwenPaw/issues/4634) | Window size/position memory (desktop) | Medium | Desktop UX polish; Tauri migration makes this feasible |
| [#4633](https://github.com/agentscope-ai/QwenPaw/issues/4633) | Customizable slash command shortcut menu | Medium | Discoverability improvement; low implementation cost |
| [#4617](https://github.com/agentscope-ai/QwenPaw/issues/4617) | Remote Playwright endpoint for browser_use | Medium | Infrastructure flexibility; resource sharing |
| [#4628](https://github.com/agentscope-ai/QwenPaw/pull/4628) | Plugin export/download as ZIP | Medium | Backup/sharing ecosystem |
| [#4630](https://github.com/agentscope-ai/QwenPaw/pull/4630) | MCP marketplace + health check + key validation | Medium | MCP (Model Context Protocol) infrastructure expansion |

**Likely in next release:** Multi-line text tool (#4632) and per-model rate limiting (#4624) address acute production pain points. Plugin hooks (#4613) may follow if ecosystem strategy prioritizes third-party extensions.

---

## 7. User Feedback Summary

### Pain Points

| Theme | Evidence | Severity |
|:---|:---|:---|
| **Data reliability** | #4620 (history loss), #3984 (orphaned messages after compaction) | Critical |
| **Model compatibility lag** | #4474 (GPT-5.5), #4625 (MiniMax XML), #4051 (DeepSeek thinking), #4605 (Gemini) | High |
| **Channel reliability** | #4521/#4612/#4607 (WeChat false success/NO_PROXY), #4586 (DingTalk encoding) | High |
| **Configuration effectiveness** | #4556 (ignored Whisper config), #4607 (ignored NO_PROXY) | Medium |
| **Desktop experience gaps** | #4634 (window memory), #4631 (Python icon), #3813 (Tauri ongoing) | Medium |

### Use Cases Emerging

- **Multi-model production deployments** — users mixing MiniMax, DeepSeek, OpenAI, Gemini with different quotas and formats
- **Enterprise/corporate environments** — proxy configuration, stable channel integrations (WeChat/DingTalk)
- **Plugin ecosystem development** — LightRAG knowledge base, data analysis (DataPaw), MCP servers
- **Desktop-native usage** — Tauri migration in progress (#3813)

### Satisfaction Signals

- Responsive maintainer fixes for channel bugs (same-day merges for WeChat/DingTalk)
- Active first-time contributor onboarding (4 PRs)
- Security test coverage expansion (#4395, #4467)

### Dissatisfaction Signals

- "Critical bug and existed for a long time" — [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620)
- "急盼修复" (urgently awaiting fix) — [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625)
- "全局统一的 LLM 自动重试和并发限流配置，已经无法适配" — [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624)

---

## 8. Backlog Watch

| Issue/PR | Age | Status | Risk | Action Needed |
|:---|:---|:---|:---|:---|
| [#3984](https://github.com/agentscope-ai/QwenPaw/issues/3984) | 23 days | 🔴 OPEN, 3 comments | **Data integrity** — context compaction orphans assistant messages; related to #4620 | Root cause analysis; likely same subsystem as critical #4620 |
| [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) | 29 days | 🔴 OPEN, first-time contributor | **Desktop strategy** — Tauri 2.x desktop support; significant architectural addition | Maintainer review decision; merge or provide feedback |
| [#4464](https://github.com/agentscope-ai/QwenPaw/pull/4464) | 6 days | 🔴 OPEN | Test infrastructure — e2e migration with mock infrastructure | CI integration review |
| [#4467](https://github.com/agentscope-ai/QwenPaw/pull/4467) | 6 days | 🔴 OPEN | **Security coverage** — 967 tests, 89% security coverage, CI gate upgrade | Merge to enforce quality standards |
| [#4565](https://github.com/agentscope-ai/QwenPaw/pull/4565) | 3 days | 🔴 OPEN | **Access control** — unified channel ACL with Matrix refactor | Architecture review; cross-channel impact |
| [#3707](https://github.com/agentscope-ai/QwenPaw/issues/3707) | 31 days | ✅ CLOSED today | MiniMax multimodal | **Resolved** — but pattern suggests provider flag maintenance needs automation |

**Urgent maintainer attention:** [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) (critical data loss) and [#3984](https://github.com/agentscope-ai/QwenPaw/issues/3984) (related compaction bug) need coordinated investigation. The Tauri desktop PR [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) risks contributor attrition after 29 days without resolution.

---

*Digest generated from GitHub activity data for agentscope-ai/CoPaw (QwenPaw) — 2026-05-23*

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw Project Digest — 2026-05-23

## 1. Today's Overview

ZeroClaw shows **exceptionally high development velocity** with 41 items updated in the last 24 hours (18 issues, 23 PRs), though merge throughput remains low with only 2 PRs closed versus 21 remaining open. The project is undergoing a major architectural expansion centered on a **standalone TUI (Terminal User Interface)** with at least 6 related issues/PRs filed by core contributor `singlerider` in a single day, alongside critical channel stability fixes for WhatsApp, Slack, and Telegram. The high open-to-closed ratio (95% PRs still open, 94% issues active) suggests either a review bottleneck or deliberate batching ahead of a significant release. No new versions were published today.

---

## 2. Releases

**None** — No releases published in the last 24 hours.

---

## 3. Project Progress

### Closed Items Today

| Item | Type | Description | Link |
|------|------|-------------|------|
| #5890 | Issue (RFC) | **Multi-agent UX flow design** — Accepted after core team vote (two-thirds majority), pending extraction to `docs/proposals/multi-agent-ux-flow.md` | [zeroclaw-labs/zeroclaw#5890](https://github.com/zeroclaw-labs/zeroclaw/issues/5890) |
| #6549 | PR | **Claude Code provider vision support** — Added vision input to `ClaudeCodeProvider`, fixing rejection of inbound images by agent loop's vision guard | [zeroclaw-labs/zeroclaw#6549](https://github.com/zeroclaw-labs/zeroclaw/pull/6549) |
| #6849 | PR | **Local merge** (Chinese title: 本地合并) — Massive cross-cutting PR touching all subsystems; closed without merge, likely superseded by smaller PRs | [zeroclaw-labs/zeroclaw#6849](https://github.com/zeroclaw-labs/zeroclaw/pull/6849) |

### Notable Advanced Work

- **TUI ecosystem bootstrapping**: 6 coordinated issues (#6821, #6823–6826, #6827, #6837) establishing architecture for `zeroclaw-tui` binary with Unix socket RPC, ACP bridge, agent chat, and theming
- **ACP protocol extensions**: Diff/file-proposal message types for approval workflows (#6820)
- **Memory architecture**: New `MemoryStrategy` trait to decouple policies from storage backends (#6850)

---

## 4. Community Hot Topics

| Rank | Item | Comments | Heat Analysis |
|------|------|----------|---------------|
| 1 | [#5890](https://github.com/zeroclaw-labs/zeroclaw/issues/5890) Multi-agent UX flow RFC | 10 | **Highest engagement**. Core design tension: how to orchestrate multiple agents without overwhelming users. Accepted by governance process but implementation pending. Signals community readiness for complex multi-agent workflows. |
| 2 | [#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) Work Lanes, Board Automation, and Label Cleanup | 3 | Governance fatigue. Maintainers seeking to reduce manual routing overhead. Underlying need: scale project management without bureaucracy. |
| 3 | [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) WhatsApp QR not showing | 2 | **S1 workflow blocked** — user onboarding failure. Immediate revenue/adoption risk if users cannot complete WhatsApp setup. |
| 4 | [#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820) ACP protocol extensions | 2 | Power-user feature for file editing approval. Shows demand for granular human-in-the-loop controls. |

**Underlying needs detected**: (a) **Operational scalability** — project governance and issue routing straining under growth; (b) **Onboarding reliability** — channel setup friction directly blocks users; (c) **Developer experience** — TUI as power-user escape hatch from web dashboard limitations.

---

## 5. Bugs & Stability

| Severity | Issue | Component | Status | Fix PR? | Link |
|----------|-------|-----------|--------|---------|------|
| **S1** | WhatsApp QR code not displaying during onboarding | `channel:whatsapp` | Accepted, no-stale | **Yes**: #6845 (LID→phone reply fix, related WhatsApp work) | [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) |
| **S1** | `vision_provider` silently ignored; images routed to fallback | `provider`, `channel:telegram` | Accepted, no-stale | No dedicated PR; #6549 (closed) addressed Claude Code vision | [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) |
| **S1** | Slack `bot_token` must be in config, cannot use env var | `channel:slack` | Accepted, no-stale | **Yes**: #6237 previously attempted fix, regression reported | [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844) |
| **S2** | `setup.bat --minimal` produces 26 MB vs expected ~6 MB | `runtime/daemon`, Windows | Accepted, no-stale | No | [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836) |

**Stability assessment**: Three S1 bugs active, all channel/provider configuration related. The Slack token regression (#6844) is particularly concerning — a previous fix (#6237, commit `5c2bfdca`) failed, suggesting test coverage gaps for environment variable resolution. Windows build bloat (#6836) indicates documentation drift or packaging toolchain issue.

---

## 6. Feature Requests & Roadmap Signals

| Feature | Signal Strength | Predicted Version | Rationale |
|---------|---------------|-------------------|-----------|
| **TUI (Terminal UI)** | ⭐⭐⭐ **Certain** | 0.80-beta or 0.81 | 6 coordinated issues, tracker #6826 marked "in-progress", RPC transport (#6837) and ACP bridge (#6823) in parallel development |
| **MemoryStrategy trait** | ⭐⭐⭐ High | Next minor | Architectural debt reduction; enables plugin ecosystem |
| **jina.ai web search provider** | ⭐⭐ Medium | Next minor | Simple integration, strong user value proposition (10M free requests) |
| **File upload protocol** | ⭐⭐ Medium | Paired with TUI | Blocked by TUI client need; base64-in-NDJSON design ready |
| **Ephemeral daemon mode** | ⭐⭐ Medium | Next minor | Low complexity, enables container/serverless deployments |
| **Session-scoped runtime overrides** | ⭐⭐ Medium | Next minor | Complements ephemeral mode for multi-tenant scenarios |
| **Lark/Feishu approval + cron** | ⭐⭐⭐ High | Imminent | Two PRs (#6851, #6852) filed same day, small scope |

**Roadmap prediction**: ZeroClaw is pivoting from "web-dashboard-primary" to "multi-interface" (web + TUI + headless). The TUI work is not cosmetic — it includes dedicated RPC transport, suggesting eventual feature parity and possibly TUI-as-primary for server deployments.

---

## 7. User Feedback Summary

### Direct Pain Points (from issue reports)

| User | Pain Point | Emotional Signal | Use Case |
|------|-----------|------------------|----------|
| MushiTheMoshi (#6847) | Cannot onboard WhatsApp — QR missing | Gratitude → frustration | SMB automation via WhatsApp |
| ppoloskov (#6841) | Vision config ignored silently | Confusion (expected multimodal) | Telegram bot with image understanding |
| mgstoyanov (#6844) | Slack token env var ignored | Annoyance (duplicate bug) | Enterprise Slack deployment, security policy requires env vars |
| rockswang (#6836) | Windows build 4× larger than docs claim | Distrust in documentation | Minimal Windows server deployment |

### Satisfaction Indicators

- **Strong project attachment**: MushiTheMoshi's "Best tool out there. Wishing way more stars" — genuine enthusiasm despite blocker
- **Active power-user engagement**: Multiple feature requests from repeat contributors (`singlerider`, `Audacity88`, `phrozen`)

### Dissatisfaction Patterns

1. **Configuration surprises**: Silent failures (vision routing), env var limitations, path expansion inconsistencies
2. **Platform inequality**: Windows-specific issues (build size, shell encoding in #6772)
3. **Channel reliability**: WhatsApp and Slack regressions suggest integration test gaps

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed | Link |
|------|-----|------|---------------|------|
| #5779 Gated commands TOTP for shell tool | ~5 weeks | **High** — security feature, "needs-author-action" | Author `DjaPy` to address review feedback; maintainer nudge | [#5779](https://github.com/zeroclaw-labs/zeroclaw/pull/5779) |
| #5987 Nix flake support | ~4 weeks | **High** — reproducible builds, "needs-author-action" | Author `srghma` to finalize; significant community demand for Nix | [#5987](https://github.com/zeroclaw-labs/zeroclaw/pull/5987) |
| #5652 Native extended thinking (Anthropic/Bedrock) | ~6 weeks | **Medium** — competitive feature, "needs-author-action" | Large PR (size L), provider complexity; may need splitting | [#5652](https://github.com/zeroclaw-labs/zeroclaw/pull/5652) |
| #5187 ARM64 Docker target | ~7 weeks | **High** — deployment blocker for Apple Silicon/ARM servers | Simple PR (size S), CI-only; unclear why stalled | [#5187](https://github.com/zeroclaw-labs/zeroclaw/pull/5187) |
| #6611 File rotation crate | ~10 days | **Medium** — marked "blocked" | Dependency or design blocker unspecified; needs status update | [#6611](https://github.com/zeroclaw-labs/zeroclaw/pull/6611) |

**Maintainer attention recommended**: #5187 (ARM64) is lowest-effort, highest-impact unblock. #5779 and #5987 have "needs-author-action" tags suggesting reviewer feedback was given but not addressed — risk of contributor attrition if stalled further.

---

*Digest generated from 41 GitHub activity items on 2026-05-23. All links reference `https://github.com/zeroclaw-labs/zeroclaw`.*

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*