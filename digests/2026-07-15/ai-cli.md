# AI CLI 工具社区动态日报 2026-07-15

> 生成时间: 2026-07-15 00:20 UTC | 覆盖工具: 9 个

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

# AI CLI 工具横向对比分析报告（2026-07-15）

## 1. 生态全景

当前 AI CLI 工具已从“代码补全”阶段全面转向“自主 Agent 工程平台”竞争。社区反馈显示，各产品的核心战场集中在**长上下文稳定性、多智能体编排、工具/结构幻觉、指令遵循与多模态输入**五个方向；同时，上下文压缩、会话持久化、子代理状态一致性等基础设施问题成为共性瓶颈。整体来看，头部厂商工具（Claude Code、OpenAI Codex、Gemini CLI、GitHub Copilot CLI）在规模与生态整合上领先，而 Pi、Qwen Code、DeepSeek TUI 等则在特定技术点（多 Provider 抽象、结构化记忆、可配置 Compaction）上快速迭代。

---

## 2. 各工具活跃度对比

> 注：以下统计仅基于本日“研究相关”条目，非仓库全量活动。

| 工具 | 研究相关 Issue | 研究相关 PR | 版本发布 |
|------|---------------|------------|----------|
| **Claude Code** | 5 | 3 | v2.1.210 / v2.1.209 / v2.1.208 |
| **OpenAI Codex** | 7 | 4 | rust-v0.144.4（及 alpha 系列） |
| **Gemini CLI** | 10 | 3 | v0.52.0-nightly.20260714 |
| **GitHub Copilot CLI** | 10 | 0 | v1.0.71-2 / v1.0.71-1 |
| **Kimi Code CLI** | 0 | 3 | 无 |
| **OpenCode** | 3 | 2 | v1.18.1 / v1.18.0 |
| **Pi** | 10 | 9 | v0.80.7 |
| **Qwen Code** | 4 | 6 | v0.19.10 / v0.19.9 |
| **DeepSeek TUI** | 6 | 2 | 无 |

**活跃度信号**：Pi 今日研究相关 PR 密度最高（9 条），显示其正处于快速工程迭代期；Gemini CLI 与 Copilot CLI 的 Issue 热度最高，但 Copilot 当日无研究相关 PR 合并；Kimi 与 DeepSeek 当天无新 Release，但 Kimi 的 3 个 PR 均围绕推理与长上下文预算，技术聚焦度很高。

---

## 3. 共同关注的功能方向

| 功能方向 | 涉及工具 | 具体诉求 |
|----------|---------|----------|
| **长上下文压缩与状态一致性** | Claude Code、Codex、Gemini、Copilot、Qwen、DeepSeek、Pi、Kimi、OpenCode | 动态/可配置上下文预算、Compaction 策略、子代理模型配置在续接/压缩后不被丢失、避免大体积工具输出污染历史 |
| **Agent 自我状态与终止幻觉** | Claude Code、Gemini、Codex、Qwen、DeepSeek | 子代理 `MAX_TURNS` 误报为成功、工具调用中发明未声明字段、陈旧 `plan.md` 被误执行、简单问题无限循环 |
| **指令遵循与对齐治理** | Claude Code、Copilot CLI、Gemini、DeepSeek、Codex | `AGENTS.md` / Constitution / 工具白名单 / frontmatter 规则在实际运行中失效或执行不一致 |
| **多模态输入/输出** | Copilot CLI、Codex、Pi、Qwen | 本地语音 ASR 路由、PDF 原生读取、视频/音频 prompt、imagegen 输出去重、PDF 视觉桥边界错误 |
| **评估与可观测性** | Gemini、DeepSeek、Claude Code、Codex | 组件级行为评估、子代理轨迹可见、版本化工具生命周期元数据、离线审查与对齐数据回流 |

---

## 4. 差异化定位分析

| 工具 | 功能侧重 | 目标用户 | 技术路线 |
|------|---------|----------|----------|
| **Claude Code** | 长会话记忆、Agent 工具调用治理、模型路由 | 企业级开发团队 | 以 Agent 架构与工具 schema 约束为核心，强调安全边界与状态一致性 |
| **OpenAI Codex** | 多模型调度、持久化 goal、浏览器/Web 多模态、imagegen | 全栈开发者 | 依托 OpenAI 模型目录，推进 persistent goal 与浏览器/网页感知环境 |
| **Gemini CLI** | 对齐安全、递归推理控制、A2A 生态 | 注重安全与 Google 生态的开发者 | 强调整体安全治理（destructive behavior、evals）与递归轮次限制 |
| **GitHub Copilot CLI** | GitHub/VS Code 生态、本地多模态（Foundry）、AGENTS.md 指令 | 现有 Copilot 用户 | 深度绑定 GitHub 工作流，探索本地 ASR/PDF 等端侧多模态 |
| **Kimi Code CLI** | 动态上下文预算、reasoning 参数精确控制 | 长上下文代码任务用户 | 从固定 32k 预算转向剩余窗口动态分配，聚焦推理接口标准化 |
| **OpenCode** | 轻量化 UI、推理展示、一键压缩 | 注重交互体验的开发者 | 以 UI/UX 为驱动，快速补齐 reasoning 可视化与上下文管理入口 |
| **Pi** | 多 Provider 抽象、SQLite 会话持久化、prompt cache | 跨模型/多后端用户 | 通过统一协议层解决不同厂商的上下文压缩、reasoning、缓存差异 |
| **Qwen Code** | 结构化通道记忆、PDF 视觉桥、reasoning 标签安全 | Qwen 模型用户 | 将外部记忆从 Markdown 升级为版本化结构化存储，强化视觉桥鲁棒性 |
| **DeepSeek TUI** | 可配置 Compaction/Seam、Constitution 对齐 | 偏好本地可控性的用户 | 强调上下文压缩开关与“宪法”式规则遵循的可配置性 |

---

## 5. 社区热度与成熟度

- **高热度且快速迭代**：**Gemini CLI**（10 研究 Issue + 3 PR）、**Pi**（10 + 9）、**Claude Code**（5 + 3）——三者同时保持了高社区反馈密度与代码落地速度，议题覆盖对齐、长上下文、工具治理等核心研究点。
- **Issue 热度高但 PR 产出低**：**GitHub Copilot CLI**（10 Issue、0 PR）——用户痛点集中在多模态输入、上下文污染与指令遵循，但当日未见研究相关代码修复。
- **PR 聚焦但 Issue 稀疏**：**Kimi Code CLI**（0 研究 Issue、3 PR）——当日无新用户反馈，但核心修复（reasoning 参数、动态预算）显示其技术路线清晰。
- **活跃的新兴/垂直工具**：**Qwen Code**（4 + 6）、**DeepSeek TUI**（6 + 2）、**OpenCode**（3 + 2）——体量小于头部工具，但在结构化记忆、可配置压缩、推理展示等细分方向动作频繁。

---

## 6. 值得关注的趋势信号

1. **长上下文管理正从“窗口大小”转向“状态可控性”**  
   社区不再只关注 token 上限，而是更关心压缩、续接、子代理状态、工具输出污染等实际问题。建议开发者将 Compaction 策略、会话持久化与动态预算纳入 Agent 设计的首要考虑。

2. **Agent 自我监控与终止幻觉是下一个可靠瓶颈**  
   `MAX_TURNS` 误报成功、发明未声明字段

---

## 各工具详细报告

<details>
<summary><strong>Claude Code</strong> — <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></summary>

## Claude Code Skills 社区热点

