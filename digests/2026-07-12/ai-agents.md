# OpenClaw 生态日报 2026-07-12

> Issues: 461 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-12 00:24 UTC

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

## OpenClaw 项目深度报告

# OpenClaw 项目研究动态日报 — 2026-07-12

> 分析师按：今日仓库活跃度极高（Issues 461 条、PRs 500 条），但内容以**运行时、会话系统、工具输出表示与可靠性**为主。与研究主题直接相关的：  
> 1）**视觉/多模态表示**：工具输出被错误地渲染为 “(see attached image)” 占位符，导致模型无法读取原始文本；  
> 2）**推理与长上下文**：嵌入式 prompt cache 在跨 room-event/policy/Responses 边界时失效；  
> 3）**训练后对齐/可靠性**：模型判定的操作批准、凭据掩码、记忆来源信任标签、上下文溢出回退等。  
> 以下按研究相关度筛选，并略去一般产品/商业更新。

---

## 1. 今日速览

- 今日仓库活跃度**极高**：过去 24 小时 Issues 461 条（新开/活跃 225，关闭 236），PRs 500 条（待合并 233，已合并/关闭 267），并发布 `v2026.7.1-beta.5`。  
- 研究/技术层面最突出的问题是**工具输出到模型可观察文本的表示链路**：长流程中 stdout/stderr 被折叠为图像附件占位符，甚至直接返回字面字符串 `(see attached image)`，严重影响基于文本证据的推理。  
- 长上下文与推理效率方面，嵌入式 prompt cache 在多个会话边界处失效，模型可见工具清单在相邻轮次间变化 44% 以上，导致缓存命中率下降。  
- 会话状态、内存增长与并发隔离仍是稳定性主战场，数项 P0/P1 回归已有关键修复关闭。  
- 无直接的视觉语言模型训练、后训练或对齐算法论文式更新；研究信号主要体现在**系统可靠性、幻觉/输出可靠性、长上下文推理与模型输出边界**的实证问题中。

---

## 2. 版本发布

### [v2026.7.1-beta.5](https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.5)

Highlights（与研究相关部分）：

- **Conversational onboarding**：Crestodian 现在在 CLI、Web 安装和 macOS app 中运行真正的 agent-loop，支持 AI 引导的 provider 设置。  
- **模型判定的操作批准**： approvals 与 exact operations 绑定，属于 post-deployment 对齐/安全控制机制。  
- **Masked credential prompts**：凭据输入被掩码，降低 prompt-injection 泄露风险。  
- **Deterministic fallback**：无模型可用时的确定性降级。

> 本次发布未引入明确的模型训练或后训练方法变更，主要是 onboarding 与部署安全流程。

---

## 3. 项目进展

### 已关闭/合并的重要项

| 项 | 类型 | 说明 | 链接 |
|---|---|---|---|
| **#88838** | Issue | 通过 accessor seam 追踪核心 session/transcript SQLite 迁移 | [Issue](https://github.com/openclaw/openclaw/issues/88838) |
| **#86538** | Issue | Session JSONL 写锁超时阻塞主线程、cron 与 subagent 投递通道 | [Issue](https://github.com/openclaw/openclaw/issues/86538) |
| **#86572** | Issue | 将 `withOwnedSessionTranscriptWrites` ALS 作用域提升到 `agent.prompt()`，修复 vanilla-openclaw 同车道竞态 | [Issue](https://github.com/openclaw/openclaw/issues/86572) |
| **#55334** | Issue | `sessions.json` 无界增长导致 Gateway OOM，修复 `skillsSnapshot` 重复与临时会话不清理 | [Issue](https://github.com/openclaw/openclaw/issues/55334) |
| **#54155** | Issue | Gateway 内存泄漏 389 MB → 14.7 GB 的会话累积问题 | [Issue](https://github.com/openclaw/openclaw/issues/54155) |
| **#45718** | Issue | 修复 `skillsSnapshot` 与 `systemPromptReport` 每次运行累积的 session bloat | [Issue](https://github.com/openclaw/openclaw/issues/45718) |
| **#63998** | Issue | Session transcript doomloop：崩溃-重启循环使 transcript 膨胀至 OOM | [Issue](https://github.com/openclaw/openclaw/issues/63998) |
| **#66443** | Issue | 上下文溢出恢复时重复 `role=user` 消息，放大 transcript 增长 | [Issue](https://github.com/openclaw/openclaw/issues/66443) |
| **#92057** | Issue | 多 session/多 agent 负载下 Gateway 变慢或超时 | [Issue](https://github.com/openclaw/openclaw/issues/92057) |
| **#91212** | Issue | 网关重启后 delivery-recovery 在 channel transport 就绪前启动，导致消息丢失 | [Issue](https://github.com/openclaw/openclaw/issues/91212) |
| **#103332** | Issue | 在 `pi` 中无法运行 `codex/gpt5.6` 的回归已关闭 | [Issue](https://github.com/openclaw/openclaw/issues/103332) |
| **#103704** | PR | `fix(mcp)`: 为短生命周期 MCP OAuth 请求增加超时，避免无限挂起 | [PR](https://github.com/openclaw/openclaw/pull/103704) |
| **#104795** | PR | `fix(sessions)`: 通过物化缓存读取 zstd transcript 归档 | [PR](https://github.com/openclaw/openclaw/pull/104795) |

### 高价值但未合并的 PR 进展

| 项 | 说明 | 链接 |
|---|---|---|
| **#103147** | TUI 修复：在 tool calls 与恢复流之间保持 assistant 文本时序，并压缩 tool cards | [PR](https://github.com/openclaw/openclaw/pull/103147) |
| **#103706** | 修复 ANSI sanitizer 状态在跨 bash 输出块时丢失，影响模型对工具输出的可读性 | [PR](https://github.com/openclaw/openclaw/pull/103706) |
| **#102189** | 修复嵌入式 prompt cache 在跨 policy/Responses 边界时失效 | [PR](https://github.com/openclaw/openclaw/pull/102189) |
| **#104757** | 可编辑文件面板 + CodeMirror + `sessions.files.set` hash-CAS 写入 | [PR](https://github.com/openclaw/openclaw/pull/104757) |
| **#104815** | `sessions_send` 注册显式状态变化 watcher，改进 manager-agent 协调推理 | [PR](https://github.com/openclaw/openclaw/pull/104815) |

---

## 4. 社区热点

### 讨论最活跃的 Issues

