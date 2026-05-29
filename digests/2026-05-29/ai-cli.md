# AI CLI 工具社区动态日报 2026-05-29

> 生成时间: 2026-05-29 00:34 UTC | 覆盖工具: 9 个

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

# AI CLI 工具生态横向对比分析报告 | 2026-05-29

---

## 1. 生态全景

当前 AI CLI 工具生态正从"功能竞赛"转向"可靠性攻坚"阶段。长上下文（1M tokens）已成为头部产品的标配，但**有效上下文利用率**与**会话状态一致性**成为共性瓶颈——Claude Code、Copilot CLI、Pi 均暴露严重的 thinking block / message ID 冲突问题。多 Agent 编排从概念走向产品（Claude Code dynamic workflows、Kimi 并行 subagent），但超时控制、状态同步等基础机制仍不成熟。推理可控性（reasoning effort 调节、adaptive thinking）成为差异化焦点，却伴随 UI 架构退化与参数兼容性的新矛盾。

---

## 2. 各工具活跃度对比

| 工具 | 今日 Issues | 今日 PRs | 版本发布 | 核心动态 |
|:---|:---|:---|:---|:---|
| **Claude Code** | 11 个研究相关（#10199 集群集中爆发） | 4 个（2 open, 2 closed） | **v2.1.154** | Opus 4.8 默认 high effort + dynamic workflows；thinking block 400 错误大规模爆发 |
| **OpenAI Codex** | 9 个研究相关 | 10+ 个（多组系列 PR） | **rust-v0.135.0** | 结构化上下文保留提案、内部上下文片段 goal steering、统一 exec sandbox |
| **Gemini CLI** | 9 个研究相关 | 8 个 | v0.45.0-preview.1（低相关性） | AST 感知工具链调研、行为评估扩展至 76 例、组件级 eval 体系 |
| **Copilot CLI** | 10 个研究相关 | **0 个** | v1.0.56-0 / v1.0.55 | contextTier 持久化修复、reasoning tokens 报告上线；重复 fc_call ID 错误集群爆发 |
| **Kimi CLI** | 4 个研究相关 | 9 个 | 无（#2391 推进 v1.46.0） | 大 context ConnectTimeout、orphan tool_calls 修复、undo/context 索引对齐 |
| **OpenCode** | 10 个研究相关 | 10 个 | **v1.15.12** | adaptive reasoning controls 修复启用；DeepSeek V4 reasoning_content 断裂、V2 UI 可控性退化 |
| **Pi** | 10 个研究相关 | 10+ 个 | **v0.77.0** | GPT-5.5 1M→272K 截断修复、reasoning_details 时序缓冲、跨模型会话恢复冲突 |
| **Qwen Code** | 10 个研究相关 | 10 个 | v0.16.1-nightly（低相关性） | 全历史摘要+恢复附件重构、thinking 瞬态化、daemon 遥测补全 |
| **DeepSeek TUI** | 9 个研究相关 | 10 个 | 无 | 多模型/OCR/视觉需求、18分钟阻塞、IME 中文输入修复、工具预加载 |

> **活跃度排序**（按研究相关 Issue + PR 总量）：Claude Code ≈ OpenAI Codex ≈ Pi ≈ Qwen Code ≈ OpenCode > Gemini CLI ≈ Copilot CLI ≈ DeepSeek TUI > Kimi CLI

---

## 3. 共同关注的功能方向

| 共同方向 | 涉及工具 | 具体诉求 |
|:---|:---|:---|
| **长上下文可靠性** | **全部 9 个工具** | Claude Code: thinking block 不可变性与会话恢复冲突；Copilot CLI: contextTier 回退 200K；Pi: 1M→272K 截断；Kimi: 120k+ timeout；Qwen: body timeout 300s；OpenCode: 6KB 文件静默失败 |
| **推理可控性/透明度** | Claude Code, OpenCode, Pi, Copilot CLI, Qwen Code | Claude Code: `/effort xhigh`；OpenCode: adaptive reasoning controls + V2 UI 隐藏 selector；Pi: reasoning_details 缓冲；Qwen: thinking 瞬态化配置；Copilot: reasoning tokens 报告 |
| **会话状态一致性** | Claude Code, OpenAI Codex, Kimi, Pi, Qwen Code | Claude Code: bridge/remote-control 重放；Codex: 重启后历史丢失；Kimi: orphan tool_calls / wire-context 索引错位；Pi: 跨模型恢复 ID 冲突；Qwen: 压缩后回退映射 |
| **多 Agent 协调** | Claude Code, OpenAI Codex, Kimi, Gemini CLI | Claude Code: "tens to hundreds of agents" dynamic workflows；Codex: 7.5h wait_agent 阻塞；Kimi: 并行 subagent API key pool；Gemini: 子 Agent 虚假成功报告 |
| **工具调用确定性** | Kimi, DeepSeek TUI, Gemini CLI, Claude Code | Kimi: tool_calls 状态透传；DeepSeek: 模式不一致 + 安全绕过；Gemini: 128+ 工具硬限制；Claude Code: interleaved thinking + tool use 竞争 |
| **多模态/OCR 基础设施** | DeepSeek TUI, Gemini CLI, OpenCode, Kimi | DeepSeek TUI: 视觉/OCR/向量多模型路由；Gemini CLI: AST 感知代码理解（隐含视觉-结构映射）；OpenCode: https 图像 URI 过滤修复；Kimi: 图像格式转换 |

---

## 4. 差异化定位分析

| 工具 | 功能侧重 | 目标用户 | 技术路线特征 |
|:---|:---|:---|:---|
| **Claude Code** | 企业级 multi-agent 编排、extended thinking 深度推理 | 专业开发者、企业团队 | **闭源模型绑定**（Anthropic 全家桶），API 层与应用层深度耦合；thinking block 不可变性设计哲学与工程实践冲突 |
| **OpenAI Codex** | 结构化上下文保留、云-端配置一致性、安全沙箱 | 云原生开发者、大型组织 | **Rust 核心 + 云配置分发**，强调运行时模型行为控制；internal context fragments 隐式引导标准化 |
| **Gemini CLI** | 评估驱动迭代、AST 感知代码理解、组件级行为 eval | 研究型用户、Google 生态 | **评估基础设施优先**，76 行为 eval + bleed 消除；代码语义结构化而非文本线性扫描 |
| **Copilot CLI** | IDE 深度集成、模型能力分层（Pro/Free/Student）、经济约束下的推理分配 | VS Code/Copilot 现有用户 | **产品策略强约束**（200K cap vs 1M 模型能力），成本乘数守卫优先于用户显式选择 |
| **Kimi CLI** | 长上下文稳定性、ACP 协议标准化、并行 subagent 扩展 | 长文档/代码库分析用户 | **自研 ACP 协议**，强调会话可恢复性与跨会话连续性；API key pool 支撑横向扩展 |
| **OpenCode** | 多提供商统一、推理可控性、V2 UI 现代化 | 多模型切换的高级用户 | **提供商抽象层**最厚，adaptive reasoning 跨模型适配；V2 UI 架构与推理透明度存在张力 |
| **Pi** | 跨提供商会话互操作、流式推理时序精确性、工具调用透明度 | 多模型并用的极客用户 | **去中心化模型路由**，OpenRouter + 多提供商原生支持；reasoning_details 缓冲机制精细 |
| **Qwen Code** | 全历史语义压缩、daemon 模式异步化、内置 Computer Use | 中文开发者、阿里生态 | **Claude Code 风格压缩重构**，summary + restoration attachments 替代尾保留；热重载支持快速迭代 |
| **DeepSeek TUI** | 多语言输入（CJK）、本地部署兼容、工具目录确定性 | 中文用户、本地模型部署者 | **终端原生 TUI**，IME 层深度优化；单 provider 架构向多模型路由演进中 |

---

## 5. 社区热度与成熟度

### 高活跃度 · 快速迭代期
| 工具 | 证据 | 成熟度判断 |
|:---|:---|:---|
| **Claude Code** | v2.1.154 发布即引发 11 个关联 Issue 集群，multi-agent 功能透明度低 | **功能激进，可靠性承压**；extended thinking 架构债务集中暴露 |
| **OpenCode** | v1.15.12 修复 adaptive reasoning，同时 V2 UI 退化引发可控性危机 | **产品重构期**，新旧架构交替中的一致性风险 |
| **Pi** | v0.77.0 + 10 Issue/10 PR，跨模型兼容修复密集 | **生态适配期**，多提供商抽象层的边际成本递增 |
| **Qwen Code** | 压缩范式重构（#4592/#4599）、daemon 遥测补全、Computer Use 内置 | **架构升级期**，向长上下文+多模态 Agent 跃迁 |

### 中活跃度 · 稳定优化期
| 工具 | 证据 | 成熟度判断 |
|:---|:---|:---|
| **OpenAI Codex** | rust-v0.135.0 结构化改进，但无重大架构变更；#24810 长上下文提案待响应 | **平台巩固期**，云配置与沙箱体系成熟，社区提案驱动演进 |
| **Gemini CLI** | 评估体系扩展（76→更多）、AST 工具链调研，版本发布低频 | **研究导向期**，工程节奏保守，评估基础设施领先 |
| **DeepSeek TUI** | 无版本发布但 PR 活跃（10 个），多语言/工具确定性基础加固 | **基础夯实期**，核心体验（输入、编码、工具）优先于高级功能 |

### 相对低活跃度 · 瓶颈期
| 工具 | 证据 | 成熟度判断 |
|:---|:---|:---|
| **Copilot CLI** | 今日 **0 PR**，重复 fc_call ID 错误集群爆发未获工程响应；模型 cap 张力持续 | **产品僵化期**，微软-OpenAI 协作架构下的迭代自由度受限 |
| **Kimi CLI** | 4 Issue/9 PR，聚焦修复而非新功能；无版本发布 | **收敛期**，ACP 协议标准化后的功能补全阶段 |

---

## 6. 值得关注的趋势信号

| 趋势信号 | 数据支撑 | 对开发者的参考价值 |
|:---|:---|:---|
| **🔴 "1M 上下文"名义化危机** | Copilot CLI 200K cap、Pi 272K 错误截断、Claude Code auto-compact 失效 | **不要轻信标称上下文长度**。评估工具时需测试实际可用预算，关注系统提示开销占比（Copilot CLI 已达 73%）。长上下文任务的可靠性仍高度依赖工程实现。 |
| **🔴 Thinking/Reasoning 块成为新故障域** | Claude Code 11 个 thinking block 关联 Issue、DeepSeek V4 reasoning_content 丢失、Pi reasoning_details 时序缓冲 | **推理可追溯性是幻觉检测的前提**。选择工具时验证：① reasoning 内容是否持久化 ② 跨会话/跨模型时是否保留 ③ 流式传输中是否可能丢失。 |
| **🟡 多 Agent 从"能用"到"可靠"差距巨大** | Claude Code "tens to hundreds of agents" 无技术细节、Codex 7.5h 阻塞、Gemini 子 Agent 虚假成功 | **谨慎投入生产级 multi-agent 工作流**。当前超时控制、状态同步、诚实性保障均不成熟。优先验证单 Agent 长会话可靠性再扩展。 |
| **🟡 上下文压缩范式迁移：尾保留 → 语义摘要** | Qwen Code #4592/#4599 全历史摘要+恢复附件、Codex #24810 结构化保留提案 | **关注压缩策略的语义完整性**。传统滑动窗口/尾保留在长程依赖场景下失效，需评估工具的压缩机制是否保留关键决策节点与依赖关系。 |
| **🟢 评估基础设施成为差异化壁垒** | Gemini CLI 76 行为 eval、Qwen Code daemon 遥测补全、Claude Code 缺乏公开 eval | **优先选择评估透明的工具**。社区驱动的行为评估（behavioral evals）比厂商声明更可信，尤其关注"bleed"消除与对抗性测试覆盖。 |
| **🟢 CJK/多语言输入从"边缘"到"基础设施"** | DeepSeek TUI #2330 IME 修复、#2323 中文输入、Kimi CLI 无相关 Issue（已解决？） | **中文开发者应重点测试输入层可靠性**。IME 路由、编码检测、终端能力协商（bracketed paste）仍是多数工具的隐性缺陷。 |

---

*报告生成时间：2026-05-29 | 数据覆盖：9 个主流 AI CLI 工具仓库*

---

## 各工具详细报告

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills 社区热点

