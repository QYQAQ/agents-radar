# OpenClaw Ecosystem Digest 2026-07-10

> Issues: 500 | PRs: 500 | Projects covered: 13 | Generated: 2026-07-10 00:29 UTC

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

⚠️ Summary generation failed.

---

## Cross-Ecosystem Comparison

# Cross-Project Analysis: Personal AI Agent / Assistant Ecosystem — 2026-07-10

## 1. Ecosystem Overview

The open-source personal AI assistant / agent landscape is highly fragmented, with a handful of high-velocity runtimes (NanoBot, Hermes Agent, ZeroClaw) and many smaller, channel-specific or thin-wrapper projects (PicoClaw, NanoClaw, Moltis, LobsterAI). Most projects are not training new models or advancing post-training alignment science; instead, the 2026-07-10 window shows engineering effort concentrated on **runtime reliability, tool-use grounding, sandbox isolation, multimodal I/O hygiene, and long-context efficiency**. Release cadence is low across the board—no project in the sample published a new release today—while issue and PR velocity remains high, indicating the ecosystem is in a stabilization and hardening phase rather than a feature-expansion phase.

---

## 2. Activity Comparison

| Project | Issues (24h) | PRs (24h) | Merged / Closed PRs | Releases | Health Score* |
|---|---|---|---|---|---|
| **OpenClaw** (core reference) | N/A | N/A | N/A | N/A | N/A |
| **NanoBot** | 23 updated (12 open/active, 11 closed) | 22 updated (17 open, 5 merged/closed) | 5 | 0 | 6.5 / 10 |
| **Hermes Agent** | 50 updated | 50 updated | Unknown | 0 | 7.0 / 10 |
| **PicoClaw** | 3 active | 16 updated | 4 | 0 | 7.0 / 10 |
| **NanoClaw** | 9 open/active | 14 open | 3 | 0 | 6.0 / 10 |
| **LobsterAI** | 5 updated | 14 updated | 11 | 0 | 7.5 / 10 |
| **ZeroClaw** | 32 updated (23 open/active, 9 closed) | 50 updated (46 open, 4 merged/closed) | 4 | 0 | 6.5 / 10 |
| **Moltis** | 0 | 1 open | 0 | 0 | 4.0 / 10 |
| **NullClaw** | 0 | 0 | 0 | 0 | 3.0 / 10 |
| **TinyClaw** | 0 | 0 | 0 | 0 | 3.0 / 10 |
| **ZeptoClaw** | 0 | 0 | 0 | 0 | 3.0 / 10 |
| **IronClaw** | Summary failed | Summary failed | Unknown | Unknown | N/A |
| **CoPaw** | Summary failed | Summary failed | Unknown | Unknown | N/A |

\*Health score is a 24-hour snapshot estimate based on issue/PR velocity, merge throughput, and unresolved critical severity. It is not a long-term maturity rating.

---

## 3. OpenClaw's Position

**Advantages vs. peers**
- **Ecosystem anchor:** OpenClaw is treated as the reference runtime by downstream projects (e.g., LobsterAI explicitly sends prompts, tools, and memory configs through an “OpenClaw gateway”).
- **Reference architecture:** It defines shared abstractions—memory dreaming, managed cron jobs, subagent delegation, and tool-history reconciliation—that other projects import or emulate.
- **Broader scope:** Compared to channel-specific bots, OpenClaw appears to sit at the agent-runtime layer, making it a general-purpose substrate rather than a chat-app integration.

**Technical approach differences**
- OpenClaw is positioned as a **backend agent runtime** with persistent memory, tool delegation, and long-context management, whereas NanoBot, PicoClaw, and NanoClaw are **integration-heavy wrappers** around Telegram, Matrix, WhatsApp, LINE, QQ, etc.
- Its design exposes lower-level primitives (dream jobs, subagent history, continuity capsules), while peers optimize for user-facing UX polish and adapter reliability.

**Community size comparison**
- Quantitative community data is unavailable today (summary generation failed), but indirect evidence is significant: LobsterAI’s Cowork product depends on OpenClaw, and several projects reference OpenClaw gateway compatibility. This suggests a larger downstream ecosystem than most active peers, even if direct contribution velocity cannot be measured in this window.

---

## 4. Shared Technical Focus Areas

