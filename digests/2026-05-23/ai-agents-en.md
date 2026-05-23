# OpenClaw Ecosystem Digest 2026-05-23

> Issues: 500 | PRs: 500 | Projects covered: 13 | Generated: 2026-05-23 00:30 UTC

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

OpenClaw shows **extremely high development velocity** with 500 issues and 500 PRs updated in the last 24 hours, indicating a large, active contributor base and potentially a backlog-heavy triage process. The project has **no new releases today**, suggesting focus on stabilization rather than shipping. With 433 open/active issues (86.6%) and 386 open PRs (77.2%), the maintainers face significant review queue pressure. Critical security and privacy issues are receiving urgent attention—most notably a P0 cross-user memory leakage bug was identified and closed same-day. The project appears to be in a **intensive pre-release stabilization phase** with heavy investment in auth, session reliability, and platform expansion.

---

## 2. Releases

**No new releases** (0 releases published).

---

## 3. Project Progress

### Merged/Closed PRs Today

| PR | Author | Summary | Status |
|:---|:---|:---|:---|
| [#85554](https://github.com/openclaw/openclaw/pull/85554) | shakkernerd | Route OpenAI video edits to correct `/v1/videos/edits` endpoint; fix API routing bug | **Closed/Merged** |
| [#84439](https://github.com/openclaw/openclaw/pull/84439) | TurboTheTurtle | Scope config preflight note suppression—replace global stdout monkey-patch with async-scoped suppression | **Closed/Merged** |
| [#65212](https://github.com/openclaw/openclaw/pull/65212) | SYU8384 | Normalize QMD direct file collection paths (file-vs-directory handling) | **Closed/Merged** |
| [#81304](https://github.com/openclaw/openclaw/pull/81304) | MoerAI | Preserve existing primary model when applying provider auth in setup wizard | **Closed/Merged** |
| [#80882](https://github.com/openclaw/openclaw/pull/80882) | jameswniu | Eliminate ~30-min WhatsApp connection flap with presence keepalive | **Closed/Merged** |

### Key Advances

- **OpenAI video API correctness**: Fixed misrouted video edit requests
- **Setup wizard reliability**: Prevented unwanted model substitution during auth flow
- **WhatsApp stability**: Major availability improvement for personal accounts (30-min disconnect cycle eliminated)
- **TUI/Gateway performance**: Multiple PRs targeting cold-start optimization and memory bounding

---

## 4. Community Hot Topics

### Most Active Issues (by engagement)

| Issue | Comments | 👍 | Topic | Link |
|:---|:---|:---|:---|:---|
| **#75 Linux/Windows Clawdbot Apps** | 105 | 75 | Cross-platform desktop expansion | [openclaw/openclaw#75](https://github.com/openclaw/openclaw/issues/75) |
| **#9443 Prebuilt Android APK releases** | 24 | 1 | Mobile distribution | [openclaw/openclaw#9443](https://github.com/openclaw/openclaw/issues/9443) |
| **#44925 Subagent completion silently lost** | 14 | 0 | Critical orchestration reliability | [openclaw/openclaw#44925](https://github.com/openclaw/openclaw/issues/44925) |
| **#12602 Slack Block Kit support** | 13 | 0 | Enterprise messaging UX | [openclaw/openclaw#12602](https://github.com/openclaw/openclaw/issues/12602) |
| **#10659 Masked Secrets** | 12 | 4 | Security architecture | [openclaw/openclaw/issues/10659](https://github.com/openclaw/openclaw/issues/10659) |

### Underlying Needs Analysis

- **Platform parity demand**: #75's massive engagement (105 comments, 75 👍) reveals strong enterprise need for Linux/Windows desktop clients—currently macOS/iOS/Android have first-class support
- **Distribution friction**: #9443 (submitted by AI assistant QING on behalf of user Lysen) signals accessibility barriers for non-developer Android users
- **Silent failure intolerance**: #44925's "no retry, no notification, no auto-restart" pattern indicates subagent orchestration maturity gaps affecting production deployments
- **Security-conscious enterprise adoption**: #10659's masked secrets request reflects demand for credential isolation architectures comparable to secrets managers

---

## 5. Bugs & Stability

| Severity | Issue | Description | Fix PR? |
|:---|:---|:---|:---|
| **P0** | [#85240](https://github.com/openclaw/openclaw/issues/85240) | **Cross-user privacy leakage via `relevant-memories` semantic recall without `sender_id` isolation** | **Closed same day** — likely emergency fix |
| **P1** | [#85333](https://github.com/openclaw/openclaw/issues/85333) | `openclaw doctor --fix` 4-5x slower (55s → 229s+) — session snapshot path traversal bottleneck | None visible |
| **P1** | [#55334](https://github.com/openclaw/openclaw/issues/55334) | Gateway OOM from unbounded `sessions.json` growth with duplicated `skillsSnapshot` | None visible |
| **P1** | [#44925](https://github.com/openclaw/openclaw/issues/44925) | Subagent completion silently lost — no retry/notification/timeout recovery | None visible |
| **P1** | [#52249](https://github.com/openclaw/openclaw/issues/52249) | ACP parent session stuck until refresh when yielded waiting for child | None visible |
| **P1** | [#57019](https://github.com/openclaw/openclaw/issues/57019) | Session write lock race — async release can delete newly-acquired lock | None visible |
| **P1** | [#58479](https://github.com/openclaw/openclaw/issues/58479) | Approval dialog succeeds but exec never consumes approval (regression) | **Closed** |
| **P1** | [#71992](https://github.com/openclaw/openclaw/issues/71992) | Control UI webchat duplicates every assistant reply (regression from #5964/#39469) | None visible |

### Regressions & Performance

- **Performance regression**: `openclaw doctor --fix` severely degraded in 2026.5.20 — path traversal bottleneck identified
- **Memory regression**: Gateway sessions.json unbounded growth — ~50-100 MB/min leak rate
- **UI regression**: Duplicate message rendering in Control UI webchat

---

## 6. Feature Requests & Roadmap Signals

### Likely Near-Term (High Signal)

| Feature | Issue | Confidence | Rationale |
|:---|:---|:---|:---|
| **Native secrets management** (AWS SM, Vault) | [#13610](https://github.com/openclaw/openclaw/issues/13610) | High | Complements #10659 masked secrets; security-critical for enterprise |
| **Per-model usage logging** | [#13219](https://github.com/openclaw/openclaw/issues/13219) | High | Cost tracking is universal production need; low implementation risk |
| **Session snapshots (save/load)** | [#13700](https://github.com/openclaw/openclaw/issues/13700) | Medium-High | Natural extension of existing session infrastructure |
| **Model fallback on context-length exceeded** | [#9986](https://github.com/openclaw/openclaw/issues/9986) | Medium | Config exists but incomplete; clear user pain |

### Platform Expansion

| Feature | Issue | Blockers |
|:---|:---|:---|
| **Linux/Windows desktop apps** | [#75](https://github.com/openclaw/openclaw/issues/75) | Resource allocation; macOS parity target complex |
| **Prebuilt Android APKs** | [#9443](https://github.com/openclaw/openclaw/issues/9443) | Build/release infrastructure; signing/distribution |
| **Vapi voice call provider** | [#13337](https://github.com/openclaw/openclaw/issues/13337) | Third-party API integration; Japanese-language contribution active |

### Security & Governance (Enterprise Blockers)

| Feature | Issue | Strategic Importance |
|:---|:---|:---|
| **Pre-response enforcement hooks (hard gates)** | [#13583](https://github.com/openclaw/openclaw/issues/13583) | Required for regulated industries (finance, ops) |
| **Capability-based permissions** | [#12678](https://github.com/openclaw/openclaw/issues/12678) | Default-deny security model |
| **Unbypassable outbound policy enforcement** | [#56349](https://github.com/openclaw/openclaw/issues/56349) | Compliance/audit requirement |
| **Filesystem sandboxing config** | [#7722](https://github.com/openclaw/openclaw/issues/7722) | Multi-tenant safety |

---

## 7. User Feedback Summary

### Pain Points

| Category | Specific Feedback | Source Issues |
|:---|:---|:---|
| **Silent failures** | Subagent results lost without any user-visible error; sessions hang without recovery | #44925, #52249, #54531 |
| **Memory/performance** | Gateway OOM, session bloat, doctor command slowdown | #55334, #85333 |
| **Platform gaps** | No Linux/Windows desktop; no prebuilt Android; mobile distribution friction | #75, #9443 |
| **Security anxiety** | Raw API key exposure, no native secrets manager, broad OAuth scopes | #10659, #13610, #13751 |
| **Operational visibility** | No per-model cost tracking; config warning spam; status misreporting | #13219, #25574, #57256 |

### Use Cases Emerging

- **Multi-channel business operations**: WhatsApp/Slack/Discord/Telegram orchestration with reply routing guarantees (#54531)
- **Regulated autonomous agents**: Financial/quant workflows requiring hard policy enforcement before any action (#13583)
- **Team/collaborative AI**: Group chat context disambiguation with multiple agents (#56692)

### Satisfaction Indicators

- Strong engagement with feature requests (detailed proposals, mock implementations)
- Active third-party contributions (Vapi provider, QQBot fixes)
- Rapid security response (P0 closed same-day)

### Dissatisfaction Indicators

- High open/closed ratio suggests triage backlog
- Multiple "needs-maintainer-review" and "needs-product-decision" labels indicate decision bottleneck
- Recurring "regression" tags signal test coverage gaps

---

## 8. Backlog Watch

### Critical Items Needing Maintainer Attention

| Issue/PR | Age | Blocker | Risk |
|:---|:---|:---|:---|
| [#75](https://github.com/openclaw/openclaw/issues/75) Linux/Windows apps | ~5 months | Product decision, resource allocation | **Platform parity gap** — highest community demand |
| [#10659](https://github.com/openclaw/openclaw/issues/10659) Masked secrets | ~3.5 months | Security review, product decision | **Enterprise adoption blocker** |
| [#13583](https://github.com/openclaw/openclaw/issues/13583) Hard gates | ~3.5 months | Security review, product decision | **Regulated industry requirement** |
| [#6731](https://github.com/openclaw/openclaw/issues/6731) Safe/unsafe ClawdBot | ~3.5 months | Product decision, architectural | **Safety architecture** — includes Rust rewrite suggestion |
| [#85341](https://github.com/openclaw/openclaw/pull/85341) Internalize OpenClaw agent runtime | New | Needs proof, massive surface (XL) | **Foundational refactor** — steipete's runtime internalization |

### PR Review Queue Pressure

- **386 open PRs** with many marked "needs proof" or "waiting on author"
- **"Actively grinding"**: [#80482](https://github.com/openclaw/openclaw/pull/80482) auth billing fix
- **"Ready for maintainer look"** accumulating: #84649, #85403, #85541, #85119, #85533, #85258

### Triage System Observations

The `clawsweeper:` label taxonomy suggests automated triage with categories:
- `no-new-fix-pr` / `fix-shape-clear`: Fix coordination
- `needs-maintainer-review` / `needs-product-decision` / `needs-security-review`: Decision gates
- `source-repro`: Reproduction requirements

**Bottleneck pattern**: Security review and product decision labels appear frequently together, suggesting serialized review processes that may delay parallel engineering progress.

---

*Digest generated from 500 issues and 500 PRs updated 2026-05-23. Data source: github.com/openclaw/openclaw*

---

## Cross-Ecosystem Comparison

# Cross-Project Comparison Report: Open-Source AI Agent Ecosystem
**Date:** 2026-05-23 | **Analyst:** Senior AI Agent Ecosystem Analyst

---

## 1. Ecosystem Overview

The open-source personal AI assistant ecosystem is experiencing intense fragmentation and parallel evolution, with **10+ active projects** pursuing distinct architectural philosophies—from OpenClaw's gateway-centric multi-channel orchestration to IronClaw's ground-up "Reborn" Rust rewrite. The space is maturing from "chatbot wrappers" toward **production-grade agent runtimes** with enterprise security requirements, multi-agent orchestration, and voice/telephony integration. However, **maintainer bandwidth constraints** are universal: even high-velocity projects show 70-90% open PR ratios, indicating engineering demand significantly outpaces review capacity. No single project has achieved platform dominance; instead, specialization by deployment target (embedded, desktop, cloud, containerized) is emerging.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Releases | Health Score | Assessment |
|:---|:---|:---|:---|:---|:---|
| **OpenClaw** | 500 | 500 | None | ⚠️ **Stressed** | Extreme velocity with severe triage backlog; 86.6% open issues, 77.2% open PRs |
| **NanoBot** | 7 | 20 | None | ✅ **Healthy** | 60% merge rate, focused feature consolidation; manageable scale |
| **Hermes Agent** | 50 | 50 | None | ⚠️ **Concerning** | 94% open issues, 82% open PRs; P1 bugs unassigned |
| **PicoClaw** | 10 | 20 | Nightly (v0.2.8) | 🟡 **Caution-Positive** | 70% issue closure but stale-bot closing critical bugs unverified |
| **NanoClaw** | 6 | 31 | None | ✅ **Healthy** | 90% merge rate; Apple Container skill unmaintained is localized risk |
| **NullClaw** | 0 | 4 | None | 🟡 **Stable-Pending** | Zero issues concerning; 46-day PR aging indicates review stall |
| **IronClaw** | 23 | 50 | None | 🟡 **Intense-Pre-release** | Core-team driven; 72% open PR ratio acceptable for architectural overhaul phase |
| **LobsterAI** | Minimal data | 21 | **2026.5.22** | 🟡 **Caution** | Corporate-driven, zero community engagement; security PRs languishing |
| **Moltis** | 8 | 9 | None | ✅ **Strong** | 87.5% issue closure, 100% PR merge; exceptional maintainer bandwidth |
| **CoPaw** | 24 | 23 | None | ⚠️ **Stressed-Growing** | 71% open issues, 57% open PRs; growing pains with provider compatibility |
| **ZeroClaw** | 37 | 50 | None | ⚠️ **Stressed** | 57% open issues; governance scaling pain explicit in community |

*Health Score methodology: Merge/closure velocity vs. open backlog, release cadence, critical bug response, maintainer bandwidth indicators.*

---

## 3. OpenClaw's Position

### Advantages vs. Peers

| Dimension | OpenClaw | Peer Comparison |
|:---|:---|:---|
| **Scale** | 500 issues/PRs daily | 10-50x larger than all peers; indicates dominant mindshare |
| **Security response** | Same-day P0 closure (cross-user memory leak) | Hermes has 3 P1s unassigned for days; LobsterAI security PRs stale 6 weeks |
| **Platform breadth** | macOS/iOS/Android first-class, Linux/Windows demanded | PicoClaw embedded-focused; Moltis container-first; NanoClaw channel-diverse |
| **Provider ecosystem** | OpenAI video API, WhatsApp, Slack, Discord, Telegram | Most peers cover subset; ZeroClaw comparable but fragmented |

### Technical Approach Differences

- **Gateway-centric architecture**: OpenClaw's `clawsweeper` automated triage and gateway event system (per LobsterAI #2036 request) positions it as **infrastructure layer** for other projects—LobsterAI explicitly building on OpenClaw gateway
- **Session reliability investment**: Unique focus on session write locks, snapshots, subagent orchestration—vs. NanoClaw's transcript rotation, ZeroClaw's Dream Mode memory
- **Enterprise security depth**: Native secrets management demand (#10659, #13610) exceeds peers' implementations; IronClaw comparable with "Lanes" security architecture

### Community Size Comparison

OpenClaw operates at **ecosystem-hub scale** (500 daily items) versus **project scale** (NanoBot 27, Moltis 17, PicoClaw 30). Only ZeroClaw (87) and IronClaw (73) approach comparable velocity. However, OpenClaw's **engagement-to-resolution ratio** is weakest among major projects—suggesting success has created coordination overhead that smaller projects avoid.

---

## 4. Shared Technical Focus Areas

| Requirement | Projects | Specific Needs |
|:---|:---|:---|
| **Multi-channel reliability** | OpenClaw, NanoClaw, ZeroClaw, CoPaw, PicoClaw | WhatsApp protocol fragility (ZeroClaw #6246, OpenClaw #80882, NanoClaw #2579); WeChat token isolation (CoPaw #4627); Telegram topic context (PicoClaw #2791) |
| **Subagent/orchestration maturity** | OpenClaw, LobsterAI, IronClaw, PicoClaw | Silent failure recovery (OpenClaw #44925); persistence (LobsterAI #2034); spawn parent resumption (IronClaw #3875); peer-to-peer comms (PicoClaw #2929) |
| **Enterprise security & compliance** | OpenClaw, IronClaw, NanoBot, Moltis | Masked secrets (OpenClaw #10659); capability-based permissions (#12678); hard enforcement gates (#13583); vault encryption opt-out (Moltis #1033) |
| **Container/Docker hardening** | Moltis, PicoClaw, NanoClaw, ZeroClaw | Nested container path resolution (Moltis #977); sandbox media reads (#1040); rootless Podman (NanoClaw #2572); ARM64 builds (PicoClaw #2625, ZeroClaw #5187) |
| **Voice/telephony integration** | Moltis, PicoClaw, ZeroClaw | Twilio gather parsing (Moltis #1032); voice transcription routing (PicoClaw #2817); TTS format interoperability (Moltis #1030, #1041) |
| **Model provider agility** | CoPaw, NanoBot, ZeroClaw, OpenClaw | Gemini parameter mapping (CoPaw #4621); DeepSeek thinking controls (PicoClaw #2928); Codex-only path (NanoClaw #2580); context-length fallback (OpenClaw #9986) |
| **Observability & diagnostics** | ZeroClaw, OpenClaw, NanoBot | OTel tool spans (ZeroClaw #6009); `doctor` command degradation (OpenClaw #85333); `nanobot doctor` (NanoBot #3776) |

---

## 5. Differentiation Analysis

| Project | Primary Differentiator | Target User | Architecture Signature |
|:---|:---|:---|:---|
| **OpenClaw** | Gateway-centric multi-channel orchestration; ecosystem hub | Enterprise ops, power users | Rust/Go hybrid; event-driven gateway; pluggable providers |
| **NanoBot** | "Lean and mean" CLI-first; local image generation | Developers, CLI-native users | TypeScript; skill registry; lightweight containerization |
| **Hermes Agent** | Kanban/task management integration; desktop-native | Knowledge workers, GTD practitioners | Tauri/Electron; local-first; skill bundles |
| **PicoClaw** | Embedded/IoT deployment; Go runtime efficiency | Raspberry Pi, edge compute, Sipeed hardware | Pure Go; minimal resource footprint; Telegram focus |
| **NanoClaw** | Container-native; Apple Silicon optimization; bun runtime | macOS developers, container enthusiasts | TypeScript/bun; Codex parity; scoped approvals |
| **NullClaw** | NEAR blockchain ecosystem; decentralized AI | Web3/crypto developers | Rust; cron subsystem; minimal surface area |
| **IronClaw** | Ground-up Rust "Reborn" architecture; Google ecosystem | Security-conscious enterprise; Google Workspace users | Rust; WASM sandboxing; composable auth "Lanes" |
| **LobsterAI** | Subagent UX sophistication; NetEase corporate backing | Chinese market; desktop assistant users | Electron; SQLite persistence; OpenClaw gateway client |
| **Moltis** | Voice-first telephony; Docker-native deployment | Call centers, voice AI applications | Rust; Twilio integration; container sandboxing |
| **CoPaw** | Multi-model Chinese ecosystem; plugin marketplace | Chinese enterprise; Qwen ecosystem | Python; WeChat/DingTalk integration; Tauri migration |
| **ZeroClaw** | "Dream Mode" autonomous memory; TUI-daemon architecture | Self-hosting enthusiasts; agent autonomy seekers | Rust; MCP ecosystem; Unix socket runtime RPC |

**Key architectural divergence**: **Event-driven vs. polling** (OpenClaw/LobsterAI gateway events vs. NanoClaw transcript rotation), **Compiled vs. interpreted** (IronClaw/PicoClaw/NullClaw/Moltis/ZeroClaw Rust/Go vs. NanoBot/NanoClaw/CoPaw TypeScript/Python), **Gateway vs. embedded** (OpenClaw central hub vs. Hermes desktop-native).

---

## 6. Community Momentum & Maturity

### Activity Tiers

| Tier | Projects | Characteristics |
|:---|:---|:---|
| **Hypervelocity (50+ daily items)** | OpenClaw, ZeroClaw, IronClaw | Engineering throughput exceeds review capacity; risk of contributor burnout and PR bit-rot |
| **High-velocity (20-50 items)** | CoPaw, NanoClaw, Hermes Agent | Active sprint cycles; manageable but growing backlog |
| **Steady (10-20 items)** | NanoBot, PicoClaw, Moltis | Sustainable pace; high closure ratios; mature triage |
| **Maintenance/consolidation (<10 items)** | NullClaw, LobsterAI | NullClaw stable-pending; LobsterAI corporate-controlled with security debt |

### Rapid Iteration Phase

- **IronClaw**: "Reborn" architectural overhaul; no releases by design; high technical risk/high reward
- **ZeroClaw**: TUI integration + Dream Mode + v0.8.0 pre-release; governance scaling explicitly acknowledged (#6808)
- **OpenClaw**: Pre-release stabilization; security-intensive; platform expansion (Linux/Windows #75)

### Stabilization Phase

- **Moltis**: Exceptional health metrics; feature-complete for voice use case; polishing container edge cases
- **NanoBot**: Image generation consolidation; CLI Apps ecosystem launch; security hardening
- **PicoClaw**: v0.2.9 approaching; stale-bot risk notwithstanding; Telegram/Matrix context fixes

### At-Risk Projects

| Project | Risk Factor | Mitigation Needed |
|:---|:---|:---|
| **Hermes Agent** | 3 P1 bugs unassigned; 94% open issues | Emergency maintainer allocation or scope reduction |
| **LobsterAI** | Security PRs stale 6 weeks; zero community | Corporate security review mandate; external audit |
| **NullClaw** | 46-day PR aging; zero issues may indicate low adoption | Community outreach; release to validate interest |

---

## 7. Trend Signals

### For AI Agent Developers

| Trend | Evidence | Strategic Implication |
|:---|:---|:---|
| **Agent autonomy narratives → runtime complexity** | ZeroClaw Dream Mode (11 comments), IronClaw subagent spawn design (#3798), OpenClaw subagent silent failures (#44925) | "Self-improving agents" require deep hooks into memory, scheduling, reflection—far beyond simple LLM loops |
| **Container-native as default deployment** | Moltis Docker sandboxing, NanoClaw rootless Podman, PicoClaw ARM64 demand, ZeroClaw ARM64 Docker | Developers should assume containerized deployment; bare-metal support becoming secondary |
| **Voice/telephony as emerging standard** | Moltis Twilio, PicoClaw voice transcription, ZeroClaw TTS ecosystem | Text-only agents are legacy; multimodal voice+text expected |
| **Provider format fragmentation accelerating** | CoPaw Gemini/DeepSeek/MiniMax fixes, NanoBot Anthropic 400 errors, OpenClaw OpenAI video routing | Abstraction layers must normalize provider quirks; "OpenAI-compatible" insufficient |
| **Security as competitive differentiator, not checkbox** | OpenClaw P0 same-day response, IronClaw capability-based permissions, NanoBot exec confirmation (#3937) | Enterprise adoption gated on hard security guarantees; "trust us" insufficient |
| **Governance tooling as scaling bottleneck** | ZeroClaw Work Lanes RFC (#6808), OpenClaw `clawsweeper` labels, Hermes manual triage strain | Projects investing in automation early (labels, bots, RFCs) will sustain velocity |
| **Cross-project dependency emergence** | LobsterAI building on OpenClaw gateway; NanoClaw Codex parity; IronClaw NEAR ecosystem | Ecosystem layering: infrastructure (OpenClaw) → application (LobsterAI) → specialized runtime (IronClaw) |

### Investment Priorities for Developers Evaluating Projects

1. **Production reliability**: Moltis (proven), NanoBot (responsive), OpenClaw (capable but backlogged)
2. **Enterprise security**: IronClaw (architectural), OpenClaw (responsive), NanoBot (hardening)
3. **Voice/telephony**: Moltis (mature), ZeroClaw (developing)
4. **Embedded/edge**: PicoClaw (purpose-built)
5. **Developer experience**: NanoClaw (fast fixes), NanoBot (CLI-first)
6. **Ecosystem extensibility**: OpenClaw (gateway), ZeroClaw (MCP), CoPaw (plugins)

---

*Report generated from 11 project digests covering 1,247+ GitHub items (2026-05-22 to 2026-05-23).*

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot Project Digest — 2026-05-23

## 1. Today's Overview

NanoBot showed **strong development velocity** with 20 PRs and 7 issues updated in the past 24 hours, indicating an active maintainer team and engaged contributor base. The project is in a **feature consolidation phase** with significant work on CLI Apps, image generation providers, and memory system improvements. No new release was cut today, suggesting the team may be batching changes for a larger version bump. The high merge rate (12/20 PRs closed) reflects healthy code review throughput. Internationalization and security hardening received notable attention, signaling production-readiness efforts.

---

## 2. Releases

**No new releases** — No version tags or release notes published today.

---

## 3. Project Progress

### Merged/Closed PRs (12 items)

| PR | Description | Impact |
|:---|:---|:---|
| [#2364](https://github.com/HKUDS/nanobot/pull/2364) | Prevent cron job self-duplication by injecting anti-recursion directive | **Fixes critical heartbeat bug** — closes recursion loop where cron jobs spawned duplicate scheduled tasks |
| [#3964](https://github.com/HKUDS/nanobot/pull/3964) | Fill remaining WebUI locale keys (es, fr, id, ko, vi) | i18n completeness for 5 languages |
| [#3965](https://github.com/HKUDS/nanobot/pull/3965) | Cover CLI Apps on Windows CI | **Platform parity** — eliminates Unix-only test assumptions |
| [#3963](https://github.com/HKUDS/nanobot/pull/3963) | Add CLI Apps for CLI-Anything integrations | **Major feature** — installs apps from official/public registry for `@` mentions |
| [#3928](https://github.com/HKUDS/nanobot/pull/3928) | Validate redirect targets before fetching | **Security fix** — closes SSRF vulnerability in `web_fetch` redirects |
| [#3962](https://github.com/HKUDS/nanobot/pull/3962) | Fill zh-TW and ja locale keys | East Asian i18n coverage |
| [#3961](https://github.com/HKUDS/nanobot/pull/3961) | Dedupe Responses replay item ids | Fixes Codex conversation resumption failures |
| [#3946](https://github.com/HKUDS/nanobot/pull/3946) | Add Ollama image generation support | **New provider** — local image gen via `/api/generate` |
| [#3954](https://github.com/HKUDS/nanobot/pull/3954) | Add OpenAI and Codex image generation provider support | **New providers** — Responses API routing for Codex OAuth |
| [#3960](https://github.com/HKUDS/nanobot/pull/3960) | Remove deprecated patch mode from `apply_patch` | **Breaking cleanup** — simplifies tool to `edits`-only |
| [#3957](https://github.com/HKUDS/nanobot/pull/3957) | Avoid misleading file edit counters in WebUI | UX polish for diff display |

**Key advancement areas:** Image generation (3 providers added in 2 days), CLI Apps ecosystem launch, security hardening, and heartbeat reliability.

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|:---|:---|:---|
| [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI conversation closes after first response | **6 comments**, closed | High-impact UX bug; rapid resolution suggests WebUI stability is prioritized |
| [#3846](https://github.com/HKUDS/nanobot/issues/3846) Keep skill content in multi-turn conversations | 4 comments, 👍1 | **Architectural tension** — users need persistent skill context beyond `read_file`; indicates skill system design gap |
| [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill` lists disabled skills | 4 comments, new | Configuration-UI inconsistency; suggests skill management needs refinement |

**Underlying needs:** The skill system is emerging as a **core friction point** — users want finer-grained control over skill lifecycle, persistence, and visibility. The conversation-closing bug (#3884) and disabled-skill leak (#3959) both point to **state management robustness** as a user trust issue.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR |
|:---|:---|:---|:---|
| 🔴 **Critical** | [#3956](https://github.com/HKUDS/nanobot/issues/3956) Anthropic API 400 error from list-structured tool results | **Closed** | [#3961](https://github.com/HKUDS/nanobot/pull/3961) (dedupe replay IDs) — *partial; root cause was list format in history* |
| 🟡 **High** | [#3028](https://github.com/HKUDS/nanobot/issues/3028) Heartbeat creates duplicate scheduled tasks | **Open** | [#2364](https://github.com/HKUDS/nanobot/pull/2364) merged — *may resolve; needs verification* |
| 🟡 **High** | [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI conversation closes after first response | **Closed** | Resolved in unspecified PR |
| 🟢 **Medium** | [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill` lists disabled skills | **Open** | None yet |

**Note:** The Anthropic 400 error (#3956) reveals a **systemic API compatibility risk** — tool result serialization format varies by provider, and history replay doesn't normalize. The heartbeat duplication (#3028) is a **long-standing issue** (opened April 11) that may finally be addressed by PR #2364's anti-recursion directive.

---

## 6. Feature Requests & Roadmap Signals

| Request | Issue/PR | Likelihood in Next Version |
|:---|:---|:---|
| Ollama image generation | [#3941](https://github.com/HKUDS/nanobot/issues/3941) → [#3946](https://github.com/HKUDS/nanobot/pull/3946) | ✅ **Shipped** |
| OpenAI/Codex image generation | [#3954](https://github.com/HKUDS/nanobot/pull/3954) | ✅ **Shipped** |
| Weather skill → example folder | [#3958](https://github.com/HKUDS/nanobot/issues/3958) | 🔶 **High** — aligns with "lean and mean" philosophy, trivial implementation |
| BM25-lite skill router | [#3865](https://github.com/HKUDS/nanobot/pull/3865) | 🔶 **Moderate** — ~60% token reduction is compelling, but needs review bandwidth |
| `nanobot doctor` diagnostic command | [#3776](https://github.com/HKUDS/nanobot/pull/3776) | 🔶 **Moderate** — 10 automated checks, high user value, stalled since May 14 |
| Manifest LLM router support | [#3568](https://github.com/HKUDS/nanobot/pull/3568) | 🔷 **Lower** — open since April 30, gateway provider niche |
| User confirmation for dangerous `exec` commands | [#3937](https://github.com/HKUDS/nanobot/pull/3937) | 🔶 **High** — security-critical, closes #3887 |

**Prediction:** Next release will likely bundle image generation expansion, CLI Apps v1, and security UX (exec confirmation). The BM25 router and `doctor` command are **mature PRs at risk of bit-rot** without maintainer focus.

---

## 7. User Feedback Summary

### Pain Points
- **Heartbeat system reliability**: "重复创建了定时任务" (duplicate scheduled tasks) — users experiencing spam from broken cron logic (#3028)
- **WebUI fragility**: Conversations terminating unexpectedly (#3884), misleading edit counters (#3957)
- **Skill system opacity**: Disabled skills still appear; skill context lost between turns (#3846, #3959)
- **Provider-specific breakages**: Anthropic history format incompatibility (#3956)

### Use Cases
- **Local-first image generation**: Strong demand for Ollama support (#3941) — users running `x/z-image-turbo` locally
- **Multi-language deployments**: Active i18n contributions (es, fr, id, ko, vi, zh-TW, ja) suggest global user base
- **CLI-Anything ecosystem**: Users want to extend nanobot with external CLI tools via registry

### Satisfaction Signals
- Rapid closure of critical bugs (6-day resolution for #3884)
- Responsive security fixes (#3928 SSRF closed promptly)

### Dissatisfaction Signals
- Long-open PRs (#3568, #3776, #3865) may indicate contributor frustration
- Heartbeat bug open 6+ weeks (#3028) before potential fix

---

## 8. Backlog Watch

| Item | Age | Risk | Needs |
|:---|:---|:---|:---|
| [#3028](https://github.com/HKUDS/nanobot/issues/3028) Heartbeat duplicate cron tasks | 6+ weeks | **User trust erosion** | Verify PR #2364 actually resolves; add regression test |
| [#3568](https://github.com/HKUDS/nanobot/pull/3568) Manifest LLM router | ~3 weeks | Contributor abandonment | Maintainer review or explicit deferral |
| [#3776](https://github.com/HKUDS/nanobot/pull/3776) `nanobot doctor` | ~1.5 weeks | High-value feature stall | Review cycle; 10-check diagnostic is complete |
| [#3865](https://github.com/HKUDS/nanobot/pull/3865) BM25 skill router | ~1 week | Token optimization at scale | Performance benchmark review; potential merge conflict with skill system changes |
| [#1443](https://github.com/HKUDS/nanobot/pull/1443) Decouple heartbeat reasoning from notification | ~2.5 months | **Architectural debt** | Long-running PR; may need rebase; core heartbeat redesign |

**Urgent attention:** PR #1443 (heartbeat reasoning decoupling) is the **oldest active PR** and intersects directly with the critical bug #3028. Consolidating these two would resolve systemic heartbeat issues. The `doctor` command (#3776) is **low-risk, high-visibility** — a quick win for user onboarding.

---

*Digest generated from HKUDS/nanobot GitHub activity on 2026-05-23. All links: https://github.com/HKUDS/nanobot*

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent Project Digest — 2026-05-23

## 1. Today's Overview

Hermes Agent shows **extremely high community activity** with 50 issues and 50 PRs updated in the last 24 hours, indicating a vibrant but potentially strained development cycle. The project is in an active stabilization phase for v0.14.0, with zero new releases and a heavy focus on bug fixes over new features. The high open-to-closed ratio (47:3 issues, 41:9 PRs) suggests maintainer bandwidth may be lagging behind community contributions. Gateway infrastructure and platform adapters dominate the discussion, reflecting growing production deployment complexity. Overall project health is **moderate-to-strong on engagement, but concerning on resolution velocity**.

---

## 2. Releases

**No new releases** — v0.14.0 remains the current version. The absence of a patch release despite multiple P1/P2 bugs (state.db corruption, crash loops, silent exits) suggests maintainers may be accumulating fixes for a larger release or are blocked on verification.

---

## 3. Project Progress

### Merged/Closed PRs Today (9 total, notable items)

| PR | Author | Summary | Impact |
|:---|:---|:---|:---|
| [#30671](https://github.com/NousResearch/hermes-agent/pull/30671) | 125938899 | **CLOSED** — Full Chinese (Simplified) dashboard translation (5794 insertions) | Withdrawn in favor of smaller scoped PR |
| [#30672](https://github.com/NousResearch/hermes-agent/pull/30672) | 125938899 | **OPEN** — Narrowed Chinese translation (achievements/kanban/logs only, 232 insertions) | i18n momentum continues; maintainer preference for incremental PRs |
| [#30664](https://github.com/NousResearch/hermes-agent/pull/30664) | HushUr2Pups8008 | **CLOSED** — Harden scratch workspace cleanup (security) | Prevents path traversal in kanban; merged quickly (P1 security) |
| [#30665](https://github.com/NousResearch/hermes-agent/pull/30665) | orlandoburli | **CLOSED** — `kanban.default_workspace` config option | Superseded by [#30668](https://github.com/NousResearch/hermes-agent/pull/30668) |
| [#24661](https://github.com/NousResearch/hermes-agent/pull/24661) | briandevans | **CLOSED** — Bridge `gateway_restart_notification` from config.yaml | Fixes long-standing config wiring bug |

### Active Development Areas
- **Gateway hardening**: Identity guards, HTTP client lifecycle, session key consistency
- **Cross-platform computer use**: Windows support via `cua-driver-rs` ([#30660](https://github.com/NousResearch/hermes-agent/pull/30660))
- **Skill system optimization**: Deterministic runtime bundles with L1 compression ([#30663](https://github.com/NousResearch/hermes-agent/pull/30663))

---

## 4. Community Hot Topics

### Most Active Issues by Engagement

| Issue | Comments | 👍 | Topic | Underlying Need |
|:---|:---|:---|:---|:---|
| [#7237](https://github.com/NousResearch/hermes-agent/issues/7237) **CLOSED** | 33 | 4 | Response truncation on output length | **Core reliability**: Users need predictable long-form generation for production use |
| [#15602](https://github.com/NousResearch/hermes-agent/issues/15602) | 4 | 9 | Google Workspace multi-account | **Professional use cases**: Power users managing multiple identities/work contexts |
| [#19471](https://github.com/NousResearch/hermes-agent/issues/19471) | 4 | 0 | Gateway crash loop after SIGTERM→SIGKILL | **Production stability**: Event loop lifecycle management under process supervisors |
| [#5254](https://github.com/NousResearch/hermes-agent/issues/5254) | 3 | 0 | Tool call repetition with LM Studio | **Local model compatibility**: Fragmented tool calling in non-OpenAI endpoints |
| [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) | 3 | 6 | Cloud sync for all configurations | **Multi-device workflows**: Configuration portability across workstations |

### Analysis
The 33-comment [#7237](https://github.com/NousResearch/hermes-agent/issues/7237) closure indicates **output length management** remains a critical pain point despite resolution—likely the fix needs validation. High 👍 on multi-account and cloud-sync features reveals user base maturation beyond single-machine hobbyist use.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR | Description |
|:---|:---|:---|:---|:---|
| **P1** | [#30636](https://github.com/NousResearch/hermes-agent/issues/30636) | OPEN | None | `state.db` corruption from SIGTERM during launchd shutdown under high load |
| **P1** | [#19471](https://github.com/NousResearch/hermes-agent/issues/19471) | OPEN | None | `--profile` gateway crash loop: event loop lost on restart |
| **P1** | [#30623](https://github.com/NousResearch/hermes-agent/issues/30623) | OPEN | None | `hermes -z` oneshot exits 0 silently before API call when stdout is non-TTY |
| **P2** | [#30653](https://github.com/NousResearch/hermes-agent/issues/30653) | OPEN | None | Model picker ignores `key_env` on custom providers → "0 models listed" |
| **P2** | [#23975](https://github.com/NousResearch/hermes-agent/issues/23975) | OPEN | None | Context compression interrupted by gateway messages |
| **P2** | [#18362](https://github.com/NousResearch/hermes-agent/issues/18362) | OPEN | [#18366](https://github.com/NousResearch/hermes-agent/pull/18366) | `/busy` command CLI-only despite onboarding hints |
| **P2** | [#30626](https://github.com/NousResearch/hermes-agent/issues/30626) | OPEN | None | Gateway profile-blind: ignores live profile switches |
| **P2** | [#30586](https://github.com/NousResearch/hermes-agent/issues/30586) | OPEN | None | macOS launchd hardcodes `gui/` domain, breaks SSH/non-console users |
| **P2** | [#26358](https://github.com/NousResearch/hermes-agent/pull/26358) | OPEN | **PR available** | HTTP clients not released on shutdown, subagents block 12+ min |

### Critical Concerns
- **Three P1 bugs with no fix PRs** — all involve process lifecycle (SIGTERM handling, event loops, TTY detection). These are classic production deployment issues.
- **macOS platform debt**: Both [#30636](https://github.com/NousResearch/hermes-agent/issues/30636) and [#30586](https://github.com/NousResearch/hermes-agent/issues/30586) indicate launchd/daemonization assumptions need overhaul.
- **Gateway reliability gap**: Profile switching, session consistency, and graceful shutdown all have active bugs.

---

## 6. Feature Requests & Roadmap Signals

| Feature | Issue/PR | 👍 | Maturity Signal | v0.15.0 Likelihood |
|:---|:---|:---|:---|:---|
| Microsoft 365/Outlook skill | [#25979](https://github.com/NousResearch/hermes-agent/issues/25979) | 0 | Working implementation offered by author | **High** — fills Google Workspace parity gap |
| XMPP + OMEMO encryption | [#2988](https://github.com/NousResearch/hermes-agent/issues/2988) | 7 | Long-standing, aligns with self-hosting ethos | **Medium** — security-focused, but niche |
| Dynamic model routing | [#30652](https://github.com/NousResearch/hermes-agent/issues/30652) | 0 | Fresh request, no implementation | **Medium** — cost optimization trend |
| Cloud/cross-device sync | [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) | 6 | Strong demand, complex security implications | **Low-Medium** — likely external plugin first |
| Cursor SDK integration | [#30640](https://github.com/NousResearch/hermes-agent/issues/30640) | 0 | RFC with two-phase approach | **Medium** — coding assistant convergence |
| OpenRouter STT provider | [#24415](https://github.com/NousResearch/hermes-agent/issues/24415) | 1 | Straightforward provider extension | **High** — follows existing pattern |
| Profile isolation (Docker) | [#30585](https://github.com/NousResearch/hermes-agent/issues/30585) | 0 | Security/compliance need | **Medium** — infrastructure-heavy |

### Prediction
**v0.15.0** will likely emphasize: (1) **gateway productionization** (fixes over features), (2) **Microsoft ecosystem parity** (Outlook skill), and (3) **model provider flexibility** (OpenRouter STT, dynamic routing). The Cursor SDK RFC could be a dark horse if coding-agent market pressure intensifies.

---

## 7. User Feedback Summary

### Pain Points (Explicit Complaints)
| Theme | Evidence | Severity |
|:---|:---|:---|
| **Silent failures** | [#30623](https://github.com/NousResearch/hermes-agent/issues/30623) (zero output, exit 0), [#30601](https://github.com/NousResearch/hermes-agent/issues/30601) (dropped MCP resources) | High — breaks automation trust |
| **Gateway "ghost" behavior** | [#28208](https://github.com/NousResearch/hermes-agent/issues/28208)/[#18848](https://github.com/NousResearch/hermes-agent/issues/18848) (unwanted WhatsApp replies), [#18362](https://github.com/NousResearch/hermes-agent/issues/18362) (missing /busy) | High — social/operational risk |
| **Configuration fragility** | [#30626](https://github.com/NousResearch/hermes-agent/issues/30626) (profile blindness), [#30653](https://github.com/NousResearch/hermes-agent/issues/30653) (env var loading order) | Medium — power user friction |
| **Local model incompatibility** | [#5254](https://github.com/NousResearch/hermes-agent/issues/5254) (LM Studio tool repetition) | Medium — vendor lock-in concern |

### Positive Signals
- **Strong i18n contribution**: Two Chinese translation PRs in 24h indicates global adoption
- **Production deployment attempts**: launchd, systemd, Docker, SSH/cron usage all reported
- **Skill ecosystem growth**: Three new skill proposals (Outlook, Cursor, Windows computer use) in one week

### Satisfaction/Dissatisfaction Ratio
**Mixed-to-concerned**. Users are heavily invested (building skills, translating, deploying to production) but encountering **basic reliability blockers** at the deployment boundary. The gap between "works on my machine" and "works in production" is the dominant theme.

---

## 8. Backlog Watch

### Issues Needing Maintainer Attention (>2 weeks old, high impact)

| Issue | Age | Priority | Risk if Ignored |
|:---|:---|:---|:---|
| [#15602](https://github.com/NousResearch/hermes-agent/issues/15602) Google Workspace multi-account | 4 weeks | P3 | **User attrition**: 9 👍, clear workaround pain |
| [#5254](https://github.com/NousResearch/hermes-agent/issues/5254) LM Studio tool repetition | 7 weeks | unlabeled | **Local model ecosystem**: Blocks non-API users |
| [#2988](https://github.com/NousResearch/hermes-agent/issues/2988) XMPP/OMEMO | 9 weeks | unlabeled | **Values alignment**: Privacy community credibility |
| [#22110](https://github.com/NousResearch/hermes-agent/issues/22110) `hermes mcp serve` on NixOS | 2 weeks | P2 | **Platform support**: NixOS community blocked |
| [#20660](https://github.com/NousResearch/hermes-agent/pull/20660) Native per-OS computer use | 2+ weeks | P3 | **Cross-platform parity**: Large PR, needs review |

### PRs at Risk of Stagnation

| PR | Age | Blocker |
|:---|:---|:---|
| [#27437](https://github.com/NousResearch/hermes-agent/pull/27437) Docker multi-stage build (5.6GB→2GB) | 6 days | Performance win, needs infra review |
| [#29302](https://github.com/NousResearch/hermes-agent/pull/29302) API server session controls | 3 days | Gateway architecture review |
| [#20660](https://github.com/NousResearch/hermes-agent/pull/20660) Per-OS computer use | 2+ weeks | Large surface area, needs platform testing |

### Recommendation
Maintainers should prioritize **P1 bug triage** (3 unassigned) and **gateway infrastructure review** to prevent production user churn. The [#27437](https://github.com/NousResearch/hermes-agent/pull/27437) Docker improvement is a quick win for CI/CD costs and startup latency.

---

*Digest generated from GitHub activity 2026-05-22 to 2026-05-23. All links: https://github.com/nousresearch/hermes-agent*

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-05-23

## 1. Today's Overview

PicoClaw shows **moderate-to-high activity** with 30 items updated in the last 24 hours (10 issues, 20 PRs), indicating an active development cycle. The project released a new nightly build (`v0.2.8-nightly.20260522.5bbebb5f`), suggesting steady iteration toward the next patch release. Notably, **7 of 10 issues were closed**, demonstrating effective backlog triage—though 5 were marked `stale`, indicating automated cleanup rather than active resolution. Open PRs outnumber merged ones (8 vs. 12), with several substantial feature PRs awaiting review. The community is pushing toward richer channel integrations (Telegram media, Matrix fixes), agent-to-agent communication, and provider compatibility improvements.

---

## 2. Releases

| Version | Type | Notes |
|---------|------|-------|
| [`v0.2.8-nightly.20260522.5bbebb5f`](https://github.com/sipeed/picoclaw/compare/v0.2.8...main) | Nightly | Automated build from `main`; may be unstable. No manual changelog provided. Full diff available [here](https://github.com/sipeed/picoclaw/compare/v0.2.8...main). |

**Assessment:** No stable release this cycle. The nightly suggests v0.2.9 may be approaching, but users should exercise caution with this build.

---

## 3. Project Progress

### Merged/Closed PRs (12 total)

| PR | Author | Summary | Impact |
|----|--------|---------|--------|
| [#2930](https://github.com/sipeed/picoclaw/pull/2930) | lc6464 | Security: bump `golang.org/x/net` to v0.55.0 | Fixes `govulncheck` findings in HTML-to-Markdown path |
| [#2788](https://github.com/sipeed/picoclaw/pull/2788) | LiusCraft | **feat(session): per-message `created_at` timestamps** | Closes [#2787](https://github.com/sipeed/picoclaw/issues/2787); enables accurate message timelines in UI |
| [#2914](https://github.com/sipeed/picoclaw/pull/2914) | lxowalle | **feat: request-scoped context policies via `turn_profile`** | Major: allows per-turn control of history, system context, skills, tools |
| [#2827](https://github.com/sipeed/picoclaw/pull/2827) | Ashid332 | Fix Matrix `allow_from` filter parsing of `@`-prefixed MXIDs | Closes [#2815](https://github.com/sipeed/picoclaw/issues/2815) |
| [#2822](https://github.com/sipeed/picoclaw/pull/2822) | bogdanovich | Fix child tool feedback dismissal after sync subturn | Improves subagent UX cleanliness |
| [#2814](https://github.com/sipeed/picoclaw/pull/2814) | bogdanovich | Fix `exec` sandbox misclassifying relative script paths | Security/stability fix for path traversal guard |
| [#2794](https://github.com/sipeed/picoclaw/pull/2794) | bogdanovich | Preserve origin context for async follow-ups | Fixes routing context loss in async tool callbacks |
| [#2791](https://github.com/sipeed/picoclaw/pull/2791) | bogdanovich | Preserve Telegram topic context for final replies | Fixes forum topic reply routing |
| [#2789](https://github.com/sipeed/picoclaw/pull/2789) | bogdanovich | Configurable tool feedback edit throttling | Adds `animation_interval_secs` setting |
| [#2756](https://github.com/sipeed/picoclaw/pull/2756) | bogdanovich | Telegram topic context preservation (earlier iteration) | Superseded by #2791 |
| [#2921](https://github.com/sipeed/picoclaw/pull/2921) | dependabot | Bump `gronx` 1.19.7 → 1.20.0 | Cron scheduling library update |
| [#2923](https://github.com/sipeed/picoclaw/pull/2923) | dependabot | Bump `line-bot-sdk-go` 8.19.0 → 8.20.0 | LINE channel SDK update |

**Key Advances:**
- **Session API maturity:** Per-message timestamps land, unblocking frontend accuracy
- **Telegram ecosystem hardening:** 3 PRs from bogdanovich systematically fix topic/thread context propagation
- **Agent control granularity:** `turn_profile` enables sophisticated multi-agent orchestration
- **Security maintenance:** Dependency bumps address known vulnerabilities

---

## 4. Community Hot Topics

### Most Active Discussions

| Rank | Item | Comments | Engagement | Underlying Need |
|------|------|----------|------------|---------------|
| 1 | [#2625](https://github.com/sipeed/picoclaw/issues/2625) WhatsApp support in arm64 builds | 6 | 👍 1 | **Embedded/IoT deployment friction**: Raspberry Pi Zero 2 users need out-of-box WhatsApp without manual compilation |
| 2 | [#2785](https://github.com/sipeed/picoclaw/issues/2785) Feishu notification center tool display | 3 | 0 | Enterprise messaging UX polish for Lark/Feishu users |
| 3 | [#2744](https://github.com/sipeed/picoclaw/issues/2744) Android data access failure | 3 | 0 | **Mobile/Termux reliability**: Android as first-class platform |

### Emerging High-Interest PRs

| PR | Focus | Why It Matters |
|----|-------|--------------|
| [#2929](https://github.com/sipeed/picoclaw/issues/2929) | Agent-to-agent peer communication | Fills architectural gap between `spawn`/`delegate` (hierarchical) and true cooperative multi-agent patterns |
| [#2856](https://github.com/sipeed/picoclaw/pull/2856) | Media attachments in `message` tool | Unifies file+text delivery; reduces agent complexity |
| [#2838](https://github.com/sipeed/picoclaw/pull/2838) | Frontmatter tool policy filters | Enables fine-grained capability control per-agent via `AGENT.md` |

**Community Signal:** Strong demand for **deployment simplicity** (pre-built binaries with all channel support) and **enterprise messaging polish** (Feishu, Telegram topics, Matrix). The agent-to-agent communication issue (#2929) represents a strategic architectural evolution.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR | Details |
|----------|-------|--------|--------|---------|
| 🔴 **High** | [#2817](https://github.com/sipeed/picoclaw/issues/2817) Voice transcription not passed to LLM | **CLOSED (stale)** | None merged | Groq Whisper succeeds but LLM receives `[voice]` placeholder; **regression risk** if stale-closed without fix |
| 🔴 **High** | [#2744](https://github.com/sipeed/picoclaw/issues/2744) Android v0.2.8 data access failure | **CLOSED (stale)** | None | Complete data inaccessibility on Android; unclear if actually fixed |
| 🟡 **Medium** | [#2815](https://github.com/sipeed/picoclaw/issues/2815) Matrix `allow_from` filter broken | **CLOSED** | [#2827](https://github.com/sipeed/picoclaw/pull/2827) ✅ | Any non-empty allowlist blocked all messages; **fixed** |
| 🟡 **Medium** | [#2816](https://github.com/sipeed/picoclaw/issues/2816) Matrix sender identity missing | **CLOSED (stale)** | None | Agent lacks sender context vs. Telegram's `chat_id`; **gap remains** |
| 🟡 **Medium** | [#2787](https://github.com/sipeed/picoclaw/issues/2787) Session messages lack timestamps | **CLOSED** | [#2788](https://github.com/sipeed/picoclaw/pull/2788) ✅ | Frontend accuracy issue; **fixed** |
| 🟢 **Low** | [#2785](https://github.com/sipeed/picoclaw/issues/2785) Feishu notification display | **CLOSED (stale)** | None | UI polish; `separate_messages=false` interaction |

**Stability Assessment:** Concerning pattern of **stale-closing critical bugs** (#2817 voice, #2744 Android) without verified fixes. The voice transcription bug is particularly severe—breaks a core user interaction path. Recommend maintainers verify these before v0.2.9 release.

---

## 6. Feature Requests & Roadmap Signals

| Feature | Issue/PR | Likelihood in v0.2.9 | Rationale |
|---------|----------|----------------------|-----------|
| **Compiled builds with WhatsApp** | [#2625](https://github.com/sipeed/picoclaw/issues/2625) | Medium | Build system change; blocked by licensing/complexity? Long-open (1 month) |
| **Agent-to-agent peer comms** | [#2929](https://github.com/sipeed/picoclaw/issues/2929) | Low-Medium | Architectural; needs design consensus. Just opened. |
| **Media attachments in `message`** | [#2856](https://github.com/sipeed/picoclaw/pull/2856) | **High** | PR open, well-scoped, closes #2855 |
| **Tool policy filters in frontmatter** | [#2838](https://github.com/sipeed/picoclaw/pull/2838) | **High** | PR open, completes AGENT.md governance model |
| **DeepSeek thinking controls** | [#2928](https://github.com/sipeed/picoclaw/pull/2928) | **High** | Provider parity; small, targeted change |
| **Message bus backpressure** | [#2906](https://github.com/sipeed/picoclaw/pull/2906) | Medium | Infrastructure; addresses goroutine leak under load |
| **Tirith security scanning** | [#2877](https://github.com/sipeed/picoclaw/pull/2877) | Medium | Optional security layer; needs review bandwidth |

**Predicted v0.2.9 contents:** Media attachments, tool policy filters, DeepSeek thinking, per-message timestamps (already merged), plus Telegram/Matrix context fixes.

---

## 7. User Feedback Summary

### Pain Points

| Theme | Evidence | Severity |
|-------|----------|----------|
| **Build complexity for embedded** | [#2625](https://github.com/sipeed/picoclaw/issues/2625) Pi Zero 2 + WhatsApp manual compilation | High |
| **Android as neglected platform** | [#2744](https://github.com/sipeed/picoclaw/issues/2744) complete data failure | High |
| **Voice interaction reliability** | [#2817](https://github.com/sipeed/picoclaw/issues/2817) transcription succeeds but silently fails downstream | Critical |
| **Matrix as second-class channel** | [#2815](https://github.com/sipeed/picoclaw/issues/2815), [#2816](https://github.com/sipeed/picoclaw/issues/2816) filter broken, no sender identity | Medium |
| **Enterprise messaging polish** | [#2785](https://github.com/sipeed/picoclaw/issues/2785) Feishu notifications | Medium |

### Positive Signals

- **Multi-agent architecture maturing:** Users actively using `spawn`/`subagent`/`delegate`, now requesting peer-to-peer layer ([#2929](https://github.com/sipeed/picoclaw/issues/2929))
- **Frontend API improvements:** Timestamp fix (#2788) shows responsiveness to UI developer needs
- **Security consciousness:** Tirith integration PR (#2877) indicates operational security awareness

---

## 8. Backlog Watch

### Issues/PRs Needing Maintainer Attention

| Item | Age | Risk | Action Needed |
|------|-----|------|---------------|
| [#2625](https://github.com/sipeed/picoclaw/issues/2625) WhatsApp arm64 builds | 31 days | User attrition on embedded | Decision: include in CI or document workaround? |
| [#2351](https://github.com/sipeed/picoclaw/issues/2351) Validate skill binary requirements | 47 days | LLM hallucinates capabilities | Design review: pre-flight check architecture |
| [#2662](https://github.com/sipeed/picoclaw/pull/2662) Unify providers documentation | 29 days | Documentation debt | Simple docs PR; low risk to merge |
| [#2877](https://github.com/sipeed/picoclaw/pull/2877) Tirith pre-exec scanning | 7 days | Security feature stalled | Review for optional integration pattern |
| [#2906](https://github.com/sipeed/picoclaw/pull/2906) Message bus backpressure | 2 days | Production stability | Performance review needed |
| [#2929](https://github.com/sipeed/picoclaw/issues/2929) Agent-to-agent comms | 1 day | Strategic direction | RFC or design discussion |

### Concern: Stale-Bot Impact

5 issues closed as `stale` today, including 2 high-severity bugs (#2817 voice, #2744 Android). Recommend:
- Exempt `type: bug` from stale automation, OR
- Require maintainer triage before stale closure

---

**Overall Project Health:** 🟡 **Caution-Positive**

- ✅ Strong feature velocity (tool policies, media, timestamps, context fixes)
- ✅ Active dependency maintenance
- ⚠️ Risk of bug debt accumulation via stale-closure without verification
- ⚠️ Embedded/mobile platform support gaps widening
- 🔮 v0.2.9 shaping as significant polish release if open PRs land

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw Project Digest — 2026-05-23

## 1. Today's Overview

NanoClaw saw **exceptionally high activity** in the past 24 hours with **31 PRs updated** (28 merged/closed, 3 open) and **6 issues** (4 open, 2 closed). The project demonstrates strong maintainer velocity with zero release backlog and rapid turnaround on critical fixes. However, **four new open issues** all surfaced within hours of each other, suggesting either a recent regression wave or users hitting previously untested paths—particularly around the Apple Container skill and local development workflows. The project appears healthy in merge throughput but may need focused stabilization on container runtime edge cases and developer experience.

---

## 2. Releases

**No new releases** (v0.0.0 or no tagged versions).

---

## 3. Project Progress

### Merged/Closed PRs (28 total — highlights by impact)

| PR | Author | Description | Link |
|:---|:---|:---|:---|
| **#2580** | chiptoe-svg | **Full Codex-only installation support** — Codex as AI-coding CLI, sole agent provider, OneCLI credential management; skill catalog and persona parity with Claude Code | [PR #2580](https://github.com/nanocoai/nanoclaw/pull/2580) |
| **#2586** | IamAdamJowett | **Session transcript rotation** — prevents unbounded growth of `projects/<cwd>/<session>.jsonl` that blocked agent `Read` on long-lived sessions | [PR #2586](https://github.com/nanocoai/nanoclaw/pull/2586) |
| **#2573** | matt1995ai | **Context-window introspection** — surfaces usage stats to agents so they can pace work against token budget | [PR #2573](https://github.com/nanocoai/nanoclaw/pull/2573) |
| **#2556** | IamAdamJowett | **Fix `<messages>` envelope bug** — resolves synthetic "No response requested." from Claude Agent SDK when batching 2+ messages | [PR #2556](https://github.com/nanocoai/nanoclaw/pull/2556) |
| **#2552** | IamAdamJowett | **WhatsApp mentions + shutdown race fix** — `@<phone>` mentions now render as tags; prevents credential wipe on shutdown race | [PR #2552](https://github.com/nanocoai/nanoclaw/pull/2552) |
| **#2553** | IamAdamJowett | **WhatsApp formatting skill** — agents now use protocol-correct `@<phone-digits>` syntax | [PR #2553](https://github.com/nanocoai/nanoclaw/pull/2553) |
| **#2584** | snymanpaul | **Signal-cli 0.13+ compatibility** — reads `number` field instead of deprecated `account` | [PR #2584](https://github.com/nanocoai/nanoclaw/pull/2584) |
| **#2579** | cfis | **WhatsApp 401 logout handling** — clears dead credentials immediately to prevent retry loops | [PR #2579](https://github.com/nanocoai/nanoclaw/pull/2579) |
| **#2572** | bromleymindfulness | **Rootless Podman support** — fixes dual gotchas with `--user` mapping and bind mount permissions | [PR #2572](https://github.com/nanocoai/nanoclaw/pull/2572) |
| **#2566** | Hinotoi-agent | **Security: scoped channel approvals** — prevents privilege escalation where scoped admins could connect channels to unauthorized groups | [PR #2566](https://github.com/nanocoai/nanoclaw/pull/2566) |
| **#2567** | floflo11 | **Fix `CLAUDE.local.md` import** — per-group memory now reaches agents (was documented as working but never wired) | [PR #2567](https://github.com/nanocoai/nanoclaw/pull/2567) |
| **#2571** | ira-at-work | **RTK skill** — 60–90% token savings on dev commands via CLI proxy integration | [PR #2571](https://github.com/nanocoai/nanoclaw/pull/2571) |
| **#2593** | sumsumai | **Default agent shared session mode** | [PR #2593](https://github.com/nanocoai/nanoclaw/pull/2593) |
| **#2578** | sumsumai | **Telegram claim link feature** | [PR #2578](https://github.com/nanocoai/nanoclaw/pull/2578) |

**Infrastructure/Setup fixes:** #2551 (WhatsApp auth CLI), #2557 (setup splash removal), #2558 (OneCLI URL subdomain), #2563 (scoped `--assistant-name`), #2592 (Teams CLI docs)

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|:---|:---|:---|
| **#2588** — `skill/apple-container` branch out of sync with mainline | **Critical path blocker** — opened 2026-05-22, zero comments, but fundamental breakage | The `/convert-to-apple-container` skill is **completely non-functional**. Root cause: branch references extinct APIs, missing modules, and assumes Node+tsc instead of bun. Indicates either (a) Apple Container was deprioritized during bun migration, or (b) no CI tests skill branches. **Need:** Dedicated maintainer review or archival decision. [Issue #2588](https://github.com/nanocoai/nanoclaw/issues/2588) |
| **#2589** — `host.docker.internal` unresolvable in Apple Container | Companion to #2588 — network layer mismatch with Apple Container runtime | Reveals architectural assumption that Docker Desktop networking works everywhere. Apple Container lacks `--add-host` support. **Need:** Platform-agnostic proxy discovery or documented workaround. [Issue #2589](https://github.com/nanocoai/nanoclaw/issues/2589) |
| **#2590** — "I just hate Node apps" — dependency hell debugging locally | Emotional/urgent tone, Node 22 + SQLite wrapper conflicts | Classic DX friction: container-first design makes bare-metal debugging painful. User bounced between Node versions for native module compilation (`node-gyp`). **Underlying need:** Better documented host-dev path or devcontainer/VS Code extension. [Issue #2590](https://github.com/nanocoai/nanoclaw/issues/2590) |

**Notable pattern:** Three of four open issues cluster around **Apple Container** (2 issues) and **local development friction** (1 issue), suggesting the project's "works in container" abstraction is leaking at the edges.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR | Details |
|:---|:---|:---|:---|:---|
| **🔴 Critical** | #2588 — Apple Container skill completely broken | **OPEN** | None | Branch bitrot; skill fails immediately. No assignee. |
| **🔴 Critical** | #2589 — `host.docker.internal` DNS failure in Apple Container | **OPEN** | None | Blocks all agent network egress on Apple Container. Depends on #2588 resolution. |
| **🟡 High** | #2587 — Stale `npm run build` in Apple Container Dockerfile | **OPEN** | None | Build fails due to bun migration; trivial fix but unmerged. |
| **🟡 High** | #2555 — `<messages>` envelope caused synthetic SDK responses | **CLOSED** | #2556 | Fixed: batch envelope removed, SDK now calls API correctly. |
| **🟡 High** | #2581 — Signal-cli 0.13+ JSON field mismatch | **CLOSED** | #2584 | Fixed: now reads `number` field. |
| **🟢 Medium** | #2590 — Node dependency hell for local debugging | **OPEN** | None | DX issue; no crash but blocks contributors. |

**Stability assessment:** Core agent-runner and channel adapters (WhatsApp, Signal) are actively maintained with fast fixes. **Apple Container skill is unmaintained and should be considered deprecated until explicitly revived.**

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Release |
|:---|:---|:---|
| **Apple Container resurrection or removal** | #2587, #2588, #2589 | **High** — must resolve triad |
| **Better bare-metal / local dev support** | #2590 | **Medium** — may be docs-only |
| **Codex as first-class provider** | #2580 merged | **Shipped** — now supported |
| **Context window budgeting tools** | #2573 merged | **Shipped** |
| **Token-saving dev tool integrations** | #2571 (RTK) merged | **Shipped** |
| **Telegram claim flows** | #2578, #2593 merged | **Shipped** |
| **Multi-channel transcript enrichment** | #2521 open | **Medium** — low comment activity, clear use case |

**Emerging theme:** "Agent self-awareness" (#2573 context window, #2586 transcript rotation) suggests roadmap toward longer-lived, more autonomous agents that manage their own resource constraints.

---

## 7. User Feedback Summary

### Pain Points
| Issue | User Voice | Systemic Problem |
|:---|:---|:---|
| #2590 | *"I just hate Node apps...missing dependencies hell"* | Container-first abstraction excludes Node-averse developers; native module compilation (`node-gyp`, SQLite) is fragile across Node versions |
| #2588-2589 | (implied by rapid filing) | Apple Container skill was marketed/documented but not maintained through bun migration |

### Positive Signals
- **WhatsApp reliability improving rapidly**: #2552, #2553, #2579, #2551 show concentrated investment
- **Provider flexibility**: Codex-only path (#2580) reduces vendor lock-in concern
- **Security consciousness**: #2566 scoped approvals shows mature access control thinking

### Satisfaction/Dissatisfaction Ratio
- **Satisfied**: Users getting fixes for WhatsApp, Signal, Podman, context window (fast turnaround)
- **Dissatisfied**: Apple Container users (complete breakage), local developers (toolchain friction)

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed |
|:---|:---|:---|:---|
| **#2521** — Add `from-channel`/`from-type` to XML attributes | 6 days open | **Stagnation** | Small, well-scoped PR with clear use case. Needs maintainer review. [PR #2521](https://github.com/nanocoai/nanoclaw/pull/2521) |
| **#2588** — Apple Container branch out of sync | 1 day open, but **pre-existing bitrot** | **Reputational** | Decide: archive skill, or assign owner for rewrite. Currently misleading in docs. |
| **#2587** — Stale `npm run build` | 1 day open | **Quick win** | One-line fix; should be mergeable immediately if branch is kept. |

**Maintainer attention priority:**
1. **#2588** — Decision required: Apple Container fate
2. **#2521** — Community PR, low risk, should not languish
3. **#2587** — Trivial fix, batch with any Apple Container work

---

*Digest generated from 31 PRs and 6 issues updated 2026-05-22 to 2026-05-23.*

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw Project Digest — 2026-05-23

---

## 1. Today's Overview

NullClaw shows **moderate development velocity** with four active pull requests all receiving recent updates on 2026-05-22, indicating sustained contributor engagement despite no new releases or issue activity in the past 24 hours. The project appears to be in a **consolidation phase**—no critical bugs were reported, no releases cut, and all visible work is additive or corrective engineering rather than disruptive refactoring. The contributor base is concentrated: two PRs from `vernonstinebaker` (infrastructure/stability fixes), one from `yanggf8` (major cron subsystem), and one from `PierreLeGuen` (new cloud provider integration). Zero open issues suggests either effective issue triage or potentially underreported user problems. Overall project health reads as **stable but release-pending**—the accumulated PRs likely warrant a version bump once reviewed.

---

## 2. Releases

**No new releases** in the past 24 hours. The latest release remains unspecified in available data.

---

## 3. Project Progress

**No PRs were merged or closed today.** All four active PRs remain open with recent activity:

| PR | Status | Progress Assessment |
|---|---|---|
| [#783](https://github.com/nullclaw/nullclaw/pull/783) Cron subagent | Open, updated 2026-05-22 | Feature-complete implementation awaiting review; substantial scope (DB schema, worker queue, CLI, security hardening) suggests lengthy review cycle |
| [#922](https://github.com/nullclaw/nullclaw/pull/922) NEAR AI Cloud provider | Open, updated 2026-05-22 | Recently submitted (2026-05-21); full provider integration with model catalog parsing; likely targeting next release |
| [#891](https://github.com/nullclaw/nullclaw/pull/891) Curl probe transport failures | Open, updated 2026-05-22 | Diagnostic precision fix; ready for merge pending maintainer review |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) POSIX nanosleep | Open, updated 2026-05-22 | Low-level correctness fix; addresses scheduler behavior discrepancy |

**No features advanced to completion today.** The cron subagent PR (#783) represents the largest latent capability increase but has been open since 2026-04-07 (46 days), suggesting either review bandwidth constraints or architectural deliberation.

---

## 4. Community Hot Topics

**No commented or reacted items exist**—all four PRs show `👍: 0` and `Comments: undefined`. This indicates:

- **Low community engagement** with in-flight work, or
- **Early-stage review** occurring outside GitHub (Discord, internal channels), or
- **Contributor-driven development** without broad user visibility

**Most significant by scope:** [#783 Cron subagent](https://github.com/nullclaw/nullclaw/pull/783) — introduces entirely new subsystem for scheduled execution. Underlying need: users require reliable, observable background job execution with timezone awareness and security boundaries.

**Most significant by ecosystem expansion:** [#922 NEAR AI Cloud](https://github.com/nullclaw/nullclaw/pull/922) — adds decentralized AI infrastructure option. Underlying need: diversification beyond centralized providers, alignment with NEAR blockchain ecosystem.

---

## 5. Bugs & Stability

**No new bug reports today.** Two stability-oriented PRs are in flight:

| Severity | Item | Description | Fix Status |
|---|---|---|---|
| Medium | [#891](https://github.com/nullclaw/nullclaw/pull/891) | Provider health probes collapsing distinct curl transport errors into generic failures, impairing operational diagnostics | **Fix PR open**, awaiting review |
| Medium | [#878](https://github.com/nullclaw/nullclaw/pull/878) | `thread.sleep()` using cooperative yield instead of actual OS suspension on POSIX, causing unpredictable scheduling in managed runtime | **Fix PR open**, awaiting review |

Both fixes are **correctness issues rather than crashes**—no data loss or security vulnerabilities indicated. The nanosleep fix (#878) may affect production workloads with strict timing requirements.

---

## 6. Feature Requests & Roadmap Signals

**No explicit user feature requests** in today's data. Inferred roadmap signals from active PRs:

| Feature | Source | Likelihood in Next Release | Rationale |
|---|---|---|---|
| **Cron/scheduled job execution** | [#783](https://github.com/nullclaw/nullclaw/pull/783) | High | Long-running PR, comprehensive implementation, fills major capability gap |
| **NEAR AI Cloud provider** | [#922](https://github.com/nullclaw/nullclaw/pull/922) | Moderate-High | Clean provider addition pattern, but depends on maintainer priority |
| **Enhanced provider diagnostics** | [#891](https://github.com/nullclaw/nullclaw/pull/891) | High | Low-risk fix, improves operability |
| **POSIX scheduling correctness** | [#878](https://github.com/nullclaw/nullclaw/pull/878) | Moderate | Platform-specific, may be bundled with other fixes |

**Predicted next version focus:** Infrastructure reliability (cron, scheduling, diagnostics) over user-facing features.

---

## 7. User Feedback Summary

**No direct user feedback captured today.** Inferred patterns:

| Pain Point | Evidence | Satisfaction Indicator |
|---|---|---|
| Need for scheduled/background execution | Existence of #783 | Neutral-to-positive (being addressed) |
| Provider ecosystem fragmentation | #922 adding NEAR AI | Neutral (expanding options) |
| Operational debuggability | #891 fixing error classification | Negative (was poor, improving) |
| Cross-platform behavior consistency | #878 POSIX fix | Negative (was incorrect, improving) |

**No dissatisfaction signals** in public channels, but zero issues may also indicate **low adoption** or **alternative support channels**.

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed |
|---|---|---|---|
| [#783](https://github.com/nullclaw/nullclaw/pull/783) Cron subagent | **46 days open** | **High** — large feature PR aging, risk of merge conflicts, contributor fatigue | Maintainer architectural review; consider splitting into smaller PRs (schema, worker, CLI, security) |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) nanosleep | 23 days open | Moderate — correct but narrow; may be deprioritized | Simple review, should merge or request changes |
| [#891](https://github.com/nullclaw/nullclaw/pull/891) curl probe | 18 days open | Low-Moderate | Straightforward review |

**Critical concern:** [#783](https://github.com/nullclaw/nullclaw/pull/783) represents substantial engineering investment at risk of stalling. No maintainer comments visible. Recommend: explicit maintainer assignment or community call for testing.

---

*Digest generated from GitHub activity 2026-05-22 to 2026-05-23. Data source: nullclaw/nullclaw repository.*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw Project Digest — 2026-05-23

## 1. Today's Overview

IronClaw shows **extremely high development velocity** with 73 total items updated in 24 hours (23 issues, 50 PRs), indicating an active sprint cycle. The project is heavily focused on the **"Reborn" architectural overhaul**, with workstreams spanning auth systems, WebUI surfaces, native extensions, and sandboxing infrastructure. No new releases were cut, suggesting the team is accumulating changes for a larger milestone. The 36:14 open-to-merged PR ratio and 19:4 active-to-closed issue ratio indicate substantial in-flight work that hasn't yet landed. Core contributors (serrrfirat, henrypark133, hanakannzashi, zmanian) are driving parallel workstreams with minimal external contribution, pointing to a tightly controlled core-team phase.

---

## 2. Releases

**No new releases** — none published.

---

## 3. Project Progress

### Merged/Closed PRs Today (14 total, notable items)

| PR | Author | Summary | Significance |
|:---|:---|:---|:---|
| [#3878](https://github.com/nearai/ironclaw/pull/3878) | hanakannzashi | **Product auth composition seam** — `RebornProductAuthServices` as single composition point for auth flows, wired into `build_reborn_services` | **Critical infrastructure**: unifies auth stack for all product surfaces |
| [#3863](https://github.com/nearai/ironclaw/pull/3863) | serrrfirat | **Skill asset access and execution adapter** — final PR in Reborn skills stack, adds scoped bundle reader and execution adapter | **Completes skills foundation** for first-party extension system |
| [#3837](https://github.com/nearai/ironclaw/pull/3837) | henrypark133 | **Google Suite extensions design spec** — 9-capability Calendar + 6-capability Gmail design, introduces `ironclaw_oauth` + `ironclaw_native_extensions` crates | **Roadmap anchor**: enables major native extension vertical |

### Closed Issues Today

| Issue | Author | Resolution |
|:---|:---|:---|
| [#3803](https://github.com/nearai/ironclaw/issues/3803) | serrrfirat | Secrets/egress substrate wired through production tool composition (Lane 3 complete) |
| [#3611](https://github.com/nearai/ironclaw/issues/3611) | serrrfirat | Minimal native WebChat v2 routes implemented |
| [#3626](https://github.com/nearai/ironclaw/issues/3626) | serrrfirat | WebUI caller/thread scope bound to canonical TurnScope |
| [#3625](https://github.com/nearai/ironclaw/issues/3625) | serrrfirat | WebUI idempotency and accepted-message ledger added |

**Key advancement**: The auth stack reached a major integration milestone with #3878, while the skills system (#3863) and WebUI beta infrastructure (#3611, #3625, #3626) are now substantially complete.

---

## 4. Community Hot Topics

### Most Active by Engagement

| Rank | Item | Comments | Analysis |
|:---|:---|:---|:---|
| 1 | [#3702](https://github.com/nearai/ironclaw/issues/3702) Binary-E2E test framework plan | 4 comments | **Deep technical debt concern**: 88 `tests/*.rs` files audited, 29 core agent-loop files classified; team is systematically rebuilding test parity for Reborn. Signals anxiety about regression risk in architecture transition. |
| 2 | [#3803](https://github.com/nearai/ironclaw/issues/3803) *(now closed)* Secrets/egress production wiring | 2 comments | **Infrastructure completion**: Closed after PRs merged; represents Lane 3 of a structured migration. |
| 3 | [#3798](https://github.com/nearai/ironclaw/issues/3798) Subagent spawn design | 2 comments | **Architectural expansion**: Designing subagent orchestration for Reborn loop — indicates ambition toward multi-agent systems beyond single-turn execution. |
| 4 | [#3094](https://github.com/nearai/ironclaw/issues/3094) Approval/auth interaction services | 2 comments | **UX-safety critical**: Bridging blocked run-states to UI-safe flows; foundational for trustworthy agent operation. |

### Underlying Needs Analysis

- **Test confidence**: #3702's 4-comment depth reveals the team is investing heavily in proving Reborn matches legacy behavior before wider rollout
- **Composability**: Multiple "Lane" and "Phase" issues (#3803, #3805, #3806, #3894-#3898) show a methodical, dependency-ordered migration strategy
- **Trust/safety**: Approval/auth services (#3094, #3889, #3891) are receiving sustained attention, suggesting product readiness for user-facing deployment depends on these

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **HIGH** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E failed | Scheduled run failed on `v2-engine` E2E job; commit `030cfeb` | **UNFIXED** — no comments, no linked PR; stale since May 10 |
| **MEDIUM** | [#3875](https://github.com/nearai/ironclaw/issues/3875) Blocking spawn parent recovery gap | Parent doesn't resume after child completion in subagent E2E §5.2; exposed during #3872 draft | **IN PROGRESS** — tracked as integration gap, likely fix in #3872 or follow-up |
| **MEDIUM** | [#3871](https://github.com/nearai/ironclaw/issues/3871) `executor.rs` decomposition | File exceeds architecture size guidelines; subagent additions worsened | **TRACKED** — no active PR, deferred cleanup |

**Stability assessment**: The persistent nightly E2E failure (#3447) is concerning — 12 days without resolution or visible investigation suggests either deprioritization or systemic v2-engine instability. The blocking spawn gap (#3875) is active and contained to draft PR work.

---

## 6. Feature Requests & Roadmap Signals

### User/Contributor Requests (from issue labels and descriptions)

| Feature | Source | Likelihood in Next Release | Rationale |
|:---|:---|:---|:---|
| **Cron/trigger loops** | [#3873](https://github.com/nearai/ironclaw/issues/3873) | **HIGH** | Well-scoped V1 design ("synthetic inbound message"), fits Reborn architecture, no blockers listed |
| **Google Calendar + Gmail native extensions** | [#3837](https://github.com/nearai/ironclaw/pull/3837) design; [#3894](https://github.com/nearai/ironclaw/pull/3894)-[#3898](https://github.com/nearai/ironclaw/pull/3898) phases | **HIGH** | 6-phase PR sequence already in flight (Phases 2-6 open), OAuth substrate landed |
| **GitHub WASM read/write tools** | [#3806](https://github.com/nearai/ironclaw/issues/3806), [#3910](https://github.com/nearai/ironclaw/pull/3910), [#3909](https://github.com/nearai/ironclaw/pull/3909) | **MEDIUM-HIGH** | Read path has test fixture (#3910) and v2 package (#3909); write path pending |
| **Notion MCP capability** | [#3805](https://github.com/nearai/ironclaw/issues/3805) | **MEDIUM** | Blocked on "extension-v2 catalog/runtime baseline and secrets/auth composition lanes" |
| **Safe user-scoped tool installs** | [#3905](https://github.com/nearai/ironclaw/issues/3905) | **MEDIUM** | Clear scoped model exists, but "needs design" for third-party path; infrastructure gap |
| **Local file/MCP bridge for cloud** | [#2117](https://github.com/nearai/ironclaw/issues/2117) | **LOW-MEDIUM** | Long-standing (April 7), size:L, risk:medium; no linked PRs; deprioritized against Reborn |

### Predicted Next Release Contents
- Reborn WebUI Beta (M1-M2 modules nearing completion)
- Google Extensions (Gmail + Calendar) with OAuth
- Hooks framework v1 (#3573) + performance follow-ups (#3911, #3913)
- Budgets/cost controls (#3899)

---

## 7. User Feedback Summary

### Explicit Pain Points from Issues

| Issue | Pain Point | User Impact |
|:---|:---|:---|
| [#2117](https://github.com/nearai/ironclaw/issues/2117) | Cloud-hosted IronClaw cannot access local files | **Blocker for personal knowledge management** (Obsidian vaults, local projects) |
| [#3905](https://github.com/nearai/ironclaw/issues/3905) | No safe path for user-installed third-party tools | **Extensibility limitation** — first-party only is too restrictive |
| [#3447](https://github.com/nearai/ironclaw/issues/3447) | Nightly E2E failing | **Quality signal** — undermines confidence in v2-engine stability |

### Inferred Satisfaction/Dissatisfaction

- **Satisfied**: Core team velocity, architectural clarity (well-documented "Lanes," "Phases," "Steps"), security-conscious design (approval flows, credential isolation)
- **Dissatisfied**: No releases to consume progress, cloud-local gap unaddressed, test flakiness persistent

---

## 8. Backlog Watch

| Issue/PR | Age | Risk | Action Needed |
|:---|:---|:---|:---|
| [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E failed | 13 days | **HIGH** | Investigate v2-engine failure or disable/modify job; silent failures erode trust |
| [#2117](https://github.com/nearai/ironclaw/issues/2117) Local file/MCP bridge | 46 days | **MEDIUM** | Community-requested, no owner assigned; consider "good first issue" or roadmap slot |
| [#3094](https://github.com/nearai/ironclaw/issues/3094) Approval/auth interaction services | 24 days | **MEDIUM** | Partially unblocked by #3878-#3888; needs closure verification |
| [#3573](https://github.com/nearai/ironclaw/pull/3573) Hooks framework | 10 days open | **LOW** | XL PR with active follow-ups (#3911-#3914); monitor for merge readiness |

---

*Digest generated from 73 GitHub items (23 issues, 50 PRs) updated 2026-05-22 to 2026-05-23.*

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI Project Digest — 2026-05-23

## 1. Today's Overview

LobsterAI (NetEase Youdao's AI agent/personal assistant project) showed **exceptionally high development velocity** on 2026-05-22 with **21 PRs updated** (12 merged/closed, 9 open) and **1 new release shipped**. The activity was heavily concentrated around the **subagent system**, indicating this is a major strategic feature launch. Notably, 8 PRs were merged by two core contributors (`btc69m979y-dotcom`, `fisherdaddy`) in a single day, suggesting a coordinated release push. However, community engagement remains low—zero reactions on all visible items and minimal issue activity—indicating either a corporate-driven development model or limited external contributor base. Dependency maintenance PRs from Dependabot are accumulating and going stale, creating potential security/technical debt.

---

## 2. Releases

### [LobsterAI 2026.5.22](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.5.22)

**Major feature release** focused on subagent UX and model configuration flexibility.

| Change | Author | PR |
|--------|--------|-----|
| **Subagent session sidebar display and detail view** | @btc69m979y-dotcom | [#2011](https://github.com/netease-youdao/LobsterAI/pull/2011) |
| **Model custom params + thinking block display** | @btc69m979y-dotcom | [#2019](https://github.com/netease-youdao/LobsterAI/pull/2019) |
| **Cowork engine improvements** (truncated in data) | — | — |

**Breaking changes / Migration notes:** None explicitly documented. The subagent message persistence uses a **new `subagent_messages` SQLite table** with lazy backfill for legacy sessions—users should experience seamless migration.

---

## 3. Project Progress

### Merged/Closed PRs (12 items)

#### Subagent System — Core Feature Launch
| PR | Description | Key Technical Detail |
|----|-------------|-------------------|
| [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034) | Persist subagent session messages to local DB | New `subagent_messages` table; lazy backfill; avoids blocking main thread |
| [#2030](https://github.com/netease-youdao/LobsterAI/pull/2030) | Reuse main conversation rendering pipeline for subagents | Extracted `ConversationTurnsView` component; unified `CoworkMessage` format |
| [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | Fix subagent session bugs | Tool result sync, sidebar highlight state, empty/error handling, spawn error detection |
| [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | Fix subagent sidebar style, duplicate tracking, missing tool results | `toolCallId` as unique DB key (was `agentId` causing collisions) |
| [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) | Fix subagent page sidebar toggle, draggable header, Mac padding | 68px left padding for Mac window controls; draggable header for frameless window |

#### Bug Fixes
| PR | Description | Area |
|----|-------------|------|
| [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | Fix model switch error when custom models | docs, main, openclaw |
| [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | Fix browser config invalid | renderer, main, openclaw |
| [#2035](https://github.com/netease-youdao/LobsterAI/pull/2035) | Fix Qwen coding plan for Qwen 3.6 Plus | docs |

#### Polish & Release
| PR | Description |
|----|-------------|
| [#2038](https://github.com/netease-youdao/LobsterAI/pull/2038) | Release 2026.5.19 — comprehensive release PR covering all above |
| [#2037](https://github.com/netease-youdao/LobsterAI/pull/2037) | Optimize IM-related copywriting |
| [#2028](https://github.com/netease-youdao/LobsterAI/pull/2028) | UI update |

---

## 4. Community Hot Topics

### Most Active Discussion

| Item | Activity | Analysis |
|------|----------|----------|
| [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) — OpenClaw gateway event broadcasting | 1 comment, 0 reactions | **Architectural request for real-time persistence**: User `woxinsj` requests `agent:turn` or `agent:loop` events in OpenClaw gateway to enable "true real-time disk persistence." This reveals a **current limitation**: subagent persistence today requires polling/fetching, not event-driven. The "拿到这个事件后，才能真正做到实时落盘" ("only with this event can we achieve real-time persistence") phrasing suggests this is a known gap blocking a desired architecture. |

**Underlying need:** Event-driven architecture for agent execution loops, enabling reactive UI updates and reliable persistence without polling. This aligns with the subagent persistence work in [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034) but at a deeper protocol level.

### Stale but Significant PRs (updated but unmerged for ~6 weeks)
| PR | Topic | Significance |
|----|-------|------------|
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) | Security: API proxy log credential leak fix | **Critical security** — logs contained API keys, tokens, conversation content |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | Security: KV store IPC key whitelist | **Defense in depth** — renderer could access sensitive main-process data |
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | Local session usage statistics | User-facing analytics feature |
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | Theme color UI compact selector | UX polish |

---

## 5. Bugs & Stability

| Severity | Issue/PR | Description | Fix Status |
|----------|----------|-------------|------------|
| **High** (fixed) | [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033), [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | Subagent session sync missing tool results, duplicate tracking with colliding `agentId` keys, spawn error detection gaps | **Fixed in release** |
| **High** (fixed) | [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | Model switch error with custom models | **Fixed** |
| **Medium** (fixed) | [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | Browser config invalid | **Fixed** |
| **Medium** (open, architectural) | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | No `agent:turn`/`agent:loop` events in OpenClaw gateway — blocks true real-time persistence | **No fix PR**; requires upstream OpenClaw changes |
| **High** (unfixed, stale) | [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) | API proxy logs leak credentials and full response bodies | **PR open since April 7, updated but unmerged** |
| **High** (unfixed, stale) | [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | Renderer process can access sensitive KV store keys | **PR open since April 7, updated but unmerged** |

**Stability assessment:** The subagent system had significant pre-release bugs (sync, deduplication, UI state) that were rapidly fixed, suggesting **aggressive feature development with reactive stabilization**. The pattern of "merge fixes same day as release" indicates tight release management but some quality risk.

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Version |
|--------|--------|---------------------------|
| **Event-driven agent loop protocol** (`agent:turn`/`agent:loop`) | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | **High** — explicitly requested by team member, blocks "true" real-time persistence; may require OpenClaw gateway changes |
| **Real-time subagent persistence** (complement to [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034)'s fetch-then-persist) | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | **High** — natural evolution of current work |
| **Usage statistics dashboard** | [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | **Medium** — PR exists but stale; low priority vs. core features |
| **Enhanced theme customization** | [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | **Low** — cosmetic, consistently deprioritized |

**Emerging pattern:** Heavy investment in **subagent orchestration** (sidebar, persistence, rendering pipeline) suggests LobsterAI is positioning as a **multi-agent system** rather than single-chat assistant. The "thinking block display" feature indicates transparency into model reasoning is a product priority.

---

## 7. User Feedback Summary

### Pain Points (from issue/PR analysis)

| Pain Point | Evidence | Severity |
|------------|----------|----------|
| **Subagent reliability** | Multiple same-day fixes for sync, deduplication, error handling | High — was blocking release |
| **Model configuration fragility** | [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) custom model switch errors, [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) browser config invalid | Medium — configuration edge cases |
| **Security hygiene in logs/IPC** | [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534), [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | High — unaddressed despite PRs ready |
| **Mac-specific UI issues** | [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) window control overlap | Low — quickly fixed |

### Satisfaction Indicators
- Rapid bug turnaround (same-day fixes for release blockers)
- Thoughtful architecture (dedicated table for subagent messages, component extraction for reusability)

### Dissatisfaction/Risk Indicators
- Zero external community engagement (no 👍, no comments from non-team)
- Security PRs languishing for 6+ weeks despite being "ready"

---

## 8. Backlog Watch

### Critical: Security PRs Needing Immediate Attention

| PR | Age | Risk | Action Needed |
|----|-----|------|---------------|
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) | ~6 weeks | **Credential leakage to local logs** — API keys, Bearer tokens, conversation content in plaintext electron-log files | Merge or provide rejection rationale |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | ~6 weeks | **Renderer compromise → sensitive data access** — bypasses Electron sandbox assumptions | Merge or provide rejection rationale |

### Stale Dependency Upgrades (Risk: Security/Compatibility Debt)

| PR | Package | Jump | Risk |
|----|---------|------|------|
| [#1766](https://github.com/netease-youdao/LobsterAI/pull/1766) | vite | 5.4.21 → 8.0.13 | **Major version** — build system, potential breaking changes |
| [#1764](https://github.com/netease-youdao/LobsterAI/pull/1764) | react-dom | 18.3.1 → 19.2.6 | **Major version** — React 19 compatibility |
| [#1765](https://github.com/netease-youdao/LobsterAI/pull/1765) | @headlessui/react | 1.7.19 → 2.2.10 | **Major version** — UI component API changes |
| [#1763](https://github.com/netease-youdao/LobsterAI/pull/1763) | @vitejs/plugin-react | 4.7.0 → 6.0.1 | **Major version** — build tooling |
| [#1277](https://github.com/netease-youdao/LobsterAI/pull/1277) | electron, electron-builder | 40.2.1 → 42.1.0 | **Major version** — core framework, security patches |

**Assessment:** 5 dependency PRs covering core framework (Electron), build toolchain (Vite), and UI library (React/Headless UI) are all open and stale. The React 19 + Vite 8 combination is particularly risky to defer. Electron 42 likely contains security fixes given the 2-version jump.

### Architectural Issue
| Issue | Need |
|-------|------|
| [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | Requires cross-project coordination with OpenClaw gateway; should be tracked with milestone |

---

**Overall Project Health:** 🟡 **Caution**

- **Strengths:** High feature velocity, responsive bug fixing for release blockers, clear subagent strategic focus
- **Risks:** Security backlog, dependency stagnation, zero community engagement, potential "release crunch" quality patterns

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis Project Digest — 2026-05-23

## 1. Today's Overview

Moltis demonstrates **exceptional engineering velocity** with 9 PRs merged/closed and 7 of 8 issues resolved within a 24-hour window, indicating a highly responsive maintainer team (notably `penso` as primary contributor). The project shows no open PRs and only one remaining open issue, reflecting aggressive triage and rapid iteration cycles. Activity clusters around **Docker/container hardening**, **voice/telephony reliability**, and **agent documentation accessibility**—suggesting Moltis is maturing from core functionality toward deployment robustness and user onboarding. The zero-release day despite heavy code movement implies either a rolling release model or accumulation toward a larger version bump. Overall project health appears **strong** with maintainer bandwidth clearly available for community reports.

---

## 2. Releases

**No new releases** (2026-05-23).

---

## 3. Project Progress

### Merged/Closed PRs Today (9 items)

| PR | Author | Summary | Impact |
|:---|:---|:---|:---|
| [#1044](https://github.com/moltis-org/moltis/pull/1044) | penso | **Expose local Moltis docs to agents** — Multi-layer docs resolution (`MOLTIS_DOCS_DIR` → packaged → source → embedded fallback) with config template generation | Major UX: Agents now self-document via local knowledge, reducing external dependency |
| [#1043](https://github.com/moltis-org/moltis/pull/1043) | penso | **Piper TTS WAV metadata fix** — Distinct `AudioFormat::Wav` vs raw PCM; proper WAV wrapping for non-PCM requests | Fixes audio pipeline correctness; resolves [#1029](https://github.com/moltis-org/moltis/issues/1029) |
| [#1042](https://github.com/moltis-org/moltis/pull/1042) | penso | **Arbitrary chat attachments** — Web UI file upload beyond images, with MIME/size metadata through persistence layer | Major feature expansion: general document support in chat |
| [#1041](https://github.com/moltis-org/moltis/pull/1041) | penso | **OpenAI TTS MP3 fallback** — Uses MP3 for OpenAI-compatible TTS (Speaches compatibility), preserves OGG/Opus for others | Fixes [#1030](https://github.com/moltis-org/moltis/issues/1030); ecosystem interoperability |
| [#1040](https://github.com/moltis-org/moltis/pull/1040) | penso | **Docker sandbox media reads** — Host-to-container path fallback, `docker cp` stderr preservation, `send_image`/`send_document` resolution | Fixes [#977](https://github.com/moltis-org/moltis/issues/977) and [#1037](https://github.com/moltis-org/moltis/issues/1037); critical Docker deployment fix |
| [#1039](https://github.com/moltis-org/moltis/pull/1039) | dependabot | **OpenSSL 0.10.79 → 0.10.80** | Security/maintenance |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) | penso | **Vault encryption opt-out** — `auth.vault_enabled` flag, authenticated disable API with decryption of secrets before disabling | Operational flexibility; simplifies certain deployment scenarios |
| [#1034](https://github.com/moltis-org/moltis/pull/1034) | penso | **Twilio gather speech dispatch** — Fixes `SpeechResult`/`Digits` parsing priority over `CallStatus`, adds regression tests | Fixes [#1032](https://github.com/moltis-org/moltis/issues/1032); telephony critical path |
| [#1035](https://github.com/moltis-org/moltis/pull/1035) | penso | **Auto-detect Docker host data mounts** — Container mount scanning fallback for sandbox path resolution | Fixes [#977](https://github.com/moltis-org/moltis/issues/977); container infrastructure robustness |

**Key advancement pattern**: All 6 feature/bugfix PRs by `penso` directly close corresponding issues with **same-day or next-day turnaround**, indicating tight issue-to-PR linkage.

---

## 4. Community Hot Topics

### Most Active Discussion
- **[#977](https://github.com/moltis-org/moltis/issues/977)** — Browser sandbox Docker failure (5 comments, closed)
  - **Underlying need**: Container-native deployment is a primary Moltis use case; users expect sandboxed browser tools to work seamlessly in Docker/Podman/LXC stacks. The complexity of nested containerization (Moltis in Docker with sandbox execution) creates path resolution edge cases.

- **[#1028](https://github.com/moltis-org/moltis/issues/1028)** — Agent access to Moltis docs OOTB (2 comments, closed)
  - **Underlying need**: Users expect self-hosting to be **self-contained**; depending on public internet for documentation retrieval breaks air-gapped or offline deployments and creates latency/reliability issues.

### Engagement Pattern
Zero 👍 reactions across all issues suggests either: (a) small but vocal user base, (b) issues resolved too quickly for community pile-on, or (c) reaction culture not established. Comment counts are modest despite rapid resolution.

---

## 5. Bugs & Stability

| Severity | Issue | Status | Fix PR | Description |
|:---|:---|:---|:---|:---|
| **High** | [#977](https://github.com/moltis-org/moltis/issues/977) | ✅ Closed | [#1040](https://github.com/moltis-org/moltis/pull/1040), [#1035](https://github.com/moltis-org/moltis/pull/1035) | Docker sandbox browser/media failures — **nested container path resolution** |
| **High** | [#1032](https://github.com/moltis-org/moltis/issues/1032) | ✅ Closed | [#1034](https://github.com/moltis-org/moltis/pull/1034) | Twilio call: agent non-responsive to speech — **telephony gather parsing** |
| **Medium** | [#1030](https://github.com/moltis-org/moltis/issues/1030) | ✅ Closed | [#1041](https://github.com/moltis-org/moltis/pull/1041) | OpenAI TTS hardcoded `opus` format incompatible with Speaches |
| **Medium** | [#1037](https://github.com/moltis-org/moltis/issues/1037) | ✅ Closed | [#1040](https://github.com/moltis-org/moltis/pull/1040) | `send_image`/`send_document` fail in Docker |
| **Low** | [#1045](https://github.com/moltis-org/moltis/issues/1045) | 🔴 **OPEN** | None | No code block syntax highlighting in light mode |

**Stability assessment**: Exceptional closure rate (7/8). The sole open issue is cosmetic (UI theme). Docker/container edge cases dominated today's bug volume, suggesting the platform is being stress-tested in production-like deployments.

---

## 6. Feature Requests & Roadmap Signals

| Request | Issue | Status | Likelihood in Next Release |
|:---|:---|:---|:---|
| Agent local docs access | [#1028](https://github.com/moltis-org/moltis/issues/1028) | ✅ Implemented in [#1044](https://github.com/moltis-org/moltis/pull/1044) | **Shipped** |
| Arbitrary file attachments in web UI | [#1036](https://github.com/moltis-org/moltis/issues/1036) | ✅ Implemented in [#1042](https://github.com/moltis-org/moltis/pull/1042) | **Shipped** |
| Piper TTS audio conversion handling | [#1029](https://github.com/moltis-org/moltis/issues/1029) | ✅ Implemented in [#1043](https://github.com/moltis-org/moltis/pull/1043) | **Shipped** |
| Vault encryption disable option | (no issue) | ✅ Implemented in [#1033](https://github.com/moltis-org/moltis/pull/1033) | **Shipped** |

**Emerging patterns**: 
- **Voice/telephony maturity**: Multiple TTS/telephony fixes suggest active production use in call-center-like scenarios
- **Container-first deployment**: Repeated Docker hardening indicates target architecture
- **Agent self-sufficiency**: Docs OOTB + arbitrary attachments = reducing external dependencies

**Predicted next features**: Dark/light theme parity fix for [#1045](https://github.com/moltis-org/moltis/issues/1045); expanded attachment type preview; additional telephony provider support beyond Twilio.

---

## 7. User Feedback Summary

### Pain Points
| Area | Evidence | Severity |
|:---|:---|:---|
| **Docker/container complexity** | [#977](https://github.com/moltis-org/moltis/issues/977), [#1037](github.com/moltis-org/moltis/issues/1037) | High — path resolution between host/container/sandbox layers is fragile |
| **TTS ecosystem fragmentation** | [#1030](https://github.com/moltis-org/moltis/issues/1030) | Medium — OpenAI API compatibility assumptions break on alternatives (Speaches) |
| **Telephony reliability** | [#1032](https://github.com/moltis-org/moltis/issues/1032) | High — silent failures in speech recognition render calls unusable |

### Use Cases
- **Self-hosted AI assistant** with voice calling (Twilio integration)
- **Document-heavy workflows** requiring arbitrary file attachments
- **Containerized deployment** on Proxmox/LXC/Docker stacks
- **Offline/air-gapped** operation requiring local documentation

### Satisfaction Indicators
- ✅ Rapid issue resolution (same-day PRs)
- ✅ Direct maintainer engagement (`penso` responsive)
- ⚠️ Zero reactions may indicate limited community scale or engagement mechanisms

---

## 8. Backlog Watch

**No critical backlog items identified** — all issues from 2026-05-06 onward are closed except [#1045](https://github.com/moltis-org/moltis/issues/1045) (cosmetic, 0 comments, 0 reactions).

| Watch Item | Age | Risk | Notes |
|:---|:---|:---|:---|
| [#1045](https://github.com/moltis-org/moltis/issues/1045) Light mode syntax highlighting | 1 day | Very Low | Likely quick CSS fix; no user urgency expressed |

**Maintainer capacity**: `penso` merged 6 PRs in 24 hours. No PRs remain open. The project appears **unblocked and well-staffed** for current velocity.

---

*Digest generated from github.com/moltis-org/moltis data as of 2026-05-23.*

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw Project Digest — 2026-05-23

## 1. Today's Overview

CoPaw (QwenPaw) shows **elevated community activity** with 24 issues and 23 PRs updated in the last 24 hours, indicating an active development cycle despite no new release. The project is experiencing growing pains around **multi-model provider compatibility** (MiniMax, Gemini, DeepSeek, ChatGPT-5.5), **channel reliability** (WeChat, DingTalk), and **UI/UX polish**. With 17 open issues and 13 open PRs, the maintainers face a healthy but demanding backlog. Notably, first-time contributors are active (4 PRs), suggesting improving contributor onboarding, though several critical bugs around chat history persistence and proxy configuration remain unaddressed.

---

## 2. Releases

**No new releases** (v1.1.8.post1 remains current).

---

## 3. Project Progress

### Merged/Closed PRs Today (10 total)

| PR | Description | Impact |
|:---|:---|:---|
| [#4621](https://github.com/agentscope-ai/QwenPaw/pull/4621) | **fix(gemini): map max_tokens to max_output_tokens** | Critical fix for Gemini/Gemma model crashes; resolves pydantic ValidationError by proper parameter mapping |
| [#4627](https://github.com/agentscope-ai/QwenPaw/pull/4627) | **fix(WeChat): replace instance-level token invalid flag with per-request meta flag** | Fixes cross-request interference bug where one invalid token blocked all subsequent requests |
| [#4600](https://github.com/agentscope-ai/QwenPaw/pull/4600) | **fix(DingTalk): decode percent-encoded Chinese filenames** | Resolves Chinese filename corruption in file sending |
| [#4434](https://github.com/agentscope-ai/QwenPaw/pull/4434) | **feat(cron): add option to clear context before running agent tasks** | New automation feature for clean task execution environments |
| [#4626](https://github.com/agentscope-ai/QwenPaw/pull/4626) | **fix(qwenpaw-pet): fix pet stuck in Done state** | UI state machine fix for consecutive conversations |
| [#4618](https://github.com/agentscope-ai/QwenPaw/pull/4618) | **fix(WeChat): skip subsequent sends when context_token invalid** | Defensive handling for WeChat iLink API edge case (superseded by #4627) |
| [#4623](https://github.com/agentscope-ai/QwenPaw/pull/4623) | **style(console): update skill market page** | UI polish (menu icon, performance) |
| [#4395](https://github.com/agentscope-ai/QwenPaw/pull/4395) | **test(security): cover tool guard utilities** | Test coverage expansion for security module |
| [#4636](https://github.com/agentscope-ai/QwenPaw/pull/4636) | **feat(chat): add customizable slash command shortcut menu** | Closed (likely duplicate of #4637) |
| [#4565](https://github.com/agentscope-ai/QwenPaw/pull/4565) | **refactor(channel): unified access control system** | Major channel architecture refactor (open, ongoing) |

**Key advancement**: The Gemini `max_tokens` fix and WeChat token flag fixes address production-critical stability issues. The cron context-clear feature improves automation reliability.

---

## 4. Community Hot Topics

### Most Active by Engagement

| Rank | Issue/PR | Comments | Analysis |
|:---|:---|:---|:---|
| 1 | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) Chat history disappeared | **12 comments** | **Critical data loss bug** — users report intermittent chat history disappearance on session switch. Long-standing issue (author claims "existed for a long time"). High anxiety topic; no fix PR yet. |
| 2 | [#4051](https://github.com/agentscope-ai/QwenPaw/issues/4051) DeepSeek think content parsing | 10 comments | **Closed** — DeepSeek v4 flash's `<thinking>` tags not properly rendered, causing empty replies. Community workaround identified; provider-specific parsing remains fragile. |
| 3 | [#4474](https://github.com/agentscope-ai/QwenPaw/issues/4474) ChatGPT-5.5 support | 8 comments | Users eager for latest OpenAI model; configuration attempts failing. Signals **model provider lag** as competitive disadvantage. |
| 4 | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) NO_PROXY env var ignored | 6 comments | Enterprise/networking blocker — proxy configuration bypass broken, affecting corporate deployments. |
| 5 | [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625) MiniMax-M2.5 XML thinking format incompatible | 4 comments | Provider output format incompatibility causing conversation interruption. |

**Underlying needs**: 
- **Data reliability** (#4620) is the #1 trust issue
- **Model provider agility** — users expect rapid support for new models (GPT-5.5, DeepSeek v4)
- **Enterprise deployment** — proxy/network configuration needs first-class treatment

---

## 5. Bugs & Stability

| Severity | Issue | Description | Fix Status |
|:---|:---|:---|:---|
| 🔴 **Critical** | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) | Chat history disappearance — data loss | **No fix PR** |
| 🔴 **Critical** | [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625) | MiniMax-M2.5 XML thinking breaks execution | **No fix PR** |
| 🟡 **High** | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) | NO_PROXY ignored — forced proxy traversal | **No fix PR** |
| 🟡 **High** | [#4616](https://github.com/agentscope-ai/QwenPaw/issues/4616) | Dream awakening task error (WeChat channel misconfiguration) | **No fix PR** |
| 🟡 **High** | [#4556](https://github.com/agentscope-ai/QwenPaw/issues/4556) | Voice transcription ignores Whisper config, uses browser API | **No fix PR** |
| 🟡 **High** | [#4619](https://github.com/agentscope-ai/QwenPaw/issues/4619) | Web UI visual inconsistencies | **No fix PR** |
| 🟢 **Medium** | [#4611](https://github.com/agentscope-ai/QwenPaw/issues/4611) | ACP session leak — duplicate session conflict | PR [#4615](https://github.com/agentscope-ai/QwenPaw/pull/4615) open |
| 🟢 **Medium** | [#3984](https://github.com/agentscope-ai/QwenPaw/issues/3984) | context_check splits user/assistant pairs | **No fix PR** |

**Fixed today**: Gemini validation error (#4605 → #4621), WeChat token cross-contamination (#4612 → #4627), DingTalk filename encoding (#4586 → #4600)

---

## 6. Feature Requests & Roadmap Signals

| Feature | Issue/PR | Likelihood in Next Version | Rationale |
|:---|:---|:---|:---|
| **Customizable slash commands** | [#4633](https://github.com/agentscope-ai/QwenPaw/issues/4633) → PR [#4637](https://github.com/agentscope-ai/QwenPaw/pull/4637) | **High** | PR ready, clear UX win, low risk |
| **Plugin lifecycle hooks** | [#4613](https://github.com/agentscope-ai/QwenPaw/issues/4613) → PR [#4638](https://github.com/agentscope-ai/QwenPaw/pull/4638) | **High** | Enables ecosystem growth; PR submitted |
| **Plugin export/download ZIP** | PR [#4628](https://github.com/agentscope-ai/QwenPaw/pull/4628) | **Medium-High** | Completes plugin management loop |
| **Per-model retry/rate-limit config** | [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624) | **Medium** | Production necessity; complex config schema |
| **Mobile-responsive WebUI** | [#4635](https://github.com/agentscope-ai/QwenPaw/issues/4635) | **Medium** | Large user ask; significant frontend work |
| **Window size/position memory** | [#4634](https://github.com/agentscope-ai/QwenPaw/issues/4634) | **Medium** | Desktop polish; Tauri PR (#3813) may enable |
| **Remote Playwright endpoint** | [#4617](https://github.com/agentscope-ai/QwenPaw/issues/4617) | **Medium** | Infrastructure flexibility; aligns with containerization trends |
| **Multi-line text write tool** | [#4632](https://github.com/agentscope-ai/QwenPaw/issues/4632) | **Medium** | Core agent capability gap |
| **Tauri desktop app** | PR [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) | **Low-Medium** | Large PR, under review since April |

---

## 7. User Feedback Summary

### Pain Points
| Theme | Evidence | Severity |
|:---|:---|:---|
| **Data trust** | #4620 history loss, #3984 orphaned messages | Critical |
| **Provider fragility** | #4051 DeepSeek think tags, #4625 MiniMax XML, #4605 Gemini max_tokens, #4474 GPT-5.5 missing | High |
| **Channel reliability** | #4612/#4521 WeChat "success" but no delivery, #4556 voice transcription wrong backend | High |
| **Enterprise deployment** | #4607 proxy bypass failure | High |
| **Discovery/discoverability** | #4633 hidden slash commands, #4635 mobile limitations | Medium |

### Use Cases Emerging
- **Multi-model production deployments** (#4624) — users mixing providers for cost/performance optimization
- **Plugin ecosystem development** (#4613, #4628, #4632) — power users building extensions
- **Automation/scheduled tasks** (#4434 cron clear) — moving beyond chat to agent workflows

### Satisfaction Signals
- Active first-time contributions (4 PRs) = healthy community
- Rapid bug fixes for Gemini, WeChat, DingTalk = responsive maintainers
- Feature PRs matching user requests (#4637 slash commands) = good feedback loop

### Dissatisfaction Signals
- "Existed for a long time" (#4620) — accumulated technical debt
- "急盼修复" (urgently awaiting fix) (#4625) — user frustration with response time
- Closed issues with workarounds, not root fixes (#4051)

---

## 8. Backlog Watch

| Item | Age | Issue | Risk |
|:---|:---|:---|:---|
| **Tauri desktop support** | ~1 month | PR [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) | Large architectural PR; may conflict with ongoing work |
| **context_check message splitting** | ~3 weeks | [#3984](https://github.com/agentscope-ai/QwenPaw/issues/3984) | Data integrity; affects compaction feature |
| **MiniMax multimodal support** | ~1 month | [#3707](https://github.com/agentscope-ai/QwenPaw/issues/3707) | Competitive parity; closed but may need reopening |
| **E2E test infrastructure** | ~1 week | PR [#4464](https://github.com/agentscope-ai/QwenPaw/pull/4464) | Quality gate for releases |
| **Security test hard gate** | ~1 week | PR [#4467](https://github.com/agentscope-ai/QwenPaw/pull/4467) | 967 tests, 89% coverage; CI upgrade pending |

**Maintainer attention needed**: 
- [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) history loss — highest user impact, no assignee visible
- [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) proxy bypass — enterprise blocker
- PR [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) Tauri — long review cycle discourages large contributions

---

*Digest generated from GitHub activity 2026-05-22 to 2026-05-23. All links reference https://github.com/agentscope-ai/QwenPaw*

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw Project Digest — 2026-05-23

## 1. Today's Overview

ZeroClaw shows **high-velocity development** with 87 items updated in the last 24 hours (37 issues, 50 PRs), indicating an active pre-release sprint. No new releases were cut today, suggesting the project is in a consolidation phase toward v0.8.0. The activity is heavily weighted toward **MCP tooling fixes**, **WhatsApp channel stability**, and **TUI/daemon architecture refactoring** — with significant engineering investment in runtime internals rather than user-facing polish. Community engagement is strong with 11 comments on the flagship "Dream Mode" memory feature, though maintainer bandwidth appears stretched across multiple parallel workstreams.

---

## 2. Releases

**None today.**

The project appears to be accumulating changes for a future release, likely v0.8.0 given the `integration/v0.8.0` branch references in issues like [#6801](https://github.com/zeroclaw-labs/zeroclaw/issues/6801) and PRs like [#6805](https://github.com/zeroclaw-labs/zeroclaw/pull/6805).

---

## 3. Project Progress

### Merged/Closed PRs (14 total, key items)

| PR | Author | Summary | Impact |
|:---|:---|:---|:---|
| [#6706](https://github.com/zeroclaw-labs/zeroclaw/pull/6706) | alexandme | **WhatsApp protocol parity restored** — bumped `whatsapp-rust` ecosystem to 0.6, fixing post-April 2026 server-side protocol break | **Critical channel fix** — unblocks WhatsApp users |
| [#6838](https://github.com/zeroclaw-labs/zeroclaw/pull/6838) | puneetdixit200 | `doctor models` now reads configured provider credentials correctly | Fixes false-negative model listing for custom providers |
| [#6814](https://github.com/zeroclaw-labs/zeroclaw/pull/6814) | Project516 | Labeler fix: stops mis-tagging `.github/` image changes as `ci` | Minor workflow hygiene |
| [#6769](https://github.com/zeroclaw-labs/zeroclaw/pull/6769) | Project516 | Fixed 5 malformed Markdown links in `philosophy.md` | Docs polish |
| [#6804](https://github.com/zeroclaw-labs/zeroclaw/pull/6804) | vernonstinebaker | Parametrized `@@RPI_USER@@` in systemd template | Deploy flexibility for non-`pi` users |
| [#6009](https://github.com/zeroclaw-labs/zeroclaw/pull/6009) | alexandme | OTel tool spans enriched with `gen_ai.tool.*` semantic conventions | Observability foundation for production monitoring |
| [#6748](https://github.com/zeroclaw-labs/zeroclaw/pull/6748) | Project516 | Image optimization via ImgBot (24 assets) | Repo size reduction |

### Notable Open PRs Advancing

- [#6848](https://github.com/zeroclaw-labs/zeroclaw/pull/6848): **TUI integration branch** — large cross-cutting PR merging TUI into mainline (singlerider)
- [#6693](https://github.com/zeroclaw-labs/zeroclaw/pull/6693): **Dream Mode memory consolidation** — 5-phase engine implementation (JordanTheJet)
- [#6861](https://github.com/zeroclaw-labs/zeroclaw/pull/6861): **MCP tool_filter_groups fix** — origin-based detection replacing broken `__` heuristic (nick-pape)

---

## 4. Community Hot Topics

### Most Active by Engagement

| Rank | Item | Comments | Core Tension |
|:---|:---|:---|:---|
| 1 | [#5849](https://github.com/zeroclaw-labs/zeroclaw/issues/5849) Dream Mode — Periodic Memory Consolidation | **11 comments** | **Architectural ambition vs. implementation complexity** — community wants "sleep/reflect" metaphors for agents, but PR [#6693](https://github.com/zeroclaw-labs/zeroclaw/pull/6693) reveals this requires deep runtime hooks (cron, memory pruning, LLM reflection pipeline) |
| 2 | [#6246](https://github.com/zeroclaw-labs/zeroclaw/issues/6246) WhatsApp protocol break | 6 comments | **Vendor dependency fragility** — WhatsApp's unilateral server changes force emergency crate migrations; now closed via [#6706](https://github.com/zeroclaw-labs/zeroclaw/pull/6706) |
| 3 | [#6699](https://github.com/zeroclaw-labs/zeroclaw/issues/6699) MCP `tool_filter_groups` no-op | 6 comments | **Configuration surface vs. runtime reality** — documented features silently fail due to prefix-check bug; fix PR [#6861](https://github.com/zeroclaw-labs/zeroclaw/pull/6861) in flight |
| 4 | [#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) RFC: Work Lanes, Board Automation | 4 comments | **Governance scaling pain** — maintainer Audacity88 proposing automation to reduce manual triage burden as project grows |

### Underlying Needs Analysis

- **Dream Mode (#5849)**: Users want agents that *improve without prompting* — a self-tuning system. The 11-comment depth shows this resonates as a differentiator vs. "stateless" competitors.
- **Work Lanes RFC (#6808)**: Project has outgrown informal triage; needs structured contribution flow without "making maintainers keep another manual system alive" (author's words).

---

## 5. Bugs & Stability

### S1 (Workflow Blocked) — Immediate Attention Required

| Issue | Component | Status | Fix PR? |
|:---|:---|:---|:---|
| [#6699](https://github.com/zeroclaw-labs/zeroclaw/issues/6699) MCP `tool_filter_groups` no-op | agent/runtime/tool | **OPEN** | ✅ [#6861](https://github.com/zeroclaw-labs/zeroclaw/pull/6861) (open, nick-pape) |
| [#6036](https://github.com/zeroclaw-labs/zeroclaw/issues/6036) Infinite tool-call loop on Termux/Android | agent/runtime | **OPEN**, `needs-repro` | ❌ None |
| [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) WhatsApp QR not showing | channel:whatsapp | **OPEN** | ❌ None (related to [#6246](https://github.com/zeroclaw-labs/zeroclaw/issues/6246) fix?) |
| [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) `vision_provider` silently ignored — images routed to fallback | provider/multimodal | **OPEN** | ❌ None |
| [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844) Slack `bot_token` must be in config, not env | channel:slack | **OPEN** | ❌ None (regression of [#6237](https://github.com/zeroclaw-labs/zeroclaw/issues/6237)) |

### S2 (Degraded Behavior)

| Issue | Component | Status | Fix PR? |
|:---|:---|:---|:---|
| [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836) `setup.bat --minimal` builds 26 MB not ~6 MB | scripts/Windows | **OPEN** | ❌ None |
| [#6856](https://github.com/zeroclaw-labs/zeroclaw/issues/6856) `show_tool_calls` missing from channel schema v3 | channel/config | **OPEN** | ❌ None |
| [#6813](https://github.com/zeroclaw-labs/zeroclaw/issues/6813) Brittle timing threshold in parallel-dispatch test | channel/tests | **OPEN** | ❌ None |

### Regressions Noted

- **Slack token handling (#6844)**: Previous fix ([#6237](https://github.com/zeroclaw-labs/zeroclaw/issues/6237)) claimed resolved by [5c2bfdc](https://github.com/zeroclaw-labs/zeroclaw/commit/5c2bfdca7e59a5124b2184357c70) but user reports still broken — **suggests incomplete fix or config migration path failure**.

---

## 6. Feature Requests & Roadmap Signals

### Likely Near-Term (v0.8.0 or v0.8.1)

| Feature | Issue/PR | Signal Strength | Rationale |
|:---|:---|:---|:---|
| **TUI Agent Chat** | [#6824](https://github.com/zeroclaw-labs/zeroclaw/issues/6824), [#6848](https://github.com/zeroclaw-labs/zeroclaw/pull/6848) | ⭐⭐⭐ HIGH | Integration PR open, stacked PRs (#6858 first-run states), singlerider driving |
| **Dream Mode** | [#5849](https://github.com/zeroclaw-labs/zeroclaw/issues/5849), [#6693](https://github.com/zeroclaw-labs/zeroclaw/pull/6693) | ⭐⭐⭐ HIGH | 11-comment engagement, PR in progress, "accepted" status |
| **ACP Protocol Extensions (diff/file-proposal)** | [#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820) | ⭐⭐⭐ HIGH | Enables TUI approval flows; blocked by TUI readiness |
| **Runtime RPC/Unix Socket** | [#6837](https://github.com/zeroclaw-labs/zeroclaw/issues/6837) | ⭐⭐⭐ HIGH | Infrastructure for TUI-daemon communication; "in-progress" |
| **Session-scoped overrides** | [#6817](https://github.com/zeroclaw-labs/zeroclaw/issues/6817) | ⭐⭐ MEDIUM | User demand for dynamic model/temperature changes without reload |

### Medium-Term Signals

| Feature | Issue | Signal Strength |
|:---|:---|:---|
| **MemoryStrategy trait decoupling** | [#6850](https://github.com/zeroclaw-labs/zeroclaw/issues/6850) | ⭐⭐ MEDIUM — architectural RFC, enables Dream Mode extensibility |
| **Skills UX v0.7.6** | [#6253](https://github.com/zeroclaw-labs/zeroclaw/issues/6253) | ⭐⭐ MEDIUM — tracker open, community input solicited |
| **ARM64 Docker target** | [#5187](https://github.com/zeroclaw-labs/zeroclaw/pull/5187) | ⭐⭐ MEDIUM — stale since April, `needs-author-action` |

---

## 7. User Feedback Summary

### Pain Points (Explicit)

| Issue | User Quote / Symptom | Severity |
|:---|:---|:---|
| WhatsApp broken (twice) | "pair succeeds but messages don't flow" → "not showing QR" | **Recurring platform fragility** |
| Windows builds oversized | Expected ~6 MB, got ~26 MB | **Docs accuracy / trust erosion** |
| Config env var limitations | Slack token "cannot be supplied by environment variable" | **12-factor deployment friction** |
| Vision routing silent failure | `vision_provider` "silently ignored" | **Configuration debugging nightmare** |
| Android infinite loops | "repeatedly outputting the same message without ever terminating" | **Mobile runtime immaturity** |

### Satisfaction Signals

- **"Best tool out there. Wishing way more stars."** — [MushiTheMoshi](https://github.com/MushiTheMoshi) in [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847), despite reporting S1 bug
- Strong engagement with Dream Mode concept suggests **emotional connection to agent autonomy narrative**

### Use Case Patterns

- **Self-hosting enthusiasts**: Custom Telegram endpoints (#6807), Signal reactions (#6840), Raspberry Pi deploys (#6804)
- **Enterprise-adjacent**: OTel observability (#5980/#6009), config validation (#6079), model provider flexibility (#6756)
- **Developer tooling**: Skills authoring (#6253, #6860), MCP ecosystem integration (#6699, #6861)

---

## 8. Backlog Watch

### Critical Items Needing Maintainer Action

| Issue | Age | Blocker | Risk |
|:---|:---|:---|:---|
| [#6036](https://github.com/zeroclaw-labs/zeroclaw/issues/6036) Android infinite loop | ~1 month | `needs-repro` — no Termux/Android maintainer bandwidth? | **Mobile platform abandonment signal** |
| [#6074](https://github.com/zeroclaw-labs/zeroclaw/issues/6074) 153 commits lost in bulk revert | ~1 month | "Help wanted" — audit/recovery of c3ff635 | **Knowledge loss, contributor discouragement** |
| [#6243](https://github.com/zeroclaw-labs/zeroclaw/issues/6243) Streaming decode error — custom provider | ~3 weeks | `needs-repro` — GPU hangs at 50% | **Resource leak, production instability** |
| [#5187](https://github.com/zeroclaw-labs/zeroclaw/pull/5187) ARM64 Docker | ~7 weeks | `needs-author-action` — cross-compilation complexity | **Deployment diversity gap** |

### Governance Concern

- **Label/Project Hygiene**: [#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) RFC explicitly addresses that current manual triage doesn't scale. With 30 open issues updated today alone, maintainer burnout risk is material.

---

*Digest generated from GitHub activity 2026-05-22 to 2026-05-23. All links: [github.com/zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)*

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*