> 数据来源: [anthropics/skills](https://github.com/anthropics/skills)

# Claude Code Skills 社区热点报告（截至 2026-05-29）

---

## 1. 热门 Skills 排行（按社区活跃度）

| 排名 | Skill | 功能 | 讨论热点 | 状态 |
|:---|:---|:---|:---|:---|
| 1 | **[document-typography](https://github.com/anthropics/skills/pull/514)** | AI生成文档的排版质量控制：防止孤行、寡行、编号错位等排版问题 | 触及Claude生成文档的普适痛点；作者指出"用户很少主动要求好排版，但问题无处不在" | OPEN |
| 2 | **[ODT skill](https://github.com/anthropics/skills/pull/486)** | OpenDocument格式（.odt/.ods）的创建、模板填充与HTML转换 | 开源标准格式支持 vs 商业格式生态；企业合规场景需求 | OPEN |
| 3 | **[frontend-design](https://github.com/anthropics/skills/pull/210)** | 前端设计技能清晰度与可执行性改进 | Skill指令的"可执行性"边界：如何在单轮对话中给出可落地的设计指导 | OPEN |
| 4 | **[skill-quality-analyzer / skill-security-analyzer](https://github.com/anthropics/skills/pull/83)** | Skill元分析工具：质量五维评估 + 安全审计 | 元Skill（meta-skill）的方法论：社区开始关注Skill本身的工程化标准 | OPEN |
| 5 | **[SAP-RPT-1-OSS predictor](https://github.com/anthropics/skills/pull/181)** | SAP开源表格基础模型的预测分析集成 | 企业ERP数据+开源模型的垂直场景；Apache 2.0许可的合规性 | OPEN |
| 6 | **[AURELION skill suite](https://github.com/anthropics/skills/pull/444)** | 四层认知框架：结构化思维模板、顾问模式、智能体、记忆系统 | AI协作的认知架构设计；专业知识管理的持久化上下文 | OPEN |
| 7 | **[testing-patterns](https://github.com/anthropics/skills/pull/723)** | 全栈测试体系：测试哲学、单元测试、React组件测试、集成/E2E | Testing Trophy模型的实践落地；"测什么/不测什么"的决策边界 | OPEN |
| 8 | **[shodh-memory](https://github.com/anthropics/skills/pull/154)** | AI智能体的持久化记忆系统，跨会话维持上下文 | proactive_context的调用时机；记忆结构化与检索效率 | OPEN |

---

## 2. 社区需求趋势（Issues 提炼）

| 方向 | 代表 Issue | 核心诉求 |
|:---|:---|:---|
| **企业级协作与治理** | [#228](https://github.com/anthropics/skills/issues/228) 组织级Skill共享 | 从个人工具→团队知识库：共享库、直链分发、权限管控 |
| **安全与信任边界** | [#492](https://github.com/anthropics/skills/issues/492) 命名空间仿冒 | `anthropic/` 命名空间的社区Skill导致信任滥用，需官方签名或隔离机制 |
| **Agent治理与对齐** | [#412](https://github.com/anthropics/skills/issues/412) agent-governance | 政策执行、威胁检测、信任评分、审计追踪——AI系统的安全护栏Skill化 |
| **MCP协议互通** | [#16](https://github.com/anthropics/skills/issues/16) Skills as MCPs | Skill与MCP的双向转化：算法艺术Skill → `generateAlgorithmArt()` API |
| **长上下文/数据压缩** | [#1102](https://github.com/anthropics/skills/issues/1102) MCP数据过载 | 数据库类MCP返回巨量数据时的上下文拥堵，需工程化压缩方案 |
| **文档处理安全** | [#1175](https://github.com/anthropics/skills/issues/1175) SharePoint文档权限 | 在SKILL.md中内嵌访问控制逻辑的上下文窗口与安全风险权衡 |
| **跨平台部署** | [#29](https://github.com/anthropics/skills/issues/29) AWS Bedrock兼容 | 从Claude生态向第三方推理平台的Skill迁移 |

---

## 3. 高潜力待合并 Skills（评论活跃 + 近期更新）

| Skill | PR | 活跃度信号 | 落地概率评估 |
|:---|:---|:---|:---|
| **document-typography** | [#514](https://github.com/anthropics/skills/pull/514) | 触及所有文档生成场景的通用痛点；作者持续迭代 | ⭐⭐⭐⭐⭐ 高——问题普适，实现轻量 |
| **ODT skill** | [#486](https://github.com/anthropics/skills/pull/486) | 开源标准合规需求；4月仍有更新 | ⭐⭐⭐⭐☆ 中高——企业采购场景驱动 |
| **testing-patterns** | [#723](https://github.com/anthropics/skills/pull/723) | 全栈覆盖完整；4月持续优化 | ⭐⭐⭐⭐☆ 中高——开发者工具链刚需 |
| **AURELION suite** | [#444](https://github.com/anthropics/skills/pull/444) | 认知框架方法论；5月仍在更新 | ⭐⭐⭐⭐☆ 中高——Agent记忆层基础设施 |
| **skill-quality-analyzer** | [#83](https://github.com/anthropics/skills/pull/83) | 元Skill方法论；质量量化评估 | ⭐⭐⭐☆☆ 中等——需官方标准背书 |
| **ServiceNow platform** | [#568](https://github.com/anthropics/skills/pull/568) | 企业ITSM全模块覆盖；垂直场景深 | ⭐⭐⭐☆☆ 中等——受众垂直但企业付费意愿强 |

**技术债修复类**（高合并优先级）：
- [#538](https://github.com/anthropics/skills/pull/538) PDF大小写引用修复、[#539](https://github.com/anthropics/skills/pull/539) YAML特殊字符校验、[#541](https://github.com/anthropics/skills/pull/541) DOCX书签ID冲突——Lubrsy706 集中提交的文档Skill稳定性修复，技术债务低、合并阻力小。

---

## 4. Skills 生态洞察

> **当前社区最集中的诉求：从"功能工具"向"可信基础设施"跃迁——企业级治理（命名空间安全、组织共享、权限管控）、Agent认知架构（持久记忆、结构化推理、安全护栏）、以及跨平台互操作性（MCP协议、Bedrock兼容）正成为Skill生态成熟度的核心度量，而文档/排版/测试等"传统"开发效率工具仍在持续夯实基础层。**

---

*报告基于 anthropic/skills 仓库公开数据生成，截止 2026-05-29*

---

# Claude Code 研究动态摘要 | 2026-05-29

## 今日速览

今日 Claude Code 2.1.154 发布，核心变化为 Opus 4.8 默认启用 high effort 模式及动态工作流（multi-agent 编排），但引发大规模 **"thinking blocks cannot be modified"** 400 错误——涉及 extended thinking 会话恢复、bridge/remote-control 重放及异步工具回调等场景，暴露长上下文推理链的 transcript 状态管理缺陷。同时，1M 上下文默认开启、auto-compact 未触发等议题持续发酵，反映长上下文可靠性仍是关键瓶颈。

---

## 版本发布

**v2.1.154** ([Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.154))
- Opus 4.8 默认 high effort，`/effort xhigh` 支持极限任务
- **动态工作流（dynamic workflows）**：用户可要求 Claude 创建跨数十至数百 agent 的后台编排工作流——属于 **multi-agent 长上下文协调** 研究方向，但实现细节未公开

**v2.1.153** ([Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.153))
- 纯工程维护（Git LFS、npm 更新提示、`COLUMNS` 环境变量），无直接研究关联

---

## 研究相关 Issues

| # | 标题 | 状态 | 研究价值 |
|---|------|------|---------|
| [#10199](https://github.com/anthropics/claude-code/issues/10199) | API Error 400 - Thinking Block Modification Error | OPEN | **核心研究议题**：extended thinking 的 thinking/redacted_thinking blocks 在消息序列中被修改时触发 API 400，涉及推理链的不可变性与会话恢复机制设计 |
| [#63147](https://github.com/anthropics/claude-code/issues/63147) | Resuming extended-thinking session fails permanently with 400 "thinking blocks cannot be modified" | OPEN | **长上下文推理可靠性**：transcript 存储 thinking text 为空但保留 signature，导致会话永久损坏——揭示 thinking block 的序列化/反序列化与验证逻辑缺陷 |
| [#63394](https://github.com/anthropics/claude-code/issues/63394) | 2.1.154 regression: bridge/remote-control session replay re-sends persisted (empty-text, signed) thinking blocks | OPEN | **分布式长上下文推理**：cloud bridge/remote control 场景下持久化 thinking blocks 的重放机制与 API 约束冲突，涉及跨设备会话状态同步 |
| [#63322](https://github.com/anthropics/claude-code/issues/63322) | Regression (2.1.147–2.1.150?): resuming extended-thinking session after CC update/model-switch → unrecoverable 400 | OPEN | **模型切换与推理连续性**：版本更新或模型切换后 extended thinking 会话恢复失败，指向推理状态与模型版本耦合问题 |
| [#30492](https://github.com/anthropics/claude-code/issues/30492) | Real-time steering: priority message channel for redirecting Claude mid-execution | OPEN | **推理干预与对齐**：多步工作流中的实时转向机制，涉及 **inference-time steering** 和 **human-in-the-loop 对齐**，对长任务的可控性至关重要 |
| [#62063](https://github.com/anthropics/claude-code/issues/62063) | Claude Code defaults to 1M context on fresh session with no workaround on Pro plan | OPEN | **长上下文资源管理**：1M 上下文默认启用且无法降级，引发成本与性能权衡争议，涉及上下文窗口的自适应策略 |
| [#63426](https://github.com/anthropics/claude-code/issues/63426) | Context window fills quickly and auto-compact not triggering at 80% threshold | OPEN | **长上下文压缩机制**：auto-compact 阈值触发失效，Sonnet/Opus 上下文消耗异常加速，指向 **上下文摘要/压缩算法** 的可靠性问题 |
| [#63221](https://github.com/anthropics/claude-code/issues/63221) | Anthropic API Error: Cannot modify thinking blocks in assistant message | OPEN | 同 #10199 集群，具体场景涉及 interleaved thinking + tool use 的交互模式 |
| [#63393](https://github.com/anthropics/claude-code/issues/63393) | 400 'thinking blocks cannot be modified' when run_in_background tool completes (interleaved thinking + Opus 1M) | OPEN | **异步推理与工具调用**：`run_in_background` 任务完成时注入异步结果与 interleaved thinking 冲突，涉及 **并发推理状态管理** |
| [#61056](https://github.com/anthropics/claude-code/issues/61056) | API Error: request triggered cyber-related safeguards | OPEN | **幻觉缓解与安全防护**：cyber-related safeguards 的误触发问题，涉及 **过度拒绝（over-refusal）** 与 **安全-能力权衡** 的后训练对齐挑战 |

---

## 研究相关 PR 进展

| # | 标题 | 状态 | 技术贡献 |
|---|------|------|---------|
| [#62941](https://github.com/anthropics/claude-code/pull/62941) | fix(ralph-wiggum): correctly read last assistant text from transcript | OPEN | **推理链解析可靠性**：修复 stop hook 仅读取 transcript 最后一行导致无法正确提取 assistant text blocks 的问题——涉及多模态内容块（thinking/text/tool_use）的序列化解析，对 **长上下文 transcript 的结构化处理** 有参考价值 |
| [#63262](https://github.com/anthropics/claude-code/pull/63262) / [#63252](https://github.com/anthropics/claude-code/pull/63252) | feat: add side-threads plugin (/thread and /back) | CLOSED | **对话状态管理与推理分支**：Slack 风格线程化对话模式，支持主对话与侧线程的上下文切换——属于 **多分支推理与上下文隔离** 的轻量级实现，对长对话的注意力管理有启发 |
| [#63382](https://github.com/anthropics/claude-code/pull/63382) | Fix Hookify tests example semantics | OPEN | **评估与对齐**：修正 hook 机制的语义测试，涉及基于 substring 的断言与行为契约验证，对 **后训练评估基础设施** 有边际贡献 |
| [#63189](https://github.com/anthropics/claude-code/pull/63189) | Use PR template in /commit-push-pr command | OPEN | 工程自动化，无直接研究关联 |

---

## 研究方向信号

1. **Extended Thinking 的工程-研究张力**：thinking blocks 的不可变性设计（API 层）与 Claude Code 的会话恢复、bridge 重放、异步工具注入（应用层）存在系统性冲突。这要求重新审视 **推理痕迹（reasoning traces）的存储、传输与重放协议**，而非仅修复单点 bug。

2. **长上下文默认化带来的压缩需求**：1M 默认 + auto-compact 失效的组合，预示 **上下文压缩/摘要** 将从可选优化变为必要基础设施，需发展更可靠的 **基于语义的自适应压缩** 而非简单阈值触发。

3. **Multi-Agent 编排的透明度缺失**：动态工作流（dynamic workflows）作为产品功能发布，但无技术细节公开。社区对 "tens to hundreds of agents" 的协调机制、状态一致性、幻觉传播控制存在信息缺口。

4. **实时推理干预（Real-time Steering）**：#30492 的高赞反映用户对长任务可控性的强烈需求，指向 **inference-time alignment** 和 **可中断/可转向推理** 的研究空间。

---

## 技术局限性

| 限制类别 | 具体表现 | 涉及 Issue 集群 |
|---------|---------|--------------|
| **Thinking Block 不可变性与会话变异的不兼容** | 任何 transcript 修改（恢复、重放、工具回调）均可能破坏 thinking block 的原始性 | #10199, #63147, #63394, #63322, #63221, #63380, #63321, #63404, #63201, #63393, #63418 |
| **上下文窗口管理的黑箱性** | 1M 默认不可降级、auto-compact 阈值不透明、token 消耗昼夜波动 | #62063, #63426 |
| **跨模型/跨版本推理状态迁移失败** | 版本更新或模型切换后 extended thinking 会话不可逆损坏 | #63322 |
| **异步推理与同步消息协议的冲突** | `run_in_background` 结果注入与 interleaved thinking 的时序竞争 | #63393, #60094 |
| **安全对齐的过度拒绝** | Cyber safeguards 误触发，缺乏细粒度申诉/调整机制 | #61056 |

---

*注：本摘要过滤了 Windows Cowork VM、UI/TUI、权限沙箱、Git 操作等纯工程议题，聚焦长上下文推理、多模态/视觉语言、后训练对齐与幻觉缓解相关信号。*

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

# OpenAI Codex 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日研究相关动态聚焦于**长上下文会话的稳定性与结构化保留**、**模型上下文片段的隐式引导机制**，以及**沙箱安全与执行可靠性**的深层改进。核心工程团队正通过内部上下文片段（internal context fragments）和云配置分发体系，推进运行时模型行为的精细化控制。

---

## 2. 版本发布

**rust-v0.135.0** 已发布，研究相关更新：
- `codex doctor` 增强环境诊断能力，包含 Git、终端、app-server 及**线程清单（thread inventory）**诊断，支持长会话故障排查（[#24261](https://github.com/openai/codex/pull/24261), [#24311](https://github.com/openai/codex/pull/24311), [#24305](https://github.com/openai/codex/pull/24305)）
- `/status` 新增远程连接详情与服务器版本展示，支撑分布式/远程推理场景的可观测性（[#24420](https://github.com/openai/codex/pull/24420)）

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 |
|---|------|------|---------|
| [#24810](https://github.com/openai/codex/issues/24810) | **Session Bridge - Structured Context Preservation for Long-Running Agent Sessions** | OPEN | **长上下文推理**：提出"结构化上下文保留"替代简单压缩，将知识路由至永久存储而非扁平化摘要，直接关联长会话记忆机制与上下文窗口优化 |
| [#21671](https://github.com/openai/codex/issues/21671) | `/compact` fails with unknown service_tier parameter | CLOSED | **长上下文/后训练对齐**：`service_tier` 参数错误暴露 API 层对模型能力分层的配置脆弱性，影响上下文压缩功能的可靠性 |
| [#22876](https://github.com/openai/codex/issues/22876) | `/responses/compact` sends `service_tier` when provider-scoped API-key auth is used | OPEN | **后训练对齐/长上下文**：第三方模型 provider 场景下压缩接口的参数污染问题，反映多 provider 对齐的复杂性 |
| [#15349](https://github.com/openai/codex/issues/15349) | Loss of large amount of recent conversation turns / history / context after app restart | OPEN | **长上下文推理**：应用重启后大量对话历史丢失，暴露会话状态持久化与上下文恢复机制的关键缺陷 |
| [#15709](https://github.com/openai/codex/issues/15709) | Codex CLI loses conversation history after session resume (history truncated) | OPEN | **长上下文推理**：会话恢复后历史截断，与上下文窗口管理、流式状态同步机制相关 |
| [#24951](https://github.com/openai/codex/issues/24951) | multi_agent wait_agent/spawn_agent can block for ~7.5h; wait_agent timeout_ms not enforced during runtime stall | OPEN | **多智能体推理/可靠性**：多智能体协调中的超时机制失效，反映分布式推理调度的幻觉性阻塞问题 |
| [#24280](https://github.com/openai/codex/issues/24280) | Remote-created threads on connected host do not receive automation_update/load_workspace_dependencies | OPEN | **多模态/工具调用**：远程线程的动态工具供给缺失，影响跨设备视觉-语言-工具协同能力 |
| [#18708](https://github.com/openai/codex/issues/18708) | Allow edit on any message, not just the last one | OPEN | **交互式推理/幻觉缓解**：任意消息编辑能力缺失限制用户修正模型错误理解，影响迭代式对齐效率 |
| [#10561](https://github.com/openai/codex/issues/10561) | Plan Mode: Add "Copy Plan" button & "Clear Context and Start Coding" workflow | OPEN | **长上下文/规划推理**：规划与执行阶段的上下文桥接需求，反映复杂任务分解中的状态转移问题 |
| [#14601](https://github.com/openai/codex/issues/14601) | Prevent Configuration Pollution: Separate `projects.xxxx.trusted_level` from `config.toml` | OPEN | **后训练对齐/安全性**：项目级信任配置与全局配置的隔离需求，关联模型能力分级的安全对齐 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|---------|
| [#24918](https://github.com/openai/codex/pull/24918) | **Use internal model context fragments for goal steering** | **后训练对齐/推理引导**：将目标引导从 `<goal_context>` 专用包装迁移至 source-labeled 内部上下文片段，为 core 与 extensions 提供统一的隐式模型引导形状，支持更精细的推理时干预而不暴露提示结构 |
| [#24126](https://github.com/openai/codex/pull/24126)-[#24127](https://github.com/openai/codex/pull/24127)-[#23976](https://github.com/openai/codex/pull/23976) | **Next-prompt suggestion engine [1-3 of 3]** | **长上下文/交互式推理**：构建核心建议引擎→app-server API→TUI 渲染的完整链路，基于会话历史主动生成下一步提示，降低用户认知负荷并维持长会话连贯性 |
| [#24979](https://github.com/openai/codex/pull/24979)-[#24981](https://github.com/openai/codex/pull/24981)-[#24982](https://github.com/openai/codex/pull/24982)-[#24980](https://github.com/openai/codex/pull/24980) | **Unified exec zsh fork composition & sandbox trampoline** | **可靠性/安全性**：组合 `shell_zsh_fork` 与 unified exec 模式，通过 trampoline 机制保持沙箱权限层级，解决特权提升场景下的重复授权问题，增强命令执行的可验证性 |
| [#17573](https://github.com/openai/codex/pull/17573) | **Add sandbox violation monitoring in codex-sandboxing** | **幻觉缓解/可靠性**：统一沙箱违规模型（filesystem/network），建立标准化的拒绝分类体系，为安全策略的精确评估与模型行为的可解释性提供基础设施 |
| [#24621](https://github.com/openai/codex/pull/24621)-[#24622](https://github.com/openai/codex/pull/24622) | **Cloud config bundle transport & runtime switch** | **后训练对齐/系统可靠性**：统一云配置分发体系，替换遗留运行时路径，支持模型能力参数、安全策略的动态下发与版本一致性 |
| [#24992](https://github.com/openai/codex/pull/24992)/[#24959](https://github.com/openai/codex/pull/24959) | **Move skills path refs into exec server** | **多模态工具调用**：将技能路径引用绑定至执行服务器环境抽象 `EnvironmentPathRef`，统一本地/远程/插件技能的文件系统解析，支撑跨环境视觉-语言-工具协同 |
| [#22668](https://github.com/openai/codex/pull/22668)/[#22673](https://github.com/openai/codex/pull/22673) | **Managed MITM CA trust & credentialed route discovery** | **安全性/可靠性**：托管代理的证书信任注入与凭据路由发现，为受控网络环境下的安全工具调用与数据流审计提供基础 |

---

## 5. 研究方向信号

| 趋势 | 证据 |
|------|------|
| **长上下文结构化保留 > 简单压缩** | [#24810](https://github.com/openai/codex/issues/24810) 明确反对"压缩为扁平文件"，主张知识路由至永久结构化存储；[#24126](https://github.com/openai/codex/pull/24126) 系列推进会话级主动建议以维持连贯性 |
| **隐式模型引导的标准化** | [#24918](https://github.com/openai/codex/pull/24918) 将 goal steering 泛化为 internal context fragments，预示运行时干预机制从 ad-hoc 向系统化演进 |
| **多智能体调度的可靠性瓶颈** | [#24951](https://github.com/openai/codex/issues/24951) 7.5小时阻塞暴露 timeout 语义与运行时 stall 的脱节，分布式推理的协调层需根本性重设计 |
| **云-端配置一致性成为对齐基础设施** | [#24621](https://github.com/openai/codex/pull/24621)-[#24622](https://github.com/openai/codex/pull/24622) 将模型能力参数、安全策略纳入统一配置 bundle，后训练对齐从模型权重扩展至系统运行时 |
| **沙箱违规的可解释性需求** | [#17573](https://github.com/openai/codex/pull/17573) 统一违规分类，反映安全策略评估从"是否阻断"向"为何阻断、如何归类"的精细化需求 |

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 关联 Issue/PR |
|---------|---------|-------------|
| **上下文窗口的脆弱性** | 压缩接口 (`/compact`) 因 API 参数层级错误失败；会话恢复/重启导致历史截断或丢失 | [#21671](https://github.com/openai/codex/issues/21671), [#22876](https://github.com/openai/codex/issues/22876), [#15349](https://github.com/openai/codex/issues/15349), [#15709](https://github.com/openai/codex/issues/15709) |
| **多智能体超时的语义失效** | `timeout_ms` 参数在运行时 stall 期间不被执行，阻塞时间可达数小时 | [#24951](https://github.com/openai/codex/issues/24951) |
| **远程-本地环境的能力漂移** | 远程创建线程缺失动态工具供给，Chrome 插件在远程/Windows 场景下可用性不一致 | [#24280](https://github.com/openai/codex/issues/24280), [#21598](https://github.com/openai/codex/issues/21598), [#21791](https://github.com/openai/codex/issues/21791) |
| **配置污染与安全隔离** | 项目级信任配置与全局配置耦合，影响多项目场景下的能力分级安全 | [#14601](https://github.com/openai/codex/issues/14601) |
| **规划-执行阶段的上下文断裂** | 用户需手动复制计划、清空上下文再进入编码，缺乏结构化状态转移机制 | [#10561](https://github.com/openai/codex/issues/10561) |

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

# Gemini CLI 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日 Gemini CLI 的更新以稳定性修复为主，核心研究信号集中在**Agent 评估基础设施**与**长上下文工具调度**两大方向。值得关注的是，组件级行为评估（behavioral evals）体系已扩展至 76 个测试用例，同时 AST 感知代码理解工具链的调研进入实质性阶段，可能对未来代码 Agent 的上下文推理效率产生显著影响。

---

## 2. 版本发布

| 版本 | 研究相关性 | 说明 |
|:---|:---|:---|
| v0.45.0-preview.1 | 低 | 补丁版本，仅包含稳定性修复（cherry-pick #bd53951），无研究相关变更 |
| v0.44.1 | 低 | 同上，针对 v0.44.0 的冲突修复补丁 |
| v0.45.0-nightly.20260528.g5cac7c10f | 无 | Vim 按键映射修复，纯 UI 交互改进 |

> 今日无直接涉及模型能力、推理架构或训练对齐的版本更新。

---

## 3. 研究相关 Issues

### 评估与对齐基础设施

| # | 标题 | 研究价值 | 链接 |
|:---|:---|:---|:---|
| **#24353** | Robust component level evaluations | **核心研究基础设施**。行为评估体系已从初始 16 个扩展至 76 个测试，覆盖 6 个 Gemini 模型版本。该体系直接支撑 Agent 能力的量化评估与 post-training 迭代，是模型对齐的关键反馈闭环。 | [链接](https://github.com/google-gemini/gemini-cli/issues/24353) |
| **#23166** | Stabilize and Enhance Internal Project Evaluations | 内部项目评估的"bleed"问题（结果不一致）直接影响训练信号可靠性。解决此问题对提升 SFT/RLHF 数据质量具有基础意义。 | [链接](https://github.com/google-gemini/gemini-cli/issues/23166) |
| **#23313** | Change the steering eval test to always pass | 转向评估（steering eval）的稳定性问题暴露了**对齐目标与评估指标之间的 tension**——当评估本身成为优化目标时可能失效，需研究更鲁棒的对齐验证方法。 | [链接](https://github.com/google-gemini/gemini-cli/issues/23313) |

### 长上下文与代码推理

| # | 标题 | 研究价值 | 链接 |
|:---|:---|:---|:---|
| **#22745** | Assess the impact of AST-aware file reads, search, and mapping | **长上下文效率的关键突破口**。AST 感知工具可减少因边界不对齐导致的重复读取（降低 token 消耗）、提升跨文件依赖推理精度，直接缓解"长上下文利用率不足"问题。 | [链接](https://github.com/google-gemini/gemini-cli/issues/22745) |
| **#22746** | Investigate using AST aware CLI tools to map codebase | 调研 tilth/glyph 等 AST 工具用于代码库映射，目标是增强 `codebase_investigator` 的**结构化上下文构建能力**。 | [链接](https://github.com/google-gemini/gemini-cli/issues/22746) |
| **#22747** | Investigate using AST aware tools to search and perform file reads | 评估 AST-grep 等工具的查询语言对 Agent 搜索效率的提升，涉及**结构化查询 vs 语义检索**的权衡研究。 | [链接](https://github.com/google-gemini/gemini-cli/issues/22747) |

### Agent 可靠性与幻觉缓解

| # | 标题 | 研究价值 | 链接 |
|:---|:---|:---|:---|
| **#21409** | Generalist agent hangs | **长上下文推理中的循环/停滞问题**。Generalist agent 在简单任务上无限挂起，暴露了点对点工具调用架构在复杂推理链中的**终止条件判定缺陷**，与推理链可靠性直接相关。 | [链接](https://github.com/google-gemini/gemini-cli/issues/21409) |
| **#22323** | Subagent recovery after MAX_TURNS is reported as GOAL success | **幻觉式成功报告**：子 Agent 达到最大回合限制却返回"成功"状态，属于**自我评估幻觉（self-evaluation hallucination）**，严重影响多 Agent 协作的可信度。 | [链接](https://github.com/google-gemini/gemini-cli/issues/22323) |
| **#21968** | Gemini does not use skills and sub-agents enough | **元认知能力缺陷**：模型无法自主识别何时调用专用技能/子 Agent，反映**工具使用意图识别**与**自我能力边界感知**的训练不足，是对齐研究的典型问题。 | [链接](https://github.com/google-gemini/gemini-cli/issues/21968) |
| **#24246** | Gemini CLI encounters 400 error with > 128 tools | **工具过载与上下文压缩**：>128 工具触发 API 错误，需研究**动态工具选择/压缩机制**，涉及长上下文中的注意力分配与工具相关性排序。 | [链接](https://github.com/google-gemini/gemini-cli/issues/24246) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 | 链接 |
|:---|:---|:---|:---|
| **#27496** | fix(core): harden PTY resize against native crashes | **可靠性工程**：通过"纵深防御"策略解决 `node-pty` 的 C++ 层竞态崩溃。虽为基础设施，但终端稳定性直接影响**长交互会话的数据完整性**（对收集训练数据至关重要）。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27496) |
| **#27531** | fix(core): handle EBADF error when resizing a closed PTY | 同上，针对平铺窗口管理器/终端复用器场景的**竞态条件修复**，减少异常终止导致的会话数据丢失。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27531) |
| **#27529** | Handle errors safely in shellExecutionService | 显式处理 `EBADF` 错误防止应用崩溃，提升**长时间运行 Agent 的鲁棒性**。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27529) |
| **#22590** | fix(cli): include all Executing subagent tool calls in useToolScheduler state | **工具调度状态机修正**：修复子 Agent 工具调用在 `useToolScheduler` 中的状态透传，直接影响**多 Agent 协作的上下文一致性**与长链推理的可观测性。 | [链接](https://github.com/google-gemini/gemini-cli/pull/22590) |
| **#27523** | fix(core): guard isFunctionCall/isFunctionResponse against empty parts | **防御性编程**：防止空 parts 导致的函数调用识别错误，减少**工具调用幻觉**（空响应被误判为有效调用）。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27523) |
| **#27455** | feat(core): Add Amazon URL parsing and metadata extraction | **结构化网页理解**：Amazon 短链接解析与产品元数据提取，涉及**半结构化数据的多模态理解**（文本+布局+图像隐含信息），但当前实现为纯文本规则，视觉理解扩展空间显著。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27455) |
| **#27522** | fix(core): skip width-0 continuation cells in terminal serializer | 终端序列化器对零宽续行单元格的过滤，影响**终端输出的精确重建**——这对基于终端截图/输出的视觉语言模型训练数据质量有间接意义。 | [链接](https://github.com/google-gemini/gemini-cli/pull/27522) |

---

## 5. 研究方向信号

```
┌─────────────────────────────────────────────────────────────────────────┐
│  趋势 1: 结构化代码理解成为长上下文优化的主攻方向                          │
│  ─────────────────────────────────────────────────────────────────────  │
│  • AST 感知工具链（#22745-22747）形成完整调研矩阵：读取 → 搜索 → 映射      │
│  • 目标：将"线性文本扫描"转为"语义结构导航"，降低 O(n) token 消耗至 O(k)   │
│  • 隐含需求：代码的多模态表示（AST + 文本 + 执行轨迹）                    │
├─────────────────────────────────────────────────────────────────────────┤
│  趋势 2: 评估基础设施从"存在性"走向"可靠性"                               │
│  ─────────────────────────────────────────────────────────────────────  │
│  • 76 个行为评估 → 组件级隔离评估 → 消除评估"bleed"                      │
│  • 关键张力：steering eval 的"总是通过"需求 vs 真实能力度量               │
│  • 指向需求：对抗性评估、动态难度调整、基于人类偏好的评估校准              │
├─────────────────────────────────────────────────────────────────────────┤
│  趋势 3: 多 Agent 系统的"元认知"与"诚实性"成为对齐新前沿                   │
│  ─────────────────────────────────────────────────────────────────────  │
│  • #22323 (虚假成功报告) + #21968 (技能调用不足) = 自我评估与自我调度双缺陷 │
│  • 需要研究：显式不确定性估计、能力边界感知、诚实性奖励塑造                  │
├─────────────────────────────────────────────────────────────────────────┤
│  趋势 4: 工具规模扩张倒逼动态上下文管理研究                                │
│  ─────────────────────────────────────────────────────────────────────  │
│  • 128+ 工具触发硬限制 (#24246)                                           │
│  • 需求：工具检索、工具摘要、层次化工具空间、工具使用预测                   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. 技术局限性

| 重复性限制 | 出现频率 | 研究空白 |
|:---|:---|:---|
| **Agent 循环/挂起无终止** | 高（#21409, #25166 等） | 缺乏基于**执行轨迹动态复杂度**的自适应回合限制；需要研究**推理链的实时进展度量** |
| **子 Agent 状态误判与恢复失败** | 高（#22323, #22093） | 多 Agent 系统的**全局一致性协议**缺失；需要形式化的 Agent 间状态机验证 |
| **工具过载导致硬失败** | 中（#24246） | 动态工具选择仍依赖启发式，缺乏**基于任务嵌入的工具检索**机制 |
| **终端/PTY 竞态崩溃** | 中（#27496, #27531, #27529） | 长时间交互会话的**状态持久化与恢复**不足，影响训练数据连续性 |
| **模型对自有能力认知不足** | 中（#21968, #21432） | **元认知训练**在 post-training 中的缺失，需引入显式的自我反思与能力边界学习目标 |

---

*摘要基于 google-gemini/gemini-cli 2026-05-28 公开数据生成。标注 🔒 的 Issue/PR 为维护者可见，摘要中仅引用已公开的标题与标签信息。*

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

# GitHub Copilot CLI 研究动态摘要 | 2026-05-29

---

## 1. 今日速览

今日 Copilot CLI 密集暴露**长上下文推理**相关的工程缺陷：上下文窗口分层配置持久化失败、系统/工具提示过度消耗 200K 窗口导致负可用空间、以及会话状态恢复时重复工具调用 ID 引发的级联故障。Claude Opus 4.8 接入与 reasoning tokens 用量报告上线，但模型能力（1M tokens）与产品层限制（200K cap）的张力持续加剧。

---

## 2. 版本发布

### v1.0.56-0 / v1.0.55（2026-05-28）

| 更新项 | 研究相关性 |
|--------|-----------|
| **Context window tier selection 持久化修复** — 分层配置现在可靠写入 session events，SDK-only resume 路径下能重新应用 tier-derived limits | 🔬 **长上下文推理**：解决上下文窗口分层（200K vs 更高 tier）在会话恢复时的状态丢失问题，直接影响长文档/代码库推理的稳定性 |
| **Claude thinking (reasoning) tokens 用量报告** | 🔬 **推理透明度**：首次在 session usage summaries 中暴露 reasoning token 消耗，为推理效率优化与成本建模提供数据基础 |
| **Claude Opus 4.8 支持** | 🔬 **模型能力迭代**：新模型接入，但需关注实际上下文窗口 cap 是否仍受产品层限制 |

> 注：Free/Student 用户强制 Auto model selection 为商业策略，不纳入研究总结。

---

## 3. 研究相关 Issues

### 长上下文推理（Long-Context Reasoning）

| # | Issue | 研究价值 |
|---|-------|---------|
| **#3527** | [contextTier setting persisted but not applied on session start](https://github.com/github/copilot-cli/issues/3527) | **核心缺陷**：用户显式选择的长上下文 tier（如 1M）在会话重启后回退至 200K 默认值，暴露配置-运行时状态同步的系统性问题，直接影响长代码库推理的可复现性 |
| **#3355** | [Allow configurable context window for Claude Opus 4.6 (200K cap vs 1M model capability)](https://github.com/github/copilot-cli/issues/3355) | **能力-产品张力**：模型原生支持 1M tokens 但产品层硬编码 200K cap，导致 80% 上下文损失与频繁 auto-compaction；是研究"有效上下文利用率"与"压缩-推理权衡"的典型案例 |
| **#3539** | [System/Tools consume 73% of context window, triggering auto-compaction on first message](https://github.com/github/copilot-cli/issues/3539) | **上下文预算分配**：~10 个 MCP servers + plugins 的 system/tools 提示占用 146K/200K，用户消息前已无可用空间；揭示工具化 Agent 架构中"固定开销膨胀"对有效推理长度的侵蚀 |
| **#3543** | [Startup input lag: unbounded recursive glob over $COPILOT_CUSTOM_INSTRUCTIONS_DIRS](https://github.com/github/copilot-cli/issues/3543) | **上下文预处理效率**：自定义指令目录的递归 glob 在大型代码库上导致 15-30s 冻结，反映上下文索引/加载阶段的算法复杂度问题 |

### 会话状态与推理可靠性（Session State → Hallucination/Error Propagation）

| # | Issue | 研究价值 |
|---|-------|---------|
| **#3559** | [Frequent websocket_error: Duplicate item found (fc_call_* replay from session-state)](https://github.com/github/copilot-cli/issues/3559) | **状态恢复一致性**：会话状态持久化中工具调用 ID 重复，导致服务端拒绝请求；揭示 deterministic ID generation 与 session replay 的可靠性缺陷，可能引发推理链断裂 |
| **#3560** | [Duplicate item found with id fc_call_... after tool/function call](https://github.com/github/copilot-cli/issues/3560) | **时序相关故障**：同一版本同一工作流白天正常、晚间故障，提示服务端/客户端状态同步存在时间窗口或部署相关的非确定性，是研究"工具调用幂等性"的边界案例 |
| **#3558** | [Duplicate Item Errors](https://github.com/github/copilot-cli/issues/3558) | **同根故障确认**：多用户独立报告相同错误模式，确认非孤立事件，指向工具调用 ID 分配或会话序列化中的系统性 race condition |

### 模型调度与推理控制（Model Routing / Reasoning Control）

| # | Issue | 研究价值 |
|---|-------|---------|
| **#3565** | [Task tool silently downgrades subagent model via multiplier guard](https://github.com/github/copilot-cli/issues/3565) | **推理资源分配**：subagent 的显式模型选择（frontmatter 或运行时 override）被成本乘数守卫静默覆盖，导致"预期推理能力"与"实际执行模型"不一致；是研究"经济约束下的推理质量保障"的关键案例 |
| **#3185** | [BYOK Anthropic: catch-all defaultReasoningEffort: "medium" breaks Claude Haiku 4.5](https://github.com/github/copilot-cli/issues/3185) | **推理参数兼容性**：非注册模型的默认 reasoning effort 配置导致请求失败，暴露"模型能力检测-参数适配"机制的脆弱性，对多模型后端的路由逻辑有借鉴意义 |

### 工具-模型交互可靠性（Tool-Model Interaction）

| # | Issue | 研究价值 |
|---|-------|---------|
| **#3258** | [MCP tool responses: only structuredContent forwarded, unstructured content dropped](https://github.com/github/copilot-cli/issues/3258) | **多模态/结构化推理**：MCP 工具返回的混合内容中仅 structuredContent 传入模型，文本描述被静默丢弃；可能破坏工具输出语义完整性，影响基于工具反馈的推理链正确性 |

---

## 4. 研究相关 PR 进展

**今日无更新 PR**（过去 24 小时内 0 条 PR 活动）。

---

## 5. 研究方向信号

### 趋势一：长上下文"名义容量" vs "有效容量"的鸿沟扩大
- 模型层持续扩展（1M+ tokens），但产品层因成本/延迟限制维持 200K cap
- 系统提示（MCP tools + plugins）进一步侵蚀用户可用预算，形成"负可用空间"现象
- **研究需求**：动态上下文预算分配算法、工具提示压缩/摘要机制、分层上下文激活策略

### 趋势二：会话状态持久化成为可靠性瓶颈
- 重复 `fc_call_*` ID 错误集中爆发，涉及 session-state replay、SDK-only resume、并行会话冲突
- **研究需求**：确定性会话序列化、工具调用幂等性保证、跨会话状态隔离与合并语义

### 趋势三：推理透明度与可控性需求上升
- Claude thinking tokens 开始被计量报告，但 reasoning effort 的自动/手动控制仍显粗糙（如 #3185 的 catch-all 配置）
- **研究需求**：细粒度 reasoning budget 控制、推理深度-延迟-成本的 Pareto 前沿建模

### 趋势四：多 Agent/Subagent 系统的资源竞争
- Task tool 的成本乘数守卫静默降级子 Agent 模型，违背用户显式意图
- **研究需求**：多 Agent 系统的资源公平分配、能力契约验证、预期行为一致性保障

---

## 6. 技术局限性

| 限制类别 | 具体表现 | 影响的研究问题 |
|---------|---------|-------------|
| **上下文窗口硬编码上限** | Claude Opus 4.6/4.8 的 1M 能力被限制为 200K，且 `contextTier` 配置不可靠 | 长代码库理解、跨文件依赖推理、大规模文档分析的有效性 |
| **系统提示开销无界增长** | MCP servers + plugins 的静态描述累积，缺乏动态加载/卸载机制 | 工具化 LLM 的可扩展性、上下文预算的最优分配 |
| **会话状态非确定性** | 工具调用 ID 重复、并行会话权限覆盖、resume 路径状态丢失 | 长期交互的可靠性、推理链的可复现性 |
| **模型路由的静默覆盖** | 成本约束优先于用户显式选择，且降级行为不透明 | 用户意图对齐、推理质量的可预期性 |
| **混合内容过滤损失** | MCP 响应中结构化/非结构化内容的选择性丢弃 | 多模态/工具反馈信息的完整性利用 |

---

*摘要生成时间：2026-05-29 | 数据来源：github.com/github/copilot-cli*

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

# Kimi Code CLI 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日 Kimi CLI 仓库无新版本发布，但社区对**长上下文可靠性**的痛点集中爆发：大 context 场景下的 ConnectTimeout 问题（#2384）获得关注，同时多个 PR 聚焦**历史会话恢复中的工具调用一致性**（#2383）和**上下文截断映射修复**（#2386），反映出长程交互中的状态管理仍是核心研究挑战。多模态方面，ReadMediaFile 的图像格式转换 PR（#2382）扩展了视觉输入兼容性。

---

## 2. 版本发布

无新版本发布。PR #2391 正在推进 1.46.0 版本 bump，但属于常规版本迭代，无研究相关功能更新。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 | 链接 |
|---|------|---------|------|
| **#2384** | 大 context 请求频繁 ConnectTimeout，httpx connect_timeout 不可配 | **长上下文推理基础设施**：120k+ input token 时网络层超时暴露长上下文服务的工程瓶颈，涉及流式传输优化、超时策略自适应等研究问题 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2384) |
| **#2394** | ACP 客户端无法获取 per-turn token usage | **推理效率与可观测性**：token usage 的透明化是评估长上下文成本、优化上下文压缩策略的前提，对上下文预算管理和推理效率研究有直接意义 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2394) |
| **#2127** | 未实现 ACP 协议的 `session/list`、`session/get` 等方法 | **长程会话管理**：历史会话检索的缺失限制了多轮推理任务的连续性研究，涉及会话状态持久化与长期记忆机制 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/2127) |
| **#1984** | 终端退出挂起与 MCP 连接泄漏 | **系统可靠性与资源对齐**：长时间会话后的优雅退出机制，关联到 agent 生命周期管理与资源释放的对齐问题 | [链接](https://github.com/MoonshotAI/kimi-cli/issues/1984) |

> **跳过**：#1894（skill 目录递归加载，产品功能）、#2381（社区分裂争议，非技术）、#2385（Zed 文件搜索死循环，IDE 集成 bug）

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 | 链接 |
|---|------|---------|------|
| **#2383** | fix(soul): 修复历史回放时的 orphan tool_calls | **幻觉缓解/工具调用一致性**：会话中断（OOM/kill -9）后，持久化的 `context.jsonl` 可能包含未完成 tool_call 的 assistant 消息，导致历史回放时模型产生幻觉式工具调用。本 PR 修复该状态不一致问题，提升长程交互可靠性 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2383) |
| **#2386** | fix(session): 将 undo wire turns 映射到 context turns | **长上下文一致性/状态对齐**：`/undo` 和 fork 操作此前混用 wire 索引与 context 索引，导致本地 slash-command 场景下上下文截断错误。修复后保证多轮编辑-撤销场景下的上下文一致性，对迭代式代码生成任务的推理稳定性至关重要 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2386) |
| **#2382** | fix(file): ReadMediaFile 中转换不支持的图像格式为 PNG | **多模态推理/OCR 前置**：将 `.ico` 等非常规格式转换为模型可接受的 `image/png`，扩展视觉输入兼容性。这是视觉语言模型工具链中图像预处理的标准化研究问题 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2382) |
| **#2132** | fix(acp): 加载时回放 session 历史 | **长程会话恢复**：为 ACP 运行持久化 wire history，使加载的会话具备可回放事件，支撑跨会话的长程推理连续性 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2132) |
| **#1985** | fix(term, app): 防止退出时 TTY 挂起并关闭 MCP 连接 | **系统可靠性/资源对齐**：通过非阻塞 I/O 修复终端挂起，确保 MCP 连接在关闭时正确释放，减少长时间运行 agent 的资源泄漏 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/1985) |
| **#2387** | fix(tools): 保留 shell 命令 headline 细节 | **推理可解释性**：修复长命令被 `shorten_middle` 截断导致的可读性损失，改善工具调用轨迹的人类审计与调试体验 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2387) |
| **#2389** | fix(tools): 错误摘要中包含尾部输出并以纯文本渲染 | **错误恢复与推理调试**：失败命令的尾部输出对诊断工具调用错误至关重要，纯文本渲染避免格式干扰，提升 agent 自我纠错能力 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2389) |
| **#2369** | feat(subagent): 并行 subagent 执行的 API key pool | **分布式推理扩展**：轮询式 API key 分配器支持并行 subagent 执行，为大规模代码分析等长上下文分治策略提供基础设施 | [链接](https://github.com/MoonshotAI/kimi-cli/pull/2369) |

> **跳过**：#2047（MCP 配置加载，产品功能）、#2393/#2390（文档/欢迎语更新，UI）、#2388（粘贴文本占位符，交互细节）

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|------|------|---------|
| **长上下文可靠性 > 规模扩展** | #2384（120k+ 超时）、#2383（中断恢复）、#2386（undo 一致性） | 社区焦点从"能处理多长"转向"长程交互中的容错与一致性"，提示需要研究：上下文检查点机制、渐进式状态同步、自适应超时策略 |
| **工具调用状态的幻觉风险** | #2383（orphan tool_calls）、#2386（wire/context 索引错位） | 复杂 agent 系统中，状态持久化与回放的不一致是幻觉的新来源，需研究形式化的工具调用事务语义 |
| **视觉输入标准化需求** | #2382（图像格式转换） | 多模态工具链的鲁棒性仍依赖预处理层，端到端视觉理解对格式无关性的研究有需求 |
| **Token 效率可观测性缺口** | #2394（per-turn usage 缺失） | 长上下文成本优化缺乏细粒度数据，阻碍上下文压缩、选择性记忆等 post-training 对齐研究 |

---

## 6. 技术局限性

| 限制 | 来源 | 研究空白 |
|------|------|---------|
| **长上下文网络层超时不可配置** | #2384 | 缺乏针对大 payload 的自适应传输协议研究；httpx 固定超时与流式推理的动态需求不匹配 |
| **会话中断后的状态腐败** | #2383, #1984 | 无事务性持久化机制，kill -9/OOM 场景下缺乏崩溃一致性保证，类似数据库的 WAL/快照机制尚未引入 |
| **wire 与 context 双层索引的语义鸿沟** | #2386 | 交互层（wire）与模型层（context）的状态映射缺乏形式化定义，导致编辑/撤销操作的语义漂移 |
| **Token usage 的观测盲区** | #2394 | ACP 协议层的 usage 透传缺失，限制了外部系统对推理成本的实时反馈与优化闭环 |

---

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

# OpenCode 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日 OpenCode 生态中，**推理控制与可靠性**成为核心议题：DeepSeek V4 系列的 `reasoning_content` 传递机制出现断裂（#29618），GPT-5.5 的推理级别选择器在 V2 UI 中被隐藏（#29051），同时 Anthropic 的自适应推理控制刚在 v1.15.12 中修复启用。这些信号表明，**长上下文推理的可控性与透明度**仍是生产环境中的关键痛点。

---

## 2. 版本发布

### v1.15.12
| 项目 | 内容 |
|:---|:---|
| **研究相关更新** | 为 Anthropic 模型启用 **adaptive reasoning controls**（自适应推理控制）— 允许动态调节推理深度 |
| **基础设施** | 新增 WebSocket transport for OpenAI responses（实验性，`OPENCODE_EXPERIMENTAL_WEBSOCKETS=true`）— 可能改善流式推理的延迟稳定性 |
| **链接** | [Release v1.15.12](https://github.com/anomalyco/opencode/releases/tag/v1.15.12) |

> **研究价值**：自适应推理控制直接关联 **post-training 对齐** 中的推理-计算权衡（reasoning-compute tradeoff），是长上下文场景中优化延迟与质量的核心机制。

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 | 链接 |
|:---|:---|:---|:---|:---|
| **#29618** | `reasoning_content` is missing when using DeepSeek V4 Flash in thinking | 🔴 OPEN | **长上下文推理 / 幻觉缓解**：DeepSeek V4 Flash/Pro 的 thinking 模式下，`reasoning_content` 未回传导致 API 报错。暴露多轮推理链的**状态传递脆弱性**，直接影响推理可追溯性与幻觉检测能力。 | [链接](https://github.com/anomalyco/opencode/issues/29618) |
| **#29051** | V2 prompt input hides model reasoning selector | 🔴 OPEN | **长上下文推理 / UI 对齐**：GPT-5.5 等模型的 reasoning variant selector 在 V2 UI 中被隐藏，用户无法动态调节推理强度。反映**推理可控性**在前端架构中的退化。 | [链接](https://github.com/anomalyco/opencode/issues/29051) |
| **#29079** | GPT Models takes too long to respond | 🔴 OPEN | **长上下文推理 / 效率**：GPT 5.4 xhigh 等高级推理模型响应时间极端不稳定（秒级→分钟级），暴露**自适应推理调度**的调度策略缺陷。 | [链接](https://github.com/anomalyco/opencode/issues/29079) |
| **#6651** | Dynamic model selection for subagents via Task tool | 🔴 OPEN | **Post-training 对齐 / 多智能体**：主 agent 无法为子任务动态选择模型，导致简单任务被过度推理或复杂任务推理不足。涉及**任务-推理能力匹配**的自动化对齐问题。 | [链接](https://github.com/anomalyco/opencode/issues/6651) |
| **#29571** | Conversation permanently stuck after 'vision is not enabled' error | 🔴 OPEN | **多模态推理 / 幻觉缓解**：GitHub Copilot provider 的 vision 能力检测失败导致会话永久僵死，暴露**多模态能力声明与实际可用性**的错位，以及错误恢复机制的缺失。 | [链接](https://github.com/anomalyco/opencode/issues/29571) |
| **#29779** | write/edit tools silently abort for files >~6KB | 🟢 CLOSED | **长上下文 / 可靠性**：大文件（>6KB）的编辑工具静默失败，无错误反馈。反映**长上下文窗口内的工具执行边界**未明确，可能导致幻觉性"成功"状态。 | [链接](https://github.com/anomalyco/opencode/issues/29779) |
| **#29764** | opencode nuke files | 🟢 CLOSED | **幻觉缓解 / 安全性**：LLM 指令导致文件被无故删除/覆盖，缺乏**预防性安全对齐**机制。用户被动防御模式不可持续，需研究**工具调用的保守性约束**。 | [链接](https://github.com/anomalyco/opencode/issues/29764) |
| **#23464** | Opus 4.7 occasionally failing tool calls (ex: question tool) | 🟢 CLOSED | **多模态推理 / 结构化输出**：Claude Opus 4.7 的 tool call 参数类型错误，暴露**视觉-语言模型的结构化推理**在复杂 schema 上的不稳定性。 | [链接](https://github.com/anomalyco/opencode/issues/23464) |
| **#29776** | Azure AI Foundry partner deployments capped at 4096 output tokens | 🔴 OPEN | **长上下文推理 / 部署对齐**：DeepSeek-V4-Pro、Kimi-K2.6 等第三方模型被错误路由至 OpenAI Responses API，输出 token 被截断。反映**模型能力-API 路由对齐**的系统性问题。 | [链接](https://github.com/anomalyco/opencode/issues/29776) |
| **#28686** | Desktop V2 UI hides prompt controls and status popover | 🔴 OPEN | **多模态推理 / 交互对齐**：agent selector、model variant/thinking-effort selector、MCP/LSP 状态均被隐藏。V2 UI 的**推理透明度与可控性**显著退化。 | [链接](https://github.com/anomalyco/opencode/issues/28686) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 状态 | 技术贡献 | 链接 |
|:---|:---|:---|:---|:---|
| **#29801** | fix: de-flake compaction backoff-abort and openai ws-pool tests | 🔵 OPEN | **可靠性 / 长上下文**：修复 session compaction 的竞态条件与 OpenAI WebSocket 连接池的 wall-clock race。后者是流式推理延迟稳定性的基础设施修复。 | [链接](https://github.com/anomalyco/opencode/pull/29801) |
| **#29738** | fix(opencode): update skill handling in context and permissions | 🔵 OPEN | **Post-training 对齐 / 权限对齐**：`skill.available()` 权限过滤 + `skill.format` 配置序列化（XML/JSON/Markdown）。技能注入格式的可控性直接影响**上下文污染与幻觉风险**。 | [链接](https://github.com/anomalyco/opencode/pull/29738) |
| **#24852** | feat: add `skills.format` config option for skill serialization format | 🟢 CLOSED | **Post-training 对齐**：同上，技能序列化格式的显式控制，减少因格式不一致导致的**指令跟随偏差**。 | [链接](https://github.com/anomalyco/opencode/pull/24852) |
| **#24816** | fix(acp): accept https:// URIs in image content blocks | 🟢 CLOSED | **多模态推理 / OCR-HMER**：ACP 协议此前仅接受 `http:` 前缀的图像 URI，`https://` 被错误过滤。修复**安全图像传输**的协议兼容性，影响视觉输入的完整性。 | [链接](https://github.com/anomalyco/opencode/pull/24816) |
| **#11303** | feat: let ACP client expose the input/output properly | 🔵 OPEN | **多模态推理 / 可解释性**：ACP 工具调用的 input/output 暴露方式重构，从 `kind: "execute"` 迁移至更透明的流式更新。提升**推理过程的可观察性**，辅助幻觉检测。 | [链接](https://github.com/anomalyco/opencode/pull/11303) |
| **#29666** | fix(opencode): enforce storage path invariants | 🔵 OPEN | **长上下文 / 可靠性**：PathStorage 值对象 + 跨平台路径归一化。会话事件 JSON 的持久化一致性，直接影响**长会话历史的完整恢复**。 | [链接](https://github.com/anomalyco/opencode/pull/29666) |
| **#24726** | feat(session): add methods to migrate session | 🟢 CLOSED | **长上下文 / 状态管理**：会话历史与孤儿会话恢复的一等支持。长上下文应用中的**会话连续性**是推理一致性的基础。 | [链接](https://github.com/anomalyco/opencode/pull/24726) |
| **#24720** | fix(desktop): prevent 100% CPU usage caused by infinite reconnects | 🟢 CLOSED | **可靠性 / 资源对齐**：无限重连与递归目录遍历导致的 CPU 耗尽。极端情况下的**推理服务可用性**保障。 | [链接](https://github.com/anomalyco/opencode/pull/24720) |
| **#24707** | Add Effect Drizzle SQLite adapter | 🟢 CLOSED | **基础设施 / 可扩展性**：SQLite 查询的 Effect 化封装，为**大规模会话数据的结构化查询**提供类型安全基础。 | [链接](https://github.com/anomalyco/opencode/pull/24707) |
| **#24740** | fix(opencode): batch vcs git show calls | 🟢 CLOSED | **长上下文 / 效率**：大重构场景下的 `git show` 批量化，减少 VCS 上下文加载的 I/O 瓶颈。 | [链接](https://github.com/anomalyco/opencode/pull/24740) |

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|:---|:---|:---|
| **🔥 推理可控性危机** | #29618, #29051, #29079, v1.15.12 adaptive reasoning fix | 用户与系统均需要**显式的推理级别控制**，但 UI 架构与 API 协议未能同步支持。研究需求：推理强度的**动态预测与自适应调节**算法。 |
| **🔥 多模态能力-声明错位** | #29571 (vision), #24816 (https image URI), #29776 (Azure routing) | 视觉能力的**运行时检测与优雅降级**机制缺失，导致硬失败。研究需求：多模态模型的**能力协商协议**（capability negotiation）。 |
| **⚠️ 长上下文工具边界模糊** | #29779 (6KB 静默失败), #29764 (文件误删) | 工具执行在上下文边界处的**失败模式不透明**，用户无法区分"成功"与"幻觉性成功"。研究需求：**工具调用的保守性验证**与可撤销执行。 |
| **⚠️ 子智能体对齐碎片化** | #6651 (动态模型选择), #27497 (权限继承断裂) | 多智能体系统中的**任务-模型匹配**与权限传递缺乏统一框架。研究需求：基于任务复杂度的**自动化模型路由**与权限继承的形式化规范。 |

---

## 6. 技术局限性

| 局限性 | 典型表现 | 研究空白 |
|:---|:---|:---|
| **推理链状态传递脆弱** | DeepSeek V4 `reasoning_content` 丢失导致 API 级联失败 (#29618) | 缺乏**推理中间状态的校验与恢复**机制；thinking 模式的标准化协议缺失 |
| **自适应推理的延迟不可预测性** | GPT 5.4 xhigh 秒级~分钟级波动 (#29079) | 无**推理深度-延迟的显式建模**，用户无法获得服务质量承诺 |
| **视觉能力运行时检测失效** | "vision is not enabled" 僵死会话 (#29571) | 缺乏**多模态能力的声明-验证闭环**；组织策略与模型能力的动态同步机制 |
| **大文件编辑的静默截断** | >6KB 文件 write/edit 无错误反馈 (#29779) | 工具输出的**长度边界显式协商**缺失；长上下文中的分块策略未标准化 |
| **UI 架构与推理能力解耦** | V2 UI 隐藏 reasoning selector (#29051, #28686) | 前端框架缺乏**推理可控性的一等公民**设计模式 |

---

> **分析师注**：今日数据强烈指向一个核心矛盾——**推理能力的增强与推理可控性的退化同步发生**。v1.15.12 对 adaptive reasoning controls 的修复是积极信号，但 V2 UI 的架构退化（#29051, #28686）表明产品迭代中缺乏对推理透明度的系统性保障。建议关注 ACP 协议中 input/output 暴露的 PR #11303 进展，这可能是构建可解释推理基础设施的关键节点。

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

# Pi 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日 Pi 的核心研究动态集中在**长上下文可靠性修复**与**推理链完整性保障**两大方向。GPT-5.5 的 1M 上下文窗口被错误截断至 272K 的问题获修复，同时多个 PR 针对推理内容（reasoning_content）的流式传输时序、工具调用签名匹配等关键缺陷进行了深度修补，直接影响多步推理的可追溯性与幻觉控制。

---

## 2. 版本发布

**v0.77.0** 已发布，研究相关更新：
- **Claude Opus 4.8 自适应推理支持**：更新 Opus 模型的 adaptive-thinking 元数据，扩展动态推理深度调节的覆盖范围（与 post-training 对齐中的推理控制策略相关）
- **选择性工具禁用（`--exclude-tools` / `-xt`）**：支持精确排除特定内置/扩展/自定义工具，为工具使用策略的对齐实验提供细粒度控制

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 |
|---|------|------|----------|
| [#5087](https://github.com/earendil-works/pi/issues/5087) | OpenAI GPT-5.5 context window is capped at 272K | **CLOSED** | **长上下文核心修复**：GPT-5.5 实际支持 1,050,000 token 上下文，但 Pi 错误限制为 272K，导致长文档推理、代码库级分析等场景的严重截断与信息丢失。直接影响长上下文推理的可用性上限。 |
| [#4945](https://github.com/earendil-works/pi/issues/4945) | openai-codex can hang on Working... with zero-usage aborted turns | **OPEN** | **流式推理可靠性**：GPT-5.5/Codex 在 TUI 中无文本流、无工具调用、无错误的"假死"状态，需强制中断。反映长程交互中模型响应状态机与客户端流式解析的同步缺陷，可能导致幻觉性"沉默失败"。 |
| [#5148](https://github.com/earendil-works/pi/issues/5148) | Resuming session with ChatGPT 5.5 after Claude Opus 4.7 extended thinking returns 400 | **CLOSED** | **跨模型上下文迁移与推理链完整性**：Claude 的 extended-thinking  turns 与 OpenAI 响应格式混用导致重复消息 ID 错误。暴露多提供商推理历史序列化中的标识冲突问题，影响长对话的连续性。 |
| [#4801](https://github.com/earendil-works/pi/issues/4801) | Error: 400 reasoning_effort for DeepSeek v4 pro xhigh | **CLOSED** | **推理强度参数对齐**：DeepSeek v4 Pro 的 `reasoning_effort` 枚举值 `"xhigh"` 被错误拒绝，显示提供商间推理控制参数的标准化缺口，影响 post-training 推理策略的跨平台部署。 |
| [#5106](https://github.com/earendil-works/pi/issues/5106) | DeepSeek v4 flash missing reasoning_content with custom preset | **CLOSED** | **推理内容可追溯性**：自定义预设下 `reasoning_content` 字段丢失，导致模型思维链不可见，直接削弱幻觉检测与推理审计能力。 |
| [#5149](https://github.com/earendil-works/pi/issues/5149) | gpt-5.5: 400 Duplicate item found with id msg_4 after a few turns | **CLOSED** | **长对话消息去重机制**：5+ turns 后消息 ID 冲突，根因是 `convertResponsesMessages` 对无 text block 的消息使用索引生成 fallback ID。暴露长上下文场景下消息序列化的脆弱性。 |
| [#5117](https://github.com/earendil-works/pi/issues/5117) | Qwen 3.7 Max on OpenRouter is broken | **OPEN** | **多模态角色定义兼容性**：`developer` 角色不被 OpenRouter 接受，反映 Qwen 系列模型在系统提示角色分配上的非标准扩展，影响多模态对话框架的互操作性。 |
| [#4955](https://github.com/earendil-works/pi/issues/4955) | Add provider-hosted tools support | **CLOSED** | **工具执行架构与对齐**：提供商侧工具（如 Perplexity 搜索、Google 地图）与本地工具执行器的分离，涉及工具调用链的信任边界、延迟差异与幻觉风险分配。 |
| [#5132](https://github.com/earendil-works/pi/issues/5132) | System prompt lists exploration tools that aren't registered | **CLOSED** | **系统提示与工具能力对齐**：硬编码的"优先使用 grep/find/ls"指南与实际注册工具不匹配，导致模型产生对不存在工具的幻觉性依赖，属于典型的指令-能力错位。 |
| [#5040](https://github.com/earendil-works/pi/issues/5040) | PI_CODING_AGENT_SESSION_DIR forces flat storage | **OPEN** | **长会话组织结构**：扁平存储破坏按工作目录的会话作用域隔离，长程 coding agent 任务的历史检索与上下文恢复效率下降。 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 状态 | 技术贡献 |
|---|------|------|----------|
| [#5118](https://github.com/earendil-works/pi/pull/5118) | fix(ai): buffer reasoning_details that arrive before tool_calls | **CLOSED** | **推理-工具调用时序修复**：OpenRouter 等提供商在 `tool_calls` chunk 前流式传输 `reasoning_details`（含加密思维签名），原逻辑因 ID 查找失败静默丢弃签名。PR 引入缓冲机制保障推理链完整性，**直接防止工具调用推理痕迹的丢失导致的幻觉不可检测**。 |
| [#4971](https://github.com/earendil-works/pi/pull/4971) | Add allowEmptySignature compat option for Anthropic-compatible providers | **CLOSED** | **推理缓存与提示稳定性**：空 `thinkingSignature` 导致 thinking block 被重写为纯文本，破坏 prompt caching 并触发 400 错误。兼容性选项保留空签名，**维护长上下文中的推理一致性**。 |
| [#4978](https://github.com/earendil-works/pi/pull/4978) + [#5107](https://github.com/earendil-works/pi/pull/5107) | feat(coding-agent): expose streamingBehavior to input events | **CLOSED** | **流式推理行为显式化**：扩展可区分 idle prompt / mid-stream steer / queued follow-up 三种状态，为**人机协同推理中的干预时机**提供结构化信号，支持对齐研究中的实时反馈机制。 |
| [#5088](https://github.com/earendil-works/pi/pull/5088) | feat(coding-agent): collapse grouped tool calls | **OPEN** | **工具调用模式抽象**：实验性工具调用分组，潜在支持复合工具操作的语义压缩，**降低长程任务中工具调用历史的上下文膨胀**。 |
| [#5029](https://github.com/earendil-works/pi/pull/5029) | fix(coding-agent): abort in-flight LLM call on AgentSession.dispose() | **CLOSED** | **推理资源与状态一致性**：session 切换/销毁时未终止进行中的 LLM HTTP 请求，导致**幽灵推理流**与后续会话的上下文污染。 |
| [#5115](https://github.com/earendil-works/pi/pull/5115) | fix(coding-agent): drain follow-ups queued during agent_end | **CLOSED** | **推理链尾部处理**：`agent_end` 期间入队的 follow-up 因未指定 `deliverAs` 而阻塞至下一条用户消息，修复**自主推理循环的闭环完整性**。 |
| [#5139](https://github.com/earendil-works/pi/pull/5139) | fix(coding-agent): file review diff empty root cause fix | **CLOSED** | **长上下文 GC 与内容完整性**：子 agent GC 误删主会话依赖的 blob 对象，导致文件评审 diff 返回 null。重写 `InternalGit.gc()` 的 tree 保护逻辑，**保障代码审查场景下的长程引用稳定性**。 |
| [#5085](https://github.com/earendil-works/pi/pull/5085) | Expose full tool definitions from getAllTools | **CLOSED** | **工具模式透明度**：向扩展开放完整工具定义（只读），支持工具调用的可解释性分析与**工具描述幻觉**的检测。 |
| [#5140](https://github.com/earendil-works/pi/pull/5140) | Extension API additions for non-TUI remote clients | **CLOSED** | **多模态交互架构**：为远程客户端（手机、Web 桥接）暴露 `executeInputLine`、`watchPrompt` 等 API，支撑**非文本模态的输入事件流**与跨设备推理同步。 |
| [#5110](https://github.com/earendil-works/pi/pull/5110) | Add Ant-ling Provider with Ling-2.6-1T, Ling-2.6-flash & Ring-2.6-1T | **OPEN** | **大规模语言模型接入**：1T 参数级模型的兼容性适配层，涉及超长上下文（1M+）的流式处理与**大模型推理稳定性**验证。 |

---

## 5. 研究方向信号

| 趋势 | 证据 |
|------|------|
| **长上下文"标称 vs 实际"鸿沟** | #5087（1M→272K 截断）、#5149（长对话 ID 冲突）显示上下文窗口的标称值与实际工程实现存在系统性差距，需建立**上下文预算的精确审计机制** |
| **推理链的流式时序脆弱性** | #5118、#5106、#4801 集中暴露 reasoning_content / thinkingSignature / reasoning_effort 在流式传输中的丢失、错位、兼容性问题，**推理可追溯性**成为关键需求 |
| **跨提供商推理历史互操作** | #5148（Claude↔OpenAI 会话恢复）、#5117（Qwen 角色定义差异）反映多模型生态中**推理序列标准化**的缺失 |
| **工具调用作为幻觉源** | #5132（未注册工具被提示）、#5085（工具定义透明化）指向系统提示与工具能力不匹配引发的**指令幻觉** |
| **自主推理循环的工程闭环** | #5115、#5029 关注 agent 生命周期中的推理状态管理，**自我修正与终止条件**的可靠性待加强 |

---

## 6. 技术局限性

| 限制领域 | 具体表现 | 研究空白 |
|----------|----------|----------|
| **流式协议状态同步** | TUI "Working..." 假死（#4945）、tmux 内联图像失效（#5098）、SIGTERM 清理不全（#5080） | 缺乏**流式响应的正式状态机模型**，客户端-服务端在长时间推理中的心跳/超时/恢复机制不明确 |
| **消息 ID 生成策略** | 多轮后 fallback ID 冲突（#5149）、跨提供商 ID 空间碰撞（#5148） | 需要**分布式会话的因果标识方案**，而非简单的索引或前缀 |
| **推理内容格式碎片化** | reasoning_content / reasoning_details / thinkingSignature / reasoning_effort 等字段语义重叠且提供商实现各异 | 缺乏**思维链表示的统一抽象层**，阻碍跨模型幻觉检测工具的开发 |
| **上下文窗口动态管理** | 静态截断（#5087）、扁平存储（#5040） | 需要**任务感知的上下文分层压缩**，而非简单的 token 计数或目录结构 |
| **工具-提示对齐验证** | 硬编码提示与实际工具注册脱节（#5132） | 缺少**系统提示与工具模式的形式化一致性检查**机制 |

</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

# Qwen Code 研究动态摘要 | 2026-05-29

## 1. 今日速览

今日核心研究动态聚焦于**长上下文推理架构重构**与**幻觉缓解机制**：社区提出以 Claude Code 风格的"全历史摘要+恢复附件"模型替代传统的尾保留压缩策略（#4592/#4599），同时针对长会话中的无界内存增长问题持续优化历史管理机制（#2128）。此外，daemon 模式的遥测对齐与工具链路追踪为 post-training 阶段的系统可靠性评估提供了基础设施支撑。

---

## 2. 版本发布

**v0.16.1-nightly.20260528.34b7d472e**

- 仅包含 CLI 启动警告输出修复（stderr 前置）与 TUI 间距密度调整的终端录屏证据，**无直接研究相关更新**。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 | 链接 |
|---|------|---------|------|
| **#4592** | refactor(core): replace tail-preservation compaction with "summary + restoration attachments" model | **长上下文推理核心重构**：放弃按字符数分割的 70/30 压缩策略，改为全历史侧查询摘要+结构化恢复附件，直接影响长程依赖保留与推理一致性，是上下文窗口管理的范式迁移 | [Issue](https://github.com/QwenLM/qwen-code/issues/4592) |
| **#2128** | Memory grows unboundedly during long sessions — UI History accumulates without limit | **长上下文可靠性**：数十小时会话中 `useHistoryManager.history` 无界增长导致 OOM，暴露当前历史压缩与内存释放机制的设计缺陷，需结合 #4592 的压缩重构协同解决 | [Issue](https://github.com/QwenLM/qwen-code/issues/2128) |
| **#3004** | [P1] API Exponential Backoff & Fallback Retry | **Post-training 对齐/系统可靠性**：缺乏指数退避、529 降级重试与 token 刷新机制，影响长推理链的稳定性与对齐反馈回路的完整性 | [Issue](https://github.com/QwenLM/qwen-code/issues/3004) |
| **#3696** | Comprehensive hot-reload system for skills, extensions, MCP, and configuration | **Post-training 对齐基础设施**：运行时热重载能力支持快速迭代对齐策略与工具定义，减少反馈循环延迟，对 RLHF/RLAIF 风格的在线调优至关重要 | [Issue](https://github.com/QwenLM/qwen-code/issues/3696) |
| **#3712** | Refactor: merge IDE context into user message instead of separate API history entries | **长上下文推理优化**：将 IDE 上下文从独立 history entries 合并至用户消息，减少 API 历史膨胀，改善长会话中的上下文利用效率与推理聚焦度 | [Issue](https://github.com/QwenLM/qwen-code/issues/3712) |
| **#4604** | API Error: terminated (cause: Body Timeout Error) | **长推理链可靠性**：处理网页等长内容时 body timeout，暴露当前流式传输与长生成超时配置的不足，制约长上下文任务的完成率 | [Issue](https://github.com/QwenLM/qwen-code/issues/4604) |
| **#4582** | [Daemon] POST /prompt should be non-blocking — decouple trigger from completion | **异步推理基础设施**：同步阻塞设计导致长 agentic 循环（模型推理+工具执行+多步）与基础设施超时冲突，需异步化以支撑复杂长程推理工作流 | [Issue](https://github.com/QwenLM/qwen-code/issues/4582) |
| **#4579** | fix(rewind): false "compressed turn" error when mid-turn messages exist | **幻觉缓解/状态一致性**：工具执行中用户消息导致的回退误报，暴露压缩状态与交互状态的同步漏洞，可能引发用户侧对系统可靠性的认知偏差 | [Issue](https://github.com/QwenLM/qwen-code/issues/4579) |
| **#4597** | feat(stats): 增强stats能力，支持跨session的全局用量统计 | **Post-training 评估基础设施**：跨会话持久化用量追踪为长上下文推理的成本-效益分析、模型行为审计与对齐效果评估提供数据基础 | [Issue](https://github.com/QwenLM/qwen-code/issues/4597) |
| **#3658** | Deepseek v4: API Error: 400 The reasoning_content in the thinking mode must be passed back | **推理链完整性/幻觉风险**：reasoning_content 回传机制缺失导致外部推理模型集成失败，影响思维链可见性与推理过程的可审计性 | [Issue](https://github.com/QwenLM/qwen-code/issues/3658) |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 | 链接 |
|---|------|---------|------|
| **#4599** | refactor(core)!: replace tail-preservation compaction with summary + restoration attachments | **长上下文推理架构**：实现 Claude Code 风格压缩，全历史摘要替代 70/30 分割，附加上下文恢复附件，显著提升长程依赖保留与推理连贯性 | [PR](https://github.com/QwenLM/qwen-code/pull/4599) |
| **#4598** | fix(tui): Make thinking output transient | **推理过程可视化/幻觉缓解**：将思维输出从持久化改为瞬态，配置 `ui.thinkingDisplayMode`（preview/loading），减少推理噪声对用户判断的干扰，同时保留思维链调试能力 | [PR](https://github.com/QwenLM/qwen-code/pull/4598) |
| **#4608** | feat(telemetry): add tool spans and session.id to daemon/ACP path | **Post-training 可观测性**：补全 daemon 路径的 `session.id`、`tool`、`tool.execution` span，使 ARMS 可按会话查询，支撑工具调用可靠性评估与对齐调试 | [PR](https://github.com/QwenLM/qwen-code/pull/4608) |
| **#4556** | feat(telemetry): trace daemon prompt lifecycle | **对齐基础设施**：OpenTelemetry 跨 HTTP 路由、ACP bridge、子 prompt 执行的全链路传播，为长程 agentic 循环的延迟分析与故障定位提供追踪基础 | [PR](https://github.com/QwenLM/qwen-code/pull/4556) |
| **#4610** | feat(daemon): add POST /session/:id/btw endpoint for side questions | **长上下文交互**：`/btw` 旁路提问的 daemon HTTP 化，支持不中断主会话的侧查询，提升长会话中的信息检索效率与上下文管理灵活性 | [PR](https://github.com/QwenLM/qwen-code/pull/4610) |
| **#4242** | fix(cli): map rewind turns after compression | **压缩后推理一致性**：压缩摘要折叠早期用户轮次后的回退映射修正，确保 ACP 模型面向轮次计数、历史快照与恢复回滚的准确性，防止状态幻觉 | [PR](https://github.com/QwenLM/qwen-code/pull/4242) |
| **#4605** | fix(core): disable undici 300s bodyTimeout for no-proxy Node.js path | **长生成可靠性**：本地 LLM 后端（LM Studio/MLX/Ollama）无代理场景下 300s body timeout 禁用，解除长推理/长生成任务的硬性时间限制 | [PR](https://github.com/QwenLM/qwen-code/pull/4605) |
| **#4595** | fix(tui): Tighten message and tool spacing | **多模态交互密度**：TUI 消息与工具间距收紧，提升长会话中的信息扫描效率，不改变内容/颜色/边框/思维可见性等核心推理相关配置 | [PR](https://github.com/QwenLM/qwen-code/pull/4595) |
| **#4590** | feat(computer-use): zero-config built-in via open-computer-use MCP | **多模态推理扩展**：零配置内置 Computer Use（9 工具覆盖 macOS/Windows/Linux），将视觉-动作循环纳入 agentic 推理，扩展多模态任务空间 | [PR](https://github.com/QwenLM/qwen-code/pull/4590) |
| **#4570** | feat(skill): add /triage skill for AI-native PR intake and issue triage | **自动化对齐/质量门控**：AI 原生 PR 准入与 issue 分类技能，整合预检分类、审查规则，可作为推理质量与对齐策略的自动化评估入口 | [PR](https://github.com/QwenLM/qwen-code/pull/4570) |

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究意义 |
|------|------|---------|
| **上下文压缩范式迁移** | #4592/#4599 提出全历史摘要+恢复附件替代尾保留 | 从"保近弃远"的启发式压缩转向语义完整的结构化摘要，可能改善长程依赖推理与事实一致性 |
| **长会话内存与状态管理** | #2128 无界增长、#4582 异步化、#3712 IDE 上下文合并 | 工程层面密集优化支撑超长上下文（数十小时、千级轮次）的可行性，接近"无限记忆"产品承诺 |
| **推理过程可控可见性** | #4598 思维输出瞬态化、#4376 PermissionDenied hooks | 在透明性与干扰之间寻求平衡，PermissionDenied 的结构化反馈可用于 RLHF 奖励建模 |
| **Daemon 模式可靠性基建** | #4608/#4556 遥测补全、#4606 请求级日志、#4610 旁路查询 | 为 post-training 阶段的系统级评估、A/B 测试与对齐效果量化提供工程基础 |
| **多模态 Agent 扩展** | #4590 Computer Use 内置、#4591 零配置安装 | 视觉-动作循环纳入核心推理路径，但当前未涉及 OCR/HMER 专用能力，视觉理解仍依赖外部模型 |

---

## 6. 技术局限性

| 限制 | 表现 | 研究空白 |
|------|------|---------|
| **长生成超时硬边界** | #4604 body timeout 300s（#4605 局部修复仅覆盖 no-proxy） | 缺乏自适应超时机制，未区分网络延迟与模型生成时间，长推理链仍可能中断 |
| **压缩状态同步漏洞** | #4579 误报"compressed turn"、#4242 回退映射复杂 | 压缩与交互状态的并发管理缺乏形式化验证，可能引发不可复现的状态不一致 |
| **推理链外部依赖脆弱性** | #3658 DeepSeek reasoning_content 回传、#3004 降级缺失 | 对外部模型推理格式的强依赖，缺乏协议抽象层，跨模型对齐困难 |
| **视觉-语言能力边界** | #4590 Computer Use 聚焦 GUI 自动化，无 OCR/HMER 专用管道 | 代码场景中的公式、图表、手写体识别仍依赖通用多模态模型，无针对性优化 |
| **评估数据闭环缺失** | #4597 stats 持久化刚起步，无自动化的推理质量标注回流 | 长上下文推理的错误模式缺乏系统性收集，制约针对性微调与幻觉缓解 |

---

*摘要基于 GitHub 公开数据生成，聚焦长上下文推理、OCR/HMER、多模态推理、post-training 对齐、幻觉缓解五大研究方向。*

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

# DeepSeek TUI 研究动态摘要 | 2026-05-29

---

## 1. 今日速览

今日无新版本发布，但社区对**多模型/多模态支持**和**长上下文可靠性**的需求显著升温。Issue #2300 明确提出需要同时配置多个模型（含视觉、OCR、向量化模型）并实现自动路由，而 #2317 暴露了超长回复（18分钟）导致会话阻塞的上下文管理缺陷。PR 侧聚焦**工具调用一致性**（#2331 预加载 shell 工具集）与**输入层多语言可靠性**（#2330 修复 IME 中文输入路由），显示工程层面对多模态交互基础的持续加固。

---

## 2. 版本发布

无新版本发布。

---

## 3. 研究相关 Issues

| # | 标题 | 状态 | 研究价值 |
|---|------|------|---------|
| [#2300](https://github.com/Hmbown/CodeWhale/issues/2300) | 兼容多模型支持 | OPEN | **核心多模态基础设施需求**。用户要求同时配置多个模型（OpenAI/vLLM 格式）、视觉模型、OCR 模型、向量化模型，并按需自动路由。直接关联 OCR/HMER 与多模态推理方向，但当前架构仅支持单 provider 切换。 |
| [#2317](https://github.com/Hmbown/CodeWhale/issues/2317) | 超长回复阻塞后续输入 | OPEN | **长上下文推理可靠性**。18分钟长任务导致 UI 锁死，暴露流式生成中的上下文窗口管理、进度反馈与交互连续性缺陷，对长文档/代码生成场景至关重要。 |
| [#1747](https://github.com/Hmbown/CodeWhale/issues/1747) | Cache hit problem | OPEN | **推理效率与上下文复用**。用户反馈难以跟踪 Agent 执行过程，暗示 KV-cache 复用机制与流式展示之间存在张力，影响长对话中的推理成本与用户体验。 |
| [#2323](https://github.com/Hmbown/CodeWhale/issues/2323) | 未适配中文输入法 | OPEN | **多语言输入层与多模态交互**。IME 拼音提示未隐藏、字母误注入输入区，属于视觉-语言交互的基础缺陷，对 CJK 用户的多模态输入体验构成系统性障碍。 |
| [#2328](https://github.com/Hmbown/CodeWhale/issues/2328) | exec_shell 模式可用性不一致 | OPEN | **工具调用对齐与模式一致性**。同一工具在 YOLO/Agent 模式表现不一，暴露工具目录（tool catalog）与模式标志的耦合缺陷，影响 Agent 推理的确定性。 |
| [#2303](https://github.com/Hmbown/CodeWhale/issues/2303) | allow_shell 安全门控不完整 | OPEN | **Agent 安全性与对齐**。`task_shell_start` 绕过 `allow_shell` 默认 false 的限制，属于安全策略与工具实现对齐失败，对可控 AI/对齐研究有警示意义。 |
| [#1675](https://github.com/Hmbown/CodeWhale/issues/1675) | Agent 实时输出中文乱码 | OPEN | **多语言渲染与编码可靠性**。Obsidian/Word 内容生成场景下的编码问题，涉及终端渲染层与模型输出层的跨模态一致性。 |
| [#2247](https://github.com/Hmbown/CodeWhale/issues/2247) | 支持自定义 DeepSeek 兼容 API 提供商 | OPEN | **模型后训练与本地部署对齐**。支持第三方/本地部署的 DeepSeek 兼容端点，为模型微调、RLHF 后训练模型的接入提供基础设施。 |
| [#1615](https://github.com/Hmbown/CodeWhale/issues/1615) | docker 拉取直接跑乱码 | CLOSED | **部署层编码可靠性**。虽为用户情绪激烈的报告，但乱码问题与终端编码检测、locale 传播机制相关，对跨平台多语言部署有参考价值。 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|---------|
| [#2331](https://github.com/Hmbown/CodeWhale/pull/2331) | fix(tools): eagerly load all exec_shell companion tools | **工具调用可靠性**。将 6 个 shell 伴生工具预加载至 `DEFAULT_ACTIVE_NATIVE_TOOLS`，解决 Agent 模式下工具目录不完整导致的 "Tool not available" 错误，提升多步推理中工具链的确定性。 |
| [#2330](https://github.com/Hmbown/CodeWhale/pull/2330) | fix(tui): route IME-committed Chinese characters directly to composer | **多语言输入层修复**。绕过 bracketed paste 缺失环境下的 paste-burst 启发式误判，将 IME 提交字符直接路由至 composer，消除中文输入"无显示"现象，对 CJK 多模态交互至关重要。 |
| [#2326](https://github.com/Hmbown/CodeWhale/pull/2326) | feat: enforce allowed tools for custom slash commands | **Agent 可控性与对齐**。为自定义 slash 命令引入 `allowed-tools` frontmatter 约束，是"受限工具集"对齐策略的落地，防止未授权工具调用导致的推理偏离。 |
| [#2318](https://github.com/Hmbown/CodeWhale/pull/2318) | feat(hooks): allow message_submit to transform submitted text | **输入层对齐与干预**。实现可变 `message_submit` hooks，支持通过 stdout JSON 替换提交文本或阻断提交（exit code 2），为 prompt 注入检测、内容过滤等后训练对齐机制提供扩展点。 |
| [#2325](https://github.com/Hmbown/CodeWhale/pull/2325) | fix: approval dialog shows empty params | **工具调用透明度**。修复审批对话框因 `pending_tool_uses` 提前 drain 而显示空参数的问题，提升人机协同中的可解释性与信任度。 |
| [#2320](https://github.com/Hmbown/CodeWhale/pull/2320) | fix(i18n): localize right-click context menu | **多语言 UI 一致性**。补齐右键菜单的本地化链路，消除非英语 locale 下的语言混杂，对多语言用户研究场景的体验控制有意义。 |
| [#2316](https://github.com/Hmbown/CodeWhale/pull/2316) | fix(composer): allow slash-space messages | **输入歧义消除**。将 `/ `（斜杠+空格）重新分类为普通消息而非命令，减少用户意图与解析器的对齐误差。 |
| [#2324](https://github.com/Hmbown/CodeWhale/pull/2324) | fix(statusline): keep picker selection visible | **长列表导航可靠性**。修复终端高度不足时光标行被裁剪的滚动问题，属于复杂 UI 状态下的交互确定性改进。 |
| [#2302](https://github.com/Hmbown/CodeWhale/pull/2302) | fix(tui): replace standalone compacting label with animated working label | **长时操作反馈**。为 compacting 阶段添加动画与耗时显示，缓解用户对长时间无反馈操作的"挂起"幻觉。 |
| [#2329](https://github.com/Hmbown/CodeWhale/pull/2329) | fix(tui): skip hidden worktrees in workspace discovery | **上下文管理效率**。排除隐藏 git worktrees 的遍历，防止子 Agent 并发时的 I/O 饱和与 TUI 卡顿，对多 Agent 长上下文场景的性能稳定性有直接增益。 |

---

## 5. 研究方向信号

| 趋势 | 证据 | 研究含义 |
|------|------|---------|
| **多模型/多模态架构需求迫切** | #2300 明确要求视觉、OCR、向量化多模型并行与自动路由 | 当前单 provider 架构将成为瓶颈，需研究模型编排（model orchestration）与动态路由策略 |
| **长上下文交互断裂** | #2317（18分钟阻塞）、#1747（cache 可见性） | 流式生成中的进度感知、可中断性与上下文续接机制需系统性改进 |
| **工具调用确定性不足** | #2328（模式不一致）、#2303（安全绕过）、#2331（预加载修复） | Agent 推理的可靠性高度依赖工具目录的一致性，需强化工具-模式绑定与权限对齐 |
| **CJK 输入作为多模态基础设施** | #2323、#2330、#1675、#1615 集中爆发 | IME 处理不仅是本地化问题，而是文本-视觉交互的底层通道，影响所有多模态输入场景 |
| **用户可控性与幻觉缓解** | #2326（工具白名单）、#2318（提交变换 hooks）、#2325（参数透明度） | 社区正从"功能实现"转向"可控生成"，与 post-training 对齐、RLHF 部署后的行为约束形成呼应 |

---

## 6. 技术局限性

| 限制领域 | 具体表现 | 研究空白 |
|---------|---------|---------|
| **多模型并行架构缺失** | 仅支持单 provider 切换，无视觉/OCR/向量模型并行能力 | 缺乏模型路由策略、多模态注意力调度、跨模态缓存共享机制 |
| **长上下文会话管理脆弱** | 超长生成阻塞 UI、无进度中断/续接机制 | 流式生成的用户级 checkpoint、增量上下文压缩、交互式 backpressure 控制 |
| **工具-模式耦合不一致** | 同一工具在不同模式可用性不同，安全策略存在绕过路径 | 工具目录的形式化验证、模式感知的权限推理、动态工具沙箱 |
| **IME/编码层系统性缺陷** | 中文输入在多场景（Docker/终端/Agent 输出）出现乱码或丢失 | 终端能力协商（bracketed paste、focus event）的跨平台抽象层不完善 |
| **Agent 可解释性断层** | 审批对话框参数丢失、执行过程难以跟踪 | 工具调用链的实时可视化、中间状态持久化与恢复（如 #2306 的 trophy cards 初步尝试） |

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*