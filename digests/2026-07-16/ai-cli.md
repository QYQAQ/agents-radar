# AI CLI 工具社区动态日报 2026-07-16

> 生成时间: 2026-07-16 00:23 UTC | 覆盖工具: 9 个

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

# AI CLI 工具研究动态横向对比分析报告（2026-07-16）

## 1. 生态全景

当前 AI CLI 工具已明显从“单轮代码补全”向“长上下文 Agent 平台”演进：社区关注焦点集中在**上下文预算管理、子代理编排、推理透明度与工具安全**四个维度。过去 24 小时内，主流仓库（Claude Code、OpenAI Codex、OpenCode、GitHub Copilot CLI、Qwen Code、Pi、DeepSeek TUI）均出现了与研究相关的 Issue 或 PR，其中**长上下文压缩/溢出、多 Agent 通信、reasoning/thinking 块处理**是最突出的共性痛点。与此同时，多模态/OCR/HMER 方向在当前 sprint 中并未成为热点，仅在语音 ASR、浏览器截图、GUI 自动化等少数链路出现相关信号。整体来看，社区正努力把“模型能力”转化为“系统级 harness、缓存、记忆与评测基础设施”。

---

## 2. 各工具活跃度对比

| 工具 | 研究相关 Issues | 研究相关 PR | 今日版本/发布 | 核心关键词 |
|---|---|---|---|---|
| **Claude Code** | 10 | 4（无直接相关） | v2.1.211 | 子代理透明化、权限预览、长上下文压缩、嵌套通信 |
| **OpenAI Codex** | 6 | 8 | 无研究相关发布 | prompt cache、子代理分页历史、外部记忆迁移 |
| **Gemini CLI** | — | — | 摘要生成失败 | 无可用数据 |
| **GitHub Copilot CLI** | 9 | 0 | v1.0.71-3 | 语音 ASR、1M 上下文、工具输出污染、reasoning 可见性 |
| **Kimi Code CLI** | 0 | 1（telemetry） | 无 | 无研究方向信号 |
| **OpenCode** | 9 | 6 | v1.18.2 | 上下文溢出检测、图像归一化、子代理深度、模型幻觉 |
| **Pi** | 7 | 4 | 无 | 会话压缩、thinking 块、XML 工具解析、流式可靠性 |
| **Qwen Code** | 7 | 0 | cua-driver-rs v0.7.2 | 长上下文效率、安全分类器、tool-call 解析、CUA/GUI 自动化 |
| **DeepSeek TUI** | 10 | 0 | 无 | KV cache 持久化、LLM-as-judge、多 Agent 合成/归约 |

> 注：Issues/PR 数为“研究相关”（长上下文、OCR/HMER、多模态、post-training 对齐、幻觉缓解）口径；Gemini CLI 当日数据缺失。

---

## 3. 共同关注的功能方向

| 共同方向 | 涉及工具 | 社区具体诉求 |
|---|---|---|
| **长上下文/上下文预算管理** | Claude Code、OpenAI Codex、Copilot CLI、OpenCode、Pi、Qwen Code、DeepSeek TUI | Claude Code 的 `/compact` 丢失系统指令、OpenCode 的 overflow 检测跨步延迟、Copilot CLI 二进制 diff 污染历史、Codex 的 cache write token 追踪、Pi 的 compaction 失败即中断、Qwen 的 managed memory 配置失效、DeepSeek TUI 的持久化 KV cache 胶囊 |
| **多 Agent 编排与通信** | Claude Code、OpenAI Codex、OpenCode、Qwen Code、DeepSeek TUI | Claude Code 的嵌套 agent 通信失效、Codex 的子代理分页历史继承、OpenCode 的子代理深度限制、Qwen 的 subagent 通信薄弱、DeepSeek TUI 的 WhaleFlow swarm 合成/归约 |
| **推理透明度与可控性** | Copilot CLI、OpenAI Codex、Pi、Qwen Code | Copilot CLI 的 Codex 5.3 缺少 reasoning 输出、Codex 的 `reasoning.effort=max` 被后端拒绝、Pi 的 thinking 块解析/渲染、Qwen 的 `</think>` 关闭标签解析 |
| **工具/MCP 安全与信任** | Claude Code、OpenAI Codex、Copilot CLI、Qwen Code、DeepSeek TUI | Claude Code 的权限预览对抗清洗、Codex 的 JSON schema 被工具静默忽略、Copilot CLI 的 MCP 空 user 消息污染、Qwen 的安全分类器 fail-closed、DeepSeek TUI 的审批弹窗查看 reasoning 与 judge 裁判 |
| **多模态（语音/图像/GUI）可靠性** | Copilot CLI、Claude Code、OpenCode、Qwen Code | Copilot CLI 的 ASR 静默失败、Claude Code 的浏览器截图超时、OpenCode 的图像 Base64 导致 413、Qwen 的 cua-driver-rs 多模态 GUI 驱动 |

---

## 4. 差异化定位分析

| 工具 | 功能侧重 | 目标用户 | 技术路线 |
|---|---|---|---|
| **Claude Code** | 企业级 Agent 编排、安全提示清洗、子代理透明化 | 企业开发者、安全敏感场景 | 以 Anthropic 模型为中心，强调权限预览、技能（skills）系统与嵌套 Agent 治理 |
| **OpenAI Codex** | 多 Agent 记忆继承、外部记忆迁移、工具/技能统一 | 中大型工程团队、OpenAI 生态 | 强依赖 `world state`、host skill、MCP connector，推进“可迁移的跨会话记忆” |
| **GitHub Copilot CLI** | 终端原生体验、语音输入、超长上下文（1M） | 终端重度用户、GitHub Copilot 订阅者 | 与 Copilot/CAPI 后端深度集成，关注终端兼容性与多模态语音 |
| **OpenCode** | 多模型支持、上下文溢出防御、图像归一化 | 开源多模型用户、第三方模型尝鲜者 | 插件化系统提示路由、Provider 默认参数、V2 子代理深度控制 |
| **Pi** | 长会话记忆结构、session JSONL 持久化、thinking 块解析 | 长期会话研究者、Agent 平台构建者 | SQLite 存储、retainedTail 树路径、分支摘要 token 元数据 |
| **Qwen Code** | 中文/多语言模型、安全分类器、计算机使用代理（CUA） | 中文开发者、GUI 自动化用户 | 自研 cua-driver-rs、强制 `tool_choice`、安全审批与工具解析并重 |
| **DeepSeek TUI** | 模型专属缓存策略、KV cache 持久化、开放微调/评测闭环 | 模型研究者、开源对齐团队 | Model Lab、轨迹导出、LLM-as-judge、WhaleFlow shared-memo |
| **Kimi Code CLI** | 当日无研究方向信号 | — | 数据未显示活跃研究动向 |
| **Gemini CLI** | 数据缺失 | — | 摘要生成失败，无法评估 |

---

## 5. 社区热度与成熟度

