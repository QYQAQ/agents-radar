# OpenClaw Ecosystem Digest 2026-07-02

> Issues: 290 | PRs: 500 | Projects covered: 13 | Generated: 2026-07-02 00:33 UTC

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

# OpenClaw Research-Relevant Digest — 2026-07-02

> **Scope filter:** vision-language capabilities, reasoning mechanisms, training methodologies, and hallucination / reliability issues. General product, commercial, channel-auth, and pure UI updates are omitted.

---

## 1. Today’s Overview

OpenClaw saw heavy activity in the last 24 hours: **290 issues** updated (174 open/active, 116 closed) and **500 PRs** updated (455 open, 45 merged/closed), with **no new releases**. The research-relevant signal is narrow but concentrated: the largest pain points are **Anthropic reasoning/thinking-block replay integrity**, **agent memory trust/poisoning**, **long-context tool-loop overflow**, and **multimodal context hygiene**. Most of the remaining traffic is integration, auth, and channel plumbing, so the research-relevant subset points to live reliability gaps in deployed reasoning and memory systems rather than new model-training work.

---

## 2. Releases

**None.** No new versions were published today.

---

## 3. Project Progress — Merged / Closed Today

Only a few PRs in the sample are closed/merged, and none directly advance core vision-language or reasoning research:

- **PR [#68936](https://github.com/openclaw/openclaw/pull/68936)** *(closed)* — Adds a PR-review autofix pipeline using the Claude Agent SDK subscription and a Windows daemon. Relevant to **automated alignment/repair workflows**, but it is tooling, not a model change.
- **PR [#98138](https://github.com/openclaw/openclaw/pull/98138)** *(closed)* — Defensive guard in `setDeep()` for Chrome profile decoration. Not research-relevant.

Notable **open** research-adjacent PRs that advanced toward review but did not merge:

- **PR [#98236](https://github.com/openclaw/openclaw/pull/98236)** — Flips session and transcript storage to SQLite, directly relevant to **long-context durability**.
- **PR [#86655](https://github.com/openclaw/openclaw/pull/86655)** — Proposes a first-class **Claude/Anthropic bridge harness** to achieve parity with the OpenAI/Codex path.
- **PR [#98679](https://github.com/openclaw/openclaw/pull/98679)** — Bounds MiniMax VLM API response reads to prevent OOM.

---

## 4. Community Hot Topics

| # | Item | Comments | Research angle |
|---|------|----------|----------------|
| **#92201** | [Embedded runner: Anthropic thinking signatures invalid on replay; recovery wrapper never fires](https://github.com/openclaw/openclaw/issues/92201) | 17 | Reasoning-block integrity / chain-of-thought replay |
| **#7707** | [Memory Trust Tagging by Source](https://github.com/openclaw/openclaw/issues/7707) | 13 | Hallucination / memory poisoning / provenance |
| **#45608** | [Pre-reset agentic memory flush](https://github.com/openclaw/openclaw/issues/45608) | 11 | Long-context / session memory preservation |
| **#94228** | [Native Anthropic path: replaying historical thinking blocks bricks long tool-use threads](https://github.com/openclaw/openclaw/issues/94228) | 10 | Reasoning / tool-use coherence |
| **#85103** | [Model fallback chain not triggered on quota exhaustion](https://github.com/openclaw/openclaw/issues/85103) | 10 | Reliability / cascading failure |

**Underlying needs:** The community is pushing for **trustworthy long-horizon reasoning** — signatures/thinking blocks must survive replay, memory must carry provenance, and sessions must not lose state on reset or model failover. The cluster of Anthropic thinking-block issues suggests the current serialization path is fragile for multi-turn tool reasoning.

---

## 5. Bugs & Stability — Research-Relevant Regressions & Failures

### P1 / Regression

- **#98672** — [Sessions breaking constantly](https://github.com/openclaw/openclaw/issues/98672) *(regression after 2026.6.11)*. Broad session failure; no fix PR identified yet.
- **#98528** — [Tool output returns empty after first call per turn](https://github.com/openclaw/openclaw/issues/98528) *(2026.6.11 regression)*. Breaks multi-step reasoning; no fix PR.
- **#98416** — [v2026.6.11 dist missing reentrancy guard — reply session initialization conflicted](https://github.com/openclaw/openclaw/issues/98416). Race condition in session startup.
- **#92201** / **#94228** — Anthropic thinking-block signature failures on replay; permanently breaks long tool-use threads.
- **#96857** — [Tool text outputs degrade to “(see attached image)” placeholders](https://github.com/openclaw/openclaw/issues/96857). The agent becomes “blind” to ordinary command output, a direct **hallucination/context-degradation** risk.
- **#93917** — [`genericRepeat` circuit-breaker never fires when exec results vary slightly](https://github.com/openclaw/openclaw/issues/93917). Tool-loop detection weakness.
- **#78562** — [Repeated tool-loop context overflows cause successive auto-compactions](https://github.com/openclaw/openclaw/issues/78562). Long-context thrashing.
- **#88362** — [WhatsApp inbound image fails on second read](https://github.com/openclaw/openclaw/issues/88362). Multimodal asset identity bug.

### Fix PRs in flight

- **PR [#98679](https://github.com/openclaw/openclaw/pull/98679)** — Bounds MiniMax VLM response reads.
- **PR [#76732](https://github.com/openclaw/openclaw/pull/76732)** — Prunes stale history images when current turn has fresh attachments to prevent multimodal context contamination.
- **PR [#98788](https://github.com/openclaw/openclaw/pull/

---

## Cross-Ecosystem Comparison

**Cross-Project Comparison Report — Personal AI Agent Ecosystem**
*As of 2026-07-02*

---

## 1. Ecosystem Overview

The open-source personal AI assistant / agent ecosystem is currently focused on **orchestration, reliability, and production hardening** rather than on new base-model training or multimodal reasoning breakthroughs. Most active projects are gateway or agent-framework layers that sit between end-users and commercial LLM/VLM providers, which means their research-relevant work concentrates on **long-context management, memory provenance, tool-use safety, reasoning replay integrity, and graceful model fallback**. High activity does not always translate to stability: the largest project by volume is also the most visibly stressed by regressions, while smaller projects are prioritizing test coverage, sandboxing, and security.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Releases (24h) | Health Score* |
|---|---|---|---|---|
| **OpenClaw** | 290 (174 open/active, 116 closed) | 500 (455 open, 45 merged/closed) | None | **3.0 / 5** — High velocity, strained stability |
| **NanoBot** | 8 (5 open, 3 closed) | 47 (25 open, 22 closed/merged) | None | **4.0 / 5** — Active and maturing |
| **PicoClaw** | 2 active | 11 updated | **nightly v0.3.1-nightly.20260701** | **3.5 / 5** — Stable, smaller scale |
| **NanoClaw** | 6 active | 12 touched (6 closed/merged, 6 open) | None | **2.5 / 5** — Stabilization phase |
| **NullClaw** | 1 | 0 | None | **1.5 / 5** — Dormant |
| **Hermes Agent** | N/A | N/A | N/A | **N/A** — summary unavailable |
| **IronClaw** | N/A | N/A | N/A | **N/A** — summary unavailable |
| **LobsterAI** | N/A | N/A | N/A | **N/A** — summary unavailable |
| **CoPaw** | N/A | N/A | N/A | **N/A** — summary unavailable |
| **ZeroClaw** | N/A | N/A | N/A | **N/A** — summary unavailable |
| **TinyClaw** | 0 | 0 | None | **1.0 / 5** — No activity |
| **Moltis** | 0 | 0 | None | **1.0 / 5** — No activity |
| **ZeptoClaw** | 0 | 0 | None | **1.0 / 5** — No activity |

\*Health score is a qualitative balance of 24-hour activity volume, merge/close rate, and the severity of open stability/security regressions.

---

## 3. OpenClaw’s Position

**Scale:** OpenClaw operates at an order of magnitude more activity than any peer in this snapshot (290 issues and 500 PRs in 24 hours). Its community and integration surface are clearly the largest.

**Advantages:**
- Broadest provider and channel coverage, including a new **Anthropic bridge harness** and deep work on **multimodal context hygiene**.
- Most explicit attention to **reasoning-block integrity** (Anthropic thinking/thought signatures) and **long-context tool loops**.
- The only project in this set directly tackling **agent memory trust/poisoning** through provenance tagging.

**Risks vs. peers:**
- The same scale is generating severe instability: **P1 regressions** in sessions, empty tool outputs, broken thinking-block replay, and context-overflow thrashing.
- By contrast, **NanoBot** and **PicoClaw** are smaller but landing security, sandbox, and correctness fixes with less visible chaos.

**Technical approach:** OpenClaw is a broad, multi-channel assistant stack that is migrating core storage to SQLite and normalizing provider-specific reasoning formats. Peers are more modular: NanoBot emphasizes deterministic runner/test harnesses, PicoClaw focuses on gateway/routing, and NanoClaw uses a skill-based architecture.

---

## 4. Shared Technical Focus Areas

| Requirement | Projects | Specific Needs |
|---|---|---|
| **Long-context durability / pruning** | OpenClaw, NanoBot, NanoClaw | SQLite session storage; prune stale history images; low-value payload pruning; semantic conversation search |
| **Memory provenance & trust** | OpenClaw, NanoBot | Source tagging for memories to prevent poisoning/hallucination; archived memory gates |
| **Reasoning replay integrity** | OpenClaw | Anthropic thinking-block signatures must survive replay; tool threads must not break on historical reasoning blocks |
| **Tool-use grounding & safety** | OpenClaw, NanoBot, PicoClaw | `edit_file` line-hint disambiguation; tool output not degraded to placeholders; sandbox deny-pattern enforcement; recover leaked XML tool calls |
| **Tool-loop detection** | OpenClaw | Circuit-breakers when exec results vary; auto-compaction from overflow |
| **Model fallback / provider portability** | OpenClaw, PicoClaw, NanoClaw | Configurable fallback chains; Anthropic bridge parity; custom API endpoints |
| **Session reset / memory preservation** | OpenClaw, NanoBot | Pre-reset memory flush; preserve delivery context during consolidation |
| **Sandbox / execution boundary** | NanoBot, PicoClaw | Relative symlink escape fixes; deny-pattern enforcement; blocked finish reasons |

---

## 5. Differentiation Analysis

| Project | Primary Focus | Target User / Use Case | Architectural Difference |
|---|---|---|---|
| **OpenClaw** | General-purpose personal assistant with wide channel/provider integration | End-users and bot operators needing a multi-modal, multi-provider agent | Monolithic, storage moving to SQLite; heavy provider-specific normalization |
| **NanoBot** | Research-grade agent runner with memory lifecycle and safety boundaries | Developers and researchers building reproducible agent experiments | Modular runner + test harnesses; explicit memory consolidation pipeline |
| **PicoClaw** | Gateway for multi-channel bots with model fallback | Multi-channel bot deployers (Telegram, QQ, WebSocket) | Gateway/routing-centric with channel capability abstractions |
| **NanoClaw** | Skill-based assistant with retrieval and audio input | Users wanting modular skills (search, voice) | Skill plugin architecture; semantic conversation-search skill |
| **NullClaw / TinyClaw / Moltis / ZeptoClaw** | Niche or dormant | Not clear from current data | Minimal or no recent activity |
| **Hermes / Iron / Lobster / CoPaw / ZeroClaw** | Unknown for this period | Cannot assess | Summary generation failed |

---

## 6. Community Momentum & Maturity

- **Tier 1 — High-velocity, high-stress:** **OpenClaw**. The community is iterating rapidly, but the bug load is dominated by regressions that break reasoning, sessions, and tools.
- **Tier 2 — Active and hardening:** **NanoBot** and **PicoClaw**. Both show consistent merges, security fixes, and regression tests. Maturity is improving without the instability of the largest project.
- **Tier 3 — Stabilizing with lighter activity:** **NanoClaw**. A few skills landed (semantic search), but the day is marked by gateway/webhook reliability fires rather than feature expansion.
- **Tier 4 — Dormant / minimal:** **NullClaw**, **TinyClaw**, **Moltis**, **ZeptoClaw**. No meaningful research-relevant activity or none at all.
- **Tier 5 — Unknown:** **Hermes Agent**, **IronClaw**, **LobsterAI**, **CoPaw**, **ZeroClaw**. Digest generation failed, so momentum cannot be scored.

---

## 7. Trend Signals

1. **Reliability is the new capability.** The dominant community energy is on making existing agents not hallucinate, break, or lose state — not on adding new model capabilities.
2. **Long-context economics matter.** Multiple projects are pruning low-value payloads, compacting tool loops, and moving session storage to durable backends.
3. **Memory provenance is becoming a first-class concern.** Source tagging and archival gating are being proposed to prevent memory poisoning and hallucination drift.
4. **Tool-use needs finer grounding.** Disambiguation hints, line-number guards, and structured extraction fixes show that “calling a tool” is not enough; *which* occurrence is modified matters.
5. **Reasoning transparency is fragile.** Anthropic thinking-block replay issues indicate that chain-of-thought serialization remains brittle across multi-turn tool use.
6. **Provider portability and failover are production requirements.** Fallback chains and provider bridges are being treated as operational must-haves, not nice-to-haves.
7. **Edge/mobile deployment is a pain point.** Termux/Android build and gateway crashes are recurring, signaling demand for lighter, more portable agent runtimes.

**Value for AI agent developers:** The strongest ROI right now is in **deterministic replay**, **memory provenance**, **context pruning**, **sandbox hardening**, and **fallback orchestration** — the infrastructure that turns a demo agent into a reliable product.

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

**NanoBot Research Digest — 2026-07-02**

*Filter applied: vision-language capabilities, reasoning mechanisms, training methodologies, and hallucination-related issues. Commercial/product items (e.g., OAuth, IM-channel formatting) are de-emphasized.*

---

## 1. Today’s Overview

NanoBot saw high activity in the last 24 hours: **8 updated issues** (5 open, 3 closed) and **47 updated PRs** (25 open, 22 closed/merged), with **no new releases**. The research-relevant signal is concentrated on **agent reliability, long-context management, memory consolidation, and tool-use grounding** rather than new multimodal or training features. Several security and stability fixes landed, while open work is pushing on context pruning, memory provenance, and `edit_file` disambiguation. Overall project health appears active and maturing, but the volume of security and correctness PRs suggests the codebase is still hardening its agent execution boundary.

---

## 2. Releases

**No new releases** today.

---

## 3. Project Progress

### Closed / merged PRs (research-relevant)

- **#3982** — `test: add scripted agent runner harness`  
  https://github.com/HKUDS/nanobot/pull/3982  
  Adds a reusable test harness that captures the exact provider transcript (tool call → tool result → final response → usage). This directly supports reproducible research on reasoning loops and tool-use behavior.

- **#3983** — `test: cover runner blocked tool-call finish reasons`  
  https://github.com/HKUDS/nanobot/pull/3983  
  Adds regression tests ensuring `refusal`, `content_filter`, and `error` finish reasons do **not** dispatch tools or append tool messages, improving alignment and safety.

- **#4119** — `fix(exec): block relative symlink workspace escapes`  
  https://github.com/HKUDS/nanobot/pull/4119  
  Prevents sandboxed `exec` commands from escaping the workspace via relative symlinks, tightening the agent execution boundary.

- **#4193** — `test: add memory lifecycle harness`  
  https://github.com/HKUDS/nanobot/pull/4193  
  Adds an end-to-end memory test harness covering session → consolidation → `history.jsonl` → GitStore, useful for studying memory drift and hallucination propagation.

### Closed issues

- **#4615** — Gateway crash when `CronService` calls `fsync()` on parent directory  
  https://github.com/HKUDS/nanobot/issues/4615  
  Startup crash resolved.

- **#4434** — MCP `enabledTools` deny-all policy bypass exposes resources/prompts to the model  
  https://github.com/HKUDS/nanobot/issues/4434  
  Security fix: an empty allowlist no longer leaks MCP resources/prompts.

- **#4490** — OpenAI-compatible API now requires auth when bound to all interfaces  
  https://github.com/HKUDS/nanobot/issues/4490  
  Brings API server safety parity with the WebSocket gateway.

---

## 4. Community Hot Topics

Most active items by comment count (with research implications):

- **#4604** — Anthropic OAuth support request (3 comments)  
  https://github.com/HKUDS/nanobot/issues/4604  
  *Research note:* While primarily an integration ask, it signals demand for broader model-provider diversity, which affects reproducibility of reasoning experiments across backends.

- **#4615** — CronService gateway crash (2 comments)  
  https://github.com/HKUDS/nanobot/issues/4615  
  Underlying need: reliable headless agent deployment.

- **#4434** — MCP `enabledTools` bypass (2 comments)  
  https://github.com/HKUDS/nanobot/issues/4434  
  Underlying need: strict, trustworthy tool-access boundaries to prevent model exposure to unauthorized resources.

- **#4634** — `edit_file` target disambiguation dominates exact-edit benchmark failures (0 comments but high correctness impact)  
  https://github.com/HKUDS/nanobot/issues/4634  
  Underlying need: better tool grounding so model-selected edits modify the intended occurrence, not just a syntactically matching one.

- **#4581** — Prune low-value context payloads (open PR)  
  https://github.com/HKUDS/nanobot/pull/4581  
  Underlying need: keep long-context agent runs within token/attention budgets without losing task-relevant history.

---

## 5. Bugs & Stability

| Severity | Item | Status | Notes |
|---|---|---|---|
| **High** | **#4615** CronService `fsync()` crash | Closed | Gateway startup failure; no fix PR visible in today’s data but issue is closed. |
| **High** | **#4434** MCP `enabledTools` deny-all bypass | Closed | Security flaw exposing MCP resources/prompts; fix landed. |
| **High** | **#4629** Relative symlink workspace escapes | Open PR | https://github.com/HKUDS/nanobot/pull/4629 — active fix with regression tests. |
| **Medium** | **#4634** `edit_file` wrong-occurrence failures | Open issue + open fix PR | https://github.com/HKUDS/nanobot/issues/4634 ; fix in **#4635** https://github.com/HKUDS/nanobot/pull/4635 adds `line_hint`, `target_line`, and `target_start_line` guards. |
| **Medium** | **#4630** Blocked tool-call finish reasons | Open PR | https://github.com/HKUDS/nanobot/pull/4630 — prevents unsafe execution on refusal/content-filter/error responses. |
| **Medium** | **#4627** Preserve delivery context during consolidation | Open PR | https://github.com/HKUDS/nanobot/pull/4627 — avoids memory replay cutting off proactive delivery context. |
| **Low / product** | **#4637** Telegram long-message split rendering | Open | UI/UX issue; not research-relevant. |

---

## 6. Feature Requests & Roadmap Signals

Research-relevant requests and in-progress enhancements:

- **#4581** — Context pruning for low-value payloads  
  https://github.com/HKUDS/nanobot/pull/4581  
  *Likely near-term:* directly addresses long-context reasoning and cost.

- **#4621** — Gate archived memory facts with provenance context  
  https://github.com/HKUDS/nanobot/pull/4621  
  *Likely near-term:* introduces source-discipline rules to reduce hallucinated or ungrounded memory entries.

- **#4626** — Opt-in eager memory consolidation  
  https://github.com/HKUDS/nanobot/pull/4626  
  *Likely near-term:* related to #2604; enables earlier archival of conversation slices.

- **#4635** — `edit_file` line guards  
  https://github.com/HKUDS/nanobot/pull/4635  
  *Likely near-term:* pairs with #4634 to improve tool-use accuracy.

- **#4623** — Subagent spawn model override  
  https://github.com/HKUDS/nanobot/pull/4623  
  *Medium-term:* supports heterogeneous reasoning by routing subagent tasks to different models.

- **#4624** — Aggregated subagent result mode  
  https://github.com/HKUDS/nanobot/pull/4624

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-07-02

**Repository:** [sipeed/picoclaw](https://github.com/sipeed/picoclaw)  
**Period:** Last 24 hours (2026-07-01 → 2026-07-02)

---

## 1. Today's Overview

PicoClaw saw moderate activity over the past 24 hours: **2 active issues** and **11 pull requests** were updated, alongside a new nightly release. The activity is heavily weighted toward stability, security, and API-compatibility fixes rather than core model capability work. Notably, **no items directly address vision-language models, reasoning mechanisms, training methodologies, or hallucination mitigation** in this batch. The strongest research-relevant signals are in **tool-call extraction reliability** ([#3165](https://github.com/sipeed/picoclaw/pull/3165)), **model fallback/routing configuration** ([#3200](https://github.com/sipeed/picoclaw/pull/3200)), and **gateway lifecycle correctness** ([#3116](https://github.com/sipeed/picoclaw/pull/3116)). Overall project health appears stable, with an active cleanup of stale PRs and several security-hardening patches.

---

## 2. Releases

- **nightly: `v0.3.1-nightly.20260701.2cf030d2`**  
  - Automated nightly build; flagged as potentially unstable.  
  - Full changelog: [v0.3.1...main](https://github.com/sipeed/picoclaw/compare/v0.3.1...main)  
  - **No breaking changes or migration notes were supplied in the release metadata.**  
  - **Research relevance:** Low — this is an automated CI artifact, not a stable release with documented model/reasoning changes.

---

## 3. Project Progress

### Merged / Closed Today

- **PR #3116** — [fix(pico): complete `turn.done` lifecycle signaling](https://github.com/sipeed/picoclaw/pull/3116)  
  - Closes [#2984](https://github.com/sipeed/picoclaw/issues/2984). Fixes three gaps in the Pico `turn.done` lifecycle: preserves `request_id` for queued steering/follow-up messages, and ensures every inbound Pico request receives the signal.  
  - **Research relevance:** Medium — improves deterministic conversation state management and end-of-turn signaling, which affects multi-turn reasoning and tool-use orchestration.

- **PR #2975** — [feat(telegram): treat reply to bot message as mention in group chats](https://github.com/sipeed/picoclaw/pull/2975)  
  - When `mention_only: true` is configured, replying to a bot message now triggers the bot as if it were an `@mention`.  
  - **Research relevance:** Low — interaction UX change.

### Notable Open Progress

- **PR #3200** — [feat(models): add configurable default fallback chain](https://github.com/sipeed/picoclaw/pull/3200)  
  - Adds a UI workflow to set a default model, add fallback models, reorder the chain, and persist it via the backend API.  
  - **Research relevance:** Medium — directly impacts deployment reliability and graceful degradation for LLM inference.

- **PR #3165** — [fix(openai_compat): recover Seed XML tool calls](https://github.com/sipeed/picoclaw/pull/3165)  
  - Recovers Volcengine Doubao Seed `<seed:tool_call>` XML blocks from OpenAI-compatible responses and strips them from user-visible/streaming output.  
  - **Research relevance:** Medium-High — addresses tool-call leakage and structured-output extraction from provider-specific formats, reducing malformed tool-use traces and potential hallucination-like behavior from leaked XML.

- **PR #3202** — [fix(routing): strip leading/trailing underscores in ID normalization](https://github.com/sipeed/picoclaw/pull/3202)  
  - Corrects `NormalizeAgentID` / `NormalizeAccountID` regex compliance (`^[a-z0-9][a-z0-9_-]{0,63}$`).  
  - **Research relevance:** Low — routing correctness.

---

## 4. Community Hot Topics

| Item | Link | Engagement | Underlying Need |
|---|---|---|---|
| **Issue #3164** — Process hooks crash gateway on Android/Termux | [#3164](https://github.com/sipeed/picoclaw/issues/3164) | 1 comment | **Deployment reliability on mobile/edge environments** — users are trying to run the gateway on constrained Android/Termux hosts and need stable JSON-RPC stdio hook support. |
| **Issue #3201** — Support streaming output for QQ channel | [#3201](https://github.com/sipeed/picoclaw/issues/3201) | 0 comments | **Real-time user experience parity** — QQ is missing the streaming capability already implemented for Telegram and Pico WebSocket. |
| **PR #3200** — Configurable default fallback chain | [#3200](https://github.com/sipeed/picoclaw/pull/3200) | 0 comments | **Operational resilience** — users need visible, persistent model fallback chains to survive provider/model outages. |

**Analysis:** The highest-engagement item is the Android/Termux crash, which suggests an active edge-deployment community. Streaming and fallback-chain requests indicate users are pushing the gateway toward production use where latency and uptime matter.

---

## 5. Bugs & Stability

Ranked by severity:

1. **High — Issue #3164**: [Process hooks crash gateway on Android/Termux (v0.2.9, config v3)](https://github.com/sipeed/picoclaw/issues/3164)  
   - Minimal "hello world" JSON-RPC hook causes gateway death within 2 seconds of startup.  
   - **No fix PR is currently linked.**  
   - **Research relevance:** Low — infrastructure crash.

2. **High — PR #3161**: [fix(exec): keep deny patterns active for custom allow rules](https://github.com/sipeed/picoclaw/pull/3161)  
   - Fixes a sandbox escape where `custom_allow_patterns` skipped `deny-pattern` enforcement, allowing `jq` payloads to read process environment variables.  
   - **Research relevance:** Medium — improves tool-execution safety when LLM agents invoke shell utilities.

3. **Medium-High — PR #3160**: [fix(auth): reject cross-site launcher setup requests](https://github.com/sipeed/picoclaw/pull/3160)  
   - Adds `Sec-Fetch-Site`, `Origin`, and `Referer` checks to `POST /api/auth/setup` to prevent cross-site password-store mutation.  
   - **Research relevance:** Low — security hardening.

4. **Low — PR #3158**: [test: cover sandbox fs Windows path handling](https://github.com/sipeed/picoclaw/pull/3158)  
   - Adds regression tests for `sandboxFs.ReadDir` / `sandboxFs.Open` using `filepath.Join`-generated paths on Windows.  
   - **Research relevance:** Low — platform correctness.

---

## 6. Feature Requests & Roadmap Signals

- **Issue #3201**: [Support streaming output for QQ channel](https://github.com/sipeed/picoclaw/issues/3201)  
  - Likely to be implemented soon, given that Telegram and Pico WebSocket already support `StreamingCapable`. Low complexity, high user value.

- **PR #3200**: [Configurable default fallback chain](https://github.com/sipeed/picoclaw/pull/3200)  
  - Fills a clear operational gap in the web UI. Strong candidate for next minor release.

- **PR #3165**: [Recover Seed XML tool calls](https://github.com/sipeed/picoclaw/pull/3165)  
  - Indicates ongoing provider-compatibility work; likely needed for users depending on Doubao/Seed models via OpenAI-compatible endpoints.

- **PR #2975** (closed): [Telegram reply-as-mention](https://github.com/sipeed/picoclaw/pull/2975)  
  - Suggests continued investment in multi-channel chat UX.

**No signals observed** for vision-language capabilities, chain-of-thought reasoning, RLHF/alignment training, or explicit hallucination-reduction features.

---

## 7. User Feedback Summary

**Real pain points:**
- **Edge deployment instability:** Android/Termux crashes block mobile/low-resource use.
- **Incomplete streaming parity:** QQ users wait for full responses while Telegram/WebSocket users get token-by-token output.
- **Model failover opacity:** Need for UI-driven fallback chains shows users currently manage failover manually or outside the gateway.

**Use cases emerging:**
- Mobile/Termux bot hosting.
- Multi-channel LLM bots (Telegram, QQ, WebSocket).
- Multi-model production deployments requiring fallback resilience.

**Satisfaction signals:**
- Active maintenance of stale PRs and security patches indicates a healthy review cycle.
- No recent regressions beyond the isolated Android/Termux report.

---

## 8. Backlog Watch

The following stale PRs and issues remain open and may need maintainer attention:

- **PR #3165** — [Recover Seed XML tool calls](https://github.com/sipeed/picoclaw/pull/3165) (stale, 0 comments) — provider compatibility fix, likely needed by Doubao users.
- **PR #3161** — [Exec deny-pattern enforcement](https://github.com/sipeed/picoclaw/pull/3161) (stale, 0 comments) — security fix, should be prioritized.
- **PR #3160** — [Cross-site auth setup rejection](https://github.com/sipeed/picoclaw/pull/3160) (stale, 0 comments) — security hardening.
- **PR #3158** — [Sandbox fs Windows path tests](https://github.com/sipeed/picoclaw/pull/3158) (stale, 0 comments) — test coverage.
- **Issue #3164** — [Android/Termux gateway crash](https://github.com/sipeed/picoclaw/issues/3164) (stale, 1 comment) — awaiting investigation or fix.
- **Dependency PRs** — [#3104](https://github.com/sipeed/picoclaw/pull/3104), [#3103](https://github.com/sipeed/picoclaw/pull/3103), [#3100](https://github.com/sipeed/picoclaw/pull/3100) (stale, dependabot).

**Research-relevant backlog:** None of the stale items address core model reasoning, vision-language, or hallucination research. The closest is **PR #3165**, which improves tool-call extraction reliability for OpenAI-compatible providers.

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

**NanoClaw Project Digest — 2026-07-02**  
*Research filter applied: vision-language capabilities, reasoning mechanisms, training methodologies, hallucination/AI reliability.*

---

### 1. Today’s Overview

NanoClaw had **6 active issues** and **12 PRs** touched in the last 24 hours (6 closed/merged, 6 open), with **no new release**. For the research-relevant lens, the day is light on core model updates: there are no direct changes to vision-language models, reasoning algorithms, training pipelines, or hallucination mitigation. The strongest signals are an open voice-transcription skill (multimodal audio input) and a recently closed semantic conversation-search skill (retrieval / long-context memory). At the same time, several critical reliability issues surfaced around gateway networking and webhook failures, suggesting the project is in a stabilization-focused phase.

---

### 2. Releases

None today.

---

### 3. Project Progress (Research-Relevant)

- **Closed / merged**  
  - [`nanocoai/nanoclaw#1597`](https://github.com/nanocoai/nanoclaw/pull/1597) — feat(skills): add QMD skill for semantic conversation search. Adds semantic retrieval over conversation history, directly relevant to **long-context understanding** and memory-augmented generation.  
  - [`nanocoai/nanoclaw#1257`](https://github.com/nanocoai/nanoclaw/pull/1257) — support custom API endpoints (e.g., z.ai). Not a training/reasoning update,

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw Project Digest — 2026-07-02

## Research-Relevant Filter Applied
- **Focus areas:** vision-language capabilities, reasoning mechanisms, training methodologies, hallucination-related issues.
- **Result:** No issues, PRs, or releases in the last 24 hours matched these research-relevant categories. The only activity is a build/compilation bug on Android/Termux.

---

## 1. Today's Overview
Activity in the `nullclaw/nullclaw` repository over the last 24 hours was very low. Only one issue was updated, and there were no new PRs, merges, or releases. The single active issue is a build-environment regression on Android/Termux (aarch64). From a research standpoint, there were no updates touching multimodal reasoning, long-context understanding, post-training alignment, or AI reliability/hallucination. Overall project health appears stable but dormant on the research front.

---

## 2. Releases
- **None.**  
  No new releases were published in the last 24 hours.

---

## 3. Project Progress
- **No PRs merged or closed today.**  
- No code changes, feature advances, or fixes were recorded in the 24-hour window.

---

## 4. Community Hot Topics
The only active discussion is:

- **Issue #868 — [bug] zig build fails on Android/Termux (aarch64) with AccessDenied on options.zig linkat**  
  - **Status:** Open  
  - **Author:** NOTJuangamer10  
  - **Created:** 2026-04-23 | **Updated:** 2026-07-01  
  - **Comments:** 6 | **Reactions:** 0  
  - **Link:** [https://github.com/nullclaw/nullclaw/issues/868](https://github.com/nullclaw/nullclaw/issues/868)

**Underlying need:** Users are trying to build NullClaw natively on constrained mobile/Termux environments. The reported `linkat` / `AccessDenied` failure points to filesystem/linking constraints on Android's FUSE or Termux storage, not a logic bug in the core system. The community signal is broader build-system portability rather than a research capability gap.

---

## 5. Bugs & Stability
| Severity | Item | Status | Notes |
|----------|------|--------|-------|
| Medium | **Issue #868** — `zig build` fails on Android/Termux aarch64 with `AccessDenied` on `options.zig linkat` | Open | Build regression affecting mobile/Termux users. No fix PR linked yet. |

**Research-relevant bugs/crashes:** None observed today.

---

## 6. Feature Requests & Roadmap Signals
- **None in the last 24 hours.**  
- No vision-language, reasoning, training, or hallucination-related feature requests appeared in the current window.

---

## 7. User Feedback Summary
- **Real pain point:** Native compilation on Android/Termux is unreliable, blocking users on aarch64 mobile devices.
- **Use case:** Running or developing NullClaw on low-resource/mobile environments.
- **Satisfaction/dissatisfaction:** Neutral-to-negative for this segment; the issue has persisted since April 2026 with ongoing discussion but no merged resolution.

---

## 8. Backlog Watch
- **Issue #868** — Build failure on Android/Termux aarch64.  
  - **Link:** [https://github.com/nullclaw/nullclaw/issues/868](https://github.com/nullclaw/nullclaw/issues/868)  
  - **Watch reason:** Open since 2026-04-23, recently active (2026-07-01), and has 6 comments. It may need maintainer attention to determine whether the fix belongs in NullClaw's build scripts, upstream Zig, or Termux packaging.  

---

**Note:** This digest is filtered for research-relevant topics. If you would like a broader digest covering all community, product, or commercial updates, let me know.

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

⚠️ Summary generation failed.

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

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

⚠️ Summary generation failed.

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*