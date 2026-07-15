# OpenClaw 生态日报 2026-07-15

> Issues: 500 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-15 00:20 UTC

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

# 个人 AI 助手 / 自主智能体开源生态横向对比（2026-07-15）

## 1. 生态全景

过去 24 小时，主流 Agent 框架呈现“工程密度高、基础模型研究弱”的整体态势：IronClaw、ZeroClaw 等核心项目仍在高频推进运行时架构与稳定性治理；PicoClaw、Moltis、NanoClaw 以 Provider 适配、本地小模型兼容和通道集成为主；OpenClaw、NanoBot、Hermes Agent、CoPaw 因摘要失败未能纳入当日可比范围。生态已经从“拼功能”转向“拼可靠性、可观测性与成本可控”，但视觉语言、推理机制等前沿研究信号尚未在公开社区集中涌现。

---

## 2. 各项目活跃度对比

| 项目 | Issues 数 | PRs 数 | 版本发布 | 健康度/阶段评估 |
|---|---|---|---|---|
| **OpenClaw** | — | — | 无 | 摘要生成失败，无法评估 |
| **NanoBot** | — | — | 无 | 摘要生成失败，无法评估 |
| **Hermes Agent** | — | — | 无 | 摘要生成失败，无法评估 |
| **PicoClaw** | 3（新增/活跃） | 9（5 已关闭/合并，4 待合并） | 无 | 稳定维护，Provider 层优化为主，研究信号弱 |
| **NanoClaw** | 0 | 26（19 开放，7 已关闭/合并） | 无 | 维护密集，稳定性与通道集成优先 |
| **NullClaw** | 0 | 0 | 无 | 24 小时无活动 |
| **IronClaw** | 49（37 活跃/新开，12 关闭） | 50（23 待合并，27 已关闭/合并） | 无 | 高速迭代，但稳定性与 CI 债务显著 |
| **LobsterAI** | ~4（均为关闭） | ~3（均为关闭） | 无 | 稳定收敛，主要做 OpenClaw backport 与 stale 清理 |
| **TinyClaw** | 0 | 0 | 无 | 24 小时无活动 |
| **Moltis** | 3（2 开放，1 关闭） | 12（8 已关闭/合并，4 待合并） | 20260714.11 | 活跃发布，关注本地小模型兼容与语音输入 |
| **CoPaw** | — | — | 无 | 摘要生成失败，无法评估 |
| **ZeptoClaw** | 0 | 0 | 无 | 24 小时无活动 |
| **ZeroClaw** | 32（24 活跃/新开，8 关闭） | 50（26 待合并，24 已关闭/合并） | 无 | 高强度冲刺，记忆架构与目标控制双栈并行 |

---

## 3. 研究定位分析

| 项目 | 多模态推理 | 长上下文/上下文效率 | 对齐/可靠性/安全 | 技术路线特点 |
|---|---|---|---|---|
| **PicoClaw** | 无直接信号 | Bedrock/Anthropic prompt caching、token 用量暴露 | 工具调用流式稳定性、JSON Schema 校验、SecureString 安全 | **Provider-First**：聚焦多模型接入、渠道消息渲染与成本可观测 |
| **NanoClaw** | 语音/附件回退（Telegram 语音/音频） | skill 按需注入 | 安装安全、环境变量隔离、容器镜像供应链 | **多通道+安全**：以 Slack/Telegram/Discord/Dial 集成和运行时安全为主 |
| **IronClaw** | 无直接信号 | 上下文预览上限、skill 按需激活、context cache | self-verification pass、错误保真度、工具参数形状 CI 验证、记忆隔离 | **Reborn 架构+Benchmark 驱动**：强调推理循环、测试覆盖与错误状态真实 |
| **LobsterAI** | 无 | 无 | OpenClaw Agent tool-loop 终止、aborted tool run 边界 | **OpenClaw 衍生**：以稳定性 backport 与消费级 UX 为主 |
| **Moltis** | 本地 STT（FunASR/SenseVoice 请求） | 工具结果持久化截断、上下文命令注入 | 小模型工具参数类型强制化、浏览器工具空值容错 | **本地/隐私优先**：兼容 Gemma 4 / oMLX 等端侧小模型 |
| **ZeroClaw** | 无直接信号 | Hindsight 记忆后端、对话历史与长期记忆解耦、Slack thread 上下文回填 | SOP 审批门、goal 委托边界、多租户 RBAC、工具调用参数验证 | **治理型 Agent**：SOP/goal 控制 + 企业级权限与审计 |

> **总体判断**：视觉语言（VLM）研究在 Agent 框架层尚未形成公开讨论；长上下文、记忆架构、工具可靠性与错误保真度是当前最活跃的研究-工程交叉点。

---

## 4. 共同关注的技术方向

| 方向 | 涉及项目 | 具体诉求/关键条目 |
|---|---|---|
| **工具调用可靠性** | PicoClaw、IronClaw、ZeroClaw、Moltis、LobsterAI | 流式 tool_calls 不丢失、self-verification、loop 终止、参数 JSON 校验、小模型标量参数字符串化 |
| **长上下文成本与效率** | PicoClaw、IronClaw、Moltis、ZeroClaw | prompt caching、上下文窗口预览上限、工具结果截断、skill 按需注入、记忆分层 |
| **错误保真度 / 反幻觉** | IronClaw、ZeroClaw、PicoClaw | 禁止“成功但 delivery 失败”的泛化错误、test-connection 误报、审批门绕过、默认模型限速失效 |
| **本地/小模型兼容** | Moltis、PicoClaw | 小模型输出 `null`/`stringified` 参数、LM Studio 严格 JSON Schema |
| **安全与权限边界** | ZeroClaw、NanoClaw、IronClaw | 多租户 RBAC、工具访问策略隔离、容器镜像拉取控制、记忆隔离 |
| **可观测性** | PicoClaw、ZeroClaw、IronClaw | 每轮 token 用量、OTel 跨轮次 conversation ID、CI 信号真实化 |
| **渠道与多模态输入** | PicoClaw、NanoClaw、ZeroClaw、Moltis | 钉钉/飞书原生消息、Telegram/Discord/Dial、本地语音 STT |

---

## 5. 差异化定位分析

