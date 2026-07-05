# OpenClaw 生态日报 2026-07-05

> Issues: 500 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-05 00:28 UTC

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

# OpenClaw 项目研究动态日报（2026-07-05）

> 说明：本日报已按“多模态推理、长上下文理解、post-training 对齐、AI 可靠性”四个研究维度进行筛选，剔除了常规产品、商业、计费、市场运营等与研究无关的条目。

---

## 1. 今日速览

过去 24 小时 OpenClaw 仓库活跃度极高，Issues 与 PR 各更新 500 条，但无新版本发布。从研究视角看，今日信号集中在**长上下文效率**、**多模态/工具输出可靠性**、**幻觉与失败模式 containment**、**agent 推理链的可见性/可控性**四个方向。多数讨论仍属于“agent 运行时工程”范畴，真正触及底层模型训练或 post-training 对齐的条目有限，但工程层面对“模型行为可预测性”的约束正在加强。

---

## 2. 版本发布

今日无新版本发布，本部分省略。

---

## 3. 项目进展：今日合并/关闭及推进中的关键 PR

### 已关闭/合并的可靠性修复

- **PR #100047** — `fix(gateway): truncateCloseReason drops partial UTF-8 code point instead of emitting mojibake`
  - 修复 WebSocket close reason 截断时切断多字节 UTF-8 序列导致的 mojibake，属于多模态/文本流边界处理的基础可靠性修复。
  - https://github.com/openclaw/openclaw/pull/100047
- **PR #100026** — `fix(runtime): repair sessions and allow staged media through symlinked dirs`
  - 修复 macOS `/var -> /private/var` 等符号链接路径下的 session 清理与媒体文件放行，影响长期运行时的状态一致性。
  - https://github.com/openclaw/openclaw/pull/100026
- **PR #100114** — `fix(qa-channel): handle metadata-free final replies`
  - 处理 QA 通道中无元数据的最终回复，提升评测通道的确定性。
  - https://github.com/openclaw/openclaw/pull/100114

### 推进中的研究相关 PR

- **PR #100115** — `fix(diagnostics): expose zero-output context pressure`
  - 将“上下文压力导致零输出/零 tool-call”的终端调用事件暴露到诊断系统，对长上下文压缩与模型退化的研究有直接价值。
  - https://github.com/openclaw/openclaw/pull/100115
- **PR #99574** — `fix(litellm): honor Anthropic cache retention`
  - 修复通过 LiteLLM 代理 Claude 时 `cache_control` prompt-cache 标记被丢弃的问题，直接关联长上下文推理成本与缓存机制。
  - https://github.com/openclaw/openclaw/pull/99574
- **PR #96532** — `fix(openai): preserve cron thinking for GPT-5 nano`
  - 修复 cron 任务对 `gpt-5-nano` 的 `thinking` 请求因 catalog 陈旧而被忽略，影响推理链路一致性。
  - https://github.com/openclaw/openclaw/pull/96532
- **PR #100118** — `fix(agents): allow model fallback when takeover wrapper holds classifiable promptError`
  - 让主轮超时包装器保留可分类的 provider 失败，从而进入模型回退链，提升推理失败时的鲁棒性。
  - https://github.com/openclaw/openclaw/pull/100118
- **PR #100119** — `fix(channels): expose inbound media download failures`
  - 将 WhatsApp、LINE、Signal、iMessage、Teams、Feishu 等渠道的入站媒体下载失败显式上报，避免“幽灵占位图”和 caption 丢失，对多模态输入可靠性至关重要。
  - https://github.com/openclaw/openclaw/pull/100119
- **PR #99088** — `feat(xai): add realtime voice provider`
  - 为 xAI/Grok 添加原生实时语音 provider，扩展语音-文本多模态能力。
  - https://github.com/openclaw/openclaw/pull/99088
- **PR #100123** — `fix(tui): queue prompts while the agent is busy`
  - 解决 TUI 用户在 agent 运行时提交新提示被阻塞的问题，改善交互式推理流控制。
  - https://github.com/openclaw/openclaw/pull/100123

---

## 4. 社区热点：高讨论度研究议题

| 条目 | 评论/优先级 | 核心诉求 |
|------|-------------|----------|
| **Issue #44925** — Subagent completion silently lost | 20 / P1 | 子代理结果在超时、E31/E42/E45 等失败模式下静默丢失，要求可观测的 retry/restart 机制。 |
| **Issue #22438** — Tiered bootstrap file loading | 17 / P2 | 大 workspace 每次会话都加载全部 bootstrap 文件浪费上下文窗口，要求按层级/按需加载。 |
| **Issue #45740** — gh-issues skill 将未受信 issue body 直接注入子代理 prompt | 14 / P2 | 未清洗的外部文本进入 LLM prompt，存在 jailbreak/数据注入风险。 |
| **Issue #48003** — Steer mode 未能在主会话 turn 中注入消息 | 14 / P1 | 用户“steer”指令被排队到 turn 结束后，破坏了实时推理干预。 |
| **Issue #50090** — Community Skill Development & ClawHub | 15 / P2 | 社区技能生态漂移，需要版本化、评测与治理机制。 |
| **Issue #13583** — Pre-response enforcement hooks (hard gates) | 12 / P2 | 将“必须调用工具 X”等软规则改为 hard gate，强制约束最终响应前行为。 |
| **Issue #43367** — Multi-agent orchestration unstable | 13 / P1 | 并发 agent add/config 覆盖、session-lock 失败、游离子任务。 |
| **Issue #72015** — active-memory 阻塞回复并拖垮网关 | 9 / P1 | 记忆插件在 QMD 启动时过载，影响多代理网关的响应性。 |
| **Issue #49876** — Cron sessions deliver hallucinated output instead of failing | 9 / P1 | 工具失败后 LLM 生成看似可信的幻觉输出并发送给用户。 |
| **Issue #99241** — Tool outputs render as image attachments | 7 | ANSI/富文本工具输出被折叠为图片占位，agent 无法读取原始文本。 |

---

## 5. Bug 与稳定性：按严重程度排序

### P1 级（高严重，需立即关注）

- **Issue #49876** — Cron 会话在工具失败时生成幻觉输出而非干净失败
  - 标签：`impact:session-state`, `impact:security`
  - 状态：尚无 linked fix PR
  - https://github.com/openclaw/openclaw/issues/49876
- **Issue #44925** — 子代理完成结果静默丢失
  - 状态：已有 `clawsweeper:linked-pr-open`
  - https://github.com/openclaw/openclaw/issues/44925
- **Issue #48003** — Steer mode 未注入消息 mid-turn
  - 状态：已有 `clawsweeper:linked-pr-open`
  - https://github.com/openclaw/openclaw/issues/48003
- **Issue #43367** — 多代理编排不稳定
  - 状态：已有 `clawsweeper:linked-pr-open`
  - https://github.com/openclaw/openclaw/issues/43367
- **Issue #41744** — Fe

---

## 横向生态对比

**个人 AI 助手 / 自主智能体开源生态横向对比分析**  
*数据口径：2026-07-05 过去 24 小时各项目动态；研究视角：多模态推理、长上下文理解、post-training 对齐、AI 可靠性*

---

### 1. 生态全景