- **高活跃且研究密集**：**Claude Code**（10 条研究 Issue + 发布）与 **OpenCode**（9 Issue + 6 PR + 发布）处于快速迭代期，问题覆盖面广，社区反馈与代码改动同步推进。
- **工程深度强**：**OpenAI Codex**（8 PR）持续在 prompt cache、历史继承、world state 等底层机制上投入，偏向平台化与记忆架构。
- **垂直场景活跃**：**GitHub Copilot CLI**（9 Issue）和 **Qwen Code**（7 Issue + CUA 驱动发布）分别在终端多模态、GUI 自动化上形成鲜明标签。
- **基础设施探索期**：**Pi**（7 Issue + 4 PR）和 **DeepSeek TUI**（10 Issue，0 PR）仍偏“想法/需求”阶段，PR 落地较少，但议题前沿（KV cache 持久化、LLM-as-judge）。
- **低活跃/数据缺失**：**Kimi Code CLI** 当日无研究方向信号；**Gemini CLI** 摘要生成失败，无法评估。

---

## 6. 值得关注的趋势信号

1. **长上下文已从“模型窗口竞赛”转向“系统级预算工程”**  
   社区不再单纯追求 1M token，而是聚焦 **overflow 检测、压缩时机、跨步 token 统计、工具输出回注、图像 Base64 治理、KV cache 持久化**。对开发者而言，构建 Agent 时需要优先考虑“上下文会计”与“缓存策略”，而非盲目堆叠上下文长度。

2. **多 Agent 通信是下一个瓶颈**  
   从 Claude Code 的嵌套通信失败、Codex 的子代理分页历史继承，到 OpenCode 的子代理深度限制、DeepSeek TUI 的 swarm 合成归约，行业正在从“单个 Agent 调用”走向“分布式多 Agent 协调”。建议提前设计 Agent 间的状态传递、失败重试与角色交接机制。

3. **推理透明度成为信任基础**  
   多个仓库（Copilot CLI、Codex、Pi、Qwen Code、DeepSeek TUI）都在处理 reasoning/thinking 输出可见性或解析鲁棒性问题。对高风险的代码/工具执行场景，**让人类在审批前查看 CoT/执行计划**将成为安全对齐的标配。

4. **工具/MCP 生态需要更强的 schema 与信任治理**  
   JSON schema 被静默忽略、MCP namespace 包装、安全分类器 fail-closed、untrusted MCP 绕过确认等问题频发，说明工具增强型 Agent 的**幻觉与权限边界**仍不稳定。建议引入显式工具 schema 校验、权限 profile 与 LLM-as-judge 复核。

5. **OCR/HMER 与多模态视觉尚未成为 CLI 工具热点**  
   除 Copilot CLI 语音 ASR、Claude Code 截图、Qwen CUA 驱动、OpenCode 图像归一化外，未见手写数学表达式识别或文档视觉理解相关研究信号。若面向教育、科研或工程图纸场景，**OCR/HMER 仍是一个相对空白且可切入的差异化方向**。

6. **开放对齐/评测基础设施正在成型**  
   DeepSeek TUI 的 Model Lab、轨迹导出、LLM-as-judge，Codex 的外部记忆迁移，OpenCode 的模型专属系统提示，标志着 CLI 工具从“消费模型”转向“可审计、可评测、可微调”的开放工作流。开发者应开始关注如何从真实会话中构建训练/评测数据闭环。

---

## 各工具详细报告

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills 社区热点

