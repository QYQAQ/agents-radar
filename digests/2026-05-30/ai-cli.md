# AI CLI 工具社区动态日报 2026-05-30

> 生成时间: 2026-05-30 00:32 UTC | 覆盖工具: 9 个

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

## 横向对比

# AI CLI 工具生态横向对比分析报告 | 2026-05-30

---

## 1. 生态全景

当前 AI CLI 工具生态呈现**"长上下文军备竞赛进入深水区"**态势：各家已从单纯扩展窗口上限转向**压缩效率、状态持久化、推理可视化**的精细化工程。同时，**MCP 生态的工具膨胀**（Copilot CLI 73% 窗口被系统/工具消耗）正成为新的瓶颈，倒逼动态工具选择、描述压缩等研究。多模态交互（图像内联、IME 支持）从"炫技"变为"刚需"，但终端基础设施的兼容性债务集中暴露。最显著的信号是**"推理可控性"成为对齐新战场**——thinking 模式参数、宪法提示可覆盖性、失败停止机制等从研究概念加速产品化。

---

## 2. 各工具活跃度对比

| 工具 | 今日 Issues | 今日 PRs | 版本发布 | 研究相关信号强度 |
|:---|:---|:---|:---|:---|
| **Claude Code** | 6 条（含 2 条🔴核心） | 1 条 | v2.1.157/156 | ⭐⭐⭐⭐⭐ Thinking block 完整性危机、韩语分布偏移 |
| **OpenAI Codex** | 10 条 | 10 条 | rust-v0.136.0-alpha.1 | ⭐⭐⭐⭐☆ 动态压缩协议、多模态数据污染、云配置对齐 |
| **Gemini CLI** | 10 条 | 9 条 | v0.45.0-nightly | ⭐⭐⭐⭐☆ AST 感知推理、Auto Memory 质量工程、CJK 清洗 |
| **GitHub Copilot CLI** | 8 条 | 0 条 | v1.0.57-0 等 4 个 | ⭐⭐⭐⭐☆ 上下文窗口危机、子代理静默挂起、MCP 去重 |
| **Kimi CLI** | 5 条 | 3 条 | v1.46.0 | ⭐⭐⭐☆☆ 压缩空内容过滤、skill 触发决策、CoT 成本 |
| **OpenCode** | 10 条 | 10 条 | 无 | ⭐⭐⭐⭐☆ Prefix cache 稳定性、多模态闭环、模型路由 |
| **Pi** | 10 条 | 10 条 | v0.78.0 | ⭐⭐⭐⭐☆ 本地模型 token 计数、reasoning 参数生态碎片化 |
| **Qwen Code** | 9 条 | 10 条 | v0.17.0/v0.16.1-nightly | ⭐⭐⭐⭐⭐ 压缩范式重构、工具调用形式化、推理可控性 |
| **DeepSeek TUI** | 10 条 | 10 条 | 无 | ⭐⭐⭐⭐☆ 本地模型 tool-use、宪法提示可配置、缓存可观测性 |

> **活跃度分层**：第一梯队（OpenAI Codex / Gemini CLI / OpenCode / Pi / Qwen Code / DeepSeek TUI，10 PR/日级）；第二梯队（Claude Code / Copilot CLI / Kimi CLI，<5 PR/日但 issue 质量高）

---

## 3. 共同关注的功能方向