整体生态正从“功能 demo”进入“可靠性工程”阶段：头部运行时（OpenClaw、ZeroClaw、IronClaw、NanoClaw）保持高频迭代，但今日无任一项目发布新版本，说明重点工作是缺陷收敛与架构加固而非能力发布。研究信号明显向**长上下文压缩/记忆一致性、工具边界隔离、失败静默传播、审批与人机信任**倾斜，真正触及底层模型训练或 post-training 对齐的代码仍偏少。与此同时，大量中小项目（NullClaw、ZeptoClaw、TinyClaw、Moltis）处于停摆，生态分化加剧。

---

### 2. 各项目活跃度对比

| 项目 | 24h Issues | 24h PRs | 新版本 | 健康度评估 | 阶段 |
|---|---|---|---|---|---|
| **OpenClaw** | 500 | 500 | 0 | 极高活跃，但 P1 可靠性债务密集（cron 幻觉、子代理静默丢失、steer 失效、多代理不稳定） | 快速迭代 + 质量巩固 |
| **NanoBot** | 3 | 12 | 0 | 中低频维护，MCP 异常隔离与并发竞态已修复；未解决 P1 #4302 是最大风险 | 质量巩固 |
| **Hermes Agent** | — | — | — | 摘要生成失败，无有效数据 | 数据缺失 |
| **PicoClaw** | 4 | 7 | 0 | 低活跃，维护性更新为主；AI “失忆”Issue 被 stale 关闭未修复 | 维护期 |
| **NanoClaw** | 1 | 38 | 0 | 高活跃，集中在安全边界、状态一致性、LiteLLM 路由；高严重性 UI 欺骗漏洞尚无修复 | 快速迭代 + 安全加固 |
| **NullClaw** | 0 | 0 | 0 | 无任何活动 | 停滞 |
| **IronClaw** | 9 | 50 | 0 | 高活跃，基础设施与 CI 为主；开始将“错误必须上浮”从文档推向编译期强制 | 架构/可靠性升级 |
| **LobsterAI** | 1 | 3 | 0 | 活跃度极低，核心技能生成阻塞与多模态上传问题长期 stale | 停滞风险 |
| **TinyClaw** | 0 | 0 | 0 | 无活动 | 停滞 |
| **Moltis** | 0 | 0 | 0 | 无活动 | 停滞 |
| **CoPaw / QwenPaw** | 10 | 3 | 0 | beta 阶段活跃；多模态缓存 bug 已关闭，但长上下文压缩与记忆状态丢失构成新风险 | 快速迭代（beta） |
| **ZeptoClaw** | 0 | 0 | 0 | 无活动 | 停滞 |
| **ZeroClaw** | 50 | 50 | 0 | 高活跃，工具调用链路、上下文压缩、MCP 发现、SOP/Goal 审批门持续修复 | 快速迭代 + 企业可靠性 |

---

### 3. 研究定位分析

| 项目 | 多模态推理 | 长上下文理解 | post-training 对齐 / AI 可靠性 | 技术路线差异 |
|---|---|---|---|---|
| **OpenClaw** | 修复 UTF-8 截断、渠道入站媒体下载失败；核心关注工具输出与多模态输入可靠性 | 诊断上下文压力零输出、按层级加载 bootstrap 文件、缓存 retention | 幻觉/失败 containment（cron 幻觉、子代理静默丢失、hard gates）、模型回退链 | 以“Agent 运行时工程”约束模型不可预测行为，强调可观测性与可干预性 |
| **NanoBot** | 无直接 VLM 进展；工具输出结构化为错误 | 并发 token 刷新影响长会话 | MCP 工具异常隔离、子代理 MCP 继承、崩溃安全写入 | 工具增强型 Agent 平台，聚焦 MCP 生态的鲁棒性 |
| **PicoClaw** | 无 | Agent 级 `max_tokens` / summarization / `split_on_marker` 覆盖；上下文“失忆” | 多 Agent 路由会话一致性 | 轻量移动/IM 助手，配置正从全局走向按 Agent 精细化 |
| **NanoClaw** | 无 | 会话状态持久化（`inReplyTo` 跨进程）、LiteLLM 路由 | 容器安全边界、审批 UI 欺骗（人机信任）、Phase-1 安全治理 | 安全优先的沙箱化 Agent，强调 human-in-the-loop 可信度 |
| **IronClaw** | 无 | 无 | Agent 循环输出解析、工具披露白名单、错误不可静默吞掉的静态强制 | 编译期/类型系统驱动的失败传播，偏向 Rust 工程化 |
| **CoPaw / QwenPaw** | 多模态能力缓存被 HTTP 400 误判污染并修复 | scroll 压缩导致上下文与 `reasoning_content` 丢失；auto-memory 状态丢失 | 记忆状态持久化、模型 fallback、长会话一致性 | 面向中文 IM/QQ 生态，v2 beta 强调记忆与长上下文压缩 |
| **ZeroClaw** | 无 | 上下文压缩丢弃 tool 消息已修复 | 工具空列表校验、MCP 发现、`<think>` 标签误删、Anthropic refusal、Goal/SOP 审批门 | 企业工作流/SOP 导向，强调推理阶段对齐与合规可追溯 |
| **LobsterAI** | 附件上传 UI 阻塞 | 无 | 技能生成黑盒阻塞、同模型不同入口理解偏差 | 低活跃，问题集中在可观测性与跨组件一致性 |

---

### 4. 共同关注的技术方向

| 方向 | 涉及项目 | 具体诉求 |
|---|---|---|
| **MCP / 工具集成可靠性** | OpenClaw、NanoBot、IronClaw、ZeroClaw | 工具异常结构化（NanoBot #4666）、MCP 重连不崩溃（NanoBot #4302）、TUI 工具发现（ZeroClaw #8193）、工具输出避免被渲染为图片（OpenClaw #99241）、空 `tools` 参数校验（ZeroClaw #7862） |
| **长上下文管理与记忆一致性** | OpenClaw、PicoClaw、CoPaw、ZeroClaw、NanoClaw | 上下文压力零输出可视化（OpenClaw #100115）、Agent 级 summarization 阈值（PicoClaw #3225）、scroll 压缩丢失上下文（CoPaw #5778）、auto-memory 状态持久化（CoPaw #5775）、上下文压缩保留 tool 消息（ZeroClaw #6361） |
| **幻觉与失败静默传播** | OpenClaw、NanoBot、CoPaw、ZeroClaw | cron 工具失败却生成幻觉输出（OpenClaw #49876）、子代理结果静默丢失（OpenClaw #44925）、多模态能力缓存误判降级（CoPaw #5772）、`<think>` 标签误删与 refusal 处理（ZeroClaw） |
| **多 Agent 编排与路由** | OpenClaw、PicoClaw、IronClaw、ZeroClaw | 并发配置覆盖与 session-lock 失败（OpenClaw #43367）、`/clear` 路由清理错误（PicoClaw #3224）、子 Agent 门控与工具继承（IronClaw、NanoBot） |
| **人机信任与审批完整性** | NanoClaw、ZeroClaw | `ask_user_question` 卡片可被伪造点击篡改（NanoClaw #2923）、SOP 审计 key 缺失（ZeroClaw #6689）、Goal 模式拆分 Tracker（ZeroClaw #8681） |

---

### 5. 差异化定位分析