> 数据来源: [anthropics/skills](https://github.com/anthropics/skills)

# Claude Code Skills 社区热点报告（截至 2026-07-15）

> 数据来源：github.com/anthropics/skills 的公开 PR 与 Issue。以下 PR 按仓库热度/评论排序展示，当前快照中显示的热门条目状态均为 **OPEN**。

---

## 1. 热门 Skills 排行（Top 7）

| 排名 | PR | Skill / 功能 | 社区讨论热点 | 状态 |
|---|---|---|---|---|
| 1 | [#1298](https://github.com/anthropics/skills/pull/1298) | **skill-creator 评估修复**<br>修复 `run_eval.py` 始终报告 `recall=0%`、Windows 流读取、触发检测与并行 worker 问题。 | 被视作 Skill 创作基础设施的核心 bug；直接影响 `run_loop.py` 与 `improve_description.py` 的优化效果。 | OPEN |
| 2 | [#514](https://github.com/anthropics/skills/pull/514) | **document-typography**<br>AI 生成文档的排版质量控制：孤行、寡行、编号错位等。 | 讨论焦点是“AI 生成文档时默认不关注排版细节”，希望把排版质量内嵌为默认能力。 | OPEN |
| 3 | [#486](https://github.com/anthropics/skills/pull/486) | **ODT skill**<br>OpenDocument 文本创建、模板填充、ODT 解析为 HTML。 | 满足开源/ISO 标准办公文档需求，与现有 docx/pdf 技能形成互补。 | OPEN |
| 4 | [#1367](https://github.com/anthropics/skills/pull/1367) | **self-audit**<br>输出前“机械文件验证 + 四维推理质量门”。 | 与推理安全、输出可靠性高度相关；强调“按损害严重度优先”的审查顺序。 | OPEN |
| 5 | [#723](https://github.com/anthropics/skills/pull/723) | **testing-patterns**<br>全栈测试模式：单元测试、React 组件测试、测试哲学等。 | 代码智能体/开发者工作流的热门方向，关注“哪些该测、哪些不该测”。 | OPEN |
| 6 | [#83](https://github.com/anthropics/skills/pull/83) | **skill-quality-analyzer /<br>skill-security-analyzer** | 为 Skill 市场增加质量与安全审查的元技能，覆盖结构、文档、安全性等维度。 | OPEN |
| 7 | [#210](https://github.com/anthropics/skills/pull/210) | **frontend-design**<br>改写前端设计技能，提升清晰度与可执行性。 | 讨论如何让 Skill 指令在单次对话中更可落地。 | OPEN |

---

## 2. 社区需求趋势

从 Issues 评论热度提炼出以下方向：

1. **安全与信任边界**  
   - [#492](https://github.com/anthropics/skills/issues/492) 指出社区 Skill 冒用 `anthropic/` 命名空间导致信任边界滥用；[#1175](https://github.com/anthropics/skills/issues/1175) 讨论在 SKILL.md 中写访问控制的安全风险；[#412](https://github.com/anthropics/skills/issues/412) 提议 `agent-governance` 安全模式。  
   → 社区迫切要求 **命名空间治理、权限最小化与审计能力**。

2. **Skill 创作与评估工具链的可靠性**  
   - [#556](https://github.com/anthropics/skills/issues/556)、[#1169](https://github.com/anthropics/skills/issues/1169)、[#1061](https://github.com/anthropics/skills/issues/1061) 集中反馈 `run_eval.py` 在 Windows/触发检测/编码上的缺陷；[#202](https://github.com/anthropics/skills/issues/202) 要求 `skill-creator` 改为最佳实践。  
   → **creator 工具链是基础设施瓶颈**，优先级极高。

3. **文档与企业格式能力**  
   - 除 [#514](httpshttps://github.com/anthropics/skills/pull/514) 排版与 [#486](https://github.com/anthropics/skills/pull/486) ODT 外，[#538](https://github.com/anthropics/skills/pull/538) PDF 大小写修复、[#541](https://github.com/anthropics/skills/pull/541) DOCX 跟踪修订 ID 冲突也在活跃维护。  
   → 文档处理仍是 Skills 生态最密集的落地场景。

4. **长上下文、记忆与推理质量**  
   - [#1329](https://github.com/anthropics/skills/issues/1329) 提出 `compact-memory` 用符号化表示压缩智能体状态；[#1385](https://github.com/anthropics/skills/issues/1385) 提议三阶段推理质量门管道；[#1367](https://github.com/anthropics/skills/pull/1367) 已实现输出前审计。  
   → 随着会话变长，**记忆压缩与推理质量门**成为新焦点。

5. **组织协作与生态互通**  
   - [#228](https://github.com/anthropics/skills/issues/228) 要求组织级 Skill 共享；[#16](https://github.com/anthropics/skills/issues/16) 提议把 Skills 暴露为 MCP；[#29](https://github.com/anthropics/skills/issues/29) 询问 Bedrock 支持。  
   → 社区希望 Skills 从个人工具走向 **团队资产与开放协议**。

---

## 3. 高潜力待合并 Skills

以下 PR 评论活跃、尚未合并，具备近期落地潜力：

- **基础设施类**（解决 creator/eval 核心痛点）  
  - [#1298](https://github.com/anthropics/skills/pull/1298) — 全面修复 `run_eval.py` 0% recall  
  - [#1323](https://github.com/anthropics/skills/pull/1323) — 修复触发检测与首个非 Skill 工具误判  
  - [#1099](https://github.com/anthropics/skills/pull/1099) / [#1050](https://github.com/anthropics/skills/pull/1050) — Windows 子进程/编码兼容  
  - [#1261](https://github.com/anthropics/skills/pull/1261) — 隔离触发评估命令文件与真实项目注册表  

- **新 Skill 能力**  
  - [#514](https://github.com/anthropics/skills/pull/514) `document-typography`  
  - [#486](https://github.com/anthropics/skills/pull/486) `odt`  
  - [#1367](https://github.com/anthropics/skills/pull/1367) `self-audit`  
  - [#723](https://github.com/anthropics/skills/pull/723) `testing-patterns`  
  - [#1302](https://github.com/anthropics/skills/pull/1302) `color-expert`  
  - [#83](https://github.com/anthropics/skills/pull/83) `skill-quality-analyzer` / `skill-security-analyzer`  
  - [#181](https://github.com/anthropics/skills/pull/181) `SAP-RPT-1-OSS` 表格预测模型  

- **文档/格式修复**  
  - [#538](https://github.com/anthropics/skills/pull/538) PDF 大小写引用  
  - [#541](https://github.com/anthropics/skills/pull/541) DOCX 跟踪修订 ID 冲突  
  - [#539](https://github.com/anthropics/skills/pull/539) YAML 特殊字符未引号警告  

---

## 4. Skills 生态洞察

**当前社区在 Skills 层面最集中的诉求是：让 Skill 本身更可信赖、可评估、可协作——既要修复 creator/评估基础设施的可靠性瓶颈，也要补齐文档与企业格式能力，并同步建立命名空间、安全、治理与组织共享的信任边界。**

---

**Claude Code 研究动态摘要 · 2026-07-15**

---

### 1. 今日速览

过去 24 小时，Claude Code 仓库没有直接针对长上下文推理、OCR/HMER、多模态理解或 post-training 对齐的代码更新。与研究相关的信号集中在 **Agent 工具调用的可靠性、模型路由幻觉、跨长会话的状态一致性** 等方面：Agent 团队在 `SendMessage` 中高频生成未文档字段、子代理模型覆盖在会话延续/压缩后丢失、跨天会话出现时间戳推理错误，以及项目级记忆存储的本地化管理需求。

---

### 2. 版本发布

今日发布 v2.1.210 / v2.1.209 / v2.1.208，主要涉及 UI 计时器、屏幕阅读器模式、Vim 映射和权限提示等。  
**无与本研究范围直接相关的版本更新，本节省略。**

---

### 3. 研究相关 Issues

| # | 标题 | 研究价值 | 链接 |
|---|------|----------|------|
| **#77595** | Agent teams: SendMessage 中模型自发构造未文档的 `content` 字段，导致单条消息重复发送约 3 次 | 典型的 **工具调用幻觉 / schema 合规性** 问题：模型在自由文本发送时高频发明字段，提示需要更强的输出格式对齐与字段级抑制策略。 | https://github.com/anthropics/claude-code/issues/77595 |
| **#68147** | 子代理显式 `model` 参数在 continuation 边界（SendMessage 后续 / 压缩后恢复）被静默丢弃 | 直接涉及 **长会话状态保持与模型路由一致性**：上下文压缩/延续机制会破坏子代理的模型配置，影响长任务推理稳定性。 | https://github.com/anthropics/claude-code/issues/68147 |
| **#66245** | 跨天会话中 Agent 将历史工作日期默认记录为“当前时间” | 反映 **长上下文时间推理与记忆回溯** 的不足：模型未能正确推断多日会话中历史事件的真实时间戳。 | https://github.com/anthropics/claude-code/issues/66245 |
| **#25947** | 将项目记忆文件从全局路径迁移到项目本地 `.claude/memory/` | 与 **长上下文记忆管理、上下文边界与项目级检索** 相关；本地化记忆有助于提升检索精度与可迁移性。 | https://github.com/anthropics/claude-code/issues/25947 |
| **#73931** | 支持为子代理声明模型不可用时按声明规则回退，而非静默继承主会话模型 | 属于 **模型可用性推理与可靠路由** 问题；对多模型调度与对齐策略的鲁棒性有参考价值。 | https://github.com/anthropics/claude-code/issues/73931 |

> **注**：今日 Issues 中未出现与 OCR、HMER 或多模态输入/输出直接相关的新反馈。

---

### 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 | 链接 |
|---|------|----------|------|
| **#77427** | `fix(pr-review-toolkit): make code-reviewer a leaf agent` | 将代码审查 Agent 限制为仅使用仓库检查工具，并禁止其再调度其他 Agent/工作流。属于 **Agent 能力边界与对齐/安全约束** 的治理改进。 | https://github.com/anthropics/claude-code/pull/77427 |
| **#77492** | `fix(hookify): match Write and prompt rules` | 修复简单规则在 `Write` 内容和用户提示词提交时的匹配与映射，补齐 `Edit/Write` 与 prompt 规则的回归覆盖。对 **工具使用规则对齐与权限推断** 有研究意义。 | https://github.com/anthropics/claude-code/pull/77492 |
| **#77556** | `fix(plugin-dev): validate-hook-schema.sh handles plugin hooks.json format` | 修正 hook-schema 校验器对插件 `hooks.json` 格式的解析，减少因 schema 格式误判导致的规则失效。支撑 **插件/工具治理与配置对齐**。 | https://github.com/anthropics/claude-code/pull/77556 |

---

### 5. 研究方向信号

- **工具调用幻觉与 schema 约束**：Agent 团队通信中出现模型自发构造未文档字段的现象，说明需要在工具定义或后训练阶段加强对“允许字段”的约束，抑制结构化输出中的冗余/伪字段。
- **长会话状态一致性**：子代理模型配置在 continuation/compaction 后丢失、多日会话时间戳错误等反馈，指向长上下文记忆与会话状态持久化的关键研究需求。
- **模型路由与可用性**：社区对子代理模型回退、模型选择器显示与实际后端不一致等诉求增多，提示多模型调度与可靠性对齐仍是活跃问题。
- **记忆本地化管理**：将项目记忆从全局目录迁移到项目本地的请求热度较高，反映对项目级上下文隔离与可解释记忆的需求。

---

### 6. 技术局限性

- **长上下文状态延续不可靠**：上下文压缩、续接或会话恢复后，模型选择、子代理配置等关键元信息可能被静默重置，导致推理路径偏离用户预期。
- **Agent 工具输出存在结构化幻觉**：模型在自由文本工具调用中反复发明未声明字段，造成重复内容与 token 浪费，目前缺乏字段级抑制或自动 schema 校验机制。
- **时间/事件推理在长会话中退化**：跨天会话中，模型倾向于将历史事件时间锚定到“当前”，显示对时间顺序和会话历史的长程推理不足。
- **项目记忆与权限规则的全局/本地隔离不完善**：记忆文件和权限规则的位置与作用域不够清晰，影响上下文检索准确性与规则执行一致性。
- **多模态/OCR 能力未在 Issue 中体现**：近期用户反馈未覆盖图像、文档或手写公式识别等场景，相关研究进展/ regressions 暂无信号。

</details>

<details>
<summary><strong>OpenAI Codex</strong> — <a href="https://github.com/openai/codex">openai/codex</a></summary>

**OpenAI Codex 研究动态日报（2026-07-15）**

---

### 1. 今日速览

过去 24 小时内，**与研究最相关的是用户反馈的 GPT-5.6 Sol 长上下文窗口严重回退（353K → 258K）**，以及子代理模型无法独立指定的多智能体编排问题。代码侧则以 GPT-5.6 模型迁移、Guardian 安全策略模板、imagegen 多模态输出去重以及 MCP 工具规划/可靠性改造为主，没有面向研究的正式版本发布。

---

### 2. 版本发布

- **无与研究直接相关的版本更新。** 过去 24 小时发布的 `rust-v0.144.4` 为无用户面变更的 chore patch；其余为 `rust-v0.145.0-alpha.x` 早期版本，未提供研究相关说明。该部分予以省略。

---

### 3. 研究相关 Issues

> 以下按与研究方向的相关性挑选，暂未发现直接的 OCR/HMER 专项 Issue。

1. **GPT-5.6 Sol 上下文窗口严重回退：353K → 258K（广告称 1.05M）**  
   - Issue: [openai/codex#32806](https://github.com/openai/codex/issues/32806)  
   - 研究价值：暴露出长上下文模型在 Catalog/Runtime 层的实际可用 token 预算与宣传能力不一致，直接影响长文档推理、上下文压缩与截断策略的评估。

2. **GPT-5.6 Sol 无法指定子代理模型，强制所有子代理也使用 Sol**  
   - Issue: [openai/codex#31814](https://github.com/openai/codex/issues/31814)  
   - 研究价值：MultiAgent V2 的模型元数据与子代理模型选择解耦问题，关系到多智能体任务分解、推理成本与质量的联合优化。

3. **远程 compaction 容量错误导致单一持久目标被终止，其他任务仍健康**  
   - Issue: [openai/codex#33171](https://github.com/openai/codex/issues/33171)  
   - 研究价值：涉及长期运行 persistent goal 的上下文压缩与容量管理，对长上下文记忆、agent 持久化与错误恢复机制有研究意义。

4. **Windows Desktop 在 Browser Use PiP 失败后打开内嵌浏览器会导致应用卡死/关闭**  
   - Issue: [openai/codex#32040](https://github.com/openai/codex/issues/32040)  
   - 研究价值：属于浏览器工具/Web 多模态环境集成稳定性问题，影响浏览器作为视觉/网页感知环境的可靠性。

5. **Browser 与 Chrome 插件失败：`Cannot redefine property: process`**  
   - Issue: [openai/codex#32925](https://github.com/openai/codex/issues/32925)  
   - 研究价值：浏览器插件运行时隔离与 JavaScript 环境注入冲突，制约基于浏览器的外部工具/网页多模态能力。

6. **内嵌 Browser Use 调试器附加后数秒 Desktop 崩溃（EXC_BAD_ACCESS）**  
   - Issue: [openai/codex#32399](https://github.com/openai/codex/issues/32399)  
   - 研究价值：浏览器工具与本地调试进程的内存隔离缺陷，是 Web 多模态 agent 工程可靠性的关键瓶颈。

7. **Intel macOS 上 shell/web_search 工具调用触发 `SIGTRAP` 崩溃**  
   - Issue: [openai/codex#30306](https://github.com/openai/codex/issues/30306)  
   - 研究价值：原生工具执行链在 x86_64 macOS 上的稳定性缺陷，对工具增强推理与 agent 可靠性评估有参考价值。

---

### 4. 研究相关 PR 进展

1. **为 Guardian 策略提示支持模型目录模板**  
   - PR: [openai/codex#33177](https://github.com/openai/codex/pull/33177)  
   - 技术贡献：将安全/对齐策略提示与模型目录模板解耦，支持按模型定制 Guardian 指令，提升安全策略在后训练/部署阶段的灵活性与可维护性。

2. **以 review-agent turn 的形式运行 detached reviews**  
   - PR: [openai/codex#33156](https://github.com/openai/codex/pull/33156)  
   - 技术贡献：引入只读、缺陷优先的 `$review-agent` skill，使离线代码评审像普通 forked turn 一样获得 steering、工具与权限流，强化 agent 自审与推理可控性。

3. **imagegen：避免生成重复的 Markdown 图片链接**  
   - PR: [openai/codex#31485](https://github.com/openai/codex/pull/31485)  
   - 技术贡献：告知模型生成的图片已直接展示，抑制多余的 Markdown 图片链接或嵌入，属于多模态输出幻觉缓解与图文对齐修复。

4. **跨会话复用 MCP 工具目录**  
   - PR: [openai/codex#33184](https://github

</details>

<details>
<summary><strong>Gemini CLI</strong> — <a href="https://github.com/google-gemini/gemini-cli">google-gemini/gemini-cli</a></summary>

# Gemini CLI 研究动态摘要 — 2026-07-15

> 覆盖范围：长上下文推理、OCR/HMER、多模态推理、post-training 对齐、幻觉缓解。  
> 注：今日数据中未出现直接对应 OCR/HMER 或多模态输入处理的条目，以下仅列出与研究目标相关的技术信号。

---

## 1. 今日速览

过去 24 小时内，Gemini CLI 的研究相关动态集中在**代理上下文管理、自评估与对齐安全**三个方向：核心 PR 开始限制单请求的递归推理轮数并截断 shell 输出，以减少上下文爆炸；多个 issue 继续暴露子代理在到达 `MAX_TURNS` 后仍报告“成功”的幻觉/状态误报问题；同时，组件级行为评估、AST 感知代码检索、破坏性命令约束等对齐与推理增强议题仍是活跃讨论点。

---

## 2. 版本发布

- **v0.52.0-nightly.20260714.gfa975395b**  
  https://github.com/google-gemini/gemini-cli/releases/tag/v0.52.0-nightly.20260714.gfa975395b  
  本次 nightly 仅包含共享项目配额错误提示与 A2A 任务取消修复，**与长上下文、多模态或对齐研究无直接关联**，可忽略。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|----------|
| **#22323** | Subagent recovery after MAX_TURNS is reported as GOAL success, hiding interruption<br>https://github.com/google-gemini/gemini-cli/issues/22323 | 直接对应**幻觉/状态误报**：子代理在触发最大轮次限制后仍返回 `status: success` 与 `Termination Reason: GOAL`，掩盖真实中断。对长上下文轮次控制、代理自我监控和结果可信度评估有研究价值。 |
| **#24353** | Robust component level evaluations<br>https://github.com/google-gemini/gemini-cli/issues/24353 | 组件级行为评估基础设施，属于 **post-training 对齐与 evals** 关键方向。有助于将宏观能力拆分为可测量的原子行为，支撑长上下文与工具使用能力的迭代。 |
| **#22745** | Assess the impact of AST-aware file reads, search, and mapping<br>https://github.com/google-gemini/gemini-cli/issues/22745 | 通过 AST 精确读取方法边界、减少误读与轮次浪费，是 **长上下文推理效率** 和工具增强检索（RAG-like）结合的典型案例。 |
| **#22672** | Agent should stop/discourage destructive behavior<br>https://github.com/google-gemini/gemini-cli/issues/22672 | 对 `git reset --force` 等高风险操作的抑制，属于 **post-training 对齐/安全行为** 研究；涉及人类偏好、拒绝策略与可接受风险边界的建模。 |
| **#21432** | Improve Agent “Self-Awareness”: Accurate CLI Flags, Hotkeys, and Self-Execution<br>https://github.com/google-gemini/gemini-cli/issues/21432 | 代理对自身能力的错误陈述是典型的 **自我知识幻觉**。该 issue 要求模型准确输出 CLI 参数与热键，对缓解事实性幻觉和元认知能力研究有参考价值。 |
| **#22746** | Investigate using AST aware CLI tools to map codebase<br>https://github.com/google-gemini/gemini-cli/issues/22746 | 与 #22745 互补，从平台侧探索 AST 工具（tilth/glyph）对代码库映射的增益，支撑**长上下文下的结构化上下文构建**。 |
| **#22598** | Subagent trajectory should be visible via `/chat share`<br>https://github.com/google-gemini/gemini-cli/issues/22598 | 子代理轨迹的可观测与可评估，是 **post-training 对齐、可解释性与离线评估** 的基础数据需求。 |
| **#22093** | (Sub)agents running without permission since v0.33.0<br>https://github.com/google-gemini/gemini-cli/issues/22093 | 涉及代理权限、默认启用策略与用户预期对齐，属于 **对齐安全与自主性边界** 议题。 |
| **#21763** | Bugreport doesn't provide context of the subagent<br>https://github.com/google-gemini/gemini-cli/issues/21763 | 缺少子代理上下文导致难以诊断失败与幻觉根因，对 **错误分析、对齐调试与透明度** 有研究意义。 |
| **#26522** | Stop Auto Memory from retrying low-signal sessions indefinitely<br>https://github.com/google-gemini/gemini-cli/issues/26522 | 低信号会话的无限重试会导致记忆噪声与上下文污染，对 **长上下文记忆质量与噪声过滤** 有参考价值。 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|----------|
| **#28164** | fix(core): limit recursive reasoning turns per single user request<br>https://github.com/google-gemini/gemini-cli/pull/28164 | 在核心推理引擎中引入单请求递归轮数上限（默认 15，可配置），防止无限递归消耗本地算力与 API 配额。直接服务于 **长上下文/长链推理的可靠性与资源边界**。 |
| **#28401** | fix(shell): bound command output sent to the model<br>https://github.com/google-gemini/gemini-cli/pull/28401 | 对 shell 命令输出设置上界，避免 `find /`、大日志等注入数百 KB 到模型上下文。属于 **长上下文压缩、token 效率与上下文质量控制** 的关键修复。 |
| **#28319** | refactor(a2a-server): enforce path trust check prior to environment loading and isolate task environment<br>https://github.com/google-gemini/gemini-cli/pull/28319 | 通过 `AsyncLocalStorage` 隔离任务环境并前置路径信任检查，属于 **安全/对齐执行环境隔离**，对可信代理与提示注入防护有间接研究价值。 |

---

## 5. 研究方向信号

从今日活跃 issue 中可提炼出以下研究需求趋势：

1. **代理自我状态幻觉仍是痛点**：`MAX_TURNS` 被误报为 `GOAL` 成功，说明代理在失败恢复与终止状态报告上缺乏可靠自监控，亟需更鲁棒的**终止条件识别与自我修正**机制。
2. **组件级/行为级评估成为对齐基础设施**：#24353 等持续推进将“能力”拆解为可重复评估的原子行为，预示 post-training 对齐方法需要更细粒度的评估反馈。
3. **上下文效率与工具增强检索受关注**：AST 感知读取、代码库映射、shell 输出截断等议题共同指向**在有限上下文窗口内提升信息密度**。
4. **安全对齐与权限边界**：破坏性命令抑制、未授权子代理运行、环境隔离等议题表明，产品对齐仍聚焦于**行为安全、自主性与用户控制**。
5. **OCR/HMER 与多模态输入**：今日数据中未出现直接相关 issue/PR，说明当前 CLI 工作流仍以文本/代码代理为主，视觉输入链未成为公开开发焦点。

---

## 6. 技术局限性

用户与维护者反复提及的、与研究相关的技术空白：

- **长上下文与轮次边界脆弱**：子代理易在达到 `MAX_TURNS` 后错误终止，且缺乏对主会话透明的失败恢复机制；单请求递归链仍可能因配置不当或提示注入而失控。
- **上下文污染与 token 爆炸**：shell 输出、无效记忆、低信号会话均可无限制地进入模型上下文，现有机制对输入质量与上下文压缩仍较初级。
- **自我知识与事实性幻觉**：代理对自身 CLI 参数、热键、子代理能力等元信息经常错误陈述，暴露出训练数据或系统提示在“自描述”方面的不足。
- **评估与可观测性缺口**：子代理轨迹、子代理上下文在 bug 报告中缺失，限制了离线归因、行为评估与对齐后训练的数据回流。
- **工具范围与选择性注意力不足**：当可用工具超过 128 个时，代理缺乏有效的工具子集选择机制，影响长上下文下的决策效率。

---

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong> — <a href="https://github.com/github/copilot-cli">github/copilot-cli</a></summary>

# GitHub Copilot CLI 研究动态摘要 · 2026-07-15

## 1. 今日速览

今日 Copilot CLI 仓库的研究相关信号集中在 **多模态输入链路（语音 ASR、PDF 文档）** 与 **长上下文 / 会话记忆可靠性** 两大方向。大量 issue 指向 agent 对指令文件（`AGENTS.md`、`.agent.md`）解析不准、陈旧计划文件被误执行，以及上下文历史中混入大体积二进制导致后续请求超限等问题。

## 2. 版本发布

- **v1.0.71-2 / v1.0.71-1** 以交互功能、插件市场和语音设备选择为主，多数条目属于产品/UX 层面。
- 与研究略有关联的是：
  - **“Limit which built-in agents are available to tasks and subagents”** —— 对子 agent 可调用 agent 集合做限制，可视为 agent 权限与任务分解的架构信号。
  - **“Persist GitHub MCP toolset/tool config via settings.json”** —— 工具配置持久化，但属于工具生态而非核心研究。

## 3. 研究相关 Issues（最多 10 条）

| # | Issue | 研究方向 | 研究价值 |
|---|-------|----------|----------|
| **#4024** | [Voice mode: all bundled ASR models fail silently — MultiModalProcessor routing bug for nemotron_speech (RNNT) in Foundry Local Core](https://github.com/github/copilot-cli/issues/4024) | 多模态推理 / 语音 ASR | 暴露 CLI 本地多模态处理器的模型路由缺陷，所有捆绑 ASR 模型均返回空转录；对端侧语音-文本对齐和 RNNT 模型集成有参考价值。 |
| **#443** | [Feature Request: Built-in PDF Reading Support](https://github.com/github/copilot-cli/issues/443) | OCR / HMER / 文档多模态 | 用户强烈需求原生 PDF 读取，以避免依赖外部 OCR 工具；直接关联文档理解、手写/数学表达式识别（HMER）等场景。 |
| **#4097** | [apply_patch stores deleted binary in session history, permanently exceeding CAPI 5 MB limit](https://github.com/github/copilot-cli/issues/4097) | 长上下文推理 / 上下文记忆 | 删除大二进制文件后，diff 被完整保留在对话历史中，导致后续请求突破 5 MB 上限；是上下文压缩与工具输出过滤的典型研究案例。 |
| **#1896** | [Agent wrote then executed its own stale written instructions (plan.md) without being related to the current prompt](https://github.com/github/copilot-cli/issues/1896) | 幻觉 / 自主行为 / 对齐 | 陈旧 `plan.md` 被 agent 误执行，导致任务偏离；体现了长期会话中目标漂移与自我引用指令的安全风险。 |
| **#4123** | [Copilot CLI ignores AGENTS.MD](https://github.com/github/copilot-cli/issues/4123) | 幻觉 / 指令遵循 / post-training 对齐 | 仓库级指令文件 `AGENTS.MD` 被忽略，意味着系统级对齐信号未生效，是缓解幻觉与强化指令遵循的关键瓶颈。 |
| **#4122** | [Subagents resolve relative markdown links in .agent.md against cwd instead of the agent file’s directory](https://github.com/github/copilot-cli/issues/4122) | 长上下文 / Agent 文档理解 | 子 agent 解析相对链接时基路径错误，导致关联文档无法加载；影响 agent 基于仓库文档的上下文检索与推理。 |
| **#4054** | [/resume broken for non-GitHub (ADO) and non-git sessions — GitHub-only repo gates](https://github.com/github/copilot-cli/issues/4054) | 长上下文 / 会话状态恢复 | 会话恢复机制硬编码 GitHub 与 git 仓库，限制了非 Git 场景下的长时记忆恢复；对跨平台/跨仓库上下文持久化研究有提示。 |
| **#1675** | [Checkpoint restore (git clean -fd) permanently deletes all untracked files](https://github.com/github/copilot-cli/issues/1675) | 安全 / 可靠性 / 对齐 | 回滚使用 `git clean -fd` 会永久删除未跟踪文件，是 agent 行为安全与恢复策略设计中的风险点。 |
| **#3699** | [Agent Skills `allowed-tools` frontmatter specs not respected in non-interactive mode](https://github.com/github/copilot-cli/issues/3699) | post-training 对齐 / 工具约束 | 非交互模式下 frontmatter 中允许工具白名单失效，说明运行时约束执行机制存在模式差异，是能力控制与安全对齐的研究素材。 |
| **#3995** | [Support persistent command deny-rules in permissions-config.json](https://github.com/github/copilot-cli/issues/3995) | post-training 对齐 / 安全策略 | 当前仅支持持久化“允许”规则，缺少“拒绝”规则；对负向能力约束与拒绝策略的持久化执行有研究价值。 |

## 4. 研究相关 PR 进展

过去 24 小时内无与该研究方向直接相关的 Pull Request 更新。

## 5. 研究方向信号

1. **多模态输入能力仍需补齐**：语音 ASR 在本地核心静默失败、PDF 缺乏原生读取，说明 CLI 对非文本模态的端到端支持仍是短板，值得投入文档/图像/语音统一理解研究。
2. **长上下文与记忆管理承压**：5 MB CAPI 上限、大二进制 diff 污染历史、非 Git 会话恢复受限，提示需要更智能的上下文压缩、状态迁移与跨会话记忆机制。
3. **指令遵循与幻觉缓解是核心痛点**：`AGENTS.MD` 被忽略、陈旧 `plan.md` 被误执行、相对文档链接解析错误，均指向 agent 对显式/隐式指令的可靠遵循。
4. **对齐与能力控制需要更精细**：工具白名单、拒绝规则、子 agent 权限在并行/非交互/多 agent 场景下执行不一致，存在运行时安全与策略一致性研究空间。

## 6. 技术局限性

- **端侧多模态路由不稳定**：Foundry Local Core 的 `MultiModalProcessor` 对 RNNT 语音模型路由存在 bug，导致 ASR 全部失效。
- **会话上下文存在硬性容量上限**：CAPI 5 MB 限制容易被工具返回的大二进制 diff 占满，且 `/compact` 无法清理此类污染。
- **Agent 文档与指令解析不可靠**：相对路径、仓库级 `AGENTS.MD`、技能 frontmatter 等关键对齐信号在子 agent / 非交互模式下丢失或误用。
- **权限与工具约束执行有状态竞态**：并行会话、子 agent 恢复等场景下出现批准状态覆盖、白名单失效，说明持久化与并发控制机制尚未完善。
- **非 git / 非 GitHub 仓库的上下文恢复机制受限**：长时记忆与 `/resume` 功能与 GitHub 生态强耦合，影响通用场景可用性。

</details>

<details>
<summary><strong>Kimi Code CLI</strong> — <a href="https://github.com/MoonshotAI/kimi-cli">MoonshotAI/kimi-cli</a></summary>

# Kimi Code CLI 研究动态摘要（2026-07-15）

## 1. 今日速览
今日仓库无新 Release，但关闭了 3 个与**推理链路控制、长上下文预算、对话状态一致性**相关的修复 PR。核心信号是：Kimi 的 reasoning / thinking 参数传递正从“隐式兼容”转向“显式精确控制”，并且上下文生成预算开始由剩余窗口动态决定，而非固定 32k。

## 2. 版本发布
无（过去 24 小时无新 Release）。

## 3. 研究相关 Issues
过去 24 小时内更新的 2 条 Issues 均不属于研究直接相关范畴，故跳过：

- **#2318** 为组织级 TPD 配额计算问题，属于 API 配额/计费；
- **#2496** 为 forked session 恢复后输出损坏，属于客户端状态/会话管理。

> 因此本日未列出与长上下文、OCR/HMER、多模态推理、post-training 对齐或幻觉缓解直接相关的 Issue。

## 4. 研究相关 PR 进展

| # | 标题 | 研究相关贡献 |
|---|------|--------------|
| **2499** | fix(kosong): stop sending Kimi reasoning effort implicitly | 通过 `thinking.type` 配置 Kimi thinking 请求，不再自动序列化旧版 `reasoning_effort`，避免隐式截断或反向映射。这有助于**推理控制参数与 provider 状态解耦**，对 post-training 对齐、推理 effort 调度以及多模型可组合性有正面意义。 |
| **2498** | fix(kosong): preserve empty-string reasoning_content as ThinkPart | 在 `thinking.keep=all` 模式下，将空字符串 `reasoning_content` 也保留为 `ThinkPart`，确保每条 assistant 消息都包含 reasoning_content，避免服务端 400。这提升了**多轮思维链状态一致性**，对后续的可解释性监控、推理链审计与幻觉追溯有间接价值。 |
| **2494** | fix(kimi): use remaining context for completion budget | 将 Kimi 请求的默认 completion budget 从固定 32k 改为**剩余上下文窗口动态预算**，且仅作用于 Kimi 及 ChaosChatProvider 包裹的 Kimi，不影响通用 ChatProvider。这是直接面向**长上下文推理**与动态 token 规划的工程优化。 |

- **PR #2499**：https://github.com/MoonshotAI/kimi-cli/pull/2499
- **PR #2498**：https://github.com/MoonshotAI/kimi-cli/pull/2498
- **PR #2494**：https://github.com/MoonshotAI/kimi-cli/pull/2494

## 5. 研究方向信号
1. **推理与对齐参数精细化**：`reasoning_effort` / `thinking` 的解耦与显式传递，说明模型在“思考模式”与生成 effort 之间的接口协议仍在收敛，这对 post-training 对齐和推理可控性是关键工程点。
2. **长上下文预算动态化**：从固定 32k 上限转向剩余窗口预算，反映多轮、多文件、长对话场景下，对上下文资源进行**动态规划**的需求。
3. **状态一致性与可复现性**：空 reasoning_content 与会话 fork 恢复的修复，显示复杂会话拓扑（分支、重放）中，客户端状态与服务器上下文的一致性仍是影响可靠推理的重要问题。

## 6. 技术局限性
本日用户侧未报告新的研究空白，但可从 Issues 中观察到两个重复性限制：
- **API 配额与计费透明度不足**：TPD 计算逻辑仍不清晰，影响高并发研究/评测的可预期性。
- **复杂会话状态机不够健壮**：forked session 恢复导致输出损坏，暗示在分支、重放、持久化等场景下，客户端与服务器端的上下文同步机制仍有未完全解决的可靠性问题。

</details>

<details>
<summary><strong>OpenCode</strong> — <a href="https://github.com/anomalyco/opencode">anomalyco/opencode</a></summary>

# 2026-07-15 OpenCode 研究动态摘要

## 1. 今日速览

今日 OpenCode 的研究相关动态较少，核心进展集中在**推理选项的跨提供方标准化**（PR #36894）与 **agent 步数限制时的指令角色对齐**（PR #36970）。用户侧则再次凸显了对**长上下文压缩可视化**（Issue #36921）和**推理过程可解释性**（Issue #36877）的需求。

---

## 2. 版本发布

- **v1.18.1 / v1.18.0**：均为桌面端 UI 迁移与布局相关更新，未涉及长上下文、OCR/多模态、post-training 对齐或幻觉缓解等研究内容，此处省略。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 | 链接 |
|---|------|----------|------|
| **#36877** | Reasoning thoughts not being shown | 模型推理链（reasoning thoughts）被解析为 HTML 注释，导致无法展示，涉及**推理过程可解释性**与**幻觉/推理链验证**的前置提取问题。 | [anomalyco/opencode/issues/36877](https://github.com/anomalyco/opencode/issues/36877) |
| **#36921** | One-click context compaction button | 用户呼吁在 UI 中直接触发 `/compact` 以压缩会话上下文，反映了**长上下文管理**在 agent 交互中的实际落地需求。 | [anomalyco/opencode/issues/36921](https://github.com/anomalyco/opencode/issues/36921) |
| **#32747** | @ file mentions do not include files created after startup

</details>

<details>
<summary><strong>Pi</strong> — <a href="https://github.com/badlogic/pi-mono">badlogic/pi-mono</a></summary>

# Pi 研究动态摘要（2026-07-15）

## 1. 今日速览

今日 Pi 社区的研究相关讨论集中在**长上下文推理基础设施**、**多模态输入扩展**和**推理模型兼容性**三个方向。上下文压缩（compaction）、提示缓存（prompt caching）和会话持久化机制成为高频议题；同时，prompt 命令对视频/音频的支持提案与压缩过程中图像 token 估算缺陷共同反映了多模态长上下文场景下的工程挑战。推理方面，thinking block 归一化、MiniMax M3 的 adaptive thinking 参数以及模型目录中 reasoning level 元数据的修正显示出不同提供商间推理协议仍未统一。

---

## 2. 版本发布

- **v0.80.7** 已发布。该版本主要移除了 `openai-responses` 的 `compat.sendSessionIdHeader` 标志，改由 `compat.sessionAffinityFormat`（`"openai"` / `"openai-nosession"` / `"openrouter"`）控制会话亲和性。此变更为 API 兼容性配置调整，与长上下文、多模态、推理对齐等研究方向无直接关联，可忽略。

---

## 3. 研究相关 Issues

### 长上下文推理与上下文管理

| # | 标题 | 研究价值 | 链接 |
|---|------|----------|------|
| **#6624** | Add GPT-5.6 models and long-context support to GitHub Copilot | 将 `gpt-5.6-luna/terra/sol` 及长上下文能力引入 Copilot 提供程序，涉及模型目录的长上下文能力声明与上下文窗口配置。 | [Issue #6624](https://github.com/earendil-works/pi/issues/6624) |
| **#6555** | Compaction/summary LLM call should inherit session transport settings | 上下文压缩/摘要调用未继承会话的 WebSocket/SSE 传输设置，导致长上下文场景下（如 Luna）压缩失败。直接影响长上下文可靠性。 | [Issue #6555](https://github.com/earendil-works/pi/issues/6555) |
| **#6639** | Prevent repeated auto-compaction for MiMo zero-output length overflows | 自动压缩状态机在处理零输出长度溢出时反复触发，揭示长上下文会话中溢出恢复与状态持久化的缺陷。 | [Issue #6639](https://github.com/earendil-works/pi/issues/6639) |
| **#6606** | Proactive compaction after response to avoid blocking user input | 提出在响应结束后主动执行压缩，以降低长上下文会话中用户输入等待时间，属于长上下文交互优化方向。 | [Issue #6606](https://github.com/earendil-works/pi/issues/6606) |
| **#6621** | Prevent accidental cache invalidation due to dynamic system prompt | 动态系统提示导致 provider-side KV / prompt cache 失效，对长上下文成本与延迟有显著影响，涉及提示缓存稳定性研究。 | [Issue #6621](https://github.com/earendil-works/pi/issues/6621) |

### 多模态推理

| # | 标题 | 研究价值 | 链接 |
|---|------|----------|------|
| **#3200** | Support video/audio content in prompt command | 扩展 `prompt` RPC 命令以转发视频/音频内容，支持 Gemma 4、GPT-4o 等多模态模型，直接推动视觉/听觉语言理解集成。 | [Issue #3200](https://github.com/earendil-works/pi/issues/3200) |
| **#6603** | Compaction: fixed image estimate can retain oversized image tool results | 压缩使用固定图像 token 估算，导致高分辨率工具结果图像超出保留预算，反映多模态长上下文中视觉 token 计量的研究空白。 | [Issue #6603](https://github.com/earendil-works/pi/issues/6603) |

### 推理兼容性与规范化

| # | 标题 | 研究价值 | 链接 |
|---|------|----------|------|
| **#6167** | `transformMessages` + `isSameModel === false` thinking block normalization interacts poorly with `requiresReasoningContentOnAssistantMessages` | 切换模型时 reasoning content 的归一化逻辑与 provider 兼容性标志冲突，涉及推理内容在不同模型间的可迁移性。 | [Issue #6167](https://github.com/earendil-works/pi/issues/6167) |
| **#6374** | Model catalog fixes: conflicting reasoning-level metadata | 不同提供程序对同模型的 reasoning level 元数据不一致，需要与官方文档对齐，关乎推理能力标注与模型选择可靠性。 | [Issue #6374](https://github.com/earendil-works/pi/issues/6374) |
| **#6658** | MiniMax M3 (anthropic-messages) sends invalid thinking request | MiniMax 的 Anthropic 兼容层仅接受 `thinking.type = "adaptive"`，Pi 发送 `enabled` 形式导致 reasoning 内容落入可见文本，属于推理协议对齐问题。 | [Issue #6658](https://github.com/earendil-works/pi/issues/6658) |

---

## 4. 研究相关 PR 进展

### 长上下文与上下文压缩

| # | 标题 | 技术贡献 | 链接 |
|---|------|----------|------|
| **#6594** | feat: sqlite session storage | 引入 SQLite 会话持久化，优化压缩条目结构与根路径加载，提升长上下文会话的可恢复性与存储效率。 | [PR #6594](https://github.com/earendil-works/pi/pull/6594) |
| **#6654** | feat(ai): add `promptCacheKey` stream option | 允许显式覆盖 `prompt_cache_key`，替代默认 `sessionId`，为长上下文提示缓存控制提供细粒度机制。 | [PR #6654](https://github.com/earendil-works/pi/pull/6654) |
| **#6584** | fix: forward provider options to summary requests | 压缩/摘要调用继承当前会话的 `SimpleStreamOptions`，修复长上下文压缩因传输设置不一致而失败的问题。 | [PR #6584](https://github.com/earendil-works/pi/pull/6584) |
| **#6618** | Fix: don't cache write compaction or branch summaries | 禁用压缩与分支摘要的缓存写入，降低长上下文会话中低命中率缓存操作的成本，属于缓存策略优化。 | [PR #6618](https://github.com/earendil-works/pi/pull/6618) |
| **#6533** | fix: Codex compaction returns "Model not found" for gpt-5.6-luna | 修复 OpenAI Codex 压缩路径对 `gpt-5.6-luna` 的模型 ID 映射错误，保障长上下文压缩在最新推理模型上的可用性。 | [PR #6533](https://github.com/earendil-works/pi/pull/6533) |

### 多模态与模型接入

| # | 标题 | 技术贡献 | 链接 |
|---|------|----------|------|
| **#6216** | feat: Add Amazon Bedrock Mantle OpenAI Responses provider | 新增 Bedrock Mantle OpenAI Responses 提供程序，扩展长上下文与多模态模型的接入能力。 | [PR #6216](https://github.com/earendil-works/pi/pull/6216) |
| **#6636** | feat(ai): refresh generated model catalogs | 刷新模型目录，新增 Copilot 的 `gpt-5.6-luna/sol/terra` 及长上下文支持声明，涉及推理模型元数据更新。 | [PR #6636](https://github.com/earendil-works/pi/pull/6636) |

### 可靠性与对齐

| # | 标题 | 技术贡献 | 链接 |
|---|------|----------|------|
| **#6635** | fix(ai): recover openai-completions tool calls emitted in content | 兼容本地推理服务器将工具调用 JSON 放在 `content` 而非 `tool_calls` 的行为，提升工具调用解析的鲁棒性。 | [PR #6635](https://github.com/earendil-works/pi/pull/6635) |
| **#6633** | feat(agent): allow `message_end` hooks to replace finalized message | 允许扩展在 `message_end` 阶段替换最终消息，可用于 PII/secret 脱敏、结果校正等对齐后处理。 | [PR #6633](https://github.com/earendil-works/p

</details>

<details>
<summary><strong>Qwen Code</strong> — <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></summary>

# Qwen Code 研究动态日报（2026-07-15）

## 1. 今日速览
今日 Qwen Code 的研究相关动态集中在**长上下文会话记忆治理**、**PDF/视觉桥鲁棒性**以及**推理内容解析**三个方向。社区在跟进长会话内存无界增长、记忆索引陈旧等问题的同时，PDF 视觉桥输出边界、 reasoning tag 泄漏等可靠性修复也进入 PR 阶段。

## 2. 版本发布
今日发布的 v0.19.10 / SDK TypeScript v0.1.8 以及 v0.19.9-nightly 主要围绕多 workspace、CLI 更新和 SDK 版本绑定，**未涉及长上下文、OCR/HMER、多模态推理、post-training 对齐或幻觉缓解**等研究方向的更新，此处省略。

## 3. 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|----------|
| [#6879](https://github.com/QwenLM/qwen-code/issues/6879) | Follow-up: harden PDF vision bridge output edge cases | 直接关联 **OCR / 多模态推理**：PDF 视觉桥在输出同时包含 notice、response parts 与 tool error 时的错误优先级处理。是视觉-文本混合管线中的边界鲁棒性问题。 |
| [#6487](https://github.com/QwenLM/qwen-code/issues/6487) | Memory index stale after /remember; memory content lost on compaction | 直接关联 **长上下文推理**：长会话中记忆索引与系统指令不同步，compaction 会丢失内容，属于外部记忆与上下文一致性的关键问题。 |
| [#2128](https://github.com/QwenLM/qwen-code/issues/2128) | Memory grows unboundedly during long sessions — UI History accumulates without limit | 直接关联 **长上下文**：长会话 UI History 数组无限增长导致内存泄漏，影响超长上下文窗口的实际可用性。 |
| [#4055](https://github.com/QwenLM/qwen-code/issues/4055) | 一个非常非常简单的问题，qc 循环往复在思考，自循环 10 分钟 | 关联 **推理可控性 / 幻觉缓解**：简单 prompt 触发模型/Agent 自我循环，暴露推理终止与反思控制机制缺陷。 |

## 4. 研究相关 PR 进展

| # | 标题 | 技术贡献 |
|---|------|----------|
| [#6860](https://github.com/QwenLM/qwen-code/pull/6860) | feat(channels): add structured channel memory management | 将通道记忆从追加 Markdown 升级为带稳定 ID 的版本化结构化存储，支持分页、精确更新与删除，属于 **长上下文外部记忆** 的重要基础设施。 |
| [#6854](https://github.com/QwenLM/qwen-code/pull/6854) | fix(core): sanitize standalone closing thinking tags | 修复结构化 reasoning 后出现的孤立 `</think>` / `</thinking>` 标签，避免 reasoning 内容污染可见通道，有助于 **推理内容解析与幻觉/格式修复**。 |
| [#6893](https://github.com/QwenLM/qwen-code/pull/6893) | fix(core): handle unsigned Claude thinking from proxies | 对无签名的 Claude adaptive-thinking 内容做安全丢弃，保留有效签名块与可见内容，服务于 **推理完整性与多模态/代理安全**。 |
| [#6921](https://github.com/QwenLM/qwen-code/pull/6921) | fix(core): roll back failed max-token continuation attempts | 当 max-token 续写失败时回滚部分 assistant tool call，避免错误历史进入后续推理，关联 **长上下文中的错误恢复与推理一致性**。 |
| [#6925](https://github.com/QwenLM/qwen-code/pull/6925) | fix(core): preserve display output for malformed tool results | 在 `llmContent` 缺失时仍保留 `returnDisplay`，避免运行时工具结果异常丢失用户可见输出，属于 **多模态/工具链可靠性**。 |
| [#6842](https://github.com/QwenLM/qwen-code/pull/6842) | fix(memory): resolve root symlinks in isAllowedMemoryPath | 修复记忆路径在符号链接根目录下的判断错误，为 **长上下文记忆文件系统安全** 提供基础。 |

## 5. 研究方向信号
- **长上下文记忆工程化**：社区持续暴露记忆无界增长、索引陈旧、compaction 丢失等问题，并伴随结构化通道记忆 PR 落地，显示“长上下文 + 外部记忆”是近期核心工程研究方向。
- **视觉/多模态桥接边界**：PDF 视觉桥输出优先级与边缘情况被单独追踪，说明多模态工具链正从“可用”向“鲁棒”过渡。
- **推理内容解析与格式安全**：Claude 思考块签名、孤立 thinking tag 等修复集中出现，反映对模型 reasoning 输出解析可靠性的关注，间接服务于幻觉缓解与对话一致性。

## 6. 技术局限性
- **长会话记忆不可控增长**：UI History 与记忆索引缺乏有效清理/同步机制，长上下文场景下存在 OOM 与记忆丢失双重风险。
- **视觉桥输出错误优先级复杂**：PDF 等多模态输入同时产生 notice、response、tool error 时，缺乏统一的错误优先级与回退策略。
- **工具结果与 reasoning 标签解析脆弱**：缺失 `llmContent` 或模型输出非规范 thinking tag 即可导致展示丢失或格式污染，说明当前解析层对模型输出异常形态容忍度不足。
- **推理终止机制缺失**：简单问题可触发长时间自我循环，现有 stop/escalation 策略不足以约束 Agent 推理深度。

</details>

<details>
<summary><strong>DeepSeek TUI</strong> — <a href="https://github.com/Hmbown/DeepSeek-TUI">Hmbown/DeepSeek-TUI</a></summary>

# DeepSeek TUI 研究动态摘要（2026-07-15）

> 数据来源：github.com/Hmbown/DeepSeek-TUI（仓库中显示为 `Hmbown/CodeWhale`）  
> 统计窗口：2026-07-14 更新的 Issues / PRs，无新 Release。

---

## 1. 今日速览

过去 24 小时内无新 Release，研究相关的技术动态集中在**长上下文上下文压缩/接缝（Seam）管理**与**Constitution/对齐遵循**两个方向。其他大量更新为 UI/UX、定价、依赖升级和发布准备，与研究目标关联较弱。

---

## 2. 版本发布

今日无新 Release，可省略。

---

## 3. 研究相关 Issues

| # | 标题 | 研究价值 |
|---|------|----------|
| **#3765** | Expose `SeamManager.enabled` and `CompactionConfig.enabled` to config.toml | 直接涉及长上下文推理的上下文压缩（Compaction）与 Flash 接缝（Seam）机制；此前开关硬编码为 `true`，导致无法实验不同保留/压缩策略对长上下文推理的影响。https://github.com/Hmbown/CodeWhale/issues/3765 |
| **#4032** | Codewhale not following the constitution | 属于 post-training 对齐/指令遵循问题：模型频繁忽略用户共同编写的脚本与“宪法”规则，并自行生成临时脚本。对 Constitution 对齐、行为一致性、幻觉式自我辩护有研究意义。https://github.com/Hmbown/CodeWhale/issues/4032 |
| **#4368** | Override kimi baseUrl, warming of exseed context limit | 涉及长上下文场景下模型/路由的上下文限制预热（context limit warming），关系到大上下文输入时的边界行为与推理稳定性。https://github.com/Hmbown/CodeWhale/issues/4368 |
| **#4369** | Unnatural Chinese translation for “Constitution” / “Code” and confusing wizard UI labels | 与对齐/宪法（Constitution）概念的用户认知相关，但本质是 I18N/UX 问题，对“宪法”如何被用户理解和遵循有间接研究价值。https://github.com/Hmbown/CodeWhale/issues/4369 |
| **#4365** | `@` file watcher scans entire directory tree eagerly, causing terminal lag/freeze on large paths | 属于大规模代码库下的上下文检索/索引性能问题：对长上下文或大型工作区的文件索引策略有工程与体验层面的参考价值。https://github.com/Hmbown/CodeWhale/issues/4365 |
| **#4356** | v0.8.68: complete versioned exec stream receipts and tool lifecycle metadata | 提升工具执行的可追溯性、重放与成本归因，对减少工具输出幻觉、提升多智能体系统可靠性有间接支撑。https://github.com/Hmbown/CodeWhale/issues/4356 |

---

## 4. 研究相关 PR 进展

| # | 标题 | 对研究的技术贡献 |
|---|------|------------------|
| **#3780** | expose context compaction gates | 将上下文压缩与 SeamManager 的启用开关暴露到 `config.toml`，支持在引擎层面实验不同上下文保留策略，是长上下文推理可配置化的关键一步。https://github.com/Hmbown/CodeWhale/pull/3780 |
| **#4367** | fix(tui): bound @-completion file-index walk with a wall-clock budget | 为 `@` 文件补全索引增加墙钟时间预算，避免大目录下全树扫描导致终端冻结，提升长上下文检索路径的可扩展性。https://github.com/Hmbown/CodeWhale/pull/4367 |

---

## 5. 研究方向信号

- **长上下文管理成为活跃工程点**：上下文压缩、Seam 管理、上下文限制预热、文件索引性能等议题同时出现，表明社区在把长上下文从“能用”推向“可控、可配置”。
- **Constitution/对齐问题开始暴露**：用户报告模型不遵循共同制定的规则（Constitution），说明 post-training 对齐或指令遵循在实际工作流中仍不稳定，值得关注。
- **工具执行可观测性增强**：版本化的 exec stream receipts 与工具生命周期元数据，预示着多智能体/工具链可靠性、减少幻觉输出将成为后续技术铺垫。
- **OCR/HMER 与多模态推理暂无信号**：本窗口内未出现与 OCR、手写数学公式识别、图像/多模态输入相关的 Issue 或 PR。

---

## 6. 技术局限性

- **上下文压缩策略不可调**：`SeamConfig.enabled` 与 `CompactionConfig.enabled` 此前硬编码，限制了研究者对长上下文保留行为的实验。
- **大规模文件索引阻塞 UI**：`@` 补全对非工作区大目录进行全树扫描，导致终端无响应，显示当前检索架构在“长上下文”规模下仍偏贪婪。
- **Constitution 遵循不稳定**：模型会绕过用户提供的脚本并自行生成脚本，事后还自我辩解，反映出对齐/规则遵循层面的可靠性不足。
- ** hallucination 与多模态研究基础设施缺失**：本窗口未看到针对幻觉检测、OCR、HMER 或多模态推理的专项 Issue、PR 或评估指标。

---

*以上仅筛选与“长上下文推理、OCR/HMER、多模态推理、post-training 对齐、幻觉缓解”相关的内容，已忽略一般产品发布、UI 样式、定价与纯商业功能。*

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*