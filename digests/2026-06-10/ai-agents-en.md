# OpenClaw Ecosystem Digest 2026-06-10

> Issues: 453 | PRs: 497 | Projects covered: 13 | Generated: 2026-06-10 00:36 UTC

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

# OpenClaw Project Digest — 2026-06-10

## 1. Today's Overview

OpenClaw shows **very high development velocity** with 453 issues and 497 PRs active in the last 24 hours, indicating a large-scale release cycle around v2026.6.5. The project is heavily focused on **infrastructure hardening** (auth, session state, message routing) rather than core model capabilities. Notably, **reasoning scaffolding leakage** received immediate patch attention in both stable and beta releases, suggesting production urgency around LLM output sanitization. Research-relevant activity is sparse—no direct multimodal training, vision-language architecture, or hallucination mitigation work is visible in today's top issues. The community is preoccupied with **messaging channel reliability**, **tool-call trace sanitization**, and **session state management** rather than model behavior research.

---

## 2. Releases

### v2026.6.5 (stable) & v2026.6.5-beta.6
- **GitHub**: [v2026.6.5](https://github.com/openclaw/openclaw/releases/tag/v2026.6.5) | [v2026.6.5-beta.6](https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.6)

| Change | Research Relevance |
|--------|------------------|
| **QQBot strips `<thinking>` reasoning scaffolding** (#89913, #90132) | **Directly relevant**: Prevents raw chain-of-thought / reasoning traces from leaking to end users. Related to **post-training alignment** and **controllable generation**—ensuring model reasoning remains internal. |
| **MCP tool result coercion for `resource_link`, `resource`, `audio`, malformed images** | **Moderately relevant**: Robustness in multimodal tool outputs; handles malformed image data gracefully. |

**No breaking changes or migration notes** explicitly documented. Both releases share identical changelogs, suggesting beta.6 → stable promotion with no additional changes.

---

## 3. Project Progress

### Merged/Closed PRs Today (Research-Relevant Filter Applied)

| PR | Status | Summary | Research Relevance |
|----|--------|---------|------------------|
| [#91750](https://github.com/openclaw/openclaw/pull/91750) | **CLOSED** | Enforce native web search tool policy across all policy layers | **Relevant to AI reliability**: Gates provider-native `web_search` behind comprehensive tool policy, preventing unauthorized information retrieval |
| [#91787](https://github.com/openclaw/openclaw/pull/91787) | **CLOSED** | TTS legacy migration path preservation | Low relevance |
| [#91757](https://github.com/openclaw/openclaw/pull/91757) | **CLOSED** | Retired skill workshop plugin warning clarification | Low relevance |
| [#91780](https://github.com/openclaw/openclaw/pull/91780) | **CLOSED** | Drain restored chat queue after session switch | Low relevance |
| [#91782](https://github.com/openclaw/openclaw/pull/91782) | **CLOSED** | Voice-call WebSocket path boundary (superseded by #91784) | Low relevance |

### Notable Open PRs Advancing

| PR | Area | Research Relevance |
|----|------|------------------|
| [#91790](https://github.com/openclaw/openclaw/pull/91790) | Google Gemini CLI image capability shim | **Vision-language**: Fixes false `UnsupportedAttachmentError` for image inputs to Gemini models—capability detection bug |
| [#91594](https://github.com/openclaw/openclaw/pull/91594) | Codex memory recall guidance restoration | **Long-context understanding**: Ensures memory capability activates before rendering memory recall guidance in Codex turns |
| [#91770](https://github.com/openclaw/openclaw/pull/91770) | Memory search embedding abort on timeout | **Reliability**: Prevents hanging embedding operations from cascading failures |
| [#84792](https://github.com/openclaw/openclaw/pull/84792) | Memory flush before preflight compaction | **Long-context**: Preserves memory state before aggressive context compaction |

---

## 4. Community Hot Topics

### Most Active Issues (by comment count, filtered for research relevance)

| Issue | Comments | Status | Core Concern | Research Angle |
|-------|----------|--------|--------------|--------------|
| [#25592](https://github.com/openclaw/openclaw/issues/25592) | 29 | OPEN | **Text between tool calls leaks to messaging channels** | **Hallucination/artifact leakage**: Internal processing output (errors, acknowledgments, narration) surfaces to users—similar to reasoning scaffolding leakage |
| [#88312](https://github.com/openclaw/openclaw/issues/88312) | 15 | OPEN | **Codex turn-completion stall regression** | **Session state / reasoning reliability**: Multi-tool agent turns fail with "stopped before confirming turn complete"—orchestration failure in complex reasoning chains |
| [#87307](https://github.com/openclaw/openclaw/issues/87307) | 14 | OPEN | Matrix thread reply routing regression | Low relevance (channel-specific) |
| [#73424](https://github.com/openclaw/openclaw/issues/73424) | 10 | **CLOSED** | **"Failed to optimize image" in VLM preprocessing** | **Vision-language pipeline**: Built-in `image` tool fails with `nvidia/google/gemma-4-31b-it` despite direct API working—preprocessing vs. model capability mismatch |
| [#74586](https://github.com/openclaw/openclaw/issues/74586) | 9 | OPEN | **AM embedded run aborts `memory_search` as timeout** | **Long-context / reliability**: False timeout classification when model actually completed—measurement/reward hacking in timeout logic |

### Underlying Needs Analysis

- **Trace sanitization is a systemic problem**: #25592, #44905, and the release-patch #89913/#90132 all address the same pattern—internal LLM artifacts (tool calls, reasoning, processing text) leaking to users. This suggests **inadequate output filtering architecture** rather than isolated bugs.
- **Codex reliability remains fragile**: #88312 is a regression of #84076, indicating fixes for turn-completion don't generalize across model versions or tool-complexity levels.
- **Vision-language preprocessing is brittle**: #73424 and #91790 both involve image capability detection/preprocessing failures, suggesting the VLM pipeline has **fragile capability negotiation** with providers.

---

## 5. Bugs & Stability

| Severity | Issue | Description | Fix PR? | Research Relevance |
|----------|-------|-------------|---------|------------------|
| **P1** | [#88312](https://github.com/openclaw/openclaw/issues/88312) | Codex turn-completion stall regression | No explicit fix PR | **Reasoning orchestration**: Multi-tool turn failures |
| **P1** | [#25592](https://github.com/openclaw/openclaw/issues/25592) | Inter-tool text leaks to channels | No | **Output sanitization / hallucination control** |
| **P1** | [#48003](https://github.com/openclaw/openclaw/issues/48003) | Steer mode fails to inject messages mid-turn | No | **Session state / interactive reasoning** |
| **P1** | [#86996](https://github.com/openclaw/openclaw/issues/86996) | Active Memory + Codex = latency, timeouts, stalls | No | **Long-context performance degradation** |
| **P1** | [#89315](https://github.com/openclaw/openclaw/issues/89315) | Gateway heap unbounded growth → OOM | No | **System reliability under long contexts** |
| **P1** | [#84569](https://github.com/openclaw/openclaw/issues/84569) | WhatsApp stalls on long model_call, incomplete turns | No | **Timeout/reasoning interaction** |
| P2 | [#87299](https://github.com/openclaw/openclaw/issues/87299) | Spurious failures in large Telegram sessions | No | **Context compaction side effects** |
| P2 | [#90354](https://github.com/openclaw/openclaw/issues/90354) | Unbounded append in pre-compaction memory flush | No | **Memory write safety / long-context** |

**Key pattern**: No fix PRs are linked for the highest-severity issues, indicating **maintainer bandwidth constraints** or architectural complexity blocking resolution.

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Signal | Likelihood in Next Version |
|----------|--------|---------------------------|
| [#54373](https://github.com/openclaw/openclaw/issues/54373) | **Context Provenance metadata** — source/volatility tags for injected context | **Moderate**: RFC-style, no implementation; aligns with long-context research trends but needs architectural buy-in |
| [#56110](https://github.com/openclaw/openclaw/issues/56110) | **STATE.md auto-loading** — recover working state after compaction | **Moderate-High**: Directly addresses #86996/#87299 pain points; referenced Anthropic research suggests industry alignment |
| [#42840](https://github.com/openclaw/openclaw/issues/42840) | MathJax/LaTeX in Control UI | Low: UI polish, not core |
| [#53638](https://github.com/openclaw/openclaw/issues/53638) | Per-channel model overrides | Low: Config complexity concern |
| [#90354](https://github.com/openclaw/openclaw/issues/90354) | Bounded append semantics for memory flush | **High**: Safety guardrail, P2 but actively discussed |

**No explicit vision-language or multimodal feature requests** in top issues—the project's multimodal work appears **reactive** (fixing image preprocessing bugs) rather than **proactive** (expanding capabilities).

---

## 7. User Feedback Summary

### Pain Points (Research-Relevant)

| Theme | Evidence | Severity |
|-------|----------|----------|
| **Reasoning/trace leakage** | #25592, #44905, #89913/#90132 release patches | **Critical** — recurring, multi-channel, patched twice in one release |
| **Context loss under pressure** | #87299 ("aggressive/unsafe compaction"), #86996 (Active Memory + Codex latency), #84569 (incomplete turns) | **High** — long-context systems fail when most needed |
| **False timeout classifications** | #74586 (memory_search aborted despite completion), #53540 (large param generation > timeout) | **High** — reward/measurement hacking in timeout logic |
| **VLM capability detection failures** | #73424 (image optimization fails), #91790 (Gemini CLI image shim) | **Moderate** — preprocessing pipeline brittleness |

### Satisfaction Indicators
- **Positive**: Rapid patch for reasoning leakage (#89913/#90132) shows responsive maintainer team
- **Negative**: Regression cycles (#88312 regresses #84076); same bug classes recur across releases

---

## 8. Backlog Watch

### Long-Unanswered Critical Issues

| Issue | Age | Last Update | Blocker | Research Relevance |
|-------|-----|-------------|---------|------------------|
| [#25592](https://github.com/openclaw/openclaw/issues/25592) | ~3.5 months | 2026-06-09 | Needs maintainer review, product decision, security review, source repro | **Hallucination/artifact control** — foundational output sanitization |
| [#48003](https://github.com/openclaw/openclaw/issues/48003) | ~3 months | 2026-06-09 | Fix PR open, needs review | **Interactive reasoning** — steer mode for real-time intervention |
| [#44905](https://github.com/openclaw/openclaw/issues/44905) | ~3 months | 2026-06-09 | Same multi-review blockers as #25592 | **Trace leakage** — Discord-specific variant |
| [#31331](https://github.com/openclaw/openclaw/issues/31331) | ~4 months | 2026-06-09 | Security review, source repro | Sandbox security boundary |

### PRs Needing Maintainer Attention

| PR | Age | Status | Research Value |
|----|-----|--------|--------------|
| [#84792](https://github.com/openclaw/openclaw/pull/84792) | ~3 weeks | Ready for maintainer look | Memory flush ordering — long-context preservation |
| [#91594](https://github.com/openclaw/openclaw/pull/91594) | ~1 day | Ready for maintainer look | Codex memory recall — reasoning augmentation |
| [#91790](https://github.com/openclaw/openclaw/pull/91790) | ~1 day | Needs proof | Gemini VLM capability detection |

---

## Research Assessment Summary

**OpenClaw's current development is operationally intensive but research-light.** The project exhibits mature engineering around LLM deployment (auth, routing, session management) but shows **no visible investment in**:

- Novel vision-language architectures or training methodologies
- Explicit hallucination detection/mitigation beyond output filtering
- Reasoning mechanism research (chain-of-thought optimization, tool-use learning)
- Long-context algorithmic improvements (compression, retrieval, attention)

The repeated **reasoning leakage** and **context compaction** issues suggest underlying research needs in:
1. **Controllable generation** — robust separation of internal reasoning from external output
2. **Adaptive context management** — compaction that preserves task-relevant state
3. **Reliable timeout/reward estimation** — preventing false aborts of valid reasoning chains

---

## Cross-Ecosystem Comparison

# Cross-Project Analysis: Open-Source AI Agent Ecosystem
## 2026-06-10 Research Synthesis

---

## 1. Ecosystem Overview

The open-source personal AI assistant landscape is experiencing a **bifurcation between operational infrastructure and frontier capability research**. Most projects (OpenClaw, ZeroClaw, IronClaw, NanoClaw) function as **deployment orchestration layers**—messaging gateways, session managers, and tool routers—rather than model development platforms. Only CoPaw and NanoBot show active research-relevant work in reasoning handling and context compression, while vision-language capabilities remain **reactive and underdeveloped across the board**. The ecosystem is collectively grappling with a **context window crisis**: expanding tool definitions and memory systems are colliding with fixed token budgets, forcing ad-hoc compression and truncation strategies that undermine reliability.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Releases | Health Score | Assessment |
|:---|:---|:---|:---|:---|:---|
| **OpenClaw** | 453 | 497 | v2026.6.5 stable + beta | ⚠️ High velocity, high debt | Rapid patch cycles; P1 bugs unassigned; operational focus |
| **NanoBot** | 6 | 23 | None | ✅ Moderate, research-relevant | Concentrated memory/alignment work; lower volume, higher signal |
| **Hermes Agent** | 50 | 50 | None | ⚠️ Active, fragmented | Infrastructure-heavy; delegation features advancing |
| **PicoClaw** | 20 | 20 | Nightly only | 🔴 Security-critical | 15 CVE-grade disclosures; rapid triage but systemic exposure |
| **NanoClaw** | 1 | 43 | None | ✅ Consolidating | High merge throughput; low research signal; security-hardening |
| **NullClaw** | 5 | 7 | None | ✅ Stable maintenance | Tight resolution cycles; tool-filtering and PII work |
| **IronClaw** | 47 | 50 | None | ⚠️ Pre-release crunch | Reborn production push; tool-reliability fixes; multimodal prep |
| **LobsterAI** | 2 | 5 | None | ✅ Product-stable | Desktop client focus; multi-agent orchestration; low research signal |
| **CoPaw** | 33 | 34 | v1.1.11-beta.2 | ⚠️ Migrating | AgentScope 2.0 transition; reasoning bugs; modular VLM proposal |
| **ZeroClaw** | 50 | 50 | None | 🔴 Backlog accumulation | Low close rate vs. open volume; context architecture crisis |
| **TinyClaw** | 0 | 0 | None | ⚪ Dormant | No activity |
| **Moltis** | 0 | 0 | None | ⚪ Dormant | No activity |
| **ZeptoClaw** | 0 | 0 | None | ⚪ Dormant | No activity |

*Health Score methodology: Balances velocity against resolution rate, security posture, research relevance, and architectural coherence.*

---

## 3. OpenClaw's Position

### Advantages vs. Peers
| Dimension | OpenClaw | Peer Comparison |
|:---|:---|:---|
| **Scale** | 453 issues / 497 PRs in 24h | 10-20× higher than NanoBot, LobsterAI, NullClaw; comparable to ZeroClaw/IronClaw in volume |
| **Release discipline** | Same-day stable promotion from beta | Faster than CoPaw's extended beta cycles; more structured than PicoClaw's nightly-only |
| **Response latency** | Reasoning leakage patched in <24h (#89913/#90132) | Matches PicoClaw's security triage; exceeds ZeroClaw's 55-day context bug |
| **Integration breadth** | QQ, Telegram, Discord, WhatsApp, Matrix | Widest channel coverage; ZeroClaw and Hermes Agent comparable |

### Technical Approach Differences
- **OpenClaw**: **Output-sanitization-first** architecture—reasoning scaffolding leakage addressed via post-hoc stripping (`<thinking>` tags) rather than structural separation of reasoning and generation paths
- **CoPaw/NanoBot**: **Provider-normalization** approach—reasoning content handled per-provider with display logic; more fragile but preserves reasoning for debugging
- **IronClaw**: **Contractual validation** layer (`NormalizingProvider`)—forces tool-use finish reasons, schema normalization; serving-layer alignment

### Community Size Comparison
OpenClaw operates at **infrastructure-project scale** (comparable to ZeroClaw's 50/50 daily volume) but with **higher issue-to-PR ratio** (0.91 vs. ZeroClaw's 1.0), suggesting either more bug reports per fix or less efficient triage. NanoBot's 6:23 issue-to-PR ratio indicates healthier contributor-driven development.

---

## 4. Shared Technical Focus Areas

| Requirement | Projects | Specific Needs |
|:---|:---|:---|
| **Reasoning trace sanitization** | OpenClaw, CoPaw, NanoBot, IronClaw | Prevent internal CoT/tool-call artifacts from reaching users; preserve for debugging |
| **Context compression correctness** | OpenClaw, NanoBot, ZeroClaw, CoPaw, PicoClaw | Configurable thresholds; preserve corrections over model errors; session isolation |
| **Tool-use reliability** | OpenClaw, NanoBot, Hermes Agent, IronClaw, ZeroClaw | Handle text-format tool calls; validation strictness; finish-reason normalization; JSON robustness |
| **Provider API drift** | CoPaw, IronClaw, NanoBot, ZeroClaw | `max_tokens` → `max_completion_tokens`; temperature deprecation; reasoning field standards (`reasoning` vs. `reasoning_content`) |
| **Vision-language preprocessing** | OpenClaw, CoPaw, IronClaw | Capability detection brittleness; image optimization failures; routing false-positives |
| **Memory/retrieval alignment** | NanoBot, ZeroClaw, Hermes Agent | Cross-session pollution prevention; relevance weighting; correction retention |

**Emerging cross-project pattern**: No project has a **unified reasoning architecture**. Each patches provider-specific behaviors, creating fragmentation that complicates multi-provider deployments.

---

## 5. Differentiation Analysis

| Project | Core Differentiation | Target User | Architecture Signature |
|:---|:---|:---|:---|
| **OpenClaw** | Maximum channel integration; rapid operational response | Multi-platform deployers | Message-router-centric; heavy sanitization layer |
| **NanoBot** | Memory system research; episodic memory integrity | Researchers, long-context users | Memory-first architecture; conversation branching |
| **Hermes Agent** | Model delegation/routing; multi-agent skill marketplace | Power users, automation-heavy | Delegate tool with per-task overrides; Honcho memory |
| **PicoClaw** | Security-hardened; multi-agent collaboration bus | Security-conscious operators | Agent Collaboration Bus; TEE provider support (NEAR AI) |
| **NanoClaw** | Deterministic safety policies; trace observability | Compliance-sensitive deployments | Code-based policy enforcement; skill marketplace |
| **NullClaw** | Lightweight; cross-instance memory sync | Minimalist self-hosters | Event-stream synchronization; tool-filter groups |
| **IronClaw** | Production-grade provider normalization; Reborn kernel | Enterprise, TEE deployments | Layered provider decorators; strict-mode validation |
| **LobsterAI** | Desktop-native; Cowork session orchestration | End-user desktop agents | Electron renderer; deferred session initialization |
| **CoPaw** | Modular VLM proposal; self-evolving skills | Chinese-market researchers | AgentScope backend; OpenSandbox isolation |
| **ZeroClaw** | Extreme multi-channel routing; cron automation | Automation-heavy multi-platform users | Three divergent turn engines (unification RFC pending) |

**Critical gap**: No project offers **end-to-end multimodal reasoning**—vision-language capabilities are consistently blocked on text-only legacy or reactive bug-fixing.

---

## 6. Community Momentum & Maturity

| Tier | Projects | Characteristics |
|:---|:---|:---|
| **Rapidly iterating, high debt** | OpenClaw, ZeroClaw, IronClaw | 50+ daily items; accumulation of unassigned P1s; architectural tension between velocity and coherence |
| **Active consolidation** | CoPaw, Hermes Agent, PicoClaw | Significant architectural transitions (AgentScope 2.0, Reborn, security batch); feature freeze risk |
| **Steady maintenance** | NanoBot, NullClaw, NanoClaw | Lower volume; higher resolution rate; focused scope |
| **Product-stable, low research** | LobsterAI | Desktop polish; minimal breaking changes; narrow use case |
| **Dormant** | TinyClaw, Moltis, ZeptoClaw | No 24h activity; likely abandoned or private development |

**Maturity paradox**: OpenClaw has the **highest operational maturity** (releases, patch velocity) but **lowest research maturity** (no visible investment in reasoning, multimodal, or alignment beyond output filtering). NanoBot inverts this—lower operational scale, higher research signal.

---

## 7. Trend Signals

| Trend | Evidence | Value for Agent Developers |
|:---|:---|:---|
| **Context window as scarce resource** | ZeroClaw #5808 (32k budget overflowed by system prompt); OpenClaw #86996 (Active Memory + Codex latency); NanoBot #4264 (compaction truncates corrections) | **Design for progressive disclosure**: Hierarchical tool summarization, dynamic inclusion, semantic clustering |
| **Reasoning token standardization gap** | ZeroClaw #6584 (`reasoning` vs. `reasoning_content`); CoPaw multiple provider-specific reasoning display bugs; OpenClaw `<thinking>` stripping | **Abstract reasoning layer**: Dual-read logic; provider-agnostic reasoning extraction; structured reasoning storage |
| **Safety-reasoning tradeoff** | Hermes Agent #43083 (credential redaction breaks tool coherence); NanoBot #4259 (cross-session pollution); OpenClaw #25592 (inter-tool text leaks) | **Structured tool representations**: Separate display history from reasoning history; model-aware redaction |
| **Heterogeneous model routing** | Hermes Agent #16525/#43134 (per-task model override); LobsterAI #2132 (M3 planning + DeepSeek execution); ZeroClaw #7415 (unify turn engines) | **Explicit handoff protocols**: Cross-model state synchronization; completion guarantees; failure propagation |
| **Multimodal infrastructure lag** | IronClaw #4644 (text-only transcript); CoPaw #4992 (visual model fallback proposal); OpenClaw reactive image preprocessing fixes | **Decouple V and L**: Independent vision model configuration; extensible format registries; media URL validation |
| **Observability as alignment prerequisite** | NanoClaw #1202 (agent trace logging); CoPaw #5009 (Langfuse/OpenTelemetry request); NanoBot #4193 (memory lifecycle test harness) | **Invest in tracing early**: Token-level reasoning observation; tool-call attribution; hallucination measurement |

**Strategic implication**: The ecosystem is **converging on common failure modes** (context, reasoning, tool-use, multimodal) but **diverging on solutions**. This creates both interoperability risk and opportunity for standardization efforts.

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot Project Digest — 2026-06-10
## Research-Focused Filter: Multimodal Reasoning, Long-Context Understanding, Post-Training Alignment, AI Reliability

---

## 1. Today's Overview

NanoBot shows **moderate research-relevant activity** with 23 PR updates and 6 active issues in the past 24 hours, though no new releases. The project demonstrates continued investment in **context management reliability** (memory cursor monotonicity, cross-session contamination prevention), **tool-use robustness** (structured vs. text-format tool call parsing, validation strictness), and **multimodal infrastructure** (ASR provider expansion, LaTeX rendering). Notably, several issues directly address **hallucination-adjacent problems** in long-context scenarios—specifically how history compaction may preserve erroneous model outputs when user corrections fall outside the retention window. The research community should track memory system evolution closely, as this is where alignment and reliability concerns converge.

---

## 2. Releases

**None** — No new releases in the past 24 hours.

---

## 3. Project Progress

### Merged/Closed PRs with Research Relevance

| PR | Title | Research Significance |
|:---|:---|:---|
| [#4190](https://github.com/HKUDS/nanobot/pull/4190) | Improve tool call validation strictness | **Post-training alignment / reliability**: Prevents silent coercion of malformed tool arguments into executable `{}`, reducing unintended execution paths. Preserves provider-emitted arguments for explicit validation failure rather than silent repair. |
| [#4252](https://github.com/HKUDS/nanobot/pull/4252) | fix(webui): render TeX math delimiters | **Vision-language capabilities**: Adds native TeX math rendering (`\(...\)`, `\[...\]`, guarded `$...$`) via micromark/remark extension, improving scientific/technical document multimodal presentation. |
| [#4208](https://github.com/HKUDS/nanobot/pull/4208) | feat(webui): add assistant reply fork-from-here | **Long-context understanding**: Enables conversation branching from arbitrary points, supporting iterative reasoning exploration and hypothesis testing without context loss. |
| [#3434](https://github.com/HKUDS/nanobot/pull/3434) | feat(lateX): add lateX to feishu channel using codecogs | **Vision-language capabilities**: LaTeX formula rendering for Feishu channel via CodeCogs API image generation—multimodal output adaptation for messaging platforms. |
| [#3400](https://github.com/HKUDS/nanobot/pull/3400) | feat(dream): allow users to decide whether dream can edit USER.md and SOUL.md | **Post-training alignment / AI reliability**: Governance control over automated identity file modification, preventing uncontrolled self-modification of agent persona—relevant to recursive self-improvement safety. |
| [#4177](https://github.com/HKUDS/nanobot/pull/4177) | docs: make onboarding friendlier for beginners | *Filtered: documentation, not research-relevant* |
| [#4265](https://github.com/HKUDS/nanobot/pull/4265) | feat(english-read): change cron schedule from daily to every 2 days | *Filtered: operational, not research-relevant* |
| [#4034](https://github.com/HKUDS/nanobot/pull/4034) | Add GitAgent Protocol support | *Filtered: protocol standardization, minimal research relevance* |

---

## 4. Community Hot Topics

### Most Active Issues/PRs by Engagement

| Rank | Item | Comments | Research Analysis |
|:---|:---|:---|:---|
| 1 | [#4253](https://github.com/HKUDS/nanobot/issues/4253) — support overriding model per conversation | 3 comments | **Reasoning mechanisms / cost-reliability tradeoffs**: User needs dynamic model selection based on privacy/sensitivity—implies research interest in **adaptive compute allocation** and **capability-appropriate reasoning delegation**. Underlying need: heterogeneous model orchestration for task-aligned reasoning depth. |
| 2 | [#4259](https://github.com/HKUDS/nanobot/issues/4259) — `history.jsonl` cross-session injection causes context pollution | 2 comments | **Long-context understanding / hallucination**: Critical bug where `ContextBuilder.build_system_prompt()` lacks session isolation, merging unprocessed cross-session entries. Directly impacts **contextual grounding** and can introduce **hallucinated attributions** (model believes prior session facts are current-user stated). |
| 3 | [#4061](https://github.com/HKUDS/nanobot/issues/4061) — OpenAI-compatible text-format tool calls not parsed | 1 comment | **Reasoning mechanisms / tool-use reliability**: Gap between provider text markup and structured execution. Models emitting "reasoning" in text tool calls fail to dispatch—relevant to **emergent tool-use patterns** in post-trained models. |

### Emerging Research Threads

- **Memory system integrity** (Issues #4259, #4264, PR #4256, #4193): Concentrated effort on cursor monotonicity, compaction correctness, and lifecycle testing suggests the project is stabilizing its **episodic memory architecture**—foundational for long-horizon reasoning reliability.

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **Critical** | [#4259](https://github.com/HKUDS/nanobot/issues/4259) | Cross-session context pollution: `history.jsonl` entries from other sessions leak into current system prompt via unisolated `# Recent History` injection. **Directly causes hallucination/confabulation of user statements.** | **No fix PR yet** — active discussion |
| **High** | [#4264](https://github.com/HKUDS/nanobot/issues/4264) | `idleCompact` truncates last 8 messages, potentially **preserving erroneous model outputs and discarding user corrections** in history archives. Creates **aligned-hallucination persistence**: model "learns" wrong answers from its own compacted history. | **No fix PR yet** — reported today |
| **High** | [#4261](https://github.com/HKUDS/nanobot/issues/4261) / [#4263](https://github.com/HKUDS/nanobot/pull/4263) | GPT-5.x rejects `max_tokens`, requires `max_completion_tokens`. Breaks reasoning model compatibility. | **Fix PR open** (#4263) — model-name-based fallback |
| **Medium** | [#4061](https://github.com/HKUDS/nanobot/issues/4061) | Text-format tool calls from OpenAI-compatible providers fail to parse, rendering raw markup and failing tool dispatch. | **No fix PR yet** |
| **Medium** | [#4267](https://github.com/HKUDS/nanobot/pull/4267) | WebUI intermittently drops assistant replies from rendering (race condition in token streaming). | **Fix PR open** |

### Research-Critical Stability Note

Issues **#4259** and **#4264** form a **compound reliability risk**: cross-session pollution introduces false premises, while compaction truncation preserves model errors over user corrections. Together, these undermine **truthful long-context reasoning** and **correction-based alignment**—core concerns for reliable AI systems.

---

## 6. Feature Requests & Roadmap Signals

| Request | Source | Research Relevance | Likelihood Near-Term |
|:---|:---|:---|:---|
| Per-conversation model override | [#4253](https://github.com/HKUDS/nanobot/issues/4253) | Adaptive reasoning delegation, compute optimization | High — architectural, no blockers |
| Session-isolated history injection | [#4259](https://github.com/HKUDS/nanobot/issues/4259) | Contextual grounding, hallucination prevention | **Critical priority** — likely immediate |
| Compaction window awareness of corrections | [#4264](https://github.com/HKUDS/nanobot/issues/4264) | Error recovery, user feedback incorporation | High — memory system focus |
| StepFun ASR SSE provider | [#4260](https://github.com/HKUDS/nanobot/pull/4260) | **Multimodal input**: streaming audio transcription | Medium — provider expansion pattern |
| Fenced-code-block-aware message splitting | [#4257](https://github.com/HKUDS/nanobot/pull/4257) | Structured output integrity in long messages | Medium — quality-of-life |

---

## 7. User Feedback Summary

### Pain Points (Research-Relevant)

| Theme | Evidence | Implication |
|:---|:---|:---|
| **Context integrity failures** | #4259 (pollution), #4264 (truncation), #4267 (render drops) | Users cannot trust long-context persistence; model behavior becomes non-reproducible |
| **Tool-use fragility** | #4061 (text→structured gap), #4190 (validation strictness needed) | Post-trained models with emergent text-based tool reasoning break execution pipelines |
| **Reasoning model compatibility** | #4261/#4263 (GPT-5.x parameter naming) | Rapid provider API evolution strains abstraction layers |
| **Correction futility** | #4264 explicit: "user corrections may not be in summary context" | **Alignment concern**: systems that don't learn from feedback amplify errors |

### Use Case Signals

- **Privacy-sensitive adaptive deployment** (#4253): Users actively partition tasks across local/capable models—validating research on **capability-aware routing**.
- **Scientific/technical communication** (#4252, #3434): LaTeX math rendering demand indicates research/science user segment.

---

## 8. Backlog Watch

### Issues/PRs Requiring Maintainer Attention

| Item | Age | Issue | Research Urgency |
|:---|:---|:---|:---|
| [#4259](https://github.com/HKUDS/nanobot/issues/4259) | 1 day | Cross-session context pollution — **no assigned fix** | **Critical**: Foundational hallucination vector |
| [#4264](https://github.com/HKUDS/nanobot/issues/4264) | 1 day | Compaction truncates corrections — **no assigned fix** | **Critical**: Undermines feedback-based alignment |
| [#4061](https://github.com/HKUDS/nanobot/issues/4061) | 11 days | Text-format tool calls — **no fix PR** | High: Emerging model behavior compatibility |
| [#4193](https://github.com/HKUDS/nanobot/pull/4193) | 6 days | Memory lifecycle test harness — **open, needs review** | Medium: Infrastructure for reliability validation |
| [#3983](https://github.com/HKUDS/nanobot/pull/3983) | 17 days | Runner blocked tool-call finish reasons — **open** | Medium: Safety coverage for refusal/content_filter paths |

### Recommended Research Tracking

Monitor **#4259** and **#4264** for resolution patterns—these represent **active failure modes in long-context alignment** that are likely generalizable beyond NanoBot to other agent architectures using compressed episodic memory.

---

*Digest generated from HKUDS/nanobot GitHub activity 2026-06-09 to 2026-06-10. Filtered for research relevance: multimodal reasoning, long-context understanding, post-training alignment, AI reliability.*

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent Project Digest — 2026-06-10

## 1. Today's Overview

Hermes Agent saw **high activity** over the past 24 hours with **50 issues and 50 PRs updated**, though **no new releases** were cut. The signal-to-noise ratio for research-relevant updates is moderate: most activity centers on gateway/CLI infrastructure, multi-platform integrations (Telegram, Discord, QQ, Telegram), and dashboard UX rather than core model capabilities. Notable research-adjacent threads include **context compaction/persistence fixes**, **model routing and delegation mechanisms**, **credential redaction side effects on tool execution**, and **false-positive content filtering in prompt building**. The project appears healthy in terms of velocity but continues to accumulate UX and integration debt ahead of any focused alignment or reasoning push.

---

## 2. Releases

**No new releases** today.

---

## 3. Project Progress

### Merged/Closed PRs Today

| PR | Title | Research Relevance |
|---|---|---|
| [#42871](https://github.com/NousResearch/hermes-agent/pull/42871) | fix(desktop): edit the default profile's SOUL.md from a single-profile setup | Low — profile UX |
| [#43109](https://github.com/NousResearch/hermes-agent/pull/43109) | fix(desktop): stage dropped files into the remote session workspace | Low — file handling |
| [#43171](https://github.com/NousResearch/hermes-agent/pull/43171) | fix: mirror script cron deliveries and sanitize ACP overrides | Low — cron delivery |

No merged PRs directly address vision-language, reasoning, training, or hallucination. The most relevant **open** progress items are:

- **[#43067](https://github.com/NousResearch/hermes-agent/pull/43067)** — `fix: preserve messages after compaction split, keep busy follow-ups as separate turns`: Fixes **context compaction** losing assistant messages and incorrectly merging user follow-ups. Directly relevant to **long-context understanding** and conversation state coherence.
- **[#43184](https://github.com/NousResearch/hermes-agent/pull/43184)** — `fix(tools): filter compaction summaries from session_search bookends and cap content length`: Prevents **prompt bloat** from compaction handoff summaries in search retrieval. Relevant to **retrieval quality and context efficiency**.
- **[#43134](https://github.com/NousResearch/hermes-agent/pull/43134)** / **[#43185](https://github.com/NousResearch/hermes-agent/pull/43185)** — `feat(delegate_tool): per-task model/provider override`: Advances **model routing for reasoning delegation**, allowing subtasks to use different models/providers.

---

## 4. Community Hot Topics

### Most Active Threads

| # | Item | Comments | Research Angle |
|---|---|---|---|
| [#21587](https://github.com/NousResearch/hermes-agent/issues/21587) | Telegram Guest Bots, Bot-to-Bot, Stickers and Chat Automation | 9 | Multi-agent orchestration surface; no direct VLM/reasoning signal |
| [#10567](https://github.com/NousResearch/hermes-agent/issues/10567) | `--host` and CORS config for dashboard remote access | 8 | Infrastructure |
| **[#43083](https://github.com/NousResearch/hermes-agent/issues/43083)** | **Passwords redacted as `***` but model reads back conversation history and fails on second tool call** | **6** | **Tool-use reliability / hallucination-adjacent: model confused by redacted history** |
| [#16525](https://github.com/NousResearch/hermes-agent/issues/16525) | Expose `model_switch` as agent-callable tool | 6 | **Autonomous reasoning / self-routing** |
| [#42006](https://github.com/NousResearch/hermes-agent/issues/42006) | macOS `launchd_restart` missing `bootout` | 5 | Infrastructure |

### Underlying Needs

- **#43083** reveals a tension in **defense-in-depth vs. model coherence**: redacting credentials from persisted tool-call arguments breaks the model's ability to reason about its own prior actions, causing repeated or failed tool calls. This is a **post-training alignment / tool-use hallucination** issue worth tracking.
- **#16525** signals demand for **meta-reasoning**: the agent should introspect on task complexity and pick its own model, rather than rely on hardcoded rules or user slash commands.

---

## 5. Bugs & Stability

| Severity | Issue | Summary | Fix PR? |
|---|---|---|---|
| **P1** | **[#43083](https://github.com/NousResearch/hermes-agent/issues/43083)** | Credential redaction in `chat_completion_helpers.py` strips arguments from history; model re-reads its own redacted turns and fails second tool call | None listed |
| P1 | [#43014](https://github.com/NousResearch/hermes-agent/issues/43014) | `deliver=origin` fails to resolve delivery target in CLI sessions | None |
| P1 | [#43067](https://github.com/NousResearch/hermes-agent/pull/43067) (PR) | Assistant messages lost after context compaction; follow-ups merged | **PR open** |
| P2 | [#43026](https://github.com/NousResearch/hermes-agent/issues/43026) | Gemini OpenAI-compatible provider returns HTTP 400/404 via internal HTTP client | None |
| P2 | [#37968](https://github.com/NousResearch/hermes-agent/issues/37968) | Cron gateway approvals vulnerable to environment pollution (CVSS 6.3–7.0) | None |
| P2 | [#43146](https://github.com/NousResearch/hermes-agent/issues/43146) | Context scanner false-positive: German "Praxis" flagged as C2 framework | None |
| P2 | [#42006](https://github.com/NousResearch/hermes-agent/issues/42006) | macOS gateway restart fails under launchd | None |
| P3 | [#34070](https://github.com/NousResearch/hermes-agent/issues/34070) | Honcho memory prefetch hang on fresh CLI subprocess | None |
| P3 | [#43042](https://github.com/NousResearch/hermes-agent/issues/43042) | Desktop file browser ENOENT due to `session.info` CWD overwrite | None |

### Research-Relevant Stability Notes

- **#43083** is the highest-priority research-relevant bug: it illustrates how **safety interventions can degrade reasoning** when the model's context no longer matches its actual prior behavior. A better fix may require structured tool-call representations or model-aware redaction.
- **#43146** is a **hallucination/false-positive** case in the prompt builder's threat-pattern scanner, where a bare token regex overgeneralizes across languages. This affects **reliability of content moderation** and international use.
- **#43067** addresses **long-context state corruption**, a core concern for sustained reasoning sessions.

---

## 6. Feature Requests & Roadmap Signals

| Issue | Request | Likelihood in Next Version |
|---|---|---|
| **[#16525](https://github.com/NousResearch/hermes-agent/issues/16525)** | `model_switch` as agent-callable tool for autonomous complexity-based routing | **High** — active, well-scoped, aligns with delegation trends |
| **[#38954](https://github.com/NousResearch/hermes-agent/issues/38954)** | Automatic role-based model routing | Medium — overlaps with #16525, may be consolidated |
| **[#43134](https://github.com/NousResearch/hermes-agent/pull/43134)** / **[#43185](https://github.com/NousResearch/hermes-agent/pull/43185)** | Per-task model/provider override in `delegate_tool` | **High** — PR already open and in review-fix loop |
| [#31322](https://github.com/NousResearch/hermes-agent/issues/31322) | `service_tier` support for Amazon Bedrock | Medium — provider parity request |
| [#13314](https://github.com/NousResearch/hermes-agent/pull/13314) | You.com as web backend and research skill | Medium — research skill expansion |
| [#37106](https://github.com/NousResearch/hermes-agent/pull/37106) | Curated default skills bootstrap | Medium — onboarding/scope control |

**No explicit vision-language feature requests** appeared in the top 30 issues. The closest VLM-adjacent item is **#40457** (QQ Bot media delivery), which is infrastructure rather than model capability.

---

## 7. User Feedback Summary

### Real Pain Points

1. **Tool-use coherence breaks under safety redaction** (#43083)  
   Users expect credential masking, but the current implementation causes the model to "forget" or misread its own tool history.

2. **Model routing is too manual** (#16525, #38954)  
   Power users want the agent to self-select models by task complexity or role, reducing human-in-the-loop overhead.

3. **Context compaction loses state** (#43067)  
   Long sessions suffer from assistant message loss and merged turns, undermining trust in sustained reasoning.

4. **False positives in content scanning** (#43146)  
   International users hit overbroad regex filters, blocking legitimate files.

5. **Local/slow-provider UX friction** (#43028)  
   Spinner timeouts with Ollama/local models degrade the CLI experience.

### Satisfaction/Dissatisfaction

- **Positive**: Active development on delegation, memory plugins, and multi-platform gateways.
- **Negative**: Recurring class of bugs around **context persistence**, **configuration discoverability**, and **safety/reasoning tradeoffs**.

---

## 8. Backlog Watch

| Issue/PR | Age | Why It Needs Attention |
|---|---|---|
| **[#16525](https://github.com/NousResearch/hermes-agent/issues/16525)** | ~6 weeks | Core autonomous reasoning primitive; high comment count, no maintainer resolution |
| **[#38954](https://github.com/NousResearch/hermes-agent/issues/38954)** | ~1 week | Duplicates/overlaps with #16525; needs triage to avoid parallel design tracks |
| **[#13314](https://github.com/NousResearch/hermes-agent/pull/13314)** | ~7 weeks | Research skill expansion (You.com); stale but strategically relevant |
| **[#14390](https://github.com/NousResearch/hermes-agent/pull/14390)** | ~7 weeks | P1 test-suite stabilization; large scope may be blocked on review bandwidth |
| **[#37106](https://github.com/NousResearch/hermes-agent/pull/37106)** | ~1 week | Default skill curation; affects agent behavior scope and hallucination surface from overloaded toolsets |

---

## Research Summary

For a project positioned around agentic reasoning, today's digest shows **more infrastructure motion than model-capability advancement**. The most valuable research signals are:

- **Tool-history redaction breaking coherence** (#43083) — a concrete case for **aligned tool-use representation learning**.
- **Autonomous model routing demand** (#16525, #38954, #43134/#43185) — touches **meta-reasoning and compute-optimal inference**.
- **Context compaction integrity** (#43067, #43184) — directly relevant to **long-context reliability**.
- **Prompt-builder false positives** (#43146) — a **hallucination/safety calibration** issue in heuristic filters.

**Vision-language capabilities remain unrepresented** in the top activity; no issues or PRs address image/video understanding, multimodal tool use, or vision-enabled reasoning workflows.

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-06-10

## Today's Overview

PicoClaw experienced an **exceptionally high-velocity security incident response day** with 15 new CVE-grade vulnerabilities disclosed and partially patched, alongside routine maintenance activity. The project shows **strong operational health** with rapid triage of security issues, though the volume of SSRF and access-control bypasses suggests systemic attack surface in the tool-calling and channel-gateway layers. Non-security development progressed on context compression correctness, streaming protocol semantics, and provider compatibility. The 20 active issues and 20 PRs (5 merged/closed) indicate sustained community engagement, with security researcher YLChen-007 responsible for the majority of today's high-impact disclosures.

---

## Releases

| Version | Type | Notes |
|---------|------|-------|
| [v0.2.9-nightly.20260609.46b29a0a](https://github.com/sipeed/picoclaw/compare/v0.2.9...main) | Nightly | Automated build; **unstable**. No research-relevant feature changes identified in changelog. |

*No stable release. No breaking changes or migration notes relevant to research use cases.*

---

## Project Progress

### Merged/Closed PRs (Research-Relevant)

| PR | Author | Summary | Research Relevance |
|----|--------|---------|------------------|
| [#3064](https://github.com/sipeed/picoclaw/pull/3064) | chengzhichao-xydt | Defensive type assertion with `ok` check in config migration | **Reliability**: Prevents panics on malformed model config entries |
| [#2942](https://github.com/sipeed/picoclaw/pull/2942) | LegendAlessandro-Liguori | Canonical hyphenated model ID for Claude Sonnet | **Provider alignment**: Corrects model identifier mapping to Anthropic API |
| [#2940](https://github.com/sipeed/picoclaw/pull/2940) | LegendAlessandro-Liguori | Omit `temperature` for `claude-opus-4-7` | **Training/inference methodology**: Adapts to provider-level parameter deprecation; signals evolving provider API contracts |
| [#2937](https://github.com/sipeed/picoclaw/pull/2937) | afjcjsbx | **Agent Collaboration Bus** — inter-agent mailboxes, threads, structured envelopes | **Multi-agent reasoning**: Durable cross-agent context sharing with permission-aware routing; relevant to distributed reasoning and emergent collaboration research |

### Open PRs with Research Relevance

| PR | Author | Summary | Research Relevance |
|----|--------|---------|------------------|
| [#2990](https://github.com/sipeed/picoclaw/pull/2990) | yuxuan-7814 | Fix session history display: show all user messages, not just last | **Long-context integrity**: Corrects history truncation bug in `readJSONLSession()` |
| [#2988](https://github.com/sipeed/picoclaw/pull/2988) | yuxuan-7814 | Respect `summarize_token_percent` for context compression | **Context compression methodology**: Fixes hardcoded 76800-token threshold; configurable compression ratios |
| [#2987](https://github.com/sipeed/picoclaw/pull/2987) | yuxuan-7814 | Preserve `tool_calls` during streaming auxiliary message filtering | **Tool-use reasoning**: Prevents tool invocation messages from being dropped mid-stream |
| [#2983](https://github.com/sipeed/picoclaw/pull/2983) | afjcjsbx | Retry on semantically empty LLM responses (`content: null`, no tool calls) | **Hallucination/robustness**: Addresses silent failure mode when models return empty outputs; gap between HTTP 200 and valid semantic content |

---

## Community Hot Topics

### Most Active Discussion: Streaming Protocol Semantics
- **[#2404](https://github.com/sipeed/picoclaw/issues/2404)** — "Add in config to send streaming HTTP request" (11 comments, 👍1)
  - **Underlying need**: Deterministic streaming behavior for LLM backend integration; parity with OpenAI client's `stream=True`
  - **Research angle**: Streaming impacts token-level reasoning observation and intermediate state extraction

### Protocol Completion Signaling
- **[#2984](https://github.com/sipeed/picoclaw/issues/2984)** — "Add explicit turn completion signal for Pico WebSocket clients" (1 comment, 👍1)
  - **Underlying need**: Ambiguity in `typing.stop` vs. actual processing completion; affects multi-turn reasoning chains and evaluation frameworks that depend on turn boundaries

### Context Compression Configuration
- **[#2988](https://github.com/sipeed/picoclaw/pull/2988)** + **[#2796](https://github.com/sipeed/picoclaw/issues/2796)** (closed)
  - **Pattern**: Users expect transparent, configurable context management; hardcoded thresholds create trust issues in long-context reliability

---

## Bugs & Stability

| Severity | Item | Description | Fix Status |
|----------|------|-------------|------------|
| **Critical** | [#3072](https://github.com/sipeed/picoclaw/issues/3072) | CSRF in first-run password setup → local control-plane takeover | **No fix PR** |
| **Critical** | [#3081](https://github.com/sipeed/picoclaw/issues/3081) | Approval hook `cwd` symlink race: `exec` runs in unapproved directory | **No fix PR** |
| **Critical** | [#3075](https://github.com/sipeed/picoclaw/issues/3075) | Untrusted `./skills/` metadata auto-loaded into system prompt | **No fix PR** — **Directly relevant to prompt injection and hallucination attack surface** |
| **High** | [#3078](https://github.com/sipeed/picoclaw/issues/3078) | `web_fetch` SSRF bypass via HTTP proxy environment | **No fix PR** |
| **High** | [#3077](https://github.com/sipeed/picoclaw/issues/3077) | `web_fetch` SSRF bypass via `198.18.0.0/15` | **PR [#3085](https://github.com/sipeed/picoclaw/pull/3085)** open |
| **High** | [#3074](https://github.com/sipeed/picoclaw/issues/3074) | `web_fetch` SSRF bypass via ISATAP IPv6 literals | **No fix PR** |
| **High** | [#3070](https://github.com/sipeed/picoclaw/issues/3070) | OneBot media URL arbitrary fetch | **No fix PR** |
| **High** | [#3069](https://github.com/sipeed/picoclaw/issues/3069) | `allowed_cidrs` bypass via reverse proxy `RemoteAddr` trust | **PR [#3083](https://github.com/sipeed/picoclaw/pull/3083)** open |
| **Medium** | [#3080](https://github.com/sipeed/picoclaw/issues/3080) | `allowed_cidrs` bypass via loopback proxying | **PR [#3083](https://github.com/sipeed/picoclaw/pull/3083)** open |
| **Medium** | [#3079](https://github.com/sipeed/picoclaw/issues/3079) | `exec` whitelist skips deny-pattern for `jq` | **No fix PR** |
| **Medium** | [#3076](https://github.com/sipeed/picoclaw/issues/3076) | WeCom group trigger policy bypass | **No fix PR** |
| **Medium** | [#3073](https://github.com/sipeed/picoclaw/issues/3073) | LINE webhook replay → duplicate execution | **No fix PR** |
| **Medium** | [#3071](https://github.com/sipeed/picoclaw/issues/3071) | Unauthorized `/reload` via WebSocket | **No fix PR** |
| **Medium** | [#3068](https://github.com/sipeed/picoclaw/issues/3068) | MQTT `allow_from` bypass via `client_id` spoof | **No fix PR** |

### Research-Relevant Stability Issues

| Item | Description | Relevance |
|------|-------------|-----------|
| [#2983](https://github.com/sipeed/picoclaw/pull/2983) | Empty LLM response retry gap | **Hallucination/robustness**: Distinguishes transport success from semantic validity |
| [#2987](https://github.com/sipeed/picoclaw/pull/2987) | `tool_calls` dropped during streaming | **Tool-use reasoning integrity**: Streaming state machines may lose critical reasoning steps |
| [#2796](https://github.com/sipeed/picoclaw/issues/2796) | History compression shows only last user message | **Long-context reliability**: User-visible history ≠ model-visible context; trust gap |

---

## Feature Requests & Roadmap Signals

| Item | Signal | Likelihood in Next Version |
|------|--------|---------------------------|
| **Streaming HTTP config** ([#2404](https://github.com/sipeed/picoclaw/issues/2404)) | High community demand (11 comments); infrastructure for observability | **High** |
| **Explicit turn completion signal** ([#2984](https://github.com/sipeed/picoclaw/issues/2984)) | Protocol correctness for external clients; evaluation tooling need | **Medium-High** |
| **Agent Collaboration Bus** ([#2937](https://github.com/sipeed/picoclaw/pull/2937)) | Merged; multi-agent architecture now first-class | **Released in nightly** |
| **NEAR AI Cloud provider** ([#2917](https://github.com/sipeed/picoclaw/pull/2917)) | TEE-capable model support; decentralized AI infrastructure | **Medium** |
| **vodozemac replacement for libolm** ([#3088](https://github.com/sipeed/picoclaw/issues/3088)) | Security-driven; libolm deprecated | **Medium** |
| **DeltaChat gateway** ([#3063](https://github.com/sipeed/picoclaw/pull/3063)) | Channel diversity; federated messaging | **Low-Medium** |

### Predicted Research-Relevant Evolution
- **Context compression transparency**: Multiple PRs ([#2988](https://github.com/sipeed/picoclaw/pull/2988), [#2990](https://github.com/sipeed/picoclaw/pull/2990)) suggest maintainers are prioritizing user-visible context integrity; expect configurable compression strategies
- **Provider parameter adaptation**: Claude temperature deprecation ([#2939](https://github.com/sipeed/picoclaw/issues/2939), [#2940](https://github.com/sipeed/picoclaw/pull/2940)) indicates need for provider-specific request shaping, potentially model cards or capability negotiation

---

## User Feedback Summary

### Pain Points

| Theme | Evidence | Severity |
|-------|----------|----------|
| **Context opacity** | [#2796](https://github.com/sipeed/picoclaw/issues/2796), [#2988](https://github.com/sipeed/picoclaw/pull/2988) | High — users cannot trust what the model sees |
| **Streaming unpredictability** | [#2404](https://github.com/sipeed/picoclaw/issues/2404), [#2984](https://github.com/sipeed/picoclaw/issues/2984), [#2987](https://github.com/sipeed/picoclaw/pull/2987) | High — critical for real-time applications |
| **Provider compatibility fragility** | [#2939](https://github.com/sipeed/picoclaw/issues/2939), [#2942](https://github.com/sipeed/picoclaw/pull/2942) | Medium — breaking changes in upstream APIs cascade immediately |
| **Security trust boundary confusion** | [#3075](https://github.com/sipeed/picoclaw/issues/3075) — local files affect system prompt | Critical — unexpected prompt injection vector |

### Use Cases Emerging
- **Evaluation/observation frameworks**: Need deterministic turn boundaries ([#2984](https://github.com/sipeed/picoclaw/issues/2984))
- **Multi-agent research**: Collaboration bus ([#2937](https://github.com/sipeed/picoclaw/pull/2937)) enables distributed reasoning experiments
- **Long-context document analysis**: Compression configuration ([#2988](https://github.com/sipeed/picoclaw/pull/2988)) directly impacts viability

---

## Backlog Watch

| Item | Age | Issue | Risk |
|------|-----|-------|------|
| **Agent Collaboration Bus** | ~17 days | [#2937](https://github.com/sipeed/picoclaw/pull/2937) merged; needs documentation | Low — feature delivered |
| **Context compression fix** | ~8 days | [#2988](https://github.com/sipeed/picoclaw/pull/2988) | **Medium** — affects all long-context users; unmerged |
| **Session history fix** | ~8 days | [#2990](https://github.com/sipeed/picoclaw/pull/2990) | **Medium** — data integrity issue |
| **Streaming retry for empty responses** | ~9 days | [#2983](https://github.com/sipeed/picoclaw/pull/2983) | **Medium-High** — silent failure mode in LLM loop |
| **NEAR AI provider** | ~20 days | [#2917](https://github.com/sipeed/picoclaw/pull/2917) | Low — feature addition, not regression |
| **Turn completion signal** | ~8 days | [#2984](https://github.com/sipeed/picoclaw/issues/2984) | **Medium** — protocol design decision needed |

### Maintainer Attention Needed
- **Security batch**: 15 disclosures from YLChen-007 require coordinated response; only 2 have open PRs
- **Context management trio**: [#2988](https://github.com/sipeed/picoclaw/pull/2988), [#2990](https://github.com/sipeed/picoclaw/pull/2990), [#2987](https://github.com/sipeed/picoclaw/pull/2987) — related to compression and streaming correctness; should be reviewed together for architectural consistency

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw Project Digest — 2026-06-10

## 1. Today's Overview

NanoClaw shows **high velocity but low research-relevant signal** in the last 24 hours. Of 43 PRs updated, 39 were merged/closed—indicating active maintainer throughput—but the overwhelming majority concern infrastructure, documentation, security hardening, and skill marketplace mechanics rather than core model capabilities. **Zero releases** and only **one open issue** (#1690) suggest the project is in a consolidation phase rather than expansion. Notably absent from today's activity: any PRs addressing vision-language integration, reasoning architecture, training methodology, or hallucination mitigation—key areas for multimodal AI research.

---

## 2. Releases

**None.** No new versions published in the last 24 hours.

---

## 3. Project Progress

### Merged/Closed PRs with Research-Relevant Dimensions

| PR | Focus | Research Relevance | Status |
|---|---|---|---|
| [#337](https://github.com/nanocoai/nanoclaw/pull/337) | Prompt trace logging with configurable redaction/truncation | **Moderate** — enables observability for prompt injection, data leakage, and response consistency studies; supports reproducibility research | Closed |
| [#357](https://github.com/nanocoai/nanoclaw/pull/357) | External markdown seed files in persistence context | **Low-Moderate** — long-context conditioning mechanism; could study how injected context affects hallucination or persona drift | Closed |
| [#1202](https://github.com/nanocoai/nanoclaw/pull/1202) | Agent trace observability with token/tool call logging | **Moderate** — foundational for analyzing reasoning traces, tool-use patterns, and failure modes; no truncation on tool I/O is notable for faithfulness research | Closed |
| [#1192](https://github.com/nanocoai/nanoclaw/pull/1192) | Explicit Claude model specification in code | **Low** — reduces opacity in model selection; relevant for reproducibility but not capability advancement | Closed |
| [#1605](https://github.com/nanocoai/nanoclaw/pull/1605) | Deterministic security policy engine (non-prompt-based gating) | **Moderate** — **alignment-relevant**: demonstrates shift from prompt-based to code-based safety enforcement, reducing jailbreak surface; tool restriction architecture could constrain hallucinated tool calls | Closed |

### Infrastructure-Heavy Closures (Low Research Relevance)
- #212 (WebUI control panel), #214 (security audit docs), #1285 (direct runner mode), #1309 (skill marketplace), #1387 (plugin system), #1527 (Room API proxy), #1161 (dev setup skill), #1245 (approval-gated skills), #1333 (build metadata), #2722 (CSPRNG fix), #2721/#379/#380/#481/#1084 (documentation)

---

## 4. Community Hot Topics

### Most Active Discussion: [#1690 — Multi-runtime agent SDK abstraction](https://github.com/nanocoai/nanoclaw/issues/1690)
- **Activity**: 4 comments, 3 reactions, last updated 2026-06-09
- **Core proposal**: Modular agent runtime interface (`AgentRuntime`) enabling plug-and-play substitution between Claude SDK, Codex, and local models via skill-like installation pattern
- **Underlying research need**: **Model interoperability and capability benchmarking** — users want to compare reasoning quality, cost, latency across model providers without architectural lock-in
- **Research implication**: If implemented, would create natural A/B testing infrastructure for hallucination rates, tool-use accuracy, and long-context adherence across model families
- **Gap**: No explicit mention of vision-language models in proposal; local model path unspecified (quantized? MoE?)

### No Other High-Activity Items
All PRs show `undefined` or zero comments—indicating either low controversy or maintainer-driven merge patterns without community debate.

---

## 5. Bugs & Stability

| Issue/PR | Severity | Description | Fix Status |
|---|---|---|---|
| [#2722](https://github.com/nanocoai/nanoclaw/pull/2722) | **High (Security)** | `Math.random` used for pairing codes → predictable ownership hijacking; fixed with `crypto.randomInt` | Open (unmerged, but fix ready) |
| [#1605](https://github.com/nanocoai/nanoclaw/pull/1605) | **Moderate (Security/Reliability)** | Previous prompt-based security gating bypassable; replaced with deterministic code enforcement | Closed |

**Research-relevant stability note**: The CSPRNG fix (#2722) and security policy engine (#1605) both address **adversarial robustness**—a prerequisite for reliable AI systems. However, neither targets model-level hallucination or reasoning failure modes specifically.

---

## 6. Feature Requests & Roadmap Signals

### Explicitly Requested or Implied Directions

| Signal | Source | Likelihood in Next Version | Research Relevance |
|---|---|---|---|
| Multi-model runtime abstraction | #1690 | High — aligns with skill architecture pattern | Enables systematic model comparison for VLM/reasoning benchmarks |
| Enhanced observability/tracing | #337, #1202 | Already landed; likely extension to streaming traces | Critical for hallucination detection research |
| External context seeding | #357 | Landed; may expand to dynamic retrieval | Long-context understanding, RAG integration |
| Deterministic safety enforcement | #1605 | Landed; pattern may extend to output filtering | Alignment methodology: code > prompts |

### Notably Absent from Roadmap Signals
- **Vision-language capabilities**: No PRs or issues mention image/video input, multimodal grounding, or visual reasoning
- **Chain-of-thought or reasoning transparency**: No explicit reasoning step logging beyond token counts
- **Hallucination detection/mitigation**: No dedicated features; reliance on generic observability
- **Fine-tuning or post-training alignment**: No training infrastructure exposed

---

## 7. User Feedback Summary

### Pain Points (Inferred from PR Motivations)
1. **Opacity in model behavior**: #1192 ("hard to find out which model is being used") — reproducibility friction
2. **Container overhead**: #1285 (direct runner mode) — latency/cost for local development
3. **Security trust**: #1605, #2722 — users need deterministic, auditable safety guarantees
4. **Customization complexity**: #2721, #481 — merge conflicts on update drive skill-based architecture

### Satisfaction Drivers
- Modular skill system appears well-adopted (marketplace PR #1309, multiple skill PRs)
- Observability investments (#1202) suggest user demand for operational visibility

### Dissatisfaction/Research Gap
- **No evidence of multimodal demand being addressed** — project remains text-centric despite "NanoClaw" branding suggesting potential hardware/edge integration
- **No hallucination-specific tooling** — users must build their own detection on top of generic traces

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|---|---|---|---|
| [#1690](https://github.com/nanocoai/nanoclaw/issues/1690) Multi-runtime abstraction | ~2 months open | **Moderate** — high engagement, no assignee | **High** — would unlock cross-model reasoning studies |
| [#212](https://github.com/nanocoai/nanoclaw/pull/212) WebUI control panel | ~4 months, blocked/pending closure | Low — superseded by other work | Low |
| [#214](https://github.com/nanocoai/nanoclaw/pull/214) Security audit docs | ~4 months, needs review | Low — documentation | Low |

### Critical Gap for Research Community
**No open issues or PRs address**: vision-language integration, reasoning chain verification, RLHF/DPO-style alignment, or hallucination metrics. The project's architecture (skills, traces, deterministic policies) provides *infrastructure* for such research, but the core team appears focused on platform stability and security rather than capability advancement. Researchers may need to contribute upstream or build on this foundation independently.

---

## Research Assessment Summary

| Dimension | Score | Notes |
|---|---|---|
| Vision-Language Capabilities | ⚪ None | No evidence in codebase activity |
| Reasoning Mechanisms | 🟡 Nascent | Traces exist; no CoT extraction, no step-level verification |
| Training Methodologies | ⚪ None | No training/fine-tuning infrastructure exposed |
| Hallucination Mitigation | 🟡 Indirect | Generic observability only; no targeted detection |
| AI Reliability | 🟢 Active | Security hardening, deterministic policies, CSPRNG fixes |

**Recommendation for researchers**: NanoClaw's trace infrastructure (#1202, #337) and deterministic policy framework (#1605) provide a solid foundation for studying agent behavior, but the project currently functions as a **deployment platform** rather than a **research vehicle** for multimodal reasoning advancement. The multi-runtime abstraction (#1690) represents the highest-leverage near-term opportunity for cross-model capability studies.

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw Project Digest — 2026-06-10

## 1. Today's Overview

NullClaw shows moderate maintenance activity with **6 closed and 1 open PR** alongside **4 closed and 1 open issue** in the past 24 hours, indicating steady bug-fix velocity without new feature development. No releases were published. The activity pattern suggests a stabilization phase focused on configuration robustness, provider interoperability, and UI polish rather than architectural expansion. Notably, all closed items received same-day resolution, pointing to responsive maintainer engagement. The single open PR (#946) touches on tool-filtering logic for system prompts—a research-relevant area for reasoning and agent control.

---

## 2. Releases

**None** — No new versions published.

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant Items)

| PR | Focus | Research Relevance |
|---|---|---|
| [#946](https://github.com/nullclaw/nullclaw/pull/946) *(open)* | Tool filtering in system prompts by `tool_filter_groups` | **Reasoning/control**: Separates tool visibility in text prompts from actual tool availability via API-native calling; enables dynamic tool gating without prompt pollution |
| [#945](https://github.com/nullclaw/nullclaw/pull/945) | PII redaction: reject ISO date/time as false-positive phone matches | **Hallucination/robustness**: Reduces over-redaction that corrupts temporal reasoning signals |
| [#940](https://github.com/nullclaw/nullclaw/pull/940) | Query `base_url` for custom OpenAI-compatible providers | **Training/evaluation infrastructure**: Enables swapping model backends for benchmarking |
| [#939](https://github.com/nullclaw/nullclaw/pull/939) | Honor `compact_context` flag | **Long-context**: Gives explicit control over context compression, relevant to context window studies |
| [#711](https://github.com/nullclaw/nullclaw/pull/711) | Cross-memory event stream | **Multi-agent reasoning**: Deterministic memory synchronization across agent instances |

**Skipped as non-research**: [#947](https://github.com/nullclaw/nullclaw/pull/947) (commercial provider addition), [#943](https://github.com/nullclaw/nullclaw/pull/943) (UI typing indicator)

---

## 4. Community Hot Topics

| Item | Activity | Underlying Need |
|---|---|---|
| [#941](https://github.com/nullclaw/nullclaw/issues/941) *(open)* | 1 comment, active since May 31 | **Agent execution reliability**: Cron-scheduled agent tasks fail silently; subprocess spawning broken for `agent` job type |
| [#936](https://github.com/nullclaw/nullclaw/issues/936) → [#940](https://github.com/nullclaw/nullclaw/pull/940) | 1 comment, resolved | **Provider abstraction integrity**: Hardcoded model fallbacks undermine custom endpoint evaluation |
| [#946](https://github.com/nullclaw/nullclaw/pull/946) *(open)* | No comments yet | **Fine-grained tool control**: Users need selective tool exposure without losing dynamic dispatch capability |

**Analysis**: The strongest signal is demand for **predictable agent execution infrastructure** (#941) and **configurable reasoning boundaries** (#946). The tool-filtering PR suggests users want to constrain agent reasoning scope without disabling tools entirely—relevant to safety and capability control research.

---

## 5. Bugs & Stability

| Severity | Issue | Fix Status | Research Impact |
|---|---|---|---|
| **High** | [#941](https://github.com/nullclaw/nullclaw/issues/941): Agent cron jobs silently fail—no subprocess spawned, no Telegram delivery | **Open, no PR** | Breaks automated evaluation pipelines; agent outputs lost without trace |
| Medium | [#944](https://github.com/nullclaw/nullclaw/issues/944): PII redactor corrupts date/time output | Fixed by [#945](https://github.com/nullclaw/nullclaw/pull/945) | Corrupted timestamps disrupt temporal reasoning benchmarks |
| Medium | [#936](https://github.com/nullclaw/nullclaw/issues/936): Custom providers ignored for model listing | Fixed by [#940](https://github.com/nullclaw/nullclaw/pull/940) | Blocks systematic model comparison studies |
| Low | [#937](https://github.com/nullclaw/nullclaw/issues/937): `compact_context` dead flag | Fixed by [#939](https://github.com/nullclaw/nullclaw/pull/939) | Previously forced unwanted context loss; now user-controllable |

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Release |
|---|---|---|
| **Dynamic tool visibility in prompts** | [#946](https://github.com/nullclaw/nullclaw/pull/946) | High — open PR, active review |
| **Cross-instance memory synchronization** | [#711](https://github.com/nullclaw/nullclaw/pull/711) | Moderate — merged but needs adoption patterns |
| **Robust agent scheduling/execution** | [#941](https://github.com/nullclaw/nullclaw/issues/941) | High — blocking core functionality |
| **Enhanced PII redaction configurability** | [#944](https://github.com/nullclaw/nullclaw/issues/944)/[#945](https://github.com/nullclaw/nullclaw/pull/945) | Moderate — pattern library likely to expand |

**Research-relevant trajectory**: The tool-filtering work (#946) suggests movement toward **modular reasoning architectures** where tool availability can be conditioned on context without re-prompting. This aligns with broader trends in constrained agent reasoning and safety filtering.

---

## 7. User Feedback Summary

| Pain Point | Evidence | User Segment |
|---|---|---|
| Silent failures in automated workflows | [#941](https://github.com/nullclaw/nullclaw/issues/941) | Power users, integration-dependent |
| Over-aggressive output sanitization | [#944](https://github.com/nullclaw/nullclaw/issues/944) | All users (default-on feature) |
| Configuration flags that don't take effect | [#937](https://github.com/nullclaw/nullclaw/issues/937) | Advanced users tuning context behavior |
| Provider lock-in despite "compatible" claims | [#936](https://github.com/nullclaw/nullclaw/issues/936) | Researchers, multi-model evaluators |

**Satisfaction**: Rapid fix turnaround (all closed items resolved within 24h of update).
**Dissatisfaction**: Core reliability gaps (#941) and "magic" defaults that override explicit configuration (#937, #944).

---

## 8. Backlog Watch

| Item | Age | Risk | Action Needed |
|---|---|---|---|
| [#941](https://github.com/nullclaw/nullclaw/issues/941) Agent cron subprocess failure | 10 days | **High** — core functionality broken, no PR linked | Maintainer assignment or community PR |
| [#946](https://github.com/nullclaw/nullclaw/pull/946) Tool filtering | 7 days | Moderate — open, needs review/merge decision | Code review, merge or request changes |

No stale long-term backlog items are visible in today's data; the project appears to maintain relatively tight issue resolution cycles.

---

*Digest generated from NullClaw GitHub activity 2026-06-09. Filtered for research relevance: vision-language capabilities, reasoning mechanisms, training methodologies, hallucination-related issues. Commercial/provider marketing content excluded where possible.*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw Project Digest — 2026-06-10
## Research Focus: Vision-Language, Reasoning, Training Methodologies, Hallucination/Reliability

---

## 1. Today's Overview

IronClaw shows **high engineering velocity** with 97 items updated in 24 hours (47 issues, 50 PRs), though **zero new releases** indicate this is pre-release consolidation phase. Activity is heavily concentrated on **Reborn production readiness** (M4 host-kernel module) and **security/audit hardening** rather than frontier model capabilities. Notably absent from today's feed: explicit vision-language model work, multimodal reasoning research, or training methodology papers—suggesting IronClaw remains an **infrastructure/orchestration layer** for AI systems rather than a model development platform. The research-relevant signal lies in **provider normalization**, **tool-use reliability fixes**, and **hallucination-adjacent validation bugs** (strict-mode schema rejection, duplicate field serialization).

---

## 2. Releases

**None** — No new releases in the tracking period.

---

## 3. Project Progress

### Closed Issues (Research-Relevant Subset)

| Item | Description | Research Relevance |
|------|-------------|------------------|
| [#4447](https://github.com/nearai/ironclaw/issues/4447) | OpenAI-compatible API migration closure — compatibility/security tests | **API reliability**, provider abstraction completeness |
| [#4446](https://github.com/nearai/ironclaw/issues/4446) | SSE streaming translation for Chat/Responses | **Streaming reasoning**, real-time tool-use feedback loops |
| [#4591](https://github.com/nearai/ironclaw/issues/4591) | Operator command-plane foundation | Infrastructure, not research-relevant |
| [#4604](https://github.com/nearai/ironclaw/issues/4604) | WebUI v2 E2E testing gap | Test methodology, not core research |
| [#4609](https://github.com/nearai/ironclaw/issues/4609) | Auth parity for WebChat v2 | Security, not research-relevant |

### Merged/Closed PRs — No explicit merges listed; 8 PRs in merged/closed state total. Research-relevant advances appear in **open PRs** targeting reliability:

- **[#4583](https://github.com/nearai/ironclaw/pull/4583)** — `NormalizingProvider` Layer-3 decorator: **Forces `FinishReason::ToolUse` when `tool_calls` non-empty + non-`ToolUse` finish_reason**. Directly addresses **reasoning consistency** and **tool-use hallucination** where models emit tool calls but incorrect finish reasons.
- **[#4650](https://github.com/nearai/ironclaw/pull/4650)** — Temperature dropping for reasoning models (Opus 4.7/4.8, gpt-5.x): Provider-level **training-inference mismatch handling**, relevant to **post-training alignment** where model families diverge in parameter acceptance.

---

## 4. Community Hot Topics

### By Comment Activity

| Rank | Item | Comments | Core Tension |
|------|------|----------|------------|
| 1 | [#3026](https://github.com/nearai/ironclaw/issues/3026) — Reborn production wiring/cutover readiness | 3 | **System reliability vs. deployment velocity** — production graph validation |
| 2 | [#4642](https://github.com/nearai/ironclaw/issues/4642) — Strict-mode null-for-unset-optionals rejected | 1 | **LLM provider behavior variance** — strict-mode schemas vs. flexible tool calling |
| 3 | [#88](https://github.com/nearai/ironclaw/issues/88) — Security hardening (pairing, media URL validation) | 1 | **Multimodal safety** — media URL validation touches vision-language input boundaries |
| 4 | [#4551](https://github.com/nearai/ironclaw/issues/4551) — Postgres storage config wiring | 1 | Infrastructure persistence |
| 5 | [#4548](https://github.com/nearai/ironclaw/issues/4548) — Duplicate `model` field with tools (DeepSeek 400) | 1 | **Provider-specific serialization bugs** — tool-use reliability |

### Research-Relevant Analysis

**[#4642](https://github.com/nearai/ironclaw/issues/4642)** — **Hallucination-adjacent schema validation failure**: Strict-mode providers (OpenAI, Anthropic) send `null` for unset optionals; IronClaw's capability-port validator rejects against original non-nullable schema. This is a **contractual hallucination** where the system invents invalidity from valid model behavior. Fix requires **schema normalization layer** — aligns with post-training alignment concerns about tool-use reliability.

**[#4548](https://github.com/nearai/ironclaw/issues/4548)** — **DeepSeek tool-call serialization bug**: Duplicate `model` field when tools included. Suggests **request construction fragility** in multimodal/tool-use paths; DeepSeek's 400 rejection indicates **provider-specific reasoning path divergence**.

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|----------|------|-------------|------------|
| **P0-equivalent** | [#4642](https://github.com/nearai/ironclaw/issues/4642) | Strict-mode provider tool calls rejected — **breaks most first-party tools** | No linked fix PR |
| **P1** | [#4548](https://github.com/nearai/ironclaw/issues/4548) | DeepSeek 400 on tool calls (duplicate `model` field) | No linked fix PR |
| **P1** | [#4640](https://github.com/nearai/ironclaw/issues/4640) | Google Calendar `list_events` returns oldest/unordered — **temporal reasoning failure** | No linked fix PR |
| **P2** | [#4587](https://github.com/nearai/ironclaw/issues/4587) | Minimax provider configuration fails (secret metadata read) | No linked fix PR |

### Research-Relevant Stability Notes

- **[#4640](https://github.com/nearai/ironclaw/issues/4640)** — **Temporal reasoning defect in tool implementation**: Missing `timeMin` default and `singleEvents`/`orderBy` parameters causes "what are my upcoming meetings?" to return oldest events. This is a **grounding failure** where the system lacks implicit temporal context—relevant to **long-context understanding** (event sequences) and **hallucination** (returning irrelevant historical data as current).

- **[#4583](https://github.com/nearai/ironclaw/pull/4583)** (open, not bug but fix architecture) — `NormalizingProvider` addresses **reasoning consistency** at the provider boundary. The forced `FinishReason::ToolUse` correction suggests observed **model misalignment** where tool-calling and finish-reason signals desynchronize—possible **emergent behavior** in chain-of-thought or tool-augmented reasoning paths.

---

## 6. Feature Requests & Roadmap Signals

| Item | Signal | Research Relevance |
|------|--------|------------------|
| [#4647](https://github.com/nearai/ironclaw/issues/4647) — Unified (omni) search | **Multimodal retrieval** across threads, skills, extensions, memory | Long-context understanding, cross-modal retrieval |
| [#4644](https://github.com/nearai/ironclaw/issues/4644) — Universal attachments, extensible format registry | **Vision-language input pipeline** for Reborn; format registry for future modalities | Multimodal reasoning infrastructure |
| [#4628](https://github.com/nearai/ironclaw/issues/4628) — Admin-shared tools with per-user auth | **Tool-use governance**, permissioned reasoning | Post-training alignment, safety |
| [#4559](https://github.com/nearai/ironclaw/pull/4559) — Agent-driven Trace Commons onboarding | **Agent autonomy**, consent-gathering workflows | Agentic reasoning, reliability |

### Prediction

**[#4644](https://github.com/nearai/ironclaw/issues/4644)** (universal attachments) is most likely to surface in next release as it unblocks **multimodal input** for Reborn. Current `MessageContent` is text-only—this is a **foundational gap for vision-language capabilities**. The "extensible format registry" design suggests preparation for image, audio, video modalities.

---

## 7. User Feedback Summary

### Explicit Pain Points (from issue descriptions)

| Pain Point | Source | Research Dimension |
|------------|--------|------------------|
| "Reborn's transcript contract is text-only" — attachments silently dropped | [#4644](https://github.com/nearai/ironclaw/issues/4644) | **Multimodal reasoning blocked** |
| "what are my upcoming meetings?" returns oldest events | [#4640](https://github.com/nearai/ironclaw/issues/4640) | **Temporal grounding failure** |
| Strict-mode providers' valid tool calls rejected | [#4642](https://github.com/nearai/ironclaw/issues/4642) | **Tool-use reliability**, provider alignment |
| DeepSeek rejects requests with tools | [#4548](https://github.com/nearai/ironclaw/issues/4548) | **Cross-provider reasoning consistency** |
| No unified search across modalities | [#4647](https://github.com/nearai/ironclaw/issues/4647) | **Long-context retrieval fragmentation** |

### Implicit Signal

High volume of **security/audit PRs** (#4563, #4565, #4567, #4568, #4569) by `zmanian` suggests **production deployment anxiety** — the system is being hardened for real-world exposure where **hallucination-induced security failures** (credential leaks, unauthorized egress) would be catastrophic. This is **alignment-adjacent**: ensuring model actions stay within policy boundaries.

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|------|-----|------|------------------|
| [#88](https://github.com/nearai/ironclaw/issues/88) — Security hardening (media URL validation) | 116 days | **Medium** | **Vision-language safety**: media URL validation is prerequisite for safe image/video input processing |
| [#3026](https://github.com/nearai/ironclaw/issues/3026) — Reborn production wiring | 43 days | **High** | Infrastructure blocking research-relevant features |
| [#4539](https://github.com/nearai/ironclaw/issues/4539) — Persistent approval policies (parent of #4613) | Implied | Medium | **Post-training alignment**: human-in-the-loop governance |

### Maintainer Attention Needed

- **[#88](https://github.com/nearai/ironclaw/issues/88)** — Media URL validation is **foundational for multimodal safety** but languishing at P2-P3. Without this, vision-language capabilities risk **SSRF via malicious image URLs**, **prompt injection through media metadata**, or **untrusted content execution**.

- **[#4642](https://github.com/nearai/ironclaw/issues/4642)** + **[#4548](https://github.com/nearai/ironclaw/issues/4548)** — Both are **active tool-use reliability failures** with no linked PRs. These affect **first-party tool coverage** and **major provider compatibility** (DeepSeek). Given Reborn's production push, these represent **regression risk** for reasoning-dependent workflows.

---

## Research Synthesis

IronClaw on 2026-06-10 is **infrastructure-consolidation mode**, not frontier-research mode. The research-relevant signals are:

1. **Tool-use reliability engineering** — `NormalizingProvider`, strict-mode schema fixes, temperature handling for reasoning models. This is **post-training alignment at the serving layer**.

2. **Multimodal infrastructure preparation** — Universal attachments (#4644), omni-search (#4647), media URL validation (#88). Vision-language capabilities are **blocked on text-only legacy** but actively being unblocked.

3. **Hallucination-adjacent validation** — Temporal grounding failures (#4640), finish-reason normalization (#4583), provider-specific serialization bugs (#4548). These are **system-level mitigations for model misbehavior** rather than model-level fixes.

4. **Absent**: No explicit work on **long-context architectures**, **multimodal training recipes**, **RLHF/RLAIF**, or **evaluation benchmarks**. IronClaw's research contribution is **reliable orchestration of unreliable models**, not model improvement itself.

**Recommendation for research tracking**: Monitor [#4644](https://github.com/nearai/ironclaw/issues/4644) and [#88](https://github.com/nearai/ironclaw/issues/88) for multimodal capability emergence; [#4583](https://github.com/nearai/ironclaw/pull/4583) and [#4642](https://github.com/nearai/ironclaw/issues/4642) for empirical insights into tool-use misalignment patterns across providers.

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI Project Digest — 2026-06-10

## 1. Today's Overview

LobsterAI shows **moderate engineering activity** with 5 PRs updated (4 merged/closed, 1 open) and 2 new issues opened, but **zero releases**. The day's work centers on **Cowork session infrastructure**—specifically task completion notifications and cross-session state recovery—rather than core model capabilities. Notably absent from today's activity are any commits touching vision-language models, reasoning architectures, or training pipelines. The project appears to be in a **product stabilization phase** with emphasis on desktop client reliability and multi-agent orchestration workflows. No hallucination-related or alignment-focused research surfaced in the 24-hour window.

---

## 2. Releases

**None** — No new versions published.

---

## 3. Project Progress

### Merged/Closed PRs Today

| PR | Author | Areas | Research Relevance | Link |
|:---|:---|:---|:---|:---|
| **#2130** — feat(cowork): add task completion notifications | liuzhq1986 | renderer, build, docs, main | **Low** — Desktop notification infrastructure; privacy-preserving design pattern (no prompt exposure) may inform future **safety-critical agent deployments** | [PR #2130](https://github.com/netease-youdao/LobsterAI/pull/2130) |
| **#2134** — task complete notice (restoration logic) | liuzhq1986 | renderer, docs, main | **Low-Medium** — Session state recovery for **long-running multi-agent workflows**; relevant to context persistence research | [PR #2134](https://github.com/netease-youdao/LobsterAI/pull/2134) |
| **#2136** — data backup and migration | fisherdaddy | renderer, docs, main | **None** — User data portability | [PR #2136](https://github.com/netease-youdao/LobsterAI/pull/2136) |
| **#2135** — temporary close databackup | fisherdaddy | renderer | **None** — Feature rollback | [PR #2135](https://github.com/netease-youdao/LobsterAI/pull/2135) |

**Key Technical Detail:** PR #2134 implements **deferred renderer readiness checks** (`Wait for the renderer notification handler to be ready before opening the target Cowork session`), suggesting race-condition hardening in asynchronous agent session initialization—a pattern relevant to **reliable multi-step reasoning pipelines**.

---

## 4. Community Hot Topics

### Issue #2132: Cross-Model Subtask Collaboration Mechanism
- **Status:** OPEN | **Comments:** 0 | **Reactions:** 0
- **Link:** [Issue #2132](https://github.com/netease-youdao/LobsterAI/issues/2132)
- **Author:** woxinsj

**Research-Relevant Analysis:**

This issue exposes a **critical architectural gap in heterogeneous agent orchestration**:

| Aspect | Detail |
|:---|:---|
| **Problem** | Cross-model subtask delegation lacks the callback/notification mechanism present in same-model subtasks |
| **Root Cause Identified** | `call_function_gblu0nmqpcej_1` is a **gateway function call**, not a `sessions_spawn`-created subtask—bypassing the session tracking registry |
| **Proposed Fix** | (1) Port same-model completion callbacks to cross-model paths; (2) Implement proactive subtask→parent notification on completion or blockage |

**Research Significance:** Directly touches **multi-agent reasoning topology**, **orchestration reliability**, and **failure-mode propagation**—all active areas in LLM systems research. The "M3 (planning/verification) + DeepSeek (execution)" decomposition mirrors **hierarchical reasoning** architectures (e.g., Tree of Thoughts, Meta-Reasoning). The absence of cross-model state synchronization risks **silent failures** and **hallucinated completion status** (agent believes subtask finished when it hasn't).

> **Prediction:** This pattern—heterogeneous model routing with explicit handoff protocols—will become a core requirement for reliable compound AI systems.

### Issue #2131: Hermes Agent Support
- **Status:** OPEN | **Comments:** 1 | **Reactions:** 0
- **Link:** [Issue #2131](https://github.com/netease-youdao/LobsterAI/issues/2131)
- **Research Relevance:** **Low** — Framework integration request; no technical detail provided

---

## 5. Bugs & Stability

| Severity | Item | Description | Fix Status |
|:---|:---|:---|:---|
| **Medium** | **PR #2133** [OPEN] — fix export and code copy bugs | Export functionality and code copying broken in renderer/cowork areas | **Fix proposed, awaiting merge** — [PR #2133](https://github.com/netease-youdao/LobsterAI/pull/2133) |
| **Low** (resolved) | PR #2135 | Temporary rollback of data backup feature | Mitigated via revert |

**Stability Assessment:** No crashes or regressions in core inference paths reported. The open export/code-copy bug affects **artifact extraction from agent sessions**—potentially impacting research reproducibility if users cannot capture model outputs.

---

## 6. Feature Requests & Roadmap Signals

| Signal | Source | Likelihood in Next Release | Research Relevance |
|:---|:---|:---|:---|
| **Cross-model subtask notification protocol** | Issue #2132 | **High** — Architectural debt, user-blocking | **High** — Enables reliable heterogeneous agent evaluation |
| Hermes agent framework integration | Issue #2131 | Medium | Low |
| Persistent notification state recovery | PR #2134 | Shipped | Low |

**Missing Signals:** No explicit requests for:
- Vision-language input support (image understanding, video)
- Chain-of-thought visualization or reasoning trace export
- RLHF/alignment tooling
- Hallucination detection/mitigation features

This **absence is notable** given the project's apparent multi-agent orientation—suggesting either (a) these capabilities exist in undisclosed branches, or (b) LobsterAI's current scope is narrowly focused on text-based orchestration.

---

## 7. User Feedback Summary

### Pain Points
| Issue | Evidence | Underlying Need |
|:---|:---|:---|
| **Silent cross-model task failures** | Issue #2132 detailed root-cause analysis | **Observability and guaranteed handoffs** in distributed agent systems |
| **Session state fragility** | PR #2134 addresses main window destruction | Long-running agent workflows need **persistent context** independent of UI lifecycle |
| **Privacy concern in notifications** | PR #2130 explicitly avoids exposing "task titles or user prompts" | **Output sanitization** for agent systems handling sensitive prompts |

### Satisfaction Indicators
- User woxinsj provided **detailed technical diagnosis** with proposed fix architecture—suggesting engaged power-user base capable of contributing systems-level improvements

---

## 8. Backlog Watch

| Item | Age | Risk | Research Relevance |
|:---|:---|:---|:---|
| **Issue #2132** — Cross-model subtask collaboration | 1 day | **High** — Open, zero maintainer response, blocks heterogeneous agent workflows | **High** — Core to reliable multi-model reasoning |
| **PR #2133** — Export/code-copy fixes | 1 day | Medium — Open, affects data extraction | Low |

**Maintainer Attention Needed:** Issue #2132 warrants priority response given its **systems-architecture scope** and the reporter's investment in root-cause analysis. The proposed solution (gateway call tracking, proactive notification) should be evaluated against existing `sessions_spawn` semantics.

---

## Research Analyst Notes

**Vision-Language Capabilities:** **No evidence** in today's activity. No image/video processing PRs, no multimodal model integration issues.

**Reasoning Mechanisms:** **Indirect evidence only** — Issue #2132's "M3 planning + DeepSeek execution" decomposition suggests internal use of **specialized reasoning routing**, but no explicit reasoning architecture (chain-of-thought, tree search, self-consistency) is visible.

**Training Methodologies:** **None observed.**

**Hallucination-Related Issues:** **None explicitly labeled.** However, Issue #2132's "subtask completion without parent notification" represents a **structural hallucination risk**—the parent agent may proceed on false assumptions of subtask success. PR #2130's privacy-safe notification design (hiding prompt content) prevents **information leakage** but does not address **content veracity**.

**Overall Assessment:** LobsterAI appears to be a **mature orchestration layer** (desktop client, session management, multi-agent routing) rather than a **research-active foundation model project**. Today's activity is consistent with **product engineering** rather than **model capability advancement**. Researchers tracking this project should monitor Issue #2132 for signals about heterogeneous agent reliability, but should not expect frontier multimodal or alignment research to surface in public commits.

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

# CoPaw Project Digest — 2026-06-10
## Research Focus: Multimodal Reasoning, Long-Context Understanding, Post-Training Alignment & AI Reliability

---

## 1. Today's Overview

CoPaw shows **high development velocity** with 33 issues and 34 PRs updated in 24 hours, indicating an active maintenance cycle for the v1.1.11-beta.2 release. Research-relevant activity concentrates on **reasoning content handling** (multiple closed issues around thinking/reasoning display), **long-context compression mechanics** (context window configuration fixes), and **vision-language architecture** (visual model fallback proposals). The project is mid-migration to AgentScope 2.0 backend, suggesting significant architectural shifts affecting reproducibility of prior experimental results. Notably, **hallucination-adjacent issues** appear in reasoning content parsing errors and tool call extraction failures in streaming contexts.

---

## 2. Releases

### v1.1.11-beta.2
- **Browser automation enhancements**: Page coordinate click support added to `browser_control` ([PR #4905](https://github.com/agentscope-ai/QwenPaw/pull/4905))
- **Cross-browser isolation**: CDP timeout parameterization and browser profile isolation for switching contexts ([PR by x1n95c](https://github.com/agentscope-ai/QwenPaw/pull/))

*Research relevance*: Browser control improvements support web-grounded multimodal agents; profile isolation enables cleaner experimental separation of agent environments.

---

## 3. Project Progress

### Merged/Closed PRs (Research-Relevant)

| PR | Description | Research Relevance |
|:---|:---|:---|
| [#5021](https://github.com/agentscope-ai/QwenPaw/pull/5021) | Fix `/compact` and auto-compaction ignoring model's `max_input_length` when `active_model` unset | **Long-context understanding**: Corrects silent fallback to 128K default, critical for reproducible context window experiments |
| [#4857](https://github.com/agentscope-ai/QwenPaw/pull/4857) | Enhanced make-skill flow with **self-evolving skill creation** | **Post-training alignment**: Background execution via `spawn_subagent(fork=True)` with full context inheritance enables autonomous skill iteration loops |
| [#5043](https://github.com/agentscope-ai/QwenPaw/pull/5043) | OpenSandbox plugin with MCP protocol | **AI reliability**: Isolated execution environment for untrusted code reduces capability overhang risks |
| [#5049](https://github.com/agentscope-ai/QwenPaw/pull/5049) | Zero-config free models & OAuth authentication | Infrastructure; reduces experimental setup friction |
| [#5048](https://github.com/agentscope-ai/QwenPaw/pull/5048) | Fix unawaited coroutine in `_broadcast_to_subscribers` | **Reliability**: Async metaclass hook misidentification could cause non-deterministic message propagation |

---

## 4. Community Hot Topics

### Most Active Research-Relevant Discussions

| Issue/PR | Comments | Topic | Underlying Research Need |
|:---|:---|:---|:---|
| [#5017](https://github.com/agentscope-ai/QwenPaw/issues/5017) | 10 | Hermes Agent "learning loop" feature comparison | **Autonomous skill acquisition**: Community seeking self-improving agent architectures beyond static fine-tuning |
| [#5003](https://github.com/agentscope-ai/QwenPaw/issues/5003) | 8 | Qwen3.7-plus freezing in coding plans | **Reasoning reliability**: Model-specific hanging suggests prompt/reasoning chain incompatibility |
| [#4727](https://github.com/agentscope-ai/QwenPaw/issues/4727) | 7 | **AgentScope 2.0 migration** (OPEN, breaking change) | **Backend reproducibility**: Major architecture shift; research code targeting 1.x APIs will break |
| [#4937](https://github.com/agentscope-ai/QwenPaw/issues/4937) | 5 | `/compact` ignores custom `max_input_length` | **Long-context mechanics**: Configuration propagation failures in context compression pipelines |
| [#4992](https://github.com/agentscope-ai/QwenPaw/issues/4992) | 3 | **Visual Model Fallback** (OPEN) | **Vision-language decoupling**: Architectural proposal for separating vision and language model responsibilities |

**Key insight**: The Hermes Agent comparison (#5017) and Visual Model Fallback (#4992) both signal community demand for **modular, composable model architectures** rather than monolithic multimodal endpoints—enabling better experimental control and failure mode isolation.

---

## 5. Bugs & Stability

### Severity-Ranked Research-Critical Issues

| Severity | Issue | Description | Fix Status |
|:---|:---|:---|:---|
| **High** | [#5039](https://github.com/agentscope-ai/QwenPaw/issues/5039) | **Tool call extraction race condition**: Tag-derived tool calls from multiple thinking/text blocks overwrite each other in OpenAI-compatible stream parser | Closed; root cause: per-block dict assignment instead of accumulation |
| **High** | [#5045](https://github.com/agentscope-ai/QwenPaw/issues/5045) / [#5034](https://github.com/agentscope-ai/QwenPaw/issues/5034) | **Tool naming incompatibility**: `pat.batch_plan` dot-notation violates OpenAI `^[a-zA-Z0-9_-]+$` regex; DeepSeek API rejects, causes 400 errors | Closed in `stateful_client.py` |
| **High** | [#4006](https://github.com/agentscope-ai/QwenPaw/issues/4006) | **Reasoning content leakage**: MiniMax provider fails to filter reasoning content in OpenAI-compatible mode | Closed |
| **Medium** | [#4962](https://github.com/agentscope-ai/QwenPaw/issues/4962) | **DeepSeek reasoning collapse**: API responses fold content into thinking process, requiring manual expansion | Closed |
| **Medium** | [#5013](https://github.com/agentscope-ai/QwenPaw/issues/5013) | **KimiCode thinking display failure**: Reasoning content generated but not surfaced in UI | Closed |
| **Medium** | [#4989](https://github.com/agentscope-ai/QwenPaw/issues/4989) | Local Qwen3.6-27B via vLLM: responses hang (regression from 1.1.5.post2) | **OPEN** — reproducibility concern for local model experiments |

**Pattern**: **4/6 high-impact bugs involve reasoning content handling**, indicating fragility in the reasoning-to-action pipeline—critical for reliability of chain-of-thought dependent systems.

---

## 6. Feature Requests & Roadmap Signals

| Request | Issue | Likelihood in Next Version | Research Implication |
|:---|:---|:---|:---|
| **Independent Visual Model Configuration** | [#4992](https://github.com/agentscope-ai/QwenPaw/issues/4992) | High — 3 comments, 👍1, aligns with modular architecture trend | Enables controlled V→L ablation studies; separates vision hallucination sources from reasoning |
| **Self-Evolving Memory System** | [#4994](https://github.com/agentscope-ai/QwenPaw/issues/4994) | Medium — referenced in PR #4857 skill evolution | Hierarchical memory frameworks for long-context retention without context window expansion |
| **Observability/Tracing Integration** (Langfuse, OpenTelemetry) | [#5009](https://github.com/agentscope-ai/QwenPaw/issues/5009) | Medium — enterprise demand, 2 comments | Essential for **measuring hallucination rates** and reasoning chain attribution in production |
| **OpenSandbox Isolation** | [#4951](https://github.com/agentscope-ai/QwenPaw/issues/4951) | **Shipped** in PR #5043 | Reduces experimental contamination from environment state |

---

## 7. User Feedback Summary

### Pain Points with Research Relevance

| Category | Issue | Implication |
|:---|:---|:---|
| **Reasoning transparency** | Users cannot reliably access/view model thinking across providers (DeepSeek, KimiCode, MiniMax) | **Hallucination debugging blocked**: Without reasoning visibility, cannot trace error propagation |
| **Context window configuration** | `max_input_length` silently ignored, `/compact` behavior unpredictable | **Non-reproducible long-context experiments**: Actual context usage diverges from configured limits |
| **Local model regression** | Qwen3.6-27B + vLLM worked in 1.1.5.post2, hangs in 1.1.9+ | **Version-dependent compatibility** complicates local replication studies |
| **Desktop performance collapse** | Streaming output causes system-level lag (#4792) | **Measurement artifact risk**: UI blocking may confound human evaluation timing studies |

### Satisfaction Drivers
- Strong localization for Chinese market
- "Out-of-box" experience for standard configurations

---

## 8. Backlog Watch

### Long-Duration Issues Requiring Attention

| Issue | Age | Status | Risk |
|:---|:---|:---|:---|
| [#4727](https://github.com/agentscope-ai/QwenPaw/issues/4727) AgentScope 2.0 migration | ~2 weeks | OPEN, 7 comments | **Breaking change**; blocks research reproducibility until stabilized |
| [#2777](https://github.com/agentscope-ai/QwenPaw/issues/2777) GPT-5.x `max_tokens` parameter error | ~2 months | OPEN, 4 comments | Hardcoded model lists prevent evaluation of newer reasoning models |
| [#4989](https://github.com/agentscope-ai/QwenPaw/issues/4989) Local Qwen3.6-27B hang | ~3 days | OPEN, 4 comments | Regression in local deployment path; no fix PR identified |
| [#4992](https://github.com/agentscope-ai/QwenPaw/issues/4992) Visual Model Fallback | ~3 days | OPEN, 3 comments, 👍1 | Architectural proposal with no assigned implementation |

---

## Research Assessment Summary

| Dimension | Score | Evidence |
|:---|:---|:---|
| **Vision-language maturity** | ⚠️ Moderate | Visual fallback not yet native; relies on monolithic model multimodality |
| **Reasoning robustness** | ⚠️ Moderate | Multiple provider-specific reasoning display bugs; stream parsing race conditions |
| **Long-context reliability** | ⚠️ Moderate | Configuration propagation fixes recent; silent defaults persist in edge cases |
| **Post-training alignment** | ✅ Improving | Self-evolving skills (#4857), OpenSandbox isolation (#5043) show progress |
| **Hallucination traceability** | ❌ Weak | No native observability integration; reasoning content filtering inconsistent across providers |

**Recommended monitoring**: AgentScope 2.0 migration completion (#4727), Visual Model Fallback implementation (#4992), and observability integration (#5009) as indicators of research infrastructure maturation.

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw Project Digest — 2026-06-10

## 1. Today's Overview

ZeroClaw shows **high engineering velocity** with 50 active issues and 50 pull requests updated in the last 24 hours, though merge throughput remains low (only 2 issues closed, 1 PR merged/closed). The project is in an **intensive development phase** with substantial architectural work in progress—particularly around context window management, provider abstraction, and multi-channel routing. Notably, several research-relevant items touch on **reasoning output handling**, **multimodal routing logic**, and **prompt compression/truncation strategies** that directly impact LLM reliability. The low close rate relative to open volume suggests either a backlog accumulation or maintainer bandwidth constraints on review.

---

## 2. Releases

**No new releases** (0 releases in last 24h). Current latest appears to be v0.8.0-beta-1 per issue references.

---

## 3. Project Progress

### Merged/Closed Today
| PR/Issue | Link | Summary | Research Relevance |
|----------|------|---------|------------------|
| #4710 (Issue, CLOSED) | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/4710) | Logo redesign — **non-research, filtered** | — |
| #7117 (Issue, CLOSED) | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/7117) | Config UX parity across surfaces — **non-research, filtered** | — |
| #7425 (PR, CLOSED) | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7425) | Channel pricing fallback fix | Cost accounting for LLM inference |

### Significant Open PRs with Research-Relevant Advances

| PR | Link | Progress | Research Relevance |
|----|------|----------|------------------|
| #7440 | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7440) | **Fixes futile history trim when system prompt exceeds budget** — skips preemptive trim when tool definitions alone overflow context window | **Critical for long-context understanding**: addresses fundamental context budget exhaustion from system prompt bloat (~107k tokens with default tools) |
| #7345 | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7345) | **Gates path-listing tool results from vision routing** — prevents `[IMAGE:…]` marker pollution in multimodal routing decisions | **Multimodal reasoning**: fixes false-positive vision model routing triggered by filesystem tool outputs containing image path strings |
| #7244 | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7244) | **Reinforces tool formatting prompts + robust JSON fallback parser** for `file_write` with unescaped quotes in HTML/code payloads | **Hallucination/robustness**: addresses malformed tool calls from models generating invalid JSON due to unescaped content |
| #7438 | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7438) | **Fixes Telegram delivery prompt discouraging tool use** — removes "use tool results silently" instruction causing tool execution failures on smaller models | **Alignment/prompt engineering**: incorrect system prompt induced capability underutilization (model "forgot" it could use tools) |
| #6584 (Issue) | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6584) | OpenAI-Compatible provider ignores `reasoning` field, only reads `reasoning_content` | **Reasoning mechanisms**: interoperability gap with emerging reasoning token standards (OpenRouter, vLLM) |

---

## 4. Community Hot Topics

### Most Active Research-Relevant Threads

| Rank | Issue/PR | Comments | Link | Underlying Need |
|------|----------|----------|------|---------------|
| 1 | #5808 — Default 32k context budget exceeded by system prompt + tool definitions | 3 comments | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5808) | **Fundamental long-context architecture**: Default context window (32k) is **~3.3× overflowed on iteration 1** by system prompt + tool definitions alone. Indicates need for dynamic context budgeting, hierarchical tool summarization, or prompt compression. |
| 2 | #5844 — "Too much emphasis on memory" | 6 comments | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5844) | **Retrieval-augmented generation alignment**: System prompt weighting between retrieved memories vs. current prompt is misaligned, causing cron jobs to hallucinate or over-weight stale context. Directly relevant to **contextual grounding and hallucination reduction**. |
| 3 | #6034 — User message loss in single/multi-turn dialogue | 5 comments | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6034) | **Dialogue state integrity**: Critical message dropping bug affecting conversation coherence — potential root in provider compatibility layer or history serialization. |
| 4 | #7415 — RFC: Unify three agent turn engines | 1 comment (new) | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/7415) | **Architectural consolidation for reasoning reliability**: Three divergent implementations of agent turn loop (`run_tool_call_loop`, `turn_streamed`, `Agent::turn`) with inconsistent safety guarantees. Unification would reduce behavior variance and audit surface. |

### Analysis of Underlying Needs

- **Context window crisis**: #5808 and #5844 together reveal a systemic tension between expanding capabilities (more tools, memory retrieval) and fixed context budgets. The community is effectively **discovering the "context collapse" problem** in production.
- **Reasoning token fragmentation**: #6584 shows standards divergence between `reasoning` vs. `reasoning_content` fields across providers, creating reliability issues for chain-of-thought extraction and monitoring.
- **Tool use reliability**: #7438 and #7244 demonstrate that **prompt phrasing significantly affects tool execution rates**, particularly on smaller/distilled models — a post-training alignment challenge.

---

## 5. Bugs & Stability

| Severity | Issue | Link | Description | Fix PR? |
|----------|-------|------|-------------|---------|
| **S1 — Workflow blocked** | #5808 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5808) | Context budget exhausted before any user input; perpetual preemptive trim | **#7440** addresses symptom (skip futile trim), not root cause |
| **S1 — Workflow blocked** | #6034 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6034) | User messages dropped in single/multi-turn dialogue | None identified |
| **S1 — Workflow blocked** | #6646 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6646) | `web_search_tool` and `web_fetch` not firing via Telegram | **#7438** (prompt fix) |
| **S1 — Workflow blocked** | #6687 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6687) | Two independent `SopEngine` instances — state fragmentation | None identified |
| **S2 — Degraded behavior** | #5844 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5844) | Excessive memory weighting causes misalignment with current prompt | None identified |
| **S2 — Degraded behavior** | #6584 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6584) | Reasoning field incompatibility with OpenRouter/vLLM standards | None identified |
| **S2 — Degraded behavior** | #6002 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6002) | Messages not clearly addressed to assistant (Telegram + llama.cpp) | None identified |

### Research-Critical Stability Notes

- **#5808 + #7440**: The "skip futile trim" fix is a **band-aid**; the deeper issue is that tool definition token estimation appears unbounded. This resembles findings from LMSYS context compression research and suggests need for **progressive tool disclosure** or **semantic tool clustering**.
- **#6034**: Message loss in multi-turn dialogue is a **hallucination trigger** — when prior user turns vanish, model generates from partial context, producing confabulated continuity.

---

## 6. Feature Requests & Roadmap Signals

| Issue/PR | Link | Signal | Likelihood in Next Version |
|----------|------|--------|---------------------------|
| #7415 — Unify turn engines | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/7415) | **Major architectural RFC**; reduces reasoning path fragmentation | High — sponsored by core contributor, references prior audit requirements |
| #5937 — Unify providers architecture | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5937) | Refactor reqwest/client management for provider consistency | Medium-High — accepted, high risk label |
| #7248 — Persist cached input tokens for cost accounting | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/7248) | Prompt caching observability (Anthropic/OpenAI-compatible) | Medium — accepted, single comment |
| #7345 — Gate path-listing from vision routing | [Link](https://github.com/zeroclaw-labs/zeroclaw/pull/7345) | **Multimodal routing hygiene** | High — small PR, addresses clear bug |

### Predicted Research-Relevant Directions

1. **Dynamic context budgeting**: Given #5808's severity, expect schema changes to `agent.max_context_tokens` or adaptive tool inclusion.
2. **Reasoning token standardization**: #6584 suggests provider abstraction layer will need `reasoning`/`reasoning_content` dual-read logic.
3. **Memory retrieval weighting**: #5844 may drive configurable attention mechanisms or memory relevance scoring.

---

## 7. User Feedback Summary

### Explicit Pain Points (Research-Relevant)

| Source | Pain Point | Implication |
|--------|-----------|-------------|
| #5844 (databillm) | "System prompt should be altered... gives too much value/weight to the memories" | **Retrieval-augmented generation misalignment**: Retrieved context dominates over immediate task, causing goal drift |
| #5808 (JordanTheJet) | "Default 32k context budget is exceeded by system prompt + tool definitions on iteration 1" | **Capability-context mismatch**: Tool expansion outpaced context scaling |
| #6034 (lazy-hs) | "Single-turn and multi-turn dialogue loses user message" | **State management fragility**: Silent data loss in conversation history |
| #7438 context | Telegram prompt wording caused tool use failure on Qwen3 via LM Studio | **Prompt sensitivity for smaller models**: Alignment techniques that work on GPT-4 class models fail on distilled/quantized variants |

### Use Case Patterns

- **Cron/automation-heavy**: Multiple issues (#5844, #6037) reference cron jobs, indicating batch/long-running task reliability is a primary use case.
- **Multi-provider deployments**: Heavy use of "compatible" providers (LM Studio, OpenRouter, custom endpoints) exposes interoperability gaps.
- **Multi-channel**: Telegram, Discord, WhatsApp, WeChat, MQTT all active — routing logic complexity is high.

---

## 8. Backlog Watch

### Long-Unanswered Critical Items Needing Maintainer Attention

| Issue | Age | Last Update | Link | Risk of Staleness |
|-------|-----|-------------|------|-----------------|
| #5808 — Context budget overflow | ~55 days | 2026-06-09 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5808) | **High** — S1 severity, only symptomatic fix (#7440), no root cause PR |
| #5844 — Memory emphasis misalignment | ~54 days | 2026-06-09 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5844) | **High** — No fix PR, affects core reasoning reliability |
| #6034 — Message loss | ~48 days | 2026-06-09 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/6034) | **Critical** — S1, no identified fix, breaks basic dialogue |
| #4853 — Skills from `.well-known` URI | ~75 days | 2026-06-09 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/4853) | Medium — accepted but blocked on external standard |
| #5775 — Per-skill security permissions | ~56 days | 2026-06-09 | [Link](https://github.com/zeroclaw-labs/zeroclaw/issues/5775) | Medium — blocked, security-critical |

### Research-Specific Concerns

- **No dedicated tracking for hallucination metrics**: While #5844 and #7438 touch on hallucination-inducing conditions, there's no systematic issue for measuring or benchmarking hallucination rates.
- **Missing: Vision-language evaluation framework**: #7345 fixes a vision routing bug, but no issue requests end-to-end VLM capability testing or multimodal benchmark integration.
- **Missing: Long-context benchmark suite**: #5808's context crisis would benefit from standardized long-context stress tests (e.g., Needle-in-Haystack with tool-loaded system prompts).

---

*Digest generated from 50 issues and 50 PRs updated 2026-06-09 to 2026-06-10. Filtered for research relevance: vision-language capabilities, reasoning mechanisms, training/post-training methodologies, and hallucination-related issues. General product/commercial updates excluded per mandate.*

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*