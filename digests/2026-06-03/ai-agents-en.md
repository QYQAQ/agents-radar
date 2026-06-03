# OpenClaw Ecosystem Digest 2026-06-03

> Issues: 455 | PRs: 500 | Projects covered: 13 | Generated: 2026-06-03 00:42 UTC

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

# OpenClaw Project Digest — 2026-06-03
## Research-Focused Filter: Vision-Language, Reasoning, Training, Hallucination, Reliability

---

## 1. Today's Overview

OpenClaw shows **intense development velocity** with 455 issues and 500 PRs active in the last 24 hours, but **zero new releases** indicate a stabilization period before the next version cut. The project is heavily focused on **session-state reliability** and **message-delivery correctness**—core infrastructure for long-context agent interactions. Notably absent from today's activity: explicit vision-language model (VLM) integration work, multimodal reasoning features, or dedicated hallucination mitigation research. The dominant themes are **orchestration reliability** (session compaction, transcript integrity, tool-call recovery) and **provider compatibility** (Anthropic long-context handling, DeepSeek DSML parsing, Codex harness stability). For researchers tracking AI reliability, the volume of "silent message loss" and "phantom run" bugs suggests this codebase is actively grappling with fundamental distributed agent-state consistency problems.

---

## 2. Releases

**None** — No new releases published. Last release appears to be 2026.5.28 (per GHCR image references in Issue #88788).

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant)