| 维度 | 代表项目 | 关键差异 |
|---|---|---|
| **运行时架构** | ZeroClaw（SOP/goal + Hindsight 记忆）、IronClaw（Reborn + benchmark profile） | ZeroClaw 强调“治理流程驱动”；IronClaw 强调“以评测数据驱动上下文/成本调优” |
| **接入层重心** | PicoClaw（Bedrock/Anthropic/钉钉/飞书）、NanoClaw（多通道安全） | PicoClaw 做深企业 IM 与云端模型；NanoClaw 做广通道覆盖与安装安全 |
| **部署形态** | Moltis（本地小模型 + 语音）、LobsterAI（OpenClaw 消费级衍生） | Moltis 面向隐私/端侧；LobsterAI 面向终端用户 UI 体验 |
| **目标用户** | ZeroClaw → 企业工作流；IronClaw → 构建复杂 Agent 的开发者；PicoClaw → 多模型企业集成；Moltis → 本地/隐私用户 | 生态已出现明显的垂直分层 |
| **技术债务类型** | IronClaw（CI flaky、并发消息乱序）、ZeroClaw（大型 PR 栈未合并）、PicoClaw（stale 积压） | 高活跃项目普遍存在“稳定性与治理

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目日报 — 2026-07-15

> 研究视角说明：今日 PicoClaw 的活跃度以基础设施、Provider 适配和渠道消息渲染为主，**未出现直接涉及视觉语言（VLM）、推理机制、训练方法或幻觉治理的研究型 Issue/PR**。以下按研究分析师关注的「长上下文效率、工具可靠性、AI 可观测性、系统安全」等维度进行筛选与解读。

---

## 1. 今日速览