| Focus Area | Why it matters | Projects with concrete evidence |
|---|---|---|
| **Tool-use hallucination & grounding** | Users abandon agents that invent `exec` calls or drop malformed tool batches. | NanoBot (#937 exec hallucinations), PicoClaw (#3180 invalid JSON batch handling), NanoClaw (#2998 hidden MCP args), ZeroClaw (small-model prompt leakage) |
| **Sandboxing & isolation** | Legitimate media workflows conflict with strict security boundaries; escapes break trust. | NanoBot (#4629 symlink escape, #940 filesystem access, #931 SandboxDriver proposal), PicoClaw (#3226 overwrite coaching removal), NanoClaw (#2993 container-runtime degradation), ZeroClaw |
| **Long-context efficiency** | Caching, context metering, and message-loss bugs are becoming first-class concerns. | Hermes (GLM long-context overflow fix), PicoClaw (#3163 Bedrock prompt caching), ZeroClaw (message-loss bug), Moltis (#1146 GPT-5.6 context-window bookkeeping), NanoBot (#990 zero-token routing) |
| **Multimodal / vision-language I/O boundaries** | Images, data-URLs, attachments, and markdown are fragile across adapters. | NanoBot (#4859 mxc:// image URL rewriting), PicoClaw (#3115 base64 data-URL misclassification), NanoClaw (#2618 image/voice/PDF restoration), LobsterAI (#2300 steer-queue attachments, #2303 image/video tools) |
| **Reasoning & delegation control** | Sustained goals, subagent loops, and tool-history sync need explicit termination and traceability. | NanoBot (#4844 goal gating, #4864 endless loop, #4522/#4645 repeated-call guards), ZeroClaw (goal/delegation tools), LobsterAI (#2299 subagent tool-history sync) |
| **Observability, audit, and conversation reuse** | Developers and users need transparent tool traces, search, and export. | NanoBot (#954 streaming leaks), NanoClaw (#2987 audit logs, #2981 task control plane), LobsterAI (#1343 full-text search, #1345 Markdown export) |
| **Model-provider abstraction & task routing** | Different tasks (chat, tool-use, browser) need different models and context windows. | NanoBot (#912 task-specific models, #1267 provider config), Moltis (#1146 GPT-5.6 catalog), Hermes (reasoning-effort controls) |

---

## 5. Differentiation Analysis

| Project | Primary target / use case | Architecture emphasis | Standout differentiator |
|---|---|---|---|
| **OpenClaw** | General-purpose agent runtime / reference backend |

---

## Peer Project Reports

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot Project Digest — 2026-07-10

**Project:** HKUDS/nanobot  
**Analysis lens:** multimodal reasoning, long-context understanding, post-training alignment, AI reliability  
**Data window:** Issues/PRs updated 2026-07-09

---

## 1. Today's Overview

NanoBot saw high activity in the last 24 hours with **23 issues updated** (12 open/active, 11 closed) and **22 pull requests updated** (17 open, 5 merged/closed), but **no new releases**. The project remains focused on its AI-agent runtime rather than model training, so today's research-relevant signal is concentrated in **agent reliability, tool-use hallucination, repeated-tool-call loops, sandbox isolation, and vision-language I/O edge cases**. A notable closed report explicitly flags **hallucinations in the `exec` tool** as a blocker, while several open PRs are hardening tool-execution safety and goal-loop termination. There is little direct activity on model training, post-training alignment, or long-context modeling.

---

## 2. Releases

No new releases were published today.

---

## 3. Project Progress

Merged/closed PRs today (research-relevant items highlighted):

- **PR #4859 — `fix(matrix): preserve mxc markdown image sources`**  
  *Merged/closed.* Fixes a regression where `mistune==3.3.3` rewrote Matrix `mxc://` image URLs to `#harmful-link`, breaking vision-rich message rendering. Keeps the existing `nh3` sanitization policy for non-MXC sources.  
  https://github.com/HKUDS/nanobot/pull/4859

- **PR #4629 — `fix(exec): block relative symlink workspace escapes`**  
  *Merged/closed.* Prevents restricted `exec` commands from following relative-path symlinks outside the workspace. Adds regression coverage for `cat link.txt` style escapes. Important for **sandbox isolation and tool-use safety**.  
  https://github.com/HKUDS/nanobot/pull/4629

- **PR #4857 — `Add Dockerfile arg to override optional Python dependencies`**  
  *Closed.* Adds a `NANOBOT_EXTRAS` build argument to the Dockerfile. Infrastructure-only; less relevant to research priorities.  
  https://github.com/HKUDS/nanobot/pull/4857

Open but active research-relevant PRs that advanced:

- **PR #4862 — `fix(exec): isolate exec session managers`**  
  Gives each `AgentLoop` and `SubagentManager` its own `ExecSessionManager`, scoping session listings and writes to the current request.  
  https://github.com/HKUDS/nanobot/pull/4862

- **PR #4844 — `Gate sustained goals behind explicit runtime mode`**  
  Replaces always-visible `long_task`/`complete_goal` with runtime-gated `create_goal`/`update_goal`, moving long-goal guidance into per-run prompt templates.  
  https://github.com/HKUDS/nanobot/pull/4844

- **PR #4645 / #4522 — Repeated-tool-result/call guards**  
  Add model-facing hints after repeated tool results and a generic guard against repeated identical tool calls to prevent infinite loops.  
  https://github.com/HKUDS/nanobot/pull/4645  
  https://github.com/HKUDS/nanobot/pull/4522

---

## 4. Community Hot Topics

Most active items by comments/reactions, with research interpretation:

- **Issue #1267 — `zhipu provider does not work?`** (6 comments)  
  Provider configuration / API-key handling problem. Underlying need: **reliable model-provider abstraction**, a prerequisite for task-specific or multi-model routing.  
  https://github.com/HKUDS/nanobot/issues/1267

- **Issue #912 — `Feat: Support Task-Specific Model Configuration`** (5 comments, 3 👍)  
  Request to use different models for conversational, tool-use, and browser tasks. Directly relevant to **reasoning routing and model specialization**.  
  https://github.com/HKUDS/nanobot/issues/912

- **Issue #954 — `Progress streaming leaks internal tool calls to user chat`** (4 comments)  
  Streaming UI exposes raw tool calls (`exec()`, `read_file()`, etc.). Underlying need: **observability vs. user-facing abstraction**, important for agent reliability UX.  
  https://github.com/HKUDS/nanobot/issues/954

- **Issue #4823 — `whatsapp - groups` regression** (4 comments)  
  Channel-access control regression after v0.2.2. Operational reliability issue; less central to research priorities.

- **Issue #937 — `Too many hallucinations in using exec tool`** (3 comments)  
  User discontinued evaluation because the framework hallucinates `exec` tool usage. **Key hallucination signal** for tool-use reliability.  
  https://github.com/HKUDS/nanobot/issues/937

---

## 5. Bugs & Stability

Ranked by research-relevant severity:

| Severity | Item | Summary | Fix PR |
|---|---|---|---|
| **High** | **Issue #4864** — `Endless loop for <tool_call> <function=complete_goal>` | Gateway parses `recap` as a bare string instead of JSON, causing `complete_goal` to error in a loop. Clear **reasoning/tool-argument serialization bug**. | None yet |
| **High** | **PR #4840** — `fix(shell): reap zombie processes on all subprocess exit paths` | Hardens process cleanup to prevent zombie accumulation and `waitpid` races during shell tool execution. | Open |
| **High** | **Issue #937** — `Too many hallucinations in using exec tool` | User reports hallucinated `exec` invocations, causing loss of trust. Closed as stale but unresolved. | None |
| **Medium** | **PR #4862** — `fix(exec): isolate exec session managers` | Prevents cross-request session leakage and improves per-loop isolation. | Open |
| **Medium** | **PR #4816** — `fix(runner): narrow BaseException catch to Exception in tool execution` | Stops `KeyboardInterrupt`, `SystemExit`, `MemoryError` from being swallowed as conversational errors. | Open |
| **Medium** | **PR #4843** — `fix(mcp): defer stale stack cleanup during reconnect` | Fixes MCP reconnect gateway crash by deferring `AsyncExitStack` cleanup. | Open |
| **Medium** | **Issue #940** — `AI Agent Cannot Access Host Filesystem – Skills & Media Processing Blocked` | Sandboxing blocks legitimate media/skill creation. Tension between **security isolation and multimodal/media workflows**. | None |
| **Low/Operational** | **Issue #4823** — `whatsapp - groups` | Channel allow-list regression. | None |

Links:  
- https://github.com/HKUDS/nanobot/issues/4864  
- https://github.com/HKUDS/nanobot/pull/4840  
- https://github.com/HKUDS/nanobot/issues/937  
- https://github.com/HKUDS/nanobot/pull/4862  
- https://github.com/HKUDS/nanobot/pull/4816  
- https://github.com/HKUDS/nanobot/pull/4843  
- https://github.com/HKUDS/nanobot/issues/940  
- https://github.com/HKUDS/nanobot/issues/4823

---

## 6. Feature Requests & Roadmap Signals

Research-relevant requests and likely near-term direction:

- **Task-specific model configuration (Issue #912)** — High community interest; would let users route different tasks to different models. Likely to appear in a near-term release if maintainers pick it up.
- **Native sandbox interface for untrusted plugins (Issue #931)** — Proposes a `SandboxDriver` defaulting to `deno` or `firecracker`. Strong alignment with AI safety/reliability.
- **Pre-handler hook for zero-token message routing (Issue #990)** — Bypasses LLM processing for deterministic patterns; relevant to long-context efficiency and cost-aware routing.
- **Multi-tenant gateway for multiple agents (Issue #936)** — Operational scalability; less research-centric.
- **Control plane for subagents (Issue #1006)** — `list`/`kill` commands for runaway subagents; important for reliability at scale.
- **Core tool additions: `nano_timer` (PR #4853)** — Time/timezone/calendar utility; modest but improves grounded temporal reasoning.

Links:  
- https://github.com/HKUDS/nanobot/issues/912  
- https://github.com/HKUDS/nanobot/issues/931  
- https://github.com/HKUDS/nanobot/issues/990  
- https://github.com/HKUDS/nanobot/issues/936  
- https://github.com/HKUDS/nanobot/issues/1006  
- https://github.com/HKUDS/nanobot/pull/4853

---

## 7. User Feedback Summary

Real pain points from the last 24 hours:

- **Hallucination in tool use:** The closed Issue #937 is a blunt signal: users stop evaluating when the agent invents `exec` commands. Reliability of tool grounding is a top user satisfaction driver.
- **Infinite loops and repeated tool calls:** Issues #4864 and the guard PRs (#4522, #4645) show users hitting reasoning loops on goal completion, web lookups, and file reads.
- **Sandbox/security vs. capability trade-off:** Issue #940 highlights that strict isolation blocks legitimate media and skill creation, suggesting the sandbox model needs finer-grained access policies.
- **Provider/model configuration friction:** Issues #1267 and #912 indicate users struggle with provider setup and want per-task model selection.
- **Channel regressions:** WhatsApp and Matrix regressions (#4823, #4859) show that multimodal/vision-rich I/O (images, markdown) is fragile across integrations.

---

## 8. Backlog Watch

Important but long-unanswered issues and PRs that need maintainer attention:

- **Issue #912 — Task-specific model configuration**  
  Open since 2026-02-20, 5 comments, 3 upvotes. Highly requested; stale label but no maintainer resolution.  
  https://github.com/HKUDS/nanobot/issues/912

- **Issue #937 — Hallucinations in `exec` tool**  
  Closed as stale with no fix. This is a high-impact reliability issue that may warrant reopening or a dedicated hallucination-mitigation PR.  
  https://github.com/HKUDS/nanobot/issues/937

- **Issue #931 — Native Sandbox Interface for untrusted plugins**  
  Security/reliability proposal with no maintainer response.  
  https://github.com/HKUDS/nanobot/issues/931

- **Issue #990 — Pre-handler Hook for Zero-Token Message Routing**  
  Could reduce unnecessary LLM calls and improve context efficiency.  
  https://github.com/HKUDS/nanobot/issues/990

- **Issue #940 — AI Agent Cannot Access Host Filesystem**  
  Blocks media/skill workflows; needs a design decision on sandbox granularity.  
  https://github.com/HKUDS/nanobot/issues/940

- **Issue #1006 — Control plane MVP for subagents**  
  Operational reliability for runaway subagents; no recent maintainer engagement.  
  https://github.com/HKUDS/nanobot/issues/1006

---

**Bottom line:** NanoBot is in a high-velocity stabilization phase. The most valuable research signals today are around **hallucination in tool execution, repeated-tool-call loops, sandbox isolation, and vision-language I/O correctness**. There is no evidence of new model training, post-training alignment, or long-context research in this window.

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent Research Digest — 2026-07-10

*Filtering applied: vision-language capabilities, reasoning mechanisms, long-context handling, post-training reliability, and hallucination-adjacent agent behavior. General product, auth, billing, and commercial/platform updates are excluded.*

---

## 1. Today's Overview

The repository saw high surface activity (50 issues and 50 PRs updated in the last 24 hours, zero releases), but the research-relevant signal is narrow. The core advances are one closed fix for GLM long-context overflow classification and several open PRs tightening reasoning-effort controls and transcript compaction. At the same time, unresolved reports continue to flag fragility in vision routing,

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw Project Digest — 2026-07-10
*(Research-relevant focus: multimodal reasoning, long-context handling, post-training alignment / tool safety, and AI reliability)*

---

## 1. Today’s Overview

PicoClaw had **no new releases** and **moderate maintenance activity** over the last 24 hours: 3 active issues and 16 pull-request updates, with 4 PRs closed/merged. The bulk of activity is routine connector, packaging, and dependency maintenance. From a research perspective, the signal is limited but nontrivial: notable open work touches **long-context prompt caching** for Bedrock, **multimodal text/media boundary handling** (inline data URLs in tool output), and **tool-call robustness / safety**. No vision-language model training or fine-tuning changes appeared in today’s data. Overall project health is stable but incremental.

---

## 2. Releases

**None.**

No new releases were published.

---

## 3. Project Progress

### Closed / merged PRs today

| PR | Title | Research / reliability relevance |
|---|---|---|
| [#3226](https://github.com/sipeed/picoclaw/pull/3226) | fix(tools): stop write_file from coaching destructive overwrite | **High** — removes a prompt/UX pattern that inadvertently encouraged the model to overwrite `memory/MEMORY.md`; alignment / tool-safety fix. |
| [#3171](https://github.com/sipeed/picoclaw/pull/3171) | fix(line): add ok checks for sync.Map type assertions in Send | Stability / panic prevention in LINE channel. |
| [#3213](https://github.com/sipeed/picoclaw/pull/3213) | build(deps): bump AWS SDK config | Dependency only — excluded from detailed analysis. |
| [#3207](https://github.com/sipeed/picoclaw/pull/3207) | build(deps): bump GitHub Copilot SDK | Dependency only — excluded from detailed analysis. |

### Active work advancing

- [#3163](https://github.com/sipeed/picoclaw/pull/3163) — Bedrock Converse prompt caching via explicit cache points (`system`, `tools`, `messages`). Relevant to **long-context efficiency** and reasoning cost.
- [#3115](https://github.com/sipeed/picoclaw/pull/3115) — Fixes corruption of session history when base64 `data:image/...` strings inside plain text tool output are misclassified as media attachments. Relevant to **multimodal / vision-language boundary handling**.
- [#3180](https://github.com/sipeed/picoclaw/pull/3180) — Skips CLI tool calls with invalid JSON arguments instead of dropping the whole batch. Relevant to **tool-use reasoning reliability**.

---

## 4. Community Hot Topics

Engagement is low today; no PRs show non-zero reactions, and most comment counts are undefined. The issues with measurable discussion are:

- **[#3201](https://github.com/sipeed/picoclaw/issues/3201)** — Support streaming output for QQ channel (2 comments). Underlying need: real-time, low-latency user experience across channels.
- **[#3203](https://github.com/sipeed/picoclaw/issues/3203)** — Matrix sync loop silently dies after network disruption (1 comment). Underlying need: long-running agent reliability and auto-recovery.
- **[#3206](https://github.com/sipeed/picoclaw/issues/3206)** — v2→v3 config migration fails with false “unknown field” error (1 comment). Underlying need: smooth upgrade path and onboarding.

Among PRs, research-oriented items such as [#3163](https://github.com/sipeed/picoclaw/pull/3163) (Bedrock caching), [#3115](https://github.com/sipeed/picoclaw/pull/3115) (data-URL media extraction), and [#3202](https://github.com/sipeed/picoclaw/pull/3202) (ID normalization) continue to see activity but lack visible comment traction.

---

## 5. Bugs & Stability

| Severity | Item | Issue / PR | Status |
|---|---|---|---|
| **Critical** | Matrix `/sync` loop dies permanently on network disruption; no auto-reconnect, so systemd restart is never triggered. | [#3203](https://github.com/sipeed/picoclaw/issues/3203) | Open; no fix PR yet |
| **High** | v2→v3 config migration fails on fresh installs, falsely reporting `build_info` and `session.dm_scope` as unknown fields. | [#3206](https://github.com/sipeed/picoclaw/issues/3206) | Open; no fix PR yet |
| **Medium** | Inline data URLs in text tool output (`read_file`, `exec`) are incorrectly treated as media attachments, corrupting session history. | [#3115](https://github.com/sipeed/picoclaw/pull/3115) | Fix PR open |
| **Medium** | `NormalizeAgentID` / `NormalizeAccountID` permit leading/trailing underscores, violating the documented allowed regex. | [#3202](https://github.com/sipeed/picoclaw/pull/3202) | Fix PR open |
| **Medium** | Malformed CLI tool-call arguments can cause the whole batch to be dropped; should skip only invalid entries. | [#3180](https://github.com/sipeed/picoclaw/pull/3180) | Fix PR open |
| **Low** | `openai_compat` provider fails to parse 9router gateway responses; also missing ARMv7 build target. | [#3205](https://github.com/sipeed/picoclaw/pull/3205) | Fix PR open |

---

## 6. Feature Requests & Roadmap Signals

Research and reliability-related signals:

- **Long-context / cost optimization:** [#3163](https://github.com/sipeed/picoclaw/pull/3163) adds Bedrock Converse prompt caching via cache points. This suggests the project is moving toward cheaper, longer-context inference.
- **Multimodal correctness:** [#3115](https://github.com/sipeed/picoclaw/pull/3115) aims to correctly separate base64 image strings inside generic

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw Project Digest — 2026-07-10

**Research-relevance note:** Most of the past 24 h of activity is operational (Telegram adapter behavior, message delivery, scheduled tasks, MCP security). The only directly vision-language-relevant item is the multimodal restoration PR. There are no updates on reasoning architectures, training methodologies, or explicit hallucination mitigation in this period.

---

## 1. Today's Overview

NanoClaw had **9 open issues** and **14 open PRs** updated in the last 24 h, with **3 PRs closed/merged** and **no new releases**. Activity is concentrated on adapter reliability, message delivery correctness, MCP server security, and scheduled-task infrastructure. Research-relevant threads are limited: a single PR restoring multimodal content blocks (image/voice/PDF) and a cluster of guard/approval work that touches AI reliability and alignment. No code changes related to model training, reasoning, or hallucination detection appeared in this window.

---

## 2. Releases

No new releases today.

---

## 3. Project Progress

**Merged/closed PRs today**

- [PR #2981](https://github.com/nanocoai/nanoclaw/pull/2981) — *Scheduled tasks: `ncl tasks` control plane, isolated sessions, script gate* (core-team). Ships the full `ncl tasks` resource, per-series isolated sessions, run history, and the pre-task script gate. This advances the agent reliability/control layer.
- [PR #2993](https://github.com/nanocoai/nanoclaw/pull/2993) — *Make NanoClaw resilient to a down container runtime*. Previously a failed `docker info` check at boot crashed the whole process; the host now treats this as a degraded state rather than exiting. Directly improves system reliability.
- [PR #2621](https://github.com/nanocoai/nanoclaw/pull/2621) — *chore: add `.gitattributes` to enforce LF line endings* (closed). Pure infrastructure hygiene.

**Research-relevant open progress**

- [PR #2618](https://github.com/nanocoai/nanoclaw/pull/2618) — *feat(multimodal,reactions): restore v1 image/voice/PDF + chat.onReaction*. This is the main vision-language-relevant item, re-adding image, voice, and PDF attachments as multimodal content blocks.
- [PR #2986](https://github.com/nanocoai/nanoclaw/pull/2986) — *Guard seam: one decision function for every privileged action*. Centralizes privileged-action decisions through a single `guard()` function; relevant to alignment/safety engineering.

---

## 4. Community Hot Topics

Most active by engagement (1 comment each):

- [Issue #2989](https://github.com/nanocoai/nanoclaw/issues/2989) — Telegram channels are silently blackholed when a bot token previously polled with a narrower `allowed_updates`. Underlying need: predictable, explicit adapter configuration so the system does not inherit stale server-side state.
- [Issue #2985](https://github.com/nanocoai/nanoclaw/issues/2985) — `opencode` provider: silent no-reply when the final text snapshot misses `session.idle`. Underlying need: reliable end-of-turn detection and delivery for streaming/agentic providers.

Other high-interest research/reliability threads:

- [PR #2618](https://github.com/nanocoai/nanoclaw/pull/2618) — multimodal restoration.
- [PR #2986](https://github.com/nanocoai/nanoclaw/pull/2986) — unified guard seam for privileged actions.

---

## 5. Bugs & Stability

Ranked by severity/research relevance:

| Severity | Item | Notes |
|----------|------|-------|
| **High** | [Issue #2995](https://github.com/nanocoai/nanoclaw/issues/2995) — Outbound messages to an offline channel adapter are marked `delivered` without any send. | Silent delivery failure. Fix in progress: [PR #2996](https://github.com/nanocoai/nanoclaw/pull/2996) and [PR #2226](https://github.com/nanocoai/nanoclaw/pull/2226). |
| **High** | [Issue #2985](https://github.com/nanocoai/nanoclaw/issues/2985) — `opencode` silent no-reply on long agentic turns. | Streaming-state edge case; output is generated but not surfaced. |
| **High** | [Issue #2827](https://github.com/nanocoai/nanoclaw/issues/2827) & [Issue #2762](https://github.com/nanocoai/nanoclaw/issues/2762) — `add_mcp_server` approval flow hides runtime `args`/`env`, enabling approval smuggling. | Security/alignment issue: model-initiated tool self-modification with hidden payload. Fix proposed in [PR #2998](https://github.com/nanocoai/nanoclaw/pull/2998). |
| **Medium** | [Issue #2997](https://github.com/nanocoai/nanoclaw/issues/2997) — `hasIdenticalSend` matches sends from previous fires, so recurring reminders with fixed text stop arriving. | State-deduplication bug. |
| **Medium** | [Issue #2992](https://github.com/nanocoai/nanoclaw/issues/2992) — Scheduled tasks are invisible across sessions of the same agent group. | Task isolation vs. cross-session management tension. |
| **Medium** | [Issue #2989](https://github.com/nanocoai/nanoclaw/issues/2989) — Telegram channels blackholed due to persisted `allowed_updates`. |
| **Low/Medium** | [Issue #2990](https://github.com/nanocoai/nanoclaw/issues/2990) & [Issue #2991](https://github.com/nanocoai/nanoclaw/issues/2991) — Telegram `my_chat_member` and channel `sender_scope='known'` handling. |
| **Hardening** | [PR #2802](https://github.com/nanocoai/nanoclaw/pull/2802) — `ncl` socket hardening: client timeout/cap and server fail-closed/frame-cap. | Prevents indefinite hangs and unbounded buffers. |

---

## 6. Feature Requests & Roadmap Signals

Research-relevant and reliability-oriented items likely to shape upcoming releases:

- **Multimodal content restoration** — [PR #2618](https://github.com/nanocoai/nanoclaw/pull/2618) restores image/voice/PDF handling. Likely to land soon given long-standing v2 gap.
- **Unified guard/approval layer** — [PR #2986](https://github.com/nanocoai/nanoclaw/pull/2986) and [PR #2998](https://github.com/nanocoai/nanoclaw/pull/2998) point to a broader alignment push around privileged actions.
- **Per-group capability toggles** — [PR #2983](https://github.com/nanocoai/nanoclaw/pull/2983) (lean defaults, existing groups grandfathered) suggests a “safe-by-default” configuration trend.
- **Audit/logging** — [PR #2987](https://github.com/nanocoai/nanoclaw/pull/2987) adds opt-in SIEM-shaped audit logs for the `ncl` surface.
- **Channel richness** — [PR #2877](https://github.com/nanocoai/nanoclaw/pull/2877) (Telegram `sendRichMessage`) and [PR #2994](https://github.com/nanocoai/nanoclaw/pull/2994) (Feishu delegation notifications) are more commercial/product-oriented; skipped for research focus.

**Prediction for next version:** The guard seam and the multimodal restoration PR are the most likely research-relevant features to land, followed by per-group harness toggles.

---

## 7. User Feedback Summary

Real pain points from this window:

- **Silent failures** are the dominant theme: messages dropped without error, channels blackholed, and the `opencode` provider producing answers that never reach the user.
- **Agentic/task reliability** — recurring reminders stop after the first fire, scheduled tasks are invisible across sessions, and long agentic turns fail to close properly.
- **Approval/alignment trust** — users/maintainers are concerned that hidden MCP server arguments can be smuggled through the approval flow.
- **Multimodal gap** — the open restoration PR signals user/community demand for image/voice/PDF support that existed in v1.

---

## 8. Backlog Watch

Older important issues/PRs still open and needing attention:

- [PR #2618](https://github.com/nanocoai/nanoclaw

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

**LobsterAI Project Digest – 2026-07-10**  
*Research-oriented filter: vision-language, reasoning, training/reliability, hallucination.*

---

## 1. Today’s Overview

LobsterAI saw a busy maintenance day with **19 updated items** (5 issues, 14 PRs), of which **11 PRs were merged/closed** and **1 issue was closed**. However, the **research-relevant signal is narrow**: most activity is UI/UX polish, localization, installer cleanup, and IM-group task routing. Only a handful of PRs touch the agent runtime, tool delegation, multimodal steer queues, memory configuration, or prompt-handling reliability. No new releases were published.

---

## 2. Releases

**No new releases today.**

---

## 3. Project Progress – Research-Relevant Merges

Among the 11 merged/closed PRs, the following are relevant to multimodal reasoning, agent orchestration, and reliability:

- **#2308** – fix(cowork): strip null bytes from prompts before OpenClaw gateway send  
  [https://github.com/netease-youdao/LobsterAI/pull/2308](https://github.com/netease-youdao/LobsterAI/pull/2308)  
  Sanitizes NUL bytes (`U+0000`) at ingestion and at the outbound boundary; prevents hard gateway rejects and persistence of corrupted prompts in continuity capsules and evidence bridges.

- **#2307** – fix(cowork): refine prompt modes and steer follow-up handling  
  [https://github.com/netease-youdao/LobsterAI/pull/2307](https://github.com/netease-youdao/LobsterAI/pull/2307)  
  Removes Plan Mode from the prompt menu, moves Goal/Steer status bars above the input, and fixes queued Steer follow-up behavior. This is relevant to turn-taking and reasoning control in multi-step agent workflows.

- **#2303** – fix(openclaw): support agent-scoped local tools  
  [https://github.com/netease-youdao/LobsterAI/pull/2303](https://github.com/netease-youdao/LobsterAI/pull/2303)  
  Extends `AskUserQuestion` and image/video generation tools to non-main desktop agents and delegated child sessions; routes media callbacks back to local Cowork sessions while denying IM-bound sessions. Directly touches multimodal (image/video) tool use and agent-scoped capability delegation.

- **#2301** – fix(openclaw): explicitly disable memory dreaming  
  [https://github.com/netease-youdao/LobsterAI/pull/2301](https://github.com/netease-youdao/LobsterAI/pull/2301)  
  Writes `dreaming.enabled=false` in generated OpenClaw config when LobsterAI dreaming is off, allowing OpenClaw to reconcile and remove stale managed dream cron jobs. Relevant to long-context memory and background reasoning reliability.

- **#2300** – fix(cowork): support attachments in steer queue  
  [https://github.com/netease-youdao/LobsterAI/pull/2300](https://github.com/netease-youdao/LobsterAI/pull/2300)  
  Lets follow-up messages queued during active turns carry file attachments, dragged files, pasted files, selected text, and image payloads. Multimodal inputs are snapshotted and rehydrated from local files before submission.

- **#2299** – fix(cowork): sync subagent child tool history  
  [https://github.com/netease-youdao/LobsterAI/pull/2299](https://github.com/netease-youdao/LobsterAI/pull/2299)  
  Refactors subagent gateway history parsing into a shared helper, reuses it when materializing child sessions, and recovers orphan subagent tool results by recognizing broader tool-call history shapes. Important for transparent reasoning traces across parent/child agents.

Other closed PRs today were mostly product-side (Windows title bar, sidebar pagination, agent ordering, display names, uninstaller, localized timestamps).

---

## 4. Community Hot Topics

Engagement remains low; most items have 0–1 reactions and 0–1 comments.

- **#1394** – [CLOSED] 定时任务选择不重复执行时，执行一次后会自动被永久删除  
  [https://github.com/netease-youdao/LobsterAI/issues/1394](https://github.com/netease-youdao/LobsterAI/issues/1394)  
  The most-discussed issue today with **2 comments**. Underlying need: users expect “non-repeating” scheduled tasks to remain editable and reusable after one execution, rather than being deleted automatically.

- **#1339 / #1341 / #1343 / #1345** – Open feature requests with 1 comment each  
  - [https://github.com/netease-youdao/LobsterAI/issues/1339](https://github.com/netease-youdao/LobsterAI/issues/1339) – message timestamps  
  - [https://github.com/netease-youdao/LobsterAI/issues/1341](https://github.com/netease-youdao/LobsterAI/issues/1341) – keyboard history navigation  
  - [https://github.com/netease-youdao/LobsterAI/issues/1343](https://github.com/netease-youdao/LobsterAI/issues/1343) – full-text search inside sessions  
  - [https://github.com/netease-youdao/LobsterAI/issues/1345](https://github.com/netease-youdao/LobsterAI/issues/1345) – export conversations to Markdown  

  These collectively reveal a need for better conversation metadata, discoverability, and offline text reuse rather than just image screenshots.

---

## 5. Bugs & Stability

| Severity | Item | Description | Status |
|---|---|---|---|
| **High** | **#2308** | NUL-byte payloads hard-rejected by OpenClaw gateway; can persist and re-enter via continuity capsules and evidence bridges. | **Fixed** (closed) |
| **Medium** | **#2299** | Subagent child-session tool history was not always synchronized, causing missing or orphan tool results in child session views. | **Fixed** (closed) |
| **Medium** | **#2301** | Memory dreaming state could leave stale managed cron jobs if not explicitly disabled in OpenClaw config. | **Fixed** (closed) |
| **Medium** | **#2306** | IM group scheduled-task routing broken for legacy/manual/natural runs; open PR addresses agent-scoped group sessions. | **In progress** ([https://github.com/netease-youdao/LobsterAI/pull/2306](https://github.com/netease-youdao/LobsterAI/pull/2306)) |
| **Low** | **#1394** | Non-repeating scheduled tasks auto-deleted after first run, conflicting with user expectation of edit/reuse. | **Closed** |

---

## 6. Feature Requests & Roadmap Signals

- **Conversation export as Markdown** (#1345) – strongest indicator that users want machine-readable, editable conversation archives, not just screenshots.
- **Full-text session search** (#1343) – suggests users are building long enough conversations that title-only search is insufficient.
- **Keyboard history navigation** (#1341) and **timestamps** (#1339) – point to an iterative prompting workflow where users repeatedly tweak prior instructions.
- **Research implication:** If adopted, these UX improvements could support better prompt-versioning, evaluation datasets, and longitudinal conversation analysis, but they are not core model/research features.

---

## 7. User Feedback Summary

**Real pain points captured today:**
- Scheduled-task behavior contradicts expectations of reusability.
- Chat history is hard to navigate, search, and reuse (no timestamps, no text search, no history recall).
- Exporting to image is insufficient for users who need text notes or further editing.

**Sentiment:** No explicit satisfaction metrics, but the repeated “功能缺失” (missing feature) pattern suggests the Cowork chat interface is still maturing. The core agent/runtime work is focused on **reliability** (null-byte handling, memory dreaming, tool-history sync) rather than new capability expansion.

---

## 8. Backlog Watch

These stale items from April remain open and may need maintainer triage:

- **#1339** – message timestamps (has matching PR **#1340**)  
  [https://github.com/netease-youdao/LobsterAI/issues/1339](https://github.com/netease-youdao/LobsterAI/issues/1339) / [https://github.com/netease-youdao/LobsterAI/pull/1340](https://github.com/netease-youdao/LobsterAI/pull/1340)

- **#1341** – Up/Down history navigation (has matching PR **#1342**)  
  [https://github.com/netease-youdao/LobsterAI/issues/1341](https://github.com/netease-youdao/LobsterAI/issues/1341) / [https://github.com/netease-youdao/LobsterAI/pull/1342](https://github.com/netease-youdao/LobsterAI/pull/1342)

- **#1343** – full-text search in sessions  
  [https://github.com/netease-youdao/LobsterAI/issues/1343](https://github.com/netease-youdao/LobsterAI/issues/1343)

- **#1345** – export to Markdown  
  [https://github.com/netease-youdao/LobsterAI/issues/1345](https://github.com/netease-youdao/LobsterAI/issues/1345)

- **#2306** – open PR for IM group task routing  
  [https://github.com/netease-youdao/LobsterAI/pull/2306](https://github.com/netease-youdao/LobsterAI/pull/2306)

**Note:** The matching PRs (#1340, #1342) have been open since early April without merge, suggesting they may need review, conflict resolution, or prioritization before the next release cycle.

---

**Bottom line for research relevance:** Today’s LobsterAI activity is dominated by product polish and reliability fixes. For multimodal/research audiences, the most notable signals are the improved handling of multimodal attachments in steer queues, agent-scoped image/video generation tools, and the ongoing hardening of parent/child agent tool-history synchronization.

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

No activity in the last 24 hours.

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

**Moltis Project Digest — 2026-07-10**  
*Research-relevant filter applied: vision-language capabilities, reasoning mechanisms, training methodologies, hallucination-related issues. General product/commercial updates are noted only when they have research-relevant implications.*

---

### 1. Today's Overview
The last 24 hours show minimal activity in the Moltis repository. There were **no new issues** and **no new releases**, and only **one open pull request** was updated. No merged or closed work items were recorded, so the project did not advance any active research feature today. From the available data, there are **no updates directly related to multimodal reasoning, long-context training methods, vision-language models, or hallucination mitigation**. The repository appears to be in a stable but low-velocity state.

---

### 2. Releases
**None.**  
No new versions were released in the last 24 hours.

---

### 3. Project Progress
**No merged or closed PRs today.**  
Only one open PR was touched:

- **PR #1146 — Add GPT-5.6 model support** (open)  
  - Author: PeterDaveHello  
  - Created/Updated: 2026-07-09  
  - Link: https://github.com/moltis-org/moltis/pull/1146  
  - Summary: Adds GPT-5.6 Sol, Terra, and Luna to OpenAI/OpenAI Codex fallback catalogs; applies a 1.05M-token API context window and a 372K-token ChatGPT/Codex backend limit; updates configuration templates and provider-selection documentation.

**Research relevance:** This is primarily a **model-catalog / provider-compatibility maintenance** change rather than a research advancement. The only tangentially research-relevant aspect is the **context-window bookkeeping** (1.05M vs. 372K limits), which touches long-context infrastructure but does not introduce new reasoning, training, or hallucination-mitigation methodology.

---

### 4. Community Hot Topics
**No active community threads today.**  
There are zero open or closed issues, and the single open PR has **no reactions and no recorded comments**. No underlying research demand (e.g., for multimodal support, chain-of-thought tooling, or alignment features) can be inferred from the current data.

---

### 5. Bugs & Stability
**None reported today.**  
No bug, crash, or regression issues were opened or closed in the last 24 hours.

---

### 6. Feature Requests & Roadmap Signals
**No user feature requests today.**  
With zero issues, there are no explicit research-oriented requests. The open PR (#1146) indicates ongoing maintenance to keep up with OpenAI model rollouts, but it does not signal investment in:
- vision-language capabilities,
- reasoning architectures,
- post-training alignment,
- or hallucination detection/reduction.

---

### 7. User Feedback Summary
**Insufficient data for a meaningful feedback summary.**  
No user issues, comments, or reactions were recorded in the last 24 hours, so pain points, satisfaction, or dissatisfaction cannot be assessed.

---

### 8. Backlog Watch
**No long-unanswered research issues identified.**  
The only item requiring maintainer attention is the newly opened PR:

- **PR #1146 — Add GPT-5.6 model support**  
  https://github.com/moltis-org/moltis/pull/1146  
  - Has been open for one day and has not yet been reviewed or merged.  
  - Worth monitoring because model-catalog PRs can affect downstream context-window behavior and provider fallbacks, but the change itself is operational.

---

**Overall assessment:** Moltis is quiet on research-relevant fronts today. The sole activity is a routine OpenAI model-support update with no clear implications for multimodal reasoning, training methodologies, or AI reliability.

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

# ZeroClaw Project Digest — 2026-07-10
*Research-relevant filter: vision-language, reasoning, training, hallucination/reliability*

---

## 1. Today's Overview

On 2026-07-10 ZeroClaw saw **32 issue updates** (23 open/active, 9 closed) and **50 pull-request updates** (46 open, 4 merged/closed), with **0 new releases**. The research-relevant subset is modest: most activity clusters around **agent reasoning instrumentation** (tool lifecycle, goal/delegation tools, context metering), **persistent memory curation**, and **mitigating prompt leakage on small local models**. No vision-language-specific issues or PRs surfaced in the last 24 h. The highest-impact open items are a long-context message-loss bug and a persistent-memory parity tracker. Overall project health is active, but research-adjacent progress remains scattered across runtime reliability and governance rather than model-centric advances.

---

## 2. Releases

**No new releases today.**

---

## 3. Project Progress

No merged or closed PRs today directly advance the vision-language / reasoning / training / hallucination themes. The 4 closed PRs in

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*