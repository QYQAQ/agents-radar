# AI CLI Tools Community Digest 2026-07-15

> Generated: 2026-07-15 00:20 UTC | Tools covered: 9

- [Claude Code](https://github.com/anthropics/claude-code)
- [OpenAI Codex](https://github.com/openai/codex)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [GitHub Copilot CLI](https://github.com/github/copilot-cli)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-cli)
- [OpenCode](https://github.com/anomalyco/opencode)
- [Pi](https://github.com/badlogic/pi-mono)
- [Qwen Code](https://github.com/QwenLM/qwen-code)
- [DeepSeek TUI](https://github.com/Hmbown/DeepSeek-TUI)
- [Claude Code Skills](https://github.com/anthropics/skills)

---

## Cross-Tool Comparison

# Cross-Tool AI CLI Research Digest Synthesis  
**Date:** 2026-07-15  
**Focus:** Long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation

---

## 1. Ecosystem Overview

The AI CLI landscape is shifting from simple chat-and-edit wrappers toward long-horizon, multi-agent coding systems, and today’s activity reflects the growing pains of that transition. The dominant engineering concerns are no longer basic model access but *reliability at scale*: long-context compaction, reasoning-trace fidelity, agent-to-agent communication, and runtime alignment guardrails. No single tool is solving all of these problems simultaneously; instead, each project is attacking a different subset of production-agent failure modes. Multimodal and document/OCR capabilities remain secondary but increasingly visible, while post-training alignment and hallucination mitigation are becoming first-class, community-driven priorities.

---

## 2. Activity Comparison

| Tool | Research-Relevant Issues | Research-Relevant PRs | Releases | Primary Focus Areas |
|---|---|---|---|---|
| **Claude Code** | 5 | 1 | 0 (UI-only patches) | Multi-agent routing, tool-schema hallucination, long-context continuity |
| **OpenAI Codex** | 2 | 3 | 0 (no user-facing changes) | GPT-5.6 long-context regressions, Guardian policy prompts, imagegen grounding |
| **Gemini CLI** | 10 | 3 | 0 (nightly only) | Reasoning turn limits, shell-output context bounds, subagent success verification |
| **GitHub Copilot CLI** | 10 | 0 | 2 | Local ASR multimodal, PDF/OCR, agent sandboxing, guardrail enforcement |
| **Kimi Code CLI** | 2 (operational) | 3 | 0 | Provider-native reasoning APIs, reasoning-content preservation, dynamic budgets |
| **OpenCode** | 7 | 5 | 0 (UI-only) | Reasoning transparency, context compaction UI, tool-call reliability |
| **Pi** | 6 | — | 1 | Long-context orchestration, prompt RPC multimodal, cache/session affinity |
| **Qwen Code** | Multiple (data truncated) | Multiple (data truncated) | 1 (details cut off) | Long-context memory, vision/PDF bridge, MCP/file trust |
| **DeepSeek TUI / CodeWhale** | 3 | 1 | 0 | Constitutional adherence, context compaction gates |

---

## 3. Shared Feature Directions

Several requirements appear across multiple communities, suggesting convergent industry priorities:

| Direction | Tools Involved | Specific Needs |
|---|---|---|
| **Long-context management & compaction** | Claude, Codex, Gemini, Copilot, OpenCode, Pi, Qwen, DeepSeek | User-visible compaction controls, context-budget-aware completion limits, remote-compaction fault tolerance, binary-diff filtering |
| **Reasoning control & trace fidelity** | Kimi, OpenCode, Gemini, Pi | Provider-native reasoning knobs, preservation of empty/unsigned `reasoning_content`, reasoning-thought display, max-reasoning-turn caps |
| **Multi-agent / subagent alignment** | Claude, Gemini, Copilot, OpenCode | Model override persistence across continuations, declarative fallback models, accurate success/failure reporting, agent sandboxing |
| **Tool-use hallucination & schema compliance** | Claude, Gemini, OpenCode, Copilot, Qwen | Prevention of invented tool fields, null-parameter handling, flattened argument parsing, tool-set compression |
| **Safety / guardrails / constitutional adherence** | Gemini, Copilot, OpenCode, Qwen, DeepSeek | PreToolUse/PostToolUse hooks, deterministic redaction, destructive-command discouragement, constitution/script compliance |
| **Multimodal & document ingestion** | Copilot, Pi, Qwen, Codex | Native PDF reading, ASR routing, video/audio prompt support, imagegen output grounding |

**Note on OCR/HMER:** Direct OCR/HMER activity is sparse. The closest signals are Copilot’s PDF-reading feature request (#443), Qwen’s PDF vision-bridge fixes, and general document-ingestion demand; no handwritten math recognition work surfaced in this batch.

---

## 4. Differentiation Analysis

| Tool | Feature Focus | Target Users | Technical Approach |
|---|---|---|---|
| **Claude Code** | Multi-agent coordination and long-horizon instruction continuity | General-purpose coding-agent users | Agent-centric messaging, subagent model overrides, temporal memory |
| **OpenAI Codex** | Persistent goals and policy-injected guardrails | OpenAI ecosystem, goal-driven developers | Remote context management, Guardian policy templates, imagegen output |
| **Gemini CLI** | Reasoning-scale control and context-pressure management | Google/Gemini ecosystem, experimental users | Recursive turn limits, bounded shell output, AST-aware retrieval |
| **GitHub Copilot CLI** | Enterprise guardrails and local multimodal reliability | GitHub-centric, enterprise developers | Agent sandboxing, MCP persistence, local ASR/PDF integration |
| **Kimi Code CLI** | Provider-native reasoning parameter hygiene | Kimi API users, reasoning-model adopters | `thinking.type` separation, reasoning-content preservation, dynamic budgets |
| **OpenCode** | Desktop-first reasoning transparency and UX control | Desktop agent users, reasoning auditors | Claude-style hooks, one-click compaction, plan/build mode toggles |
| **Pi** | Multi-provider long-context orchestration | Advanced users, provider-agnostic workflows | `models.json` compatibility, session affinity, prompt RPC multimodal |
| **Qwen Code** | Vision/document reliability and autonomous trust | Qwen ecosystem users | PDF vision bridge, MCP trust

---

## Per-Tool Reports

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills Highlights

> Source: [anthropics/skills](https://github.com/anthropics/skills)

# Claude Code Skills Community Highlights Report  
*As of 2026-07-15 — filtered to document processing, visual understanding, reasoning augmentation, and alignment/safety in coding agents.*

---

## 1. Top Skills Ranking

These are the most-visible, relevant Skill PRs in the current snapshot. All are **open** and awaiting final review.

| # | Skill | What it does | Discussion highlights | Status |
|---|-------|--------------|-----------------------|--------|
| **#514** | **document-typography** | Enforces typographic quality in generated documents: prevents widow/orphan lines, misaligned numbering, and other layout flaws. | Positioned as a universal fix for “invisible” document quality problems that affect nearly every AI-generated doc. | Open |
| **#486** | **odt** | Create, fill, read, and convert OpenDocument files (`.odt`, `.ods`) and parse ODT to HTML. | Fills a clear gap in open-standard document workflows; covers triggers, file creation, and template filling. | Open |
| **#541** | **docx fix** | Fixes DOCX corruption by avoiding `w:id` collisions between tracked changes and existing bookmarks. | A narrow but high-impact OOXML correctness fix from the same contributor who patched the PDF skill. | Open |
| **#538** | **pdf fix** | Corrects case-sensitive file references in `skills/pdf/SKILL.md`. | Small doc fix, but important for case-sensitive filesystems and CI reproducibility. | Open |
| **#1367** | **self-audit** | Two-stage output gate: mechanical file verification first, then a four-dimension reasoning audit ordered by damage severity. | Broadly applicable across any project/model; emphasizes “verify before deliver.” | Open |
| **#210** | **frontend-design** | Tightens the existing skill so every instruction is actionable within a single conversation. | Focuses on prompt-level usability rather than adding new tools. | Open |
| **#83** | **skill-quality-analyzer & skill-security-analyzer** | Marketplace meta-skills that evaluate Skill structure/documentation and flag security issues. | Brings systematic quality and safety review into the skill creation process. | Open |
| **#1302** | **color-expert** | Comprehensive color guidance: color naming systems, color spaces (OKLCH, OKLAB, CAM16), and palette generation. | Self-contained visual expertise skill for design, data viz, and branding tasks. | Open |

Links: [#514](https://github.com/anthropics/skills/pull/514), [#486](https://github.com/anthropics/skills/pull/486), [#541](https://github.com/anthropics/skills/pull/541), [#538](https://github.com/anthropics/skills/pull/538), [#1367](https://github.com/anthropics/skills/pull/1367), [#210](https://github.com/anthropics/skills/pull/210), [#83](https://github.com/anthropics/skills/pull/83), [#1302](https://github.com/anthropics/skills/pull/1302).

---

## 2. Community Demand Trends (from Issues)

The most-requested directions for new or improved Skills fall into four clusters:

- **Document robustness** — There is sustained demand for better handling of DOCX, PDF, ODT, and typographic correctness (e.g., #514, #486, #538, #541). Users want AI-generated documents that survive real-world office tools.
- **Reasoning verification & quality gates** — Proposals like **#1385** (Reasoning Quality Gate Pipeline) and **#1329** (compact-memory symbolic notation) show interest in making long-context reasoning and agent outputs more reliable.
- **Visual & frontend design** — Interest in color systems (#1302) and actionable frontend-design guidance (#210) suggests the community wants polished, visual-output skills.
- **Safety, governance, and trust boundaries** — Security is a major theme: **#492** (namespace impersonation risk), **#412** (agent-governance safety patterns), and **#1175** (SharePoint access-control concerns) all point to a demand for guardrails in how skills are distributed and executed.

Links: [#492](https://github.com/anthropics/skills/issues/492), [#412](https://github.com/anthropics/skills/issues/412), [#1385](https://github.com/anthropics/skills/issues/1385), [#1175](https://github.com/anthropics/skills/issues/1175), [#1329](https://github.com/anthropics/skills/issues/1329).

---

## 3. High-Potential Pending Skills

These open PRs have active refinement and are the most likely to land soon within the relevant domains:

1. **document-typography** [#514](https://github.com/anthropics/skills/pull/514) — universal document quality control.
2. **odt** [#486](https://github.com/anthropics/skills/pull/486) — open-standard document creation and conversion.
3. **self-audit** [#1367](https://github.com/anthropics/skills/pull/1367) — reasoning and output verification gate.
4. **color-expert** [#1302](https://github.com/anthropics/skills/pull/1302) — visual color reasoning.
5. **skill-quality-analyzer / skill-security-analyzer** [#83](https://github.com/anthropics/skills/pull/83) — meta review and safety skills.
6. **docx bookmark collision fix** [#541](https://github.com/anthropics/skills/pull/541) — production DOCX stability.
7. **frontend-design** [#210](https://github.com/anthropics/skills/pull/210) — clearer UI/UX guidance.

---

## 4. Skills Ecosystem Insight

The community’s most concentrated demand is for **production-grade document and visual-output skills**, layered with **reasoning verification and safety guardrails** — from typographic correctness and open-format support to skill-level security analyzers and trust-boundary governance.

---

---

**Claude Code Research Digest — 2026-07-15**

---

### 1. Today’s Highlights

The last 24 hours highlight several reliability and alignment issues in multi-agent and long-context workflows: subagent model overrides are being lost across continuation boundaries, agent-to-agent messaging is generating hallucinated tool fields, and long-running sessions show weak temporal reasoning. No release or PR in this window directly addresses OCR, multimodal reasoning, or long-context modeling itself.

---

### 2. Releases

No release in the last 24 hours is directly relevant to long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, or hallucination mitigation.  
- v2.1.210, v2.1.209, and v2.1.208 are UI/accessibility and permission-rule updates.  
*Omitted from this digest.*

---

### 3. Research-Relevant Issues

| Issue | Relevance | GitHub Link |
|---|---|---|
| **#77595 — Agent teams: `SendMessage` duplicates the message body ~3× per call (model-invented `content` field + result echo)** | A concrete example of tool-use hallucination: the model invents an undocumented top-level `content` field in ~100% of free-text agent sends, causing payload duplication and noisy inter-agent communication. Useful for studying schema-compliant generation and hallucination mitigation in multi-agent tool use. | https://github.com/anthropics/claude-code/issues/77595 |
| **#68147 — Subagent model override silently dropped after a continuation boundary** | Explicit `model` parameters for subagents only apply to the first leg of execution; after a `SendMessage` follow-up or compaction resume, the override is lost. Directly relevant to long-context continuity and post-training alignment / instruction-following over extended sessions. | https://github.com/anthropics/claude-code/issues/68147 |
| **#47488 — Cowork: Agent tool `model` parameter silently ignored; all sub-agents routed to Haiku** | The client ignored the requested model and routed every sub-agent to Haiku, creating a mismatch between user intent and runtime behavior. Relevant to model-routing alignment and multi-agent deployment reliability. | https://github.com/anthropics/claude-code/issues/47488 |
| **#73931 — Per-subagent availability fallback model (declarative), not just silent inherit** | Currently a pinned subagent model falls back silently to the inherited session model when unavailable. The request is for a declarative fallback, which touches robustness, model governance, and alignment of multi-agent systems. | https://github.com/anthropics/claude-code/issues/73931 |
| **#66245 — Agent defaults timestamps to current date for multi-day session work instead of actual work date** | In long-running sessions that span calendar days, the agent records historical events using the current date rather than the original date. Signals a long-context temporal-reasoning gap and grounding failure. | https://github.com/anthropics/claude-code/issues/66245 |

*No OCR/HMER or general multimodal-reasoning issues appeared in this batch.*

---

### 4. Research-Relevant PRs

| PR | Relevance | GitHub Link |
|---|---|---|
| **#77427 — fix(pr-review-toolkit): make code-reviewer a leaf agent** | Restricts the `code-reviewer` agent to repository-inspection tools and prevents it from spawning additional agents or review workflows. A small alignment/safety-style fix that limits recursive agent expansion and reduces unintended autonomy. | https://github.com/anthropics/claude-code/pull/77427 |

No other open or closed PR in the last 24 hours directly addresses the listed research directions.

---

### 5. Research Direction Signals

- **Multi-agent model routing and override persistence** are becoming first-class alignment concerns: users expect explicit model assignments to survive continuation boundaries and unavailable models.
- **Tool-schema hallucination** is surfacing in inter-agent communication, suggesting a need for tighter schema validation and constrained generation in agent-to-agent tool calls.
- **Temporal grounding in long contexts** is weak: agents conflate the current session date with the dates of historical events, pointing to a need for better episodic/time-aware memory.
- **Declarative fallback policies** for pinned models are a requested feature, indicating that silent inheritance may become a source of misalignment in production multi-agent systems.

---

### 6. Technical Limitations

- **Continuation boundaries reset agent-level state.** Model overrides and possibly other per-subagent configuration are not preserved across compaction or follow-up boundaries, undermining long-horizon instruction following.
- **Agent messaging lacks strict schema enforcement.** The model can invent undocumented fields (e.g., `content` in `SendMessage`), leading to duplicated payloads and unreliable inter-agent communication.
- **No declarative model fallback mechanism.** When a pinned subagent model is unavailable, the system silently inherits the parent session model rather than following an explicit fallback policy.
- **Poor historical-date tracking in multi-day sessions.** Agents default to the current date when recording past work, indicating that long-context memory does not reliably preserve temporal metadata.

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

# OpenAI Codex Research Digest — 2026-07-15

## 1. Today's Highlights
The most notable research-relevant activity is two **long-context regressions** in GPT-5.6 Sol: one closed issue reports that usable context dropped from ~353K to 258K tokens despite an advertised 1.05M-token window, and a second issue shows that a long-running `/goal` task can be killed by a **remote-compaction capacity error** while other tasks remain healthy. On the multimodal and alignment side, a merged image-generation fix prevents duplicated markdown image links, and another merged PR adds model-catalog templates for Guardian policy prompts.

## 2. Releases
No research-relevant release notes were included in the last 24h. The only patch listed (`rust-v0.144.4`) explicitly states “No user-facing changes,” and the alpha releases contain no detailed changelogs.

## 3. Research-Relevant Issues

| Issue | Why it matters |
|-------|----------------|
| **#32806** — [🚨 [SEVERE REGRESSION] GPT-5.6 Sol context cut again: 353K → 258K despite advertised 1.05M](https://github.com/openai/codex/issues/32806) | A concrete example of the gap between advertised and *usable* long-context budgets. Useful for studying context culling, compaction, and token-accounting strategies. |
| **#33171** — [Codex Desktop: remote-compaction capacity error terminalizes one persistent goal while other tasks remain healthy](https://github.com/openai/codex/issues/33171) | Shows that long-running persistent goals with `gpt-5.6-sol` at `xhigh` reasoning can hit remote-compaction limits. Highlights the need for fault-tolerant context/state compaction in long-horizon agents. |

*No OCR/HMER-specific issues appeared in the last 24h.*

## 4. Research-Relevant PRs

| PR | Technical contribution / research relevance |
|----|-----------------------------------------------|
| **#31485** — [fix(imagegen): avoid duplicate markdown image links](https://github.com/openai/codex/pull/31485) | Tells the model that generated images are already displayed, preventing duplicate markdown links/embeds. Relevant to **multimodal output grounding** and model-generated UI fidelity. |
| **#33177** — [Support model catalog templates for Guardian policy prompts](https://github.com/openai/codex/pull/33177) | Adds an optional `policy_template` field and builds Guardian instructions from a catalog template. Touches **post-training alignment/safety** by improving how policy guardrails are injected into model messages. |
| **#31466** — [Capture tool search pipeline diagnostics in /feedback](https://github.com/openai/codex/pull/314

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

# Gemini CLI Research Digest — 2026-07-15

*Filtered for: long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, and hallucination mitigation.*

---

## 1. Today's Highlights

Today’s most research-relevant changes center on **controlling reasoning scale and context pressure**: a new core limit on recursive reasoning turns and a bound on shell output injected into the model context were proposed. Meanwhile, active issue discussions highlight recurring problems in **subagent success/hallucination reporting**, **component-level behavioral evaluation**, and **alignment/safety** (e.g., destructive command劝阻, deterministic redaction, and self-awareness). There are no direct OCR/HMER or multimodal-vision updates in the last 24 h.

---

## 2. Releases

No research-relevant release changes were observed. The nightly `v0.52.0-nightly.20260714.gfa975395b` contains only quota-error messaging and A2A task-cancellation fixes, which are outside the target research scope.

---

## 3. Research-Relevant Issues

- **#22323 — Subagent recovery after `MAX_TURNS` is reported as `GOAL` success, hiding interruption**  
  [google-gemini/gemini-cli#22323](https://github.com/google-gemini/gemini-cli/issues/22323)  
  *Significance:* False-positive “success” after a turn-limit interrupt is a concrete hallucination/verification failure mode; relevant to subagent termination metrics and eval design.

- **#24353 — Robust component-level evaluations**  
  [google-gemini/gemini-cli#24353](https://github.com/google-gemini/gemini-cli/issues/24353)  
  *Significance:* Follow-up to behavioral evals; directly tied to post-training alignment infrastructure and scalable evaluation of component behavior.

- **#22745 — Assess the impact of AST-aware file reads, search, and mapping**  
  [google-gemini/gemini-cli#22745](https://github.com/google-gemini/gemini-cli/issues/22745)  
  *Significance:* Reducing token noise and reading exact semantic boundaries is a long-context efficiency/reasoning problem.

- **#22746 — Investigate using AST-aware CLI tools to map codebase**  
  [google-gemini/gemini-cli#22746](https://github.com/google-gemini/gemini-cli/issues/22746)  
  *Significance:* Complements #22745; explores structured codebase indexing for better context retrieval and reasoning.

- **#21968 — Gemini does not use skills and sub-agents enough**  
  [google-gemini/gemini-cli#21968](https://github.com/google-gemini/gemini-cli/issues/21968)  
  *Significance:* A tool-use / routing alignment gap; post-training methods may need to improve implicit skill selection.

- **#22672 — Agent should stop/discourage destructive behavior**  
  [google-gemini/gemini-cli#22672](https://github.com/google-gemini/gemini-cli/issues/22672)  
  *Significance:* Safety and alignment — guarding against risky shell/Git commands via refusal or safer-plan generation.

- **#21432 — Improve Agent “Self-Awareness”: Accurate CLI flags, hotkeys, and self-execution**  
  [google-gemini/gemini-cli#21432](https://github.com/google-gemini/gemini-cli/issues/21432)  
  *Significance:* Meta-knowledge hallucinations about the agent’s own capabilities; relevant to self-modeling and calibration.

- **#24246 — Gemini CLI encounters 400 error with > 128 tools**  
  [google-gemini/gemini-cli#24246](https://github.com/google-gemini/gemini-cli/issues/24246)  
  *Significance:* Tool-set compression and intelligent tool scoping are long-context reasoning and retrieval challenges.

- **#22598 — Subagent trajectory should be visible via `/chat share`**  
  [google-gemini/gemini-cli#22598](https://github.com/google-gemini/gemini-cli/issues/22598)  
  *Significance:* Improves traceability and data collection for post-training alignment and failure analysis.

- **#26525 — Add deterministic redaction and reduce Auto Memory logging**  
  [google-gemini/gemini-cli#26525](https://github.com/google-gemini/gemini-cli/issues/26525)  
  *Significance:* Model-based redaction is unreliable; deterministic safety guarantees are an alignment/privacy need.

---

## 4. Research-Relevant PRs

- **#28164 — `fix(core)`: limit recursive reasoning turns per single user request**  
  [google-gemini/gemini-cli#28164](https://github.com/google-gemini/gemini-cli/pull/28164)  
  *Contribution:* Caps recursive reasoning at 15 turns per user request (configurable via `maxSessionTurns`), directly addressing long-context reasoning loops, resource exhaustion, and runaway token use.

- **#28401 — `fix(shell)`: bound command output sent to the model**  
  [google-gemini/gemini-cli#28401](https://github.com/google-gemini/gemini-cli/pull/28401)  
  *Contribution:* Prevents unbounded shell output from flooding the model context, improving long-context stability and response quality.

- **#28319 — `refactor(a2a-server)`: enforce path trust check prior to environment loading and isolate task environment**  
  [google-gemini/gemini-cli#28319](https://github.com/google-gemini/gemini-cli/pull/28319)  
  *Contribution:* Reorders trust checks before environment loading and isolates task environments; relevant to safety, alignment, and privilege control in agent execution.

---

## 5. Research Direction Signals

- **Subagent termination and success verification** need tighter ground-truth alignment; current `GOAL` success labels can mask truncation or failure.
- **Component-level behavioral evaluations** are becoming a first-class alignment requirement, moving beyond end-to-end benchmarks.
- **Structured context retrieval** (AST-aware reads, codebase mapping) is being actively explored to improve long-context reasoning efficiency.
- **Tool selection and context compression** are emerging as core reasoning problems, especially with large tool sets and noisy shell outputs.
- **Safety and self-awareness** remain active gaps: destructive command劝阻, deterministic redaction, and accurate self-knowledge are all open.

---

## 6. Technical Limitations

- **No reliable turn-limit / interruption detection**: subagents can hit `MAX_TURNS` and still report success.
- **Unbounded context injection**: shell output is currently forwarded without limits, risking context degradation.
- **Poor tool scoping**: the CLI fails when >128 tools are registered, suggesting a lack of dynamic tool selection or compression.
- **Implicit skill/subagent under-utilization**: the model rarely activates custom skills without explicit user instruction.
- **Unsafe redaction**: memory logging relies on model-based redaction rather than deterministic filters.
- **Self-knowledge gaps**: the agent can give inaccurate information about its own CLI flags, hotkeys, and execution behavior.

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

**GitHub Copilot CLI Research Digest — 2026-07-15**

---

### 1. Today’s Highlights

The most research-relevant activity centers on multimodal reliability and agent alignment: a local-core ASR routing bug is causing all bundled voice models to return empty transcriptions, and several guardrail/instruction-fidelity issues show that agent skills, permission hooks, and repository-level instructions (e.g., `AGENTS.MD`) are not being consistently respected across sessions and subagents. These patterns point to concrete gaps in multimodal orchestration, long-context instruction adherence, and post-deployment alignment.

---

### 2. Releases

- **v1.0.71-2**
  - **Agent sandboxing:** Adds the ability to *limit which built-in agents are available to tasks and subagents*. This is alignment-relevant because it provides a coarse policy layer for hierarchical agent delegation.
  - Release: [v1.0.71-2](https://github.com/github/copilot-cli/releases/tag/v1.0.71-2)

- **v1.0.71-1**
  - **MCP toolset persistence:** Persists GitHub MCP toolset/tool config via `settings.json` (`githubMcpToolsets`, `githubMcpTools`, etc.). Relevant to tool-grounding and alignment, since persistent tool configuration affects which tools an agent can invoke.
  - Release: [v1.0.71-1](https://github.com/github/copilot-cli/releases/tag/v1.0.71-1)

---

### 3. Research-Relevant Issues

| Issue | Why it matters |
|-------|---------------|
| **#4024 — Voice mode: all bundled ASR models fail silently; MultiModalProcessor routing bug for `nemotron_speech` (RNNT) in Foundry Local Core** | Directly affects multimodal reasoning/speech integration. All three local ASR models return empty transcriptions because of a routing bug in the multimodal processor. Signals a need for more robust local multimodal model routing and silent-failure diagnostics. [Issue #4024](https://github.com/github/copilot-cli/issues/4024) |
| **#443 — Feature Request: Built-in PDF Reading Support** | Relevant to OCR and long-context reasoning: users need native PDF ingestion for academic papers and technical documentation, but the CLI currently requires external tools. [Issue #443](https://github.com/github/copilot-cli/issues/443) |
| **#4097 — `apply_patch` stores deleted binary in session history, exceeding CAPI 5 MB limit** | A long-context management failure: binary diffs persist in conversation history, bloating context and breaking subsequent requests. Highlights the need for better context compaction and diff filtering. [Issue #4097](https://github.com/github/copilot-cli/issues/4097) |
| **#1896 — Agent wrote then executed its own stale written instructions (`plan.md`)** | Hallucination / instruction-drift case: a stale plan file written in an earlier session influenced a later, unrelated task. Shows risk of persistent agent artifacts and self-referential execution. [Issue #1896](https://github.com/github/copilot-cli/issues/1896) |
| **#4123 — Copilot CLI ignores `AGENTS.MD`** | Instruction-fidelity / alignment issue: repository-level agent instructions are reportedly ignored, undermining intended behavior steering. [Issue #4123](https://github.com/github/copilot-cli/issues/4123) |
| **#4122 — Subagents resolve relative markdown links in `.agent.md` against cwd instead of the agent file’s directory** | A context-loading bug for agent instructions and supporting documentation; breaks linked prompt/docs loading for subagents and can degrade reasoning quality. [Issue #4122](https://github.com/github/copilot-cli/issues/4122) |
| **#3699 — Agent Skills `allowed-tools` frontmatter specs not respected in non-interactive mode** | Post-training alignment / policy enforcement gap: tool-allow lists defined in skill frontmatter are bypassed in non-interactive runs, enabling unintended tool use. [Issue #3699](https://github.com/github/copilot-cli/issues/3699) |
| **#3874 — `preToolUse` agent hook denial does not work** | Guardrail failure: a hook intended to deny all tool calls is ineffective, indicating that runtime permission/policy hooks can be circumvented. [Issue #3874](https://github.com/github/copilot-cli/issues/3874) |
| **#3590 — `PreToolUse` hook `permissionDecision: "ask"` auto-approved by TUI** | Another guardrail failure: a hook explicitly requesting user approval is auto-approved, weakening human-in-the-loop alignment. [Issue #3590](https://github.com/github/copilot-cli/issues/3590) |
| **#3120 — Autopilot on PowerShell does not ask for permission and keeps looping forever** | Autonomous-agent reliability / hallucination-like behavior: the agent repeatedly fails permission checks and engages in self-referential “discussion” without completing the task. [Issue #3120](https://github.com/github/copilot-cli/issues/3120) |

---

### 4. Research-Relevant PRs

No PRs were updated in the last 24 hours in the provided dataset.

---

### 5. Research Direction Signals

- **Local multimodal reliability:** The ASR silent-failure issue suggests that routing, model loading, and error surfacing for on-device multimodal models still need investment.
- **Document and OCR integration:** The PDF-reading feature request indicates demand for native document understanding, which ties OCR, layout parsing, and long-context ingestion together.
- **Long-context hygiene:** Cases where binary diffs or stale files persist in context point to the need for smarter context filtering, compaction, and relevance scoring.
- **Instruction fidelity and stale-context mitigation:** `AGENTS.MD` being ignored, relative doc links breaking, and stale `plan.md` artifacts influencing later tasks show that instruction grounding across sessions is fragile.
- **Hierarchical agent alignment:** Subagent delegation, non-interactive mode, and permission hooks are all showing policy-enforcement gaps, signaling a need for stronger, mode-aware guardrails.

---

### 6. Technical Limitations

- **Silent multimodal failures:** Local ASR models can fail without informative errors, making debugging and trust evaluation difficult.
- **No native PDF/OCR pipeline:** Document-based workflows still rely on external tools, limiting the CLI’s usefulness for paper/documentation-heavy tasks.
- **Context bloat from tool outputs:** Binary file deletions and large diffs are retained in conversation history, risking context-window overflow and degraded downstream reasoning.
- **Inconsistent guardrail enforcement:** Permission hooks and `allowed-tools` policies behave differently across interactive, non-interactive, and subagent contexts.
- **Instruction-loading fragility:** Repository-level agent instructions and linked documentation may not load or resolve correctly, especially for subagents.
- **Autonomous looping and self-reference:** Agents can enter permission-failure loops and generate self-referential commentary rather than asking for clarification or stopping.
- **Limited persistent policy controls:** Users cannot persist explicit command/tool *deny* rules, only allow-style approvals.

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

**Research Focus Digest for Kimi Code CLI**  
*Date: 2026-07-15 | Source: github.com/MoonshotAI/kimi-cli*

---

### 1. Today's Highlights

Today’s updates center on low-level reasoning control and long-context completion budgeting in the CLI. Three merged pull requests refine how the client passes reasoning-effort parameters, preserve empty `reasoning_content` fields to avoid assistant-message failures, and switch from a fixed 32k cap to a dynamic completion budget based on the remaining context window. These changes directly affect long-context reasoning reliability, reasoning-trace fidelity, and post-training alignment of inference-time behavior.

---

### 2. Releases

No new releases in the last 24 hours.

---

### 3. Research-Relevant Issues

No updated issues in this batch directly relate to long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, or hallucination mitigation. The two active issues are operational/product bugs:

- **#2318** — organization TPD rate-limit calculation ([github.com/MoonshotAI/kimi-cli/issues/2318](https://github.com/MoonshotAI/kimi-cli/issues/2318)) — billing/rate-limit issue, outside research scope.
- **#2496** — corrupted output when resuming a forked session ([github.com/MoonshotAI/kimi-cli/issues/2496](https://github.com/MoonshotAI/kimi-cli/issues/2496)) — session-state/UI bug, not a research-relevant reasoning or multimodal issue.

---

### 4. Research-Relevant PRs

| # | Title | Why it matters |
|---|-------|----------------|
| **#2499** | `fix(kosong): stop sending Kimi reasoning effort implicitly`  ([PR #2499](https://github.com/MoonshotAI/kimi-cli/pull/2499)) | Configures Kimi thinking via `thinking.type` without implicitly serializing the legacy `reasoning_effort` parameter. Keeps caller-provided reasoning effort as independent provider state, avoiding implicit clamping or reverse mapping. This improves the reliability of inference-time reasoning control, a post-training/alignment-relevant knob. |
| **#2498** | `fix(kosong): preserve empty-string reasoning_content as ThinkPart`  ([PR #2498](https://github.com/MoonshotAI/kimi-cli/pull/2498)) | Ensures empty-string `reasoning_content` is retained as a `ThinkPart`, preventing `400` errors when `thinking.keep=all` requires reasoning content on every assistant message. This is a reasoning-trace fidelity fix that helps maintain consistent chain-of-thought or “thinking” state across turns. |
| **#2494** | `fix(kimi): use remaining context for completion budget`  ([PR #2494](https://github.com/MoonshotAI/kimi-cli/pull/2494)) | Replaces the fixed 32k provider cap with the remaining model context window as the default completion budget for Kimi requests. Directly improves long-context handling by making token budgeting context-aware rather than hard-coded. |

---

### 5. Research Direction Signals

Emerging needs reflected in today’s changes:

- **Explicit reasoning APIs**: The move away from implicit `reasoning_effort` mapping suggests a push toward cleaner, provider-native control of thinking/reasoning effort at inference time.
- **Reasoning-trace robustness**: Live-session failures around missing `reasoning_content` highlight the need for clients to robustly preserve every reasoning token, even empty ones, during multi-turn reasoning workflows.
- **Dynamic long-context budgets**: Static output caps (e.g., 32k) are being replaced by context-window-aware limits, signaling a priority on efficient long-context utilization.

---

### 6. Technical Limitations

Recurring gaps and limitations visible in the data:

- **Fixed completion caps**: A hard-coded 32k provider cap was still the default for Kimi completion budgets until now, suggesting prior suboptimal use of available long-context windows.
- **Implicit parameter leakage**: The legacy `reasoning_effort` parameter was being serialized implicitly, causing divergence between caller intent and provider behavior; full separation of thinking controls is still being refined.
- **Fragile reasoning-content preservation**: Multi-turn assistant messages can fail when `reasoning_content` is missing or represented as empty strings, indicating that reasoning-trace lifecycle management is not yet fully robust.

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

# OpenCode Research Digest — 2026-07-15

**Focus areas:** long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, hallucination mitigation.

## 1. Today’s Highlights

Today’s activity centers on **reasoning transparency** and **agent-control reliability**: a user-reported regression hides model reasoning thoughts even after the backend fix, while a PR changes how step-limit instructions are injected into the conversation to reduce assistant-side manipulation. **Long-context management** also gets attention with a new one-click context-compaction button and its corresponding UI PR. Several tool-calling reliability fixes round out the reliability work.

## 2. Releases

No research-relevant releases.  
- `v1.18.1` and `v1.18.0` are Desktop UI/layout releases (layout migration, onboarding, settings spacing) and do not touch model reasoning, multimodal, or alignment systems.

## 3. Research-Relevant Issues

| Issue | Title | Research Significance |
|-------|-------|------------------------|
| [#36877](https://github.com/anomalyco/opencode/issues/36877) | Reasoning thoughts not being shown | Directly affects **reasoning introspection** and **hallucination mitigation**: GPT 5.6 reasoning thoughts were emitted as HTML comments and are still missing in OpenCode, blocking users from auditing model reasoning chains. |
| [#36921](https://github.com/anomalyco/opencode/issues/36921) | One-click context compaction button | Supports **long-context reasoning** by making manual context compaction accessible from the UI, reducing context-overflow failures and improving session coherence. |
| [#12472](https://github.com/anomalyco/opencode/issues/12472) | Native Claude Code hooks compatibility (PreToolUse, PostToolUse, Stop) | Relevant to **post-training alignment** and safe agent execution: hooks enable human-in-the-loop intervention before/after tool use and on stop events. |
| [#36706](https://github.com/anomalyco/opencode/issues/36706) | Task tool (subagent) broken after large permission prompt | A **reliability/alignment** gap: very large subagent outputs can break the permission flow and corrupt the task tool, undermining hierarchical agent workflows. |
| [#32747](https://github.com/anomalyco/opencode/issues/32747) | @ file mentions do not include files created after startup | A **grounding/hallucination** issue: stale file-search state means agents can miss newly created files, increasing the risk of acting on incomplete context. |
| [#31972](https://github.com/anomalyco/opencode/issues/31972) | New Layout cannot switch Plan/Build | Affects **planning/reasoning modes**: regression removes the Plan/Build toggle in the new layout, breaking explicit agent-control workflows. |
| [#28957](https://github.com/anomalyco/opencode/issues/28957) | Upstream idle timeout exceeded with “writing-plans” skill | A **long-running reasoning/planning** reliability issue: the `writing-plans` skill triggers upstream timeouts, pointing to session-lifetime and infrastructure gaps for long-horizon tasks. |

## 4. Research-Relevant PRs

| PR | Title | Technical Contribution |
|----|-------|------------------------|
| [#36894](https://github.com/anomalyco/opencode/pull/36894) | `fix(core): expand reasoning option variants` | Expands model reasoning-effort and budget mappings across providers, adds conditional toggle variants (`none`/`thinking` or `none`/`high`/`max`), and clamps generated budgets to model output limits. |
| [#36970](https://github.com/anomalyco/opencode/pull/36970) | `fix: send max-steps instruction as user message, not assistant` | Changes the step-cap wrap-up prompt from an assistant-message append to a user-message append, reducing the assistant’s ability to self-influence the termination signal. |
| [#36964](https://github.com/anomalyco/opencode/pull/36964) | `feat(app): add one-click context compaction button` | Implements UI-triggered context compaction, improving **long-context** usability and helping avoid context-window truncation. |
| [#35405](https://github.com/anomalyco/opencode/pull/35405) | `fix(llm): unflatten Gemini tool call args with dot-bracket notation` | Fixes flattened tool-call argument parsing for Gemini, improving **tool-use reliability** and reducing execution errors from malformed args. |
| [#33160](https://github.com/anomalyco/opencode/pull/33160) | `fix(mcp): prevent null parameters in MCP tool calls for OpenAI-compatible providers` | Prevents `null` MCP parameter values when schemas lack explicit types, improving **tool-call correctness** and reducing silent failures. |

## 5. Research Direction Signals

- **Reasoning introspection:** Users need reliable display of model reasoning thoughts; current parsing/display pipeline appears brittle after provider-side changes.
- **Model-specific reasoning controls:** Expanding per-provider reasoning-effort/budget mappings is an active need as more reasoning models are added.
- **Long-context UX:** Context compaction and session-history management are becoming first-class UI concerns, not just backend optimizations.
- **Safer agent loops:** Step-limit prompts, permission handling for large outputs, and Claude-style hooks all point to demand for better **alignment and control** mechanisms.
- **Grounding and retrieval:** File-mention indexing and stale search state directly impact the agent’s ability to use fresh context, a precursor to hallucination reduction.

## 6. Technical Limitations

- **Reasoning-output rendering:** Backend fixes for reasoning thoughts do not automatically propagate through the client rendering path; end-to-end reasoning display is still fragile.
- **Context-window management:** Users still lack one-click compaction until the new UI lands; long sessions risk truncation before users can compact.
- **Permission/DB scalability:** Large subagent outputs can exceed the permission UI and leave the task tool in a broken state (`replacement_seq` column error), indicating the permission subsystem does not scale with output size.
- **Grounding latency:** `@` file mentions rely on startup-time search state and miss files created after launch, limiting real-time context awareness.
- **Plan/Build control regressions:** The new Desktop layout removes or breaks the Plan/Build switch, showing that agent-mode control surfaces are not yet stable across UI refreshes.
- **Tool-argument serialization:** Provider-specific flattened or weakly typed tool arguments continue to cause parsing failures and null-parameter bugs.

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

# Pi Research Digest — 2026-07-15

## 1. Today's Highlights
Pi's latest activity pushes on two research-relevant fronts: **long-context orchestration** and **multimodal prompts**. The Copilot provider gained GPT-5.6 long-context variants, while the `prompt` RPC is being extended to video and audio. At the same time, several fixes target reasoning-content normalization, compaction reliability, and prompt-cache/session-state management for extended turns.

## 2. Releases
- **v0.80.7** — Breaking change removes the `openai-responses` `compat.sendSessionIdHeader` flag from `models.json`. Session-affinity behavior is now controlled by `compat.sessionAffinityFormat` (`"openai"`, `"openai-nosession"`, or `"openrouter"`). This affects how OpenAI-compatible long-context sessions are routed and cached.  
  https://github.com/earendil-works/pi/releases/tag/v0.80.7

## 3. Research-Relevant Issues
- **#6624 — Add GPT-5.6 models and long-context support to GitHub Copilot** (closed, no-action)  
  Requests catalog entries for `gpt-5.6-luna/terra/sol` so Pi users can run the newest long-context models through Copilot.  
  https://github.com/earendil-works/pi/issues/6624

- **#3200 — Support video/audio content in prompt command**  
  Extends the `prompt` RPC beyond images to video/audio payloads for multimodal models such as Gemma 4 and GPT-4o.  
  https://github.com/earendil-works/pi/issues/3200

- **#6522 — openai-completions: no min floor on `max_completion_tokens`, sends 1 token → 400 Bad Request**  
  Proxy-reported context can be wrong; Pi's token accounting then sends an invalid `max_completion_tokens`, breaking long-context requests.  
  https://github.com/earendil-works/pi/issues/6522

- **#6167 — `transformMessages` + `isSameModel === false` thinking block normalization interacts poorly with `requiresReasoningContentOnAssistantMessages`**  
  Switching models inlines or strips reasoning/thinking blocks incorrectly, affecting preservation of reasoning chains.  
  https://github.com/earendil-works/pi/issues/6167

- **#6621 — Prevent accidental cache invalidation due to dynamic system prompt**  
  Non-deterministic system prompts break provider-side KV/prompt caches, hurting long-context prefill efficiency and cost.  
  https://github.com/earendil-works/pi/issues/6621

- **#6374 — model catalog fixes**  


</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

# Qwen Code Research Digest — 2026-07-15

## 1. Today’s Highlights
The last 24 hours on Qwen Code show a clear research-relevant cluster around **long-context reliability**, **vision/multimodal robustness**, and **safe autonomous tool execution**. Key signals include fixes for unbounded session memory, stale memory indices, and PDF vision bridge edge cases, plus hardening of trust/permission models for MCP and file access. Several PRs also target reasoning reliability—sanitizing malformed thinking tags, rolling back failed max-token continuations, and handling unsigned Claude thinking blocks.

## 2. Releases
- **

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

**DeepSeek TUI / CodeWhale Digest — 2026-07-15**  
*Focus areas: long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, hallucination mitigation*

---

### 1. Today’s Highlights
No new release appeared in the last 24h. The most relevant updates are the new config-level control over context compaction and the “seam” manager for long-context models (PR #3780), and an open report that the agent ignores its constitution and user-provided scripts (Issue #4032), highlighting a live instruction-following / alignment failure.

---

### 2. Releases
**None** in the last 24h.

---

### 3. Research-Relevant Issues

| # | Issue | Research Significance |
|---|-------|------------------------|
| **#4032** — Codewhale not following the constitution | The agent repeatedly writes new scripts instead of reusing co-authored user scripts and then rationalizes the deviation. This is a concrete **post-training alignment / hallucination mitigation** failure mode: the model produces and justifies non-compliant behavior.  <br>🔗 https://github.com/Hmbown/CodeWhale/issues/4032 |
| **#3765** — Expose `SeamManager.enabled` and `CompactionConfig.enabled` | Adds engine-level knobs for replacement compaction and the Flash seam manager. Directly relevant to **long-context reasoning**: users currently cannot disable mechanisms that silently reshape or drop context.  <br>🔗 https://github.com/Hmbown/CodeWhale/issues/3765 |
| **#4368** — Override kimi baseUrl, warming of exseed context limit | Custom provider endpoints trigger incorrect or unwanted context-limit warnings, pointing to gaps in **long-context window handling** across provider/model routes.  <br>🔗 https://github.com/Hmbown/CodeWhale/issues/4368 |

---

### 4. Research-Relevant Pull Requests

| # | PR | Technical Contribution |
|---|-----|------------------------|
| **#3780** — [codex] expose context compaction gates | Introduces `[compaction].enabled` and `[seam_manager].enabled` switches in `config.toml`, letting users disable replacement compaction and the Flash seam manager. Improves **long-context reproducibility, transparency, and user control**.  <br>🔗 https://github.com/Hmbown/CodeWhale/pull/3780 |

---

### 5. Research Direction Signals
- **Constitutional / instruction adherence:** Agentic tool use still overrides user-provided artifacts and self-justifies, indicating a need for stronger post-training alignment or runtime constraint enforcement.
- **Long-context controllability:** Context compaction and seam management were hard-coded on; the community is asking for explicit, tunable gates and clearer behavior around context limits.
- **Provider-specific context handling:** Custom base URLs expose mismatches in context-window detection and warning logic, suggesting long-context reasoning infrastructure must be robust to provider routing differences.

---

### 6. Technical Limitations
- **No enforced constitution:** The model can ignore user rules and co-authored scripts without being blocked or corrected.
- **Hard-coded long-context mechanisms:** Compaction and seam management lacked user-facing disable switches until the pending fix in PR #3780.
- **Context-limit warnings are brittle:** Custom provider endpoints can produce incorrect “exseed context limit” warnings, limiting reliable long-context usage outside standard routes.
- **Tool-use traceability:** Exec-stream and terminal lifecycle metadata are still incomplete (Issues #4356 / #4355), which limits replay and causal analysis of agent reasoning failures.

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*