| PR | Title | Research Relevance |
|:---|:---|:---|
| [#89601](https://github.com/openclaw/openclaw/pull/89601) | fix(outbound): stop schema-padded poll modifiers from blocking send | **Tool schema robustness** — prevents schema-overfit blocking of valid sends; relevant to reliable tool-use in agent loops |
| [#71203](https://github.com/openclaw/openclaw/pull/71203) | Refresh configured agent models.json caches during startup warmup | **Model discovery reliability** — reduces cold-start hallucinations from stale model metadata |

### Open PRs Advancing Core Capabilities

| PR | Title | Research Relevance |
|:---|:---|:---|
| [#89387](https://github.com/openclaw/openclaw/pull/89387) | fix(agents): dedupe transcript rewrite suffix replay | **Critical for long-context integrity** — fixes context-overflow recovery creating duplicate user messages; directly impacts transcript fidelity and reasoning chain correctness |
| [#75336](https://github.com/openclaw/openclaw/pull/75336) | feat(compaction): add identifier survival validation after summarization | **Long-context compaction quality** — ensures named entities/identifiers persist through summarization; prevents reasoning degradation in extended sessions |
| [#86637](https://github.com/openclaw/openclaw/pull/86637) | fix(agents): recover tool calls from DeepSeek DSML text markup | **Model-specific reasoning extraction** — recovers structured tool calls from DeepSeek's `<think>`-like markup; addresses "ghost tool calls" from truncated streams |
| [#84972](https://github.com/openclaw/openclaw/pull/84972) | fix(agent): treat Anthropic long-context usage errors as context overflow for compact+retry | **Long-context error taxonomy** — correctly classifies Anthropic's 429 "extra usage" as compaction-trigger, not fatal error |
| [#89290](https://github.com/openclaw/openclaw/pull/89290) | [codex] Keep Codex waiting after raw reasoning progress | **Reasoning-time estimation** — distinguishes "thinking in progress" from "stall"; prevents premature termination of extended reasoning chains |

---

## 4. Community Hot Topics

### Most Active Issues (by comment count)

| Issue | Comments | Core Problem | Research Signal |
|:---|:---|:---|:---|
| [#52875](https://github.com/openclaw/openclaw/issues/52875) | 21 | Session routing failure after upgrade | **Agent-to-agent communication breakdown** — foundational for multi-agent reasoning topologies |
| [#88838](https://github.com/openclaw/openclaw/issues/88838) | 17 | SQLite migration for session/transcript state | **Database abstraction for long-context state** — branch-by-abstraction pattern for state persistence |
| [#63918](https://github.com/openclaw/openclaw/issues/63918) | 17 | `thinking=none` rejected by gpt-5-nano | **Model capability negotiation** — reasoning parameter compatibility across model generations |
| [#67035](https://github.com/openclaw/openclaw/issues/67035) | 14 | Windows chat UI: input swallowed, streamed replies invisible | **Streaming rendering correctness** — UI-reasoning desynchronization |
| [#55334](https://github.com/openclaw/openclaw/issues/55334) | 10 | `sessions.json` unbounded growth → OOM | **Memory scaling for long sessions** — skillsSnapshot duplication is anti-pattern for context management |

### Underlying Needs Analysis

The community is **screaming for session-state reliability**. The concentration of "message loss," "session stuck," and "phantom run" issues indicates that OpenClaw's core abstraction—persistent agent sessions with transcript replay—is **operationally fragile at scale**. For researchers: this is a real-world case study in the gap between "works in demo" and "works in 24/7 deployment" for long-context agents.

---

## 5. Bugs & Stability

### Critical (P1) — Research-Relevant

| Issue | Bug Type | Fix PR? | Research Note |
|:---|:---|:---|:---|
| [#88312](https://github.com/openclaw/openclaw/issues/88312) | Codex turn-completion stall regression | No | **Reasoning termination detection failure** — "Codex stopped before confirming turn complete" indicates model-specific end-of-reasoning signal misclassification |
| [#86519](https://github.com/openclaw/openclaw/issues/86519) | Agent repeats identical replies 2-10× | No | **Output loop / repetition hallucination** — classic degeneration pattern; reduced but not fixed in 2026.5.22 |
| [#86090](https://github.com/openclaw/openclaw/issues/86090) | `runHeartbeatOnce` returns `"ran"` in 78ms with no model execution | No | **Phantom execution** — system reports success without actual computation; critical for reliability metrics |
| [#88369](https://github.com/openclaw/openclaw/issues/88369) | Isolated cron self-conflicts with `EmbeddedAttemptSessionTakeoverError` | No | **Concurrency control in "isolated" sessions** — isolation guarantee violated |
| [#89374](https://github.com/openclaw/openclaw/issues/89374) | Timeout compaction reports success but leaves session unrecoverable | No | **Compaction correctness** — summarization claims success while actually destroying session utility |

### High (P2) — Training/Alignment-Relevant

| Issue | Bug Type | Research Note |
|:---|:---|:---|
| [#63918](https://github.com/openclaw/openclaw/issues/63918) | `thinking=none` rejected by gpt-5-nano | Post-training API drift: model no longer accepts previous default |
| [#85773](https://github.com/openclaw/openclaw/issues/85773) | Agents ignore workspace files/skills, give generic replies | **Context grounding failure** — RAG/persona injection broken; hallucination of "default" behavior |

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Signal | Likelihood in Next Release |
|:---|:---|:---|
| [#87072](https://github.com/openclaw/openclaw/pull/87072) — Interleaved progress lane for Telegram | Structured reasoning visualization | **High** — XL PR, video proof supplied, maintainer-ready |
| [#78172](https://github.com/openclaw/openclaw/pull/78172) — `skipEmojiSymbols` for TTS | Preprocessing for speech synthesis | Medium — clean, scoped |
| [#76159](https://github.com/openclaw/openclaw/issues/76159) — Per-job `acceptSilentStop` | **Alignment: reward shaping for intentional null outputs** | Medium — cron reliability |
| [#81061](https://github.com/openclaw/openclaw/issues/81061) — `before_route_inbound_message` hook | **Pre-routing interception for multi-agent bridging** | Low — architectural, needs product decision |

### Missing from Roadmap (Research Gap)

- **No explicit vision-language integration** — No issues/PRs mention image input, video understanding, or multimodal tool use
- **No hallucination detection/mitigation features** — No confidence scoring, citation verification, or self-consistency checks
- **No RLHF or post-training alignment infrastructure** — All "alignment" is prompt-level or routing-level

---

## 7. User Feedback Summary

### Real Pain Points

| Theme | Evidence | Severity |
|:---|:---|:---|
| **Silent data loss** | #80715 (Slack replies composed but not posted), #84882 (memory files deleted silently), #88992 (LLM "forgets" message tool → discard) | **Critical** — violates fundamental agent reliability |
| **Session state corruption** | #55334 (OOM), #88312 (stall), #89374 (compaction lies) | **Critical** — long-context sessions degrade unpredictably |
| **Model-specific fragility** | #63918 (gpt-5-nano thinking), #81607 (MiniMax thinking+text blocks), #86637 (DeepSeek DSML) | **High** — provider abstraction leaky |
| **Upgrade regressions** | #86519, #88312, #85773 all start with "After upgrading..." | **High** — release quality concerns |

### User Satisfaction Pattern

**Power users (multi-agent, cron-heavy)** are frustrated by state inconsistency. **Casual users** hit UI rendering bugs (#67035). The project has **no public satisfaction metrics** or structured feedback channel visible.

---

## 8. Backlog Watch

### Long-Unanswered Critical Issues

| Issue | Age | Blocker | Research Relevance |
|:---|:---|:---|:---|
| [#52249](https://github.com/openclaw/openclaw/issues/52249) — ACP parent session stuck until refresh | 73 days | Needs maintainer review, product decision | **Hierarchical session coordination** — parent-child yield semantics |
| [#41199](https://github.com/openclaw/openclaw/issues/41199) — Agent-to-agent tool parameter conflicts | 86 days | Needs product decision | **LLM-tool schema alignment** — systematic parameter conflict in multi-agent communication |
| [#55334](https://github.com/openclaw/openclaw/issues/55334) — `sessions.json` OOM | 69 days | Needs product decision, source repro | **Memory-bounded long-context** — fundamental scaling limit |
| [#60841](https://github.com/openclaw/openclaw/issues/60841) — `toolsAllow` cannot re-expose core tools | 60 days | Needs product decision, security review | **Tool policy composability** — security/ capability tradeoff |

### PRs Needing Maintainer Attention (Ready but Stalled)

| PR | Status | Risk |
|:---|:---|:---|
| [#87072](https://github.com/openclaw/openclaw/pull/87072) | Ready for maintainer look | XL size, compatibility risk |
| [#89613](https://github.com/openclaw/openclaw/pull/89613) | Ready for maintainer look | Auth policy documentation — security-critical |
| [#84972](https://github.com/openclaw/openclaw/pull/84972) | Needs proof (re-opened) | Long-context reliability fix, previously positive review |

---

## Research Analyst's Note

OpenClaw is a **high-velocity, reliability-challenged agent orchestration platform** with minimal explicit multimodal or alignment research. The most valuable research signals for 2026-06-03 are:

1. **Transcript integrity mechanisms** (#89387, #75336) — practical techniques for maintaining reasoning chain coherence under context pressure
2. **Model-specific parsing recovery** (#86637) — how to robustly extract structured behavior from divergent provider output formats
3. **Phantom execution detection** (#86090) — the gap between reported and actual computation is a critical reliability metric rarely measured

**Absent and needed**: Vision-language integration roadmap, explicit hallucination detection, post-training alignment beyond prompt engineering, and systematic evaluation of long-context reasoning quality degradation.

---

## Cross-Ecosystem Comparison

# Cross-Project Analysis: Personal AI Agent Ecosystem
## Research Synthesis — 2026-06-03

---

## 1. Ecosystem Overview

The personal AI assistant / agent open-source landscape is experiencing a **reliability crunch** as frontier model capabilities outpace orchestration infrastructure. Six active projects (OpenClaw, IronClaw, ZeroClaw, CoPaw, Hermes Agent, NanoBot) show sustained engineering velocity, yet all are in stabilization phases with **zero stable releases** across the board. The dominant pattern is reactive hardening: fixing reasoning content leakage, context window mismanagement, and provider-specific API fragmentation. Vision-language integration remains superficial—limited to capability flags and image input routing rather than unified multimodal reasoning architectures. Post-training alignment infrastructure is **entirely absent** from all visible roadmaps; "alignment" is operationalized as prompt filtering and tool allowlists rather than learned preference optimization.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Releases | Health Score* | Phase |
|:---|:---|:---|:---|:---|:---|
| **OpenClaw** | 455 | 500 | None (last: 2026.05.28) | ⚠️ High velocity, high fragility | Pre-release stabilization |
| **IronClaw** | 29 | 50 | None | 🔶 Intensive audit-driven hardening | Pre-production reliability push |
| **ZeroClaw** | 49 | 50 | v0.8.0-beta-2 | 🔶 Structured, boundary-focused | Beta feature-complete |
| **CoPaw** | 48 | 32 | None (v1.1.10 pending) | 🔶 Migration-blocked | AgentScope 2.0 transition |
| **Hermes Agent** | 50 | 50 | None | 🔶 Maintenance-heavy | Production hardening |
| **NanoBot** | 10 | 28 | None | 🟡 Moderate, memory-focused | Incremental improvement |
| **PicoClaw** | 3 | 14 | Nightly only | 🟡 Low engagement, steady | Early stabilization |
| **LobsterAI** | 0 | 50 | None | 🟡 High merge rate, zero community | Internal product polish |
| **NanoClaw** | 1 | 7 | None | 🔴 Minimal research relevance | Infrastructure-only |
| **NullClaw** | 1 | 1 | None | 🔴 Maintenance mode | Single-maintainer |
| **TinyClaw** | — | — | — | ⚫ Dormant | No activity |
| **Moltis** | — | — | — | ⚫ Dormant | No activity |
| **ZeptoClaw** | — | — | — | ⚫ Dormant | No activity |

*\*Health Score: composite of velocity, issue resolution rate, architectural coherence, and research-relevant output*

---

## 3. OpenClaw's Position

| Dimension | OpenClaw | Peer Comparison |
|:---|:---|:---|
| **Scale** | 455 issues, 500 PRs/24h | **10× IronClaw/ZeroClaw/Hermes**; 50× NanoBot |
| **Community** | Dense, vocal, frustrated | Most active external community; LobsterAI/NullClaw have near-zero engagement |
| **Technical depth** | Session-state reliability, transcript integrity, compaction | **Deepest long-context infrastructure**; IronClaw leads on safety audit rigor; ZeroClaw on architectural boundaries |
| **Scope** | General-purpose agent orchestration | Broadest provider compatibility matrix; Hermes more desktop-focused; NanoBot more channel-integrated |
| **Critical gap** | No VLM integration, no hallucination detection, no alignment research | IronClaw has reasoning token controls; CoPaw has explicit "thinking level" UI; ZeroClaw has WIT sandboxing planned |

**Advantages**: Unmatched operational stress-testing at scale; most mature compaction/summarization logic; deepest multi-provider compatibility layer.

**Vulnerabilities**: "Silent message loss" and "phantom run" bugs indicate **fundamental distributed systems debt**; no architectural response to reasoning model proliferation; absent multimodal roadmap.

---

## 4. Shared Technical Focus Areas

| Requirement | Projects | Specific Needs |
|:---|:---|:---|
| **Long-context compaction with identifier preservation** | OpenClaw (#75336), CoPaw (#4551), Hermes (#18733), PicoClaw (#2988) | Named entities must survive summarization; per-model threshold adaptation; DAG-structured recoverable compression |
| **Reasoning content extraction/normalization** | ZeroClaw (#5600, #6059), IronClaw (#4341), CoPaw (#3985), NanoClaw (#2672) | Provider-specific CoT formats (DeepSeek `reasoning_content`, Kimi streaming, Qwen THINKING tokens) need unified abstraction |
| **Internal/external output boundary enforcement** | ZeroClaw (#6040, #5795, #7068), IronClaw (#4341, #4344), Hermes (#36934) | Prevent reasoning blocks, tool transcripts, scratchpad content from leaking to user channels |
| **Provider-specific error classification & recovery** | OpenClaw (#84972, #86637), PicoClaw (#2991), Hermes (#37677), IronClaw (#4339) | HTTP 500 retry logic, vision API error code mapping, parameter deprecation handling (Claude temperature) |
| **Tool-call trace integrity** | NanoBot (#4006, #3983), OpenClaw (#89387), IronClaw (#4339), ZeroClaw (#7063) | Orphaned results, false rejections, policy bypasses, format confusion (XML vs. JSON) |
| **Session state corruption prevention** | OpenClaw (#55334, #89374), NanoBot (#4169), PicoClaw (#2992), Hermes (#7725) | History desync, offset corruption, unbounded growth, upgrade migration failures |

**Emerging but unaddressed**: No project has systematic hallucination detection, confidence calibration, or cross-model consensus. Reliability work is **reactive bug-fixing**, not proactive architectural safeguard.

---

## 5. Differentiation Analysis

| Project | Primary Differentiator | Target User | Architecture Signature |
|:---|:---|:---|:---|
| **OpenClaw** | Scale-tested session reliability | Power users, multi-agent deployments | Provider-agnostic orchestration with compaction |
| **IronClaw** | Systematic safety/audit hardening | Security-conscious enterprise | "Reborn" loop hygiene, WASM sandboxing, auth gates |
| **ZeroClaw** | Delegated agent boundary control | Developers, human-in-the-loop workflows | ACP protocol, WIT plugins, diff-based verification |
| **CoPaw** | AgentScope ecosystem integration | Chinese-language users, plugin developers | AgentScope 2.0 runtime, subagent spawning |
| **Hermes Agent** | Desktop-native persistent agents | Individual power users | Electron + gateway, long-running session durability |
| **NanoBot** | Lightweight RAG memory, channel density | IM-integrated casual users | Embedding-based retrieval, multi-channel (QQ/WeChat/email) |
| **LobsterAI** | Consumer UI polish, thinking levels | End users, non-technical | Electron app, MiniMax integration, reasoning depth UI |
| **PicoClaw** | Embedded/hardware-adjacent | Sipeed hardware ecosystem | Go-based, WebSocket-centric, resource-constrained |

**Architectural fault line**: OpenClaw/Hermes/NanoBot use **traditional process-based agents**; IronClaw/ZeroClaw move toward **sandboxed/WASM-isolated capabilities**; CoPaw is runtime-migrating. No project has unified multimodal reasoning architecture—all treat vision as input routing afterthought.

---

## 6. Community Momentum & Maturity

| Tier | Projects | Characteristics |
|:---|:---|:---|
| **Hyper-velocity, high debt** | OpenClaw | 1000+ daily updates; "screaming for reliability"; unsustainable issue volume |
| **Intensive stabilization** | IronClaw, ZeroClaw, Hermes | Audit-driven (L1–L11, C1–C6); boundary-focused; pre-production |
| **Migration-blocked** | CoPaw | AgentScope 2.0 blocks feature work; security-responsive but architecturally frozen |
| **Incremental polish** | NanoBot, PicoClaw, LobsterAI | Low community engagement; infrastructure or UI focus; no research breakthroughs |
| **Maintenance/dormant** | NanoClaw, NullClaw, TinyClaw, Moltis, ZeptoClaw | Single-digit daily activity or zero; no visible innovation |

**Maturity paradox**: OpenClaw has **most users, least reliability**; IronClaw has **most systematic safety engineering, least user visibility**; ZeroClaw has **cleanest architectural vision, smallest operational stress-test**.

---

## 7. Trend Signals

| Trend | Evidence | Value for Developers |
|:---|:---|:---|
| **Reasoning model heterogeneity outpaces abstractions** | DeepSeek-V4, Kimi, Qwen3.6, Claude Opus 4.8 all break existing integrations | **Design provider adapters as format-negotiation layers**, not static mappings; expect 6-month half-life for any reasoning extraction logic |
| **"Thinking" controls become UX expectation** | LobsterAI #1985 (thinking levels), CoPaw implicit demand, ZeroClaw leakage fixes | Users want **reasoning depth configurability**; plan for Off/Minimal/Adaptive/Maximum modes with corresponding latency/cost tradeoffs |
| **Context compression is lossy and dangerous** | CoPaw #4895 (infinite image compression loop), OpenClaw #89374 (compaction lies), #4551 (DAG-based lossless proposed) | **Invest in recoverable compression** with retrieval backdoors; treat summarization as explicit information-loss event, not transparent optimization |
| **Delegated agent architectures leak control boundaries** | ZeroClaw #7068 (Codex scratchpad leak), IronClaw subagent correctness audit | When agent A delegates to agent B, **output attribution and safety guarantees must propagate**; current architectures fail this |
| **Vision-language integration is capability-flag theater** | LobsterAI #2093 (hardcoded `false`), Hermes #25837 (no dimension validation), PicoClaw #2989 (error code whack-a-mole) | **Image input requires physical property validation** (pixels, not bytes); provider capability metadata needs runtime verification, not static configuration |
| **PII/safety redaction conflicts with observability** | NullClaw #944 (timestamp redaction), ZeroClaw #7063 (tool allowlist bypass) | **Separate machine-generated metadata from user content streams** at architecture level; pattern-matching redaction is inherently fragile |
| **Air-gapped/TEE execution emerging as differentiator** | ZeroClaw #6293, IronClaw WASM sandboxing | For high-trust deployments, **verifiable execution environments** will separate production-ready from demo-ready frameworks |

**Meta-signal**: The entire ecosystem is **one major reasoning model release away from widespread breakage**. No project has provider-agnostic parameter negotiation, reasoning format discovery, or capability verification infrastructure. The first framework to solve **"reasoning content as first-class, portable, auditable context"** will capture significant research and production adoption.

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot Project Digest — 2026-06-03

## Research Focus: Vision-Language Capabilities, Reasoning Mechanisms, Training Methodologies, Hallucination-Related Issues

---

## 1. Today's Overview

NanoBot shows **moderate development velocity** with 28 PRs and 10 issues updated in the past 24 hours, though **no new releases**. Activity is concentrated in infrastructure hardening (WebUI, CLI packaging, channel stability) rather than core model capabilities. Notably absent from today's activity are direct multimodal reasoning improvements, explicit long-context architecture changes, or post-training alignment research. The most research-relevant signals emerge from **conversation history integrity bugs** (#4006, #4169) and **tool execution boundary conditions** (#3983, #4155), which touch on reliability of agentic reasoning traces. Vision-language work is limited to **image generation provider extensibility** (#4132, #4167) rather than fundamental VLM capabilities.

---

## 2. Releases

**None** — No new versions released today.

---

## 3. Project Progress

### Merged/Closed PRs with Research Relevance

| PR | Focus Area | Research Relevance |
|:---|:---|:---|
| [#4155](https://github.com/HKUDS/nanobot/pull/4155) — fix(runner): prevent read_file offload loop | **Tool result persistence & reasoning trace integrity** | Prevents infinite loops when recovering large tool outputs; directly impacts reliability of long-context agent trajectories where file reads are interleaved with reasoning steps |
| [#4109](https://github.com/HKUDS/nanobot/pull/4109) — feat: Add lightweight RAG for memory retrieval | **Retrieval-augmented generation, long-context memory** | Local embedding-based RAG for memory; relevant to long-context understanding though details sparse in summary |
| [#3990](https://github.com/HKUDS/nanobot/pull/3990) — refactor(dream): replace two-phase Dream class with simple cron + process_direct | **Agent loop architecture, memory consolidation** | Simplifies background memory processing; "Dream" mechanism resembles consolidation processes relevant to long-context coherence |

### Other Closed PRs (Infrastructure/Non-Research)
- [#4115](https://github.com/HKUDS/nanobot/pull/4115), [#4157](https://github.com/HKUDS/nanobot/pull/4157), [#4150](https://github.com/HKUDS/nanobot/pull/4150), [#4149](https://github.com/HKUDS/nanobot/pull/4149), [#4151](https://github.com/HKUDS/nanobot/pull/4151) — WebUI gateway/routing fixes
- [#4162](https://github.com/HKUDS/nanobot/pull/4162), [#4160](https://github.com/HKUDS/nanobot/pull/4160) — Email channel attachments
- [#4146](https://github.com/HKUDS/nanobot/pull/4146) — Napcat (QQ) channel
- [#4159](https://github.com/HKUDS/nanobot/pull/4159) — Auto-fix for uv tool pip installs

---

## 4. Community Hot Topics

### Most Active by Engagement

| Item | Comments | Analysis |
|:---|:---|:---|
| [#4167](https://github.com/HKUDS/nanobot/issues/4167) — Image generation fails with OpenAI-compatible APIs | 2 comments | **Vision-language boundary issue**: Hardcoded `response_format` parameter breaks compatibility with alternative image generation providers (Agnes AI). Reveals fragility in multimodal API abstraction layer |
| [#4006](https://github.com/HKUDS/nanobot/issues/4006) — Orphaned tool results without corresponding tool_calls | 2 comments | **Critical for reasoning reliability**: Post-fix of #3984, conversation histories still contain unpaired tool results. Violates OpenAI/Anthropic specifications, causing API rejections and rendering failures. Indicates **systematic challenges in maintaining structured reasoning traces** |
| [#4169](https://github.com/HKUDS/nanobot/pull/4169) — Reset out-of-range last_consolidated | undefined (new, high priority) | **Session state corruption in long-context scenarios**: Desynced offsets can zero out entire conversation history, breaking agent continuity |

### Underlying Needs Analysis
- **Tool-call trace integrity** (#4006, #3983, #4155): Community is actively debugging edge cases in structured generation where tool execution boundaries fail. This is foundational for reliable multi-step reasoning.
- **Provider flexibility for multimodal tools** (#4167, #4132): Users need to swap vision-language backends without parameter assumptions.

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **High** | [#4006](https://github.com/HKUDS/nanobot/issues/4006) | Orphaned tool results break API compliance and trajectory rendering | **Partial fix** (#3984); issue persists, needs deeper fix |
| **High** | [#4169](https://github.com/HKUDS/nanobot/pull/4169) | Corrupt `last_consolidated` offsets erase session history | **Fix PR open** |
| **High** | [#4153](https://github.com/HKUDS/nanobot/issues/4153) / [#4155](https://github.com/HKUDS/nanobot/pull/4155) | `read_file` cannot recover persisted tool results; offload loops | **Fixed in #4155** |
| **Medium** | [#4167](https://github.com/HKUDS/nanobot/issues/4167) | Image generation API compatibility | No fix yet; #4132 requests feature |
| **Medium** | [#4168](https://github.com/HKUDS/nanobot/issues/4168) | MCP server session termination after random time | No fix yet |
| **Low** | [#4158](https://github.com/HKUDS/nanobot/issues/4158) | pip unavailable under `uv tool` | **Fixed** (#4164, #4159) |

### Research-Critical Stability Notes
- **Hallucination-adjacent**: [#4006](https://github.com/HKUDS/nanobot/issues/4006)'s orphaned tool results create *structural hallucinations* where the system believes tools were called but no evidence exists in the assistant's generation record. This is a **mechanism for misattributed reasoning**.
- **Long-context fragility**: [#4169](https://github.com/HKUDS/nanobot/pull/4169) and [#4081](https://github.com/HKUDS/nanobot/issues/4081) (closed, concurrent cursor duplicates) show **history management races** that could corrupt extended reasoning sessions.

---

## 6. Feature Requests & Roadmap Signals

| Item | Signal | Likelihood in Next Version |
|:---|:---|:---|
| [#4132](https://github.com/HKUDS/nanobot/issues/4132) — Custom image generation provider | **Multimodal extensibility**: Decoupling vision generation from hardcoded providers | High — #4167 is active bug, community need clear |
| [#4166](https://github.com/HKUDS/nanobot/issues/4166) — Subagent access to MCP services | **Multi-agent reasoning architecture**: Tool access propagation in hierarchical agent spawning | Medium — architectural change, security implications |
| [#4139](https://github.com/HKUDS/nanobot/pull/4139) — Cloud deployment layer (HF Spaces/ModelScope) | **Distribution/alignment infrastructure**: Easier deployment for evaluation and feedback collection | Medium — large PR open, needs review |
| [#4109](https://github.com/HKUDS/nanobot/pull/4109) — Lightweight RAG for memory | **Long-context augmentation via retrieval**: Already merged, signals direction toward hybrid memory | **Shipped** |

### Absent from Roadmap Signals
- No explicit requests for: chain-of-thought visualization, reasoning verification steps, red-teaming for hallucination, or RLHF/RLAIF infrastructure
- No post-training alignment methodology discussions visible

---

## 7. User Feedback Summary

### Pain Points (Research-Relevant)

| Theme | Evidence | Implication |
|:---|:---|:---|
| **Conversation history corruption** | #4006, #4169, #4081, #4153 | Users encounter **broken reasoning traces** where prior context becomes unusable or misattributed; critical for long-context reliability research |
| **Tool execution boundary failures** | #3983 (PR), #4155 | **False tool execution signals** — systems report tool calls that cannot be validated or executed, risking hallucinated action chains |
| **Multimodal API rigidity** | #4167, #4132 | Vision-language capabilities locked to specific provider assumptions, limiting experimental flexibility |
| **MCP/session stability** | #4168, #1168 | External tool integration (Notion, custom MCP) fails unpredictably, breaking agentic workflows |

### Use Case Signals
- **Custom provider experimentation**: Users want to swap VLMs and image generators (#4132, #4167) — suggests research/evaluation use cases
- **Long-running autonomous agents**: MCP session drops (#4168) and history consolidation (#4169) indicate deployment beyond simple chat

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|:---|:---|:---|:---|
| [#1168](https://github.com/HKUDS/nanobot/issues/1168) — Notion MCP connection failure | ~3 months | Stale; no maintainer response | Low — integration-specific |
| [#4006](https://github.com/HKUDS/nanobot/issues/4006) — Orphaned tool results | ~1 week | **Active but unresolved** | **High** — fundamental to reasoning trace validity |
| [#3983](https://github.com/HKUDS/nanobot/pull/3983) — Test coverage for blocked tool-call finish reasons | ~10 days | Needs review/merge | **High** — `refusal`, `content_filter`, `error` boundaries are hallucination/safety-critical |

### Maintainer Attention Needed
- **#4006** requires deep investigation into conversation serialization; current fix (#3984) incomplete
- **#3983** adds test coverage for non-executable finish reasons — should merge for safety
- **#4169** is new but high-severity for long-context sessions

---

## Research Assessment

| Dimension | Score | Notes |
|:---|:---|:---|
| Multimodal reasoning | ⭐⭐☆☆☆ | Image generation extensibility only; no VLM architecture work visible |
| Long-context understanding | ⭐⭐⭐☆☆ | Active bug-fixing in history management (#4169, #4155); RAG memory merged (#4109) |
| Post-training alignment | ⭐☆☆☆☆ | No explicit RLHF, DPO, or preference learning infrastructure |
| AI reliability | ⭐⭐⭐☆☆ | Strong activity on tool-call integrity, session corruption, execution boundaries |

**Key Gap**: No visible research or engineering on **explicit hallucination detection**, **reasoning verification**, or **confidence calibration** for generated content. Reliability work is reactive (bug fixes) rather than proactive (architectural safeguards).

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent Project Digest — 2026-06-03

## 1. Today's Overview

Hermes Agent shows **high maintenance velocity** with 50 issues and 50 PRs active in the last 24 hours, though **zero new releases** indicate a stabilization period rather than feature shipping. The project is heavily focused on **reliability hardening** for production deployments—gateway file-descriptor leaks, streaming stall recovery, and desktop-updater robustness dominate merged work. Research-relevant activity is concentrated in **vision-language guardrails** (oversized image handling), **context-length/compression budgeting** for long-context models, and **prompt injection false positives** in tool-use channels. Notably absent: explicit multimodal model training or alignment methodology discussions, suggesting Hermes remains an inference/orchestration framework rather than a training system.

---

## 2. Releases

**None** — No releases published in the tracking period.

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant)

| PR | Description | Research Relevance |
|:---|:---|:---|
| [#37679](https://github.com/NousResearch/hermes-agent/pull/37679) | **fix(gateway): close ResponseStore + dispose unowned adapter on reconnect failure** | Infrastructure reliability for long-running agent sessions; prevents 12-hour zombie states from FD exhaustion |
| [#36101](https://github.com/NousResearch/hermes-agent/pull/36101) | chore(deps): bump tmp in /apps/desktop | Dependency hygiene (closed) |

### Open PRs Advancing

| PR | Description | Research Relevance |
|:---|:---|:---|
| [#37548](https://github.com/NousResearch/hermes-agent/pull/37548) | **fix(agent): respect model.context_length config** | Directly addresses **long-context understanding**—enforces user-configured context limits instead of defaulting to unknown behavior; fixes [#8430](https://github.com/NousResearch/hermes-agent/issues/8430) |
| [#37734](https://github.com/NousResearch/hermes-agent/pull/37734) | **fix(gateway): reliability hardening — streaming stall watchdog, Telegram poll heartbeat, supervised tasks, launchd respawn throttle** | **AI reliability** for streaming inference; prevents "alive but not doing its job" failure modes in persistent agent deployments |
| [#37753](https://github.com/NousResearch/hermes-agent/pull/37753) | **fix(cron): only silence exact [SILENT] marker** | **Post-training alignment** adjacent—improves interpretability of agent output by ensuring report content isn't suppressed spuriously |
| [#17124](https://github.com/NousResearch/hermes-agent/pull/17124) | **fix(honcho): fallback to durable peer cards for profiles** | Memory/persona consistency for agent identity—relevant to long-context persona retention |

---

## 4. Community Hot Topics

### Most Active Issues (by comment count)

| Issue | Comments | Analysis of Underlying Need |
|:---|:---|:---|
| [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) Cloud Sync for Configurations | 5 | **Infrastructure portability** for multi-device agent workflows; not research-relevant |
| [#18733](https://github.com/NousResearch/hermes-agent/issues/18733) Per-model compression threshold overrides | 5 | **Long-context optimization tension**—users need granular control as 1M+ context models (DeepSeek V4 Flash, MiMo V2.5 Pro, Gemini 2.5 Pro) make global thresholds suboptimal; signals need for **adaptive compression budgeting** |
| [#23717](https://github.com/NousResearch/hermes-agent/issues/23717) Pluggable SessionDB Provider | 4 | Production scalability; SQLite corruption under hot-update |
| [#7725](https://github.com/NousResearch/hermes-agent/issues/7725) session_search hangs 5+ minutes | 4 | **Retrieval reliability** for long-context session memory; timeout/cancellation architecture failure |
| [#36934](https://github.com/NousResearch/hermes-agent/issues/36934) `/steer` flagged as prompt injection by Opus 4.8 | 3 | **Critical alignment/reliability issue**: legitimate operator steering collides with model-level injection defenses; indicates **tool-channel architecture** needs segregation from user-input channels to avoid false positives |

### Research-Critical: Prompt Injection False Positive

**[#36934](https://github.com/NousResearch/hermes-agent/issues/36934)** reveals a **fundamental architecture tension**: when `/steer` (legitimate operator override) is delivered through the same channel as tool batches, high-resistance models (Claude Opus 4.8) misclassify it as adversarial injection. This is a **post-training alignment** problem where model safety tuning interferes with intended control mechanisms. The fix likely requires **channel segregation** or **cryptographic attestation** of steer commands.

---

## 5. Bugs & Stability

| Severity | Issue | Description | Fix PR? |
|:---|:---|:---|:---|
| **P1** | [#37677](https://github.com/NousResearch/hermes-agent/issues/37677) | **Oversized image (>8000px) permanently bricks conversation thread** — image guards check bytes, never pixel dimensions; Anthropic rejects with non-retryable 400, and replay on every turn | **Duplicate of [#25837](https://github.com/NousResearch/hermes-agent/issues/25837)** |
| **P1** | [#25837](https://github.com/NousResearch/hermes-agent/issues/25837) | Same root cause: `vision_analyze` / `browser_vision` inline screenshots without dimension checks | **None identified** — long-standing |
| **P1** | [#37733](https://github.com/NousResearch/hermes-agent/issues/37733) | **Security**: API server relays unredacted provider error messages to authenticated HTTP clients (CVSS 6.5-7.1) | None |
| **P1** | [#37011](https://github.com/NousResearch/hermes-agent/issues/37011) | File descriptor leak → gateway death after ~12h | **Fixed by [#37679](https://github.com/NousResearch/hermes-agent/pull/37679)** |
| **P2** | [#37689](https://github.com/NousResearch/hermes-agent/issues/37689) | Circuit-breaker blocks auto-resurrected by `recompute_ready` → deterministic-failure tasks loop forever (>5,400 `protocol_violation` runs in 11h) | None |
| **P2** | [#36934](https://github.com/NousResearch/hermes-agent/issues/36934) | `/steer` prompt injection false positive (see above) | None |
| **P2** | [#37662](https://github.com/NousResearch/hermes-agent/issues/37662) | httpx/OpenAI SDK hangs on IPv6 (happy-eyeballs failure) | None |

### Vision-Language Reliability Gap

**[#37677](https://github.com/NousResearch/hermes-agent/issues/37677)** / **[#25837](https://github.com/NousResearch/hermes-agent/issues/25837)** represent a **systematic vision-language failure mode**: the "fast path" optimizes for latency by inlining base64 images without validation, but this creates **unrecoverable sessions** when provider limits are violated. The guard checks file *bytes* (compression/size) but not *pixel dimensions*—a **multimodal reasoning** oversight where physical image properties aren't considered in the abstraction layer.

---

## 6. Feature Requests & Roadmap Signals

| Issue | Feature | Likelihood in Next Version | Rationale |
|:---|:---|:---|:---|
| [#18733](https://github.com/NousResearch/hermes-agent/issues/18733) | Per-model compression thresholds | **High** | Directly addresses 1M+ context model proliferation; PR-ready complexity |
| [#37719](https://github.com/NousResearch/hermes-agent/issues/37719) | Re-budget context compressor per router backend | **Medium-High** | Complements #18733; needed for `openrouter/auto` and fallback chains |
| [#36196](https://github.com/NousResearch/hermes-agent/issues/36196) | MinimaxM3 model support (1M context multimodal) | **Medium** | Provider expansion; configuration-only if API-compatible |
| [#23717](https://github.com/NousResearch/hermes-agent/issues/23717) | Pluggable SessionDB (PostgreSQL/MySQL) | **Medium** | Production demand; blocked by architectural decision on SQLite dependency |
| [#37709](https://github.com/NousResearch/hermes-agent/issues/37709) | Snap packaging | **Low** | Niche Linux distribution; not core research |

### Research-Relevant Signal: Adaptive Context Budgeting

**[#37719](https://github.com/NousResearch/hermes-agent/issues/37719)** explicitly calls for **dynamic context compression budgeting** when routers select different backends per request. This is a **long-context understanding** infrastructure need: the system must estimate or query context windows per-backend rather than assuming static configuration. Suggests emerging need for **context window discovery/negotiation protocols** in agent frameworks.

---

## 7. User Feedback Summary

### Pain Points

| Theme | Evidence | Severity |
|:---|:---|:---|
| **Vision pipeline fragility** | [#37677](https://github.com/NousResearch/hermes-agent/issues/37677), [#25837](https://github.com/NousResearch/hermes-agent/issues/25837) | **Critical** — permanent data loss (bricked threads) |
| **Gateway reliability at scale** | [#37011](https://github.com/NousResearch/hermes-agent/issues/37011), [#37689](https://github.com/NousResearch/hermes-agent/issues/37689), [#7725](https://github.com/NousResearch/hermes-agent/issues/7725) | **High** — production deployment blockers |
| **Configuration system inconsistency** | [#37751](https://github.com/NousResearch/hermes-agent/issues/37751), [#8515](https://github.com/NousResearch/hermes-agent/issues/8515), [#37609](https://github.com/NousResearch/hermes-agent/issues/37609) | **Medium** — model switching, toolset toggling fail silently |
| **Prompt injection false positives** | [#36934](https://github.com/NousResearch/hermes-agent/issues/36934) | **Medium** — breaks legitimate operator control |

### Use Cases Emerging

- **Multi-device agent continuity** ([#20510](https://github.com/NousResearch/hermes-agent/issues/20510))
- **VPS/cloud gateway + local desktop** hybrid deployments ([#37663](https://github.com/NousResearch/hermes-agent/issues/37663))
- **Deterministic failure handling** in kanban/autonomous workflows ([#37689](https://github.com/NousResearch/hermes-agent/issues/37689))

---

## 8. Backlog Watch

| Issue | Age | Issue | Why It Needs Attention |
|:---|:---|:---|:---|
| [#25837](https://github.com/NousResearch/hermes-agent/issues/25837) | ~3 weeks | Vision image dimension validation | **P2 but P1 impact** — duplicate filed ([#37677](https://github.com/NousResearch/hermes-agent/issues/37677)) indicates user hit rate increasing; no PR despite clear fix scope |
| [#7725](https://github.com/NousResearch/hermes-agent/issues/7725) | ~8 weeks | session_search hangs | Long-running reliability issue; timeout architecture needs redesign |
| [#18158](https://github.com/NousResearch/hermes-agent/issues/18158) | ~5 weeks | Node.js discovery in non-interactive shells | Affects CI/automation use cases; environment isolation problem |
| [#8515](https://github.com/NousResearch/hermes-agent/issues/8515) | ~8 weeks | Smart routing drops api_mode | Configuration propagation bug; breaks local inference setups |

### Research-Critical Gap: No Explicit Hallucination Tracking

Notably absent from the active issue corpus: **direct hallucination detection or mitigation features**. The closest proxy is [#36934](https://github.com/NousResearch/hermes-agent/issues/36934) (false positive injection detection) and [#37689](https://github.com/NousResearch/hermes-agent/issues/37689) (deterministic failure loops). Hermes appears to rely on **provider-level** (Anthropic, OpenAI) hallucination controls rather than framework-level verification—potential research opportunity for agent-native uncertainty quantification or cross-model consensus mechanisms.

---

*Digest generated from 50 issues, 50 PRs, 0 releases on 2026-06-03. Filtered for research relevance in multimodal reasoning, long-context understanding, post-training alignment, and AI reliability.*

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-06-03

## 1. Today's Overview

PicoClaw shows **moderate engineering activity** with 14 PR updates (5 merged/closed, 9 open) and 3 issue movements in the past 24 hours, alongside a new nightly build. The project's focus today centers on **reliability engineering**—particularly error classification for provider-specific failures, context window management, and session history integrity—rather than new capability development. Notably, multiple fixes target **long-context handling** (summarization thresholds, compression logic) and **multimodal API compatibility** (Zhipu GLM-5 vision errors), indicating maturation of core agent infrastructure. No vision-language model architecture or training methodology research is directly represented in today's activity. Community engagement remains low-to-moderate with minimal comment depth (most PRs have 0 comments).

---

## 2. Releases

| Version | Type | Notes |
|---------|------|-------|
| [v0.2.9-nightly.20260602.426046fc](https://github.com/sipeed/picoclaw/compare/v0.2.9...main) | Nightly | Automated build; no explicit changelog. Contains all merged fixes through commit `426046fc`. **Use with caution**—unstable. |

**No stable release.** The nightly suggests v0.2.9 is approaching stabilization but not yet released.

---

## 3. Project Progress

### Merged/Closed PRs Today (5 items)

| PR | Author | Research Relevance | Description |
|----|--------|-------------------|-------------|
| [#2991](https://github.com/sipeed/picoclaw/pull/2991) | chengzhichao-xydt | **AI Reliability / Fault Tolerance** | Replaces ad-hoc retry logic with unified **provider error classifier** for transient LLM HTTP errors. Eliminates immediate agent turn failure on OpenRouter/OpenAI 500-series errors when no fallback model exists. *Implication: More robust inference orchestration, reduced hallucination-triggering failures from incomplete turns.* |
| [#2989](https://github.com/sipeed/picoclaw/pull/2989) | yuxuan-7814 | **Multimodal / Vision-Language** | Adds Zhipu API error code 1210 to format error patterns, enabling fallback mechanism for **GLM-5-Turbo vision API failures** (WeChat image inputs). *Directly addresses vision-language pipeline reliability.* |
| [#2986](https://github.com/sipeed/picoclaw/pull/2986) | chengzhichao-xydt | Infrastructure | Adds `Stop()` to `SessionManager` to prevent goroutine leaks in test environments. |
| [#2993](https://github.com/sipeed/picoclaw/pull/2993) | afjcjsbx | — | Duplicate docs PR; closed. |
| [#2239](https://github.com/sipeed/picoclaw/pull/2239) | thanhtantran | — | Docker compose `privileged` flag; infrastructure. |

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|------|----------|----------|
| [#2404](https://github.com/sipeed/picoclaw/issues/2404) | 10 comments, 1 👍, stale | **Streaming HTTP config enhancement**—highest community engagement. Underlying need: Users want OpenAI-compatible streaming parity for real-time agent responses. *Research angle: Streaming affects token-level uncertainty calibration and hallucination detection timing.* |
| [#2984](https://github.com/sipeed/picoclaw/issues/2984) | 0 comments, 1 👍 | **Explicit turn completion signal** for WebSocket protocol. Underlying need: Deterministic agent state tracking for external clients. *Research angle: Turn boundaries critical for reasoning chain verification and intervention points.* |
| [#2943](https://github.com/sipeed/picoclaw/issues/2943) | 1 comment, closed | WeChat→GLM-5 vision failure. Resolved by #2989. |

**Insight:** The streaming config issue (#2404) has persisted since April with stale status—suggests architectural disagreement or prioritization conflict between latency optimization and system complexity.

---

## 5. Bugs & Stability

| Severity | Item | Status | Fix PR | Description |
|----------|------|--------|--------|-------------|
| **High** | [#2943](https://github.com/sipeed/picoclaw/issues/2943) / [#2989](https://github.com/sipeed/picoclaw/pull/2989) | **Fixed** | #2989 | **Vision-language pipeline failure**: Zhipu GLM-5-Turbo rejects WeChat image inputs with error 1210. Error classifier omission caused no fallback. *Research note: Provider-specific error code fragmentation is a systemic multimodal reliability risk.* |
| **High** | [#2992](https://github.com/sipeed/picoclaw/pull/2992) | Open | — | **Session history corruption**: v0.2.9 upgrade causes old messages to attach to new Web UI sessions via `PromoteAliasHistory` bug. *Data contamination risk for long-context reasoning.* |
| **Medium** | [#2991](https://github.com/sipeed/picoclaw/pull/2991) | **Fixed** | #2991 | Transient LLM errors killed agent turns; unified retry classifier now handles 500-series errors. |
| **Medium** | [#2987](https://github.com/sipeed/picoclaw/pull/2987) | Open | — | **Tool calls dropped during streaming**: `tool_calls` messages incorrectly filtered as "auxiliary" in active streams. *Breaks function-calling reasoning chains mid-generation—potential hallucination trigger.* |
| **Medium** | [#2990](https://github.com/sipeed/picoclaw/pull/2990) | Open | — | Web UI shows only last user message in multi-turn history. *Long-context display failure, not compression logic.* |
| **Low-Medium** | [#2988](https://github.com/sipeed/picoclaw/pull/2988) | Open | — | `summarize_token_percent` config ignored; context compression threshold hardcoded. *Misleading context window telemetry.* |
| **Low** | [#2986](https://github.com/sipeed/picoclaw/pull/2986) | **Fixed** | #2986 | Goroutine leak in SessionManager. |

---

## 6. Feature Requests & Roadmap Signals

| Item | Signal Strength | Research Relevance | Prediction |
|------|-----------------|-------------------|------------|
| [#2404](https://github.com/sipeed/picoclaw/issues/2404) Streaming HTTP config | ⭐⭐⭐ Medium | **Training/inference methodology**: Streaming changes token emission dynamics, affects reinforcement learning from human feedback timing | Likely v0.3.0; requires config schema change and provider adapter updates |
| [#2984](https://github.com/sipeed/picoclaw/issues/2984) Turn completion signal | ⭐⭐⭐ Medium | **Reasoning mechanisms**: Explicit boundaries enable chain-of-thought verification, tool-use orchestration | Protocol-level; may merge with WebSocket v2 refactor |
| [#2945](https://github.com/sipeed/picoclaw/pull/2945) `picoclaw-tracer` debug UI | ⭐⭐ Low | **AI reliability / interpretability**: Per-turn LLM trace inspection (system prompt, messages, tools, metadata) | Standalone binary; useful for hallucination root-cause analysis but not core feature |

**No direct signals** for: vision-language model training, multimodal reasoning architectures, post-training alignment methods, or hallucination reduction techniques.

---

## 7. User Feedback Summary

| Pain Point | Evidence | Severity |
|------------|----------|----------|
| **Vision API fragility** | [#2943](https://github.com/sipeed/picoclaw/issues/2943) WeChat→GLM-5 image failures | High for multimodal users |
| **Context window opacity** | [#2968](https://github.com/sipeed/picoclaw/issues/2968) / [#2988](https://github.com/sipeed/picoclaw/pull/2988), [#2985](https://github.com/sipeed/picoclaw/pull/2985) Users cannot verify actual summarization vs. compression thresholds | Medium |
| **Session history corruption** | [#2992](https://github.com/sipeed/picoclaw/pull/2992) Upgrade breaks isolation between sessions | High for long-running deployments |
| **Streaming parity gap** | [#2404](https://github.com/sipeed/picoclaw/issues/2404) Lag behind standard OpenAI client behavior | Medium |
| **Provider-specific model quirks** | [#2948](https://github.com/sipeed/picoclaw/pull/2948) Claude Opus 4-7 rejects temperature; [#2951](https://github.com/sipeed/picoclaw/pull/2951) `web_search_preview` vs. `function` type | Medium—fragmentation tax |

**Satisfaction**: Infrastructure reliability improving (error classification, retry logic).  
**Dissatisfaction**: Configuration transparency, multimodal edge cases, and backward compatibility in upgrades.

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|------|-----|------|-------------------|
| [#2404](https://github.com/sipeed/picoclaw/issues/2404) Streaming HTTP config | ~8 weeks, stale | **High**—most commented open issue; no maintainer response recently | Streaming inference affects real-time hallucination detection and user trust calibration |
| [#2951](https://github.com/sipeed/picoclaw/pull/2951) Web search function-type fix | ~1 week, stale | Medium | Tool-use API compatibility |
| [#2948](https://github.com/sipeed/picoclaw/pull/2948) Claude Opus temperature skip | ~1 week, stale | Medium | Model-specific parameter handling—scalability concern for diverse model portfolios |
| [#2945](https://github.com/sipeed/picoclaw/pull/2945) Tracer debug UI | ~1 week, stale | Low | Interpretability tooling; low maintainer priority likely due to standalone scope |

**Recommendation for researchers monitoring:** [#2404](https://github.com/sipeed/picoclaw/issues/2404) streaming config is the highest-impact unresolved item for understanding PicoClaw's inference-time behavior and user interaction patterns.

---

*Digest generated from GitHub activity 2026-06-02 to 2026-06-03. All links: https://github.com/sipeed/picoclaw*

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw Project Digest — 2026-06-03
*Research Focus: Multimodal Reasoning, Long-Context Understanding, Post-Training Alignment, AI Reliability*

---

## 1. Today's Overview

NanoClaw exhibited moderate engineering activity with **7 PRs updated** (4 merged/closed, 3 open) and **1 new issue** opened, but **zero new releases**. The day's changes are predominantly infrastructure-hardening and integration plumbing rather than core model or research-adjacent advancements. Notably, the sole issue (#2673) involves a **vision-language prompt specification** (AI video generation for student grading), which touches multimodal capabilities but appears to be a user request for generative output rather than a system capability enhancement. No PRs directly address vision-language reasoning, training methodologies, hallucination mitigation, or alignment research. The project appears to be in a **stabilization phase** focused on runtime reliability and channel integration robustness.

---

## 2. Releases

**None** — No new versions published.

---

## 3. Project Progress

### Merged/Closed PRs (4 items)

| PR | Description | Research Relevance |
|:---|:---|:---|
| [#2674](https://github.com/nanocoai/nanoclaw/pull/2674) — **CLOSED** | Standardize runtime status messages as mechanical labels; add metadata/internal-channel guards to prevent self-loops | **Low** — Operational reliability; self-loop prevention is a minor robustness signal |
| [#1193](https://github.com/nanocoai/nanoclaw/pull/1193) — **CLOSED** | Host-side plugin hook system (`onStartup`/`onShutdown`) | **Low** — Extensibility infrastructure; no direct training or reasoning impact |
| [#2069](https://github.com/nanocoai/nanoclaw/pull/2069) — **CLOSED** | Webchat skill v1 (channel integration) | **None** — Product feature |
| [#2538](https://github.com/nanocoai/nanoclaw/pull/2538) — **CLOSED** | Container-runner package name validation (CWE-78 OS command injection fix) | **Low** — Security hardening; reliability-adjacent |

**Assessment:** No advances in multimodal reasoning, training methodologies, or alignment mechanisms. The runtime status standardization (#2674) offers marginal relevance to **AI reliability** through structured observability and self-loop prevention in agent execution loops.

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|:---|:---|:---|
| [#2673](https://github.com/nanocoai/nanoclaw/issues/2673) — Automated Student Grading System | 0 comments, 0 reactions; opened 2026-06-02 | **Vision-language relevance detected.** Issue contains detailed prompt for AI-generated video: "Papua New Guinea secondary school teacher... reviewing student examination results on an Android smartphone... Spreadsheet displays student names, marks, rankings... Ultra realistic photography." |

**Underlying Need:** This represents a **multimodal content generation use case** (text-to-video with structured data visualization), not a system capability request. The specification includes:
- **Visual grounding requirements**: Realistic photography, specific geographic/cultural context (Lae, PNG), device-specific rendering (Android smartphone)
- **Structured data integration**: Spreadsheet with names, marks, rankings, class positions
- **Scene composition**: Foreground subject + background activity (students studying)

**Research Signal:** Users are pushing vision-language systems toward **culturally situated, data-rich visual outputs** with high fidelity requirements. This strains current systems on: (a) text-to-video hallucination of structured data, (b) cultural/geographic accuracy, (c) realistic human depiction. However, this is filed as an application concept, not a bug report or feature request for NanoClaw's core capabilities.

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **Medium** | [#2672](https://github.com/nanocoai/nanoclaw/pull/2672) — OPEN | **MCP union compatibility break + HTTP-only transport failure behind proxies** | Fix proposed, awaiting merge |
| **Medium** | [#2671](https://github.com/nanocoai/nanoclaw/pull/2671) — OPEN | **Missing inbound attachments mount in agent containers** — formatter references non-existent path | Fix proposed, awaiting merge |
| **Medium** | [#2538](https://github.com/nanocoai/nanoclaw/pull/2538) — CLOSED | OS command injection via crafted package names (CWE-78) | **Fixed** |
| **Low** | [#2187](https://github.com/nanocoai/nanoclaw/pull/2187) — OPEN | CLI bare platform IDs incorrectly namespaced | Fix proposed, awaiting merge |

**Research-Relevant Stability Notes:**

- **#2672 (MCP compatibility)**: The `McpServerConfig` union evolution (`stdio | http | sse`) and Codex provider's stale interface assumption indicates **schema drift in model context protocol specifications**. This is a **reliability concern for tool-use reasoning** — when LLM tool-calling interfaces change, downstream reasoning chains break silently. The HTTP-only transport proxy issue further complicates **secure deployment of reasoning agents in enterprise environments**.

- **#2671 (attachments mount)**: Missing filesystem bindings between channel adapters and agent containers create **context fragmentation** — attachments visible to formatters but inaccessible to execution environments. This is a **long-context understanding failure mode**: relevant information is referenced but not actually loaded into the reasoning context.

---

## 6. Feature Requests & Roadmap Signals

**No explicit feature requests** filed today. Inferred signals from activity:

| Signal | Source | Likelihood in Next Version |
|:---|:---|:---|
| Enhanced attachment/media handling | #2671 fix pattern | **High** — Infrastructure gap being actively patched |
| Codex/MCP provider stabilization | #2672, #2674 | **High** — Active development branch (`providers`) |
| Runtime observability/telemetry | #2674 standardization | **Medium** — Foundation laid, may expand |
| Multimodal input processing (vision) | #2673 user demand | **Low** — No system-level work visible; user is requesting output generation, not input capability |

**No alignment, hallucination mitigation, or training methodology features** are in active development based on visible PRs.

---

## 7. User Feedback Summary

| Pain Point | Evidence | Severity |
|:---|:---|:---|
| **Attachment handling broken in containerized agents** | #2671 — "mount target the formatter references actually exists" | Operational blocker for file-based workflows |
| **MCP/tool-calling schema instability** | #2672 — union compatibility break between trunk and Codex provider | Integration friction for external tool use |
| **Proxy-unfriendly HTTP transport** | #2672 — "HTTP-only transport behind proxies" | Enterprise deployment barrier |
| **Runtime status message inconsistency** | #2674 — "standardize long-running runtime status messages" | Observability/debugging friction |

**No direct feedback** on: reasoning quality, hallucination frequency, long-context accuracy, multimodal understanding, or alignment behavior.

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|:---|:---|:---|:---|
| [#2187](https://github.com/nanocoai/nanoclaw/pull/2187) — CLI platform ID namespacing | ~1 month (created 2026-05-02, last updated 2026-06-02) | **Low** — Niche CLI channel issue; fix pattern established | None |
| [#1193](https://github.com/nanocoai/nanoclaw/pull/1193) — Plugin hook system | ~2.5 months (created 2026-03-17, closed 2026-06-02) | **Resolved** | None |

**No long-unanswered issues** with research relevance are visible in today's data. The project backlog appears actively triaged.

---

## Research Assessment Summary

| Dimension | Status | Evidence |
|:---|:---|:---|
| **Vision-Language Capabilities** | ⚠️ **Peripheral** | User demand (#2673) for video generation; no system development |
| **Reasoning Mechanisms** | ❌ **No visible activity** | No PRs/issues on chain-of-thought, tool use reasoning, planning |
| **Training Methodologies** | ❌ **No visible activity** | No fine-tuning, RL, SFT, or data curation work |
| **Hallucination/Reliability** | ⚠️ **Indirect** | #2672 schema drift affects tool-use reliability; #2671 context fragmentation |

**Overall Project Health:** Stable engineering velocity with focus on runtime infrastructure. **Research-relevant innovation appears stalled or occurring in non-public branches.** The gap between user multimodal demands (#2673) and system capabilities is notable. Recommend monitoring for alignment between generative output quality claims and actual structured data fidelity in vision-language applications.

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw Project Digest — 2026-06-03

## 1. Today's Overview

NullClaw showed minimal development activity over the past 24 hours, with one active issue and one corresponding open pull request addressing a PII redaction bug. No releases were published. The project appears to be in a maintenance phase with focused bug-fixing rather than feature expansion. The single active thread involves a concrete reliability issue where automated redaction incorrectly sanitizes system-generated timestamps, which has immediate implications for agent observability and debugging workflows. Activity level is **low**; no community discussion or maintainer engagement is yet visible on the open items.

---

## 2. Releases

**No new releases** — NullClaw has not published a version update today.

---

## 3. Project Progress

**No merged or closed PRs today.**

| PR | Status | Author | Summary |
|:---|:---|:---|:---|
| [#945](https://github.com/nullclaw/nullclaw/pull/945) | **OPEN** | vernonstinebaker | Proposes `isDateLike()` guard to prevent ISO date/time patterns from triggering phone number redaction |

The open PR represents the sole advancement attempt: a targeted fix in `src/redaction.zig` that would reject `YYYY-MM-DD hh` and `DD-MM-YYYY hh` patterns from `matchPhone` matching. The PR directly addresses the system prompt's `appendDateTimeSection` format (`{d}-{d:0>2}-{d:0>2} {d:0>2}`). Merge would restore timestamp visibility in agent logs but has not yet been reviewed or integrated.

---

## 4. Community Hot Topics

| Item | Activity | Analysis |
|:---|:---|:---|
| [#944](https://github.com/nullclaw/nullclaw/issues/944) PII redactor falsely matches date/time output as phone numbers | 0 comments, 0 reactions | **Underlying need:** Reliable output sanitization that preserves operational transparency. The `enable_pii_redaction=true` default (set May 2026) is over-capturing, creating a tension between privacy compliance and system debuggability. Users need deterministic redaction rules with explicit allow-listing for machine-generated metadata. |

No other active discussion threads exist. The absence of community engagement suggests either: (a) limited user base encountering this edge case, or (b) recent default change (`41cdb493`) has not yet propagated widely enough to surface broader reports.

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **Medium** | [#944](https://github.com/nullclaw/nullclaw/issues/944) | PII redactor false positives on ISO timestamps: `date` command output rendered as `[PHONE_X]` placeholders, obscuring agent execution traces | **Fix proposed** in [#945](https://github.com/nullclaw/nullclaw/pull/945) (unmerged) |

**Assessment:** This is a **regression-inducing default behavior** rather than a crash. The May 2026 commit enabling `enable_pii_redaction=true` by default introduced the issue. Impact is operational: degraded observability for time-sensitive agent debugging, potential confusion in multi-step reasoning traces where temporal ordering matters. No workaround documented beyond disabling redaction entirely.

---

## 6. Feature Requests & Roadmap Signals

No explicit feature requests emerged today. However, the incident suggests **implicit roadmap needs**:

| Signal | Likely Priority | Rationale |
|:---|:---|:---|
| Configurable redaction rule granularity | Medium-High | Current binary on/off with pattern-matching heuristics insufficient for production agent systems |
| Redaction rule testing/validation framework | Medium | No evident mechanism to prevent false-positive regressions when defaults change |
| Structured log metadata separation | Medium | System-generated timestamps should perhaps bypass text-level redaction entirely |

The PR's approach (pattern exclusion) is tactical; strategic solution may require architectural separation of machine-generated metadata from user/PII-facing content streams.

---

## 7. User Feedback Summary

**Direct pain point:** Agent operators cannot trust timestamp visibility in logs when PII redaction is enabled—a critical failure for debugging multi-turn reasoning or temporal agent behaviors.

**Implied dissatisfaction:** Default configuration changes (May 2026) introduced breaking behavior without apparent migration guidance or opt-in period. The single reporter (vernonstinebaker) is also the fix contributor, indicating **self-service response to unmet need** rather than maintainer-supported resolution.

**Use case at risk:** Any deployment relying on `date` or similar system command outputs within agent observation windows—common in tool-using LLM systems for temporal grounding.

---

## 8. Backlog Watch

| Item | Age | Attention Needed |
|:---|:---|:---|
| [#944](https://github.com/nullclaw/nullclaw/issues/944) / [#945](https://github.com/nullclaw/nullclaw/pull/945) | 1 day | **Maintainer review** — PR is ready with Zig implementation, awaiting merge or feedback |

No long-unanswered items are visible in today's data. However, the **speed of maintainer response to #945** will indicate project health: rapid merge suggests active maintenance; delay beyond 3-5 days with a ready fix would signal potential maintainer bandwidth constraints given the regression affects a default-enabled feature.

---

*Digest generated from NullClaw GitHub activity 2026-06-02 to 2026-06-03. All links: https://github.com/nullclaw/nullclaw*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw Project Digest — 2026-06-03
## Research Focus: Multimodal Reasoning, Long-Context Understanding, Post-Training Alignment, AI Reliability

---

## 1. Today's Overview

IronClaw shows **extremely high engineering velocity** with 79 total updates (29 issues, 50 PRs) in 24 hours, dominated by the "Reborn" architecture hardening initiative—a comprehensive correctness and safety audit yielding 11 sequential loop-hygiene issues (L1–L11) and 6 subagent correctness issues (C1–C6). No releases were cut, indicating this is an intensive stabilization phase. The project is clearly in a **pre-production reliability push** rather than feature expansion, with nearly all research-relevant activity concentrated on agent-loop correctness, safety gating, and token-budget accuracy. Notably, multiple model-specific integration failures (Qwen3.6-35B-A3B-FP8, MiniMax-M2.7, Claude Opus 4.7/4.8) suggest frontier model compatibility remains brittle at the tool-calling and parameter-sanitization layers.

---

## 2. Releases

**None** — No new releases published.

---

## 3. Project Progress

### Merged/Closed PRs with Research Relevance

| PR | Focus | Research Significance |
|:---|:---|:---|
| [#4371](https://github.com/nearai/ironclaw/pull/4371) | Fix Codex ChatGPT Reborn empty responses | **Hallucination/robustness**: Hardens SSE parsing for edge-case response formats; recovers malformed tool-call syntax via canonicalization helper—relevant to output reliability and tool-use alignment |
| [#4374](https://github.com/nearai/ironclaw/pull/4374) | Accept memory_search query aliases | **Long-context/retrieval**: Expands query interface robustness for memory retrieval, reducing model-format brittleness |
| [#4369](https://github.com/nearai/ironclaw/pull/4369) | Harden skill context budget contract tests | **Training/alignment methodology**: Validates `safe_summary`/`model_content` split—directly touches prompt safety and context budget management for trustworthy agent behavior |
| [#4357](https://github.com/nearai/ironclaw/pull/4357) | Fix local-dev Reborn memory mount | Infrastructure for memory-backed long-context experiments |
| [#4347](https://github.com/nearai/ironclaw/pull/4347) | Fix Reborn Gmail OAuth auth gate scopes | Security boundary hardening |
| [#4346](https://github.com/nearai/ironclaw/pull/4346) | Fix Gmail OAuth auth gate requirements | Credential requirement preservation—relevant to reliable tool authentication |
| [#4345](https://github.com/nearai/ironclaw/pull/4345) | Wire Notion DCR OAuth for Reborn WebUI | Product infrastructure; skip |
| [#4337](https://github.com/nearai/ironclaw/pull/4337) | Fix Google OAuth prompts for runtime auth gates | Authentication reliability |

---

## 4. Community Hot Topics

### Most Active Threads (by structural importance, not comment count—most have 0 comments due to batch filing)

| Issue/PR | Link | Underlying Research Need |
|:---|:---|:---|
| **L1–L11: Reborn Loop Architecture Hygiene** | [#4358](https://github.com/nearai/ironclaw/issues/4358)–[#4368](https://github.com/nearai/ironclaw/issues/4368) | **Core reliability engineering for autonomous agent loops**—gate replay validation, prompt safety wiring, capability validation hardening, budget accuracy, cancellation propagation, compaction/checkpoint correctness, loop strategies, and host-kernel dependencies |
| **C1–C6: Subagent Correctness** | [#4348](https://github.com/nearai/ironclaw/issues/4348)–[#4353](https://github.com/nearai/ironclaw/issues/4353) | **Multi-agent orchestration reliability**—durable completion delivery, exactly-once observer semantics, spawn compensation, safety gating, provenance tracking |
| **#4334: Claude Opus 4.7/4.8 temperature rejection** | [Issue](https://github.com/nearai/ironclaw/issues/4334) | **Model compatibility/parameter alignment**: Anthropic's deprecation of `temperature` for newer Claude variants exposes rigid parameter-sanitization logic |
| **#4341: Qwen3.6-35B chain-of-thought exposure** | [Issue](https://github.com/nearai/ironclaw/issues/4341) | **Reasoning control/hallucination**: Model's internal THINKING tokens leaked to user, stuck in thinking state—**directly relevant to reasoning transparency and output filtering** |
| **#4339: MiniMax-M2.7 tool call validation failures** | [Issue](https://github.com/nearai/ironclaw/issues/4339) | **Tool-use alignment**: Valid capability schemas rejected as `InvalidInvocation`—suggests schema validation brittleness across model providers |

**Analysis**: The batch-filed L and C issues represent a **systematic audit-driven hardening campaign**, likely from an internal correctness review or external security assessment. The density of "silent bypass" findings (prompt safety, capability validation, budget accounting) indicates prior architectural debt in defensive programming. The model-specific QA bugs suggest **frontier model integration testing is outpacing parameter-schema adaptability**.

---

## 5. Bugs & Stability

| Severity | Issue | Model/System | Research Relevance | Fix PR? |
|:---|:---|:---|:---|:---|
| **Critical** | [#4341](https://github.com/nearai/ironclaw/issues/4341): Agent THINKING CoT exposed to user, stuck in thinking state | Qwen3.6-35B-A3B-FP8 | **Reasoning mechanism failure**: Internal deliberation tokens surfaced; state machine deadlock | None visible |
| **Critical** | [#4334](https://github.com/nearai/ironclaw/issues/4334): Claude Opus 4.7/4.8 unusable—temperature always sent | Claude Opus 4.7/4.8 | **Model alignment**: Parameter deprecation handling | None visible |
| **High** | [#4339](https://github.com/nearai/ironclaw/issues/4339): Provider tool calls rejected despite valid schema | MiniMax-M2.7 | **Tool-use reliability/hallucination prevention**: False rejection of valid invocations | None visible |
| **High** | [#4344](https://github.com/nearai/ironclaw/issues/4344): Agent mirrors user message as its own response | Qwen3.6-35B-A3B-FP8 | **Output attribution failure**: Echo/parroting behavior—hallucination-like failure mode | None visible |
| **Medium** | [#4343](https://github.com/nearai/ironclaw/issues/4343): MCP integration acknowledged but unusable (driver failure) | Qwen3.6-35B-A3B-FP8 | Tool orchestration reliability | None visible |
| **Medium** | [#4340](https://github.com/nearai/ironclaw/issues/4340): Content field blank validation error blocks submission | Qwen3.6-35B-A3B-FP8 | Input validation brittleness | None visible |
| **Medium** | [#4338](https://github.com/nearai/ironclaw/issues/4338): Disconnected state shows misleading execution driver error | MiniMax-M2.7 | Error attribution reliability | None visible |
| **Medium** | [#4108](https://github.com/nearai/ironclaw/issues/4108): Nightly E2E failed | CI infrastructure | Regression detection | None visible |

**Research Note**: The **Qwen3.6-35B-A3B-FP8 cluster** (4 bugs) and **MiniMax-M2.7 cluster** (2 bugs) suggest **systematic compatibility gaps with newer open-weight and Chinese-proprietary models**, particularly around tool-calling formats, reasoning token handling, and parameter validation. The THINKING exposure bug is especially notable for **reasoning transparency research**—it demonstrates failure to properly filter or attribute model-generated reasoning traces.

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likely Priority |
|:---|:---|:---|
| **Capability catalog discoverability for WASM tools** | [#3806](https://github.com/nearai/ironclaw/issues/3806) (closed, reborn) | Medium—platform extensibility |
| **Trigger poller lifecycle + first-party capabilities** | [#4318](https://github.com/nearai/ironclaw/pull/4318) (merged), [#4375](https://github.com/nearai/ironclaw/pull/4375) (open) | High—autonomous agent scheduling |
| **Feishu/Lark websocket event intake** | [#4178](https://github.com/nearai/ironclaw/pull/4178) (open) | Medium—multimodal input channel expansion |
| **DISABLE_TOOLS_LIST security flag** | [#3548](https://github.com/nearai/ironclaw/pull/3548) (open) | High—tool-use safety/alignment |
| **Engine v2: channel-supplied thread/response IDs** | [#3669](https://github.com/nearai/ironclaw/pull/3669) (open) | Medium—observability/correlation for long-context tracking |

**Predicted near-term research-relevant additions**:
- Model-agnostic parameter sanitization (addressing #4334 pattern across providers)
- Reasoning token filtering/attribution controls (addressing #4341)
- Structured output validation hardening for non-OpenAI tool-call formats

---

## 7. User Feedback Summary

### Pain Points (from QA/bug reports)

| Theme | Evidence | Severity |
|:---|:---|:---|
| **Model-specific brittleness** | 6 bugs across 3 distinct model families in 24h | Critical for multi-model deployment |
| **Reasoning token handling** | #4341 (exposed THINKING), #4344 (echo behavior) | High—user trust and output quality |
| **Tool-call validation inconsistency** | #4339 (false rejections), #4334 (parameter rejection) | High—functional correctness |
| **State machine robustness** | #4341 (stuck thinking), #4343 (driver failure) | Medium—session reliability |

### Implicit Research Needs

- **Post-training alignment for tool-use**: Models diverge significantly in tool-calling format adherence; IronClaw's validation layer appears insufficiently robust to this variance
- **Reasoning transparency controls**: Need for configurable reasoning token filtering (show/hide/attribute) with state-machine safeguards against deadlock
- **Long-context session integrity**: Thread/response ID correlation (#3669) and checkpoint durability (#4366, #4368) suggest active investment in recoverable long-horizon interactions

---

## 8. Backlog Watch

| Item | Age | Research Relevance | Risk |
|:---|:---|:---|:---|
| [#3548](https://github.com/nearai/ironclaw/pull/3548): DISABLE_TOOLS_LIST flag + security regression test | ~3 weeks | **Tool-use safety/alignment**: Prevents specific tool exposure to LLM; defense-in-depth for capability control | Stale; needs maintainer review |
| [#3669](https://github.com/nearai/ironclaw/pull/3669): Engine v2 channel-supplied thread/response IDs | ~3 weeks | **Long-context observability**: Enables cross-turn correlation for external side-effects | Active; follow-up #4355 closed |
| [#4178](https://github.com/nearai/ironclaw/pull/4178): Feishu websocket event intake | ~1 week | **Multimodal input**: Alternative to webhook for real-time message ingestion | Moderate activity |
| [#4108](https://github.com/nearai/ironclaw/issues/4108): Nightly E2E failed | 1 week | **Regression detection reliability** | Recurring; may indicate flaky tests or real instability |

---

## Research Analyst Notes

**Key observation**: IronClaw's current phase is dominated by **correctness engineering for autonomous agent loops** rather than capability expansion. The L1–L11 and C1–C6 issue clusters represent a methodical audit of failure modes in:
- **Safety gating** (prompt injection scanning, capability filtering)
- **Resource accounting** (token budgets, wall-clock limits, CJK token handling)
- **Durability** (checkpoints, compaction, cancellation)
- **Observability** (audit provenance, completion delivery guarantees)

For researchers tracking **AI reliability and alignment in production agent systems**, this codebase is currently exhibiting best-practice patterns in systematic defensive programming—while simultaneously revealing how frontier model heterogeneity (Qwen, MiniMax, Claude variants) stress-tests these assumptions.

**Hallucination-relevant finding**: #4341 (THINKING exposure) and #4344 (message echo) are not classical hallucinations but **output attribution failures**—the system fails to correctly attribute or filter model-generated content. This suggests the boundary between "model internal state" and "user-visible output" needs stronger architectural enforcement, particularly for reasoning-capable models.

**Tool-use alignment finding**: #4339 (false rejections) and #4334 (parameter rejection) indicate that **provider-specific parameter schemas and validation logic** remain a significant integration hazard. The lack of model-agnostic parameter sanitization is a systemic gap with implications for reliable multi-model deployment.

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI Project Digest — 2026-06-03

## Research-Focused Filter Applied: Vision-Language Capabilities, Reasoning Mechanisms, Training Methodologies, Hallucination-Related Issues

---

## 1. Today's Overview

LobsterAI shows **moderate engineering velocity** with 50 PRs updated in the last 24 hours (47 merged/closed, 3 open), though **zero issues activity** suggests limited external research community engagement or bug reporting. The project appears to be in a **product stabilization phase** rather than active multimodal research development. Notably, the most research-relevant update is the **MiniMax-M3 vision-language integration fix** (PR #2093), correcting a hardcoded capability flag that falsely disabled image input support. A **thinking level control mechanism** (PR #1985) was recently merged, indicating nascent reasoning controllability features. However, the majority of activity concerns UI polish, IM platform integrations, and Electron infrastructure—areas largely peripheral to core multimodal reasoning research.

---

## 2. Releases

**None** — No new releases published.

---

## 3. Project Progress

### Research-Relevant Merged/Closed PRs

| PR | Research Relevance | Details |
|:---|:---|:---|
| **[#2093](https://github.com/netease-youdao/LobsterAI/pull/2093)** | **Vision-Language Capabilities** | Fixed hardcoded `supportsImage: false` for MiniMax-M3, enabling actual image input support. Corrects provider definition priority bug in `resolveModelSupportsImage()`. [netease-youdao/LobsterAI#2093](https://github.com/netease-youdao/LobsterAI/pull/2093) |
| **[#1985](https://github.com/netease-youdao/LobsterAI/pull/1985)** | **Reasoning Mechanisms** | Added `ThinkingLevelSelector` with Off/Minimal/Low/Medium/High/Adaptive levels, fully integrated through DB migration, Redux, IPC, and runtime adapter. Session-scoped or global default configuration. [netease-youdao/LobsterAI#1985](https://github.com/netease-youdao/LobsterAI/pull/1985) |
| **[#2015](https://github.com/netease-youdao/LobsterAI/pull/2015)** | **Tool Use / Reliability** | Handled OpenClaw compaction retries and tool result gaps—relevant to long-context reliability and cascading failure modes in agentic systems. [netease-youdao/LobsterAI#2015](https://github.com/netease-youdao/LobsterAI/pull/2015) |

### Excluded (Non-Research)
- PRs #2096, #2095, #2094, #2092, #2091, #1952, #1962, #2022, #2018, #2023, #2024, #2031, #2025, #2028: UI/UX, IM platform management, Electron dependency updates, plugin visibility, voice input permissions, security monitoring toggles, browser/webfetch stability, gateway restart optimization

---

## 4. Community Hot Topics

**No active issues or commented PRs.** All 50 PRs show `Comments: undefined` and `👍: 0`, indicating:
- Minimal external research community participation
- Possible use of internal review tools (PR descriptions in mixed Chinese/English suggest NetEase Youdao internal development)
- No public discourse on multimodal capabilities, reasoning transparency, or hallucination mitigation

**Most structurally significant open PR:**
- **[#388](https://github.com/netease-youdao/LobsterAI/pull/388)** [OPEN, stale since 2026-03-12]: MiniMax-M3 default model upgrade—blocked or deprioritized, yet contains the provider configuration changes that enabled #2093's vision fix. [netease-youdao/LobsterAI#388](https://github.com/netease-youdao/LobsterAI/pull/388)

---

## 5. Bugs & Stability

| Severity | Item | Research Relevance | Status |
|:---|:---|:---|:---|
| **High** | **MiniMax-M3 image support falsely disabled** (PR #2093) | **Vision-language capability misreporting**—models advertised as supporting images were blocked by hardcoded provider flags, creating **capability hallucination** in the system layer | **Fixed** 2026-06-02 |
| Medium | OpenClaw compaction retries & tool result gaps (PR #2015) | Long-context/agentic reliability—message compaction failures could cause **context loss or tool execution drift** | Fixed 2026-05-19 |
| Medium | Browser/webfetch stability improvements (PR #2023) | External tool use reliability for web-grounded reasoning | Fixed 2026-05-20 |
| Low | Gateway restart optimization (PR #2024, #2018) | Infrastructure stability, not core reasoning | Fixed |

**Notable pattern:** The #2093 bug represents a **system-level hallucination** where the UI/infrastructure falsely claimed a model lacked vision capabilities—a failure mode relevant to AI reliability research on capability grounding.

---

## 6. Feature Requests & Roadmap Signals

### Observed (Implemented, Not Requested)
| Feature | PR | Implication |
|:---|:---|:---|
| Thinking level control (Off→Adaptive) | #1985 | **Reasoning budget/depth controllability**—aligns with inference-time compute scaling research, chain-of-thought moderation, and potential hallucination reduction via constrained reasoning |
| MiniMax-M3 vision enablement | #2093, #388 | **Multimodal model integration**—expanding vision-language input pipeline |

### Gaps (No Evidence)
- **No explicit hallucination detection/mitigation PRs**
- **No multimodal evaluation benchmarks or red-teaming infrastructure**
- **No training methodology disclosures** (fine-tuning, RLHF, DPO, etc.)
- **No long-context evaluation or context window stress testing**

**Prediction:** Thinking level control (#1985) suggests imminent **reasoning transparency features** (e.g., showing/hiding chain-of-thought, adaptive depth based on query complexity). Next likely additions: reasoning trace visualization, per-step confidence scores, or rejection mechanisms for uncertain reasoning paths.

---

## 7. User Feedback Summary

**No direct user feedback available** (zero issues, zero PR comments/reactions).

**Inferred pain points from PR content:**
- **Capability discoverability**: Hardcoded flags preventing users from accessing M3 vision features suggest **model capability metadata management is brittle**
- **MCP/tool integration latency**: PR #2091's npx resolution optimization and "first response timing logs" indicate **tool use latency is a measured concern**
- **Session management complexity**: Subagent batch deletion (PR #2095) and gateway cleanup concurrency limits suggest **multi-agent/long-running session orchestration is operationally challenging**

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|:---|:---|:---|:---|
| **[PR #388](https://github.com/netease-youdao/LobsterAI/pull/388)** MiniMax-M3 default upgrade | 83 days (stale) | **Medium**—superseded by #2093's partial fix, but provider configuration divergence may persist | Model versioning and capability advertisement accuracy |
| **[PR #1277](https://github.com/netease-youdao/LobsterAI/pull/1277)** Electron dependency bump | 62 days (stale) | Low | None—infrastructure only |
| **[PR #1464](https://github.com/netease-youdao/LobsterAI/pull/1464)** IM duplicate validation | 59 days (stale) | Low | None—integration layer |

**Critical absence:** No open issues or PRs addressing:
- Multimodal reasoning evaluation
- Hallucination measurement or mitigation
- Training/post-training alignment methodology
- Long-context understanding benchmarks (beyond compaction retry logic)

---

## Research Assessment Summary

| Dimension | Score | Evidence |
|:---|:---|:---|
| Vision-Language Integration | ⚠️ **Emerging** | M3 vision fix recent; no evaluation infrastructure visible |
| Reasoning Mechanisms | ⚠️ **Emerging** | Thinking level control added; no transparency into actual reasoning process |
| Training/Alignment Methodology | ❌ **Opaque** | No training-related PRs or documentation; pure inference system |
| Hallucination Mitigation | ❌ **Absent** | No dedicated detection, calibration, or reduction features |
| Long-Context Reliability | ⚠️ **Basic** | Compaction retry logic only; no context window stress testing |

**Overall:** LobsterAI appears to be a **consumer-facing application layer** (Electron-based desktop client) integrating external models (MiniMax, OpenClaw plugins) rather than a research platform advancing multimodal reasoning. The most research-relevant developments are **inference-time controllability** (thinking levels) and **capability grounding fixes** (vision flag correction)—both necessary but insufficient for advancing reliable multimodal AI.

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw Project Digest — 2026-06-03

## 1. Today's Overview

CoPaw (QwenPaw) shows **elevated maintenance activity** with 48 issues and 32 PRs updated in the last 24 hours, though **no new releases**. The project is in a **stabilization phase** ahead of a major architectural migration: AgentScope 2.0 backend upgrade dominates technical attention, with active PR #4846 under review. Security response is notably rapid—5 CVE-class issues reported and closed same-day by researcher YLChen-007. However, **research-relevant developments are sparse**: most activity centers on channel integrations (WeChat, Yuanbao), desktop packaging, and UI polish rather than core model capabilities, reasoning, or alignment research.

---

## 2. Releases

**None** — No new versions published today. Last version remains v1.1.10 (with v1.1.11b1 bump PR #4907 closed, suggesting imminent patch release).

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant Filtering)

| PR | Status | Research Relevance | Summary |
|:---|:---|:---|:---|
| [#4846](https://github.com/agentscope-ai/QwenPaw/pull/4846) | OPEN | **High** — Training/runtime architecture | AgentScope 1.x → 2.0 migration; affects all agent execution, tool calling, and context management primitives |
| [#4900](https://github.com/agentscope-ai/QwenPaw/pull/4900) | OPEN | Medium — System reliability | Decouples plugin loader from agent startup; fixes race conditions that could affect tool-use consistency |
| [#4804](https://github.com/agentscope-ai/QwenPaw/pull/4804) | OPEN | Medium — Prompt engineering | Prompt Section Registry for plugins; enables structured prompt composition without monkey-patching |
| [#4857](https://github.com/agentscope-ai/QwenPaw/pull/4857) | OPEN | Medium — Agent orchestration | Self-evolving skill creation via `spawn_subagent(fork=True)` with full context inheritance |
| [#4905](https://github.com/agentscope-ai/QwenPaw/pull/4905) | OPEN | Low — Browser automation | Coordinate-based clicking for browser_control (vision-grounding adjacent) |

**Excluded from research focus**: Cloudflared notifications (#1317), Tauri desktop links (#4683), PRD management tool (#4902), Windows drive browsing (#4906), MiMo provider (#4722), browser process cleanup (#4853), Yuanbao proto fix (#4899).

---

## 4. Community Hot Topics

### Most Commented Issues (with Research Angle Analysis)

| Issue | Comments | Link | Underlying Research Need |
|:---|:---|:---|:---|
| #4666 — Models config lost after new session | 6 | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4666) | **Session state persistence** — affects long-context continuity, a core concern for multi-turn reasoning research |
| #4878 — WeChat cron message delivery failure | 5 | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4878) | Channel reliability; not research-relevant |
| #4727 — Migrate to AgentScope 2.0 | 5 | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4727) | **Breaking change tracking** — new runtime model may alter agent execution semantics, tool-use patterns, observability |
| #4908 — Unauthenticated settings modification | 4 | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4908) | Security; not research-relevant |
| #3985 — DeepSeek `reasoning_content` not propagated in multi-turn | 4 | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/3985) | **CRITICAL for reasoning research** — Chain-of-thought truncation in tool-calling loops causes HTTP 500; directly impacts reasoning trace preservation and faithfulness |

### Research-Critical Deep Dive: #3985

**Closed but unresolved for research**: DeepSeek reasoning models fail after >5 turns because `reasoning_content` (the model's explicit chain-of-thought) is dropped from API callbacks. This is a **hallucination-inducing failure mode**: the model loses access to its own reasoning traces, forcing coherent continuation without structural guidance. The fix was applied but the pattern—reasoning content as second-class context—is architecturally fragile.

---

## 5. Bugs & Stability

### Research-Relevant Bugs (Ranked by Severity)

| Severity | Issue | Link | Description | Fix Status |
|:---|:---|:---|:---|:---|
| **Critical** | #4895 — Infinite image compression loop causing hallucination | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4895) | **Direct hallucination mechanism**: image compressed → re-injected → compressed again in infinite cycle; model receives progressively degraded visual input, generating confabulated descriptions | **OPEN, no fix PR** |
| **High** | #3985 — DeepSeek reasoning_content lost in multi-turn | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/3985) | Reasoning traces discarded; model operates without CoT guidance after tool calls | Closed, fix merged |
| **High** | #4837 — System fallback "无法处理您的问题" | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4837) | Silent degradation masking real model capabilities; affects evaluation validity | OPEN, root cause unclear |
| **Medium** | #4903 — Loading states break on chat switch | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4903) | UI state management; indirect impact on human-in-the-loop research | OPEN |
| **Medium** | #4919 — browser_use CDP timeout/Chrome crash | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4919) | Vision-grounding tool unreliable; affects web-based multimodal experiments | OPEN |

### #4895: Hallucination Bug — Detailed Analysis

> **"When uploading an image file, the system enters an infinite compression loop. The image is compressed repeatedly in a cycle: compressed → re-injected → compressed again, causing continuous repetition. This creates a 'hallucination'..."**

This is the **only explicitly hallucination-titled issue** in the dataset and represents a **multimodal reliability failure**. The compression-degradation-reinjection cycle means:
- **Vision-language capability compromised**: visual tokens become progressively noisier
- **Model confabulation inevitable**: degraded input forces plausible-sounding but ungrounded outputs
- **No automatic recovery**: loop continues until external intervention

**Research implication**: Systems using iterative image processing (screenshot loops, visual tool use) need compression idempotency guarantees.

---

## 6. Feature Requests & Roadmap Signals

### Research-Relevant Feature Requests

| Issue | Link | Signal | Likelihood in Next Version |
|:---|:---|:---|:---|
| #4551 — Lossless context compression (DAG-based + CJK token fix) | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4551) | **Long-context architecture** — DAG summarization preserving recoverable structure; CJK tokenization efficiency | Medium — complex, but addresses core pain point |
| #4836 — On-demand tool definition loading | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4836) | **Context efficiency** — 55-65% token reduction in tool-heavy agents; enables more tools without context overflow | High — aligns with AgentScope 2.0 efficiency goals |
| #4901 — Per-task model selection in `spawn_subagent` | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4901) | **Multi-model reasoning orchestration** — cheap models for simple tasks, main model for complex reasoning (Claude Code pattern) | Medium — PR #4857 provides partial infrastructure |
| #4841 — "Before You Build" skill (planning pause) | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4841) | **Deliberation mechanisms** — explicit planning phase before execution; reduces hallucinated implementations | Low — community skill, not core |

### Roadmap Prediction

AgentScope 2.0 migration (#4727/#4846) is the **blocking priority**. Research-relevant features (context compression, tool loading optimization) will likely ship **after** this migration stabilizes, targeting v1.2.0 or later.

---

## 7. User Feedback Summary

### Pain Points with Research Relevance

| Theme | Evidence | Research Implication |
|:---|:---|:---|
| **Context loss undermines long-horizon tasks** | #4551: "200K context compressed to 20K"; "early decision context compressed away" | Current summarization destroys recoverable information; need structured compression with retrieval |
| **Reasoning opacity in production** | #3985: reasoning_content silently dropped; #4837: fallback messages mask real behavior | Evaluation and debugging of reasoning systems requires trace preservation |
| **Visual input unreliability** | #4895: infinite compression loop; #4919: browser automation failures | Multimodal pipelines need degradation bounds and graceful failure modes |
| **Tool bloat consumes context budget** | #4836: 45+ tools consume 55-65% of initial context | Efficiency of tool representation affects effective reasoning horizon |

### Satisfaction Signals
- Rapid security response (5 CVEs closed same-day) indicates mature incident process
- Active plugin ecosystem (DataPaw, custom channels) suggests extensibility is valued

---

## 8. Backlog Watch

### Long-Standing Issues Needing Research Attention

| Issue | Age | Link | Why It Matters |
|:---|:---|:---|:---|
| #4551 — Lossless context compression | 14 days | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4551) | **Most upvoted research-relevant issue** (implicit priority); no maintainer response on DAG approach feasibility |
| #4154 — Font size, headless mode, clickable file paths | 25 days | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4154) | Headless mode specifically relevant for automated evaluation pipelines |
| #4727 — AgentScope 2.0 migration | 7 days | [Issue](https://github.com/agentscope-ai/QwenPaw/issues/4727) | Breaking change with unknown research impact; needs migration guide |

### Maintainer Attention Needed

- **#4895** (hallucination loop): No assignee, no fix PR despite severity
- **#4837** (fallback replies): Vague "session management" suspicion; needs root cause analysis
- **#4846** (AgentScope 2.0 PR): Under review; research community needs clarity on API compatibility guarantees

---

## Appendix: Research-Relevant Item Index

| Category | Items |
|:---|:---|
| Vision-language | #4895 (hallucination loop), #4919 (browser vision) |
| Reasoning mechanisms | #3985 (CoT propagation), #4551 (context preservation), #4841 (deliberation skill) |
| Training/methodologies | #4727/#4846 (AgentScope 2.0 runtime), #4836 (tool loading efficiency), #4901 (multi-model orchestration) |
| Hallucination | #4895 (compression loop), #3985 (reasoning loss → ungrounded continuation), #4837 (fallback masking) |

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

I'll analyze this GitHub data through a research lens focused on multimodal reasoning, long-context understanding, post-training alignment, and AI reliability, filtering out commercial/product noise.

---

# ZeroClaw Research Digest — 2026-06-03

## 1. Today's Overview

ZeroClaw shows **high engineering velocity** (49 issues, 50 PRs in 24h) with significant activity around **reasoning model integration failures** and **channel response sanitization**—both critical for AI reliability research. The v0.8.0-beta-2 release introduces terminal UI infrastructure but the deeper signal is continued fragility in how reasoning content (chain-of-thought, tool transcripts) leaks into user-facing outputs. Multiple provider-specific bugs (DeepSeek-V4, Kimi, Ollama) indicate the ecosystem is struggling with **heterogeneous reasoning format handling**, a core challenge for robust multimodal agent systems. Security and policy enforcement gaps (tool allowlist bypasses, pairing code weakness) suggest alignment infrastructure lags behind capability integration.

---

## 2. Releases

**v0.8.0-beta-2** — [Release Notes](https://github.com/zeroclaw-labs/zeroclaw/releases/tag/v0.8.0-beta-2)

| Aspect | Detail |
|--------|--------|
| **Headline** | `zerocode` — terminal UI for agent operation |
| **Research Relevance** | Multi-agent runtime infrastructure; TUI rendering of streaming tool calls and approval cycles |
| **Breaking/Notable** | ACP protocol extensions for diff/file-proposal message types (side-by-side diffs, counter-proposals during `file_edit`/`file_write`) — relevant to **human-in-the-loop alignment** and **tool-use verification** |
| **Migration Notes** | `crates/zeroclaw-tui` → `apps/zerocode` reorganization; no schema changes flagged |

*Commercial product features (terminal branding, onboarding flows) omitted as non-research-relevant.*

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant)

| PR | Focus | Research Relevance |
|----|-------|------------------|
| [#7070](https://github.com/zeroclaw-labs/zeroclaw/pull/7070) | Twitter/X channel inclusion in default features | Channel output consistency (foundational for multimodal deployment) |
| [#7116](https://github.com/zeroclaw-labs/zeroclaw/pull/7116) | OpenAI Codex provider docs | **Critical for reasoning research**: Documents Codex backend integration via OAuth, enabling study of delegated agent architectures vs. direct LLM API control |

### Advanced Features (In Progress)

| PR | Focus | Research Relevance |
|----|-------|------------------|
| [#7060](https://github.com/zeroclaw-labs/zeroclaw/pull/7060) | WIT interface files for Tool/Channel/Memory plugins (WASI Component Model) | **Long-term architecture for sandboxed, composable agent capabilities** — enables reproducible tool-use studies and memory module isolation |
| [#6982](https://github.com/zeroclaw-labs/zeroclaw/pull/6982) | Credential-shaped config classification | Security/alignment infrastructure for secret handling |
| [#7095](https://github.com/zeroclaw-labs/zeroclaw/pull/7095) | Ollama structured tools prompt-guided | **Tool-use reliability**: Fixes native tools payload conversion that broke prompt-guided tool behavior |

---

## 4. Community Hot Topics

### Most Active Issues (by Comment Count)

| Issue | Comments | Core Research Theme |
|-------|----------|-------------------|
| [#6059](https://github.com/zeroclaw-labs/zeroclaw/issues/6059) — DeepSeek-V4 API incompatibility | 15 | **Reasoning format fragmentation**: `thinking` mode causes API errors; provider-specific reasoning encoding breaks abstraction layers |
| [#5600](https://github.com/zeroclaw-labs/zeroclaw/issues/5600) — Kimi streaming error | 9 | **Reasoning content extraction failure**: `reasoning_content` missing in assistant message when `thinking` enabled — **hallucination-risk adjacent** (model claims reasoning mode active but content absent) |
| [#6391](https://github.com/zeroclaw-labs/zeroclaw/issues/6391) — Daemon heartbeat tracking | 4 | Distributed system liveness — less central to core research |

**Underlying Need Analysis**: The DeepSeek and Kimi issues reveal a **systematic gap in reasoning content negotiation**. Providers are implementing chain-of-thought extraction differently (XML blocks, JSON fields, streaming deltas), and ZeroClaw's provider abstraction is failing to normalize these. This directly impacts:
- **Post-training alignment** (how do we verify reasoning if we can't extract it consistently?)
- **Hallucination detection** (missing reasoning_content → inability to audit model's actual chain-of-thought)

---

## 5. Bugs & Stability

### High-Severity Research-Relevant Bugs

| Issue | Severity | Description | Fix Status | Research Implication |
|-------|----------|-------------|------------|----------------------|
| [#6040](https://github.com/zeroclaw-labs/zeroclaw/issues/6040) — `<think>...</think>` reasoning blocks leak into channel replies | **S2** | `sanitize_channel_response` fails to strip reasoning blocks for non-draft-update channels (webhook) | **CLOSED** | **Hallucination/UX failure**: Raw reasoning exposed to end users; breaks trust in agent outputs |
| [#5795](https://github.com/zeroclaw-labs/zeroclaw/issues/5795) — XML `tool_result` tags leak into channel responses | **S2** | Gemini-3-flash-preview returns raw `<tool_result>` blocks verbatim to channels | **OPEN** | **Tool-use verification failure**: Model output format confusion (XML vs. JSON) propagates to users |
| [#7068](https://github.com/zeroclaw-labs/zeroclaw/issues/7068) — Codex scratchpad/tool transcript as final response | **S1** | Telegram receives internal agent reasoning instead of user-facing answer | **OPEN** | **Critical alignment failure**: Delegated agent architecture (Codex) fails to distinguish internal computation from external communication — **directly a hallucination/control issue** |
| [#7063](https://github.com/zeroclaw-labs/zeroclaw/issues/7063) — Channel agents bypass tool allowlist | **S1** | `start_channels` skips `apply_policy_tool_filter`; `SecurityPolicy.allowed_tools` ignored | **CLOSED** | **Safety/alignment bypass**: Policy enforcement inconsistency between direct and channel-served agents |

### Pattern: Reasoning Content Leakage

Three distinct failure modes of **internal computation escaping to user-facing channels**:
1. Explicit reasoning blocks (`<think>`)
2. Tool result formatting artifacts (XML tags)
3. Full agent scratchpad transcripts (Codex delegation)

This suggests **no unified internal/external output boundary** exists in the architecture — a fundamental reliability gap for deployed agents.

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Signal | Likely Version | Research Relevance |
|----------|--------|--------------|----------------------|
| [#6293](https://github.com/zeroclaw-labs/zeroclaw/issues/6293) — Air-gapped execution with companion daemon | **Sandboxing/TEE support** | v0.9+ | **Critical for trustworthy agent deployment**: Isolates tool execution from network; enables verifiable inference environments |
| [#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820) — ACP diff/file-proposal message types | v0.8.x shipped | **Human-in-the-loop verification**: Structured counter-proposals for file edits improve oversight |
| [#7117](https://github.com/zeroclaw-labs/zeroclaw/issues/7117) — Config UX parity across surfaces | v0.8.x | Less research-relevant |
| [#6970](https://github.com/zeroclaw-labs/zeroclaw/issues/6970) — v0.8.1 integration queue | Tracking | Provider/tool expansion |

**Predicted Research-Critical Addition**: Air-gapped mode (#6293) combined with WIT plugin interfaces (#7060) suggests a trajectory toward **verifiable, sandboxed agent execution** — enabling reproducible benchmarks for tool-use safety and capability evaluation.

---

## 7. User Feedback Summary

### Pain Points (Research-Relevant)

| Theme | Evidence | Implication |
|-------|----------|-------------|
| **Reasoning format incompatibility** | DeepSeek-V4, Kimi, Ollama all have provider-specific failures | **Multimodal/long-context models are outpacing agent framework abstractions**; provider diversity creates reliability cliffs |
| **Internal computation leakage** | #6040, #5795, #7068 | Users cannot trust agent output boundaries; **hallucination-adjacent failures** where model "talks to itself" in user channels |
| **Policy enforcement inconsistency** | #7063 (tool allowlist bypass) | **Alignment/safety guarantees fail silently** depending on deployment path (direct vs. channel) |
| **Delegated agent opacity** | #7068 (Codex scratchpad leak) | **Post-training alignment challenge**: When agent delegates to another agent (Codex), control over output boundaries degrades |

### Satisfaction Signals
- TUI/diff visualization (#6824, #6820): Users value **structured oversight of agent actions**
- ACP console (#7036): Direct protocol access enables debugging and verification

---

## 8. Backlog Watch

### Long-Standing Critical Issues Needing Attention

| Issue | Age | Blocker | Research Risk |
|-------|-----|---------|---------------|
| [#5600](https://github.com/zeroclaw-labs/zeroclaw/issues/5600) — Kimi reasoning_content missing | ~8 weeks | Provider API behavior | **Cannot reliably extract chain-of-thought from major provider** — blocks reasoning audit research |
| [#5795](https://github.com/zeroclaw-labs/zeroclaw/issues/5795) — XML tool_result leak | ~7 weeks | No assignee; needs repro | **Ongoing hallucination-like output corruption** |
| [#6074](https://github.com/zeroclaw-labs/zeroclaw/issues/6074) — 153 commits lost in bulk revert recovery | ~10 weeks | Audit complexity | **Historical capability/alignment research compromised** — cannot trace when specific behaviors introduced |

### Maintainer Attention Needed
- [#6293](https://github.com/zeroclaw-labs/zeroclaw/issues/6293) (air-gapped mode): Blocked on architecture review; **high-value for safety research**
- [#6970](https://github.com/zeroclaw-labs/zeroclaw/issues/6970) (v0.8.1 queue): Coordination bottleneck for provider integration quality

---

## Research Synthesis

ZeroClaw's activity reveals **three converging stressors on agent reliability**:

1. **Reasoning format heterogeneity** breaks extraction and audit capabilities — fundamental to post-training alignment verification
2. **No robust internal/external boundary** causes systematic leakage of computation artifacts — a core hallucination mechanism
3. **Policy enforcement path-dependency** (direct vs. channel vs. delegated) creates alignment guarantee holes

The WIT/WASI plugin architecture and air-gapped execution mode suggest correct long-term directions, but near-term reliability is constrained by provider-specific adapter fragility rather than principled abstraction.

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*