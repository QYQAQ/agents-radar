# OpenClaw 生态日报 2026-07-06

> Issues: 500 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-06 00:29 UTC

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

⚠️ 摘要生成失败。

---

## 横向生态对比

# 个人 AI 助手 / 自主智能体开源生态横向对比（2026-07-06）

## 1. 生态全景

本周期内，个人 AI 助手/自主智能体开源生态呈现**“头部高活跃、长尾沉寂”**的分化态势。  
Hermes Agent 与 IronClaw 以日均 50/28 条 PR 或 Issue 的吞吐量处于快速迭代期；NanoBot、CoPaw 等维持中等活跃度，聚焦工程稳定性与社区反馈修复；NullClaw、TinyClaw、Moltis、ZeptoClaw 完全无活动，OpenClaw 与 ZeroClaw 因数据缺失无法评估。研究型信号高度集中在**长上下文管理、工具调用可靠性、Agent 安全边界**三个方向，而视觉语言能力、显式训练/后训练方法论、幻觉定量评估等方向鲜有直接进展。整体而言，生态正从“功能扩展”转向“可靠性加固”。

---

## 2. 各项目活跃度对比

| 项目 | 今日 Issues | 今日 PRs | 今日 Release | 健康度评估 |
|---|---|---|---|---|
| **OpenClaw** | 数据缺失 | 数据缺失 | 0 | ⚠️ 摘要生成失败，无法评估 |
| **NanoBot** | 1 个新 Issue | 17 个（15 开/2 关） | 0 | 中等：工程修复型，MCP/连接器稳定性为主 |
| **Hermes Agent** | 50 条 | 50 条 | 0 | 高：活跃度高，研究-工程并重 |
| **PicoClaw** | 2 条（1 开/1 关） | 5 条（4 开/1 关） | 0 | 低：维护型，仅 AI 可靠性单点突破 |
| **NanoClaw** | 0 条更新 | 6 条（3 合/3 开） | 0 | 低-中：安全层有进展，整体热度不足 |
| **NullClaw** | 0 | 0 | 0 | 无活动 |
| **IronClaw** | 4 条 | 28 条 | 0 | 高：高变动期，E2E 失败仍需关注 |
| **LobsterAI** | 0 条 | 2 条（1 stale） | 0 | 低：沉寂，PR 长期未合并 |
| **TinyClaw** | 0 | 0 | 0 | 无活动 |
| **Moltis** | 0 | 0 | 0 | 无活动 |
| **CoPaw** | 12 条 | 5 条（全 open） | 0 | 中：讨论活跃，但无 PR 合并 |
| **ZeptoClaw** | 0 | 0 | 0 | 无活动 |
| **ZeroClaw** | 数据缺失 | 数据缺失 | 0 | ⚠️ 摘要生成失败，无法评估 |

---

## 3. 研究定位分析

| 项目 | 核心研究/可靠性方向 | 代表性信号 | 技术路线差异 |
|---|---|---|---|
| **Hermes Agent** | 长上下文理解、长期记忆、工具参数保真 | `#59256` 上下文压缩块泄露修复；`#56859` 离线 `mind` Skill；`#59253` 大整数参数保留 | **Skill 生态扩展**：通过可选 Skill 而非核心架构实现记忆与长上下文 |
| **IronClaw** | 推理循环控制、工具安全、长上下文提示组装 | `#5666` 重复工具调用断路器；`#5659` bridge meta-tool allowlist；`#5665` provider JSON 损坏；`#5663` prompt assembly 可观测性 | **系统级安全边界**：Rust 架构、CapabilitySurfaceProfileFilter、Reborn 测试-生产同构 |
| **NanoClaw** | 后训练对齐 / 应用层安全护栏 | `#2726` per-agent-group 输入/输出 guardrails；`#2956` 输出重复投递抑制 | **规则型对齐**：正则/关键词拦截 prompt injection、凭证泄露与主机隔离审计 |
| **PicoClaw

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 项目日报（2026-07-06）

> 研究视角说明：NanoBot 今日仓库活动以工程稳定性、连接器与 MCP/Provider 修复为主。严格意义上，未出现直接针对**视觉语言能力、推理机制、训练方法论或幻觉治理**的研究型更新。以下日报已按研究/可靠性相关度筛选，仅保留与多模态输入可靠性、Agent 可解释性、MCP 工具安全相关的边缘条目，并跳过纯商业/渠道配置噪音。

---

## 1. 今日速览

过去 24 小时，NanoBot 仓库共更新 **17 个 PR**（15 个待合并、2 个已关闭）与 **1 个新 Issue**，无新版本发布。整体活跃度中等，但技术焦点集中在 **MCP 网关稳定性、子代理（subagent）工具继承、执行沙箱安全与渠道消息渲染**。从多模态与 AI 可靠性研究角度看，仅有少量信号：语音转录预处理（PR #4353）涉及多模态输入可靠性，飞书“reasoning panel”（PR #4763）涉及模型推理过程的可视化，其余均为底层基础设施修复。今日仓库健康度尚可，但算法与研究层面的进展较弱。