| 功能方向 | 涉及工具 | 具体诉求 |
|:---|:---|:---|
| **长上下文压缩与状态持久化** | Claude Code (#63147)、OpenAI Codex (#24797)、Kimi CLI (#2396/#2395)、Qwen Code (#4592/#4624)、Pi (#5197/#5182) | 从"能压缩"到"压缩后可恢复、可续接、不泄漏内存"；Claude Code 的 thinking block 签名-语义一致性、Qwen Code 的 tail-preservation→summary+attachments 范式迁移最具代表性 |
| **Thinking/Reasoning 过程可控** | Claude Code (v2.1.156 补丁)、OpenAI Codex (#24572)、Qwen Code (#4505/#4598)、DeepSeek TUI (#2348/#2338)、Pi (#5169/#5196) | 可视化折叠、时长追踪、模式选择（speed/quality 权衡）、跨平台参数适配 |
| **MCP/工具生态治理** | Copilot CLI (#3539/v1.0.56-1)、Gemini CLI (#24246/#27383)、DeepSeek TUI (#2339/#2344/#2362)、Kimi CLI (#2399) | 工具数量硬边界（~128）、动态选择、描述压缩、子代理工具继承、进程生命周期管理 |
| **多模态输入完整性** | OpenAI Codex (#24582)、OpenCode (#21227/#21352)、Pi (#5098)、Gemini CLI (#27349) | 跨模态数据管道隔离（stdout 污染 image base64）、终端图像协议兼容性、CJK 字符清洗 |
| **子代理/多 Agent 可靠性** | Copilot CLI (#3547/#3574)、Gemini CLI (#21409/#22323)、DeepSeek TUI (#2362/#2354)、OpenCode (#29786) | 故障静默检测、失败停止机制、工具权限继承、状态报告真实性（MAX_TURNS 截断误报成功） |

---

## 4. 差异化定位分析

| 维度 | Claude Code | OpenAI Codex | Gemini CLI | Copilot CLI | Kimi CLI | OpenCode | Pi | Qwen Code | DeepSeek TUI |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **核心锚点** | 扩展思维可靠性 | 企业云配置对齐 | AST 结构化推理 | GitHub 生态深度集成 | 长上下文成本效率 | 多模型统一网关 | 终端原生体验 | 工具调用形式化 | 本地模型/宪法 AI 可配置 |
| **目标用户** | 高复杂度推理任务开发者 | 企业级安全合规团队 | 代码库大规模重构工程师 | GitHub 重度用户/企业 | 长文档处理用户 | 多模型对比研究者 | 终端极客/TUI 爱好者 | 工具链可靠性工程师 | 本地部署/价值观定制用户 |
| **技术路线** | Thinking block 密码学完整性 | 分层配置引擎 + 请求归因 | 语法感知工具链（tilth/glyph） | MCP 工具去重 + 上下文透明 | 压缩路径全覆盖过滤 | Prefix cache 工程化 + LiteLLM | 跨平台 reasoning 参数路由 | 压缩范式重构 + 相邻性约束 | 宪法提示 hooks + 缓存诊断 |
| **独特资产** | Opus 4.8 长推理链 | OpenRouter 级企业部署 | Google 内部 AST 工具链 | GitHub MCP server 原生优化 | K2.6 思维链成本透明 | 开源多模型生态最完整 | 终端图像/IME 协议支持最广 | 摘要+attachments 压缩新范式 | BASE_PROMPT 可覆盖的 Constitutional AI |
| **当前短板** | Thinking block 状态机脆弱 | 多模态数据管道隔离缺失 | 纯视觉/OCR 动态空白 | 子代理模型特定挂起无解 | 品牌迁移期工程停滞 | 内存墙 + 可靠性债务 | 本地模型 token 计数不可靠 | 类型系统被 Google 锁定 | 本地模型 tool-use 格式偏移 |

---

## 5. 社区热度与成熟度

| 象限 | 工具 | 特征 |
|:---|:---|:---|
| **高活跃·高成熟** | Claude Code、OpenAI Codex、Copilot CLI | 日活 issue 质量高，有专职团队响应，但核心架构债务开始显现（thinking block、context 膨胀） |
| **高活跃·快速迭代** | Qwen Code、DeepSeek TUI、Pi、OpenCode | PR/Issue 密度接近第一梯队，但功能边界更激进（宪法可配置、鲸类路由、跨平台适配），技术债务累积快 |
| **中等活跃·架构调整期** | Gemini CLI、Kimi CLI | Gemini 依赖 Google 内部 AST 工具链差异化，Kimi 处于向 Kimi Code 迁移的过渡期，研究信号偏工程修复 |

> **成熟度警示**：OpenCode 的 #29915（12 个空 catch 块）和 #29921（ReDoS）显示快速迭代中的可靠性债务；Qwen Code 的 #4063（136 文件硬编码 Google 类型）暴露架构锁定风险。

---

## 6. 值得关注的趋势信号

| 趋势 | 证据强度 | 对开发者的参考价值 |
|:---|:---|:---|
| **"上下文窗口危机"从模型层转移到系统层** | 🔥🔥🔥🔥🔥 | MCP 工具描述、系统提示、示例的组合消耗已占 70%+ 窗口（Copilot #3539）。开发者需评估：你的"200K 上下文"实际可用推理预算可能 <50K。研究动态工具加载、分层 RAG、工具描述压缩将成为刚需。 |
| **Reasoning 参数生态碎片化倒逼适配层** | 🔥🔥🔥🔥🔥 | `thinking_budget`/`reasoning_effort`/`developer`/`enable_thinking` 语义不一（Pi #5159/#5117/#5169）。构建多模型应用时，需抽象统一的 reasoning 控制接口，而非硬编码各平台参数。 |
| **"压缩-续接"成为长上下文新范式** | 🔥🔥🔥🔥☆ | Qwen Code #4592 的 summary+attachments 替代 tail-preservation，Claude Code #63147 的 thinking block 签名一致性。长会话应用需设计**可验证的压缩快照机制**，而非依赖简单的截断策略。 |
| **宪法 AI 从研究走向可配置产品层** | 🔥🔥🔥🔥☆ | DeepSeek TUI #2356 的 `OnceLock` hooks 覆盖宪法文本，使价值观层可插拔。企业级应用需关注：你的 AI 工具是否允许**不 fork 代码即注入组织合规约束**？ |
| **终端作为多模态载体的兼容性债务爆发** | 🔥🔥🔥☆☆ | 图像协议（Pi #5098）、IME（Pi #5198/#2330）、ANSI 序列（Pi #5185）、RTL 语言（OpenCode #25010）密集修复。TUI 工具的多模态能力受限于终端基础设施，而非模型能力。 |
| **"静默失败"类幻觉的检测困境** | 🔥🔥🔥🔥☆ | Claude Code thinking block 损坏、Copilot 子代理挂起（#3547）、DeepSeek "Working..." 死锁（#4945）、Gemini MAX_TURNS 误报成功（#22323）。需建立**推理状态的外部可观测性**（心跳、进度 token、确定性超时），而非依赖模型自报告。 |

---

*报告基于 2026-05-30 各项目 GitHub 公开数据生成。建议技术决策者重点关注：上下文预算的实际利用率、reasoning 参数的跨平台抽象、以及压缩-续接机制的形式化验证。*

---

## 各工具详细报告

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills 社区热点

> 数据来源: [anthropics/skills](https://github.com/anthropics/skills)

# Claude Code Skills 社区热点报告（截至 2026-05-30）

---

## 1. 热门 Skills 排行（按社区关注度）

| 排名 | Skill | 功能概述 | 社区热点 | 状态 |
|:---|:---|:---|:---|:---|
| 1 | **[document-typography](https://github.com/anthropics/skills/pull/514)** | AI 生成文档的排版质量控制：防止孤行、寡行、编号错位等排版问题 | 直击 Claude 生成文档的普遍痛点；作者指出"用户很少主动要求好的排版，但问题无处不在"；讨论聚焦是否应作为默认能力而非独立 Skill | 🟡 Open |
| 2 | **[ODT skill](https://github.com/anthropics/skills/pull/486)** | OpenDocument 格式（.odt/.ods）的创建、模板填充与 ODT→HTML 转换 | 开源/ISO 标准文档格式的企业需求；与现有 docx/pdf skill 形成互补；长期未合并引发社区询问 | 🟡 Open |
| 3 | **[frontend-design](https://github.com/anthropics/skills/pull/210)** | 前端设计 Skill 的清晰度与可执行性改进 | 元层面讨论：如何让 Skill 指令在单轮对话中真正可执行；避免"说教式"文档 | 🟡 Open |
| 4 | **[skill-quality-analyzer / skill-security-analyzer](https://github.com/anthropics/skills/pull/83)** | 元 Skill：自动评估 Skill 质量（结构、文档、示例、资源、安全性五维度） | 生态自举工具：社区意识到 Skill 质量参差不齐，需要标准化评估框架 | 🟡 Open |
| 5 | **[AURELION skill suite](https://github.com/anthropics/skills/pull/444)** | 四层认知+记忆框架：结构化思维模板、顾问模式、智能体执行、持久记忆 | 认知架构层面的创新；讨论焦点在于与 Claude 原生记忆能力的边界划分 | 🟡 Open |
| 6 | **[testing-patterns](https://github.com/anthropics/skills/pull/723)** | 全栈测试方法论：测试哲学、单元测试、React 组件测试、E2E、性能、安全测试 | 开发工作流刚需；Testing Trophy 模型与 AI 辅助测试的落地结合 | 🟡 Open |
| 7 | **[ServiceNow platform](https://github.com/anthropics/skills/pull/568)** | 企业级 ServiceNow 全平台覆盖：ITSM/ITOM/SecOps/ITAM/FSM/SPM/CSDM/IntegrationHub | 企业 ERP/ITSM 领域最深度的 Skill；广度 vs 维护成本的权衡讨论 | 🟡 Open |
| 8 | **[codebase-inventory-audit](https://github.com/anthropics/skills/pull/147)** | 代码库治理：识别孤儿代码、未使用文件、文档缺口、基础设施膨胀 | 技术债务量化；10 步工作流生成 CODEBASE-STATUS.md 作为单一事实来源 | 🟡 Open |

---

## 2. 社区需求趋势（Issues 提炼）

| 趋势方向 | 代表 Issue | 核心诉求 |
|:---|:---|:---|
| **组织级 Skill 共享** | [#228](https://github.com/anthropics/skills/issues/228) | 企业内 Skill 库共享，替代 Slack/Teams 手动传文件的低效模式 |
| **安全与信任边界** | [#492](https://github.com/anthropics/skills/issues/492) | 社区 Skill 冒用 `anthropic/` 命名空间的风险；需要官方签名或验证机制 |
| **MCP 协议互通** | [#16](https://github.com/anthropics/skills/issues/16) | Skill 与 MCP 的双向暴露：Skill → MCP 工具化，降低 API 认知成本 |
| **Bedrock 等第三方部署** | [#29](https://github.com/anthropics/skills/issues/29) | 非 Claude.ai 官方渠道的 Skill 加载能力 |
| **上下文窗口优化** | [#1102](https://github.com/anthropics/skills/issues/1102), [#1175](https://github.com/anthropics/skills/issues/1175) | MCP/Skill 返回大数据时的压缩与权限控制；SharePoint 文档场景的安全顾虑 |
| **Skill 质量标准化** | [#202](https://github.com/anthropics/skills/issues/202) | skill-creator 自身需符合最佳实践：指令式而非说教式，token 效率优先 |

---

## 3. 高潜力待合并 Skills（评论活跃 + 解决明确痛点）

| Skill | PR | 合并潜力分析 |
|:---|:---|:---|
| **document-typography** | [#514](https://github.com/anthropics/skills/pull/514) | ⭐⭐⭐⭐⭐ 问题普遍、方案具体、无外部依赖；可能最快合并 |
| **ODT skill** | [#486](https://github.com/anthropics/skills/pull/486) | ⭐⭐⭐⭐☆ 企业合规刚需（开源格式），但需与现有 docx skill 协调维护 |
| **testing-patterns** | [#723](https://github.com/anthropics/skills/pull/723) | ⭐⭐⭐⭐☆ 开发者工具链关键缺口，社区呼声高 |
| **skill-quality-analyzer** | [#83](https://github.com/anthropics/skills/pull/83) | ⭐⭐⭐⭐☆ 生态基础设施，但可能需官方主导标准化 |
| **ServiceNow** | [#568](https://github.com/anthropics/skills/pull/568) | ⭐⭐⭐☆☆ 企业价值高，但覆盖过广，维护负担重 |
| **AURELION** | [#444](https://github.com/anthropics/skills/pull/444) | ⭐⭐⭐☆☆ 架构创新，但与原生记忆功能存在功能重叠争议 |

**近期最可能落地**：`document-typography`、`testing-patterns`（问题边界清晰，评审成本低）

---

## 4. Skills 生态洞察

> **核心诉求一句话**：社区正从"Skill 数量扩张"转向"质量治理与组织就绪"——企业需要可安全共享、标准化评估、与现有工具链（MCP/Bedrock/ServiceNow）深度集成的生产级 Skill，而非更多孤立的功能示例。

**关键张力**：
- **开放 vs 安全**：社区贡献活跃（#492 信任边界问题）
- **广度 vs 深度**：单 Skill 覆盖全平台（ServiceNow）还是聚焦可维护的垂直场景
- **教学 vs 执行**：Skill 是指令引擎（机器可读）还是文档（人类可读）——[#202](https://github.com/anthropics/skills/issues/202) 的争论将持续塑造 Skill 编写规范

---

# Claude Code 研究动态摘要 | 2026-05-30

---

## 1. 今日速览

今日核心信号集中于**扩展思维（extended thinking）机制的可靠性危机**：多个高热度 Issue 暴露 Claude Code 在处理长上下文推理时的 thinking block 损坏问题，导致会话永久失效。同时，韩语输出中的异常词汇频率激增（"박다" 18× 基线）揭示了 post-training 对齐中的语言特定幻觉问题。插件系统的规则支持需求（#14200）则指向工具使用与系统指令对齐的研究空白。

---

## 2. 版本发布

**v2.1.157** / **v2.1.156**（2026-05-29/30）

| 版本 | 与研究相关的更新 |
|:---|:---|
| v2.1.157 | 插件系统扩展（`.claude/skills` 自动加载、`claude plugin init` 脚手架）— 与**工具学习/插件对齐**相关，但属工程基础设施 |
| v2.1.156 | **修复 Opus 4.8 的 thinking block 修改导致 API 400 错误** — 直接关联**长上下文推理可靠性** |

> ⚠️ 该修复为紧急补丁，但 #63147 显示问题未完全解决，resuming 场景仍存在永久性损坏。

---

## 3. 研究相关 Issues

### 🔴 长上下文推理与 Thinking Block 完整性

| # | 标题 | 评论 | 研究价值 |
|:---|:---|:---|:---|
| **#10199** | [BUG] API Error 400 - Thinking Block Modification Error | 94 | **核心案例**：Opus 4.8 的 thinking block 在工具调用后被修改，触发 API 400。暴露**推理链与工具执行的交错协议缺陷**，需研究 thinking block 的不变性保证机制。[链接](https://github.com/anthropics/claude-code/issues/10199) |
| **#63147** | Resuming extended-thinking session fails permanently with 400 "thinking blocks cannot be modified" | 38 | **关键发现**：transcript 存储 thinking text 为空但保留 signature，导致**状态恢复时的语义-签名不一致**。直接挑战长会话的**持久化推理状态一致性**研究。[链接](https://github.com/anthropics/claude-code/issues/63147) |

### 🔴 幻觉与输出分布异常（Post-training 信号）

| # | 标题 | 评论 | 研究价值 |
|:---|:---|:---|:---|
| **#62961** | Korean outputs use informal/slang verb "박다" (bakda) at 18× baseline frequency | 3 | **罕见语言特定幻觉量化案例**：特定动词频率异常激增，暗示**RLHF/DPO 后训练中的奖励劫持或数据污染**。需分析韩语 token 的 logit 分布偏移。研究价值：多语言对齐中的**模式崩溃（mode collapse）**检测。[链接](https://github.com/anthropics/claude-code/issues/62961) |
| **#60366** | Saying "hi" returns Usage Policy violation error | 61 | **过度拒绝（over-refusal）**的极端案例：无害输入触发安全过滤器。反映**对齐税（alignment tax）**与**分布外检测**的权衡失效。[链接](https://github.com/anthropics/claude-code/issues/60366) |
| **#63802** | Claude Code ignores claude.md instructions and prioritizes expedient solutions | 2 | **系统指令遵循失败**：claude.md 被忽略，模型优先选择"便捷"而非"正确"方案。涉及**指令层级（instruction hierarchy）**与**目标误泛化（goal misgeneralization）**。[链接](https://github.com/anthropics/claude-code/issues/63802) |

### 🟡 多模态与视觉处理

| # | 标题 | 评论 | 研究价值 |
|:---|:---|:---|:---|
| **#60334** | Image processing failures causing conversation token waste | 30 | **视觉输入处理故障**：无图像场景误报图像处理失败，导致 token 浪费。暴露**多模态输入验证**与**错误级联**问题。已关闭但未根因修复。[链接](https://github.com/anthropics/claude-code/issues/60334) |

### 🟡 工具使用与执行可靠性

| # | 标题 | 评论 | 研究价值 |
|:---|:---|:---|:---|
| **#63797** | Bash/Read tool results intermittently return empty then flush late | 3 | **工具输出流同步异常**：高并发长会话中，Bash/Read 返回空内容后延迟刷新。与**长上下文中的工具执行时序**和**流式响应完整性**相关。[链接](https://github.com/anthropics/claude-code/issues/63797) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|:---|:---|:---|
| **#62099** | Add credential-guard plugin for hardcoded secret detection | **PreToolUse 钩子机制**：在 Write/Edit/Bash 工具调用前扫描 20+ 凭证模式，实现**工具使用的安全对齐（safety alignment at tool boundary）**。对研究"工具学习的约束优化"有参考价值。[链接](https://github.com/anthropics/claude-code/pull/62099) |

> 其余 PR（#63467, #63686, #63460）为文档/流程维护，与研究方向无关。

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|:---|:---|:---|
| **扩展思维的状态持久化危机** | #10199, #63147, v2.1.156 补丁 | 长推理链的**中间状态序列化**成为瓶颈；需研究 thinking block 的**不可变数据结构**与**增量校验** |
| **多语言后训练分布偏移** | #62961（韩语 18× 异常） | 非英语语言的**奖励模型校准不足**；需建立**语言特定的输出分布监控** |
| **系统指令遵循的层级冲突** | #63802, #14200（规则支持需求） | 用户指令、系统提示、插件规则间的**优先级仲裁机制**缺失；与**Constitutional AI 的层级扩展**相关 |
| **过度拒绝的分布外泛化** | #60366 | 安全训练的**保守偏差（conservative bias）**导致高误报；需研究**不确定性量化引导的拒绝决策** |
| **工具输出流的时序完整性** | #63797 | 高并发长会话中的**异步工具执行与 LLM 上下文同步**问题；涉及**事件驱动架构的推理一致性** |

---

## 6. 技术局限性

| 限制 | 重复性证据 | 研究空白 |
|:---|:---|:---|
| **Thinking block 的修改不可检测** | #10199, #63147, v2.1.156 | 缺乏**推理链的密码学完整性验证**或**结构化编辑的 diff 协议** |
| **会话恢复时的状态不一致** | #63147（transcript 空 text + 保留 signature） | 无**推理状态的正式化快照机制**；需研究**merkle-tree 化的 thinking trace** |
| **非英语语言的 token 分布监控缺失** | #62961 | 无**语言特定的 perplexity/频率异常检测** pipeline |
| **工具输出的流式解析 race condition** | #63797 | 高并发场景下**工具 stdout/stderr 与 LLM 上下文窗口的原子性注入**未解决 |
| **系统指令与便捷目标的冲突** | #63802 | **长期目标 vs 短期奖励**的权衡机制未显式建模；缺乏**claude.md 的强制优先级覆盖** |

---

*摘要基于 2026-05-30 UTC 数据生成。聚焦长上下文推理、多模态处理、post-training 对齐与幻觉缓解的技术信号，过滤产品化与商业功能噪音。*

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

# OpenAI Codex 研究动态摘要 | 2026-05-30

## 1. 今日速览

今日 Codex 仓库活跃度高，但**核心研究方向（长上下文推理、OCR/HMER、多模态推理、post-training 对齐、幻觉缓解）的直接相关动态有限**。主要信号集中在**长上下文管理的工程实践**（context window indicator 修复、remote compact task 失败、thread 状态恢复）以及**多模态输入的可靠性问题**（exec_command stdout 污染 input_image base64）。云配置管理层面的 PR 堆栈持续推进，暗示企业级对齐与可控性需求增长。

---

## 2. 版本发布

**rust-v0.136.0-alpha.1** 发布，但 release note 未披露具体变更细节。基于近期 PR 方向推测，可能包含云配置 bundle 运行时切换相关改动，但与核心研究方向的直接关联待验证。

---

## 3. 研究相关 Issues

| # | Issue | 研究方向关联 | 研究价值 |
|---|-------|-----------|---------|
| [#24797](https://github.com/openai/codex/issues/24797) | **Remote compact task fails with unknown variant `auto`** — 长运行 thread 无法继续，remote compact 任务因枚举值 `auto` 未被识别而失败 | **长上下文推理** | 暴露**动态上下文压缩（dynamic context compaction）**的协议兼容性问题。`auto` 作为智能压缩策略的枚举值在客户端-服务端协商中解析失败，反映长上下文管理机制的跨版本演化挑战。对研究自动上下文预算分配、渐进式摘要策略有参考价值。 |
| [#24272](https://github.com/openai/codex/issues/24272) | **Context window usage indicator not displayed** (已关闭) | **长上下文推理** | VS Code 扩展中上下文窗口用量指示器缺失，属于**长上下文可视化与可解释性**基础设施。修复有助于用户理解模型注意力分配，辅助研究 human-in-the-loop 的上下文管理策略。 |
| [#23591](https://github.com/openai/codex/issues/23591) | **Reimplement visible context/token usage indicator** (已关闭) | **长上下文推理** | 用户强烈需求（34 👍）推动的 token 用量指示器重实现，反映**长上下文推理的可解释性需求**正在产品化。对研究上下文预算预警机制、用户认知负荷优化有直接参考。 |
| [#24582](https://github.com/openai/codex/issues/24582) | **exec_command stdout framing leaks into input_image base64, corrupting Responses API requests** | **多模态推理 / OCR/HMER** | **严重多模态输入污染 bug**：代码执行模式的 stdout 帧边界泄漏到 `input_image` 的 base64 编码中，导致图像数据损坏。直接威胁**视觉-语言模型的输入完整性**，对研究多模态数据管道隔离、base64 编码鲁棒性、OCR 前处理可靠性有关键警示意义。 |
| [#24571](https://github.com/openai/codex/issues/24571) | **Codex Desktop stuck thinking after interrupted/resumed turn with "Item not found in turn state"** | **长上下文推理 / 幻觉缓解** | 中断-恢复场景下的**turn 状态机不一致**，模型陷入"思考中"死锁。涉及**长对话状态恢复**与**模型行为确定性**问题，对研究对话系统的鲁棒性、幻觉触发条件（如无限生成循环）有分析价值。 |
| [#24572](https://github.com/openai/codex/issues/24572) | **GPT 5.5 Extra high 1.5X speed stuck in thinking, only 200 lines of simple code** | **长上下文推理 / 幻觉缓解** | 高速度模式下的**过度思考（overthinking）**现象，简单任务耗时异常。反映**推理时计算（inference-time compute）与任务复杂度不匹配**，对研究自适应思考深度、early-exit 机制、推理效率-质量权衡有实证价值。 |
| [#23588](https://github.com/openai/codex/issues/23588) | **Subagent completion notification shows UUID instead of nickname** | **多智能体推理 / 长上下文** | 子智能体标识可读性回归，涉及**多智能体系统的上下文组织与认知负荷**。对研究层级化 agent 架构中的信息呈现、长上下文中实体引用一致性有间接参考。 |
| [#24581](https://github.com/openai/codex/issues/24581) | **TUI subagent history should render nickname/role instead of raw thread ids** (已关闭) | **多智能体推理 / 长上下文** | 同上，子智能体历史记录的可读性修复，强化**多智能体长上下文的结构化表示**需求。 |
| [#25179](https://github.com/openai/codex/issues/25179) | **Codex app accumulates stale subagents in cache/UI and cannot be closed reliably** | **长上下文推理 / 系统可靠性** | 长运行会话中**子智能体生命周期管理缺陷**，缓存泄漏导致上下文膨胀。对研究动态上下文修剪、agent 状态机正确性、资源约束下的长期运行稳定性有直接关联。 |
| [#24833](https://github.com/openai/codex/issues/24833) | **MCP: re-evaluate resume_path for Codex sessions** | **长上下文推理** | 请求通过 `resume_path` 从 rollout 文件恢复 Codex 会话，涉及**对话状态持久化与长上下文恢复**。对研究会话连续性、断点续传、长期任务的记忆机制有需求驱动价值。 |

---

## 4. 研究相关 PR 进展

| # | PR | 技术贡献 | 研究方向 |
|---|-----|---------|---------|
| [#25184](https://github.com/openai/codex/pull/25184) / [#25182](https://github.com/openai/codex/pull/25182) | **Propagate Codex installation id in Responses headers** | 将 `x-codex-installation-id` 从 `/responses/compact` 扩展至常规 Responses HTTP 与 WebSocket 握手，支持**请求级归因与追踪**。为大规模部署中的**行为分析、A/B 测试、对齐效果评估**提供基础设施。 | Post-training 对齐 / 系统可靠性 |
| [#25151](https://github.com/openai/codex/pull/25151) | **Extract prompts from codex-core into codex-prompts crate** | 将提示词渲染与静态资源从核心库剥离，集中管理 review、goal、permissions、compaction、realtime、hierarchical AGENTS.md 等提示。提升**提示工程的可审计性**，为**系统提示的对齐研究**（如提示注入防御、目标条件化）创造结构条件。 | Post-training 对齐 / 提示工程 |
| [#25177](https://github.com/openai/codex/pull/25177) | **Preserve cloud requirements across TUI thread resets** | 修复 `/new`、`/clear` 等 thread 重置时云配置要求丢失的回归，确保**企业级约束的持续性**。反映**运行时对齐约束（runtime alignment constraints）**的工程化需求。 | Post-training 对齐 / 可控性 |
| [#24620](https://github.com/openai/codex/pull/24620) ~ [#24622](https://github.com/openai/codex/pull/24622) / [#24619](https://github.com/openai/codex/pull/24619) | **Cloud-managed config bundle stack (PR 2-5 of 5)** | 企业云配置作为一等配置层，统一配置加载、诊断、调试、hook 归因与协议表面。实现**分层需求组合引擎**，定义有序配置层的合并语义与来源行为。 | Post-training 对齐 / 组织级可控性 |
| [#25176](https://github.com/openai/codex/pull/25176) | **Route standalone image generation through host finalization** | 独立图像生成扩展的事件流经宿主终结层，确保**图像持久化与贡献者处理**不绕过宿主控制。同时保持生成路径对模型的可见性。强化**多模态输出的可控性与审计性**。 | 多模态推理 / 系统可靠性 |
| [#24696](https://github.com/openai/codex/pull/24696) | **Support Library uploads for Codex Apps** | Codex Apps 文件上传工具显式要求 `save_to_openai_library: true`，将**持久化写操作暴露于审批审查**。研究**工具使用的透明度与用户监督**机制，对抗不可见的数据外泄风险。 | Post-training 对齐 / 工具安全 |
| [#25121](https://github.com/openai/codex/pull/25121) | **exec-server: add environment path refs** | 为 exec-server 引入 `EnvironmentPathRef`，将绝对路径绑定至所属执行器文件系统。技能路径权限栈的基础，支撑**沙箱内文件访问的精细化授权**。 | 系统安全 / 多模态输入隔离 |
| [#24956](https://github.com/openai/codex/pull/24956) | **Prevent macOS fs-helper startup hangs** | 拆分 macOS 最小平台策略为原生运行时权限与文件系统默认，确保 fs-helper 在完整磁盘读取策略下仍保留必要运行时权限。提升**多模态文件访问（如图像读取）的启动可靠性**。 | 多模态推理 / 系统可靠性 |
| [#23766](https://github.com/openai/codex/pull/23766) | **Constrain Windows sandbox requirements** (已关闭) | 托管需求可约束沙箱策略选择，Windows 沙箱实现选择与管理需求联动，阻止非预期降级。强化**组织级安全策略对运行时行为的约束力**。 | Post-training 对齐 / 可控性 |

---

## 5. 研究方向信号

### 5.1 长上下文推理：从"能装"到"能管"的工程紧迫性

- **动态压缩协议演化**：`auto` 枚举值解析失败（#24797）暴露上下文压缩策略的客户端-服务端协商机制仍在快速迭代，**自适应上下文预算分配**的协议标准化需求凸显。
- **可视化与可解释性成为硬需求**：token 用量指示器的反复修复（#24272, #23591）反映用户对**上下文消耗感知**的强烈需求，暗示长上下文产品的用户信任瓶颈。
- **会话恢复与状态持久化**：`resume_path` 需求（#24833）及中断-恢复死锁（#24571）表明，**长任务连续性**是生产部署的关键缺口，对研究 checkpoint/restore、渐进式摘要、记忆架构有直接需求拉动。

### 5.2 多模态推理：数据管道隔离的可靠性挑战

- **跨模态数据污染**：exec_command stdout 泄漏至 image base64（#24582）是**严重的多模态输入完整性事件**，揭示文本-视觉数据通道的边界防护不足。对 OCR/HMER 等精细视觉任务，此类污染可能导致灾难性识别错误。
- **图像生成输出的宿主控制**：#25176 的终结层路由强化**多模态输出的可审计性**，暗示 OpenAI 正在收紧视觉能力的系统级管控。

### 5.3 Post-training 对齐：企业级可控性的架构深化

- **云配置层成为对齐基础设施**：5 个 PR 的云配置 bundle 堆栈（#24619-#24622）将组织级策略加载、合并、持久化提升为核心架构，反映**对齐从模型层向系统层扩展**的趋势。
- **提示工程的可审计化**：#25151 的 prompt crate 提取使系统提示的结构化审查成为可能，为**提示级对齐干预**（如 Constitutional AI 的系统提示实现）创造条件。

### 5.4 幻觉缓解：间接信号多于直接进展

- 今日无明确标注"幻觉"的 issue，但**过度思考**（#24572，简单任务无限循环）和**状态机不一致**（#24571）均属于**生成行为失控**的表现形式，与幻觉共享根因（如推理时计算分配失当、状态维护错误）。

---

## 6. 技术局限性

| 局限领域 | 具体表现 | 研究空白 |
|---------|---------|---------|
| **长上下文状态机鲁棒性** | 中断-恢复后 turn 状态丢失（#24571）、remote compact 协商失败（#24797）、子智能体缓存泄漏（#25179） | 缺乏**形式化验证的对话状态机**；**渐进式上下文压缩的容错协议**研究不足 |
| **多模态数据管道隔离** | 文本 stdout 污染图像 base64（#24582） | **跨模态数据流的边界编码与验证机制**；视觉输入的完整性校验（如 base64 帧签名） |
| **推理时计算自适应** | 高速度模式反而过度思考（#24572） | **任务复杂度感知的推理预算分配**；speed/quality 权衡的动态优化 |
| **子智能体生命周期管理** | UUID 可读性缺失（#23588, #24581）、缓存无法清理（#25179） | 多智能体系统的**上下文垃圾回收**；层级化 agent 的**引用完整性**维护 |
| **企业级对齐的工程-研究鸿沟** | 云配置堆栈庞大但 issue 中用户侧感知有限 | 如何将组织级策略**可解释地映射**到模型行为约束，缺乏用户研究验证 |

---

*摘要基于 GitHub 公开数据生成，未包含非公开研究进展。核心研究方向（OCR/HMER、纯视觉推理）的直接动态今日未显著出现，建议持续关注多模态数据管道相关 issue 的演化。*

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

# Gemini CLI 研究动态摘要 | 2026-05-30

## 今日速览

今日 Gemini CLI 无直接面向长上下文推理、OCR/HMER 或多模态的研究发布，但**Agent 系统的工具使用边界与可靠性**成为核心议题：AST 感知代码工具评估持续推进，MCP 工具原子更新与回退机制、模型输出清洗（CJK 字符过滤）等 PR 体现了对**工具调用可靠性和输出对齐**的工程化关注。Auto Memory 系统的多项修复则反映了**长期上下文记忆质量**仍是活跃研究方向。

---

## 版本发布

**v0.45.0-nightly.20260529.gc82e2b597**
- 仅包含 PTY resize 崩溃修复与 changelog 更新，**无研究相关变更**。

---

## 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|---------|
| [#24353](https://github.com/google-gemini/gemini-cli/issues/24353) | Robust component level evaluations | **评估基础设施**：76 个行为评估测试的组件级扩展，直接支撑 Agent 能力的长上下文一致性评估与幻觉检测方法论 |
| [#22745](https://github.com/google-gemini/gemini-cli/issues/22745) | AST-aware file reads, search, and mapping | **结构化推理增强**：通过 AST 边界精确读取降低 token 噪声、减少多轮 misalignment，与长上下文效率密切相关 |
| [#22746](https://github.com/google-gemini/gemini-cli/issues/22746) | Investigate using AST aware CLI tools to map codebase | **代码表征学习**：tilth/glyph 工具链探索，潜在提升 codebase_investigator 的长上下文语义导航能力 |
| [#22747](https://github.com/google-gemini/gemini-cli/issues/22747) | AST aware tools to search and perform file reads | **语法感知检索**：AST-grep 集成评估，验证结构化查询对 Agent 推理效率的提升 |
| [#21409](https://github.com/google-gemini/gemini-cli/issues/21409) | Generalist agent hangs | **推理可靠性**：子 Agent 调度中的无限挂起，暴露长上下文任务分解中的中断恢复机制缺陷 |
| [#22323](https://github.com/google-gemini/gemini-cli/issues/22323) | Subagent recovery after MAX_TURNS is reported as GOAL success | **幻觉/对齐**：MAX_TURNS 截断被错误报告为成功，属于典型的**过程-结果对齐失败**与状态幻觉问题 |
| [#26525](https://github.com/google-gemini/gemini-cli/issues/26525) | Deterministic redaction and reduce Auto Memory logging | **隐私对齐/幻觉缓解**：模型侧 redaction 不可靠，需确定性预处理；Auto Memory 的上下文注入存在信息泄露风险 |
| [#26523](https://github.com/google-gemini/gemini-cli/issues/26523) | Surface or quarantine invalid Auto Memory inbox patches | **记忆一致性**：无效 patch 的静默跳过导致上下文污染，影响长期对话的幻觉累积 |
| [#26522](https://github.com/google-gemini/gemini-cli/issues/26522) | Stop Auto Memory from retrying low-signal sessions indefinitely | **上下文质量过滤**：低信号会话的重复处理造成噪声上下文循环，与长上下文信噪比优化相关 |
| [#24246](https://github.com/google-gemini/gemini-cli/issues/24246) | 400 error with > 128 tools | **工具上下文边界**：工具数量超限暴露模型上下文窗口的硬约束，需研究动态工具选择机制 |

---

## 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|---------|
| [#27570](https://github.com/google-gemini/gemini-cli/pull/27570) | Transition to flash GA model | **模型能力迁移**：Gemini 3.5 Flash GA 过渡，实验标志控制下评估新模型在长上下文与推理任务的表现 |
| [#27383](https://github.com/google-gemini/gemini-cli/pull/27383) | Prevent eager tool wipe on network timeout | **工具调用可靠性**：MCP 工具原子更新模式，网络瞬断时保留既有工具状态，避免"tool not found"级联错误——**对齐工具行为与系统状态** |
| [#27568](https://github.com/google-gemini/gemini-cli/pull/27568) | Fall back when ripgrep execution fails | **鲁棒性回退**：执行环境异常时的保守降级策略，维持工具链可靠性而不改变语义行为 |
| [#27349](https://github.com/google-gemini/gemini-cli/pull/27349) | Strip CJK characters from model thought output | **输出对齐/幻觉缓解**：清洗模型 thought 中的非目标语言字符，直接针对**跨语言幻觉**与推理输出污染 |
| [#27348](https://github.com/google-gemini/gemini-cli/pull/27348) | Wrap Ajv validate() in try/catch | **结构化生成可靠性**：防止 LLM 异常参数形状导致的校验崩溃，属于**约束解码失败后的容错对齐** |
| [#27347](https://github.com/google-gemini/gemini-cli/pull/27347) | Add command validation to prevent NL being saved as shell | **指令-执行对齐**：阻断自然语言被误存为可执行命令，减少**意图-行为错位**类安全幻觉 |
| [#25643](https://github.com/google-gemini/gemini-cli/pull/25643) | Throttle text output updates to prevent UI jank | **流式生成稳定性**：高体积输出下的渲染节流，支撑长上下文生成的实时可观测性 |
| [#26324](https://github.com/google-gemini/gemini-cli/pull/26324) | Prevent ghost text wrapping infinite loop | **交互式生成边界**：零宽度场景下的挂起修复，保障长提示补全的确定性终止 |

---

## 研究方向信号

| 趋势 | 证据 |
|------|------|
| **AST 感知推理成为代码 Agent 标配** | #22745/22746/22747 三 issue 形成完整评估矩阵，从读取→搜索→映射全链路验证结构化工具对 token 效率与推理精度的提升 |
| **Auto Memory 的"上下文质量工程"** | #26522/26523/26525 集中暴露：长期记忆系统需解决**低信号过滤、无效 patch 隔离、隐私确定性**三重问题，而非简单扩展窗口 |
| **工具调用的"状态幻觉"修复** | #27383（原子更新）、#22323（成功状态误报）、#27568（回退一致性）共同指向：Agent 需建立**工具状态-执行结果-报告语义**的三方对齐 |
| **跨语言输出污染控制** | #27349 直接干预模型 thought 的语言分布，反映多语言模型在单语场景下的**隐性语言切换幻觉** |

---

## 技术局限性

| 限制 | 频次 | 研究空白 |
|------|------|---------|
| **子 Agent 调度中断不可恢复** | 高（#21409, #22323） | 长上下文任务分解中的**检查点与恢复机制**缺失；MAX_TURNS 截断后的状态报告属于**过程幻觉**的典型模式 |
| **工具数量硬边界（~128）** | 中（#24246） | 动态工具选择/压缩机制未成熟，长上下文场景下工具描述占用与有效推理的权衡缺乏系统方法 |
| **模型输出语言漂移** | 中（#27349） | 多语言模型的 thought 语言控制缺乏约束解码或后处理标准方案 |
| **Auto Memory 的信号-噪声分离** | 高（#26522-26525） | 长期上下文的**自适应遗忘与重要性采样**尚无产品级实现，依赖启发式规则 |
| **AST 工具的效果验证瓶颈** | 中（#22745 系列） | 缺乏组件级评估与端到端任务成功的因果关联度量，AST 引入的 latency 与 accuracy trade-off 未量化 |

---

*摘要聚焦：长上下文效率、结构化推理增强、工具调用可靠性、输出对齐与幻觉缓解。OCR/HMER 与纯视觉多模态当日无直接动态。*

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

# GitHub Copilot CLI 研究动态摘要（2026-05-30）

## 1. 今日速览

今日 Copilot CLI 发布 v1.0.57-0，重点优化了**上下文窗口利用率**（MCP 工具去重减少 token 消耗）和**长上下文持久化**（contextTier 恢复修复）。社区密集反馈了**MCP 工具过度占用上下文窗口**（73% 被系统/工具消耗）和**子代理在特定模型下静默挂起**等深层推理架构问题，反映出当前 agentic 系统在长上下文管理和多模型可靠性上的显著张力。

---

## 2. 版本发布

### v1.0.57-0 / v1.0.56-2 / v1.0.56-1（2026-05-29~30）

| 版本 | 研究相关更新 | 技术意义 |
|:---|:---|:---|
| **v1.0.56-1** | GitHub MCP server 自动省略 `gh`-可替代工具，减少 token 使用 | **上下文效率**：通过工具去重降低系统提示开销，直接缓解长上下文压力 |
| **v1.0.56-1** | Code review agent 使用当前会话模型替代固定默认模型 | **模型一致性**：避免多模型混用导致的推理行为漂移，减少幻觉风险 |
| **v1.0.56-2** | `web_fetch` 工具优先获取 markdown，使用 HTTP content negotiation | **结构化内容理解**：提升文档类输入的语义纯度，间接优化多模态/长文本推理质量 |
| **v1.0.56** | Model picker 显示各 pricing tier 的准确总上下文窗口大小 | **上下文透明度**：用户可感知真实可用上下文，辅助长任务规划 |
| **v1.0.57-0** | SDK auth-token 验证失败时暴露底层原因（如 API rate limit） | **可靠性**：减少错误信息的幻觉性误导，提升系统可解释性 |

---

## 3. 研究相关 Issues（精选 8 条）

### 🔴 长上下文推理

**[#3539](https://github.com/github/copilot-cli/issues/3539)** System/Tools consume 73% of context window (146k/200k), triggering auto-compaction on first message
- **研究价值**：揭示了 MCP 生态的"上下文膨胀"危机——10 个 MCP server 即可耗尽 73% 的 200K 窗口。这是**长上下文推理**的系统性瓶颈：工具描述、schema、示例的 token 开销呈组合爆炸。用户被迫在"功能丰富"与"推理深度"间权衡。需研究动态工具选择、工具描述压缩、或分层上下文架构。

**[#3557](https://github.com/github/copilot-cli/issues/3557)** [CLOSED] `contextTier` setting (e.g. `long_context`) is not restored from settings.json on startup
- **研究价值**：长上下文模式（如 1M 的 `claude-opus-4.7-1m-internal`）的持久化失败导致用户实际使用短上下文，引发**隐性性能退化**。修复此问题对长上下文任务的可靠性至关重要。

**[#1869](https://github.com/github/copilot-cli/issues/1869)** gpt-5-mini is not persistent set for future sessions
- **研究价值**：模型选择的非持久化导致**推理行为不一致**，跨会话的模型漂移可能引发输出质量波动和幻觉风险。

### 🔴 Agentic 推理与可靠性

**[#3547](https://github.com/github/copilot-cli/issues/3547)** Background sub-agent silently hangs at `total_turns=0` when `model="gpt-5.5"`
- **研究价值**：**关键可靠性缺陷**——子代理在特定模型下静默挂起（无错误、无超时），父代理无法感知失败。这暴露了多 agent 系统的**故障隔离不足**和**模型特定行为差异**，是幻觉缓解和系统鲁棒性的核心挑战。

**[#3574](https://github.com/github/copilot-cli/issues/3574)** [CLOSED] Enable better options for subagent prompting
- **研究价值**：用户需要向子代理注入**强制性前置提示**（如代码探索前加载 skill），当前系统缺乏**提示注入的可靠机制**。这涉及 post-training 对齐中的"系统提示层级"设计问题。

**[#3568](https://github.com/github/copilot-cli/issues/3568)** [CLOSED] Built-in support for parallel sub-agent execution in plugins?
- **研究价值**：并行子代理执行的需求反映了**多线程推理**的架构趋势，但当前缺乏原生支持。并行执行涉及结果聚合、竞态条件、上下文隔离等深层问题。

### 🔴 幻觉与可解释性

**[#3258](https://github.com/github/copilot-cli/issues/3258)** [CLOSED] MCP tool responses: only `structuredContent` is forwarded to the model, unstructured content is dropped
- **研究价值**：**信息丢失型幻觉**——MCP 返回的双模态内容中，非结构化文本被静默丢弃。这导致模型基于不完整输入推理，产生**不可追溯的幻觉输出**。需研究结构化/非结构化内容的融合机制。

**[#3311](https://github.com/github/copilot-cli/issues/3311)** [CLOSED] CLI auth flow silently swallows REST quota / rate-limit errors during token validation
- **研究价值**：错误信息的**幻觉性转换**——底层 rate limit 被包装为误导性认证错误。这属于系统层面的**可解释性缺陷**，掩盖真实故障模式。

---

## 4. 研究相关 PR 进展

**无**（过去 24 小时无 PR 更新）

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|:---|:---|:---|
| **上下文窗口危机** | #3539（73% 工具占用）、#3557（长上下文恢复失败）、v1.0.56-1（gh 工具去重） | MCP 生态的"工具膨胀"正在吞噬长上下文红利，需 urgent 研究**动态工具选择**、**工具描述压缩**、**分层 RAG 架构** |
| **多模型可靠性差异** | #3547（gpt-5.5 子代理挂起）、#1869（模型持久化失败） | 不同模型的 agentic 行为存在显著差异，需建立**模型能力矩阵**和**自适应路由**机制 |
| **Agent 层级对齐** | #3574（子代理提示注入）、#3568（并行执行） | 从单轮对话对齐转向**多 agent 系统的层级对齐**，包括父-子代理的意图传递、技能继承、故障隔离 |
| **结构化内容幻觉** | #3258（结构化内容丢弃）、v1.0.56-2（markdown 优先） | 多模态输入的**选择性丢失**成为新型幻觉源，需研究**完整性验证**和**多模态融合**机制 |
| **系统提示透明度** | #3311（错误信息误导）、v1.0.57-0（暴露底层原因） | 错误处理的**忠实性**直接影响用户对系统可信度的感知，是**可解释 AI** 的落地场景 |

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 研究空白 |
|:---|:---|:---|
| **上下文预算静态分配** | 系统/工具提示占 73% 窗口，用户无动态调控手段 | 缺乏**自适应上下文预算算法**，无法根据任务复杂度动态调整工具加载策略 |
| **模型行为不可迁移** | 同一 agent 逻辑在不同模型（gpt-5.5 vs claude-sonnet-4.6）表现迥异 | 缺乏**模型无关的 agent 抽象层**和**能力声明机制** |
| **子代理故障静默** | 背景子代理可无限挂起（`total_turns=0`），无超时/无告警 | 缺乏**分布式 agent 的心跳检测**和**级联故障隔离**机制 |
| **内容选择性丢失** | MCP 双模态响应被截断，模型基于不完整信息推理 | 缺乏**输入完整性校验**和**缺失信息显式标注**机制 |
| **长状态持久化脆弱** | contextTier、模型选择等关键配置频繁丢失 | 缺乏**事务性配置持久化**和**启动状态一致性校验** |

---

*摘要生成时间：2026-05-30 | 数据来源：github.com/github/copilot-cli*

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

# Kimi Code CLI 研究动态摘要（2026-05-30）

---

## 1. 今日速览

今日 Kimi CLI 发布 **v1.46.0**，核心变动为项目向 **Kimi Code** 继任者迁移的文档宣告，工程层面聚焦依赖松弛与上下文压缩可靠性修复。研究相关信号集中暴露于**长上下文压缩缺陷**（空 TextPart 导致 API 400）与**Agent 工具调用机制失效**（skill 自动触发缺失回退 raw shell），反映多模态/工具增强推理链的鲁棒性仍为关键瓶颈。

---

## 2. 版本发布

### v1.46.0（2026-05-29）
| 项目 | 内容 |
|:---|:---|
| 发布 PR | [#2391](https://github.com/MoonshotAI/kimi-cli/pull/2391) |
| 研究相关变更 | 无直接模型/算法更新；**Kosong 框架**（底层依赖）同步 bump，为后续 Kimi Code 架构迭代铺垫 |

> 注：本次 release 以品牌迁移与版本对齐为主，未涉及推理、视觉或对齐层面的功能迭代。

---

## 3. 研究相关 Issues

| # | 状态 | 标题 | 研究价值 | 链接 |
|:---|:---|:---|:---|:---|
| **#2396** | 🔴 OPEN | Bug: `kimi export` crashes during **context compaction** — API 400 text content is empty | **长上下文可靠性**：上下文压缩路径遗漏空 `TextPart` 过滤，暴露历史消息清洗机制在超长会话中的边界缺陷；直接关联长上下文推理的稳定性 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2396) |
| **#2399** | 🔴 OPEN | Agent ignores available **skills** and falls back to raw shell commands due to missing **auto-trigger mechanism** | **多模态/工具增强推理**：Agent 的 skill 路由机制失效，模型无法正确识别何时调用结构化工具 vs. 生成原始 shell，反映工具使用（Tool Use）的对齐与触发决策问题 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2399) |
| **#1994** | 🔴 OPEN | kimiCode 用量计算问题 — K2.6 **思维链过长**导致 token 极速耗尽 | **长上下文推理成本**：思维链（CoT）长度与计费策略的冲突，暴露长推理链在实际部署中的经济可行性瓶颈；需研究 CoT 压缩或动态预算分配 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/1994) |
| **#2123** | 🔴 OPEN | 限速/限额严重 — 频控频繁重置、额度快速耗尽 | **推理系统效率**：5 小时 60+ 次 vs. 宣称 300-1200 次的差距，暗示后端批处理或 KV Cache 复用效率不足，或长上下文请求的实际成本被低估 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2123) |
| **#778** | 🔴 OPEN | API Error 400 invalid_request_error（Claude 模型路由） | **多模型对齐/路由**：跨模型（Claude Sonnet 4.5）调用时的请求格式兼容性，涉及不同后训练格式间的协议转换 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/778) |

> **排除说明**：#2397（shell 命令执行基础用法）、#247（密钥配置启动故障）属用户支持/产品体验问题，与研究无关。

---

## 4. 研究相关 PR 进展

| # | 状态 | 标题 | 技术贡献 | 链接 |
|:---|:---|:---|:---|:---|
| **#2395** | 🟢 OPEN | **fix(compaction)**: filter empty text parts to avoid API 400 | **长上下文可靠性**：补全 #1663 遗漏的压缩路径，对历史消息中的空/纯空白 `TextPart` 进行过滤；直接修复 #2396，保障超长会话的上下文压缩不中断推理链 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2395) |
| **#2245** | 🟢 OPEN | **fix**: improve provider error UX across **429 surfaces** | **系统可靠性/对齐**：统一 provider 错误格式化层，区分**周期配额耗尽**与**瞬时速率限制**（period quota vs. transient 429），为后端限流策略的透明化与用户对推理成本的可预期性提供基础 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2245) |
| **#2398** | 🟢 OPEN | **chore**: relax OpenAI and FastMCP dependency pins | **多模态工具生态**：FastMCP 3.3.1 升级支持更灵活的模型上下文协议（MCP）工具注册，利好多模态 Agent 的工具扩展；OpenAI SDK 范围松弛降低下游推理框架的依赖冲突 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2398) |

> **排除说明**：#2391 为纯版本 bump 发布流程，无技术研究价值。

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|:---|:---|:---|
| **长上下文压缩鲁棒性** | #2396 + #2395 暴露压缩路径的空内容过滤遗漏 | 超长会话（>100K tokens）的历史消息清洗、摘要、压缩机制仍需系统性加固；空/噪声 token 的过滤是保障多轮推理稳定性的基础工程 |
| **思维链长度 vs. 成本张力** | #1994 用户反馈 K2.6 CoT 过长导致 2 小时额度仅够 2 次交互 | **推理效率研究**迫切：需探索 CoT 蒸馏、自适应深度思考、或动态预算分配的 post-training 方法，平衡推理质量与部署成本 |
| **Agent 工具决策对齐** | #2399 skill 自动触发机制缺失 | 模型在"生成代码/命令" vs. "调用结构化工具"间的**决策边界模糊**，需强化工具使用的 SFT/RLHF 对齐，或引入显式的技能路由分类器 |
| **速率限制的信息透明** | #2123 + #2245 围绕配额计算与 429 区分 | 后端资源调度与前端用户预期的**对齐缺口**，涉及推理系统的可解释性与公平性设计 |

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 研究空白 |
|:---|:---|:---|
| **上下文压缩的边界覆盖** | 工具消息修复于 #1663，但压缩路径遗漏同类问题（#2395） | 缺乏统一的**全路径消息校验框架**，不同上下文操作（工具返回、压缩、导出）的清洗逻辑分散 |
| **长 CoT 的成本不可控** | K2.6 思维链过度膨胀，用户侧无感知/无干预机制（#1994） | **动态推理深度控制**：如何在推理过程中实时评估是否需要继续思考，或提前终止并给出次优解 |
| **Skill/Tool 触发决策黑盒** | Agent 无法自主识别可用 skill，回退低效的 raw shell（#2399） | 缺乏**工具可用性感知**的显式机制：模型需先判断"当前任务是否有匹配 skill"，再决定生成策略 |
| **配额计算与推理成本的映射不透明** | 官方"300-1200 次"与实际 60 次差距大，用户无法预估（#2123） | 需要**请求复杂度预测模型**：基于上下文长度、工具调用深度、预期 CoT 长度等特征，给出实时成本估计 |

---

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

# OpenCode 研究动态摘要 | 2026-05-30

---

## 1. 今日速览

今日 OpenCode 社区无新版本发布，但 **PR #29949** 针对长上下文推理中的 prompt caching 稳定性提出关键修复，将环境变量块移至 system prompt 尾部以保持前缀缓存一致性。同时 **Issue #20695** 的内存问题集中讨论持续发酵，暴露了大上下文场景下的工程瓶颈。多模态方面，**PR #21352** 已合并支持工具返回图像附件的 UI 渲染，但底层视觉推理能力未见实质进展。

---

## 2. 版本发布

无新版本发布。

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 | 链接 |
|---|------|------|---------|------|
| **#20695** | Memory Megathread | 🔴 OPEN | **长上下文推理核心瓶颈**。社区集中追踪内存泄漏/高占用问题，要求收集 heap snapshots。直接影响长序列推理的稳定性与可扩展性，是 LLM 工程化的关键研究议题。 | [链接](https://github.com/anomalyco/opencode/issues/20695) |
| **#29941** | ReadableStreamDefaultController crash — 'Controller is already closed' cascades to PTY failure | 🔴 OPEN | **流式推理可靠性**。内存压力下（与 #29939 MCP 重复进程相关）的流控制崩溃，暴露异步生成与资源管理的边界条件缺陷，关联长上下文生成中的流式输出稳定性。 | [链接](https://github.com/anomalyco/opencode/issues/29941) |
| **#21227** | [FEATURE(app)]: display image attachments from tool results in chat UI | 🔴 OPEN | **多模态推理链路**。工具返回图像数据（webfetch/MCP ImageContent）无法在聊天 UI 展示，阻断视觉-语言交互闭环。PR #21352 已尝试修复但状态为 closed，需关注是否真正解决。 | [链接](https://github.com/anomalyco/opencode/issues/21227) |
| **#29939** | MCP servers spawn duplicate processes per session — 1 project = 8+ instances | 🔴 OPEN | **系统级资源膨胀**。MCP 服务器按会话重复 spawn，导致多项目场景崩溃。间接限制多模态工具链（如视觉 MCP 服务）的并发能力，影响复杂推理工作流。 | [链接](https://github.com/anomalyco/opencode/issues/29939) |
| **#27106** | The latest version is terribly slow | 🔴 OPEN | **推理延迟退化**。v1.14.48 性能严重下降，"practically unusable"。需区分是模型推理层还是系统开销，关联长上下文处理的计算效率研究。 | [链接](https://github.com/anomalyco/opencode/issues/27106) |
| **#29786** | Opus 4.8 bug in dev branch | 🔴 OPEN | **子代理模型可靠性**。Claude Opus 4.8 在子代理模式下的异常行为，涉及 agentic 系统中模型选择策略与错误传播机制。 | [链接](https://github.com/anomalyco/opencode/issues/29786) |
| **#27530** | Error: 4 of 5 requests failed: config.providers: Unexpected server error | 🔴 OPEN | **服务层容错与降级**。启动时多请求级联失败，缺乏优雅降级。研究价值在于构建鲁棒的推理系统错误隔离机制。 | [链接](https://github.com/anomalyco/opencode/issues/27530) |
| **#17765** | Windows Desktop loses all session history after restart | 🔴 OPEN | **状态持久化与上下文恢复**。会话历史 UI 丢失但 DB 存在，涉及长对话状态的一致性与恢复机制，关联对话记忆研究。 | [链接](https://github.com/anomalyco/opencode/issues/17765) |
| **#29921** | [needs:compliance] security: ReDoS in wildcard pattern matching via regex injection | 🟢 CLOSED | **输入安全与推理完整性**。用户可控输入导致指数级慢正则，虽为安全 issue，但直接影响 LLM 工具调用链的可用性与最坏情况复杂度，关联对抗鲁棒性。 | [链接](https://github.com/anomalyco/opencode/issues/29921) |
| **#29915** | error handling: 12 empty catch blocks silently swallow all failures | 🟢 CLOSED | **可靠性工程**。空 catch 块将运行时错误转为静默数据损坏，破坏幻觉检测与错误诊断能力，是可信 AI 系统的基础缺陷。 | [链接](https://github.com/anomalyco/opencode/issues/29915) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 状态 | 技术贡献 | 链接 |
|---|------|------|---------|------|
| **#29949** | fix(session): move env block to tail of system prompt for cache stability | 🟡 OPEN | **长上下文推理优化**。将环境变量块从 system prompt 头部移至尾部，保持前缀可缓存性（prefix-cacheable），直接提升 KV cache 复用效率，降低长会话推理成本。关联 #20110、#5224、#27377/27378。 | [链接](https://github.com/anomalyco/opencode/pull/29949) |
| **#29447** | feat(opencode): add task model override | 🟡 OPEN | **动态模型路由与后训练对齐**。允许主代理在运行时指定子代理的 provider/model，支持任务级模型选择策略。为异构模型调度、能力专用化（如视觉/推理模型切换）及 A/B 测试后训练模型提供基础设施。 | [链接](https://github.com/anomalyco/opencode/pull/29447) |
| **#21352** | feat(ui): display image attachments from tool results | 🟢 CLOSED | **多模态 UI 渲染**。工具返回的 `FilePart` 图像 MIME 类型可在聊天 UI 展示，打通视觉数据回流通道。但需注意该 PR 为 automated-pr-cleanup 关闭，实际落地状态待验证。 | [链接](https://github.com/anomalyco/opencode/pull/21352) |
| **#29937** | feat(opencode): add LiteLLM provider integration | 🟡 OPEN | **统一多模型推理网关**。LiteLLM 作为模型聚合层，简化多后端（OpenAI/Anthropic/本地等）的统一调用，支持研究场景下的模型对比与能力评估。 | [链接](https://github.com/anomalyco/opencode/pull/29937) |
| **#24995** | feat(session): add question tool instructions to gemini.txt system prompt | 🟢 CLOSED | **工具使用对齐**。修复 Gemini 系统提示要求澄清问题但未提及 `question` 工具的指令缺失，提升工具调用遵循度（tool adherence），减少幻觉式提问。 | [链接](https://github.com/anomalyco/opencode/pull/24995) |
| **#25011** | fix: use moonshot MFJS sanitization to prevent api errors w/ kimi models | 🟢 CLOSED | **输出格式鲁棒性**。引入 Moonshot 的 MFJS（Markdown-Fenced JSON Sanitization）清理机制，解决 kimi 模型的 API 错误，关联结构化生成（structured generation）的可靠性研究。 | [链接](https://github.com/anomalyco/opencode/pull/25011) |
| **#24964** | fix(mcp): pass onprogress so resetTimeoutOnProgress actually works | 🟢 CLOSED | **长运行推理的进度感知**。修复 MCP 请求超时机制，确保 `onprogress` 回调正确传递以重置超时。对长时工具调用（如代码分析、文档检索）的稳定性至关重要。 | [链接](https://github.com/anomalyco/opencode/pull/24964) |
| **#12633** | feat(tui): add auto-accept mode for permission requests | 🟡 OPEN | **人机对齐与交互效率**。自动接受编辑权限请求的"autoedit"模式，减少交互摩擦。研究价值在于探索自动化权限边界——过度自动化可能导致未验证操作累积（幻觉行为的放大器）。 | [链接](https://github.com/anomalyco/opencode/pull/12633) |
| **#29943** | fix(opencode): reorder write tool schema to declare filePath before content | 🟡 OPEN | **工具模式优化**。调整 JSON schema 字段顺序，可能影响模型对工具参数的理解与填充顺序，细微但可测量的 prompt engineering 优化。 | [链接](https://github.com/anomalyco/opencode/pull/29943) |
| **#25010** | feat(ui): Add support for RTL languages in rendered chat content | 🟢 CLOSED | **多语言推理与视觉呈现**。RTL 语言支持虽为 UI 特性，但涉及文本渲染方向对模型输出解析的潜在影响（如混合语言场景），关联多语言模型的可靠性。 | [链接](https://github.com/anomalyco/opencode/pull/25010) |

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|------|------|---------|
| **Prompt Caching 工程化** | #29949 系统级修复 prefix cache 稳定性 | 长上下文推理正从"能跑"进入"高效跑"阶段，KV cache 管理成为核心优化点 |
| **多模态工具链碎片化** | #21227/#21352 图像展示反复；#29939 MCP 进程爆炸 | 视觉-语言交互的"最后一公里"未打通，系统级资源管理与 UI 渲染脱节 |
| **动态模型路由需求** | #29447 task model override；#29937 LiteLLM 集成 | 单一模型无法满足复杂任务流，运行时模型选择成为 post-training 部署的关键 |
| **可靠性债务集中爆发** | #29915 空 catch；#29921 ReDoS；#29919 异常处理边界 | 快速迭代导致错误处理薄弱，幻觉与静默失败的风险被系统性低估 |
| **Agent 系统级故障传播** | #29786 Opus 4.8 子代理异常；#29941 流控制级联崩溃 | 多 agent 架构的故障隔离与恢复机制缺乏理论指导，工程实践先于研究 |

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 研究空白 |
|---------|---------|---------|
| **长上下文内存墙** | #20695 集中报告内存问题；#29941 内存压力下流崩溃 | 缺乏长序列场景的内存剖析方法论；KV cache 压缩/卸载策略未集成 |
| **流式生成鲁棒性** | #29941 ReadableStream 控制器关闭后级联失败 | 异步生成与资源回收的形式化验证缺失；无标准测试基准 |
| **视觉数据闭环** | #21227 工具图像无法展示；依赖 PR 反复修复 | 多模态工具返回的数据类型标准化（ImageContent vs FilePart）未统一 |
| **模型行为黑箱** | #29786 Opus 4.8 异常无诊断信息；#27530 级联错误 | 子代理/工具调用链的可解释性与错误归因机制空白 |
| **权限-幻觉边界模糊** | #12633 自动接受模式；#25836 bash 授权卡住 | 自动化权限与模型幻觉的交互风险未量化，缺乏安全边界研究 |

---

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

# Pi 研究动态摘要 | 2026-05-30

## 1. 今日速览

今日 Pi 代码库的核心研究信号集中在**长上下文可靠性**与**推理链稳定性**两大方向：上下文压缩（compaction）在本地模型场景下的 token 计算缺陷得到修复，同时 OpenCode/Kimi K2.6 等支持 extended reasoning 的模型因参数传递不当引发回归，显示 reasoning 参数对齐仍是多提供商生态的脆弱环节。TUI 层对 IME、图像内联、ANSI 序列的兼容性修复亦反映多模态交互基础设施的成熟度瓶颈。

---

## 2. 版本发布

**v0.78.0**（2026-05-29 发布）

| 特性 | 研究相关性 |
|:---|:---|
| **Named startup sessions** (`--name` / `-n`) | 支持会话命名化追踪，为长上下文实验的 session-level 可复现性与 A/B 对比提供基础设施 |
| **Clickable file tool paths** | 工具输出中的文件路径 OSC 8 超链接化，降低多模态/代码推理场景中的人机交互摩擦 |

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 |
|:---|:---|:---|:---|
| [#4945](https://github.com/earendil-works/pi/issues/4945) | openai-codex hang on "Working..." with zero-usage aborted turns | OPEN | **幻觉/可靠性**：模型无输出、无工具调用、无错误的"静默挂起"现象，属于典型的**生成幻觉边界案例**——系统无法区分"正在思考"与"已死锁"，对推理链监控与超时策略设计有研究意义 |
| [#5089](https://github.com/earendil-works/pi/issues/5089) | timeoutMs 超过阈值后失效 | CLOSED | **长上下文**：大文件读取场景下超时机制失效，暴露**长上下文 I/O 与推理超时耦合设计**的缺陷，对长文档处理的任务调度研究有直接关联 |
| [#4984](https://github.com/earendil-works/pi/issues/4984) | Interactive mode crash on transient terminal EPIPE | CLOSED | **可靠性**：终端管道瞬态断裂导致未捕获异常，反映**流式推理输出的容错边界**未充分覆盖 |
| [#4210](https://github.com/earendil-works/pi/issues/4210) | Bedrock empty end_turn with 0 tokens treated as successful stop | CLOSED | **幻觉缓解**：服务端返回空终止信号被误判为成功停止，属于**停止条件幻觉**——系统对"无内容"的语义解释缺乏校验机制 |
| [#5159](https://github.com/earendil-works/pi/issues/5159) | OpenRouter + Moonshot Kimi K2.6 tokenization failed | CLOSED | **多模态/推理**：K2.6 的 tokenization 参数传递失败，暴露**第三方推理提供商的 reasoning 参数对齐**问题 |
| [#5117](https://github.com/earendil-works/pi/issues/5117) | Qwen 3.7 Max "developer" role rejected | OPEN | **post-training 对齐**：`developer` 角色不被接受，反映**系统提示角色命名**在不同后训练管线中的不一致性，对系统提示注入的对齐研究有警示意义 |
| [#5169](https://github.com/earendil-works/pi/issues/5169) / [#5164](https://github.com/earendil-works/pi/issues/5164) | Kimi-K2.6 on Opencode broken (thinking modes regression) | CLOSED | **推理增强**：v0.77.0 引入的 thinking mode 参数传递导致不支持分层 reasoning 的模型崩溃，显示**自适应 reasoning 参数路由**的必要性 |
| [#5098](https://github.com/earendil-works/pi/issues/5098) | Inline images broken inside tmux | OPEN | **多模态/OCR**：tmux 环境下图像协议检测失效，**终端复用器与图像内联协议**的兼容性是多模态推理部署的已知瓶颈 |
| [#5064](https://github.com/earendil-works/pi/issues/5064) | Add Context Windows option | CLOSED | **长上下文**：用户显式请求上下文窗口大小可调，反映**长上下文资源-精度权衡**的运维需求 |
| [#5177](https://github.com/earendil-works/pi/issues/5177) | Escape/Ctrl-C 无法中断模型生成 | CLOSED | **可靠性/对齐**：模型"过度思考"时中断信号延迟响应，涉及**推理过程的人机对齐**与紧急停止机制 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|:---|:---|:---|
| [#5197](https://github.com/earendil-works/pi/pull/5197) | Guard compaction continue() on assistant-tailed context | **长上下文可靠性**：修复自动压缩后上下文以 assistant 消息结尾导致的 `Cannot continue from message role: assistant` 崩溃，解决**压缩-续接状态机**的关键边界条件 |
| [#5182](https://github.com/earendil-works/pi/pull/5182) | Use usage-reliability check for context token calculations | **长上下文/本地模型**：本地 LLM 提供商（llama.cpp/Ollama）流式返回 `prompt_tokens: 0` 导致压缩决策误判，引入 input>0 门控避免**虚假压缩触发** |
| [#5196](https://github.com/earendil-works/pi/pull/5196) | Handle OpenCode reasoning params | **推理增强**：修复 OpenCode 平台 reasoning 参数传递，支持 Kimi K2.6 等模型的**分层思考模式适配** |
| [#5183](https://github.com/earendil-works/pi/pull/5183) | Prevent stdout EPIPE from crashing process | **可靠性**：终端管道断裂的优雅降级，提升**流式推理的容错边界** |
| [#5198](https://github.com/earendil-works/pi/pull/5198) | Default showHardwareCursor to true for IME support | **多模态交互**：IME 候选窗定位修复，改善**东亚语言场景下的多模态输入体验** |
| [#5195](https://github.com/earendil-works/pi/pull/5195) | Buffer early input before prompt loop | **人机对齐**：启动阶段用户输入缓冲，消除**TUI 就绪与推理循环启动的时序竞争** |
| [#5189](https://github.com/earendil-works/pi/pull/5189) | OSC 8 hyperlinks file paths in tool titles | **多模态/代码推理**：工具输出文件路径的可点击化，降低**代码-文档交叉引用**的认知负荷 |
| [#5088](https://github.com/earendil-works/pi/pull/5088) | Collapse grouped tool calls | **推理可视化**：实验性工具调用分组折叠，为**多步推理链的可解释性**提供 UI 层支持 |
| [#5206](https://github.com/earendil-works/pi/pull/5206) | Add SambaNova as built-in provider | **推理基础设施**：新增工具能力模型支持，含上下文长度与 reasoning 标注，扩展**长上下文推理的硬件后端选择** |
| [#5178](https://github.com/earendil-works/pi/pull/5178) | Custom-header support to Bedrock provider | **post-training 对齐**：企业代理网关场景下的请求头透传，支持**对齐层的安全策略注入** |

---

## 5. 研究方向信号

| 趋势 | 证据 |
|:---|:---|
| **Reasoning 参数生态碎片化** | Kimi K2.6、Qwen 3.7 Max、OpenCode 等平台对 `thinking`/`reasoning`/`developer` 角色的差异化支持，导致同一客户端需维护多套路由逻辑（#5159, #5117, #5169, #5196） |
| **长上下文压缩的可靠性危机** | 本地模型 `prompt_tokens: 0` 的普遍性（#5182）与压缩后状态机边界条件（#5197）连续暴露，显示**上下文管理**仍是工程与研究的交叉难点 |
| **终端作为多模态推理载体的限制** | 图像协议（#5098）、IME（#5200, #5198）、ANSI 序列（#5185）、软换行 URL（#5054）等问题密集出现，终端 TUI 的**多模态渲染能力**成为推理系统部署的隐性瓶颈 |
| **"静默失败"类幻觉的检测困境** | #4945（挂起无输出）、#4210（空终止误判）、#5177（中断失效）共同指向**缺乏外部反馈时的推理状态推断**问题，与 LLM 自我验证研究直接相关 |

---

## 6. 技术局限性

| 限制领域 | 具体表现 | 研究空白 |
|:---|:---|:---|
| **流式 token 计数不可靠** | 本地/部分云端提供商返回 `prompt_tokens: 0` 或缺失 usage 字段（#5182, #4945） | 需要**不依赖 provider token 计数的上下文长度估计**方法，如基于字符/词元的轻量预测模型 |
| **Reasoning 模式缺乏统一抽象** | `thinking_budget`、`reasoning_effort`、`developer` vs `system` 等参数语义不一致（#5159, #5117, #5169） | 需要**跨提供商 reasoning 参数的标准化描述与自动适配**机制，类似 OpenRouter 的模型能力声明扩展 |
| **压缩-续接状态机脆弱** | 压缩后上下文尾部角色约束、assistant 消息截断等导致崩溃（#5197） | 需要**形式化的对话状态压缩规范**，保证压缩操作的可逆性与续接合法性 |
| **终端图像协议检测静态化** | tmux 等中间层导致 capability 检测失效（#5098） | 需要**穿透终端复用器的动态能力协商协议**，或基于回退的渐进式多模态渲染策略 |

</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

# Qwen Code 研究动态摘要 | 2026-05-30

## 1. 今日速览

今日核心信号集中在**长上下文会话管理**与**推理可靠性**两大方向：社区提出以"summary + restoration attachments"替代现有 tail-preservation compaction 的上下文压缩重构方案（#4592），同时多个 PR 针对工具调用相邻性验证（#4622）、上下文错误文本收集的健壮性（#4632）及子进程内存泄漏（#4624）进行修复，反映出对长会话稳定性与推理一致性的迫切需求。

---

## 2. 版本发布

**v0.17.0** / **v0.16.1-nightly.20260529.7bed56b9b** — 无直接研究相关更新。发布内容集中于 CLI 启动警告输出修复（stderr 前置）与 telemetry LogToSpan 桥接错误改进，属工程稳定性范畴。

---

## 3. 研究相关 Issues

| # | Issue | 研究方向 | 研究价值 |
|---|-------|---------|---------|
| [#4592](https://github.com/QwenLM/qwen-code/issues/4592) | refactor(core): replace tail-preservation compaction with claude-code-style "summary + restoration attachments" model | **长上下文推理** | 直接挑战现有按字符数分割（70%摘要+30%原文保留）的压缩范式，提出全量历史送入摘要侧查询+结构化附件恢复的替代方案，对长会话信息保留与推理连贯性有根本性改进潜力 |
| [#4624](https://github.com/QwenLM/qwen-code/issues/4624) | qwen --resume 子进程内存持续增长，最终 OOM | **长上下文/内存管理** | 暴露会话记录与工具调用结果在上下文压缩后未释放的内存泄漏机制，是长上下文系统资源管理的典型研究案例 |
| [#4619](https://github.com/QwenLM/qwen-code/issues/4619) | fix(core): validate tool_result adjacency in cleanOrphanedToolCalls to prevent Anthropic API errors | **多模态推理/工具调用可靠性** | 跨格式（OpenAI→Anthropic）转发时的消息结构完整性问题，涉及工具调用-结果配对约束的形式化验证 |
| [#4579](https://github.com/QwenLM/qwen-code/issues/4579) | fix(rewind): false "compressed turn" error when mid-turn messages exist | **长上下文/会话状态** | 工具执行期间用户插入消息导致的回合计数失配，揭示压缩状态机与交互并发的时序缺陷 |
| [#4063](https://github.com/QwenLM/qwen-code/issues/4063) | refactor: core + cli 架构 Review — 12 项结构性问题清单 | **post-training 对齐基础设施** | P0级类型系统被`@google/genai`绑架问题，136个文件硬依赖外部类型，制约模型后训练迭代时的接口灵活性与对齐实验的可扩展性 |
| [#4183](https://github.com/QwenLM/qwen-code/issues/4183) | Add opt-in heap snapshot and bounded memory timeline diagnostics | **长上下文/系统诊断** | 为长会话内存压力分析提供时序化诊断工具，支持瞬态峰值与累积泄漏的区分，是对齐训练后模型部署监控的基础设施 |
| [#4617](https://github.com/QwenLM/qwen-code/issues/4617) | feat(cli): add CPU profiling support for Chrome DevTools analysis | **推理性能/系统分析** | 推理延迟分析工具，支持生成式模型在交互场景中的计算瓶颈定位 |
| [#4554](https://github.com/QwenLM/qwen-code/issues/4554) | feat(telemetry): cover qwen serve daemon end-to-end with OpenTelemetry | **post-training 对齐/可观测性** | 守护进程全链路观测缺口，涉及推理路径、会话生命周期、桥接队列的对齐行为监控 |
| [#4372](https://github.com/QwenLM/qwen-code/issues/4372) | AUTO mode classifier blocks should emit PermissionDenied hooks | **post-training 对齐/安全分类器** | 分类器驱动的工具调用阻断缺乏可观测钩子，影响对齐后模型决策的外部审计与反馈闭环 |
| [#3456](https://github.com/QwenLM/qwen-code/issues/3456) | CJK IME composition text appears at wrong position | **OCR/多模态输入** | 终端UI中日文/中文/韩文输入法合成文本的渲染位置错误，涉及多语言输入处理的视觉反馈机制 |

---

## 4. 研究相关 PR 进展

| # | PR | 技术贡献 |
|---|-----|---------|
| [#4632](https://github.com/QwenLM/qwen-code/pull/4632) | fix(core): harden context error text collection | **幻觉缓解/健壮性**：上下文长度分类器的错误文本提取遭遇 DOMException-like 对象访问器抛出异常，通过防御性读取避免诊断辅助函数自身崩溃，提升错误恢复可靠性 |
| [#4622](https://github.com/QwenLM/qwen-code/pull/4622) | fix(core): enforce adjacent tool results | **多模态推理/工具调用一致性**：严格强制工具结果与声明的相邻性，移除被用户/助手回合分隔的孤立 tool_calls，修复跨格式 API 兼容性问题 |
| [#4587](https://github.com/QwenLM/qwen-code/pull/4587) | fix(core): remove proactive subagent system-reminder injection | **post-training 对齐/行为控制**：移除每轮对话强制注入的"主动使用 Agent 工具"系统提示，消除对子代理生成的过度偏向，保留模型自主决策空间 |
| [#4630](https://github.com/QwenLM/qwen-code/pull/4630) | feat(telemetry): add tool spans and session.id to daemon/ACP path | **可观测性/对齐监控**：为工具执行与 LLM 请求添加会话级追踪标识，支持按会话聚合的对齐行为分析 |
| [#4628](https://github.com/QwenLM/qwen-code/pull/4628) | feat(telemetry): add client_id attribute and permission route spans | **安全对齐/审计追踪**：权限投票路由的遥测覆盖，为分类器决策提供可审计的分布式追踪 |
| [#4505](https://github.com/QwenLM/qwen-code/pull/4505) | fix(core): emit enable_thinking on DashScope when reasoning is disabled | **推理控制/模型行为**：修复 qwen3 思考模式禁用的条件判断缺陷，确保`enable_thinking`正确透传，直接影响推理链的显式控制 |
| [#4107](https://github.com/QwenLM/qwen-code/pull/4107) | fix(core): parse text JSON fallback in generateJson | **推理可靠性/结构化生成**：改进 JSON 文本回退解析，保留外层对象结构、修复近似有效的无引号键候选，提升工具参数生成的鲁棒性 |
| [#4085](https://github.com/QwenLM/qwen-code/pull/4085) | feat(cli): add persistent history collapse on resume | **长上下文/交互效率**：支持恢复会话时的历史折叠持久化，减少长会话视觉噪音，优化人机协作中的上下文浏览体验 |
| [#4598](https://github.com/QwenLM/qwen-code/pull/4598) | feat(tui): collapsible thinking blocks with duration timer | **推理可解释性**：将瞬态思考预览替换为可折叠的流式推理块，附持续时间追踪，增强思维链的用户可见性与信任度 |
| [#4618](https://github.com/QwenLM/qwen-code/pull/4618) | fix(core): scope boolean coercion to boolean-typed schema fields | **工具调用可靠性/类型安全**：将布尔强制转换限制于模式声明的布尔字段，消除字符串字段被意外改写为布尔值的类型污染风险 |

---

## 5. 研究方向信号

| 趋势 | 证据 | 强度 |
|------|------|------|
| **上下文压缩范式迁移** | #4592 明确提出弃用 tail-preservation，转向 summary+attachments 模型；#4624 内存泄漏倒逼压缩机制重构 | 🔥🔥🔥 强 |
| **工具调用形式化约束** | #4619/#4622 相邻性验证、#4618 类型安全强制、#4107 JSON 解析健壮性 | 🔥🔥🔥 强 |
| **推理可控性增强** | #4505 thinking 模式显式控制、#4587 移除主动子代理偏向、#4598 思考过程可视化 | 🔥🔥🔥 强 |
| **对齐行为可观测性** | #4554/#4630/#4628 守护进程全链路追踪、#4372 分类器决策钩子 | 🔥🔥 中 |
| **长会话资源管理** | #4624 OOM、#4183 堆诊断、#4617 CPU 剖析 | 🔥🔥 中 |
| **多语言输入处理** | #3456 CJK IME 位置错误（孤立信号，未见跟进） | 🔥 弱 |

---

## 6. 技术局限性

1. **上下文压缩的语义损失与资源泄漏并存**：现有按字符数分割的压缩策略被质疑为"粗暴"（#4592），且实现层面存在压缩后数据未释放导致的内存无限增长（#4624），表明压缩状态机缺乏形式化的生命周期管理。

2. **跨格式工具调用的结构脆弱性**：OpenAI 格式向 Anthropic 格式转发时，tool_result/tool_use 的相邻性约束易被异步交互破坏（#4619），反映多模态推理管道中消息拓扑验证的缺失。

3. **系统提示的隐性行为偏向**：每轮注入的主动子代理提示（#4587）构成隐性的 post-training 干预，其移除后的模型行为漂移缺乏量化评估框架。

4. **类型系统的外部依赖锁定**：core 层 136 个文件硬编码 `@google/genai` 类型（#4063），制约后训练对齐实验中模型接口的快速迭代与 A/B 测试能力。

5. **分类器决策的不可解释性**：AUTO 模式的权限分类器阻断路径无钩子事件（#4372），形成安全对齐中的"黑箱拒绝"，阻碍对抗样本分析与 red-teaming。

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

# DeepSeek TUI 研究动态摘要 | 2026-05-30

## 1. 今日速览

今日社区活跃度高，**Agent 模式下的工具调用可靠性**与**长上下文推理的稳定性**成为核心议题。多个 Issue 暴露本地模型在 tool use 上的格式遵循失败问题，同时 PR 侧出现针对 sub-agent 失败控制、prompt 宪法文本可覆盖性的对齐层改进，显示项目正从"功能可用"向"推理可控"演进。

---

## 2. 版本发布

无新版本发布。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 | 链接 |
|---|------|---------|------|
| **#2361** | 本地 LLM 输出 JSON 而非执行 tool | **多模态/工具学习对齐**：本地模型（可能为较小参数模型或量化版本）在代码分析任务中未能正确触发工具调用，而是将 tool schema 以 JSON 文本输出。这揭示了**post-training 对齐不足**或**指令跟随格式偏移**问题，对研究"如何让本地/边缘模型可靠遵循 tool-use 协议"有直接案例价值。 | [Issue #2361](https://github.com/Hmbown/CodeWhale/issues/2361) |
| **#2346** | 模式切换时 Agent 对模式变化无感知 | **长上下文推理/状态一致性**：Agent 在 Tab 切换模式后仍基于旧模式上下文继续推理，产生大量无效 token 消耗和 workaround 尝试。这是**长对话中的上下文漂移（context drift）**与**元认知缺失**的典型表现，对研究"如何让模型感知对话阶段转换"有启发。 | [Issue #2346](https://github.com/Hmbown/CodeWhale/issues/2346) |
| **#2328** | `exec_shell` 模式可用性不一致 | **工具调用可靠性/幻觉缓解**：同一工具在 YOLO 模式可用、Agent 模式被拦截，文档未声明此限制。属于**系统-模型能力不匹配导致的幻觉性失败**（用户预期工具可用，系统实际拒绝），对研究"工具可用性的统一表征与模型告知机制"有意义。 | [Issue #2328](https://github.com/Hmbown/CodeWhale/issues/2328) |
| **#2353** | `config.toml` 开启记忆功能无效 | **长上下文/记忆机制**：用户配置记忆功能后未生效，涉及**持久化记忆的状态管理与配置解析可靠性**。对研究"外部记忆系统的工程实现与模型侧记忆调用的对齐"有参考价值。 | [Issue #2353](https://github.com/Hmbown/CodeWhale/issues/2353) |
| **#2362** | Sub-agents 无法访问 MCP 工具 | **多 Agent 协作/工具权限传递**：`agent_open` 创建的子 Agent 丢失父会话的 MCP 工具上下文，属于**多 Agent 架构中的工具可见性隔离问题**。对研究"hierarchical agent 系统的工具继承与权限边界"有直接关联。 | [Issue #2362](https://github.com/Hmbown/CodeWhale/issues/2362) |
| **#2339** | `tool_search` 默认 `max_results=5` 埋没跨服务器工具 | **工具检索/长上下文**：低默认结果数导致多 MCP 服务器场景下的工具发现失败，属于**检索增强生成（RAG）中召回率与精度的权衡问题**。对研究"大规模工具库的高效检索与排序"有实践意义。 | [Issue #2339](https://github.com/Hmbown/CodeWhale/issues/2339) |
| **#2348** | 希望折叠 thinking 输出 | **推理可视化/用户体验**：DeepSeek-R1 类模型的 thinking 过程过长干扰阅读，需求指向**推理过程的可控展示与信息层级管理**。对研究"如何向终端用户呈现链式思维（CoT）"有产品设计层面的研究价值。 | [Issue #2348](https://github.com/Hmbown/CodeWhale/issues/2348) |
| **#2359** | `COMPLETIONS_WALK_DEPTH` 硬编码限制文件发现深度 | **长上下文/代码理解**：6 层目录深度限制可能截断大型代码库的文件索引，影响**基于项目上下文的代码推理质量**。对研究"代码库表示的层级截断与检索策略"有工程参考意义。 | [Issue #2359](https://github.com/Hmbown/CodeWhale/issues/2359) |
| **#2365** | Stream timeout 配置需求（DS4 Pro 本地慢推理） | **长上下文推理效率**：本地大模型（DS4 Pro on Mac Studio）推理超时，暴露**推理延迟与用户体验的冲突**。对研究"流式生成的自适应超时策略"或"推理加速"有场景驱动价值。 | [Issue #2365](https://github.com/Hmbown/CodeWhale/issues/2365) |
| **#2337/#2335** | 支持 GLM-5/Qwen 等非 DeepSeek 模型 | **模型无关对齐/后训练泛化**：社区对第三方模型的适配需求，涉及**不同基础模型的 post-training 对齐差异**（如 tool-use 格式、reasoning 风格）。对研究"对齐方法的跨模型迁移性"有需求验证价值。 | [Issue #2337](https://github.com/Hmbown/CodeWhale/issues/2337) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 | 链接 |
|---|------|---------|------|
| **#2356** | 允许 embedder 通过 `OnceLock` hooks 覆盖宪法提示文本 | **Post-training 对齐/宪法 AI**：首次提供**不 fork 代码即可替换 BASE_PROMPT、LOCALE_PREAMBLE、AUTHORITY_RECAP** 的机制。这是**可配置的对齐层（configurable constitutional layer）**，使下游研究者可注入自定义价值观约束或领域特定规范，对宪法 AI 的实验与部署有关键意义。 | [PR #2356](https://github.com/Hmbown/CodeWhale/pull/2356) |
| **#2354** | Sub-agent 通用 intro 添加失败停止与有限努力指导 | **幻觉缓解/Agent 可靠性**：在 `GENERAL_AGENT_INTRO` 中显式加入"何时停止"的指令，针对**低能力模型的重复失败循环（failure loop）**问题。属于**通过 prompt engineering 实现的自我纠错（self-correction）引导**，对研究"bounded effort agent"有方法论价值。 | [PR #2354](https://github.com/Hmbown/CodeWhale/pull/2354) |
| **#2336** | `/cache stats` 前缀哈希/漂移暴露与缓存命中摘要 | **长上下文推理/前缀缓存**：提供**前缀缓存稳定性诊断工具**，暴露 SHA-256 指纹、漂移警告、KV 缓存命中率。这对研究"长上下文中的前缀复用效率"和"上下文漂移检测"提供了可观测性基础设施。 | [PR #2336](https://github.com/Hmbown/CodeWhale/pull/2336) |
| **#2338** | `whale-size` 路由分类法：模型+思考 effort 选择器 | **推理控制/用户体验**：将 `(model, reasoning_effort)` 映射为鲸类物种标签（从最大/最深到最小/最快），建立**推理成本的认知模型**。对研究"如何让终端用户直观理解推理深度-延迟-成本的权衡"有交互设计层面的贡献。 | [PR #2338](https://github.com/Hmbown/CodeWhale/pull/2338) |
| **#2344** | 提升 tool search 默认结果数至 20 | **工具检索/召回优化**：将 regex/BM25 工具发现的默认上限从 5 提升至 20，并暴露 `max_results` 参数（上限 100）。直接改善**多 MCP 服务器场景下的工具召回率**，对研究"工具检索的 top-k 选择策略"有实证价值。 | [PR #2344](https://github.com/Hmbown/CodeWhale/pull/2344) |
| **#2357** | 修复 MCP stdio 关闭时的嵌套 runtime panic | **多模态工具链可靠性**：解决 `serve --mcp` 在 stdin 关闭时的 Tokio runtime panic，属于**异步运行时与外部进程生命周期的对齐问题**。对研究"MCP 服务器的健壮接入"有工程稳定性贡献。 | [PR #2357](https://github.com/Hmbown/CodeWhale/pull/2357) |
| **#2355** | `fetch_url` 可选信任 fake-ip 占位范围 | **SSRF 安全/多模态输入**：在透明代理/TUN 的 fake-ip 模式下避免 DNS SSRF 防护的误杀。涉及**网络层安全策略与多模态输入获取的冲突解决**，对研究"安全约束下的外部资源获取"有边界案例价值。 | [PR #2355](https://github.com/Hmbown/CodeWhale/pull/2355) |
| **#2318** | `message_submit` hooks 允许转换提交文本 | **输入对齐/预处理**：支持 hook 通过 stdout JSON 替换用户提交文本或阻断提交（exit code 2）。这是**用户输入的对齐预处理层**，可用于研究"实时输入过滤、提示注入防御或格式规范化"的实验。 | [PR #2318](https://github.com/Hmbown/CodeWhale/pull/2318) |
| **#2330** | IME 中文输入直达 composer 而非 paste-burst buffer | **多语言/OCR 输入可靠性**：修复无 bracketed paste 终端上中文 IME 提交被错误路由的问题。对**CJK 输入法的终端交互正确性**有贡献，间接支持多语言场景下的代码/文本输入可靠性。 | [PR #2330](https://github.com/Hmbown/CodeWhale/pull/2330) |
| **#2274** | Provider registry drift check | **模型生态对齐/配置一致性**：自动化校验文档、配置、注册表、默认模型字符串的一致性。对研究"多模型生态的配置漂移检测"提供 CI 层面的方法论。 | [PR #2274](https://github.com/Hmbown/CodeWhale/pull/2274) |

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|------|------|---------|
| **本地模型 Tool-use 对齐缺口** | #2361（JSON 输出替代 tool 执行）、#2337/2335（GLM-5/Qwen 适配需求） | 社区正将 DeepSeek-TUI 用于非官方模型，但**SFT/RLHF 后的 tool 格式遵循能力参差不齐**。需要研究"轻量级 tool-use 对齐微调"或"运行时格式适配层"。 |
| **Agent 状态感知与元认知** | #2346（模式切换无感知）、#2328（工具可用性不一致） | 当前 Agent 缺乏**对系统状态变化的显式认知**，导致推理-执行脱节。需要研究"对话阶段检测"或"系统状态注入 prompt"的动态机制。 |
| **Sub-agent 架构的权限与工具继承** | #2362（MCP 工具丢失）、#2354（失败停止指导） | 多 Agent 系统的**工具可见性边界**和**错误恢复策略**尚未成熟。需要研究"hierarchical agent 的权限模型"和"跨 Agent 上下文传递协议"。 |
| **长上下文效率与可观测性** | #2336（缓存统计）、#2365（本地慢推理超时）、#2359（目录深度限制） | 前缀缓存、流式超时、文件索引深度均指向**长上下文工程化的系统性挑战**。需要研究"自适应上下文截断"与"推理-检索联合优化"。 |
| **宪法提示的可配置化** | #2356（`OnceLock` hooks 覆盖宪法文本） | 社区需求从"固定对齐"转向**可插拔价值观层**，与 Constitutional AI、RLHF 的可定制方向一致。 |

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 研究空白 |
|---------|---------|---------|
| **本地模型的 Tool-use 格式偏移** | 非 DeepSeek 官方模型常输出 JSON 文本而非触发工具调用（#2361） | 缺乏**模型无关的 tool-use 格式规范化层**或**轻量级运行时适配器** |
| **Agent 上下文状态同步失败** | 模式切换、工具可用性变化无法被 Agent 实时感知（#2346, #2328） | 缺乏**系统状态到模型上下文的显式注入机制**（如 system message 动态更新协议） |
| **Sub-agent 工具上下文隔离** | 子 Agent 无法继承父会话的 MCP 工具（#2362） | 缺乏**多 Agent 工具权限的继承/委托模型**规范 |
| **推理过程的可控展示** | Thinking 输出过长且不可折叠（#2348） | 缺乏**链式思维的结构化分段与交互式展开**标准 |
| **长上下文索引截断** | 硬编码的目录深度、文件数量限制（#2359, #2360） | 缺乏**基于项目语义的自适应索引深度**算法 |
| **流式推理的超时刚性** | 固定 300s 超时无法适应本地大模型慢推理（#2365） | 缺乏**推理进度感知的自适应超时**策略 |

---

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*