> 数据来源: [anthropics/skills](https://github.com/anthropics/skills)

# Claude Code Skills 社区热点报告
*数据截止：2026-07-16*

---

## 1. 热门 Skills 排行（按社区关注度与讨论热度）

| # | Skill | 功能简述 | 讨论热点 | 状态 |
|---|-------|----------|----------|------|
| 1 | **skill-creator 评估修复** | 修复 `run_eval.py` 恒报 `recall=0%`、Windows 子进程/编码/管道读取、触发检测与并行 worker 问题 | 直接回应 Issue #556 / #1169 / #1061，多个独立复现，是当前最影响创作者体验的阻塞性 Bug | OPEN |
| 2 | **run_eval 触发检测修复** | 修正 `run_single_query` 中技能名识别与首个非 Skill 工具即退出的逻辑 | 同样是 recall=0% 根因之一，与 #1298 互补 | OPEN |
| 3 | **document-typography** | 为 AI 生成文档做排版质量控制：孤行、寡行、编号错位等 | 几乎所有 Claude 生成的文档都受影响，用户却很少主动要求排版 | OPEN |
| 4 | **odt** | 创建、填充、读取、转换 OpenDocument（ODT/ODS）文件 | 面向开源/ISO 标准文档、LibreOffice 生态 | OPEN |
| 5 | **self-audit** | 先机械验证输出文件，再按伤害严重程度做四维推理质量审计 | 通用型“输出前质检”Skill，与推理增强/安全对齐高度相关 | OPEN |
| 6 | **skill-quality-analyzer & skill-security-analyzer** | 元 Skill：从结构文档、示例、资源等维度评估 Skill 质量与安全 | 社区对 Marketplace 技能治理与信任边界的直接回应 | OPEN |
| 7 | **testing-patterns** | 覆盖测试哲学、单元测试、React 组件测试、集成/契约测试等全栈测试模式 | 代码智能体场景下测试生成与质量保障需求强劲 | OPEN |
| 8 | **color-expert** | 颜色命名系统、色彩空间选型与视觉设计任务指导 | 面向视觉/多模态设计工作流 | OPEN |

**链接：**
- #1298：https://github.com/anthropics/skills/pull/1298
- #1323：https://github.com/anthropics/skills/pull/1323
- #514：https://github.com/anthropics/skills/pull/514
- #486：https://github.com/anthropics/skills/pull/486
- #1367：https://github.com/anthropics/skills/pull/1367
- #83：https://github.com/anthropics/skills/pull/83
- #723：https://github.com/anthropics/skills/pull/723
- #1302：https://github.com/anthropics/skills/pull/1302

---

## 2. 社区需求趋势（从 Issues 提炼）

- **安全与信任边界**：社区技能借用 `anthropic/` 命名空间造成身份冒用风险（#492），企业 SharePoint 文档访问控制（#1175），以及 Agent 治理/安全模式（#412）成为高频议题。
- **Skill 质量与推理门控**：`self-audit`（#1367）和“三阶段推理质量门控”（#1385）反映社区希望模型输出经过“可验证、可审计、分阶段”检查。
- **Skill 创作与评估工具链**：`skill-creator` 的 `run_eval.py` 报告失真（#556、#1169）、Windows 兼容性（#1061）以及工具链本身应遵循最佳实践（#202）是开发者最痛的阻塞点。
- **文档与办公格式**：对 DOCX/ODT/PDF 的生成、排版与元数据修复持续活跃（#514、#486、#541、#538），同时 `document-skills` 与 `example-skills` 重复安装问题（#189）也影响使用体验。
- **组织协作与分发**：强烈需求组织内共享 Skill 库（#228），将 Skill 暴露为 MCP（#16），并支持 Bedrock 等外部平台部署（#29）。
- **长上下文 Agent 记忆**：`compact-memory`（#1329）提出用符号化表示压缩长期运行 Agent 的内存状态，回应长上下文推理需求。

**关键 Issue 链接：**
- 安全与命名空间：https://github.com/anthropics/skills/issues/492
- 组织级共享：https://github.com/anthropics/skills/issues/228
- run_eval 0% recall：https://github.com/anthropics/skills/issues/556
- Agent 治理提案：https://github.com/anthropics/skills/issues/412
- 重复 Skill 问题：https://github.com/anthropics/skills/issues/189
- 推理质量门控：https://github.com/anthropics/skills/issues/1385
- 紧凑记忆：https://github.com/anthropics/skills/issues/1329
- Windows 兼容性：https://github.com/anthropics/skills/issues/1061

---

## 3. 高潜力待合并 Skills

这些 PR 与高热 Issue 直接相关、修复具体阻塞点或填补关键场景，落地概率较高：

1. **#1298 skill-creator 综合修复**：多 Bug 一并修复，是社区呼声最高的维护类 PR。  
   https://github.com/anthropics/skills/pull/1298
2. **#1323 run_eval 触发检测修复**：补齐 #1298 未覆盖的触发识别逻辑。  
   https://github.com/anthropics/skills/pull/1323
3. **#1050 / #1099 Windows 兼容性修复**：分别解决 `PATHEXT`、编码与管道读取问题，直接对应 #1061。  
   - https://github.com/anthropics/skills/pull/1050  
   - https://github.com/anthropics/skills/pull/1099
4. **#514 document-typography**：通用文档质量增强，覆盖所有 AI 生成文档场景。  
   https://github.com/anthropics/skills/pull/514
5. **#486 odt**：补齐开源办公文档格式能力。  
   https://github.com/anthropics/skills/pull/486
6. **#1367 self-audit**：推理增强与安全对齐的代表性新 Skill。  
   https://github.com/anthropics/skills/pull/1367
7. **#83 skill-quality-analyzer / skill-security-analyzer**：Marketplace 治理基础设施。  
   https://github.com/anthropics/skills/pull/83
8

---

# Claude Code 研究动态日报 · 2026-07-16

## 1. 今日速览
过去 24 小时，Claude Code 发布了 **v2.1.211**，主要涉及子代理输出透明化与权限预览的对抗性文本清洗；Issues 中 **agent 编排导致的 token 膨胀、嵌套 agent 通信失效、上下文压缩丢失系统指令、浏览器视觉工具超时**等问题突出，均与长上下文、多模态可靠性和 agent 幻觉相关。PR 端本批次无直接针对上述研究方向的代码变更。

---

## 2. 版本发布

### v2.1.211
- **新增 `--forward-subagent-text` 与 `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT`**：在 `stream-json` 输出中携带子代理文本与思考过程。  
  *研究价值*：为子代理推理链、工具调用透明度与可解释性研究提供更细粒度的日志数据，有助于 post-training 对齐与 agent 行为审计。  
- **修复权限预览中的双向覆盖、零宽字符与相似字符未 neutralization 的问题**。  
  *研究价值*：关系到提示注入、对抗性文本渲染与安全显示，是可靠人机交互与模型安全的基础环节。  
链接：https://github.com/anthropics/claude-code/releases/tag/v2.1.211

---

## 3. 研究相关 Issues（共 10 条）

| # | 标题 | 研究价值 |
|---|---|---|
| **#74990** | `/compact` 与自动压缩会丢失整个 `Available skills` 系统提示，需 `/reload-skills` 恢复 | 直接反映**长上下文压缩/摘要**过程中系统指令遗忘问题，对上下文记忆、技能保持与长期任务一致性研究有重要意义。 |
| **#63963** | Claude-in-Chrome 截图在 `document_idle` 超时后挂起 | 浏览器视觉工具链可靠性问题，关乎**多模态/OCR 管道**在真实网页环境中的鲁棒性。 |
| **#77834** | Agent fan-out 每个小任务消耗约 47K 未缓存启动 token，导致百万级 token 开销 | 提供 agent 并行化对**上下文窗口与缓存效率**的量化影响，是长上下文预算与智能调度研究的关键案例。 |
| **#65920** | 简单代码分析任务产生 272 个 agent、消耗 10M+ token | 暴露 agentic 推理中的**过度分解与 token 膨胀**，需要更好的任务-代理匹配与推理规划。 |
| **#66353** | 简单图片上传任务触发 56 个 agent 并行 | 多模态输入触发过度代理 fan-out，提示模型级规划与视觉-代理协同仍有优化空间。 |
| **#77950** | 嵌套（孙代）后台 agent 无法向直接父 agent 发送消息，父 agent 无限挂起 | 揭示**多 agent 层级通信**的可靠性缺陷，对分布式推理与协调机制研究有参考价值。 |
| **#74317** | 子代理虚构“等待后台 agent 完成”的阻塞状态，实际从未生成后台 agent | 典型的 **agent 工具使用幻觉 / 状态编造**，对幻觉缓解与工具调用验证研究直接相关。 |
| **#77932** | 原生 session-to-session（agent-to-agent）通信需求 | 反映用户对跨会话/分布式 agent 协作的需求，支持长上下文推理与多代理系统的研究方向。 |
| **#77463** | 会话实例对用户不可见，fork/resume 出现分歧、陈旧写入、token 浪费 | 涉及长会话状态一致性、实例身份与版本控制，是长期交互与上下文同步的基础问题。 |
| **#66077** | Chrome 插件：允许会话期间将截图保存到本地文件系统 | 提升视觉-语言工作流中的本地数据缓存能力，支持多模态数据集构建与可复现性。 |

---

## 4. 研究相关 PR 进展
本批次 4 个 PR（`#77916` code-quality-pipeline 插件、`#77709` 官方市场设置示例、`#77705` 插件配置校验修复、`#77613` claude-compare）均聚焦于**插件生态与配置工具**，未直接涉及长上下文推理、OCR/HMER、多模态推理、post-training 对齐或幻觉缓解，因此暂无研究相关 PR 可深入。

---

## 5. 研究方向信号
1. **Agent 编排与上下文/token 效率**：多起 issue（#77834、#65920、#66353）表明，简单任务常被过度分解为大量子代理，导致 uncached 启动 token 与上下文膨胀。信号：需要更智能的代理调度、上下文缓存策略和任务复杂度估计。
2. **视觉/多模态工具可靠性**：截图超时（#63963）与本地截图保存需求（#66077）显示，浏览器视觉链路在真实环境中仍不稳定，是

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

# OpenAI Codex 研究动态摘要（2026-07-16）

**今日速览**  
今天 `openai/codex` 的研究相关动态集中在 **agentic 多步推理可靠性** 与 **长上下文/记忆机制** 上：PR 侧新增了 prompt cache 写入 token 追踪、子 agent 分页历史继承等机制；Issues 侧则反映出 GPT-5.6 Sol 的子 agent 路由、reasoning effort 参数与后端不匹配等模型-客户端对齐问题。今日未发现与 OCR/HMER 或多模态推理直接相关的条目。

---

## 版本发布

- **无研究相关发布说明**  
  过去 24 小时仅有 `rust-v0.145.0-alpha.12/13/14` 标签，未提供涉及长上下文、OCR、多模态、对齐或幻觉缓解的变更说明，故省略。

---

## 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|----------|
| [#31814](https://github.com/openai/codex/issues/31814) | GPT-5.6 Sol 无法指定子 agent 模型，强制所有子 agent 也使用 Sol | 涉及模型元数据（`multi_agent_version = "v2"`）驱动的多 agent 路由与上下文隐藏策略，是 **长上下文/多 agent 推理** 与 **后训练对齐** 的交叉问题。 |
| [#30585](https://github.com/openai/codex/issues/30585) | Ultra 发送 `reasoning.effort=max`，但后端拒绝 | 直接反映高级推理模型在客户端-服务端参数协商上的 **对齐/可靠性** 缺口。 |
| [#15451](https://github.com/openai/codex/issues/15451) | 工具/MCP 激活时 `--json` 与 `--output-schema` 被静默忽略，输出畸形 | 结构化输出与工具调用并存时的约束违反，属于 **幻觉/可靠性** 与 **结构化推理** 范畴。 |
| [#27352](https://github.com/openai/codex/issues/27352) | CLI 在进度消息后将仍需跟进的 turn 标记为完成 | 揭示了 agent 多轮对话中 **过早终止/推理断点** 的问题，影响多步任务的长上下文连贯性。 |
| [#23186](https://github.com/openai/codex/issues/23186) | 自定义 provider 下 MCP 工具被 `type:"namespace"` 包装，严格 schema 后端无法解包 | 工具表示与后端 schema 对齐的 **function-calling / 结构化推理** 兼容性问题。 |
| [#32653](https://github.com/openai/codex/issues/32653) | 缺少工具调用结果导致桌面端崩溃 | 工具执行闭环鲁棒性缺陷，影响多步 agent 工作流的可靠性。 |

---

## 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|----------|
| [#33454](https://github.com/openai/codex/pull/33454) | Track prompt cache write token usage | 在协议、app-server、exec 与 TypeScript SDK 中暴露 `cache_write_input_tokens`，支持 **长上下文推理** 的缓存成本建模与效率优化。 |
| [#33432](https://github.com/openai/codex/pull/33432) | Preserve paginated history for spawned subagents | 子 agent 继承父 agent 分页历史与模型上下文，避免 **长上下文在 agent 分叉时丢失**，并隔离子 agent 的 roll-out prefix。 |
| [#33444](https://github.com/openai/codex/pull/33444) | Add external agent memory migration | 将外部项目的 Markdown 记忆导入 Codex memory 扩展，保留项目作用域，属于 **长期记忆/长上下文保留** 机制。 |
| [#33425](https://github.com/openai/codex/pull/33425) | Refresh host skill catalogs through world state | 通过 world state 投影刷新 host skill 目录，避免每轮重复注入，是 **动态 agent 上下文管理** 的基础。 |
| [#29500](https://github.com/openai/codex/pull/29500) | support permissions-scoped exec rules | 让执行策略规则按权限 profile 生效，强化不同风险场景下的 **安全对齐/策略执行**。 |
| [#33427](https://github.com/openai/codex/pull/33427) | Propagate deferred environment capability roots to MCP | 将延迟环境的能力根目录传播到 MCP，提升工具环境与模型上下文的一致性。 |
| [#33411](https://github.com/openai/codex/pull/33411) | Migrate plugin commands into skills on install | 将插件命令转换为生成的 skills，统一工具/技能表示，利好多模态/工具链推理的标准化。 |
| [#33414](https://github.com/openai/codex/pull/33414) | Expose connector candidates from imported sessions | 在导入外部会话时保留 MCP connector 候选信息，支撑跨会话的上下文迁移与复用。 |

---

## 研究方向信号

1. **高级推理模型与客户端配置对齐**  
   - `reasoning.effort=max` 被后端拒绝、GPT-5.6 Sol 的模型元数据强制子 agent 选型，说明 post-training 能力暴露后，客户端参数协商与模型能力边界的对齐仍是关键工程研究点。

2. **多 agent / 长上下文上下文继承**  
   - 分页历史继承、外部记忆迁移、host skill 动态刷新等 PR 密集出现，表明社区正在把“长上下文”从单会话扩展到多 agent、跨会话的记忆与技能上下文。

3. **工具调用与结构化输出的可靠性**  
   - JSON schema 被静默忽略、MCP namespace 包装、缺失工具结果崩溃等问题，说明工具增强型推理的 **幻觉/鲁棒性** 仍是高频痛点。

4. **OCR / 多模态信号缺失**  
   - 今日 Issues 与 PR 均未出现图像、公式、文档视觉理解或 HMER 相关条目，表明该方向在 Codex 仓库当前 sprint 中并非热点。

---

## 技术局限性

- **推理参数协商不一致**：客户端对 reasoning effort 的取值与后端接受范围存在偏差，暴露出模型能力声明与 API 契约之间的 **后训练对齐缺口**。
- **子 agent 上下文控制能力有限**：父 agent 的模型选择、分页历史、隐藏元数据无法显式控制，导致多 agent 长上下文分配不灵活。
- **工具调用与结构化输出互斥**：当 MCP/工具启用时，JSON schema 约束被绕过，产生 **约束违反型幻觉/输出不可靠**。
- **缺少显式多模态/OCR 支持**：用户侧未出现对图像、公式或手写内容识别的研究需求反馈，当前仓库未提供可观测的 OCR/HMER 技术能力信号。

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

# GitHub Copilot CLI 研究动态摘要 — 2026-07-16

## 1. 今日速览
今日仓库暂无新的研究相关代码合并（PR 为 0），且最新版本（v1.0.71-3）的变更集中在配置提示与终端兼容性，对模型研究本身影响有限。值得关注的信号集中在**多模态语音转录**、**超长上下文窗口诉求**、**工具/历史导致的上下文膨胀**以及**模型推理过程可见性**等方向。

## 2. 版本发布
- **v1.0.71-3**
  - `settings.json` 无效时给出警告，不再静默忽略
  - `/terminal-setup` 修复对非完整 Kitty 键盘终端的跳过行为
  - **研究相关性**：无。本次更新属于配置与终端体验修复，未涉及模型、上下文或多模态能力。

## 3. 研究相关 Issues

### 多模态 / 语音与 OCR
1. **#4024 Voice mode 下所有 ASR 模型均静默失败**  
   - **链接**：`github/copilot-cli#4024`  
   - **核心问题**：`/voice` 录音成功但所有 `nemotron` 系列 ASR 模型返回空转录，定位到 `MultiModalProcessor` 对 `nemotron_speech`（RNNT）的路由 bug。  
   - **研究价值**：直接暴露 CLI 多模态流程中的 ASR 模型加载与调度缺陷，对语音输入的可靠性、多模态处理器错误处理机制有参考意义。

### 长上下文与上下文记忆
2. **#4097 `apply_patch` 删除大二进制文件后把完整内容存入历史，导致 CAPI 5 MB 上限超限**  
   - **链接**：`github/copilot-cli#4097`  
   - **核心问题**：删除二进制文件时，`tool.execution_complete` 将整块二进制作为文本 diff 保存进 `result.detailedContent`，污染会话历史，后续请求触顶 `/compact` 也无法压缩。  
   - **研究价值**：典型的“工具输出回注导致上下文膨胀”案例，涉及长上下文中的历史压缩、差异表示优化与工具响应裁剪。

3. **#2052 持久化 Token / 上下文使用指示器**  
   - **链接**：`github/copilot-cli#2052`  
   - **核心问题**：用户希望 CLI 始终显示当前上下文窗口占用率（如 `45% context used`）。  
   - **研究价值**：反映长上下文场景下用户对窗口利用率的可观测性需求，对上下文预算策略与提示工程有指导意义。

4. **#1610 为 Opus 4.6 增加 1M 上下文支持**  
   - **链接**：`github/copilot-cli#1610`  
   - **核心问题**：早期支持 1M 上下文的 Opus 配置被移除。  
   - **研究价值**：体现长上下文模型（100 万 token）在工程侧的落地诉求。

5. **#2785 支持 Claude Opus 4.7 的 1M 上下文窗口**  
   - **链接**：`github/copilot-cli#2785`  
   - **核心问题**：与 Claude Code 的 Opus 4.7 1M 上下文默认配置不对等。  
   - **研究价值**：反映超长上下文竞争格局，对后续上下文长度、检索增强与成本权衡研究有提示。

### 推理与模型行为
6. **#1487 Codex 5.3 缺少 reasoning/thinking 输出**  
   - **链接**：`github/copilot-cli#1487`  
   - **核心问题**：用户无法获得 Codex 5.3 的推理过程，而同模型 5.2 正常。  
   - **研究价值**：涉及模型 chain-of-thought / reasoning 输出的显隐控制，对推理可解释性、后训练对齐与推理蒸馏研究相关。

7. **#1477 “Continuing autonomously (3 premium requests)” 在模型完成回答后继续自主执行**  
   - **链接**：`github/copilot-cli#1477`  
   - **核心问题**：自动模式在模型已给出完整回答后仍继续消耗 premium 请求。  
   - **研究价值**：与 agent 自主循环、停止条件与奖励/成本后训练对齐相关，属于推理执行边界控制问题。

### 研究 Agent 与工具调用
8. **#4076 内置 research agent 的 MCP 工具应可配置**  
   - **链接**：`github/copilot-cli#4076`  
   - **核心问题**：`definitions/research.agent.yaml` 硬编码了工具集，导致 `/research` 无法调用用户配置的 MCP 服务器。  
   - **研究价值**：体现“研究型子代理”在工具扩展性上的限制，对多工具协作、规划与工具检索机制的研究有现实意义。

### 指令跟随与幻觉样行为
9. **#4038 非交互模式下 MCP 晚连接注入空 user 消息，模型回显工具列表而非回答**  
   - **链接**：`github/copilot-cli#4038`  
   - **核心问题**：7 个以上工具的 MCP 服务器连接后，CLI 追加空 user 消息，模型转而回答空 turn，甚至回显系统提示中的工具列表。  
   - **研究价值**：属于提示结构异常引发的模型行为偏离，与指令跟随、系统提示污染及幻觉缓解相关。

## 4. 研究相关 PR 进展
- **无**。过去 24 小时内无与研究相关的 Pull Request 更新。

## 5. 研究方向信号
- **超长上下文成为硬性需求**：Opus 1M 窗口支持的两条高赞 Issue 显示用户已把 100 万 token 上下文视为基准，这要求更高效的上下文压缩、缓存与检索机制。
- **上下文膨胀与工具输出管理**：`apply_patch` 把二进制 diff 写入历史、以及缺少 token 指示器，说明“工具输出如何回注上下文”仍是长上下文系统瓶颈。
- **多模态语音链路尚不稳定**：ASR 模型在本地核心中“静默失败”且路由 bug，反映出多模态处理器与模型注册表间的健壮性不足。
- **Agent 自主性与工具可扩展性**：research agent 的 MCP 工具硬编码、自动模式停止条件不清，说明子代理规划和工具动态配置仍是研究热点。
- **推理透明度诉求**：Codex 5.3 reasoning 输出缺失，说明 post-training 对 reasoning 的展示策略与可解释性仍是用户与研究者共同关注点。

## 6. 技术局限性
- **上下文记忆裁剪不足**：大体积工具输出（如二进制删除 diff、图片数据）容易被原样写入历史，缺乏针对会话上下文的智能摘要与截断。
- **多模态 ASR 路由与错误静默**：voice 模式下模型失败不给出明确错误，调试困难，需要更完善的 modality 路由与失败回退。
- **自动 agent 停止与成本边界模糊**：自主模式在任务完成后仍继续调用，缺少对“完成信号”的可靠判定。
- **系统提示/工具列表污染**：异常 prompt 结构下模型会回显系统提示内容，暴露指令跟随与提示注入风险。
- **超长上下文下的工程瓶颈**：1M 上下文支持之外，仓库大文件 checkout 与全量历史加载会导致实际可用性受限，稀疏检出/懒加载成为必要补充。

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

**Kimi Code CLI 研究动态摘要 — 2026-07-16**

### 1. 今日速览
今日 GitHub 数据中未出现与长上下文推理、OCR/HMER、多模态推理、post-training 对齐或幻觉缓解直接相关的版本发布、Issue 或 PR 更新。唯一活跃的 PR 属于 telemetry 事件 schema 对齐与埋点补充，属于工程数据管道，不在当前研究范围内。

### 2. 版本发布
无相关新版本发布。

### 3. 研究相关 Issues
无。  
过去 24 小时内更新的 Issue 数量为 0，未涉及长上下文、视觉语言、对齐或可靠性相关研究点。

### 4. 研究相关 PR 进展
无符合研究方向的相关 PR。  
唯一更新的 PR 为：

- **#2500 feat(telemetry): align events with TS schema, add trace_id and missing events**  
  链接：MoonshotAI/kimi-cli PR #2500  
  说明：该 PR 仅将 Python 侧 telemetry 事件与 `agent-core-v2` 的 TS 事件注册表对齐，补充 `trace_id` 与缺失事件，对推理、OCR/HMER、多模态理解、post-training 对齐或幻觉缓解没有直接技术贡献。

### 5. 研究方向信号
暂无新信号。由于无相关 Issue/PR，未能从今日数据中提炼出推理增强、视觉能力、对齐方法或幻觉修复方面的需求趋势。

### 6. 技术局限性
无新增。当前 24 小时数据未反映用户针对上述研究方向的技术限制或研究空白。

---

**数据来源：** github.com/MoonshotAI/kimi-cli

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

# OpenCode 研究动态日报｜2026-07-16

## 1. 今日速览

今日 OpenCode 在长上下文压缩与多模态图像处理方面出现多个修复与深度讨论；v1.18.2 对子代理深度与 Meta 模型默认推理深度做了可调优限制；用户继续报告由上下文窗口溢出、图像 Base64  payload 过大以及第三方模型幻觉/乱码导致的会话中断问题。

## 2. 版本发布

**v1.18.2** — 研究相关更新：
- **子代理深度控制**：默认禁止子代理再启动嵌套子代理，并可通过 `subagent_depth` 配置限制深度，有助于控制长程推理链中的上下文爆炸与递归风险。
- **Meta 模型默认推理深度优化**：改进了 Meta 系列模型的默认推理深度，对长上下文推理与 agent 规划稳定性有直接影响。

> https://github.com/anomalyco/opencode/releases/tag/v1.18.2

## 3. 研究相关 Issues

| # | 主题 | 研究价值 |
|---|------|----------|
| **#13946** | `opencode run` 在压缩模型自身 token 用量超过 overflow 阈值后退出 | 揭示“压缩即服务”本身可能触发上下文上限，影响长上下文会话的可靠性。<br>https://github.com/anomalyco/opencode/issues/13946 |
| **#10634** | 压缩 overflow 检查直到下一步才计入大工具输出，导致上下文溢出 | 反映跨步 token 统计延迟问题，对长上下文 Agent 的实时预算控制有研究意义。<br>https://github.com/anomalyco/opencode/issues/10634 |
| **#35013** | V2 Fable/Zen 在请求字节包超出上限时绕过自动压缩 | 字节包大小与 advertised token 上限不一致，说明长上下文模型需要双重预算管理。<br>https://github.com/anomalyco/opencode/issues/35013 |
| **#32656** | `limit.input` 模型输出预算被硬 capped 在 20K，存在溢出风险 | 对输出预算预留策略的约束，关系到长上下文安全边界与模型能力匹配。<br>https://github.com/anomalyco/opencode/issues/32656 |
| **#17340** | 会话压缩失败：“即使剥离媒体后仍超出模型限制” | 直接暴露当前压缩策略在极端长上下文下的失效边界。<br>https://github.com/anomalyco/opencode/issues/17340 |
| **#14562** | 图像 Base64 导致 413 Request Entity Too Large，且 `/compact` 也失败 | 多模态图像输入与上下文压缩耦合失效，是视觉-语言长会话的关键瓶颈。<br>https://github.com/anomalyco/opencode/issues/14562 |
| **#21227** | 在聊天 UI 中展示工具返回的图像附件 | 多模态推理体验需求：让 Agent 输出中的图像可被用户验证，降低幻觉风险。<br>https://github.com/anomalyco/opencode/issues/21227 |
| **#37139** | Qwen 3.7 Plus (OpenRouter) 反复给出错误/捏造信息 | 典型幻觉与事实一致性案例，对第三方模型评测与后训练对齐有参考价值。<br>https://github.com/anomalyco/opencode/issues/37139 |
| **#37127** | GLM5.2 模型输出中文乱码/无意义重复 | 非英语输出退化现象，可能涉及 tokenization、解码或后训练对齐问题。<br>https://github.com/anomalyco/opencode/issues/37127 |

## 4. 研究相关 PR 进展

| # | 主题 | 技术贡献 |
|---|------|----------|
| **#37194** | 修复会话 overflow 检测的时间窗口缺口 | 解决“仅检查上一步 token、20K 输出预算上限、大工具输出后无检查、压缩失败静默停止”等长上下文预算问题。<br>https://github.com/anomalyco/opencode/pull/37194 |
| **#37195** | 调整压缩逻辑以清晰标识对话历史 | 提升长上下文压缩的可解释性，帮助 Agent 在压缩后保留关键推理链。<br>https://github.com/anomalyco/opencode/pull/37195 |
| **#37141** | 在结算阶段统一归一化工具与用户附件图像 | 将 `read` 以外的工具返回图像、MCP 图像及用户附件统一缩放，解决多模态会话中无界 Base64 导致的上下文与成本爆炸。<br>https://github.com/anomalyco/opencode/pull/37141 |
| **#37181** | 通过插件为不同模型选择系统提示 | 将 OpenAI、Google、Anthropic、Kimi、Arcee、Meta 的系统提示通过内置插件精细化路由，属于模型特定的提示对齐与后训练集成优化。<br>https://github.com/anomalyco/opencode/pull/37181 |
| **#32474** | `experimental.chat.system.transform` 增加 agent name 输入参数 | 为系统提示的动态转换提供额外上下文，可用于更细粒度的行为对齐与角色控制。<br>https://github.com/anomalyco/opencode/pull/32474 |
| **#37170** | 合并 dev 到 v2（包含子代理深度限制与模型默认参数调整） | V2 主干合并了子代理深度限制、Provider 默认推理参数等改动，支撑长上下文 Agent 的稳定性。<br>https://github.com/anomalyco/opencode/pull/37170 |

## 5. 研究方向信号

- **长上下文压缩与溢出检测成为核心瓶颈**：大量 issue 集中在压缩触发时机、跨步 token 统计、字节包 vs token 双上限、输出预算预留等问题，显示出当前上下文管理机制在真实 Agent 工作流中的脆弱性。
- **多模态图像处理亟需统一归一化**：用户图像、工具返回图像、MCP 图像的 Base64  Inline 传播导致 payload 爆炸，图像缩放与显示能力建设是视觉-语言推理的关键支撑。
- **模型幻觉与输出退化需要系统评估**：第三方模型（Qwen 3.7 Plus、GLM5.2）出现事实捏造与乱码，提示需要在模型选择层引入更鲁棒的幻觉检测与后训练对齐机制。
- **系统提示的模型化/插件化**：通过插件为不同模型选择系统提示，反映出对模型特定后训练行为与提示对齐的细粒度控制需求。

## 6. 技术局限性

- **极端上下文下压缩策略失效**：即使剥离媒体，部分会话仍超出模型上限，说明现有压缩/摘要策略对超长对话的压缩比不足。
- **跨步 token/字节预算统计不一致**：大工具输出、请求字节包、上一步 token 之间存在统计延迟或口径差异，导致 overflow 检测滞后。
- **图像 Inline 数据未得到全局治理**：图像缩放只在 `read` 工具中生效，其他工具、MCP 与用户附件未统一处理，造成

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

# Pi 研究动态摘要（2026-07-16）

## 1. 今日速览
过去 24 小时无新版本发布。研究相关动态集中在**长上下文会话压缩与摘要的可靠性**、**reasoning/thinking 块解析与渲染**、**工具调用结构解析**以及**模型流式输出鲁棒性**等方面。今日 Issue/PR 中未出现与 OCR/HMER 或多模态视觉理解直接相关的内容。

## 2. 版本发布
无（过去 24 小时无 Releases）。

## 3. 研究相关 Issues

| Issue | 状态 | 研究价值 |
|-------|------|----------|
| **#4945** `openai-codex` Connection Reliability Issues<br>https://github.com/earendil-works/pi/issues/4945 | OPEN | 模型流式交互在无输出、无工具调用、无显式错误时挂死，是 long-context agent 在可靠性/故障模式上的典型问题，影响长会话的连续推理。 |
| **#6212** Bedrock path should honor `compat.forceAdaptiveThinking`<br>https://github.com/earendil-works/pi/issues/6212 | OPEN | 与推理控制相关：建议根据模型定义动态选择 adaptive/legacy thinking 路径，而非仅靠硬编码模型列表。 |
| **#6640** XML tool-call collapses `<item>` children into a single string<br>https://github.com/earendil-works/pi/issues/6640 | CLOSED | 工具调用 XML 解析缺陷会导致结构化输入被错误合并，影响模型-工具交互的语义保真度。 |
| **#6647** Compaction fails on a single transient stream drop (no retry)<br>https://github.com/earendil-works/pi/issues/6647 | OPEN | 长上下文压缩单次调用失败即中断，未复用普通 assistant turn 的 retry 逻辑，是长会话记忆机制的关键脆弱点。 |
| **#6639** Prevent repeated auto-compaction for MiMo zero-output length overflows<br>https://github.com/earendil-works/pi/issues/6639 | CLOSED | 上下文长度溢出后的自动压缩策略存在反复触发问题，涉及长上下文 token 预算与恢复机制。 |
| **#6685** Intermittent failure to execute tool calls and display thinking blocks<br>https://github.com/earendil-works/pi/issues/6685 | CLOSED | 模型侧正确输出了 thinking/tool 内容，但 harness 在事件处理/转录阶段丢失，直接影响推理透明度与工具调用可靠性。 |
| **#6673** OpenAI Codex exposes raw Cloudflare 520 HTML including client IP<br>https://github.com/earendil-works/pi/issues/6673 | CLOSED | 上游错误页面被原样写入 session JSONL，属于模型输出污染与错误信息控制问题，与幻觉/安全边界相关。 |

## 4. 研究相关 PR 进展

| PR | 状态 | 技术贡献 |
|----|------|----------|
| **#6594** `feat: sqlite session storage`<br>https://github.com/earendil-works/pi/pull/6594 | OPEN | 在 compaction 条目中引入 `retainedTail`，并将 `getPathToRoot` 改为 `getPathToRootOrCompaction`，避免长上下文下不必要的完整树遍历，属于 long-context memory 优化。 |
| **#6671** `add usage info to branch summary, compaction and tool result entries`<br>https://github.com/earendil-works/pi/pull/6671 | OPEN | 为分支摘要、压缩条目和工具结果增加 token usage 元数据，支持长会话的 token 预算监控与成本感知调度。 |
| **#6533** `fix: Codex compaction returns "Model not found" for gpt-5.6-luna`<br>https://github.com/earendil-works/pi/pull/6533 | CLOSED | 修复压缩阶段模型 ID 映射错误，保证长上下文摘要/压缩在 Codex 路径上可用。 |
| **#6651** `feat(ai): add xAI device OAuth and route grok-4.5 through Responses`<br>https://github.com/earendil-works/pi/pull/6651 | OPEN | 将 `grok-4.5` 按低/中/高 reasoning 级别路由到 Responses API，其他模型保持 Completions，属于推理级别路由基础设施。 |

## 5. 研究方向信号
- **长上下文压缩与摘要可靠性**：Issue 与 PR 反复出现 compaction/stream 中断、token 预算、 retainedTail、模型映射等问题，说明长会话记忆机制是当前工程与研究结合的重点。
- **推理透明度与 thinking 块处理**：thinking block 的解析、展示、adaptive thinking 路径选择等需求突出，反映对推理过程可控与可观测的关注。
- **工具调用与结构化输出鲁棒性**：XML tool-call 解析、工具结果 usage 元数据、工具调用事件丢失等问题，显示 agent 在“模型输出 → 工具执行 → 反馈”链条上的可靠性仍需加强。
- **流式交互与故障恢复**：连接挂死、单次流中断导致失败、错误页面被回写等，提示模型-系统接口的容错机制是研究空白之一。

## 6. 技术局限性
- **Compaction 无重试**：长上下文压缩对单点流中断敏感，缺乏与普通 assistant turn 同等的重试策略。
- **Thinking/tool 内容易丢失**：模型已正确输出，但 harness 事件处理或转录阶段可能丢弃，导致用户看不到推理过程或工具调用。
- **Adaptive thinking 配置不统一**：Bedrock 等后端仍依赖硬编码模型列表，未充分复用模型元数据中的 reasoning 兼容性标志。
- **错误输出污染会话状态**：上游错误 HTML 被原样存储，影响后续 context 质量与潜在隐私泄露。
- **OCR/HMER 与多模态能力缺失**：本日数据中未见相关 Issue 或 PR，显示 Pi 当前活跃问题集中在文本/代码 agent 核心链路。

</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

# Qwen Code 研究动态摘要（2026-07-16）

## 1. 今日速览
今天 Qwen Code 在**长上下文效率、推理输出可靠性与对齐安全**方面出现多个值得研究关注的信号：Issues 侧揭示了 managed memory 配置失效导致的上下文浪费、reasoning 标签关闭时的解析脆弱性，以及安全分类器在 auto 审批模式下死锁的问题；PR 侧则通过强制 `tool_choice`、修复 tool-call 流式解析和传播可信调用上下文等改动积极应对。同时，**cua-driver-rs v0.7.2** 发布，继续支撑多模态 GUI 自动化能力。

---

## 2. 版本发布
### cua-driver-rs v0.7.2
- **更新要点**：发布预编译二进制，新增 relative-coordinate（相对坐标）fork 支持；macOS 提供 codesigned + notarized universal binary 及 `QwenCuaDriver.app`，Linux/Windows 提供 unsigned x86_64/arm64 构建。
- **研究相关性**：作为计算机使用代理（Computer Use Agent）的底层驱动，该组件支撑视觉-动作协同的多模态推理与 GUI 自动化，relative-coordinate 能力对跨分辨率、跨设备的视觉定位鲁棒性有直接影响。
- **链接**：https://github.com/QwenLM/qwen-code/releases/tag/cua-driver-rs-v0.7.2

---

## 3. 研究相关 Issues

| # | Issue | 研究价值 |
|---|-------|----------|
| **#6936** | [isManagedMemoryAvailable() ignores `enableManagedAutoMemory` setting, wasting 7-9 KB of context](https://github.com/QwenLM/qwen-code/issues/6936) | 直接关联长上下文效率：配置关闭后仍注入 ~7-9 KB 的 auto memory 指令块，提示 prompt 压缩与配置一致性仍是研究重点。 |
| **#6849** | [Avoid full-turn retries for standalone closing `</think>` tags in otherwise valid responses](https://github.com/QwenLM/qwen-code/issues/6849) | 推理模型输出解析鲁棒性：qwen3.7-max 偶发单独返回 `</think>`，当前策略会整轮重试，需更细粒度的 thinking/reasoning 边界处理。 |
| **#6927** | [分类器报错：auto approval 模式下安全分类器 fail-closed 导致所有工具被阻塞](https://github.com/QwenLM/qwen-code/issues/6927) | 对齐/安全分类器的可靠性：分类器持续误判会制造死锁，说明 post-training 对齐后的行为一致性与错误恢复仍需改进。 |
| **#6917** | [Untrusted MCP `readOnlyHint` skips default tool confirmation](https://github.com/QwenLM/qwen-code/issues/6917) | 信任边界与权限对齐：未受信任的 MCP 服务器通过 `readOnlyHint` 绕过确认，暴露安全策略与工具注解之间的冲突。 |
| **#6831** | [Trust-status "preview" check mutates cached trusted-folders config, leaking unconfirmed trust state](https://github.com/QwenLM/qwen-code/issues/6831) | 信任状态管理：预览性检查意外持久化未确认的信任配置，影响安全策略的可解释性与一致性。 |
| **#6990** | [Agent stops mid response to queries and returns XML-like output](https://github.com/QwenLM/qwen-code/issues/6990) | 模型输出/流式生成可靠性：代理在响应中途停止并返回 XML 片段，可能与结构化生成或 model-switching 的边界处理有关。 |
| **#5239** | [subagent 和主会话通信机制较弱，建议升级为双向

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

# DeepSeek-TUI 研究动态日报（2026-07-16）

## 1. 今日速览
今日无新 Release。过去 24 小时的 Issues 集中在**长上下文推理基础设施**、**多智能体协调**与**可复现的对齐/评估基础设施**三个方向。值得关注的是：模型级上下文缓存策略、持久化 KV cache 方案、运行轨迹导出与开放权重微调对接、可配置 LLM-as-judge 裁判机制，以及审批过程中回看推理链的体验优化。**OCR/HMER 与多模态视觉能力方面未见相关信号。**

## 2. 版本发布
无。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|----------|
| [#2693](https://github.com/Hmbown/CodeWhale/issues/2693) | HarnessPosture：模型专属的上下文与子代理策略 | 长上下文 / 缓存策略：按 provider/model 路由设定不同的“cache-heavy/prefix-stable”启动提示，避免对所有模型使用统一 up-front context，直接影响长程推理的效率与成本。 |
| [#2904](https://github.com/Hmbown/CodeWhale/issues/2904) | 持久化 Agent 状态与签名压缩 KV cache 胶囊 | 长上下文 / 推理连续性：通过持久化状态与本地/云端签名 KV cache 胶囊，降低长程 coding 会话的重复计算、延迟和费用，是长上下文推理的工程基础。 |
| [#4371](https://github.com/Hmbown/CodeWhale/issues/4371) | 审批弹窗期间允许滚动查看 reasoning 输出 | 幻觉缓解 / 推理可解释性：在关键操作审批前让人类可审查模型的 CoT/执行计划，减少因隐藏 reasoning 导致的错误授权。 |
| [#1977](https://github.com/Hmbown/CodeWhale/issues/1977) | Model Lab：将 CodeWhale 轨迹对接开源微调/评估服务 | Post-training 对齐 / 数据构建：把用户真实 coding 会话转化为可筛选的数据集、评测集与可选微调任务，支持开放权重模型的持续改进。 |
| [#1986](https://github.com/Hmbown/CodeWhale/issues/1986) | Team workbench：本地知识、策略包与路由证据 | 对齐 / 可靠性：为团队提供可审计的本地知识、项目策略与模型/工具/审批/成本证据，是替代黑盒 assistant 工作流的关键治理层。 |
| [#2094](https://github.com/Hmbown/CodeWhale/issues/2094) | `/hunt` 裁判系统：可配置 LLM-as-judge 与三级策略 | 幻觉缓解 / 验证：引入 strict/evidentiary/permissive 三种策略与轨迹感知判决， Codex-style 裁判机制可直接用于减少错误输出与误操作。 |
| [#2752](https://github.com/Hmbown/CodeWhale/issues/2752) | WhaleFlow/Model Lab 运行轨迹导出系统 | 对齐 / 可复现评估：结构化记录模型配置、输入与输出，支撑多模型/工作流对比、评测与后续训练数据生成。 |
| [#2975](https://github.com/Hmbown/CodeWhale/issues/2975) | WhaleFlow ARMH/RLM 共享记忆与实时引擎/遥测集成 | 长上下文 / 记忆：在多个工作流分支间共享 exact-context 记忆，避免重复模型调用，并通过 hit/miss/cost 遥测量化缓存收益。 |
| [#2977](https://github.com/Hmbown/CodeWhale/issues/2977) | cached-main overlay | 长上下文 / 提示工程：在不污染 Git main 的前提下，预热 promoted notes、workflow、branch heuristics、model/cache policy 与 prompt patches，提升后续运行的上下文质量。 |
| [#3230](https://github.com/Hmbown/CodeWhale/issues/3230) | WhaleFlow swarm：多 worker 合成/归约阶段 | 多智能体推理 / 集成学习：把多个异构模型 worker 的输出归约为一致结果，对应 ultracode/kimi-code swarm 模式，是多模型联合推理的关键步骤。 |

---

## 4. 研究相关 PR 进展
今日无与研究方向（长上下文、OCR/HMER、多模态推理、post-training 对齐、幻觉缓解）直接相关的 PR 进展。

---

## 5. 研究方向信号

1. **长上下文工程化是核心主线**：从 model-specific cache policy、持久化 KV cache、shared-memo 到 cached-main overlay，社区正在把“长上下文”从模型能力问题转化为**系统级 harness、缓存、记忆与预热**问题。
2. **评估与后训练对齐基础设施加速成型**：Model Lab、运行轨迹导出、LLM-as-judge、team workbench 的出现，说明 CodeWhale 正在从“消费模型”转向“**可审计、可评测、可微调**”的开放模型工作流。
3. **多智能体协调进入 reduce/synthesis 阶段**：WhaleFlow swarm 的合成归约与 Fleet 角色交接机制，标志着多模型/多 agent 工作流从“并行调用”走向“**可验证的一致性输出**”。
4. **推理透明度与审批对齐受关注**：审批期间查看 reasoning 的诉求，反映出对 agent 决策过程可解释性与人类监督的强需求。
5. **OCR/HMER 与多模态视觉仍是空白**：在 48 条活跃 Issue 中，未出现与手写数学表达式识别、图像理解、视觉语言模型相关的讨论。

---

## 6. 技术局限性

- **长程状态与记忆尚未统一**：持久化 KV cache、shared-memo、memory tool 等方案并行推进，但缺乏统一抽象，用户仍需在不同机制间手动选择。
- **推理链与操作审批的交互仍受限**：模型生成的 CoT/执行计划目前无法在审批弹窗中便捷滚动查看，影响人类监督质量。
- **缺乏端到端的对齐/训练闭环**：轨迹导出、LLM-as-judge、Model Lab 虽然存在，但尚未形成从“采集 → 筛选 → 评估 → 微调 → 验证”的完整 pipeline。
- **多智能体 reduce 机制待落地**：swarm 合成/归约阶段仍停留在 issue 阶段，缺少具体实现与跨模型一致性评估方案。
- **视觉/多模态能力未纳入路线图**：在已公开的讨论中，没有 OCR、HMER 或图像/视频理解相关 issue，显示该方向尚未被当前迭代覆盖。

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*