- 今日无新版本发布；过去 24 小时社区活跃度中等，新增/活跃 **Issue 3 条**、**PR 9 条**（其中 5 条已合并/关闭，4 条待合并）。
- 代码动向集中在 **Provider 层优化**（Bedrock/Anthropic 的 prompt caching、tool_calls 流式稳定性、token 用量暴露）与 **渠道消息渲染**（钉钉会话列表预览、飞书原生音视频），整体未向核心模型能力或对齐研究延伸。
- 最受关注的社区诉求是 **替换 libolm 加密库**（[sipeed/picoclaw#3088](https://github.com/sipeed/picoclaw/issues/3088)），该 issue 已被标记为 `help wanted` 和 `priority: high`。
- 稳定性方面出现两例新 bug：仅配置默认模型时速率限制失效（[sipeed/picoclaw#3232](https://github.com/sipeed/picoclaw/issues/3232)），以及钉钉聊天列表预览文案固定显示为“PicoClaw”（[sipeed/picoclaw#3255](https://github.com/sipeed/picoclaw/issues/3255)）。
- 项目健康度：交付节奏平稳，但存在多条 stale/open 的 PR/Issue 积压；在 VLM、推理、训练、幻觉等研究方向上无新信号。

---

## 2. 版本发布

**无。**

今日未发布新版本。

---

## 3. 项目进展（今日合并/关闭的重要 PR）

| PR | 标题 | 推进方向 |
|---|---|---|
| [sipeed/picoclaw#2982](https://github.com/sipeed/picoclaw/pull/2982) | fix(bedrock): drop temperature for models that deprecate it (Opus 4.8) | 修复 Claude Opus 4.8 在 Bedrock 上因 `temperature` 参数被弃用而失败的 400 错误，保证模型升级兼容性。 |
| [sipeed/picoclaw#2957](https://github.com/sipeed/picoclaw/pull/2957) | fix(channels): prevent tool_calls from being dropped during streaming | 修复流式场景下 `tool_calls` 被误过滤的问题，提升 **function calling / agent 可靠性**；新增 `outboundMessageIsToolCalls()` 辅助函数。 |
| [sipeed/picoclaw#2270](https://github.com/sipeed/picoclaw/pull/2270) | fix(config): handle non-addressable SecureString values in collectSensitive | 修复反射读取 map 中 `SecureString` 时 `v.Addr()` panic 的崩溃问题，增强配置安全与稳定性。 |
| [sipeed/picoclaw#2128](https://github.com/sipeed/picoclaw/pull/2128) | fix(tools): ensure tool parameters have valid JSON Schema properties field | 补全工具参数的 JSON Schema `properties` 字段，修复与 OpenAI 严格兼容 API（如 LM Studio）的 schema 校验失败。 |
| [sipeed/picoclaw#3156](https://github.com/sipeed/picoclaw/pull/3156) | feat(pico): emit per-turn LLM token usage on finalized message | 在 Pico 通道的最终消息上暴露每轮输入/输出 token 用量，提升 **可观测性与成本审计** 能力。 |

仍在推进的 PR 包括：
- [sipeed/picoclaw#3163](https://github.com/sipeed/picoclaw/pull/3163)：Bedrock Converse prompt caching（cache points）。
- [sipeed/picoclaw#3228](https://github.com/sipeed/picoclaw/pull/3228)：Anthropic `SystemParts` 按块携带 `cache_control`。
- [sipeed/picoclaw#3233](https://github.com/sipeed/picoclaw/pull/3233)：PR #3222 的向后兼容修复。
- [sipeed/picoclaw#3256](https://github.com/sipeed/picoclaw/pull/3256)：飞书以原生音频/视频消息类型发送媒体。

---

## 4. 社区热点（今日讨论最活跃、反应最多的 Issue/PR）

- **[sipeed/picoclaw#3088](https://github.com/sipeed/picoclaw/issues/3088)**：8 条评论、2 个 👍、`priority: high`  
  用户希望将 `libolm` 替换为官方继任库 `vodozemac`，因为 `libolm` 已无人维护且存在安全风险。  
  **背后诉求**：项目安全基线升级；希望 `libolm` 在编译期变为可选依赖，以便平滑迁移。

- **[sipeed/picoclaw#3232](https://github.com/sipeed/picoclaw/issues/3232)**：1 条评论、`stale`  
  仅配置 `agents.defaults.model_name` 而不设置 fallback 模型时，该模型的 RPM 限制失效。  
  **背后诉求**：默认模型应享受与 fallback 模型一致的限速策略，避免意外超配成本。

- **[sipeed/picoclaw#3255](https://github.com/sipeed/picoclaw/issues/3255)**：0 评论  
  钉钉渠道回复在聊天列表预览中始终显示固定文本“PicoClaw”，而非实际回复内容。  
  **背后诉求**：渠道消息透出需要符合平台 UX，避免用户在会话列表无法识别内容。

今日 PR 均无可见评论热度。

---

## 5. Bug 与稳定性（按严重程度排序）

| 严重度 | 问题 | 状态 |
|---|---|---|
| **高** | **libolm 安全依赖过时**（[sipeed/picoclaw#3088](https://github.com/sipeed/picoclaw/issues/3088)）：官方已标记为不安全，尚无 fix PR。 | OPEN，无修复 PR |
| **中高** | **默认模型速率限制失效**（[sipeed/picoclaw#3232](https://github.com/sipeed/picoclaw/issues/3232)）：无 fallback 配置时 RPM 不生效，可能导致超限。 | OPEN，无修复 PR |
| **低** | **钉钉聊天列表预览文案错误**（[sipeed/picoclaw#3255](https://github.com/sipeed/picoclaw/issues/3255)）：仅影响展示，不影响聊天内内容。 | OPEN，无修复 PR |

同时今日已关闭的修复 PR（[#2982](https://github.com/sipeed/picoclaw/pull/2982)、[#2957](https://github.com/sipeed/picoclaw/pull/2957)、[#2270](https://github.com/sipeed/picoclaw/pull/2270)、[#2128](https://github.com/sipeed/picoclaw/pull/2128)）覆盖了模型参数兼容、工具调用稳定性、配置反射安全和 JSON Schema 校验，整体稳定性有正向修复。

---

## 6. 功能请求与路线图信号

- **长期上下文 / Prompt Caching**  
  - [sipeed/picoclaw#3163](https://github.com/sipeed/picoclaw/pull/3163)：Bedrock Converse 通过 `cache points` 实现前缀缓存，直接关联 **长上下文推理成本与延迟优化**。  
  - [sipeed/picoclaw#3228](https://github.com/sipeed/picoclaw/pull/3228)：Anthropic `SystemParts` 支持按块 `cache_control`，使系统提示缓存可表达。  
  两者若合并，将显著改善 PicoClaw 在长上下文场景下的调用效率。

- **可观测性**  
  - [sipeed/picoclaw#3156](https://github.com/sipeed/picoclaw/pull/3156)：每轮输入/输出 token 用量上报，为后续成本对齐、使用审计

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目日报（2026-07-15）

**分析范围：** 过去 24 小时（2026-07-14 更新）的 GitHub 动态。  
**数据来源：** `github.com/qwibitai/nanoclaw`（PR 链接显示为 `nanocoai/nanoclaw`）。

---

## 1. 今日速览

- 过去 24 小时内仓库没有新增 Issue，也无新版本 Release；全部 26 条动态均为 PR 更新（19 条开放，7 条已合并/关闭）。
- 从研究视角筛选后，**没有直接涉及视觉语言能力、推理机制、训练方法论或幻觉问题的学术/实验性 PR**。大部分更新集中在运行时稳定性、安全、通道（Slack/Telegram/Dial/Discord）集成与文档修正。
- 仅有两项工作与多模态/智能体上下文管理间接相关：附件下载回退（[#3044](https://github.com/nanocoai/nanoclaw/pull/3044)）与 skill 片段按需注入（[#2921](https://github.com/nanocoai/nanoclaw/pull/2921)）。
- 整体活跃度中等，属于典型的“维护密集日”，模型/算法层面的研究信号较弱。

---

## 2. 版本发布

**无。** 今日未发布任何 Release。

---

## 3. 项目进展

今日已关闭/合并的 PR 共 7 条（提供清单中可见 6 条），主要推进了运营安全、安装配置与通道集成：

- **[#2728](https://github.com/nanocoai/nanoclaw/pull/2728)** — 修复 Telegram 配对时 `--intent wire-to:<folder>` 未写入 `messaging_group_agents` 的问题，保证多代理消息路由正确。
- **[#2729](https://github.com/nanocoai/nanoclaw/pull/2729)** — 修正 `add-telegram` 技能文档，使状态块名称与真实 setup 输出一致。
- **[#2730](https://github.com/nanocoai/nanoclaw/pull/2730)** — 修复 `.env` 中的 `NANOCLAW_*` 标志在 launchd/systemd 下未加载到 `process.env` 的问题，使安全/运维开关（如 egress lockdown）真正生效。
- **[#2753](https://github.com/nanocoai/nanoclaw/pull/2753)** — 修复 pre-commit hook 在 `pnpm` 不在 PATH 时失效的问题。
- **[#3042](https://github.com/nanocoai/nanoclaw/pull/3042)**（已关闭）— 提出新增 Dial 通道，后续被更窄范围的 [#3050](https://github.com/nanocoai/nanoclaw/pull/3050) 取代。
- **[#3043](https://github.com/nanocoai/nanoclaw/pull/3043)** — 将 Telegram 深度链接从 `t.me` 切换到 `telegram.me`，提升兼容性。

**整体评价：** 项目未在模型能力或算法上取得明显进展，但基础设施的健壮性与安全边界在持续加固。

---

## 4. 社区热点

GitHub 数据未提供有效的评论数/反应数（均为 `undefined`），无法按讨论热度排序。根据更新时间集中程度，可将以下主题视为当前社区焦点：

| 主题 | 相关 PR | 背后诉求 |
|---|---|---|
| **Dial 新通道** | [#3050](https://github.com/nanocoai/nanoclaw/pull/3050)、[#3042](https://github.com/nanocoai/nanoclaw/pull/3042) | 扩展可用渠道，降低接入门槛。 |
| **Slack 安装体验** | [#3047](https://github.com/nanocoai/nanoclaw/pull/3047) | 凭证配置顺序错误、代理选项说明不清，导致新用户安装失败。 |
| **消息/附件可靠性** | [#3044](https://github.com/nanocoai/nanoclaw/pull/3044)、[#3045](https://github.com/nanocoai/nanoclaw/pull/3045)、[#3049](https://github.com/nanocoai/nanoclaw/pull/3049)、[#3048](https://github.com/nanocoai/nanoclaw/pull/3048) | 确保消息不丢失、不延迟、附件（尤其是语音/音频）不静默被丢弃。 |
| **Discord 交互准确性** | [#2899](https://github.com/nanocoai/nanoclaw/pull/2899) | 审批卡片按钮路由错误，影响用户与 AI 的交互闭环。 |

---

## 5. Bug 与稳定性

按影响严重程度和修复状态排列：

### 高影响/待修复

- **[#2800](https://github.com/nanocoai/nanoclaw/pull/2800)**（开放）— 安全：在数据库/文件系统变更前验证 group 文件夹，并禁止 Docker 隐式拉取容器镜像。尚未合并，存在潜在权限升级与供应链风险。
- **[#2801](https://github.com/nanocoai/nanoclaw/pull/2801)**（开放）— 路由输入校验：原 `safeParseContent` 对非对象 JSON 原始值返回非对象，导致 `.text`/`.sender` 读取为 `undefined`，可能引发路由错误或异常行为。
- **[#3045](https://github.com/nanocoai/nanoclaw/pull/3045)**（开放）— 容器退出时消息延迟：`<message>` 块在退出时可能延迟 60 秒才能被扫把线程处理，影响实时性。
- **[#3044](https://github.com/nanocoai/nanoclaw/pull/3044)**（开放）— 入站附件丢失：无 `fetchData()` 的附件（如 Telegram 语音/音频）被静默丢弃，影响多模态输入。
- **[#2750](https://github.com/nanocoai/nanoclaw/pull/2750)**（开放）— 容器 SIGKILL 后 `outbound.db` 遗留热日志，可能导致数据损坏或重复投递。

### 中影响/部分已修复

- **[#3049](https://github.com/nanocoai/nanoclaw/pull/3049)**（开放）— 工具调用轮次中发出的 `<message>` 块未正确投递。
- **[#3048](https://github.com/nanocoai/nanoclaw/pull/3048)**（开放）— `<message>` 正文在引号 `</message>` 处被错误截断。
- **[#2899](https://github.com/nanocoai/nanoclaw/pull/2899)**（开放）— Discord DM 审批按钮因 `custom_id` 含换行符而全部路由为“

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

**IronClaw 项目日报 — 2026-07-15**

> 分析范围：过去 24 小时内 nearai/ironclaw 的 49 条 Issues（37 活跃/新开，12 关闭）与 50 条 PRs（23 待合并，27 已合并/关闭）。已按“多模态推理、长上下文理解、post-training 对齐、AI 可靠性”方向进行筛选，并跳过一般性产品/商业更新。

---

## 1. 今日速览

- 今日无新版本发布，但代码活跃度很高：50 个 PR 与 49 个 Issue 的更新量显示核心团队仍在密集推进“重生（Reborn）”架构的工程化与可靠性建设。
- 研究相关主线集中在**推理机制**（self-verification pass、tool-capable nudge、tool-call 参数校验）、**训练/推理方法论**（skill 按需激活、上下文窗口预览上限、模型选择/成本配置）、**幻觉/可靠性**（错误状态误报、test-connection 误报、并发写导致消息乱序）三方面。
- 今日数据中**未发现视觉语言（vision-language）或多模态理解相关的研究/工程条目**。
- 新增大量由核心维护者提出的系统性改进提案（#6103–#6108），主要目标是让 CI 信号、发布门禁、错误保真度、扩展生命周期从“可观测”走向“可强制”。
- 项目健康度：功能迭代速度快，但稳定性/状态一致性债务明显（Slack 生命周期、并发消息顺序、错误误报），需警惕高频率新功能对 CI 与发布管道带来的压力。

---

## 2. 版本发布

无今日新 Release。相关版本号变动见 PR #5598（release  chores），但尚未发布为正式 Release。

---

## 3. 项目进展

### 已合并/关闭的关键 PR

| PR | 主题 | 研究/可靠性意义 |
|---|---|---|
| [nearai/ironclaw#6095](https://github.com/nearai/ironclaw/pull/6095) | 修正 Slack 认证不可用通知中的错误分类；把安装存储 I/O 故障从“无效输入”中剥离 | 直接改善错误保真度，减少“幻觉式”错误归因 |
| [nearai/ironclaw#6089](https://github.com/nearai/ironclaw/pull/6089) | 从 libSQL/PostgreSQL  contention 中恢复资源治理器 | 数据库级可重试性，对长上下文/多步调用的稳定性有支撑作用 |
| [nearai/ironclaw#5896](https://github.com/nearai/ironclaw/pull/5896) | WebUI memory 浏览隔离：按认证用户作用域挂载 | 隐私/安全边界，属于 post-training 对齐与数据隔离基础设施 |
| [nearai/ironclaw#6013](https://github.com/nearai/ironclaw/pull/6013) | 让交互式编码的 completion nudge 支持 tools | 推理路径优化：agent loop 在 coding 场景下更充分利用工具调用 |
| [nearai/ironclaw#6007](https://github.com/nearai/ironclaw/pull/6007) ～ [nearai/ironclaw#6065](https://github.com/nearai/ironclaw/pull/6065) | NEA-25 统一扩展模型 Train A 系列（P4–P7b） | 统一扩展运行时，对后续多模态/多通道 agent 输入输出路由有架构意义 |

### 仍在推进的关键 PR

| PR | 主题 | 研究/可靠性意义 |
|---|---|---|
| [nearai/ironclaw#6093](https://github.com/nearai/ironclaw/pull/6093) | Reborn agent loop 增加 self-verification pass；新增 `benchmark_default` profile 启用 | **推理机制**：在循环结束前加入自验证，降低错误/幻觉输出 |
| [nearai/ironclaw#6096](https://github.com/nearai/ironclaw/pull/6096) | 按线程串行化并发 inbound-message 写入 | **长上下文/对话状态一致性**：修复消息乱序 |
| [nearai/ironclaw#6097](https://github.com/nearai/ironclaw/pull/6097) | 工具结果预览上限从 2KB 提升到 2.75KB | **上下文窗口/训练方法论**：基于 ClawBench 成本/得分数据的经验调优 |
| [nearai/ironclaw#6111](https://github.com/nearai/ironclaw/pull/6111) | WebChat v2 模型选择 + 单次运行用量/成本 | **训练/推理成本**：补齐 OpenAI 兼容 API 已有的模型覆盖能力 |
| [nearai/ironclaw#5977](https://github.com/nearai/ironclaw/pull/5977) | Reborn skills 按关键词只注入一行列表，激活时加载完整 body | **推理/提示工程**：每调用减少约 7K 无关 token，降低上下文污染与成本 |
| [nearai/ironclaw#5970](https://github.com/nearai/ironclaw/pull/5970) | MCP 注册框架骨架（owner-scoped store、minted id） | 后续工具生态对齐的基础设施 |

---

## 4. 社区热点

按评论数与核心维护者关注度排序，今日讨论最集中的是“状态一致性”与“错误保真度”两类诉求。

| 热门 Issue/PR | 讨论焦点 | 背后诉求 |
|---|---|---|
| [nearai/ironclaw#5948](https://github.com/nearai/ironclaw/issues/5948) | Assistant 把 GitHub 扩展“已安装”误报为“已激活” | 系统状态与 UI 状态必须一致，否则模型/用户都会产生错误信念 |
| [nearai/ironclaw#6105](https://github.com/nearai/ironclaw/issues/6105) | 扩展/通道生命周期状态机测试 + Slack canary lanes | 把重复回归的 Slack 生命周期问题用确定性测试覆盖 |
| [nearai/ironclaw#6108](https://github.com/nearai/ironclaw/issues/6108) | 错误保真度：禁止 generic failure、状态必须真实 | 减少“成功但 delivery 失败”这类模型/系统幻觉 |
| [nearai/ironclaw#6107](https://github.com/nearai/ironclaw/issues/6107) | 模型输入兼容性语料：在 CI 中 replay 真实 tool-call 参数形状 | 解决过度严格验证导致的模型输出被误拒问题 |
| [nearai/ironclaw#6103](https://github.com/nearai/ironclaw/issues/6103) | CI 信号恢复：7 月主分支约 70% push 失败，多为 5 个 flaky 测试 | 需要把 CI 从“噪声”变成“信号” |

---

## 5. Bug 与稳定性

按严重程度排列，优先列出与推理、长上下文、状态一致性、错误保真度相关的项。

### 高严重（正确性/幻觉风险）

| Issue | 问题 | 状态 | 相关 PR |
|---|---|---|---|
| [nearai/ironclaw#6109](https://github.com/nearai/ironclaw/issues/6109) | OpenAI 兼容 API 的 `model` override 对 Bedrock 静默失效；response label 是“盲 echo”而非真实读取 | 待修复 | 无 |
| [nearai/ironclaw#6099](https://github.com/nearai/ironclaw/issues/6099) | `POST /llm/test-connection` 对不可达 endpoint + 无效 key 返回 `ok: true` | 待修复 | 无 |
| [nearai/ironclaw#6108](https://github.com/nearai/ironclaw/issues/6108) | 失败被吞掉、泛化或误报为成功 | 待修复 | 无 |
| [nearai/ironclaw#6100](https://github.com/nearai/ironclaw/issues/6100) | 单次 context-window cache 在慢写与后发消息竞争时可能用旧快照重新播种 | 待修复 | [nearai/ironclaw#6096](https://github.com/nearai/iron

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

**LobsterAI 项目日报 — 2026-07-15**

> 数据来源：netease-youdao/LobsterAI  
> 统计窗口：2026-07-14 至 2026-07-15  
> 分析视角：重点筛选与**视觉语言能力、推理机制、训练方法论、幻觉/可靠性**相关的内容，产品/商业类 UI 问题仅作简要归类。

---

### 1. 今日速览

- 过去 24 小时项目活跃度较低：Issues 与 PRs 全部处于关闭状态，无新版本发布，亦无新增研究型 Issue 或 PR。
- 最具研究价值的是**两条 OpenClaw 智能体（Agent）控制流修复 PR**，分别处理“关键 tool-loop 终止”与“aborted tool run 后停止循环”，直接对应 **AI 可靠性与推理控制机制**。
- 其余 4 条 Issue 与 1 条 PR 为 UI/UX 与配置类问题，与研究主线关联较弱。
- 整体健康度：稳步推进稳定性修复，但研究社区新话题、新功能或长上下文/多模态方向的讨论几乎为零。

---

### 2. 版本发布

无。

---

### 3. 项目进展

| PR | 作者 | 研究/工程意义 |
|---|---|---|
| [#2331](https://github.com/netease-youdao/LobsterAI/pull/2331) | btc69m979y-dotcom | **OpenClaw Agent 控制流修复**：backport OpenClaw v2026.6.1 的双重修复，使关键 `tool-loop` veto 能够终止当前 Agent run；同时保留普通 plugin veto 行为，并允许混合并行批次中的正常 sibling tools 完成后再停止。这对**工具调用安全、循环终止与推理控制**有直接影响。 |
| [#2330](https://github.com/netease-youdao/LobsterAI/pull/2330) | btc69m979y-dotcom | **Agent 中止边界修复**：backport OpenClaw `7fe287b0d3`，在工具执行与异步 turn hooks 之后的中止边界处停止 Agent 循环，并增加了回归测试。提升 **Agent 在异常/被中断情况下的可靠性**。 |
| [#2329](https://github.com/netease-youdao/LobsterAI/pull/2329) | liuzhq1986 | UI 层修复：在流式输出时尊重用户手动滚动，取消待执行的自动滚动。属于前端体验优化，研究相关性较弱。 |

**整体进展评估**：今日进展以 **安全与稳定性 backport** 为主，未出现新的模型能力、训练方法或多模态功能迭代。

---

### 4. 社区热点

- **研究相关热点**：PR [#2331](https://github.com/netease-youdao/LobsterAI/pull/2331) 与 [#2330](https://github.com/netease-youdao/LobsterAI/pull/2330) 是今日唯一涉及 Agent 运行时的议题，对关注“工具调用失控/loop 不终止”问题的开发者有参考价值。
- **一般社区热点**：Issues 关闭数较多（4 条），但均来自 stale 流程，评论数仅 2–3 条，无新增点赞或活跃讨论。用户诉求集中在**本地化显示、分享截图完整性、邮箱配置反馈、定时任务响应**等产品体验。

---

### 5. Bug 与稳定性

| 问题 | 严重程度 | 状态 | 关联 PR |
|---|---|---|---|
| **OpenClaw 关键 tool-loop 无法终止** | **高**（可导致 Agent 运行失控） | 已修复（closed） | [#2331](https://github.com/netease-youdao/LobsterAI/pull/2331) |
| **Agent 在 aborted tool run 后未正确停止循环** | **高**（边界异常可能引发级联错误） | 已修复（closed） | [#2330](https://github.com/netease-youdao/LobsterAI/pull/2330) |
| 英文语言下中文选项仍显示英文 | 中 | 已关闭（stale） | 无明确 PR |
| 聊天过长时分享长图内容缺失 | 中 | 已关闭（stale） | 无明确 PR |
| 邮箱配置测试连通性无响应 | 中 | 已关闭（stale） | 无明确 PR |
| 定时任务更新偶尔无响应 | 中 | 已关闭（stale） | 无明确 PR |

> 研究视角下，今日两条 Agent 控制流修复是核心稳定性增量，其余为产品 UI/UX 问题。

---

### 6. 功能请求与路线图信号

- **今日无新增功能请求**。
- ** roadmap 信号**：
  1. OpenClaw 被持续 backport 与加固，说明项目正将 **Agent 运行时可解释性、工具调用安全、循环终止机制** 作为近期重点。
  2. 没有关于视觉语言、长上下文、post-training 对齐或幻觉抑制的 Issue/PR 出现，意味着这些方向尚未在公开社区形成新的讨论。

---

### 7. 用户反馈摘要

由于今日无新研究型 Issue，用户反馈主要来自已关闭的 stale 产品问题：

- **本地化一致性**：英文界面下，中文选项未按预期显示中文（[#1389](https://github.com/netease-youdao/LobsterAI/issues/1389)）。
- **长内容分享**：聊天内容过长时，右上角“分享”生成的长图会截断缺失（[#1386](https://github.com/netease-youdao/LobsterAI/issues/1386)）。
- **配置反馈不足**：邮箱配置点击“测试连通性”后无响应，用户难以判断是网络问题、密码错误还是 UI 卡死（[#1388](https://github.com/netease-youdao/LobsterAI/issues/1388)）。
- **定时任务 UX**：编辑并更新定时任务时偶尔无响应，影响工作流自动化（[#1390](https://github.com/netease-youdao/LobsterAI/issues/1390)）。

这些反馈虽然偏向工程/UI，但间接反映了**长对话场景**与**任务编排**是用户实际使用的关键路径。

---

### 8. 待处理积压

- **今日无长期未响应的新增 Issue**。4 条 Issue 均为 2026-04-03 创建、2026-07-14 因 stale 关闭，说明社区积压问题正在被清理。
- **建议关注**：OpenClaw 的 loop 终止机制虽已修复，但缺乏公开的长上下文/多模态/幻觉抑制类 Issue。建议维护者在后续版本中主动收集这些研究方向的反馈，避免社区议题过度集中于 UI 配置层。

---

**结论**：2026-07-15 的 LobsterAI 活动以**稳定性 backport 与 stale 清理**为主，Agent 工具循环安全是今日唯一的核心研究相关进展。项目健康度稳定，但研究创新讨论处于低谷。

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis 项目日报（2026-07-15）

> **研究视角筛选说明**：本报告优先关注与视觉语言、推理机制、训练方法、长上下文理解、模型可靠性及幻觉相关的信号。一般性产品/商业集成（MCP OAuth、CalDAV、依赖升级、前端构建等）仅在影响稳定性时简要提及。

---

## 1. 今日速览

今日 Moltis 仓库活跃度中等，共 **3 条 Issue 更新**（2 开放/活跃、1 关闭）和 **12 条 PR 更新**（8 已合并/关闭、4 待合并），并发布了 **1 个版本**。  
从研究角度看，今日没有发布新的训练方法或视觉语言/幻觉缓解的专门工作；研究相关信号集中在 **上下文管理/工具输出截断**、**本地小模型输出格式鲁棒性**、**多模态（语音）本地 ASR** 三个方向。已合并的 PR 中有三项直接改善 AI 系统可靠性：工具结果持久化截断、浏览器工具空值容忍、agent 标量参数字符串化修复。社区功能请求则聚焦于本地 STT、上下文命令注入和浏览器自动截图，整体健康度稳定，但缺乏面向视觉推理或幻觉控制的深度讨论。

---

## 2. 版本发布

- **20260714.11**  
  - 本次 release 在提供的元数据中仅显示版本号，**具体变更日志未披露**。  
  - 未观察到明确的模型/研究相关更新，也未标记破坏性变更。  
  - 迁移建议：待发布页面补充 changelog 后再评估；当前版本号暗示为 2026-07-14 的常规构建。

---

## 3. 项目进展（研究相关合并/关闭项）

| PR / Issue | 状态 | 研究/可靠性意义 |
|---|---|---|
| [#1089](https://github.com/moltis-org/moltis/pull/1089) Cap persisted tool results before rehydration | 已合并 | **长上下文/Token 预算**：在 session 重水合为 provider-bound `ChatMessage` 时，对 `tool`/`tool_result` 内容做截断，覆盖普通聊天、流式聊天、重试后 compaction、提示检查、静默记忆轮等场景，防止超大工具输出撑满上下文。 |
| [#1136](https://github.com/moltis-org/moltis/pull/1136) fix(agents): coerce stringified scalar tool args before validation | 已合并 | **模型输出格式鲁棒性**：本地小模型（如 Gemma 4、oMLX）常把布尔/数字标量输出为 JSON 字符串，导致验证失败；该 PR 在预分发校验前强制类型转换，提升本地模型部署稳定性。 |
| [#1098](https://github.com/moltis-org/moltis/pull/1098) fix(browser): tolerate null optional params in browser tool calls | 已合并 | **小模型兼容性**：本地小模型对未使用的浏览器工具参数显式输出 `null`，修复后 serde 可正确识别，避免调用失败。 |
| [#1146](https://github.com/moltis-org/moltis/pull/1146) Add GPT-5.6 model support | 已合并 | **模型能力接入**：注册 GPT-5.6 Sol/Terra/Luna，配置 1.05M 上下文窗口与 372K 后端限制，但属于模型接入层，不涉及训练方法或推理机制。 |
| [#1120](https://github.com/moltis-org/moltis/pull/1120) fix(mcp): direct fetch for resource_metadata | 已合并 | 产品集成修复（MCP OAuth），研究意义较低。 |

---

## 4. 社区热点

今日 3 个 Issue 均仅有 **1 条评论**，热度分散，没有形成明显讨论焦点。从研究/功能诉求看：

- **[#1102](https://github.com/moltis-org/moltis/issues/1102) Feature: Add FunASR/SenseVoice as local STT engine**  
  作者更新了 License 与能力说明，强调本地语音转写需求；反映社区对**隐私化、多模态（音频）输入**的关注。  
- **[#1132](https://github.com/moltis-org/moltis/issues/1132) “main” session can't be deleted/archived**  
  产品/数据管理 bug，无研究相关性。  
- **[#1119](https://github.com/moltis-org/moltis/issues/1119) MCP OAuth fails with invalid_target**  
  已随 PR [#1120](https://github.com/moltis-org/moltis/pull/1120) 关闭，属于外部服务集成问题。

---

## 5. Bug 与稳定性

按严重程度排列：

1. **高：Session 无法删除/归档**  
   - [#1132](https://github.com/moltis-org/moltis/issues/1132) 仍开放，无修复 PR。影响长期数据管理与用户体验。

2. **中：工具输出导致上下文膨胀**  
   - [#1089](https://github.com/moltis-org/moltis/pull/1089) 已合并，通过截断持久化工具结果缓解长上下文过载风险。

3. **中：CalDAV 非 ASCII 日期崩溃**  
   - [#1145](https://github.com/moltis-org/moltis/pull/1145) 已合并，修复远程数据解析 panic。

4. **低：本地小模型工具参数格式问题**  
   - [#1136](https://github.com/moltis-org/moltis/pull/1136)、[#1098](https://github.com/moltis-org/moltis/pull/1098) 均已合并，提升对 Gemma 4 / oMLX 等模型的兼容性。

---

## 6. 功能请求与路线图信号

- **本地多模态语音输入**  
  [#1102](https://github.com/moltis-org/moltis/issues/1102) 请求接入 FunASR/SenseVoice 作为本地 STT，符合“端侧/隐私优先”的多模态趋势，若纳入下一版本将增强音频-文本理解链路。

- **动态上下文注入**  
  [#1124](https://github.com/moltis-org/moltis/pull/1124) 提议每轮对话前运行 `chat.context_command` 并把 stdout 注入上下文，属于**长上下文提示工程/运行时上下文增强**。

- **浏览器视觉时间线**  
  [#1135](https://github.com/moltis-org

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目日报（2026-07-15）

> **研究视角说明**：ZeroClaw 是一个 agent 运行时/基础设施框架，而非基础模型研究项目。今日数据中未见**视觉语言能力**、**训练方法论**相关的直接条目；但包含大量与**推理机制**（SOP/goal 控制、路由逻辑）、**长上下文理解**（记忆分层、对话关联、历史与记忆解耦）以及**AI 可靠性/幻觉相关风险**（工具调用参数验证、审批门绕过、记忆去重、审计完整性）相关的信号。以下按研究相关性筛选，并跳过纯产品/商业更新。

---

## 1. 今日速览

过去 24 小时项目活跃度较高：Issues 更新 32 条（新开/活跃 24，关闭 8），PRs 更新 50 条（待合并 26，已合并/关闭 24），无新版本发布。主要技术推力集中在三条线上：由 `logical-and` 提交的 **Hindsight 记忆后端 7 层 stacked PR**（#9063–#9069）正在推进记忆分层、召回/注入、去重与持久化；`vrurg` 的 **goal 控制器与通道准入 PR 栈**（#8687–#8996）在补齐 agent 目标级推理与受控委托边界；安全与可靠性方面则有多个高严重度 bug 被关闭或仍在处理，涉及审批门完整性、工具调用参数验证、pipeline 权限混淆等。

---

## 2. 版本发布

**无。** 今日未发布新版本。v0.8.3 与 v0.8.4 维护列车仍在进行中（见 #7320、#8357）。

---

## 3. 项目进展

### 已关闭/合并的重要 Issue

- **[#8678](https://github.com/zeroclaw-labs/zeroclaw/issues/8678)** `[Bug]` `advance_step` 缺少运行状态守护，driver 可通过 `sop_advance` 绕过审批门（S2，高严重度）。已关闭，说明审批门完整性得到修复。
- **[#8631](https://github.com/zeroclaw-labs/zeroclaw/issues/8631)** `[Bug]` 无头 deterministic SOP 步骤未执行却被记录为 Completed，造成审计“假绿”并阻塞真实运行。已关闭。
- **[#8695](https://github.com/zeroclaw-labs/zeroclaw/issues/8695)** `[Bug]` Cron 作业在 `uses_memory = false` 时仍召回记忆。已关闭，说明记忆调用的状态隔离被修复。
- **[#6689](https://github.com/zeroclaw-labs/zeroclaw/issues/6689)** 生产 SOP 审计静默 no-op：文档承诺的 `sop_run_*`/`sop_step_*` Memory key 从未写入。已关闭。
- **[#6686](https://github.com/zeroclaw-labs/zeroclaw/issues/6686)** SOP cron triggers 没有生产调用方。已关闭。
- **[#8073](https://github.com/zeroclaw-labs/zeroclaw/issues/8073)** v0.8.3 可观测性/CI/docs/依赖 tracker 已关闭。
- **[#8071](https://github.com/zeroclaw-labs/zeroclaw/issues/8071)** v0.8.3 运行时/执行/agent loop tracker 已关闭。

### 推进中的主要 PR 栈

- **Hindsight 记忆栈（#9063–#9069，all OPEN）**：由 `logical-and` 于 2026-07-14 集中提交，共 7 层。
  - [#9063](https://github.com/zeroclaw-labs/zeroclaw/pull/9063)：Hindsight HTTP 记忆后端、配置与工厂。
  - [#9064](https://github.com/zeroclaw-labs/zeroclaw/pull/9064)：shared/family 与 system 记忆层级 + 授权。
  - [#9065](https://github.com/zeroclaw-labs/zeroclaw/pull/9065)：recall/injection 调参与 hindsight 召回类型过滤。
  - [#9066](https://github.com/zeroclaw-labs/zeroclaw/pull/9066)：consolidation 去重正确性。
  - [#9067](https://github.com/zeroclaw-labs/zeroclaw/pull/9067)：显式 `forget` / 失效 PATCH。
  - [#9068](https://github.com/zeroclaw-labs/zeroclaw/pull/9068)：async retain + Telegram DM 流式/截断。
  - [#9069](https://github.com/zeroclaw-labs/zeroclaw/pull/9069)：dashboard  per-agent 后端 + 记忆计数。

- **Goal 控制器/准入栈（#8687–#8996，all OPEN）**：由 `vrurg` 提交。
  - [#8687](https://github.com/zeroclaw-labs/zeroclaw/pull/8687)：goal 控制器与验证器完成门。
  - [#8688](https://github.com/zeroclaw-labs/zeroclaw/pull/8688)：受信 goal 工具与委托边界。
  - [#8689](https://github.com/zeroclaw-labs/zeroclaw/pull/8689)：通道 `/goal` 命令准入。
  - [#8746](https://github.com/zeroclaw-labs/zeroclaw/pull/8746)：修复活跃 goal 自恢复循环。
  - [#8996](https://github.com/zeroclaw-labs/zeroclaw/pull/8996)：daemon 重载时保留运行中的 goal。

**整体推进评估**：今日在 agent 记忆架构与目标级推理控制两个核心方向上同时推进，属于近期较高密度的功能冲刺；但主要 PR 仍处于待合并状态，代码尚未落地。

---

## 4. 社区热点

### 讨论最活跃的 Issues

1. **[#5982](https://github.com/zeroclaw-labs/zeroclaw/issues/5982)**（10 评论）  
   **多租户 per-sender RBAC**。诉求：单一 ZeroClaw 实例需服务多用户类（customer/operator/developer），隔离 workspace、工具集、rate limits 与 system prompts。这属于 agent 安全边界与访问控制的基础研究问题，与可信 AI 部署相关。

2. **[#6055](https://github.com/zeroclaw-labs/zeroclaw/issues/6055)**（7 评论）  
   **Slack thread 首次提及时的上下文回填**。诉求：在严格 mention 模式下，bot 首次被 @ 时应通过 `conversations.replies` 回填线程历史。这直接影响长对话上下文理解能力。

3. **[#8973](https://github.com/zeroclaw-labs/zeroclaw/issues/8973)**（4 评论）  
   **Landlock 沙箱在 Fedora 上阻止 `/dev/null` 访问导致 shell tool 失败**。高严重度运行时安全 bug。

4. **[#8933](https://github.com/zeroclaw-labs/zeroclaw/issues/8933)**（3 评论）  
   **RFC：OTel 导出跨轮次对话关联**。提出将不透明 conversation ID 贯穿 turn-lifecycle observer 事件，导出为 `gen_ai.conversation.id`。这是长上下文/多轮推理可观测性的关键指标。

5. **[#9048](https://github.com/zeroclaw-labs/zeroclaw/issues/9048)**（3 评论）  
   **RFC：将对话历史与 agent 策划的长期记忆分离**。指出当前实现仍将二者混在 `MemoryCategory::Conversation` 中。这是记忆架构与长上下文理解的核心研究问题。

---

## 5. Bug 与稳定性

按严重度排列：

| 严重度 | Issue | 简述 | 状态 |
|--------|-------|------|------|
| S0 安全/数据风险 | [#7947](https://github.com/zeroclaw-labs/zeroclaw/issues/7947) | `execute_pipeline` 忽略调用 agent 的 `ToolAccessPolicy`，仅使用全局 `allowed_tools`，造成 confused deputy | OPEN |
| S1 工作流阻塞 | [#8563](https://github.com/zeroclaw-labs/zeroclaw/issues/8563) | Web dashboard 聊天会话中 SOP 不可用 | OPEN |
| S1 工作流阻塞 | [#8675](https://github.com/zeroclaw-labs/zeroclaw/issues/8675) | OpenAI/OpenRouter 格式 provider 将 assistant tool-call 参数原样序列化，不验证 JSON 合法性，导致 provider 400 → 空回复 | OPEN |
| S2 降级 | [#8973](https://github.com/zeroclaw-labs/zeroclaw/issues/8973) | Landlock 沙箱阻止 `/dev/null` | OPEN |
| S2 降级 | [#8678](https://github.com/zeroclaw-labs/zeroclaw/issues/8678) | `advance_step` 可绕过审批门 | CLOSED |
| S2 降级 | [#8631](https://github.com/zeroclaw-labs/zeroclaw/issues/8631) | headless deterministic SOP 步骤未执行却记录 Completed | CLOSED |
| S2 降级 | [#8695](https://github.com/zeroclaw-labs/zeroclaw/issues/8695) | Cron 作业 `uses_memory=false` 仍召回记忆 | CLOSED |
| S2 降级 | [#9001](https://github.com/zeroclaw-labs/zeroclaw/issues/9001) | Provider 失败原因被通用重试 envelope 掩埋，缺乏 cause-specific 诊断 | OPEN |

**研究相关性**：[#8675](https://github.com/zeroclaw-labs/zeroclaw/issues/8675) 属于模型输出（工具调用参数）的结构化验证问题，与幻觉/可靠性直接相关；[#7947](https://github.com/zeroclaw-labs/zeroclaw/issues/7947) 与工具权限边界相关，是 agent 安全的关键缺陷。

---

## 6. 功能请求与路线图信号

- **记忆架构（高概率进入后续版本）**
  - [#9048](https://github.com/zeroclaw-labs/zeroclaw/issues/9048)：对话历史与长期记忆解耦。
  - [#8891](https://github.com/zeroclaw-labs/zeroclaw/issues/8891)：Persistent memory 策划、相关性与可操作性 parity tracker。
  - [#8933](https://github.com/zeroclaw-labs/zeroclaw/issues/8933)：OTel 跨轮次对话关联。
  - Hindsight PR 栈（#9063–#9069）已覆盖该方向大部分实现。

- **Agent 推理/控制机制**
  - [#8719](https://github.com/zeroclaw-labs/zeroclaw/issues/8719)：SOP `when` 条件为 false 时应进入下一步而非结束运行，支持多阶段 SOP。
  - [#8581](https://github.com/zeroclaw-labs/zeroclaw/issues/8581)：

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*