| 维度 | 头部代表 | 关键差异 |
|---|---|---|
| **生态定位** | OpenClaw | 作为“核心参照”运行时，覆盖最广的 provider/channel 矩阵，强调 Agent 运行时工程与模型行为约束。 |
| **工具增强 Agent** | NanoBot | 以 MCP 

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 项目日报 · 2026-07-05

## 1. 今日速览
过去 24 小时 NanoBot 维持中高频工程迭代：Issues 更新 3 条（1 开 2 关）、PRs 更新 12 条（5 待合并 7 已合并/关闭），无新版本发布。从研究视角看，**当日没有直接涉及视觉语言能力、长上下文训练或幻觉缓解的学术/算法向提交**，但有多项与 **AI 可靠性（AI reliability）** 和 **工具增强推理（tool-augmented reasoning）** 相关的基础设施修复：包括 MCP 工具异常隔离、子代理工具继承、并发令牌刷新竞态、崩溃安全写入等。这些改进虽不直接改变模型能力，却对多智能体推理稳定性、模型-工具交互边界有直接影响。

---

## 2. 版本发布
**无。** 过去 24 小时未发布任何 Release。

---

## 3. 项目进展（与研究/可靠性相关）

| PR | 状态 | 研究/可靠性意义 |
|---|---|---|
| [#4666](https://github.com/HKUDS/nanobot/pull/4666) `fix(mcp): contain malformed tool results` | 已关闭 | 将 MCP 工具执行异常（超时、取消、重试失败、执行错误）封装为结构化工具错误，避免进程崩溃；对工具增强推理的鲁棒性有直接提升。 |
| [#4684](https://github.com/HKUDS/nanobot/pull/4684) `fix(copilot): guard token refresh with asyncio.Lock` | 已关闭 | 修复并发请求下 GitHub Copilot token 刷新竞态，减少长上下文/多轮对话中因并发调用导致的鉴权失败。 |
| [#4653](https://github.com/HKUDS/nanobot/pull/4653) `fix(pairing): restore durable atomic writes` | 已关闭 | 恢复崩溃安全原子写入，防止配置/配对数据在异常退出时损坏。 |
| [#4690](https://github.com/HKUDS/nanobot/pull/4690) `fix(gateway): handle Windows stop fallback` | 已关闭 | 提升 gateway 在 Windows 下停止指令的健壮性。 |
| [#4646](https://github.com/HKUDS/nanobot/pull/4646) `fix(dingtalk): stop stream task on shutdown` | 已关闭 | 修复 DingTalk 通道关闭时流任务未取消导致的资源泄漏。 |
| [#4692](https://github.com/HKUDS/nanobot/pull/4692) `fix(config): serialize model presets as camelCase` | 已关闭 | 统一模型预设字段序列化，降低配置解析歧义。 |

**待合并/开放中、值得关注：**
- [#4697](https://github.com/HKUDS/nanobot/pull/4697) `feat(subagent): configurable MCP inheritance for specialist subagents`：允许子代理按配置继承主代理的 MCP 工具，有望显著提升多智能体任务分解与工具调用能力。
- [#4696](https://github.com/HKUDS/nanobot/pull/4696) `Smooth WebUI streaming Markdown reveal`：优化流式输出渲染，减少 Markdown 标记闪烁，对长上下文对话体验有边际改善。

---

## 4. 社区热点
- **[#4302](https://github.com/HKUDS/nanobot/issues/4302)** `nanobot gateway crashes after mcp reconnect`（开放，2 评论）  
  这是与 MCP 会话生命周期相关的高频崩溃问题，开发者已定位到 gateway 层，修复诉求强烈。
- **[#4652](https://github.com/HKUDS/nanobot/issues/4652)** `Nanobot process crashes directly when MCP tool call exception`（已关闭，3 评论）  
  反映社区对“MCP 工具异常不应拖垮整个进程”的共识，已在 #4666 中修复。
- **[#4677](https://github.com/HKUDS/nanobot/issues/4677)** `GitHub Copilot: token refresh race condition under concurrent requests`（已关闭，1 评论）  
  并发场景下的可靠性问题，已在 #4684 中修复。

**背后诉求：** 用户当前最关注的不是新模型能力，而是 **MCP 工具集成与并发调用时的稳定性**。

---

## 5. Bug 与稳定性
按严重程度排列：

| 优先级 | 问题 | 状态 | 修复 PR |
|---|---|---|---|
| P1 | [#4302](https://github.com/HKUDS/nanobot/issues/4302) MCP 重连后 gateway 崩溃 | **开放** | 暂无 |
| P1 | [#4652](https://github.com/HKUDS/nanobot/issues/4652) MCP 工具异常导致主进程崩溃 | 已关闭 | [#4666](https://github.com/HKUDS/nanobot/pull/4666) |
| P1 | [#4677](https://github.com/HKUDS/nanobot/issues/4677) Copilot token 刷新并发竞态 | 已关闭 | [#4684](https://github.com/HKUDS/nanobot/pull/4684) |
| P2 | [#4690](https://github.com/HKUDS/nanobot/pull/4690) `nanobot gateway stop` 在 Windows 下回退失败 | 已关闭 | 同 PR |
| P2 | [#4646](https://github.com/HKUDS/nanobot/pull/4646) DingTalk 关闭时流任务未取消 | 已关闭 | 同 PR |

**关键观察：** P1 级问题中仅 #4302 仍未解决，是当前最大的稳定性风险。

---

## 6. 功能请求与路线图信号
- **子代理 MCP 工具继承（[#4697](https://github.com/HKUDS/nanobot/pull/4697)）**  
  这是当日最具“研究/架构”意义的开放 PR。它允许子代理根据配置继承主代理的 MCP 服务器，改变当前“子代理只能使用 exec/web/file 内置工具”的限制，对 **多智能体分工、专业化子代理、工具调用链推理** 都有正向作用，纳入下一版本的概率较高。
- **Mattermost 通道支持（[#4459](https://github.com/HKUDS/nanobot/pull/4459)）**  
  已开放 13 天，属于社区集成扩展，对研究主线影响有限。
- **流式 Markdown 渲染（[#4696](https://github.com/HKUDS/nanobot/pull/4696)）**  
  提升生成式输出的可读性，属于体验增强。
- **OAuth 错误信息标准化（[#4698](https://github.com/HKUDS/nanobot/pull/4698)）**  
  降低多 Provider 接入的调试成本。

**研究向判断：** 当日没有提出新的视觉语言、训练或幻觉缓解相关功能请求。

---

## 7. 用户反馈摘要
- **痛点 1：MCP 工具异常会级联崩溃。** 用户希望错误被隔离为结构化工具错误，而非直接终止进程。
- **痛点 2：MCP 会话重连后 gateway 不稳定。** 长时间运行或超时后重连容易触发崩溃。
- **痛点 3：并发调用 Copilot 时 token 刷新冲突。** 高并发多轮对话场景下出现鉴权失败。
- **场景共性：** 当前用户主要将 NanoBot 作为 **工具增强型 Agent 平台** 使用，稳定性与工具边界处理比新增模型能力更紧迫。
- **满意度：** 对已关闭的 #4652、#4677 修复响应速度较为正面；对尚未修复的 #4302 存在持续关注。

---

## 8. 待处理积压
以下 Issue/PR 已超过一个迭代周期或属于当日开放但尚未合并，需维护者优先关注：

| 链接 | 类型 | 说明 |
|---|---|---|
| [#4302](https://github.com/HKUDS/nanobot/issues/4302) | Bug / P1 | **最长开放**，MCP 重连 gateway 崩溃，尚无 fix PR |
| [#4459](https://github.com/HKUDS/nanobot/pull/4459) | Enhancement | Mattermost 通道支持，已开放 13 天 |
| [#4697](https://github.com/HKUDS/nanobot/pull/4697) | Feature / P1 | 子代理 MCP 继承，对 Agent 架构有重要影响 |
| [#4694](https://github.com/HKUDS/nanobot/pull/4694) | Bug / P2 | WebUI 窄视口布局问题 |
| [#4698](https://github.com/HKUDS/nanobot/pull/4698) | Fix | OAuth 错误信息标准化 |

---

**研究建议：** 若希望 NanoBot 在视觉-语言推理、长上下文对齐或幻觉评测方面产生实质进展，社区需要在该仓库中提交更多针对多模态输入、模型后训练/对齐、事实性/引用可验证性（citation grounding）的 Issue 或 PR。当前 24 小时数据仍以“AI 可靠性基础设施”为主。

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目日报（2026-07-05）

**数据口径**：Issues 4 条（新开/活跃 3，关闭 1）、PR 7 条（待合并 5，已合并/关闭 2）、Release 0 个。  
**研究视角筛选**：今日与“视觉语言能力、推理机制、训练方法论、幻觉”直接相关的内容极少；多数更新集中在加密库、移动端、Docker/i18n 等工程维护。以下报告在保留项目健康度评估的同时，重点标注了与研究议题相关的信号。

---

## 1. 今日速览

今日 PicoClaw 整体活跃度偏低，新增贡献以维护性 PR 与历史 Issue 的 stale 更新为主。研究相关的实质性进展仅有两条：一是修复了多 Agent 路由场景下的 `/clear` 会话清理错误，二是提出按 Agent 独立配置 `max_tokens`、summarization 阈值与 `split_on_marker` 的运行时覆盖。这两个点都与“长上下文管理”和“Agent 可靠性”相关。视觉语言能力（VLM）、模型训练/对齐方法、幻觉评测等方向今日没有可见信号。

---

## 2. 版本发布

**无新版本发布。**

---

## 3. 项目进展

- **PR #3224 — fix(agent): clear routed agent session**（已合并/关闭）  
  修复了多 Agent 配置下 `/clear` 命令误清理“默认 Agent”会话而非“当前路由 Agent”会话的问题。  
  研究意义：属于多 Agent 路由与会话状态一致性，对 Agent 推理的上下文可靠性和用户可控性有直接影响。  
  https://github.com/sipeed/picoclaw/pull/3224

- **PR #3225 — Support agent-specific runtime overrides**（待合并）  
  允许在 `agents.list` 中为每个 Agent 独立设置 `max_tokens`、summarization 阈值与 `split_on_marker`，并在构建 `AgentInstance` 时应用。  
  研究意义：这是今日唯一明确触及“长上下文管理”与“推理 token 预算”的改动，可用于控制长对话压缩/截断策略，对长上下文理解研究有参考价值。  
  https://github.com/sipeed/picoclaw/pull/3225

---

## 4. 社区热点

- **Issue #3088 — [Feature] use vodozemac instead of libolm**（开放，高优先级，stale，👍 2，评论 4）  
  诉求：libolm 已被官方废弃且存在安全问题，社区希望迁移到 Matrix 官方替代品 vodozemac。  
  研究相关性：偏低，属于加密/安全基础设施；但它是今日反馈最活跃的功能请求，体现用户对端到端安全与可维护性的关注。  
  https://github.com/sipeed/picoclaw/issues/3088

- **Issue #3150 — [BUG] 它给自己整失忆了**（已关闭，stale，评论 4）  
  标题直指“AI 失忆”，即对话上下文/记忆丢失问题，属于长上下文理解与可靠性议题。该 Issue 被 stale 关闭，未看到后续修复或根因分析。  
  https://github.com/sipeed/picoclaw/issues/3150

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | 相关修复 |
|---|---|---|---|
| 高 | **Issue #3182** — Android 版无法启动服务，路径设置也无法更改 | 开放，无修复 PR | 无 |
| 高 | **Issue #3194** — Matrix 收到加密消息但 crypto 未启用 | 开放，无修复 PR | 无 |
| 中 | **Issue #3150** — AI “失忆”/上下文丢失 | 已关闭（stale），未修复 | 无 |
| 中 | **PR #3224** — `/clear` 在多 Agent 路由下清理错误会话 | 已合并 | 已修复 |

- **Issue #3182** https://github.com/sipeed/picoclaw/issues/3182  
- **Issue #3194** https://github.com/sipeed/picoclaw/issues/3194  
- **Issue #3150** https://github.com/sipeed/picoclaw/issues/3150  

---

## 6. 功能请求与路线图信号

- **端到端加密库迁移**（Issue #3088）：高优先级且已被标记 `help wanted`，若被纳入下一版本，将主要提升安全与合规性，而非模型能力。  
  https://github.com/sipeed/picoclaw/issues/3088

- **Agent 级运行时覆盖**（PR #3225）：如果合并，意味着项目开始从“单一全局配置”走向“按 Agent 精细化配置”。其中 `summarization` 阈值与 `split_on_marker` 可用于实验不同的长上下文压缩/分段策略，对研究长上下文对话有工具价值。  
  https://github.com/sipeed/picoclaw/pull/3225

- **其他维护性 PR**：`alpine` 镜像升级、`.gitignore` 清理、i18n 键补齐、LINE SDK 错误忽略等，与研究目标无关，但对工程健康度有帮助。

---

## 7. 用户反馈摘要

- **移动端受阻**：Android 用户因服务无法启动而无法使用，且设置中无法更改路径。
- **加密体验断裂**：Matrix 用户在已收到加密消息时系统提示 crypto 未启用，导致消息无法处理。
- **AI 记忆与上下文可靠性**：Issue #3150 的“失忆”表述反映了用户对长对话上下文保持能力的担忧，目前未获得技术性回应。
- **多 Agent 使用痛点**：用户期望 `/clear` 作用于当前正在对话的 Agent，而非回退到默认 Agent。
- **安全依赖焦虑**：社区明确希望移除 libolm，转向官方维护的 vodozemac。

---

## 8. 待处理积压

以下 Issue/PR 已标记 stale 或长期无维护者响应，建议优先关注：

- **Issue #3088**（vodozemac 迁移，高优先级，stale）  
  https://github.com/sipeed/picoclaw/issues/3088

- **Issue #3194**（Matrix 加密状态异常，stale）  
  https://github.com/sipeed/picoclaw/issues/3194

- **Issue #3150**（上下文“失忆”，已关闭但无修复）  
  https://github.com/sipeed/picoclaw/issues/3150

- **PR #3190**（i18n 键补齐，stale）  
  https://github.com/sipeed/picoclaw/pull/3190

- **PR #3189**（LINE 通道错误处理，stale）  
  https://github.com/sipeed/picoclaw/pull/3189

---

**研究侧小结**：今日 PicoClaw 的代码动态对“多模态视觉语言”和“训练/后训练对齐”几乎没有新增信息；最值得记录的是 **Agent 级上下文预算与 summarization 配置**（PR #3225）以及 **上下文失忆/会话可靠性**（Issue #3150、PR #3224），均可纳入“长上下文理解”与“AI 可靠性”跟踪清单。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

**NanoClaw 项目日报 · 2026-07-05**

*筛选范围：视觉语言能力、推理机制、训练方法论、幻觉 / 可信度 / 对齐相关议题。今日仓库未出现新的视觉-语言模型或训练框架代码，但有多项与多智能体系统可靠性、交互完整性和安全边界直接相关的修复，值得关注。*

---

### 1. 今日速览

过去 24 小时内，NanoClaw 仓库活跃度较高，共有 **38 个 PR 更新**（16 个待合并、22 个已合并/关闭）和 **1 个新 Issue**（开放），但**无新版本发布**。今日活动主题集中在**安全边界加固、运行时状态一致性、文档债务清理与运维工具扩展**，未出现直接针对模型能力或训练方法的 PR。唯一新增 Issue #2923 是一则**高严重性的 UI 完整性/显示欺骗漏洞**，可能影响用户在人机回环（human-in-the-loop）审批场景中的信任。整体来看，项目处于“维护与加固”阶段，代码健康度有所改善，但安全类未修复问题需要尽快得到维护者响应。

---

### 2. 版本发布

今日无新版本发布，省略。

---

### 3. 项目进展

今日已合并或关闭的 PR 主要推进了以下三个方向：

**安全边界与可信运行**
- 重写安全文档以匹配 v2 容器边界，并将两个仅适用于 v1 的指南标记为历史文档（[#2945](https://github.com/nanocoai/nanoclaw/pull/2945)）。
- 移除已废弃的 `data/env/env` 环境变量镜像，避免敏感凭证在无效路径中被写入（[#2946](https://github.com/nanocoai/nanoclaw/pull/2946)）。
- 挂载白名单现在正确识别 `readOnly` 与 `nonMainReadOnly` 配置，并停止对解析错误进行长期缓存，减少策略漂移（[#2943](https://github.com/nanocoai/nanoclaw/pull/2943)）。
- 将出口锁定（egress lockdown）与容器资源限制的环境变量接入统一的 `readEnvFile` 配置路径，使 shipped service 能正确读取安全策略（[#2934](https://github.com/nanocoai/nanoclaw/pull/2934)）。

**状态一致性与跨进程可靠性**
- 修复 agent-to-agent 的 `inReplyTo` 戳在跨进程场景下失效的问题：将状态从模块级内存迁移到 `session_state`/`outbound.db`，使 poll 循环与 MCP 工具能正确读取（[#2942](https://github.com/nanocoai/nanoclaw/pull/2942)）。
- 当会话文件夹被手动删除（如按 `/debug` 重置）后，`writeSessionMessage` 会自动重新初始化文件夹与数据库，避免文档化流程失效（[#2937](https://github.com/nanocoai/nanoclaw/pull/2937)）。

**模型路由与技能生态**
- 新增 `/add-litellm` 最小模型路由技能，支持本地服务器与可选的 LLM 后端切换，反映社区对多模型推理入口的需求（[#2949](https://github.com/nanocoai/nanoclaw/pull/2949)）。

---

### 4. 社区热点

由于今日新增 Issue 仅 1 条，且 PR 评论数未显示明显高峰，社区焦点集中在**安全与运维治理**：

- **[Issue #2923]** 报告称 `ask_user_question` 卡片在源端授权检查前可被伪造点击篡改显示文本（例如把标签改为 `<selectedLabel> — <attacker name>`），属于显示完整性欺骗（[#2923](https://github.com/nanocoai/nanoclaw/issues/2923)）。
- **[PR #2954]** 正在起草 Phase-1 安全报告与分类政策，呼应 #2651 中提出的 triage 框架，显示维护者希望把安全贡献流程制度化（[#2954](https://github.com/nanocoai/nanoclaw/pull/2954)）。
- **[PR #2949]** 与 **[PR #2952]** 关于 LiteLLM 路由与 OpenCode 技能栈，反映用户希望 NanoClaw 能适配更开放的本地/多模型后端，降低对单一商业模型的依赖。

这些信号说明社区当前的核心诉求是：**提升系统在审批与交互场景中的可信度，并扩展模型后端的灵活性。**

---

### 5. Bug 与稳定性

按严重程度排序：

| 严重度 | 问题 | 状态 |
|--------|------|------|
| **高** | `ask_user_question` 卡片可被伪造点击篡改显示文本，造成用户在审批界面看到错误信息（[#2923](https://github.com/nanocoai/nanoclaw/issues/2923)） | **尚无 fix PR** |
| **中** | `mention-sticky` 分支误将 bare session 存在视为订阅状态，导致未真正参与过的频道或仅累积会话被错误订阅（[#2955](https://github.com/nanocoai/nanoclaw/pull/2955)） | **修复 PR 开放中** |
| **中** | 跨进程场景下 agent-to-agent 的 `inReplyTo` 戳失效，已通过状态持久化修复（[#2942](https://github.com/nanocoai/nanoclaw/pull/2942)） | **已合并** |
| **中** | 挂载白名单忽略 `readOnly` 并缓存解析错误，可能导致安全策略错误生效（[#2943](https://github.com/nanocoai/nanoclaw/pull/2943)） | **已合并** |
| **中** | 待审批请求在投递失败或长期未处理时不会过期，造成数据堆积（[#2944](https://github.com/nanocoai/nanoclaw/pull/2944)） | **修复 PR 开放中** |
| **低** | 手动删除会话文件夹后，文档中的重置流程失效，已自动重新初始化（[#2937](https://github.com/nanocoai/nanoclaw/pull/2937)） | **已合并** |

---

### 6. 功能请求与路线图信号

结合今日 PR 与 Issue，可推断以下方向可能进入后续版本：

1. **多模型/模型路由支持**：`add-litellm` 技能（[#2949](https://github.com/nanocoai/nanoclaw/pull/2949)）暗示官方或社区希望引入统一的 LLM 路由层，便于在本地服务器与商业 API 之间切换，这对**推理机制的可控性**和**幻觉调试**有直接帮助。
2. **开放代码栈集成**：OpenCode 相关技能（[#2952](https://github.com/nanocoai/nanoclaw/pull/2952)、[#2951](https://github.com/nanocoai/nanoclaw/pull/2951)）表明对开源/本地化开发工作流的支持在加强。
3. **安全治理制度化**：Phase-1 安全报告政策（[#2954](https://github.com/nanocoai/nanoclaw/pull/2954)）与 v2 安全文档（[#2945](https://github.com/nanocoai/nanoclaw/pull/2945)）共同指向“安全优先的运维路线图”。
4. **审批 UI 可信度**：彩色按钮（[#2933](https://github.com/nanocoai/nanoclaw/pull/2933)）与 #2923 的 UI 欺骗问题都说明官方关注人机回环中的**显示完整性与用户信任**，未来可能会有更严格的审批卡片签名/验证机制。

---

### 7. 用户反馈摘要

从今日 Issue 与 PR 描述中提炼的真实痛点：

- **信任问题**：用户在审批场景中担心看到的按钮/标签并非来自真实模型响应，而是可被伪造修改（#2923）。这属于“幻觉/欺骗”风险的人机交互延伸。
- **文档过时**：SECURITY.md 与 mount topology 描述仍停留在 v1 架构，给新部署者造成误导（#2945、#2953）。
- **运维流程断裂**：`/debug` 技能推荐的 `rm -rf` 重置方式会导致后续写入失败，直到 #2937 修复。
- **配置不可达**：安全策略环境变量在 shipped service 模式下读取不到，使 egress lockdown 等机制形同虚设（#2934）。
- **审批 UX 不直观**：Approve/Reject 按钮样式相同，已通过 Slack 的 `primary`/`danger` 样式改进（#2933）。

---

### 8. 待处理积压

以下开放 Issue 与 PR 需要维护者优先关注：

- **Issue #2923**：高严重性 UI 欺骗安全漏洞，目前**0 评论、0 assignee**，应尽快复现并分配修复（[#2923](https://github.com/nanocoai/nanoclaw/issues/2923)）。
- **PR #2955**：`mention-sticky` 订阅状态错误修复，已开放待审阅，涉及会话状态与消息路由正确性（[#2955](https://github.com/nanocoai/nanoclaw/pull/2955)）。
- **PR #2954**：Phase-1 安全报告政策，需两个维护者 sign-off，当前仍为 draft（[#2954](https://github.com/nanocoai/nanoclaw/pull/2954)）。
- **PR #2944**：待审批请求过期清理，关系到系统长期运行时的数据库健康与审批状态一致性（[#2944](https://github.com/nanocoai/nanoclaw/pull/2944)）。
- **PR #2949 / #2951 / #2952**：新技能与模型路由相关，属于社区贡献，需评估是否纳入核心能力或保持为独立 skill（[#2949](https://github.com/nanocoai/nanoclaw/pull

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw 项目日报（2026-07-05）

> **研究范围过滤说明**：今日仓库活跃度较高（9 条 Issue、50 条 PR），但内容高度集中在 CI/基础设施、Slack OAuth 集成与状态迁移。按“视觉语言能力、推理机制、训练方法论、幻觉/可靠性”四项研究主题筛选后，**未发现**视觉语言或多模态训练相关条目；可直接归入研究信号的主要是**Agent 推理循环、工具披露、错误传播与测试可靠性**类更新。

---

## 1. 今日速览

- 过去 24 小时项目活跃度处于高位，共有 **9 条 Issue**（8 开/活跃、1 关闭）和 **50 条 PR**（30 待合并、20 已合并/关闭）更新。
- **今日无新版本发布**，无模型版本或训练框架 release。
- 与研究主题相关的信号集中在 **Agent 推理可靠性**：包括单轮回答被误判为 transcript 回显的修复、子 Agent 运行门控、final-answer nudge 的交互式启用，以及 bridged tool disclosure 的能力白名单缺陷。
- 多个新打开的 PR（#5651、#5652）试图把“错误不可被静默吞掉”从设计文档提升为编译期强制，这对 AI 系统的可解释性和故障传播研究有直接意义。
- 整体项目健康度：主干 CI 已恢复绿色（#5590 关闭），但 nightly E2E（#4108）和若干测试/覆盖基础设施的漂移问题仍是未清风险。

---

## 2. 项目进展

今日关闭/合并的 PR 中，与研究直接相关的较少，具体如下：

- **#5042 — [已关闭] fix(agent-loop): 修复单行回答包含 `__` 工具名时被误判为 transcript 回显的问题**  
  该问题导致模型真实最终回答被丢弃，属于 Agent 推理输出解析与可靠性缺陷。  
  https://github.com/nearai/ironclaw/pull/5042

- **#5383 — [已关闭] docs: Reborn 错误可恢复性审计与修复计划**  
  为 #5651/#5652 的编译期错误暴露策略提供了路线图，对“模型/用户可见的失败”研究有方法论意义。  
  https://github.com/nearai/ironclaw/pull/5383

- **#5590 — [已关闭] 修复 main 分支 CI 变红问题**  
  稳定性基础修复，非研究功能，但支撑后续可重复实验。  
  https://github.com/nearai/ironclaw/issues/5590

- 其余已关闭 PR（#5627 状态迁移、#5635/#5629/#5606 CI 加速）均为基础设施/工程迁移，未纳入本研究摘要。

---

## 3. 社区热点

今日 Issue/PR 评论区数据均为 `0` 或未定义，因此**没有形成显著的研究讨论热点**。但从更新频率看，以下开放 PR 与研究主题相关且值得跟踪：

- **#5651 / #5652 — 错误暴露的静态强制**  
  将 `unused_must_use` 提升为 workspace-wide deny，并配套静态保证“失败必须上浮到模型/用户”，是今日最受关注的可靠性议题。  
  https://github.com/nearai/ironclaw/pull/5651  
  https://github.com/nearai/ironclaw/pull/5652



</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目日报 · 2026-07-05

## 1. 今日速览
- **活跃度极低**：过去 24 小时仅 1 条 Issue 更新、3 条 PR 更新（2 条关闭，1 条仍为开放/stale），无新版本发布。
- **研究相关进展空白**：今日无直接涉及视觉语言、推理机制、训练方法论或幻觉治理的提交/讨论。
- **社区信号集中在工程稳定性与可观测性**：两条核心议题均为 UI/UX 阻塞（附件上传无响应）和 Agent 技能生成过程不可见/理解偏差。
- **整体健康度**：项目处于维护静默期，核心问题长期未响应，需关注 stale 积压。

---

## 2. 版本发布
- **无**

---

## 3. 项目进展
今日关闭/合并的 PR 共 2 条，均为运维与配置治理，未进入核心模型/算法层面：

| PR | 作者 | 关键内容 | 研究/可靠性意义 |
|---|---|---|---|
| **#2272** | fisherdaddy | 将遗留的 `AGENTS.md` 身份块迁移到 `IDENTITY.md`，支持备份与安全跳过/失败报告 | 减少多 Agent 身份配置冲突，提升 Agent 系统的一致性与可维护性 |
| **#2271** | fisherdaddy | 将系统代理传播到托管浏览器 | 改善网络环境一致性，降低因代理配置遗漏导致的运行时失败 |

- **链接**  
  - #2272: https://github.com/netease-youdao/LobsterAI/pull/2272  
  - #2271: https://github.com/netease-youdao/LobsterAI/pull/2271

---

## 4. 社区热点
今日无高互动讨论。唯一带评论的议题是：

- **#1352 [OPEN][stale] 任务对话框，任务运行中，附件无法上传（点击上传附件无反应）**  
  - 作者：devilszy | 评论：1 | 👍：0  
  - 链接：https://github.com/netease-youdao/LobsterAI/issues/1352  
  - **诉求分析**：用户在进行任务交互时遇到附件上传按钮失灵的 UI 阻塞，反映出前端事件处理或上传组件状态管理存在缺陷，对多模态/长上下文工作流（附件上传）构成直接体验阻碍。

---

## 5. Bug 与稳定性
按严重程度排序：

| 严重度 | 问题 | 状态 | 说明 |
|---|---|---|---|
| **高** | **#1350 skills 文件长时间生成阻塞，无中间态，用户无法继续** | 开放/stale（自 2026-04-02） | 技能生成过程无进度、无报错、无取消机制，属于典型的 Agent 可观测性缺失 |
| **高** | **#1350 同模型不同入口理解能力不一致** | 开放/stale | 相同提示词在 Openclaw 可正确生成 skills，在 skill-creator 中理解偏差，可能指向 prompt/后处理对齐或工具链调用差异 |
| **中** | **#1352 任务运行中附件上传无响应** | 开放/stale | 前端交互 Bug，影响多模态输入任务 |
| **已修复** | **#2271 系统代理未传递到托管浏览器** | 已关闭 | 网络环境稳定性修复 |

- **链接**  
  - #1350: https://github.com/netease-youdao/LobsterAI/pull/1350  
  - #1352: https://github.com/netease-youdao/LobsterAI/issues/1352

---

## 6. 功能请求与路线图信号
- **Agent 执行过程可观测性**：#1350 强烈暗示需要引入流式进度展示、中间思考/动作状态、超时/取消机制。
- **跨组件一致性对齐**：#1350 中“同模型不同入口理解有偏差”提示 skill-creator 与 Openclaw 在系统提示、工具链或后训练对齐上存在不一致，需统一推理路径与评估标准。
- **多模态附件上传健壮性**：#1352 要求在任务运行态下仍可靠上传附件，前端需支持异步文件处理与状态反馈。

---

## 7. 用户反馈摘要
- **痛点 1：黑盒式阻塞** — 技能生成长时间无响应，用户不知道模型是否在工作、是否出错、能否中断。
- **痛点 2：理解能力不稳定** — 同一模型在不同功能入口表现不一致，削弱用户对系统可靠性的信任。
- **痛点 3：UI 交互失效** — 任务运行中附件上传按钮无反应，打断多模态任务流程。
- **场景**：用户在通过 skill-creator 构建自定义技能并保存到本地空间时，遇到生成阻塞和理解偏差；在任务对话框中上传附件时遇到 UI 失灵。

---

## 8. 待处理积压
- **#1350**（开放/stale，2026-04-02 创建）：技能生成阻塞 + 理解偏差，涉及可观测性、对齐一致性与用户体验，建议优先评估是否纳入下一迭代。  
  https://github.com/netease-youdao/LobsterAI/pull/1350
- **#1352**（开放/stale，2026-04-02 创建）：附件上传无响应，直接影响多模态任务输入，需前端团队跟进。  
  https://github.com/netease-youdao/LobsterAI/issues/1352

---

**研究视角提示**：今日数据未包含视觉语言、推理机制、训练方法论或幻觉治理方面的直接进展。建议维护者在后续迭代中增加技能生成过程的中间推理日志与一致性评估，以支撑多模态推理与 AI 可靠性的研究目标。

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw（QwenPaw）研究动态日报 — 2026-07-05

> 本摘要聚焦 **多模态推理、长上下文理解、post-training 对齐、AI 可靠性** 相关信号，已过滤纯 UI/商业类更新。

---

## 1. 今日速览

过去 24 小时仓库活跃度较高：共更新 **10 条 Issues**（新开/活跃 8 条、关闭 2 条）和 **3 条 PR**（均待合并），无新版本发布。研究层面最值得关注的是：**多模态能力缓存误伤问题已修复关闭**（[#5772](https://github.com/agentscope-ai/QwenPaw/issues/5772)），但 **scroll 上下文压缩导致长对话记忆丢失与推理内容丢失**（[#5778](https://github.com/agentscope-ai/QwenPaw/issues/5778)）和 **auto-memory 状态在每次请求重建 agent 时丢失**（[#5775](https://github.com/agentscope-ai/QwenPaw/issues/5775)）成为新的稳定性风险。整体处于 v2.0.0b3 的迭代收尾期，长上下文与记忆可靠性是社区当前最突出的焦虑点。

---

## 2. 版本发布

**无新版本发布。** 当前社区主要围绕 `2.0.0b3` 与 `1.1.12` 两个版本进行问题反馈和修复验证。

---

## 3. 项目进展

- **已关闭（研究相关）：**  
  - [#5772](https://github.com/agentscope-ai/QwenPaw/issues/5772) `_is_bad_request_or_media_error()` 把所有 HTTP 400 都判定为“媒体拒绝”，导致 LM Studio 切换模型后多模态能力缓存被错误置为 `supports_multimodal=false`，后续图片消息被静默剥离。该问题已关闭，说明视觉-语言能力探测的可靠性已得到一次关键修复。
- **无已合并 PR。** 今日 3 条 PR 仍处于 Open 状态，尚未进入主干。

---

## 4. 社区热点

按讨论热度与研究相关性排序：

1. **[#5778](https://github.com/agentscope-ai/QwenPaw/issues/5778) scroll 压缩后上下文丢失，后续回复完全跑偏**  
   - 评论：1，👍：0，状态：Open  
   - 这是今日最具研究价值的风险：默认 scroll 压缩策略把关键上下文压缩成模糊标题，导致模型“像换了一个人”；同时丢弃 `reasoning_content`，配合 `auto_memory_search` 会触发 API 400。直接指向 **长上下文压缩策略与推理链一致性** 问题。

2. **[#5772](https://github.com/agentscope-ai/QwenPaw/issues/5772) 多模态能力缓存被 HTTP 400 误判污染**  
   - 评论：2，状态：Closed  
   - 反映了视觉-语言模型接入时，对 provider 返回错误的语义理解不足，导致能力检测缓存失效，属于典型的 **多模态可靠性/幻觉式能力降级**。

3. **[#5775](https://github.com/agentscope-ai/QwenPaw/issues/5775) + [#5777](https://github.com/agentscope-ai/QwenPaw/pull/5777) auto-memory 状态丢失**  
   -  issue 评论：2，PR 待合并  
   - 用户发现 `MemoryMiddleware` 状态因每次请求重建 agent 而丢失，导致 `auto_memory_interval` 永不触发。PR #5777 引入 per-session 的 `_auto_memory_turn_states`，是 **长会话记忆持久化** 的关键修复。

---

## 5. Bug 与稳定性

按严重程度排列：

| 等级 | 问题 | 研究关联 | 状态 / Fix PR |
|------|------|----------|---------------|
| **P0** | [#5778](https://github.com/agentscope-ai/QwenPaw/issues/5778) scroll 压缩导致上下文丢失、推理内容丢弃并触发 API 400 | 长上下文理解、推理链完整性、幻觉式偏离 | Open，暂无 fix PR |
| **P1** | [#5775](https://github.com/agentscope-ai/QwenPaw/issues/5775) auto-memory interval 因状态丢失永不触发 | 记忆机制、长会话一致性 | Open，fix PR [#5777](https://github.com/agentscope-ai/QwenPaw/pull/5777) 待合并 |
| **P1** | [#5772](https://github.com/agentscope-ai/QwenPaw/issues/5772) 多模态能力缓存被 HTTP 400 污染 | 视觉语言能力探测、可靠性 | **Closed** |
| **P1** | [#5773](https://github.com/agentscope-ai/QwenPaw/issues/5773) 记忆搜索导致 OpenCode/DeepSeek 渠道超时失败 | 记忆检索与 provider 兼容性 | Open |
| **P2** | [#5776](https://github.com/agentscope-ai/QwenPaw/issues/5776) 长期 IM 会话中旧 pinned 首条消息被当作当前任务 | 长上下文任务追踪、上下文边界 | Open |
| **P2** | [#5771](https://github.com/agentscope-ai/QwenPaw/issues/5771) `model_factory.py` 调试日志误用 WARNING，刷屏且涉及 `aligned_reasoning` | 推理日志、可观测性 | Open |
| **P2** | [#5774](https://github.com/agentscope-ai/QwenPaw/issues/5774) Google Gemini 渠道端点报错 | provider 兼容 | Open |

---

## 6. 功能请求与路线图信号

- **记忆状态管理（已编码）：** PR [#5777](https://github.com/agentscope-ai/QwenPaw/pull/5777) 将 auto-memory 状态从全局标记改为 per-session，预示 v2.0 在 **长会话记忆与 post-training 对齐式记忆调度** 上会更加精细化。
- **模型 fallback（接近合并）：** PR [#5597](https://github.com/agentscope-ai/QwenPaw/pull/5597) 与 UI PR [#5598](https://github.com/agentscope-ai/QwenPaw/pull/5598) 提供 per-agent / 全局的 LLM fallback。这并非训练方法，但属于 **推理阶段可靠性** 的重要基础设施。
- **UI/自定义需求（非研究重点）：** [#2865](https://github.com/agentscope-ai/QwenPaw/issues/2865) 自定义 agent 名称与头像，属于前端体验，暂不纳入研究信号。

---

## 7. 用户反馈摘要

从今日 Issue 中提炼的真实痛点：

- **长上下文压缩不可信：** 用户认为 scroll 策略“把关键信息压缩成模糊标题”，模型后续回复完全偏离任务。这是当前影响 v2.0 可用性的最大反馈。
- **推理内容被不当处理：** 在 thinking 模式下，`reasoning_content` 被压缩丢弃，且与 `auto_memory_search` 组合触发 API 400，说明推理链与记忆系统之间的协议尚未对齐。
- **多模态能力降级隐蔽：** LM Studio 用户反馈图片消息被“静默剥离”，根源是能力缓存错误，导致视觉-语言模型实际上退化成了纯文本模型，且无明显报错。
- **记忆持久化预期落空：** 开启 `auto_memory_interval > 1` 后期望自动沉淀对话记忆，但状态丢失导致完全不触发。
- **长会话任务漂移：** QQ/IM 等长期会话中，旧的首条消息被持续 pinned，模型把旧任务当作当前任务。

---

## 8. 待处理积压

- **[#5778](https://github.com/agentscope-ai/QwenPaw/issues/5778)** scroll 压缩导致上下文与推理内容丢失 — 研究优先级最高，尚无 fix PR，需维护者重点关注。
- **[#5775](https://github.com/agentscope-ai/QwenPaw/issues/5775)** + **[#5777](https://github.com/agentscope-ai/QwenPaw/pull/5777)** auto-memory 状态丢失 — 已有修复，但 PR 仍未合并，建议尽快 review。
- **[#5773](https://github.com/agentscope-ai/QwenPaw/issues/5773)** 记忆搜索与 OpenCode provider 不兼容 — 仅影响 OCG，但会阻断使用该渠道的深度记忆功能。
- **[#2865](https://github.com/agentscope-ai/QwenPaw/issues/2865)** 自定义 agent 名称/头像 — 4 月初提出，持续活跃，属于长期 UI 体验债。

---

**健康度评估：** 今日活跃度高，关键多模态 bug 已关闭，但长上下文压缩与记忆状态问题对 v2.0 的“长程推理可靠性”构成实质性风险。若 [#5778](https://github.com/agentscope-ai/QwenPaw/issues/5778) 与 [#5777](https://github.com/agentscope-ai/QwenPaw/pull

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 研究动态日报（2026-07-05）

> 分析视角：多模态推理、长上下文理解、post-training 对齐与 AI 可靠性。本报告已过滤掉一般产品/商业更新，聚焦与模型能力、推理机制、训练后对齐及幻觉/输出可靠性相关的技术动态。

---

## 1. 今日速览

过去 24 小时，ZeroClaw 保持高度活跃：Issues 更新 50 条（39 条活跃/新开，11 条关闭），PRs 更新 50 条（48 条待合并，2 条已合并/关闭），但无新版本发布。研究相关的技术焦点集中在**工具调用链路的可靠性**（MCP 发现、上下文压缩、工具参数校验）、**长程推理机制**（Goal mode、SOP 引擎、审批门）、以及**模型输出完整性**（`<think>` 标签误删、Anthropic refusal、高熵误报）。今日未出现直接的训练代码或训练数据相关提交，研究价值主要体现在推理阶段的对齐与部署可靠性。

---

## 2. 版本发布

**无。** 今日未发布新版本（Releases: 0）。

---

## 3. 项目进展

今日关闭的 Issues 中，以下几项直接推动了模型推理与工具调用可靠性：

- **上下文压缩修复**：OpenAI 兼容 provider 在 `context_compression` 中会丢弃 `assistant(tool_calls)` 与 `tool(result)` 消息，导致工具循环和 `invalid message role: system` 错误。该问题已修复。  
  [zeroclaw-labs/zeroclaw#6361](https://github.com/zeroclaw-labs/zeroclaw/issues/6361)

- **空工具列表修复**：OpenAI 兼容 provider 在 `tools` 为空时仍发送 `tool_choice: "auto"`，导致 vLLM 等校验器返回 HTTP 400。已修复。  
  [zeroclaw-labs/zeroclaw#7862](https://github.com/zeroclaw-labs/zeroclaw/issues/7862)

- **SOP 审计可追溯**：生产环境 SOP 审计原本未写入文档承诺的 `sop_run_*` / `sop_step_*` Memory keys，已修复。  
  [zeroclaw-labs/zeroclaw#6689](https://github.com/zeroclaw-labs/zeroclaw/issues/6689)

- **MCP 工具发现修复**：Gateway 能看到 MCP tools，但 Zerocode TUI 会话中缺失，已关闭。  
  [zeroclaw-labs/zeroclaw#8193](https://github.com/zeroclaw-labs/zeroclaw/issues/8193)

- **Memory embedding  provider 配置刷新**：配置变更后 Memory embedding 后端未刷新 provider profile，已修复。  
  [zeroclaw-labs/zeroclaw#8359](https://github.com/zeroclaw-labs/zeroclaw/issues/8359)

---

## 4. 社区热点

| 议题 | 评论数 | 研究相关诉求 |
|------|--------|--------------|
| [zeroclaw-labs/zeroclaw#8193](https://github.com/zeroclaw-labs/zeroclaw/issues/8193) — MCP tools 在 TUI 中不可见 | 15 | 工具发现链路与运行时不一致，直接影响 agent 的“可用工具集”感知，属于工具使用可靠性。 |
| [zeroclaw-labs/zeroclaw#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) — Work Lanes 与 Label 治理 | 13 | 工程治理 RFC，与研究方向间接相关。 |
| [zeroclaw-labs/zeroclaw#8681](https://github.com/zeroclaw-labs/zeroclaw/issues/8681) — Goal mode 实现拆分 Tracker | 7 | 长程目标推理机制正被拆分为可审查 PR，是 agent 推理架构的重要信号。 |
| [zeroclaw-labs/zeroclaw#6361](https://github.com/zeroclaw-labs/zeroclaw/issues/6361) — context_compression 丢弃 tool

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*