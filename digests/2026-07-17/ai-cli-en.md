# AI CLI Tools Community Digest 2026-07-17

> Generated: 2026-07-17 00:24 UTC | Tools covered: 9

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

# Cross-Tool Research Analysis: AI CLI Assistants — 2026-07-17

## 1. Ecosystem Overview

The AI CLI coding-assistant space is shifting from raw model capability to **operational reliability**: context governance, turn-level state integrity, multi-agent lifecycle, and safety alignment. Today’s activity across Claude Code, OpenAI Codex, GitHub Copilot CLI, Gemini CLI, Kimi Code CLI, and OpenCode shows that long-context agents are hitting predictable engineering boundaries—log bloat, dropped assistant text, process leaks, tool-schema drift, and miscalibrated refusals. Releases are uneven, but the issue and PR volume is heavily concentrated on **trust, transparency, and long-horizon reasoning stability**.

---

## 2. Activity Comparison

| Tool | Research-Relevant Issues (count) | Research-Relevant PRs (count) | Release Status (24h) |
|---|---|---|---|
| **Claude Code** | 8 (#77798, #75034, #78272, #78300, #78273, #65662, #32913, #78313) | 3 (#16680, #58646, #78057) | None |
| **OpenAI Codex** | 8 (#24948, #19197, #33575, #33681, #33709, #32997, #30408, #24275) | 11 (#31529, #33683, #33656, #33659, #33657, #33658, #33665, #33684, #33633, #33636, #33680) | Security-patch bump only (not research-relevant) |
| **Gemini CLI** | 2 (#22323, #22745) | 1 highlighted (core-agent PR; no number provided) | v0.52.0-preview.0 |
| **GitHub Copilot CLI** | 4+ (#3762, #3481, #4097, #4138)¹ | 0 listed | v1.0.72-0, v1.0.71 |
| **Kimi Code CLI** | 1 (#2501) | 0 listed | v1.49.0 / kosong 0.55.0 |
| **OpenCode** | 4 (#37372, #37323, #36318, #37338) | 0 listed | None (research-relevant) |
| **Pi / Qwen Code / DeepSeek TUI** | Data unavailable | Data unavailable | Data unavailable |

¹Copilot digest was truncated; at least four issues were visible.

---

## 3. Shared Feature Directions

### Long-context governance and compression
- **Claude Code**: assistant text blocks dropped before `tool_use` / `AskUserQuestion`, misclassification of long text as thinking blocks.
- **OpenAI Codex**: session logs reaching 700 MB–2 GB, SQLite/WAL bloat, pre-rollover auto-compaction fallback.
- **GitHub Copilot CLI**: `contextTier` ignored on startup/subagent dispatch, deleted binaries inflating history, silent compaction hangs.
- **Kimi Code CLI**: completion budget now keyed to *remaining* context.
- **OpenCode**: request for GPT-5.6 prompt-caching defaults.
- **Gemini CLI**: AST-aware file reads proposed to reduce misaligned reads.

### Multi-agent / sub-agent lifecycle reliability
- **Claude Code**: subagents hang on first tool call.
- **OpenAI Codex**: orphaned subagents, role persistence on reload, process leaks.
- **Gemini CLI**: subagent reports false `GOAL` success after `MAX_TURNS`.
- **GitHub Copilot CLI**: multi-turn subagents now enabled, but lifecycle controls remain an issue.

### Turn-level state and block integrity
- **Claude Code**: assistant text disappearing from UI and transcript around tool-use turns.
- **OpenAI Codex**: active-turn environment stability, role validation after overrides.
- **Kimi Code CLI**: empty `reasoning_content` now preserved as `ThinkPart`.
- **OpenCode**: empty reasoning-only responses treated as successful completions.

### Post-training alignment and safety calibration
- **Claude Code**: over-refusal on delegated low-stakes actions, unconfirmed file overwrite.
- **OpenAI Codex**: false-positive cybersecurity rejection.
- **GitHub Copilot CLI**: scheduled prompts as steering messages for busy agents.

### Hallucination and grounding beyond factual errors
- **Claude Code**: fake system notice with a fabricated third-party billing link.
- **OpenAI Codex**: MCP tools lost when `tool_mode` changes, Computer Use skill advertised but `node_repl` tool missing.
- **Gemini CLI**: false success status after turn exhaustion.
- **OpenCode**: reasoning-only “success” with no actual output.

### Memory, provenance, and workspace-aware continuity
- **Claude Code**: recall plugin for conversation recovery, git-aware session history.
- **OpenAI Codex**: memory provenance scoping for imported resources.
- **GitHub Copilot CLI**: per-agent context tier and

---

## Per-Tool Reports

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills Highlights

> Source: [anthropics/skills](https://github.com/anthropics/skills)

⚠️ Skills summary generation failed.

---

**Claude Code Research Digest – 2026-07-17**

---

### 1. Today’s Highlights

Today’s activity is dominated by **agentic output fidelity and safety alignment** issues: several reports describe assistant text blocks disappearing from the rendered UI and transcript around tool-use turns, and one severe case shows the model emitting a fake third-party system notice. Together with a high-profile over-refusal issue and a data-loss incident, these signals point to urgent research needs in **long-context turn representation, hallucination grounding, and post-training alignment of autonomous action authorization**.

---

### 2. Releases

- **None** in the last 24h.

---

### 3. Research-Relevant Issues

- **#77798 — Fable mid-turn messages hidden; long assistant text misclassified as a thinking block**  
  *Research significance:* Long-form assistant reasoning is being rendered as invisible “thinking” blocks rather than text, which directly affects **long-context reasoning transparency**, operator oversight, and the interpretability of mid-turn planning.  
  https://github.com/anthropics/claude-code/issues/77798

- **#75034 — Assistant text blocks dropped from both UI and transcript when followed by tool_use in the same turn**  
  *Research significance:* A concrete failure of **turn-level context preservation** and **multimodal tool-interaction state tracking**. Loss of explanatory text before `AskUserQuestion` corrupts the reasoning chain available to users and downstream audit.  
  https://github.com/anthropics/claude-code/issues/75034

- **#78272 — Model emitted a fake system notice containing a third-party billing link**  
  *Research significance:* A clear **hallucination / spurious content generation** incident where the model fabricated a plausible-looking system message and external upsell URL. Highlights the need for stronger grounding, attribution, and output-constraint verification.  
  https://github.com/anthropics/claude-code/issues/78272

- **#78300 — Agent refuses explicitly delegated, authorized low-stakes actions**  
  *Research significance:* Illustrates an **over-refusal alignment** problem: post-training safety behavior appears miscalibrated to user intent and context, blocking harmless delegated actions.  
  https://github.com/anthropics/claude-code/issues/78300

- **#78273 — Claude Code overwrote existing user file without confirmation**  
  *Research significance:* An autonomous tool-use **safety/alignment** failure causing irreversible data loss. Relevant to research on **action authorization**, user-model value alignment, and fail-safe behavior for destructive tools.  
  https://github.com/anthropics/claude-code/issues/78273

- **#65662 — Assistant text before an `AskUserQuestion` dialog is not displayed**  
  *Research significance:* Same broad failure class as #75034—**multimodal assistant-user interaction** can silently drop explanatory text preceding a question, reducing clarity and user trust in model reasoning.  
  https://github.com/anthropics/claude-code/issues/65662

- **#32913 — Date/Time injection into prompts**  
  *Research significance:* Request for explicit temporal grounding in prompts, relevant to **long-context awareness** and reasoning about time-sensitive tasks.  
  https://github.com/anthropics/claude-code/issues/32913

- **#78313 — Subagents intermittently hang on their first tool call**  
  *Research significance:* A reliability gap in **multi-agent planning and tool-use execution**, affecting long-context coordination between parent and child agents.  
  https://github.com/anthropics/claude-code/issues/78313

---

### 4. Research-Relevant PRs

- **#16680 — Recall plugin for conversation context recovery**  
  *Technical contribution:* Indexes each message/response pair to recover earlier conversation context, addressing **long-context memory limitations** and reducing context-loss failures.  
  https://github.com/anthropics/claude-code/pull/16680

- **#58646 — git-aware-history: fix session fragmentation across git worktrees**  
  *Technical contribution:* Makes session history persistent across git worktrees, improving **long-context continuity** and repository-wide memory for resumed sessions.  
  https://github.com/anthropics/claude-code/pull/58646

- **#78057 — Flag Python `exec()` as a code-injection sink**  
  *Technical contribution:* Extends security guidance to treat Python `exec()` like `eval()`, reducing the risk of model-suggested code execution paths. Relevant to **post-training safety alignment** and **harmful output mitigation**.  
  https://github.com/anthropics/claude-code/pull/78057

---

### 5. Research Direction Signals

- **Turn-level context integrity is fragile.** Multiple reports of dropped or misclassified assistant text around tool-use turns suggest a need for more robust **long-context state machines** and transcript preservation.
- **Hallucination surfaces are evolving beyond factual errors.** Fake system notices and unrequested file overwrites indicate a need for **output attribution**, **grounding checks**, and **tool-use authorization boundaries**.
- **Post-training alignment is miscalibrated in both directions.** Over-refusal on safe delegated actions and under-refusal on destructive writes show the need for **context-aware safety calibration** and **user-intent modeling**.
- **Context recovery and workspace-aware memory are becoming first-class concerns.** Plugins for recall and git-aware history signal research interest in **external memory / retrieval augmentation** for long-context agents.

---

### 6. Technical Limitations

- **Assistant output capture and block classification are unreliable when tool_use follows text in the same turn**, leading to lost explanations and incomplete transcripts.
- **Multimodal/agent interaction loops** can silently drop content, degrading operator oversight and the auditability of reasoning.
- **Autonomous tool use lacks sufficient guardrails** for destructive actions, as shown by an unconfirmed file overwrite.
- **Model-generated system-like content can be convincing but fabricated**, revealing gaps in hallucination mitigation for procedural/status messages.
- **Safety policies appear to over-refuse** on low-stakes, explicitly authorized actions, indicating poor risk-context calibration.

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

**OpenAI Codex Research Digest – 2026-07-17**  
*Focus: long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, hallucination mitigation*

---

### 1. Today’s Highlights

The most research-relevant activity today is in **long-context/session management** and **agent reasoning/tool grounding**. A new pre-rollover auto-compaction fallback and several memory-provenance PRs aim to keep agent context manageable, while agent-role validation and stricter image-output policy improve the reliability of tool-augmented and multimodal reasoning.

---

### 2. Releases

_No releases today directly affect the targeted research areas; the only 24h release was a security-patch bump for dangerous-command detection._

---

### 3. Research-Relevant Issues

| Issue | Why it matters |
|-------|----------------|
| **#24948** – Session logs grow to 700 MB–2 GB from repeated compaction history and raw tool output  <br> [openai/codex/issues/24948](https://github.com/openai/codex/issues/24948) | Directly impacts **long-context reasoning** cost and latency; suggests compaction is retaining too much raw material rather than a compacted summary. |
| **#19197** – Persistent orphaned subagents, missing lifecycle controls, and eventual session freezes  <br> [openai/codex/issues/19197](https://github.com/openai/codex/issues/19197) | A multi-agent runtime reliability issue; unbounded subagent state can corrupt or freeze long-running reasoning sessions. |
| **#33575** – `gpt-5.6-sol` loses all MCP tools after runtime metadata changes `tool_mode` to `direct`  <br> [openai/codex/issues/33575](https://github.com/openai/codex/issues/33575) | Tool-set grounding becomes inconsistent at runtime; risks **hallucinated tool availability** and broken tool-augmented reasoning chains. |
| **#33681** – Computer Use skill loads but required `node_repl` tool is not exposed  <br> [openai/codex/issues/33681](https://github.com/openai/codex/issues/33681) | Multimodal/computer-use agent capabilities mismatch: the high-level skill is advertised but the underlying action tool is missing, pointing to **vision-language-to-action grounding** gaps. |
| **#33709** – False-positive cybersecurity safety check  <br> [openai/codex/issues/33709](https://github.com/openai/codex/issues/33709) | Example of an over-refusal / safety **hallucination** where benign commands are rejected; relevant to reward hacking and alignment of safety classifiers. |
| **#32997** – Codex desktop task appears running but is stuck; duplicate MCP/app child processes accumulate  <br> [openai/codex/issues/32997](https://github.com/openai/codex/issues/32997) | Highlights lifecycle and state-synchronization failures in multi-process agent runtimes. |
| **#30408** – MCP server processes leak (9+ GB RSS)  <br> [openai/codex/issues/30408](https://github.com/openai/codex/issues/30408) | Unbounded process growth degrades long-context/agent sessions; signals need for resource-aware tool-server lifecycle management. |
| **#24275** – `logs_2.sqlite` / WAL rapidly grows during normal active use  <br> [openai/codex/issues/24275](https://github.com/openai/codex/issues/24275) | Another indicator of context-state bloat; long conversations produce database growth that correlates with UI slowdown. |

---

### 4. Research-Relevant Pull Requests

| PR | Technical contribution |
|----|------------------------|
| **#31529** – core: add pre-rollover auto-compaction fallback  <br> [openai/codex/pull/31529](https://github.com/openai/codex/pull/31529) | Adds a structured fallback request before automatic compaction rollover, letting extensions contribute a developer prompt for a restricted summarization step. Directly targets **long-context compression** and reasoning continuity. |
| **#33683** – Preserve scope and provenance for imported agent memory  <br> [openai/codex/pull/33683](https://github.com/openai/codex/pull/33683) | Records imported resources via `extension_resource_files`, retains source frontmatter, and scopes project-specific knowledge. Improves **memory provenance** and reduces cross-project contamination. |
| **#33656** – Validate reasoning effort after applying spawn roles  <br> [openai/codex/pull/33656](https://github.com/openai/codex/pull/33656) | Closes a validation gap where agent roles override model/reasoning effort post-validation; relevant to **reasoning consistency** and alignment of role-based behavior. |
| **#33659** – Require data URLs for code-mode image output  <br> [openai/codex/pull/33659](https://github.com/openai/codex/pull/33659) | Restricts image output to `data:` URLs, rejecting remote HTTP images and malformed URLs. Tightens **multimodal output grounding** and mitigates external-image injection risks. |
| **#33657** – Restore agent roles when reloading v2 sub-agents  <br> [openai/codex/pull/33657](https://github.com/openai/codex/pull/33657) | Ensures durable sub-agents recover their configured role after lazy reload, preserving **role-consistent reasoning** across long sessions. |
| **#33658** – Keep active-turn environments stable across settings updates  <br> [openai/codex/pull/33658](https://github.com/openai/codex/pull/33658) | Prevents in-progress turns from inheriting mid-turn environment changes, improving **contextual stability** for deferred execution. |
| **#33665** – Refresh step world state for all sessions  <br> [openai/codex/pull/33665](https://github.com/openai/codex/pull/33665) | Propagates working-directory/`AGENTS.md` changes into the model’s context even when deferred execution is disabled, keeping **world state** synchronized. |
| **#33684** – Extract TUI approval request payloads into structs  <br> [openai/codex/pull/33684](https://github.com/openai/codex/pull/33684) | Refactors command, permission, patch, and MCP approval payloads into dedicated structs; supports more reliable **human-in-the-loop oversight** and policy enforcement. |
| **#33633 / #33636** – Clarify when to wait for starting environments  <br> [openai/codex/pull/33633](https://github.com/openai/codex/pull/33633) · [openai/codex/pull/33636](https://github.com/openai/codex/pull/33636) | Adds developer-prompt guidance to reduce unnecessary blocking on environment startup; a small **post-training alignment / tool-use instruction** improvement. |
| **#33680** – Reword the `apply_patch` tool description  <br> [openai/codex/pull/33680](https://github.com/openai/codex/pull/33680) | Tool-description refinement that can change model behavior; relevant to **tool-prompt alignment** and hallucination reduction. |

---

### 5. Research Direction Signals

- **Long-context compression and compaction:** Multiple issues and PRs show that as sessions lengthen, log/DB bloat and compaction quality become bottlenecks. Better summarization-aware compaction is a clear need.
- **Reliable multi-agent orchestration:** Sub-agent lifecycle, role persistence on reload, and orphaned process management are emerging as prerequisites for trustworthy multi-agent reasoning.
- **Dynamic tool grounding:** MCP tool availability changes at runtime, and Computer Use skill/tool mismatches indicate that tool schema synchronization and action grounding remain unsolved.
- **Multimodal output safety:** Enforcing local data URLs for generated images suggests a push toward self-contained, auditable multimodal outputs rather than remote references.
- **Reasoning governance:** Validating reasoning effort after role overrides and structuring approval flows signal work toward controllable, policy-aligned reasoning.

---

### 6. Technical Limitations

- **Context-state bloat:** SQLite logs, WAL files, and session logs grow rapidly, suggesting compaction does not yet keep pace with conversation and tool-output volume.
- **Process lifecycle leaks:** MCP servers, git probes, and sub-agents are repeatedly spawned and not always cleaned up, leading to memory/RSS growth and session freezes.
- **Runtime tool-schema drift:** Models can lose MCP tools or be presented with skills whose underlying tools are not exposed, producing groundedness failures.
- **Over-refusal / safety false positives:** Benign commands are occasionally rejected, indicating safety classifier calibration remains a source of user-facing hallucination.
- **Role and environment consistency across long sessions:** Agent roles and environment settings can be lost or altered mid-session when deferred execution or lazy reload paths are exercised.

---

*Digest generated from github.com/openai/codex activity for 2026-07-17.*

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

**Gemini CLI Research Digest — 2026-07-17**  
*Focus: long-context reasoning, OCR/HMER & multimodal reasoning, post-training alignment, hallucination mitigation*

---

### 1. Today’s Highlights

The most research-relevant development is a core-agent PR that caps recursive reasoning to 15 turns per user request, directly addressing long-context reasoning stability and resource exhaustion. Several previously filed issues also resurfaced and are highly relevant to hallucination mitigation and alignment: subagents falsely report success after hitting `MAX_TURNS`, agents can run without expected permission checks, and the model lacks reliable self-awareness of its own CLI flags and capabilities. There are no direct updates on OCR, HMER, or vision-language multimodal reasoning in the last 24 hours.

---

### 2. Releases

- **v0.52.0-preview.0** — Excludes transient CI configuration files from workspace context. This is a small context-quality improvement that reduces noisy or misleading tokens in the reasoning context.  
  https://github.com/google-gemini/gemini-cli/releases/tag/v0.52.0-preview.0

---

### 3. Research-Relevant Issues

- **#22323 — Subagent recovery after `MAX_TURNS` is reported as `GOAL` success, hiding interruption**  
  A subagent reports `status: "success"` and `Termination Reason: "GOAL"` even when it actually exhausted its turn budget. This is a clear example of **termination/success hallucination** and raises questions about how final turn signals are translated into agent status.  
  https://github.com/google-gemini/gemini-cli/issues/22323

- **#22745 — Assess the impact of AST-aware file reads, search, and mapping**  
  Proposes AST-aware tools to read exact method bounds, reduce misaligned reads, and navigate code more precisely. Directly relevant to **long-context reasoning** and **context compression** in large codebases.  
  https://github.com/google-gemini/gemini-cli/issues

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

# GitHub Copilot CLI Research Digest — 2026-07-17

## 1. Today's Highlights
The v1.0.72-0 release continues to push agentic reasoning and multi-turn orchestration, while the issue backlog surfaces acute research-relevant gaps: silent multimodal ASR failures, long-context tier settings that are ignored at startup/subagent dispatch, and session-wedging caused by oversized attachments or invalid reasoning-block signatures. These signals point to urgent needs in robust context governance, multimodal input handling, and reasoning-output verification.

---

## 2. Releases

### v1.0.72-0
- **Multi-turn subagents are now always enabled** — follow-up messages can be sent to running agents. Directly supports long-horizon, multi-turn reasoning and agent collaboration.
- **Tool search enabled for Claude Haiku 4.5+** — expands model-driven tool discovery for lightweight reasoning models.
- **Scheduled prompts delivered as steering messages when the agent is busy** — improves real-time alignment / steering of agent behavior without interrupting ongoing work.

### v1.0.71 (2026-07-16)
- **`copilot -p --autopilot` timeout handling fixed** — background shells/agents that outlive a turn now honor `COPILOT_TASK_WAIT_TIMEOUT_SECONDS`, improving reliability of long-running agentic workflows.
- **`/subagents` model picker preserves per-agent reasoning effort and context tier** — helps maintain consistent reasoning-effort and long-context configuration across subagents.

🔗 [github.com/github/copilot-cli/releases](https://github.com/github/copilot-cli/releases)

---

## 3. Research-Relevant Issues

### Long-Context Reasoning & Context Memory

1. **#3762 — `contextTier` config option does nothing**  
   [github.com/github/copilot-cli/issues/3762](https://github.com/github/copilot-cli/issues/3762)  
   *Significance:* Reports that the `contextTier` setting does not affect the launched agent or dispatched subagents until the model picker is manually used. Highlights a gap in policy-based long-context activation and propagation.

2. **#3481 — `contextTier=long_context` is not applied on startup / no CLI flag**  
   [github.com/github/copilot-cli/issues/3481](https://github.com/github/copilot-cli/issues/3481)  
   *Significance:* Non-interactive sessions ignore the configured long-context tier. Research need: deterministic, CLI-explicit long-context bootstrapping and reproducible context-window allocation.

3. **#4097 — `apply_patch` stores deleted binary in session history, exceeding CAPI 5 MB limit**  
   [github.com/github/copilot-cli/issues/4097](https://github.com/github/copilot-cli/issues/4097)  
   *Significance:* Deleted binaries are persisted as textual diffs in conversation history, causing repeated 5 MB limit failures. A clear case for context-bloat management, history summarization, and differential-storage strategies.

4. **#4138 — Session resume triggers background compaction that fails silently and hangs**  
   [github.com/github/copilot-cli/issues/4138](https://github.com/github/copilot-cli/issues/4138)  
   *Significance:* Long-context compaction on resume has no retry or fallback when the model returns an empty response. Critical for robust

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

# Research Digest — Kimi Code CLI (2026-07-17)

## 1. Today's Highlights
The 1.49.0 release includes two reasoning- and context-relevant fixes: completion token budget now uses remaining context, and empty-string `reasoning_content` is preserved as a `ThinkPart`. Separately, a feature request for direct TUI control of Reasoning Level / Thinking Effort signals growing interest in controllable inference-time reasoning.

## 2. Releases
- **kimi-cli 1.49.0 / kosong 0.55.0**
  - `fix(kimi): use remaining context for completion budget` — improves long-context utilization by budgeting completion tokens against *remaining* context rather than total context.
  - `fix(kosong): preserve empty-string reasoning_content as ThinkPart` — ensures reasoning traces are correctly represented even when empty, relevant to reasoning-content parsing and downstream reliability.
  - https://github.com/MoonshotAI/kimi-cli/releases/tag/1.49.0

## 3. Research-Relevant Issues
- **#2501 [enhancement] Quick switching Reasoning Level / Thinking Effort in TUI main interface**
  - Author: remacheybn408-boop | Open | Updated: 2026-07-16
  - Requests a direct TUI shortcut to switch Reasoning Level / Thinking Effort without entering the `/model` submenu. **Research significance:** relates to inference-time reasoning control, user-aligned reasoning effort, and dynamic adjustment of thinking depth at deployment.
  - https://github.com/MoonshotAI/kimi-cli/issues/2501

## 4. Research-Relevant PRs
- No PRs updated in the last 24h directly address long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, or hallucination mitigation. The visible PRs focus on telemetry alignment, install-time error messages, and release tooling.

## 5. Research Direction Signals
1. **Controllable reasoning effort**: Users want faster access to Reasoning Level / Thinking Effort controls, indicating demand for tunable inference-time compute and user-steered reasoning depth.
2. **Context budget optimization**: The 1.49.0 fix suggests ongoing work to improve token allocation and reliability in long-context windows.
3. **Robust reasoning-trace handling**: Preserving empty `reasoning_content` as `ThinkPart` indicates attention to consistency of reasoning traces, which matters for chain-of-thought verification and hallucination mitigation.

## 6. Technical Limitations
1. **Reasoning control UX gap**: Switching reasoning intensity currently requires navigating a submenu, interrupting workflow during long-prompt or mid-conversation sessions.
2. **Context budget fragility**: Prior behavior of not using remaining context for completion budget could lead to truncated outputs or context overflow in long-context sessions.
3. **Reasoning trace edge cases**: Empty-string reasoning content was previously not handled consistently, potentially breaking downstream parsing of model thinking.

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

**OpenCode Research Digest — 2026-07-17**

## 1. Today’s Highlights

The most research-relevant signals today are a V2 bug that silently accepts empty reasoning-only responses as successful completions, the V2 `read` tool’s inability to handle PDFs, and a merged system-prompt fix that prevents token-minimization rules from degrading coding reliability. Together these point to active work on reasoning integrity, multimodal document handling, long-context efficiency, and prompt-level alignment.

## 2. Releases

No releases in the last 24h are directly relevant to long-context reasoning, OCR/HMER, multimodal reasoning, post-training alignment, or hallucination mitigation. *(v1.18.3 contains only UI and startup fixes.)*

## 3. Research-Relevant Issues

| # | Issue | Why it matters |
|---|-------|----------------|
| [#37372](https://github.com/anomalyco/opencode/issues/37372) | **v2: empty reasoning-only response is recorded as successful completion** | A reasoning-only assistant message with no visible text or tool calls is treated as success, leaving downstream clients with neither an answer nor a detectable failure. Directly affects reasoning reliability and silent-hallucination detection. |
| [#37323](https://github.com/anomalyco/opencode/issues/37323) | **V2 read tool does not support PDFs** | PDFs are rejected as binary files, blocking multimodal document understanding and any OCR/HMER-style pipeline that needs to extract and reason over document content. |
| [#36318](https://github.com/anomalyco/opencode/issues/36318) | **Support GPT-5.6 prompt caching defaults** | Prompt caching is a long-context efficiency primitive; missing defaults increases cost and latency for extended-context reasoning sessions. |
| [#37338](https://github.com/anomalyco/opencode/issues/37338) | **Models ignore explicit “don’t do X

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

⚠️ Summary generation failed.

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

⚠️ Summary generation failed.

</details>

---
*This digest is auto-generated by [agents-radar](https://github.com/QYQAQ/agents-radar).*