- **#75 — Linux/Windows Clawdbot Apps**（110 评论，81 👍）  
  长期需求：补齐 macOS/iOS/Android 之外的桌面平台。属于平台覆盖，与研究主题关联较弱。  
  [Issue](https://github.com/openclaw/openclaw/issues/75)

- **#88838 — Track core session/transcript SQLite migration via accessor seam**（37 评论）  
  围绕会话存储核心迁移的技术讨论，已关闭。  
  [Issue](https://github.com/openclaw/openclaw/issues/88838)

- **#99241 — Tool outputs sometimes render as image attachments and become unreadable to the agent**（21 评论，P1）  
  长流程/ANSI 重的工具输出会坍缩为 `(see attached image)` 占位符，模型无法读取原始 stdout/stderr。  
  [Issue](https://github.com/openclaw/openclaw/issues/99241)

- **#104721 — All tool results return “(see attached image)” literal string instead of actual output**（11 评论，P0，回归）  
  更

---

## 横向生态对比

# 2026-07-12 个人 AI 助手 / 自主智能体开源生态横向对比

## 1. 生态全景

过去 24 小时，头部项目（OpenClaw、ZeroClaw、Hermes Agent、CoPaw）的 Issues/PRs 双双维持 50+ 的高频迭代，说明自主智能体赛道仍处于“运行时可靠性攻坚”阶段；但高活跃度并不等同于高成熟度，多个项目同时出现长上下文压缩、工具调用配对、系统提示与工具可用性不一致等结构性问题。整体生态呈现“基础模型能力逐渐收敛，Agent 系统层（会话、缓存、工具表示、安全护栏、持久记忆）成为竞争焦点”的态势。本地/开源模型（Ollama）适配、多模态触发控制、后部署对齐成为共同的技术拉力。

---

## 2. 各项目活跃度对比

| 项目 | Issues | PRs | Release | 健康度评估 |
|---|---|---|---|---|
| **OpenClaw** | 461（225 活跃/236 关闭） | 500（233 待合并/267 已合并或关闭） | ✅ v2026.7.1-beta.5 | 极高活跃；P0/P1 修复吞吐快，但长链路工具表示与 prompt cache 仍有债务 |
| **NanoBot** | 22（19 活跃/3 关闭） | 26（20 待合并/6 已合并） | ❌ 无 | 中高活跃；prompt prefix 一致性与安全审计是核心议题 |
| **Hermes Agent** | 50（41 活跃/9 关闭） | 50（48 待合并/2 关闭） | ❌ 无 | 高讨论但低落地率；对齐与推理预算议题积压 |
| **PicoClaw** | 0 | 3（2 待合并/1 关闭） | ❌ 无 | 低活跃；维护性配置/技能开关更新 |
| **NanoClaw** | 2 | 9（7 待合并/2 关闭） | ❌ 无 | 中等活跃；聚焦 Guard 护栏与持久记忆 |
| **NullClaw** | 2 | 0 | ❌ 无 | 近乎停滞；仅渠道/provider 适配类议题 |
| **IronClaw** | — | — | — | 摘要生成失败，数据不可用 |
| **LobsterAI** | 3（全部 open stale） | 1（待合并） | ✅ 2026.7.10（前两日发布） | 低活跃；陈旧积压多，交付节奏慢 |
| **TinyClaw** | 0 | 0 | ❌ 无 | 无活动 |
| **Moltis** | 0 | 1（待合并） | ❌ 无 | 维护等待期；仅 CalDAV 时间过滤修复 |
| **CoPaw** | 22 | 7（0 合并） | ❌ 无 | 高活跃；v2.0.0 回归密集，稳定性承压 |
| **ZeptoClaw** | 0 | 0 | ❌ 无 | 无活动 |
| **ZeroClaw** | 50 | 50（4 关闭/合并） | ❌ 无 | 高活跃；推理模型对齐与长上下文预算问题突出 |

---

## 3. 研究定位分析

| 项目 | 多模态推理 | 长上下文 / 推理机制 | 对齐 / 安全 / 可靠性 | 技术路线差异 |
|---|---|---|---|---|
| **OpenClaw** | 工具输出被折叠为 `(see attached image)` 占位符，影响文本证据读取（#99241、#104721） | 嵌入式 prompt cache 跨 room-event/policy/Responses 边界失效；session bloat / OOM 修复密集 | 模型判定的操作批准、凭据掩码、记忆来源信任标签、确定性降级 | **工业级参考实现**：以会话/transcript、Gateway、缓存、审批运行时为中心 |
| **NanoBot** | `msg.content` 为 `list[dict]` 时崩溃（#4813/#4837） | prompt prefix 精确保持与 KV cache 复用；Dream/turn history 长期记忆；`long_task` 显式触发 | 42 项安全/审计发现；MCP 重连 cancel scope 隔离 | **可复现性与本地模型友好**：强调 Ollama 等本地 provider 的缓存复用 |
| **Hermes Agent** | — | 推理预算 `THINKING_BUDGET` 档位映射错误（#61339）；模型回退链稳定性 | 非 shell 工具绕过护栏、时间敏感幻觉、规划过度执行、自演化技能路线图 | **实验型对齐/安全**：更像研究沙盒，代码落地率偏低 |
| **PicoClaw** | — | — | 凭据外部化（jsonrpc）、skill 状态开关 | **嵌入式/轻量配置**：Sipeed 生态的硬件友好型 Agent 框架 |
| **NanoClaw** | — | 长工具链后 `<message to>` 包装器遗漏导致静默丢回复（#3020）；temporal sessions | Guard 统一决策函数（#2986）；provider-agnostic 持久记忆（#3012）；任务单通道投递 | **安全护栏与任务投递为中心**：所有特权操作统一走 `guard()` |
| **LobsterAI** | — | delegated subagent collaboration（多智能体任务委托） | — | **企业协作**：Cowork 多轮协作与权限提示 |
| **CoPaw** | 中文记忆文件按字符截断触发 embedding 400（#5950） | 上下文压缩跨消息边界拆散 tool_call/tool_result（#5960、#5962）；heartbeat 恢复导致 tool 消息孤儿化（#5972） | `ToolResultLimiter` 截断大工具结果（#5953）；Agent 循环震荡（#5961） | **中文长上下文与工具一致性**：Qwen 生态导向 |
| **ZeroClaw** | `__image__` 技能自动激活与图像轮次屏蔽工具调用（#8965）；多入口多模态 payload 处理（#8360） | 默认 32k 上下文预算首轮即超支导致持续 preemptive trim（#5808） | 系统提示工具可用性与实际请求不一致（#8054）；工具参数未经验证转发导致 400（#8675）；持久记忆平面（#8891） | **后部署对齐与多入口一致性**：强调 reasoning models、channels、gateway、WebSocket 的行为一致 |

---

## 4. 共同关注的技术方向

| 方向 | 涉及项目 | 具体诉求 |
|---|---|---|
| **工具输出可观测性** | OpenClaw、CoPaw、ZeroClaw、NanoClaw | stdout/stderr 不能折叠为图像占位符；大工具结果需截断摘要；ANSI 状态不能跨块丢失 |
| **Prompt 前缀 / KV cache 一致性** | NanoBot、OpenClaw | 持久化的对话历史格式必须等于实际发送格式，否则本地/开源模型 KV cache 复用失败 |
| **长上下文压缩与工具结构完整性** | CoPaw、OpenClaw、ZeroClaw | 压缩/驱逐不能拆散 `tool_call`/`tool_result` 配对；恢复时不能遗留孤儿 tool 消息 |
| **系统提示与工具可用性对齐** | ZeroClaw、OpenClaw | 推理模型对系统提示遵从度高，声明“无工具”而实际携带工具会导致拒用或幻觉 |
| **安全护栏与审批** | NanoClaw、Hermes Agent、OpenClaw | 统一 `guard()` 决策、凭据掩码、模型判定操作批准、确定性 fallback |
| **持久记忆

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

**NanoBot 项目日报（2026-07-12）**

> 本摘要已按研究相关维度（多模态推理、长上下文理解、推理机制、AI 可靠性）对 22 条 Issues 与 26 条 PRs 进行了筛选，并跳过纯产品/商业类更新。

---

## 1. 今日速览

过去 24 小时 NanoBot 仓库活跃度极高：**22 条 Issues（19 活跃/3 关闭）** 与 **26 条 PRs（20 待合并/6 已合并或关闭）** 发生更新，无新版本发布。研究相关的核心主线集中在三方面：  
1）多模态消息健壮性（`msg.content` 为 `list[dict]` 时的崩溃）；  
2）对话提示前缀（prompt prefix）的精确保持与缓存复用；  
3）长上下文 / 长期记忆模块（Dream、turn history）的正确性与边界控制。  
同时，社区爆发了大规模安全/审计报告，揭示出在资源耗尽、授权边界、密钥隔离等方面存在显著可靠性债务。

---

## 2. 版本发布

**无新版本发布**。

---

## 3. 项目进展

今日合并/关闭的关键 PR 与 Issue 主要推进了系统稳定性、对话状态一致性和长任务控制：

- **HKUDS/nanobot#4764**（已关闭）：隔离 MCP 重连时的 cancel scope，防止网关崩溃。  
- **HKUDS/nanobot#4844**（已关闭）：将 sustained-goal（`long_task`）改为显式 `/goal` 触发，避免后台目标持续占用主线程而阻塞用户交互。  
- **HKUDS/nanobot#4891**（已关闭）：将当前时间、channel、chat ID 等运行时上下文改为 opt-in，默认不再注入每条 user prompt，从而保证提示前缀稳定、可缓存。  
- **HKUDS/nanobot#4872**（已关闭，Issue）：Dream 仅在运行真正有产出时才创建 git commit，避免空提交污染记忆历史。  
- **HKUDS/nanobot#4302**（已关闭，Issue）：网关级 MCP 重连崩溃问题已解决。

整体而言，项目在长对话状态管理、提示前缀一致性和长任务控制上向前迈出了一步，但尚未完全解决架构层面的 prompt prefix 精确保持问题。

---

## 4. 社区热点

| 编号 | 标题 | 评论数 | 研究/诉求 |
|------|------|--------|-----------|
| **HKUDS/nanobot#2463** | Architectural issue: nanobot does not preserve the exact prompt prefix it previously sent | 14 | 这是今日讨论最多的问题，指出当前对话历史持久化形式与“实际发送给模型的 prompt prefix”不一致，影响可复现性与 provider 层缓存。 |
| **HKUDS/nanobot#4867** | Preserve exact prompt prefix to enable caching in Ollama and others | 4 | #2463 的后续；用户反馈在 Ollama + 32 GB VRAM 场景下，每轮因无法复用 KV cache 额外增加约 60 秒，直接“完全不可用”。 |
| **HKUDS/nanobot#4815** | Audit summary: 42 security / bug / refactor findings from deep code audit | 0 | 由社区成员发布的 42 项深度审计汇总，虽然评论数少，但覆盖面极广，是今日安全与可靠性债务的风向标。 |

**诉求分析**：核心矛盾在于“对话历史存储格式 ≠ 实际发送格式”。这对长上下文模型的 KV cache 复用、推理可复现性、以及开源/本地模型（如 Ollama）的缓存机制都有直接影响，是推动 prompt prefix 稳定性改造的最大动力。

---

## 5. Bug 与稳定性

按严重程度与研究相关性排列：

| 严重度 | 编号 | 问题 | 修复状态 |
|--------|------|------|----------|
| **P1** | **HKUDS/nanobot#4813** | `AgentLoop` 中 `msg.content.strip()` 对多模态 `list[dict]` 内容崩溃 | 待合并（与 #4837 重复） |
| **P1** | **HKUDS/nanobot#4837** | 同上，并补充 `prepare_call` 异常日志 | 待合并 |
| **P1** | **HKUDS/nanobot#4842** | MCP 关闭时未捕获 `asyncio.CancelledError` | 待合并 |
| **P1** | **HKUDS/nanobot#4764** / **HKUDS/nanobot#4302** | MCP 重连导致网关崩溃 | 已关闭 |
| **P1** | **HKUDS/nanobot

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

本报告已过滤产品、商业及平台运营类更新，聚焦于**视觉-语言能力、推理机制、训练/后训练方法、幻觉与 AI 可靠性**议题。

---

## 1. 今日速览

过去 24 小时 Hermes Agent 仓库活跃度较高，共有 **50 条 Issues** 更新（41 条活跃、9 条关闭）和 **50 条 PRs** 更新（仅 2 条完成合并/关闭，其余 48 条仍在 Open 状态）。研究相关进展集中在：智能体安全护栏（非 shell 工具绕过）、推理预算映射错误、时间敏感幻觉、规划技能过度执行、模型回退链稳定性，以及自演化技能训练路线图的社区呼声。整体看，讨论热烈但代码落袋率偏低，算法与可靠性议题的积压仍在增长。

---

## 2. 版本发布

**今日无新版本发布。**

---

## 3. 项目进展

今日可见的 **Open PR 中无已合并项**，全仓库仅有 2 个 PR 完成关闭/合并，但摘要列表未展示其具体内容。已关闭的 Issues 中，研究/可靠性相关的有：

- **#62905** — Cron 工具在网关重启后错误路由到交互式审批，导致 headless 任务静默无输出。已被关闭（无法复现）。  
  [NousResearch/hermes-agent#62905](https://github.com/NousResearch/hermes-agent/issues/62905)

- **#62828** — 熔断器失效：`recompute_ready` 在 `gave_up` 后重新提升任务。已关闭。  
  [NousResearch/hermes-agent#62828](https://github.com/NousResearch/hermes-agent/issues/62828)

- **#60385** — MCP server 进程在重连时泄漏。已关闭。  
  [NousResearch/hermes-agent#60385](https://github.com/NousResearch/hermes-agent/issues/60385)

主要推进仍依赖以下活跃 Open PR：

- **#61339** — 修复 `THINKING_BUDGET` 缺少 `minimal`/`max` 档，导致非自适应模型上推理努力度被静默降级为 `medium`（8000 token）。

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

**PicoClaw 项目日报（2026-07-12）**  
*数据来源：sipeed/picoclaw | 统计窗口：过去 24 小时*

---

### 1. 今日速览
过去 24 小时 PicoClaw 社区活跃度较低：无新增或关闭的 Issue，仅有 3 条 PR 更新（2 条待合并、1 条已关闭），无新版本发布。所有更新均集中在应用层配置、技能开关与消息协议整理，**未涉及视觉语言能力、推理机制、训练方法论或幻觉相关的研究型进展**。从研究分析师视角看，今日可视为“框架维护日”，核心模型/算法能力无实质推进。

---

### 2. 版本发布
**无。** 今日无新 Release，本部分省略。

---

### 3. 项目进展
| PR | 状态 | 核心内容 | 研究/技术意义 |
|---|---|---|---|
| **#3249** | **CLOSED** | 为 skill 增加启用/禁用状态，并在 UI 提供开关；cron 支持 `RunNow` 与暂停；状态文件位于 `workspace/skills/.skills-state.json`，依赖 mtime 自动失效 prompt cache，无需重启即可生效。 | 属于产品化/运维改进，提升多 skill 系统的可控性；与模型推理或训练方法无关。 |
| **#3225** | **OPEN** | 允许 `agents.list` 中的每个 agent 单独覆盖 `max_tokens`、摘要阈值与 `split_on_marker`；构造 `AgentInstance` 时应用这些参数；同时清理了未使用的 `openai_compat` import。 | 面向配置灵活性，属于系统级调度优化，未触及底层模型能力或对齐策略。 |
| **#3222** | **OPEN** | 重构 DeltaChat 实现，减少约 200 行代码；移除旧版 fallback、密码式邮箱配置与硬编码中继列表；密钥改由 jsonrpc 管理；重命名/补充 invite 链接接口。 | 主要提升可维护性与安全性，对研究相关议题没有直接贡献。 |

**整体判断**：今日合并/讨论的 PR 均为配置、UI 与第三方协议集成层面的改进，项目整体在“工程化”上小幅前进，但在多模态推理、长上下文理解、post-training 对齐等研究领域没有可见进展。

---

### 4. 社区热点
由于今日 **0 条 Issue**，且所有 PR 的 `👍` 数均为 0、评论数显示为 `undefined`，社区无真正“高热”讨论。按更新时间和内容类型，相对最受关注的是：

- **#3225 Support agent-specific runtime overrides**  
  [https://github.com/sipeed/picoclaw/pull/3225](https://github.com/sipeed/picoclaw/pull/3225)  
  **背后诉求**：用户希望不同 agent 能拥有独立的 token 预算与摘要策略，反映多 agent 场景下对精细化资源控制的需求。

- **#3222 refactor(deltachat): cleanup implementation, documentation -200LOC**  
  [https://github.com/sipeed/picoclaw/pull/3222](https://github.com/sipeed/picoclaw/pull/3222)  
  **背后诉求**：降低邮件桥接模块的维护成本，同时推动敏感配置（密码/密钥）从静态配置迁移到 jsonrpc，符合安全最佳实践。

---

### 5. Bug 与稳定性
**今日无新增 Bug Issue 或崩溃报告。**  
但需关注以下潜在回归风险：

1. **#3222 的破坏性变更风险**：删除密码式邮箱配置、硬编码中继列表与旧 fallback，可能导致依赖旧版配置的工作流失效；建议维护者在合并前补充迁移说明。
2. **#3249 的调度状态变更**：cron 暂停/继续逻辑改动，可能影响定时 skill 的可靠性；目前该 PR 已关闭，但后续应验证状态持久化与并发行为。
3. **#3225 的编译依赖**：移除了 `openai_compat` import，若仍有隐式引用，可能引发编译或兼容性回归。

---

### 6. 功能请求与路线图信号
**今日无新增功能请求 Issue。**  
结合现有 PR 可观察到以下路线图信号：

- **per-agent 运行时覆盖（#3225）**：大概率会被纳入下一版本，作为多 agent 调度能力的基础配置扩展。
- **安全凭证外部化（#3222）**：反映项目正逐步将 secret 管理从配置文件抽离到 jsonrpc/外部服务，这符合企业级部署的安全路线。
- **skill 动态开关（#3249）**：为后续“按需加载能力”或“权限控制”奠定基础，但当前实现与视觉/推理模型无关。

**研究相关信号**：今日数据中未发现与模型训练、后训练对齐、多模态输入处理或幻觉评估相关的路线信号。

---

### 7. 用户反馈摘要
由于今日 **0 条 Issue 且 PR 无实际评论**，无法从 Issues 评论中提炼真实用户痛点。基于 PR 描述可间接推断：

- **正面需求**：用户希望 skill 可动态启用/禁用，而不必重启整个系统；希望不同 agent 拥有独立参数配置。
- **安全诉求**：用户/贡献者希望邮箱类第三方集成的凭据不再存放在明文配置中。
- **信息缺失**：无关于视觉语言理解、推理错误、幻觉、长上下文失忆等研究型问题的直接反馈。

---

### 8. 待处理积压
- **#3225**（创建于 2026-07-04，最后更新 2026-07-11）已等待约 8 天，仍待合并。  
  [https://github.com/sipeed/picoclaw/pull/3225](https://github.com/sipeed/picoclaw/pull/3225)
- **#3222**（创建于 2026-07-03，最后更新 2026-07-11）已等待约 9 天，仍待合并。  
  [https://github.com/sipeed/picoclaw/pull/3222](https://github.com/sipeed/picoclaw/pull/3222)

这两条 PR 均涉及配置/协议层面的改进，建议维护者尽快 review，以避免影响后续依赖它们的特性开发。

---

### 研究相关性评估（供研究参考）
今日 PicoClaw 的数据对本报告重点关注的四大方向（视觉语言能力、推理机制、训练方法论、幻觉问题）**均无直接贡献**。若需追踪这些方向，建议后续监控以下内容：  
- Issue 标题/描述中是否出现 `vision`、`multimodal`、`hallucination`、`reasoning`、`RLHF`、`post-training`、`alignment`、`long-context` 等关键词；  
- PR 是否修改模型调用、prompt 构建、eval/benchmark 脚本或训练数据流水线；  
- Release notes 是否包含模型版本更新、能力评测或安全/对齐改进。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目日报 · 2026-07-12

**数据来源**：NanoClaw (`github.com/qwibitai/nanoclaw`)，统计窗口为 2026-07-11 全天。  
**研究视角**：本报告优先关注视觉-语言能力、推理机制、训练/后训练方法、幻觉与可靠性问题；与产品/商业运营相关的更新已压缩。

---

## 1. 今日速览

今日仓库活跃度中等：新增 2 条 Issue、9 条 PR（7 条待合并、2 条已关闭），无新版本发布。从研究角度看，**没有直接涉及视觉语言能力（VLM）或模型训练方法论的更新**，信号主要集中在**后训练部署对齐、长上下文工具链推理可靠性、安全护栏与持久化记忆**等 AI 可靠性议题。核心团队继续推进 Guard 统一决策函数、任务单通道投递、provider-agnostic memory 等基础设施；同时，agent-runner 在长工具链后出现 `<message to>` 包装器遗漏导致回复静默丢失的问题，对“长上下文推理 → 指令遵循退化”这一研究课题具有参考价值。

---

## 2. 版本发布

无今日发布。

---

## 3. 项目进展

- **PR #3015 — fix: preserve phase context in live progress**  
  [https://github.com/qwibitai/nanoclaw/pull/3015](https://github.com/qwibitai/nanoclaw/pull/3015)  
  已关闭/合并。修复了 E2E 测试中 Claude 首个工具事件可能早于阶段说明、导致进度卡片出现孤立“已完成读取”的问题；同时解决了 `tool_result` 60 字摘要被 warning 占满、丢失测试通过数的缺陷。采用脱敏后上限 1000 字的结构化摘要，并新增真实时序与长 warning 回归测试。该修复对**多步推理过程的可观测性**有直接意义。

- **PR #3018 — RFC: temporal (incognito) sessions**  
  [https://github.com/qwibitai/nanoclaw/pull/3018](https://github.com/qwibitai/nanoclaw/pull/3018)  
  已关闭。作者以 RFC/愿景分享形式提出“无记忆、一次性 DM 会话”，但按 `CONTRIBUTING.md` 源码级特性不应直接进 `main`，因此该 PR 被关闭作为设计讨论，尚未转化为可合并技能。

---

## 4. 社区热点

今日所有 Issue/PR 的评论数与 👍 均为 0，热度主要由**影响范围**衡量：

- **#3016 — rate_limit_event 被全部记录为 quota 错误**  
  [https://github.com/qwibitai/nanoclaw/issues/3016](https://github.com/qwibitai/nanoclaw/issues/3016)  
  自 #2965 后，即使请求被 `status="allowed"`，agent-runner 仍输出 `Rate limit (retryable: false, quota)`，一周内出现 82 次误报。这反映了**日志语义与可观测性**的可靠性问题，容易造成运维误判。

- **#3017 — Windows + VS2026 + better-sqlite3 v11.10.0 编译失败**  
  [https://github.com/qwibitai/nanoclaw/issues/3017](https://github.com/qwibitai/nanoclaw/issues/3017)  
  构建链兼容性痛点，影响 Windows 开发者 onboarding。

- **#3020 — 修复长工具链后 `<message to>` 包装器遗漏导致的静默丢回复**  
  [https://github.com/qwibitai/nanoclaw/pull/3020](https://github.com/qwibitai/nanoclaw/pull/3020)  
  关联历史 Issue #2369、#2393、#2404，是当前最贴近**长上下文推理与指令遵循**的修复。

---

## 5. Bug 与稳定性

按严重程度排序：

| 严重程度 | 问题 | 状态 | 修复 PR |
|---|---|---|---|
| **高** | **Windows 11 + VS2026 构建失败** — 阻塞 Windows 开发者环境 | Issue #3017 开放 | 尚无 |
| **高** | **Agent 30 分钟心跳停滞** — 主机因 `heartbeatAgeMs≈1,800,000` 杀死容器，出现“零 SDK 活动”长挂起 | Issue 未单独开，PR #3019 直接修复 | [PR #3019](https://github.com/qwibitai/nanoclaw/pull/3019) |
| **中** | **rate_limit_event 误报为 quota 错误** — 每次正常轮次都报错误 | Issue #3016 开放 | 尚无 |
| **中** | **长工具链后模型省略 `<message to>` 包装器，回复静默丢失** — 属于“输出格式幻觉/指令遵循退化” | PR #3020 修复中 | [PR #3020](https://github.com/qwibitai/nanoclaw/pull/3020) |
| **中** | **`hasIdenticalSend` 未绑定到当前 turn** — 可能导致重复发送检测误触发 | PR #3014 修复中 | [PR #3014](https://github.com/qwibitai/nanoclaw/pull/3014) |
| **低** | **实时进度阶段上下文丢失** | 已合并修复 | [PR #3015](https://github.com/qwibitai/nanoclaw/pull/3015) |

---

## 6. 功能请求与路线图信号

- **PR #3012 — provider-agnostic persistent memory**  
  [https://github.com/qwibitai/nanoclaw/pull/3012](https://github.com/qwibitai/nanoclaw/pull/3012)  
  为每个 agent group 搭建 `memory/index.md` 与 `memory/system/definition.md`，在启动、clear、compaction 后加载记忆，是跨 provider 的长期记忆基础设施，**属于后训练/持续学习中“外部记忆”机制**。

- **PR #2986 — Guard seam: one decision function for every privileged action**  
  [https://github.com/qwibitai/nanoclaw/pull/2986](https://github.com/qwibitai/nanoclaw/pull/2986)  
  所有跨容器/通道的特权操作统一走 `guard()` 决策函数：`allow | hold | deny`。这是**后训练对齐/安全护栏**的核心架构。

- **PR #2988 — Tasks: one-door delivery**  
  [https://github.com/qwibitai/nanoclaw/pull/2988](https://github.com/qwibitai/nanoclaw/pull/3018)  
  任务会话中 `send_message` 与 `send_file

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw 项目日报 · 2026-07-12

## 1. 今日速览
过去 24 小时内，NullClaw 仓库活跃度较低：仅有 2 条 Issues 更新，无 PR 更新、无新版本发布。所有 Issues 均处于开放状态，未有关闭或修复记录。  
**研究相关性扫描**：今日新增/活跃内容中未发现与视觉语言能力、推理机制、训练方法论或幻觉问题直接相关的讨论，主要集中于后端连接稳定性与 CLI 适配器扩展。

---

## 2. 版本发布
无。  
（今日未发布任何 Release 或 Tag。）

---

## 3. 项目进展
今日无合并或关闭的 PR，因此没有新的功能、修复或重构正式进入主分支。项目整体进展停滞。

---

## 4. 社区热点
- **#972 Telegram channel stop respond after some idle time**  
  https://github.com/nullclaw/nullclaw/issues/972  
  评论数最多（3 条），反映用户在长时间空闲后 Telegram 渠道失去响应，但后端 `nullclaw agent` 似乎仍正常运行。  
  诉求：希望解决第三方消息渠道与后台代理之间的连接/保活问题，提升长期运行稳定性。

- **#975 Add grok-cli provider (run Grok via the grok CLI's login session, unmetered)**  
  https://github.com/nullclaw/nullclaw/issues/975  
  用户希望新增 `grok-cli` provider，复用现有的 `claude-cli` / `codex-cli` / `gemini-cli` 子进程模式。  
  诉求：通过本地已登录的 `grok` CLI 使用 Grok，规避 API 计量费用，并统一 CLI 适配器体系。

---

## 5. Bug 与稳定性
| 严重度 | Issue | 标题 | 状态 | 说明 |
|---|---|---|---|---|
| 中 | #972 | Telegram channel stop respond after some idle time | 开放，无修复 PR | 长时间空闲后 Telegram 渠道无响应，后端日志显示内存计划与后端运行正常，问题可能在渠道层保活或事件循环 |
| 低 | — | 无其他崩溃/回归报告 | — | — |

---

## 6. 功能请求与路线图信号
- **#975 Add grok-cli provider**  
  https://github.com/nullclaw/nullclaw/issues/975  
  该请求与现有 `src/provider_probe.zig:43` 的 CLI provider 模式高度一致，技术路径清晰（复用子进程调用）。若维护者希望扩展大模型 provider 覆盖，该功能较容易被纳入下一版本。

---

## 7. 用户反馈摘要
- **稳定性痛点**：有用户部署在 EC2 上，发现 Telegram 渠道隔夜后“假死”，但后端 `agent` 仍可响应 `ping`（#972）。这提示渠道层与后台代理的状态同步/心跳机制可能存在缺陷。
- **成本与接入场景**：用户希望利用已付费的 `grok.com` 订阅，通过官方 grok CLI 的登录会话来接入，避免额外的 API 计费（#975）。
- **整体满意度信号**：今日样本有限，未看到针对模型能力、幻觉或训练质量的反馈。

---

## 8. 待处理积压
- **#972** 与 **#975** 均处于开放状态，且目前无 PR 跟进。建议维护者优先 triage：  
  - #972 需确认是 Telegram Bot 长连接超时、网络层保活，还是 NullClaw 渠道工作进程未正确重连；  
  - #975 可作为 CLI provider 家族的标准扩展，参考已有 `claude-cli` 实现模板。

---

**研究视角总结**：今日 NullClaw 的社区动态不包含多模态推理、长上下文机制、post-training 对齐或幻觉相关议题。若需要追踪这些研究方向，建议监控后续涉及模型输出评估、训练数据管道、视觉输入处理或 RAG/检索质量相关的 Issue/PR。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目日报 · 2026-07-12

> **分析视角**：多模态推理、长上下文理解、post-training 对齐、AI 可靠性  
> **数据来源**：GitHub `netease-youdao/LobsterAI` 过去 24h 的 Issues / PRs / Releases

---

## 1. 今日速览

- 过去 24 小时项目活跃度偏低：**3 条 Issues 全部仍处于 open 且均为 stale 状态**，**1 条 PR 待合并**，**无已合并或关闭的研发交付**。
- 在研究方向（视觉语言、推理机制、训练方法论、幻觉问题）上，**今日没有直接相关的 Issue 或 PR**；所有活跃内容均为 Cowork / Agent 产品交互层改进。
- 值得关注的路标信号来自最新版本 `2026.7.10` 中的 **delegated subagent collaboration**，可作为多智能体协作与任务推理机制方向的跟踪点。
- 整体健康度：维护节奏偏慢，社区反馈停留在 UI/UX 与配置类问题，建议维护者关注 4 月至今未关闭的 stale 积压。

---

## 2. 版本发布

### LobsterAI 2026.7.10（2026-07-10）

**发布页面**：[`netease-youdao/LobsterAI/releases/tag/2026.7.10`](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.7.10)

**What’s Changed（根据当前可获取信息）**：

| 变更项 | 关联 PR | 内容与研究/技术相关性 |
|---|---|---|
| `feat(agents): support delegated subagent collaboration` | PR #2285 by @btc69m979y-dotcom | 涉及多智能体系统中的任务委托与协作机制，与**多智能体推理 / agentic reasoning** 相关 |
| `feat(cowork): add minimizable permission prompts` | PR #2296 by @btc69m979y-dotcom | 属于产品交互体验层，与研究核心方向关联较弱 |

**破坏性变更 / 迁移注意事项**：  
当前 release notes 未提供明确的 Breaking Changes 或迁移指南。由于数据截断，建议维护者补充兼容性说明。

---

## 3. 项目进展

**今日无合并或关闭的 PR / Issue**，项目整体代码推进为 0。

唯一处于 open 的 PR：

- **PR #1327** — 功能增强：ToolUse 工具调用块批量展开/折叠  
  链接：https://github.com/netease-youdao/LobsterAI/pull/1327  
  状态：open、stale（创建于 2026-04-02，最后更新 2026-07-11）  
  说明：对应 Issue #1326，实现「一键展开/折叠全部 tool call」的 UI 功能。由于未合并，对主干暂无实际推进。

**总结**：除 7 月 10 日已发布的版本外，今日没有新的研发交付；项目处于低活跃维护期。

---

## 4. 社区热点

今日 3 条 Issues 与 1 条 PR 的互动数据完全相同（各 1 条评论、0 个赞），无显著高热度条目。按主题关联度排序：

| 条目 | 链接 | 讨论焦点 |
|---|---|---|
| Issue #1326 + PR #1327 | [Issue #1326](https://github.com/netease-youdao/LobsterAI/issues/1326) / [PR #1327](https://github.com/netease-youdao/LobsterAI/pull/1327) | 多工具调用时的 UI 操作效率；诉求是批量控制展开/折叠状态 |
| Issue #1330 | [Issue #1330](https://github.com/netease-youdao/LobsterAI/issues/1330) | 错误会话缺少视觉提示，要求增加红色错误徽标 |
| Issue #1329 | [Issue #1329](https://github.com/netease-youdao/LobsterAI/issues/1329) | 定时任务通知渠道配置异常 |

**背后诉求**：社区反馈集中在 Cowork 会话的可观测性、批量操作效率与通知配置体验，反映用户在高频协作场景下对界面信息密度的敏感。

---

## 5. Bug 与稳定性

| 严重度 | 条目 | 问题描述 | 是否有修复 PR |
|---|---|---|---|
| 中 | Issue #1329 | 新建定时任务时，「通知渠道」下拉框无选项，仅可选择「不通知」 | 否 |
| 低 | Issue #1330 | 错误状态会话缺少侧边栏红点提示，影响故障定位 | 否（PR #1327 不相关） |

- 今日未报告崩溃、回归或性能问题。
- 在 **幻觉、训练稳定性、多模态推理可靠性** 等研究方向上，今日无新增 Bug 或修复。

---

## 6. 功能请求与路线图信号

| 功能需求 | 条目 | 与研究/技术方向的关联 | 纳入下一版本可能性判断 |
|---|---|---|---|
| 批量展开/折叠 ToolUse 块 | Issue #1326 / PR #1327 | 产品交互层；对多工具调用的可解释性有轻微辅助 | 已有 PR 实现，但 stale 未合并，需维护者 review |
| 错误状态红点徽标 | Issue #1330 | 产品可观测性 | 需求明确、改动小，较易被纳入 |
| 子代理委托协作 | Release 2026.7.10 / PR #2285 | **多智能体推理 / agentic collaboration** | 已在最新版本中发布 |

**研究视角提示**：虽然本期数据以产品功能为主，但 `delegated subagent collaboration` 是 LobsterAI 向**可扩展多智能体系统**演进的信号，建议后续关注其如何影响推理一致性、任务分解与幻觉传播风险。

---

## 7. 用户反馈摘要

**真实痛点**：

- 工具调用块多时，逐个展开/折叠操作繁琐（Issue #1326）。
- 会话出错时无法一眼定位，排查效率低（Issue #1330）。
- 定时任务通知渠道配置入口异常，导致无法设置通知（Issue #1329）。

**使用场景**：用户主要在 Cowork 多轮协作、定时自动化任务等高频场景下使用，界面信息层级与状态反馈成为主要摩擦点。

**满意/不满意**：数据未显示正面评价；负面反馈集中在 UI 细节与配置可用性。

---

## 8. 待处理积压

以下条目创建时间均为 **2026-04-02**，最后更新 **2026-07-11**，已超过 3 个月无关闭或合并，属于长期 stale 积压：

| 条目 | 链接 | 待处理原因 |
|---|---|---|
| Issue #1326 | https://github.com/netease-youdao/LobsterAI/issues/1326 | 功能请求已提交，PR #1327 已开但未 review |
| PR #1327 | https://github.com/netease-youdao/LobsterAI/pull/1327 | 实现已完成，但长期未合并 |
| Issue #1329 | https://github.com/netease-youdao/LobsterAI/issues/1329 | 疑似配置/前端 Bug，无维护者响应 |
| Issue #1330 | https://github.com/netease-youdao/LobsterAI/issues/1330 | UI 增强需求明确，无对应 PR |

**建议**：维护者优先 review PR #1327，并 triage #1329（可能涉及 API 数据未返回通知渠道）与 #1330（纯 UI 改动）。

---

**结论**：LobsterAI 今日在核心研究方向上无新进展，项目活动以产品体验优化和 7 月 10 日版本中的多智能体协作功能发布为主。建议持续跟踪 `delegated subagent collaboration` 后续的推理可靠性、对齐与长上下文表现数据。

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis 项目日报 — 2026-07-12

> **研究相关性提示**：今日 24 小时数据（0 issues / 1 PR / 0 releases）全部为常规工程维护内容，未涉及视觉语言能力、推理机制、post-training 训练方法论或幻觉等研究议题。下述摘要按项目整体健康度整理，研究相关信号为空。

---

## 1. 今日速览

- 项目过去 24 小时活跃度较低：仅 1 个待合并 PR，无新增 Issue、无版本发布、无社区讨论。
- 唯一更新是 CalDAV 客户端事件列表时间范围过滤的修复，属于 calendar 同步模块的 bugfix，与研究主线无关。
- 整体项目健康度平稳，但研发节奏处于“维护等待”状态，尚未出现新的功能推进或研究进展。
- 需要关注 PR #1147 的 review/合并进度，以确认稳定性修复落地。

---

## 2. 版本发布

无。

---

## 3. 项目进展

- **今日无已合并或已关闭的 PR**。
- **唯一待合并 PR**：#1147 `fix(caldav): honor time range in list_events via server-side calendar-query`  
  - 链接：https://github.com/moltis-org/moltis/pull/1147
  - 作用：修复 `CalDavClient::list_events` 中 `_range` 参数被绑定但未被使用的问题，改为通过 CalDAV `calendar-query` 在服务器端执行时间范围过滤，使 `start/end` 参数真正生效。
  - 由于该 PR 尚未合并，今日项目尚未在代码层面“向前推进”，仍处于 review 等待状态。

---

## 4. 社区热点

- 今日无讨论活跃、评论多或点赞多的 Issue/PR。
- PR #1147（https://github.com/moltis-org/moltis/pull/1147）当前评论数为 0、点赞数为 0，社区参与度极低。
- 背后信号：当前没有集中的用户诉求或技术争议在推动讨论。

---

## 5. Bug 与稳定性

| 问题 | 严重度 | 状态 | 说明 |
|------|--------|------|------|
| CalDAV `list_events` 时间范围过滤失效，导致客户端拉取整个日历 | 中 | 已有 fix PR，待合并 | 影响查询准确性和性能；PR #1147 提供服务器端过滤方案 |

- 链接：https://github.com/moltis-org/moltis/pull/1147

---

## 6. 功能请求与路线图信号

- 今日无新功能请求。
- 结合现有 PR 无法推断出多模态推理、长上下文理解、post-training 对齐或幻觉相关研究路线图的信号。

---

## 7. 用户反馈摘要

- 今日无 Issue 评论数据，无法提炼真实用户痛点、使用场景或满意度反馈。

---

## 8. 待处理积压

- **PR #1147**：https://github.com/moltis-org/moltis/pull/1147
  - 创建与更新时间均为 2026-07-11，目前仍处于 Open 状态，需维护者关注 review 与合并。
- 无其他长期未响应的重要 Issue 或 PR。

---

**总结**：Moltis 今日处于低活跃维护状态。与研究重点相关的视觉语言、推理、训练对齐、幻觉等议题在 24 小时内没有任何数据信号，建议扩展监控范围（如 docs/research、实验分支、论文引用）或等待更长的观察周期。

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

**CoPaw 项目日报（2026-07-12）**  
*注：以下仅摘录与多模态推理、长上下文理解、post-training 对齐及 AI 可靠性相关的研究内容；UI 暗色模式、OAuth、安装包、沙箱/桌面壳等工程或产品更新已省略。*

---

## 1. 今日速览

过去 24 小时，仓库活跃度较高：新增/活跃 Issue 22 条、PR 7 条，但无新版本发布。研究相关信号集中在 **v2.0.0 长上下文压缩、tool-use 一致性、记忆索引与 Agent 推理循环稳定性** 四大主题。多个回归性 Bug 显示：2.0 版本在会话恢复、上下文裁剪、tool_call/tool_result 配对管理上出现了系统性脆弱点，对下游模型调用产生了直接的 400/可靠性影响；同时，用户开始主动要求对工具返回结果进行更精细的截断与通道控制，以缓解长上下文膨胀。

---

## 2. 版本发布

**无。**  
今日未发布任何 Release，也无破坏性变更或迁移公告。

---

## 3. 项目进展

今日没有与研究主题直接相关的 **已合并/已关闭** PR。已关闭的 4 个 PR（[#5970](https://github.com/agentscope-ai/QwenPaw/pull/5970)、[#5971](https://github.com/agentscope-ai/QwenPaw/pull/5971)、[#5973](https://github.com/agentscope-ai/QwenPaw/pull/5973)、[#5974](https://github.com/agentscope-ai/QwenPaw/pull/5974)）均为暗色模式 UI 对比度修复，对核心推理/长上下文能力影响有限。

值得关注的研究相关 **开放 PR**：

- **PR [#5953](https://github.com/agentscope-ai/QwenPaw/pull/5953)**：将 `ToolResultLimiter` 统一为大型工具结果截断的单一入口，大结果持久化为 `tool_results/` 产物文件，而上下文与滚动历史只保留带标准提示的截断摘要。这直接服务于长上下文管理与工具结果可靠性，但尚未合并。

---

## 4. 社区热点

今日讨论最活跃、且与研究议题相关的 Issue/PR 如下：

| Issue/PR | 评论/反应 | 核心诉求 |
|---|---|---|
| **#5951** Windows 沙箱 `pwsh` 递归爆炸、NTFS ACL 污染 | 7 评论 | 系统级执行环境稳定性（非核心研究议题，但执行层可靠性会间接影响 Agent 推理闭环） |
| **#5961** v2.0.0 循环执行反复写入/删除 | 3 评论 | 对 `qwen3.7-plus` 的 Agent 推理/任务循环出现规划震荡，简单任务无法收敛 |
| **#5950** 中文记忆文件触发 embedding 400 错误 | 3 评论 | 多语言/多字节文本在记忆索引阶段按字符而非 token 截断，导致长上下文嵌入失败 |
| **#5960** 上下文压缩跨消息边界拆散 tool_call/tool_result | 2 评论 | 长上下文压缩策略未保持 tool-use 结构一致性，导致 API 400 |
| **#5962** WeChat 通道滚动驱逐后 tool_result 孤儿化 | 1 评论 | 与 #5960 同源，说明压缩/驱逐机制在真实通道中已造成系统性失败 |

---

## 5. Bug 与稳定性

按对研究相关能力（长上下文、工具调用、推理可靠性）的影响严重程度排序：

### 🔴 严重

1. **#5960 [Bug] 上下文压缩跨消息边界拆散 tool_call/tool_result 配对导致 400**  
   - 问题：`_split_context_for_compression()` 以消息为粒度分割，导致同一对话中的 `tool_call` 与 `tool_result` 被拆到压缩/保留两侧，触发 API 400。  
   - 状态：开放，暂无 fix PR。  
   - 链接：[https://github.com/agentscope-ai/QwenPaw/issues/5960](https://github.com/agentscope-ai/QwenPaw/issues/5960)

2. **#5962 [Bug] WeChat 通道滚动驱逐后 tool_result 孤儿化导致 400**  
   - 问题：与 #5960 同源，会话滚动清理后遗留孤立 `tool_result`，新/旧会话均 `Internal error`。  
   - 状态：开放，暂无 fix PR。  
   - 链接：[https://github.com/agentscope-ai/QwenPaw/issues/5962](https://github.com/agentscope-ai/QwenPaw/issues/5962)

3. **#5972 [Bug] heartbeat 会话恢复加载旧 session，导致 tool 消息孤儿化**  
   - 问题：恢复时加载旧 session 的 tool 结果与压缩地图，导致 `role: tool` 消息前无对应 `tool_calls`，DeepSeek API 返回 400。  
   - 状态：开放，暂无 fix PR。  
   - 链接：[https://github.com/agentscope-ai/QwenPaw/issues/5972](https://github.com/agentscope-ai/QwenPaw/issues/5972)

4. **#5961 [Bug] v2.0.0 搭配 qwen3.7-plus 循环执行反复写入/删除**  
   - 问题：Agent 在任务循环中不断重复写入、删除、再写入，长时间无法完成简单任务，属于典型的推理/执行震荡。  
   - 状态：开放，暂无 fix PR。  
   - 链接：[https://github.com/agentscope-ai/QwenPaw/issues/5961](https://github.com/agentscope-ai/QwenPaw/issues/5961)

### 🟡 中等

5. **#5950 [Bug] 中文记忆文件触发 embedding 400 错误——截断按字符数而非 token 数**  
   - 问题：Ollama + bge-m3 场景下，中文记忆因按字符截断而超出 embedding 模型上下文长度。  
   - 状态：开放，暂无 fix PR。  
   - 链接：[https://github.com/agentscope-ai/QwenPaw/issues/5950](https://github.com/agentscope-ai/QwenPaw/issues/

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目日报（研究视角）
**日期：** 2026-07-12  
**分析焦点：** 视觉语言能力、推理机制、长上下文处理、AI 可靠性 / 幻觉相关缺陷

---

## 1. 今日速览

过去 24 小时 ZeroClaw 仓库保持高活跃度：Issues 与 PR 各更新 50 条，无新版本发布。从研究相关性看，当日议程高度集中在**推理模型的工具可用性对齐**、**多模态入口的系统提示一致性**、**长上下文预算耗尽导致的持续性截断**以及**工具调用参数的可靠性**等核心问题。这些议题均直接影响模型在 Agent 循环中的事实一致性与行为稳定性，属于典型的 post-deployment alignment / reliability 研究范畴。工程侧的新功能（如 SOP 审批流、频道网关、WASM 插件）占比较大，但与本摘要的研究焦点关联较弱，已做过滤。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展（研究相关）

今日仅有 4 条 PR 被合并/关闭，其中 2 条对 Agent 核心推理循环与工具调用可靠性具有直接研究价值：

- **fix(runtime): thread agent_alias into agent_turn's ToolLoop** ([#8921](https://github.com/zeroclaw-labs/zeroclaw/pull/8921))  
  修复 `agent_turn` 在构建 `ToolLoop` 时硬编码 `agent_alias: None` 的问题，使生命周期钩子、工具路由与记忆关联能够使用正确的 agent 标识。该修复减少了多 agent 场景下身份混淆导致的工具调用错位，属于 Agent 身份一致性（identity grounding）的可靠性改进。

- **fix(providers): route pricing catalog through dispatch** ([#8885](https://github.com/zeroclaw-labs/zeroclaw/pull/8885))  
  将实时定价刷新调用统一路由到 `ProviderDispatch`，强化 provider 调用归属路径。对模型调用成本归因与多 provider 路由的稳定性有间接贡献。

其余两条关闭 PR（#8946、#8874）分别为 SOP 流程控制修复与 CI 文档调整，研究相关性较低。

---

## 4. 社区热点（研究相关）

今日评论最多的研究相关议题集中在**系统提示与工具可用性不匹配**、**上下文预算管理**以及**多模态入口一致性**：

- **#8054** — System prompt tool-availability should match per-turn effective tools across all entry points (channels, gateway, WebSocket, multimodal, /think)  
  [Issue #8054](https://github.com/zeroclaw-labs/zeroclaw/issues/8054)  
  **评论数：9**  
  这是 #7756 / #8053 的后续。核心问题：系统提示告诉推理模型“没有可用工具”，而实际上请求中已包含 native/MCP 工具。这种**系统提示与请求内容不一致**会在推理模型中诱发工具调用幻觉或拒绝调用，已在直接 runtime agent 路径修复，但 channels、gateway、WebSocket、多模态入口和 `/think` 路径仍存在同类不一致。  
  **研究信号：** 这是典型的 prompt-context mismatch 导致的模型行为失稳，对推理模型（reasoning models）的影响尤为显著，因为其对系统提示的遵从度更高。

- **#5808** — Default 32k context budget is exceeded by system prompt + tool definitions on iteration 1, causing perpetual preemptive trim  
  [Issue #5808](https://github.com/zeroclaw-labs/zeroclaw/issues/5808)  
  **评论数：8**  
  默认 `agent.max_context_tokens = 32000` 在首次 LLM 迭代即被系统提示 + 工具定义超出约 3.3 倍，导致运行时持续进行 preemptive trimming，可能丢失关键上下文并引发幻觉式回复。  
  **研究信号：** 长上下文预算与 prompt 工程之间的张力；动态 context management 对模型推理链完整性的影响。

- **#8965** — feat(skills): declarative auto-activation with provider switch and image-turn tool blocking  
  [PR #8965](https://github.com/zeroclaw-labs/zeroclaw/pull/8965)  
  为技能（skills）增加基于入站消息触发器的声明式自动激活，包括 `__image__` 哨兵以支持图像消息触发，并在图像轮次中屏蔽工具调用。  
  **研究信号：** 视觉-语言触发与工具调用的条件化控制，属于多模态 Agent 的触发策略与能力边界管理。

---

## 5. Bug 与稳定性（按严重程度）

| 严重度 | 议题 | 状态 | 研究相关性 | 链接 |
|--------|------|------|------------|------|
| S1 | 默认 32k 上下文在首轮即超支，导致持续 preemptive trim | Open / in-progress | 长上下文幻觉风险 | [#5808](https://github.com/zeroclaw-labs/zeroclaw/issues/5808) |
| S1 | 系统提示工具可用性与各入口实际工具不一致 | Open / accepted | 推理模型幻觉/拒用工具 | [#8054](https://github.com/zeroclaw-labs/zeroclaw/issues/8054) |
| S1 | 退出网页聊天窗口后 Agent 停止工作 | Open / accepted | 推理/任务连续性中断 | [#8559](https://github.com/zeroclaw-labs/zeroclaw/issues/8559) |
| S1 | OpenRouter/OpenAI 格式 provider 发送未经验证的工具参数导致 400 | Open / accepted | 工具调用可靠性 | [#8675](https://github.com/zeroclaw-labs/zeroclaw/issues/8675) |
| S2 | stdio MCP 服务器在 daemon 下积累为僵尸进程 | Open / accepted | 外部工具生态可靠性 | [#8731](https://github.com/zeroclaw-labs/zeroclaw/issues/8731) |
| S2 | skill-review fork 在工具密集轮次后 panic / SIGSEGV | Open / in-progress | 技能评估后训练可靠性 | [#8654](https://github.com/zeroclaw-labs/zeroclaw/issues/8654) |

**已有 fix PR 的项：**
- 工具循环中 `agent_alias` 传递错误 → 已修复于 [#8921](https://github.com/zeroclaw-labs/zeroclaw/pull/8921)
- WebSocket 连接断开不应取消运行中的 Agent turn → 修复中 [#9002](https://github.com/zeroclaw-labs/zeroclaw/pull/9002)

---

## 6. 功能请求与路线图信号

- **视觉-语言触发控制（#8965）**  
  通过 `__image__` 哨兵让 skills 对图像消息自动激活，并在图像轮次中 block 工具调用。这反映出社区对“多模态输入如何安全触发 Agent 能力”的强需求，可能进入后续版本的默认行为。

- **持久记忆平面（#8891）**  
  将跨 session 记忆子系统（curation、relevance、operability）拉平至成熟 peer runtime。与长上下文、幻觉抑制、个性化一致性直接相关。

- **SOP 确定性审批管道（#8979, #8903, #8880, #8848）**  
  构建无需实时 Agent turn 的审批门控流水线。虽然偏工程，但其“确定性 pipeline + LLM gate”的组合对研究可靠性、减少自主 Agent 幻觉式行动有参考价值。

- **Provider 与 native-tool 消息序列化（#8360）**  
  包含 provider 侧多模态 payload 处理，是视觉-语言能力集成的基础设施建设。

---

## 7. 用户反馈摘要

从研究视角提炼的真实痛点：

1. **推理模型更容易被错误系统提示误导**  
   用户反馈显示，当系统提示声明“无工具可用”而实际请求携带工具时，推理模型（reasoning models）会严格按照系统提示执行，导致工具调用失败或空回复。这验证了 system-prompt dominance 在 reasoning models 中的放大效应。

2. **长上下文预算不足直接威胁任务完成率**  
   默认 32k token 预算在系统提示 + 工具定义阶段即耗尽，用户经历“perpetual preemptive trim”，关键上下文被截断，后续回复出现事实不一致或任务偏离。

3. **多入口行为不一致削弱模型可靠性**  
   同一 Agent 在 direct runtime、WebSocket、Discord/Slack 等多模态通道中的工具可用性提示不一致，导致跨入口的 Agent 行为漂移。

4. **工具参数未经验证转发至 provider 是高频故障源**  
   模型生成的 tool-call arguments 字符串若非合法 JSON，会直接触发 provider 400 错误并返回空回复，缺乏运行时校验与回退机制。

---

## 8. 待处理积压

以下长期 open 议题对研究社区值得关注，建议维护者优先响应：

- **长上下文预算 defaults 不合理（#5808）**  
  自 2026-04-16 创建，已持续近三个月，直接影响首次迭代的事实一致性与幻觉率。

- **推理模型系统提示工具可用性不一致（#8054）**  
  自 2026-06-20 创建，虽已部分修复，但多模态入口仍未覆盖，是 reasoning reliability 的关键缺口。

- **Agent runtime 选项从首个配置 provider 泄漏（#7870）**  
  涉及 provider 选择逻辑，可能导致模型配置与实际调用模型不一致，属于模型身份/能力对齐缺陷。

- **Provider 侧多模态 payload 处理（#8360）**  
  作为视觉-语言能力的基础设施，长期 open 将制约图像输入、视频帧等高级多模态场景落地。

---

**总结：** 今日 ZeroClaw 在工程上保持高活跃，但从研究视角看，最值得关注的是**推理模型系统提示与工具可用性对齐**、**长上下文预算管理失败**、**多模态入口一致性**以及**工具调用参数可靠性**四类问题。这些问题均属于模型在复杂 Agent 系统中产生事实幻觉或行为失稳的根因，建议后续跟踪 #8054、#5808、#8675、#8965 的进展。

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*