---

## 2. 版本发布

**无新版本发布。**

---

## 3. 项目进展

今日关闭/合并的 2 个 PR 如下：

- [HKUDS/nanobot#4441](https://github.com/HKUDS/nanobot/pull/4441) **[closed]** `fix(mcp): force-close streamable_http generator on reconnect failure`  
  解决 MCP streamable_http 在断线重连时因 cancel scope 跨任务退出导致网关崩溃的问题。该 PR 已关闭，说明其修复思路已被合并或已被后续方案（如 #4764）

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 研究动态日报 — 2026-07-06

## 1. 今日速览

过去 24 小时内 Hermes Agent 仓库活跃度极高（50 条 Issues、50 条 PRs、0 个 Release），但研究层面直接相关的内容相对有限。多数更新集中在平台适配、网关安全、CLI/TUI 交互与配置路由等工程侧。与多模态推理、长上下文理解与 AI 可靠性相关的信号主要来自三条线：**上下文压缩/长期记忆机制**（#59256、#56859）、**模型在对话中遗忘技能的异常行为**（#15985）、以及**长对话上下文断裂的用户报告**（#5388）。整体项目健康度良好，但研究社区关心的视觉-语言能力、显式训练方法论、幻觉评估等方面在今日数据中几乎没有直接进展。

## 2. 版本发布

今日无新版本发布。

## 3. 项目进展（研究相关 PR）

### 长上下文与上下文压缩机制修复
- **[PR #59256](https://github.com/NousResearch/hermes-agent/pull/59256)** `fix(gateway): strip [CONTEXT COMPACTION] block from user-visible responses`  
  修复了上下文压缩机制的一个关键 UX/可靠性问题：当旧轮次被总结并插入 `[CONTEXT COMPACTION — REFERENCE ONLY]` 交接块时，该块原本可能泄露到用户可见响应中，导致模型内部上下文管理痕迹被用户感知，甚至可能被模型误用。PR 确保该块仅在内部上下文中保留，不进入用户可见输出。这对长上下文对话的稳定性与一致性有直接意义。

### 并发引用展开的容错
- **[PR #59258](https://github.com/NousResearch/hermes-agent/pull/59258)** `fix(context): add return_exceptions to asyncio.gather in reference expansion`  
  在 `asyncio.gather` 中新增 `return_exceptions=True`，避免单个文件/URL 引用展开失败时拖垮整个引用展开流程。这改善了长上下文场景下多源信息聚合的鲁棒性。

### 离线项目记忆 Skill
- **[PR #56859](https://github.com/NousResearch/hermes-agent/pull/56859)** `feat(optional-skills): add mind — brain-like offline project memory skill`  
  引入一个可选 Skill `mind`，为每个项目提供本地、离线、类似大脑结构的长期记忆。该实现仅依赖 Python 标准库，无外部 API，采用加权关联记忆。这属于长上下文理解与 Agent 记忆架构的重要探索。

### 工具参数大整数保留
- **[PR #59253](https://github.com/NousResearch/hermes-agent/pull/59253)** `fix(tools): preserve large integer tool args`  
  修复工具参数强制类型转换时通过 `float()` 解析导致大整数精度丢失的问题（如 Discord/Telegram ID）。现在优先用 `int()` 解析，超出双精度范围的整数不再被静默截断。这直接影响模型调用外部工具时的数据保真度，与推理可靠性相关。

## 4. 社区热点（研究相关讨论）

### 长上下文断裂
- **[Issue #5388](https://github.com/NousResearch/hermes-agent/issues/5388)** `上下文断的`  
  用户报告：同一客户端在未结束对话前补充上下文，发现上下文割裂严重。这是典型的长上下文理解与对话状态一致性问题，已开放三个月仍有待复现与定位。

### 模型遗忘已加载 Skill
- **[Issue #15985](https://github.com/NousResearch/hermes-agent/issues/15985)** `Hermes agent running via ollama launch hermes with gemma 4 seems to forget it has skills`  
  用户通过 Ollama 使用 Gemma 4 时，Hermes Agent 在对话中途似乎“忘记”自己拥有已加载的 Skills。这属于模型行为一致性/指令遵循漂移，与幻觉、状态遗忘等可靠性问题直接相关。

### 轻量级推理工具诉求
- **[Issue #59070](https://github.com/NousResearch/hermes-agent/issues/59070)** `[Feature]: expose auxiliary_client as a one-shot delegate_completion tool`  
  用户希望将 `auxiliary_client` 暴露为一次性 `delegate_completion` 工具，避免纯文本转换任务也走完整的 subagent 循环。这反映了对 Agent 推理架构中“工具调用开销 vs. 任务复杂度”匹配的诉求，属于推理效率与机制设计范畴。

## 5. Bug 与稳定性（研究相关）

| 严重程度 | Issue | 问题 | 状态 |
|---|---|---|---|
| P2 | [#5388](https://github.com/NousResearch/hermes-agent/issues/5388) | 长对话上下文断裂/割裂 | 待复现，无 fix PR |
| P3 | [#15985](https://github.com/NousResearch/hermes-agent/issues/15985) | Gemma 4 模型遗忘已加载 Skills | 开放，无 fix PR |
| P2 | [#55314](https://github.com/NousResearch/hermes-agent/issues/55314) / [#59186](https://github.com/NousResearch/hermes-agent/issues/59186) | 工具参数大整数经 float 静默四舍五入 | 已有 fix PR [#59253](https://github.com/NousResearch/hermes-agent/pull/59253) |
| P2 | [#59235](https://github.com/NousResearch/hermes-agent/issues/59235) | 日志脱敏对拆分后的 secrets 与 traceback 覆盖不全 | 开放，无 fix PR |

## 6. 功能请求与路线图信号

- **[#29914](https://github.com/NousResearch/hermes-agent/issues/29914)** `Add first-class per-turn and per-tool-call model overrides`  
  要求支持每轮/每次工具调用级别的模型覆盖，以实现更细粒度的推理-能力路由。这与训练后对齐、多模型协同推理的方法论相关。

- **[#59070](https://github.com/NousResearch/hermes-agent/issues/59070)** `auxiliary_client as one-shot delegate_completion tool`  
  反映社区对“轻量推理”工具的需求，可能推动 Agent 推理架构从统一 agent-loop 向分层调用演进。

- **[#54864](https://github.com/NousResearch/hermes-agent/issues/54864)** `Surface the actual served / downstream model per response`  
  要求在响应中暴露实际下游模型（而非仅代理别名），这对模型能力评估、可解释性与幻觉溯源有研究价值。

- **[PR #56859](https://github.com/NousResearch/hermes-agent/pull/56859)** 的 `mind` Skill 已作为一个可选离线记忆模块出现，预示 Hermes 可能通过 Skill 生态而非核心架构来探索长期记忆与长上下文能力。

## 7. 用户反馈摘要

- **长上下文痛点**：用户在多轮补充上下文时感受到明显割裂（#5388），说明当前上下文拼接/压缩策略在用户体验层面仍有缺陷。
- **模型可靠性痛点**：Gemma 4 运行下 Skills 被中途遗忘（#15985），显示模型-工具-系统提示的交互稳定性仍是实际使用中的障碍。
- **对透明度的需求**：用户希望看到真正被调用的下游模型（#54864），并避免内部上下文压缩标记泄露到用户界面（#59256）。
- **对效率的需求**：纯文本转换任务不应启动完整 subagent 循环（#59070），社区期待更按需的推理层级。

## 8. 待处理积压

- **[Issue #15985](https://github.com/NousResearch/hermes-agent/issues/15985)** — Gemma 4 遗忘 Skills，已开放逾两个月，涉及模型行为一致性，建议维护者优先复现与定位。
- **[Issue #5388](https://github.com/NousResearch/hermes-agent/issues/5388)** — 上下文断裂，已开放三个月，需要更详细的复现步骤与日志。
- **[Issue #29914](https://github.com/NousResearch/hermes-agent/issues/29914)** — 每轮/每次工具调用模型覆盖，已开放一个半月，是推理路由与训练后对齐的重要需求。

---

**研究视角总结**：今日数据在工程安全与平台适配上非常活跃，但视觉-语言能力、显式训练方法论、幻觉定量评估等方向几乎未见直接进展。长上下文理解、Agent 记忆架构与模型行为可靠性是今日可追踪的主要研究信号。

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目日报（2026-07-06）

> **研究相关性说明**：按“视觉语言能力、推理机制、训练方法论、幻觉/AI 可靠性”进行筛选后，今日仓库中仅有 **Issue #3150 / PR #3226** 涉及模型工具误用与自我破坏性输出，属于 AI 可靠性/幻觉相关议题。其余条目多为依赖升级、构建清理、协议重构等工程维护内容，已作降权或跳过处理。

---

## 1. 今日速览

- 过去 24 小时，PicoClaw 活跃度偏**工程维护型**：2 条 Issue 更新（1 开 1 关）、5 条 PR 更新（4 开 1 关），无新版本发布。
- 研究层面唯一值得关注的信号是 **PR #3226** 针对“AI 把自己写失忆”的破坏性覆盖问题提出修复，直指工具提示词对模型行为的诱导风险。
- 今日没有视觉语言（VLM）能力、推理架构或训练/后训练（post-training）方法论相关的新进展。

---

## 2. 版本发布

无。今日未发布新版本。

---

## 3. 项目进展

- **已关闭/合并的工程项**
  - **PR #3189** —— 关闭并标记为 stale：在 LINE 通道中显式忽略 `resp.Body.Close()` 的返回错误。  
    链接：https://github.com/sipeed/picoclaw/pull/3189  
    *研究相关性低：属于 Go 资源清理的代码风格修复，未触及模型能力或对齐机制。*
  
- **研究相关但尚未合并的修复**
  - **PR #3226** —— 阻止 `write_file` 工具“诱导”模型覆盖已有文件（关联 Issue #3150）。  
    链接：https://github.com/sipeed/picoclaw/pull/3226  
    *这是今日唯一实质推进 AI 可靠性的 PR：通过修改工具描述与覆盖提示，减少模型因 prompt 诱导而自我破坏记忆文件的概率。尚未合并，需进一步 review。*

---

## 4. 社区热点

- **讨论最活跃的 Issue：#3088**  
  链接：https://github.com/sipeed/picoclaw/issues/3088  
  6 条评论、2 个 👍。诉求是用 `vodozemac` 替换已停止维护且存在安全风险的 `libolm`。  
  *研究相关性：属于密码学依赖安全，不在 VLM/推理/训练/幻觉聚焦范围内。*

- **研究侧热点：Issue #3150 + PR #3226**  
  Issue：https://github.com/sipeed/picoclaw/issues/3150  
  PR：https://github.com/sipeed/picoclaw/pull/3226  
  5 条评论，主题为 **“它给自己整失忆了”**——即 agent 将自身记忆文件 `memory/MEMORY.md` 覆盖，导致上下文丢失。PR #3226 提出修复方案，核心诉求是：**不要让工具的错误提示反过来教模型做破坏性操作**。

---

## 5. Bug 与稳定性

| 严重程度 | 条目 | 问题描述 | 是否有修复 PR |
|---|---|---|---|
| **高** | **Issue #3150** | Agent 覆盖自身记忆文件，导致“失忆”/上下文丢失，属于工具误用（misuse）导致的自我破坏性输出 | 是：PR #3226（待合并） |
| 高（安全） | Issue #3088 | `libolm` 已无人维护且不安全，需替换为 `vodozemac` | 无 |
| 低 | PR #3189（已关） | LINE 通道中忽略 `resp.Body.Close()` 错误，降低日志噪音 | 自身即为修复 |

---

## 6. 功能请求与路线图信号

- 今日没有与视觉语言、推理机制或训练/后训练方法论直接相关的功能请求。
- 从 PR #3226 可推断一个**路线图信号**：PicoClaw 可能需要在工具层引入更严格的“写入保护”语义，例如：
  - 为 `memory/MEMORY.md` 等自引用文件提供专用写入工具；
  - 在工具 schema 中明确区分 `create` 与 `overwrite`，并禁止提示词暗示模型绕过保护。
- **Issue #3088** 是功能请求，但属于加密依赖替换，对模型能力无直接影响。

---

## 7. 用户反馈摘要

- **核心痛点**：Agent 通过通用文件工具修改 `memory/MEMORY.md` 时，没有专用保护机制，容易发生自我覆盖。
- **失望点**：`write_file` 的覆盖提示不仅没有阻止破坏，反而像“教学”一样引导模型设置 `overwrite=true`，造成“它给自己整失忆了”的现象。
- **期望**：用户希望文件写入工具的提示词是**防御性**的（如明确警告“覆盖将导致数据丢失”），而不是诱导性的；同时希望为记忆文件提供更安全、独立的更新接口。

---

## 8. 待处理积压

- **Issue #3088** —— 创建已约 27 天，高优先级、`help wanted`，目前仍 open。需要维护者评估替换 `libolm` 为 `vodozemac` 的兼容性与迁移路径。  
  链接：https://github.com/sipeed/picoclaw/issues/3088

- **PR #3226** —— 针对高影响 AI 可靠性问题（Issue #3150）的修复已提交，但尚未合并，建议优先 review。  
  链接：https://github.com/sipeed/picoclaw/pull/3226

- **其他待合并的工程项**：PR #3191、#3192、#3222 均为构建/配置/DeltaChat 重构，非研究重点。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目日报（2026-07-06）

## 1. 今日速览
- 过去 24 小时活跃度偏低：0 条 Issue 更新、6 条 PR 更新（3 条已合并/关闭，3 条仍待合并），无新版本发布。
- 研究相关信号有限：仅 **#2726**（per-agent-group 输入/输出 guardrails）和 **#2956**（输出重复投递抑制）与 AI 可靠性、对齐安全直接相关。
- 其余 PR 集中在模板设置向导、Lint 通道、容器环境变量等产品与基础设施层面，已按“跳过一般性产品/商业更新”的要求做低优先级处理。
- 今日未出现视觉语言能力、推理机制、训练方法论或模型幻觉相关的专门 Issue/PR。

---

## 2. 版本发布
无新版本发布。

---

## 3. 项目进展（研究相关项）

### #2726 [CLOSED] feat: add /add-guardrails skill — per-agent-group input/output guardrails
- **链接：** [nanocoai/nanoclaw PR #2726](https://github.com/nanocoai/nanoclaw/pull/2726)
- **说明：** 为每个 agent group 引入可选的输入/输出 guardrails，基于确定性正则与关键词规则实现 prompt-injection 短语拦截、凭证泄露模式检测，并支持 `block`/`flag` 动作、聊天告警及主机端隔离审计。
- **研究意义：** 属于 **post-training 对齐 / AI 可靠性** 范畴，是在应用层对模型输入输出进行安全约束的工程实践，可降低有害指令注入与敏感信息泄露风险。
- **整体进展评估：** 项目在安全层面向前迈出一小步，但今日合并内容未涉及模型能力、视觉语言或推理机制的改进。

### 其他已关闭/合并 PR（非研究核心，仅作背景）
- **#2766** [CLOSED]：新增 `.format-lint-off` 通道格式开关 — 代码规范基础设施。
- **#2908** [CLOSED]：Codex provider 下模板 agent 的 persona prepend 与 git-independent skill 发现 — 模板生态基础设施。

---

## 4. 社区热点
- 今日无高互动条目：所有 PR 的 👍 均为 0，Issues 无评论，无活跃讨论。
- 无法从当前数据中识别出用户集中诉求或研究社区关注焦点。

---

## 5. Bug 与稳定性

### #2956 [OPEN] fix(agent-runner): suppress duplicate delivery when the final output repeats tool-sent content
- **链接：** [nanocoai/nanoclaw PR #2956](https://github.com/nanocoai/nanoclaw/pull/2956)
- **问题描述：** 当 agent 通过 `send_message` MCP 工具发送回复后，又在最终输出中重复同一段文本，会导致消息被重复投递。
- **严重程度：** 中（影响输出可靠性与用户体验，可能引发用户侧困惑或消息冗余）
- **状态：** 已有修复 PR，待合并
- **研究相关：** 属于 **AI 系统输出行为一致性** 问题，与模型生成结果如何被正确路由、去重、展示有关，是 AI 可靠性研究的下游工程问题。

---

## 6. 功能请求与路线图信号
- 今日无直接研究相关功能请求。
- 当前待合并 PR 中可见的基础设施/产品方向：
  - **#2909** [OPEN]：模板设置向导与 first-agent stamping（产品配置流程）
  - **#2036** [OPEN]：通过 DB 管理 per-group 容器环境变量（部署/配置基础设施）
- 上述 PR 未涉及视觉语言、推理机制、训练方法或幻觉缓解方向。

---

## 7. 用户反馈摘要
- 今日无 Issues 评论数据，无法提炼真实用户痛点、使用场景或满意度信息。

---

## 8. 待处理积压
- 研究相关长期未响应 Issue/PR：无数据。
- 一般性待合并 PR 提醒：
  - **#2036** [OPEN]：per-group 容器环境变量（创建于 2026-04-26，已数月未合入）
  - **#2909** [OPEN]：模板设置向导（创建于 2026-07-02）
  - **#2956** [OPEN]：输出重复投递修复（创建于 2026-07-05，建议优先合并以提升稳定性）

---

**总体健康度：** 项目维护节奏平稳，但今日缺乏核心研究突破。AI 可靠性方面通过 guardrails 的合入有积极信号，输出重复投递 bug 已有修复待合并；建议持续关注与模型推理、视觉语言、幻觉缓解相关的 Issue/PR 是否会在后续出现。

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw 项目日报（2026-07-06）

> **研究视角**：本摘要仅聚焦多模态推理、长上下文理解、post-training 对齐、AI 可靠性与幻觉相关议题，已过滤 Slack 配置、OAuth 流程、Postgres 优化、依赖升级等一般性工程/产品更新。

---

## 1. 今日速览

过去 24 小时 IronClaw 活跃度较高（28 个 PR、4 个 Issue），但**与研究直接相关**的进展集中在三条主线：代理推理环路控制（重复工具调用循环的修正机制）、长上下文提示组装（压缩截断与可观测性）、以及工具调用可靠性（LLM/Provider 层 JSON 损坏与 bridge meta-tool 的 allowlist 过滤）。多模态方面出现 PDF 附件提取的测试增强。整体上，项目在安全边界、推理稳健性和长上下文管理上有实质推进，但 E2E 持续失败与大量依赖更新提示工程系统仍处在高变动期。

---

## 2. 版本发布

无今日发布。

---

## 3. 项目进展

### 已合并/关闭的研究相关 PR

- **#5659 — [PRODUCTION CHANGE] 修复 bridge meta-tools 在窄化 allowlist 下被剥离的问题**
  - 作者：henrypark133
  - 链接：https://github.com/nearai/ironclaw/pull/5659
  - 进展：修复了 `CapabilitySurfaceProfileFilter` 安全过滤器在跨越 32-tool 桥接阈值时，错误地移除合成桥接工具 `tool_search`/`tool_describe`/`tool_call` 的问题。附带回归测试与 trust-boundary 测试。
  - 研究意义：直接关系到**工具使用能力边界**与**安全/能力对齐**，避免因权限过滤导致代理在工具桥接场景下丧失元工具推理能力。

- **#5637 — test(reborn): wiring-parity tripwire**
  - 链接：https://github.com/nearai/ironclaw/pull/5637
  - 进展：已关闭，确保集成测试 harness 的运行时形态与生产 local-dev 组合一致。
  - 研究意义：测试-生产同构性是评估 post-training 对齐与行为一致性的基础保障。

---

## 4. 社区热点

研究相关讨论热度最高的议题是代理循环与工具调用可靠性：

- **#5666 — 在 v1 agentic loop 中打破重复相同工具调用循环**
  - 链接：https://github.com/nearai/ironclaw/pull/5666
  - 诉求：为 v1 代理循环增加“重复断路器”（repetition breaker），当模型连续发出相同工具调用时，通过纠正性提示（corrective nudge）引导其脱离循环，而非直接终止。这与 Reborn 中基于失败终止的机制（#5287）形成对照。
  - 研究意义：涉及**推理错误恢复**、**自我修正（self-correction）**与**循环检测**，是减少代理“卡死”与提升可靠性的关键路径。

- **#5665 — 修复 provider 损坏的 tool-call 参数 JSON**
  - 链接：https://github.com/nearai/ironclaw/pull/5665
  - 诉求：OpenAI-compatible provider（OpenRouter、NEAR AI Cloud）在翻译模型原生 XML tool-call 格式时，会在 `arguments` 字符串中泄漏或截断尾部标签（如 `</parameter>`、DeepSeek 的 `</tool▁call>`），导致 JSON 解析失败。
  - 研究意义：属于**结构化输出幻觉/格式错误**的边界问题，对工具调用可靠性有直接影响。

---

## 5. Bug 与稳定性

| 严重程度 | 议题/PR | 问题 | 状态 |
|---|---|---|---|
| 高 | #5647 | 桥接工具披露 + 窄化能力 allowlist 导致 latent 的 bridge meta-tools 被剥离 | 已有修复 PR #5659 |
| 高 | #4108 | Nightly E2E 持续失败 | 仍在开放，无近期评论 |
| 中 | #5665 | Provider 层 tool-call JSON 损坏/截断 | 修复 PR 已提交 |
| 中 | #5666 | v1 代理循环中重复相同工具调用导致行为退化 | 修复 PR 草案已提交 |
| 低 | #5661 | InMemory store 在 CAS 竞争下的 parity 问题 | 修复 PR 已提交 |

---

## 6. 功能请求与路线图信号

- **长上下文管理优化**：PR #5663 提出 prompt-context assembly 的三项加固——压缩截断、drop 可观测性、可选指令预算。这暗示项目正在系统性地处理**上下文窗口预算与长文档/长历史推理**的权衡，可能进入下一版本的 core loop。
- **多模态文档理解**：PR #5660 开始覆盖 PDF 附件提取的真实存储路径，表明 PDF/附件解析正从 mock 测试走向生产级集成测试，是视觉-语言能力落地的信号。
- **推理可靠性**：#5666 的重复断路器与 #5659 的 bridge meta-tool 修复共同指向“代理在工具密集场景下的稳健推理”是近期重点。
- **沉默失败治理**：PR #5662 将 90 处 `let _ = <fallible>` 改为显式错误处理，反映项目对齐/可靠性工程从“功能正确”向“可观测失败模式”演进。

---

## 7. 用户反馈摘要

从 Issues 与 PR 描述中提炼的真实痛点：

- **工具调用不可靠**：Provider 对模型原生 tool-call 格式的翻译会引入 XML 标签泄漏，导致下游 JSON 解析失败。这是跨 provider 部署时影响最大的可靠性痛点。
- **代理循环“卡死”**：模型在重复相同工具调用时缺乏纠正性干预，用户/开发者需要循环检测与自我修正机制。
- **上下文静默丢失**：prompt-context assembly 存在无界 token 成本与静默截断风险，开发者需要可观测的压缩/截断行为与预算控制。
- **测试-生产形态不一致**：集成测试 harness 与生产组合不一致，会掩盖真实部署中的行为偏差。
- **安全过滤误伤能力**：Capability allowlist 的窄化过滤会错误地移除桥接元工具，导致模型在需要工具桥接时丧失必要能力。

---

## 8. 待处理积压

- **#4108 — Nightly E2E failed**
  - 链接：https://github.com/nearai/ironclaw/issues/4108
  - 创建于 2026-05-27，最新更新于 2026-07-05。长期未关闭的 E2E 失败是项目健康度的警示信号，可能影响对推理/对齐效果的端到端评估。建议维护者优先排查并补充失败分类。

- **#5657 — Coverage scope: v1-only crates exempted from Reborn coverage denominator**
  - 链接：https://github.com/nearai/ironclaw/issues/5657
  - 属于测试覆盖率度量 redesign 的跟踪议题，虽不直接影响模型能力，但关系到 Reborn 新一代架构的验证完整性，进而影响对齐评估的可信度。

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目日报（2026-07-06）

## 1. 今日速览

今日 LobsterAI 仓库活跃度极低，研究相关信号几乎沉寂。过去 24 小时内无新增或活跃的 Issue，仅 2 条 Pull Request 发生状态变更，且无新版本发布。已审查的 PR 均属于前端 UI 改造或企业 IM 集成验证，与多模态视觉语言、推理机制、训练后对齐或幻觉治理等核心研究方向无直接关联。整体来看，项目在当前统计周期内未产生可纳入研究动态摘要的技术进展。

## 2. 版本发布

无新版本发布。

## 3. 项目进展

今日无与多模态研究相关的 PR 合并或关闭。已发生状态变更的两条 PR 均偏向工程/产品层面：

- **#2273 [CLOSED]** — `renderer` 任务列表卡片重设计，新增状态 chip、开关、搜索与乐观式 UI 反馈。  
  链接：[netease-youdao/LobsterAI/pull/2273](https://github.com/netease-youdao/LobsterAI/pull/2273)  
  该 PR 属于前端交互优化，与模型能力或训练方法无关。

- **#1349 [OPEN / stale]** — 为 POPO 连通性测试添加真实 API 验证。  
  链接：[netease-youdao/LobsterAI/pull/1349](https://github.com/netease-youdao/LobsterAI/pull/1349)  
  该 PR 针对企业 IM 连接器凭据校验，属于集成稳定性修复，不涉及多模态推理研究。

**研究进展评估**：0。

## 4. 社区热点

今日无讨论、评论或反应活跃的 Issue/PR。所有 Issue 数量为 0，PR 数量仅 2 条且无评论或点赞。社区在视觉语言能力、推理机制、训练方法论或幻觉问题上的讨论完全缺失。

## 5. Bug 与稳定性

根据今日数据，无新报告的 Bug、崩溃或回归问题。仅有一条潜在修复性 PR：

- **#1349** — POPO 连接测试虚假“验证通过”问题：原代码仅检查字段非空，未真正调用 API。  
  链接：[netease-youdao/LobsterAI/pull/1349](https://github.com/netease-youdao/LobsterAI/pull/1349)  
  严重程度：中（企业集成场景下的配置误导）。  
  状态：已提交 fix PR，但长期处于 open/stale，尚未合并。

该问题属于外部服务集成，不属于模型幻觉或推理错误。

## 6. 功能请求与路线图信号

今日无新增功能请求或研究路线信号。现有 PR 中未出现视觉语言增强、推理时扩展、对齐训练（RLHF/DPO/KTO）或幻觉缓解相关提案。

## 7. 用户反馈摘要

今日无 Issue 评论可提炼。根据当前数据，无法识别用户在多模态理解、长上下文或可靠性方面的真实痛点。

## 8. 待处理积压

需提醒维护者关注以下长期未决项：

- **#1349 [stale]** — POPO 真实 API 验证 PR，创建于 2026-04-02，已逾三个月未合并。  
  链接：[netease-youdao/LobsterAI/pull/1349](https://github.com/netease-youdao/LobsterAI/pull/1349)

**研究相关积压**：当前无。

---

**健康度提示**：当前周期内项目研究活跃度极低，建议后续关注是否有视觉语言、推理与对齐训练相关 Issue/PR 出现。

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

# CoPaw 项目日报（2026-07-06）—— 研究动态摘要

> **研究相关性筛选说明**：过去 24 小时仓库活跃度较高（12 Issues / 5 PRs），但绝大多数内容集中在前端 UI、IM 通道、账号权限等工程/产品层面。直接涉及**多模态视觉语言、模型训练方法论、幻觉治理**的内容较少。以下摘要已剔除明显商业/产品类更新，重点保留与**工具推理、长上下文管理、结构化输出可靠性、Agent 消息协议**相关的信号。

---

## 1. 今日速览

- 过去 24 小时无新版本发布，5 个 PR 均处于 Open 状态，0 个已合并/关闭。
- 研究相关的技术动向主要围绕 **Agent 推理链路可靠性**：工具消息自配对修复、会话级记忆状态管理、上下文压缩的结构化输出约束。
- 未出现视觉语言能力（VLM）、多模态数据集、post-training 训练或对齐方法论的直接更新。
- 社区情绪偏期待：对 V2.0 的呼声较多，但实际技术披露有限。

---

## 2. 版本发布

**无新版本发布。**

---

## 3. 项目进展（研究相关）

今日无已合并/关闭的 PR。以下 Open PR 代表当前正在进行的技术推进：

- **[PR #5792](https://github.com/agentscope-ai/QwenPaw/pull/5792)** `fix(agents): stop dropping self-paired tool messages during sanitation`
  - 修复 `_sanitize_tool_messages` 在清理未配对 tool 消息时，误删 AgentScope 2.0 中合法的“自配对” assistant 消息（同一消息同时包含 `tool_call` 与 `tool_result`）的问题。
  - **研究意义**：直接关系多轮工具调用推理链的完整性，避免 agent 在 tool-use 循环中静默丢失关键推理步骤。

- **[PR #5777](https://github.com/agentscope-ai/QwenPaw/pull/5777)** `feat(memory): add auto-memory turn state management`
  - 在 `BaseMemoryManager` 引入 `_auto_memory_turn_states`，将会话级自动记忆状态从全局标记迁移为按 session 管理。
  - **研究意义**：长上下文与记忆模块的工程基础改进，有助于更精细地追踪多轮对话状态，减少跨会话状态污染。

- **[PR #5786](https://github.com/agentscope-ai/QwenPaw/pull/5786)** `fix: three bug fixes (#5709, #5773, #5784)`
  - 包含同名模型跨 provider 时的压缩阈值匹配修复（`model.id` + `provider_id` 双重校验）。
  - **研究意义**：属于长上下文压缩的边界正确性修复，确保前端展示的 `max_input_length` 与实际后端行为一致。

- **[PR #5783](https://github.com/agentscope-ai/QwenPaw/pull/5783)** `fix(crons): record run timestamps in job timezone`
  - 将 cron 执行时间戳从硬编码 UTC 改为使用任务配置的 `schedule.timezone`。

---

## 4. 社区热点

按评论数与活跃度，今日讨论最多的条目如下：

| 条目 | 评论数 | 研究相关度 | 诉求分析 |
|------|--------|------------|----------|
| **[Issue #5770](https://github.com/agentscope-ai/QwenPaw/issues/5770)** V2.0 正式版期待 | 3 | 低 | 用户对下一代版本抱有高期望，但缺乏技术细节披露 |
| **[Issue #5785](https://github.com/agentscope-ai/QwenPaw/issues/5785)** coding 模式无法选择隐藏文件夹 | 3 | 低 | 开发者工具链体验诉求 |
| **[Issue #5784](https://github.com/agentscope-ai/QwenPaw/issues/5784)** 同名模型跨 provider 压缩阈值显示错误 | 3 | 中 | 模型/provider 标识歧义导致长上下文配置不可信 |
| **[Issue #5779](https://github.com/agentscope-ai/QwenPaw/issues/5779)** cron API 返回 UTC 而非任务时区 | 3 | 低 | 调度系统时区一致性 |

从研究视角看，更值得关注的信号是：

- **[Issue #5789](https://github.com/agentscope-ai/QwenPaw/issues/5789)**：上下文压缩时模型输出超过 JSON Schema `maxLength`，导致 `jsonschema.validate()` 崩溃。
- **[PR #5792](https://github.com/agentscope-ai/QwenPaw/pull/5792)**：工具消息自配对被误清理，影响 Agent 推理链可靠性。

---

## 5. Bug 与稳定性

按对研究/系统可靠性的影响程度排列：

### 高严重性

- **[Issue #5789](https://github.com/agentscope-ai/QwenPaw/issues/5789)** — 上下文压缩时模型结构化输出超出 `next_steps maxLength: 200`，触发 `jsonschema.validate()` 异常崩溃。
  - **影响**：长上下文场景下 Agent 上下文压缩直接失败，可能导致会话中断。
  - **状态**：Open，**暂无 fix PR**。
  - **研究关联**：结构化输出约束与模型指令遵循能力之间的张力。

### 中等严重性

- **[Issue #5784](https://github.com/agentscope-ai/QwenPaw/issues/5784)** — 同名模型跨 provider 时前端压缩阈值显示错误。
  - **状态**：Open，已有修复 **[PR #5786](https://github.com/agentscope-ai/QwenPaw/pull/5786)**。

- **[Issue #5782](https://github.com/agentscope-ai/QwenPaw/issues/5782)** — Google Gemini 通过 OpenAI 兼容端点返回 `Embedding.index = None`，导致向量搜索静默回退为关键词搜索。
  - **状态**：Open，**暂无 fix PR**。
  - **研究关联**：嵌入/检索可靠性，影响 RAG 类 Agent 的事实性与幻觉风险。

- **[Issue #5779](https://github.com/agentscope-ai/QwenPaw/issues/5779)** — cron API 时间戳硬编码 UTC。
  - **状态**：Open，已有修复 **[PR #5783](https://github.com/agentscope-ai/QwenPaw/pull/5783)**。

### 低严重性（前端/交互）

- **[Issue #5790](https://github.com/agentscope-ai/QwenPaw/issues/5790)** — Agent 回复完成后加载动画未消失。
- **[

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

⚠️ 摘要生成失败。

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*