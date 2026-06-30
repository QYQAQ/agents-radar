# OpenClaw 生态日报 2026-06-30

> Issues: 375 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-06-30 00:33 UTC

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

# OpenClaw 项目研究动态日报（2026-06-30）

> 分析视角：多模态推理、长上下文理解、post-training 对齐、AI 可靠性  
> 数据来源：github.com/openclaw/openclaw（过去 24h：375 Issues / 500 PRs / 0 Releases）

---

## 1. 今日速览

OpenClaw 今日维持极高工程活跃度（375 Issues / 500 PRs），但无新版本发布。与研究高度相关的信号集中在：**视觉语言输入的 capability validation 缺失**、**reasoning/thinking 内容在跨通道传递中的语义丢失**、**tool-use 循环与 session 状态机的可靠性缺陷**，以及**多 provider 缓存/认证对齐问题**。社区讨论最热的仍是跨平台客户端扩展（#75），但研究价值有限，本报告已过滤。整体项目健康度表现为"高活跃、高积压"——448 个待合并 PR 提示 review 带宽是主要瓶颈。

---

## 2. 版本发布

**无新版本发布。**

---

## 3. 项目进展（与研究相关的已合并/关闭 PR）

| PR | 状态 | 研究相关性 | 说明 |
|---|---|---|---|
| [#95051](https://github.com/openclaw/openclaw/pull/95051) | CLOSED | reasoning 内容传递 | Telegram durable reasoning 回复修复，将 `isReasoning` payload 在 outbound normalization 前转换为 reasoning-lane text，避免 reasoning 块在跨通道分发中被静默丢弃。 |
| [#97875](https://github.com/openclaw/openclaw/pull/97875) | CLOSED | reasoning 内容传递 | 与 #95051 相关的 Telegram reasoning durability 修复，解决 reasoning block/final payload 被共享 reply dispatcher 抑制的问题。 |
| [#97953](https://github.com/openclaw/openclaw/pull/97953) | CLOSED | AI 安全/权限边界 | ACP runtime controls 要求 owner 权限，收紧非 owner 对 runtime 控制的调用。 |
| [#97864](https://github.com/openclaw/openclaw/pull/97864) | CLOSED | 运行时可靠性 | `createNonExitingRuntime()` 从 generic `Error` 改为可区分的退出控制流类型，减少运行时失败被吞掉的概率。 |

**研究点评**：reasoning 内容的跨通道保真传递是 post-training 对齐与可解释性的关键基础设施。#95051/#97875 表明项目正在从"功能可用"向"语义不丢失"演进，但关闭而非合并可能意味着方案被替代或需要重构。

---

## 4. 社区热点（研究相关）

| Issue/PR | 评论/反应 | 核心诉求 | 研究意义 |
|---|---|---|---|
| [#81525](https://github.com/openclaw/openclaw/issues/81525) | 5 评论，已关闭 | `media-understanding` 未验证用户声明的 vision model 是否真支持图像就静默路由 | **视觉语言能力验证**：直接触及多模态系统中 capability declaration 与 runtime routing 的错位，是幻觉/失败的重要来源 |
| [#80176](https://github.com/openclaw/openclaw/issues/80176) | 5 评论 | JSONL session-replay harness，基于真实会话历史在多个 runtime 上回放并 diff trajectory | **推理机制/对齐评估**：属于 Codex×Pi parity 测试框架，对多智能体轨迹一致性、post-training 行为对齐有研究价值 |
| [#94518](https://github.com/openclaw/openclaw/issues/94518) | 6 评论，👍 8 | DeepSeek prompt cache hit rate 在 6.x 后跌破 10%，boundary-aware caching 破坏 prefix matching | **长上下文/训练推理效率**：缓存前缀匹配策略变更对长上下文成本与一致性有显著影响 |
| [#96857](https://github.com/openclaw/openclaw/issues/96857) | 4 评论 | 普通 tool text 输出被降级为 `(see attached image)` 占位符，agent 看不到真实输出 | **幻觉/感知降级**：属于模型输入上下文中的信息丢失型幻觉 |
| [#96106](https://github.com/openclaw/openclaw/pull/96106) | 高关注度 XL PR | Anthropic reasoning/pre-tool commentary 在 Discord 上的呈现 | **reasoning 可视化/可解释性**：commentary 与 thinking progress 默认关闭、显式 opt-in，涉及 reasoning 内容的用户暴露边界 |

---

## 5. Bug 与稳定性（按研究相关性与严重程度排列）

| Issue | 严重度 | 领域 | 状态 | 说明 |
|---|---|---|---|---|
| [#81525](https://github.com/openclaw/openclaw/issues/81525) | P2，已关闭 | 视觉语言/能力验证 | 无 fix PR | vision model 能力声明未验证即路由图像，可能导致模型接收到无法处理的输入 |
| [#96857](https://github.com/openclaw/openclaw/issues/96857) | 未标注 | 幻觉/上下文丢失 | 无 fix PR | tool 文本输出被替换为 `(see attached image)`，agent 基于错误占位符推理 |
| [#77642](https://github.com/openclaw/openclaw/issues/77642) | P1，回归 | session 状态/工具循环 | 无 fix PR | lossless-claw 重复回答 + "missing tool result in session history" 合成错误 |
| [#81567](https://github.com/openclaw/openclaw/issues/81567) | P1 | 工具使用/推理机制 | 无 fix PR | GPT-4o agent 在单次文本响应后退出，不继续 tool-use 循环 |
| [#81490](https://github.com/openclaw/openclaw/issues/81490) | P1，回归 | 子 agent / session 恢复 | 无 fix PR | subagent completion 不恢复父 session，而是在父 route 上 spawn 新 run |
| [#80918](https://github.com/openclaw/openclaw/issues/80918) | P2 | 不完整 turn 分类/消息丢失 | 无 fix PR | `update_plan` 后模型产生 `stopReason=stop` 的纯文本最终 turn 被丢弃 |
| [#97877](https://github.com/openclaw/openclaw/issues/97877) | P1 | 错误重试/副作用感知 | 无 fix PR | `hadPotentialSideEffects` 阻止 empty-error-retry，导致 transient 5xx 后静默终端失败 |
| [#74586](https://github.com/openclaw/openclaw/issues/74586) | P1 | 工具调用/超时分类 | 无 fix PR | AM embedded run 中止 `memory_search` 工具调用，尽管模型已完成，仍归类为超时 |
| [#94518](https://github.com/openclaw/openclaw/issues/94518) | P1 | 长上下文缓存/前缀匹配 | 无 fix PR | DeepSeek cache hit rate 骤降，boundary-aware caching 与 prefix matching 冲突 |
| [#80040](https://github.com/openclaw/openclaw/issues/80040) | P2 | 认证/缓存/重复执行 | 无 fix PR | OAuth 失效产生空占位符回复、provider 切换导致重复工具执行、冷缓存丢失近期上下文 |

---

## 6. 功能请求与路线图信号

| Issue/PR | 类型 | 被纳入可能性 | 研究相关性 |
|---|---|---|---|
| [#80188](https://github.com/openclaw/openclaw/issues/80188) | SDK: host-owned structured plugin inference beyond media-understanding | 中-高 | **多模态推理结构化输出**：插件需要 bounded host-owned inference，而非原始 OAuth 凭证或产品特定核心路由 |
| [#80213](https://github.com/openclaw/openclaw/issues/80213) | Skill setup hook | 中 | post-training 部署/环境配置自动化 |
| [#81913](https://github.com/openclaw/openclaw/issues/81913) | Stable plugin SDK surface for installed skill workflows | 中 | 插件生态与技能工作流的可靠性边界 |
| [#80176](https://github.com/openclaw/openclaw/issues/80176) | JSONL session-replay harness | 高（已有依赖 PR） | **多智能体轨迹回放与 diff**，是对齐评估基础设施 |
| [#81061](https://github.com/openclaw/openclaw/issues/81061) | before_route_inbound_message hook | 中 | 通道桥接/代理的 pre-routing 拦截 |

---

## 7. 用户反馈摘要（研究视角提炼）

**真实痛点：**

1. **视觉语言输入的"静默失败"**：用户声明 vision model 后，系统不验证能力就路由图像（#81525）；Telegram 图片保存到磁盘后只以 `<media:image>` 占位符传给模型（#93848），模型实际无法分析图像。
2. **Reasoning 内容在通道间丢失**：Telegram/Discord 等通道对 reasoning/thinking 块的处理不一致，导致启用 reasoning 的用户收不到完整回复（#95051、#97875、#96106）。
3. **工具使用循环不稳定**：GPT-4o 单次响应后退出 tool loop（#81567）、subagent 不恢复父 session（#81490）、incomplete-turn 分类器丢弃合法最终 turn（#80918）。
4. **长上下文与缓存成本**：DeepSeek 升级后 cache hit rate 暴跌（#94518），直接影响长上下文推理的经济性与一致性。
5. **认证与状态级联故障**：OAuth 失效、provider 切换、冷缓存 bootstrap 三者叠加，产生空回复、重复执行、上下文丢失（#80040）。

---

## 8. 待处理积压（提醒维护者关注）

| Issue/PR | 创建时间 | 最后更新 | 风险 |
|---|---|---|---|
| [#80176](https://github.com/openclaw/openclaw/issues/80176) | 2026-05-10 | 2026-06-29 | JSONL session-replay 是对齐评估核心基础设施，已 stale 近两个月 |
| [#81525](https://github.com/openclaw/openclaw/issues/81525) | 2026-05-13 | 2026-06-29 | 已关闭但无明确 fix commit，vision capability validation 问题可能仍在 |
| [#77642](https://github.com/openclaw/openclaw/issues/77642) | 2026-05-05 | 2026-06-29 | P1 回归，lossless-claw 重复回答 + 合成 tool result 缺失错误 |
| [#74586](https://github.com/openclaw/openclaw/issues/74586) | 2026-04-29 | 2026-06-29 | P1，AM embedded run 错误分类模型完成为超时 |
| [#80188](https://github.com/openclaw/openclaw/issues/80188) | 2026-05-10 | 2026-06-29 | host-owned structured inference 的 SDK 设计，影响多模态插件安全边界 |

---

## 研究侧总结

今日 OpenClaw 数据中最值得跟踪的研究信号是：**多模态输入的能力声明与 runtime 路由之间的 gap（#81525/#93848）**、**reasoning 内容在跨通道传递中的语义保真（#95051/#97875/#96106）**、**tool-use/session 状态机的可靠性缺陷（#81567/#81490/#80918/#97877）**，以及**长上下文缓存策略对一致性的影响（#94518）**。这些均属于 AI 可靠性研究的核心议题，建议持续观察相关 PR 是否进入合并阶段。

---

## 横向生态对比

# 个人 AI 助手/自主智能体开源生态横向对比分析
## 2026-06-30 研究动态摘要

---

## 1. 生态全景

当前个人 AI 助手/自主智能体开源生态呈现"高活跃、高积压、重工程"的整体态势：头部项目单日 PR 量可达 50 条级别，但无合并的待处理 PR 普遍在 20–45 条区间，review 带宽成为主要瓶颈。技术重心已从"功能可用"转向"语义保真、成本可控、异常可恢复"——reasoning 内容跨通道传递、视觉语言能力声明验证、长上下文缓存效率、工具调用状态一致性成为共同焦点。同时，多项目密集推进上下文压缩、工具披露策略优化与 MCP/插件运行时标准化，显示出生态正从单 agent 框架向多 agent 协作与生产级部署平台演进。

---

## 2. 各项目活跃度对比

| 项目 | 仓库 | Issues（24h） | PRs（24h） | 待合并 PR | Release | 健康度评估 |
|---|---|---:|---:|---:|:---|:---|
| **OpenClaw** | openclaw/openclaw | 375 | 500 | ~448 | 无 | 🔶 极高活跃、极高积压；研究信号强但 review 带宽严重不足 |
| **NanoBot** | HKUDS/nanobot | 7（4开3关） | 32（22待合） | 22 | 无 | 🟢 高活跃、方向聚焦；上下文压缩与推理效率迭代密集 |
| **Hermes Agent** | NousResearch/hermes-agent | 50（47活跃） | 50（44待合） | 44 | 无 | 🔶 高活跃、高积压；稳定性修复与多 agent 编排诉求并行 |
| **PicoClaw** | sipeed/picoclaw | 3 | 3 | 3 | 无 | 🔴 活跃度低，无合并进展，多个 PR/Issue 进入 stale |
| **NanoClaw** | nanocoai/nanoclaw | 0 | 7（5待合） | 5 | 无 | 🟡 中低活跃；工程化部署与渠道适配为主，研究信号弱 |
| **NullClaw** | nullclaw/nullclaw | 0 | 4（3待合） | 3 | 无 | 🟡 低活跃；以 CLI 体验与流式工具调用维护为主 |
| **IronClaw** | nearai/ironclaw | 14（10活跃） | 50（30待合） | 30 | 无 | 🟢 高活跃；Reborn 架构测试与认证/审批流程夯实底座 |
| **LobsterAI** | netease-youdao/LobsterAI | — | 39（合并/关闭） | — | **2026.6.29** | 🟢 发布日密集收尾；OpenClaw 集成稳定性修复为主 |
| **TinyClaw** | TinyAGI/tinyagi | 0 | 0 | — | 无 | ⚫ 无活动 |
| **Moltis** | moltis-org/moltis | 0 | 0 | — | 无 | ⚫ 无活动 |
| **CoPaw** | agentscope-ai/QwenPaw | 29（20活跃） | 50（31待合） | 31 | 无 | 🟢 高活跃；AgentScope 2.0 迁移，视觉与上下文治理并重 |
| **ZeptoClaw** | qhkm/zeptoclaw | 0 | 0 | — | 无 | ⚫ 无活动 |
| **ZeroClaw** | zeroclaw-labs/zeroclaw | 50 | 50 | ~35 | 无 | 🔶 极高活跃；P1 级 reasoning+工具调用缺陷数量偏高 |

> 注：OpenClaw 数据量级显著高于其他项目，与其作为核心参照的基础框架定位一致。

---

## 3. 研究定位分析

| 项目 | 多模态推理 | 长上下文处理 | 对齐/可靠性 | 技术路线特征 |
|---|---|---|---|---|
| **OpenClaw** | 视觉能力声明验证（#81525）、图像占位符传递（#93848） | 缓存前缀匹配策略（#94518）、JSONL session-replay（#80176） | reasoning 跨通道保真（#95051/#97875）、tool-use 状态机（#81567/#81490） | 以"通道-模型-工具"三层语义保真为核心，强调跨平台一致性 |
| **NanoBot** | 今日无直接信号 | 上下文压缩（#4581/#4588）、prefix caching 修复（#4222） | 自适应 reasoning effort（#4419）、tool_call id 污染（#4595） | 成本敏感型工程优化，聚焦低上下文窗口模型的经济部署 |
| **Hermes Agent** | 视觉 fallback 链（#35876） | 128K 压缩阈值崩溃（#55191）、记忆容量挂起（#42405） | reasoning_effort 透传（#55276）、fallback 配置统一（#24039） | 多平台客户端稳定性优先，长上下文与视觉鲁棒性薄弱 |
| **PicoClaw** | 仅 Doubao Seed 工具输出泄漏（#3153） | 无显著信号 | 工具调用解析可靠性 | 网关协议扩展导向，研究参与度低 |
| **NanoClaw** | 无 | 无 | 容器 symlink 逃逸安全（#2880） | 企业级部署与渠道生态，非研究前沿 |
| **NullClaw** | 无 | 无 | 原生流式工具调用（#971） | 开发者体验与流式推理基础设施 |
| **IronClaw** | 无直接信号 | 渐进式工具披露（#5149）、长工具链失败（#5415） | 技能误激活（#5417）、状态幻觉（#5416） | Reborn 架构的认证/审批/测试底座建设，可靠性研究偏系统层 |
| **LobsterAI** | 无 | OpenClaw 缓存稳定性（#2219） | agent identity/memory 一致性（#2227） | 产品化封装 OpenClaw，聚焦会话与记忆稳定性 |
| **CoPaw** | 视觉 fallback（#5615）、MiniMax 审核误判（#5505） | 上下文硬上限（#5342/#5510）、scroll 策略（#5629） | 工具结果截断、模型自动降级（#5572） | AgentScope 2.0 迁移，强调动态模型切换与多模态降级 |
| **ZeroClaw** | vision_provider 静默忽略（#6841）、computer-use RFC（#6909） | 历史截断文档（#8436）、WhatsApp 被动上下文（#8379） | reasoning+工具调用协议适配（#5600/#7756/#8054） | provider 消息序列化合规为核心，SOP 程序记忆与 WASM 插件为 v0.8.3 方向 |

**技术路线差异**：
- **OpenClaw / ZeroClaw / CoPaw** 偏向"协议层正确性"——聚焦 provider 消息格式、reasoning 内容、工具调用序列化的跨平台一致。
- **NanoBot / IronClaw** 偏向"成本与上下文效率"——通过压缩、缓存、渐进式披露降低长上下文开销。
- **Hermes Agent / LobsterAI / NanoClaw** 偏向"产品化稳定性"——客户端崩溃、认证状态、记忆一致性等工程可靠性。
- **PicoClaw / NullClaw** 研究信号较弱，处于功能修补或维护期。

---

## 4. 共同关注的技术方向

| 方向 | 涉及项目 | 具体诉求 |
|---|---|---|
| **Reasoning 模型与工具调用的协议适配** | ZeroClaw (#5600/#7756)、OpenClaw (#95051/#97875)、CoPaw (#5573)、Hermes (#55276) | reasoning_content、thinking_budget、tool schema 在不同 provider/通道间传递时被静默丢弃或格式不兼容 |
| **视觉语言能力声明与降级** | OpenClaw (#81525/#93848)、Hermes (#35876)、CoPaw (#5615/#5505)、ZeroClaw (#6841/#6909) | 模型是否真支持图像输入缺乏验证；fallback/降级策略不一致；审核误判导致模型"看不见图"而幻觉 |
| **长上下文成本与缓存效率** | NanoBot (#4222/#4581/#4588)、OpenClaw (#94518)、CoPaw (#3891/#5510)、Hermes (#55191/#42405) | prefix caching 被破坏、上下文膨胀、压缩阈值处崩溃、工具输出无硬上限 |
| **工具调用状态一致性** | OpenClaw (#81567/#81490/#80918)、NanoBot (#4595/#4596)、ZeroClaw (#8441/#7909)、IronClaw (#5415/#5417) | tool_call id 污染、subagent 不恢复父 session、incomplete turn 被丢弃、工具选择错误 |
| **认证/权限/状态幻觉** | IronClaw (#5416/#5421)、OpenClaw (#97953/#80040)、NanoClaw (#2886/#2880) | OAuth 状态错误报告、权限边界收紧、provider 切换导致重复执行 |
| **多 agent 编排与标准化** | Hermes (#5257)、ZeroClaw (#7218)、NanoBot (#4571) | ACP/A2A 协议泛化、agent 发现、跨委托深度控制 |

---

## 5. 差异化定位分析

| 维度 | 代表性项目 | 关键差异 |
|---|---|---|
| **核心定位** | OpenClaw（基础框架）、LobsterAI（产品化封装）、NanoBot（成本敏感型）、Hermes（多平台客户端）、ZeroClaw（协议合规型） | OpenClaw 是生态参照基座；LobsterAI 做桌面/IDE 集成；NanoBot 强调低资源部署；Hermes 覆盖 Telegram/Signal/WhatsApp 等消息平台；ZeroClaw 强调 provider 兼容与 WASM 插件 |
| **目标用户** | OpenClaw/LobsterAI（开发者+终端用户）、NanoBot（自部署/成本敏感用户）、Hermes（跨平台 IM 用户）、IronClaw（NEAR AI 生态/企业）、CoPaw（Qwen/AgentScope 生态） | 用户画像从"极客开发者"到"企业工作流"分化明显 |
| **技术架构** | OpenClaw（通道-模型-工具分层）、IronClaw（Reborn 引擎+WebUI v2）、ZeroClaw（WASM 插件+SOP 程序记忆）、CoPaw（AgentScope 2.0 scroll 上下文） | 架构演进方向：从 monolithic agent loop 向可组合、可观测、可迁移的 runtime 演进 |
| **视觉语言能力** | CoPaw/ZeroClaw/Hermes  actively 推进；NanoBot/IronClaw 今日无信号；OpenClaw 聚焦验证 gap | 视觉能力从"有无"进入"正确降级与验证"阶段 |
| **商业化路径** | LobsterAI（发布节奏明确）、IronClaw（NEAR AI 绑定）、NanoClaw（企业渠道集成） | 产品化项目更关注发布稳定性与用户体验；研究型项目更关注协议与评估基础设施 |

---

## 6. 社区热度与成熟度

| 层级 | 项目 | 特征 |
|---|---|---|
| **快速迭代期** | OpenClaw、ZeroClaw、CoPaw、Hermes Agent、NanoBot | 单日 50 PR/Issue 级别，新方向密集涌现，但积压高；研究信号强，稳定性债务同步累积 |
| **质量巩固期** | IronClaw、LobsterAI | IronClaw 密集补测试/认证/QA 底座；LobsterAI 发布补丁版本修复 OpenClaw 集成回归 |
| **工程维护期** | NanoClaw、NullClaw | 活跃度中低，以渠道适配、安全修复、CLI 体验为主，研究创新少 |
| **低活跃/停滞风险** | PicoClaw、TinyClaw、Moltis、ZeptoClaw | PicoClaw 有 stale PR/Issue 但无合并；其余三者 24h 无活动 |

---

## 7. 值得关注的趋势信号

1. **Reasoning 成为 agent 可靠性的新瓶颈**：多个项目同时暴露 reasoning_content/thinking_budget 在 provider、通道、工具调用链路中的传递断裂。对开发者的启示：构建 agent 时需将 reasoning 协议视为一等公民，而非普通文本内容。

2. **视觉语言从"支持"进入"验证与降级"阶段**：能力声明未验证、图像被占位符替换、审核误判缓存等问题集中爆发。对开发者的启示：多模态系统需要 capability validation layer 和明确的降级策略，避免静默幻觉。

3. **长上下文成本驱动架构创新**：上下文压缩、渐进式工具披露、prefix caching 优化、工具输出硬上限成为共同工程主题。对开发者的启示：长上下文能力不等于"全部塞进 prompt"，检索式、分层式、预算式上下文管理将成为标配。

4. **工具调用状态机是 agent 可靠性的核心战场**：tool_call id 污染、subagent session 恢复、incomplete turn 分类、技能误激活等问题跨项目重复出现。对开发者的启示：agent 框架的竞争力正从"能调用工具"转向"工具调用状态可追踪、可恢复、可审计"。

5. **多 agent 协议标准化诉求升温**：ACP 泛化（Hermes #5257）、A2A agent 发现（ZeroClaw #7218）、NanoBot A2A delegation（#4571）显示社区对跨 agent 协作协议的强烈需求。对开发者的启示：单一 agent 框架的壁垒正在下降，协议层与编排能力将成为下一轮竞争焦点。

6. **安全与权限边界从"可选项"变为"基础设施"**：OpenClaw ACP runtime owner 权限（#97953）、NanoClaw symlink 逃逸（#2880）、NanoBot shell guard 绕过（#4592）、IronClaw RBAC（#5425）显示安全设计正在前置。对开发者的启示：agent 具备代码执行与外部调用能力后，沙箱、权限、审计必须内建于架构而非事后补丁。

---

**总结**：2026-06-30 的生态动态表明，个人 AI 助手/自主智能体开源领域正经历从"功能扩张"到"可靠性深化"的关键转折。研究者和开发者应优先关注 reasoning-工具调用协议适配、视觉能力验证、长上下文成本优化与多 agent 协作协议四个方向，这些将是下一阶段技术突破与产品差异化的主战场。

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 项目日报 · 2026-06-30

## 1. 今日速览

过去 24 小时 NanoBot 社区保持高度活跃，共更新 **7 条 Issues**（4 开 3 关）和 **32 条 PR**（22 待合并/10 已合并或关闭），无新版本发布。开发重心集中在**上下文压缩与成本优化**、**推理机制增强**、**工具调用可靠性**以及**安全加固**四个方向。多个高相关性 PR 同时推进，显示项目正处于密集迭代期，整体健康度良好，但待合并 PR 数量较高（22 条），需关注 review 带宽。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

### 已关闭/合并的重要 PR

| PR | 作者 | 进展说明 | 链接 |
|---|---|---|---|
| #4502 Add gateway webhook triggers | chengyongru | 新增顶层 `webhooks` 配置与网关入站 Webhook 触发器，替代旧的 inline health listener，引入共享 HTTP ingress、请求体限制与超时机制，支持通用与 GitHub 风格 Webhook。 | [PR #4502](https://github.com/HKUDS/nanobot/pull/4502) |

### 已关闭的重要 Issue

| Issue | 作者 | 进展说明 | 链接 |
|---|---|---|---|
| #4222 max_messages truncation and microcompact 持续破坏 prefix/prompt caching | imkuang | 识别并修复了上下文治理管道中 `max_messages` 截断边界漂移与 `microcompact` 导致的前缀缓存失效问题，对长上下文推理成本有直接影响。 | [Issue #4222](https://github.com/HKUDS/nanobot/issues/4222) |
| #660 "ultra-lightweight" 宣传与 Node.js 依赖争议 | besoeasy | 关于项目依赖体积的社区讨论已关闭，属产品定位反馈，与研究主线相关性较低。 | [Issue #660](https://github.com/HKUDS/nanobot/issues/660) |
| #4597 测试 Issue | hamb1y-bot-hkuds-nanobot | 测试用，已关闭。 | [Issue #4597](https://github.com/HKUDS/nanobot/issues/4597) |

**整体推进评估**：今日核心进展在于**长上下文缓存效率**与**外部触发机制**两大基础设施能力。上下文缓存修复直接关联推理成本与长对话稳定性；Webhook 触发器扩展了 agent 与外部系统的集成边界。

---

## 4. 社区热点

### 讨论与研究相关热点

| 条目 | 热度指标 | 核心诉求 | 链接 |
|---|---|---|---|
| #4419 Automatic reasoning effort escalation | Open, 4 评论 | 请求在配置中支持默认与升级两级 `reasoningEffort`，使模型能根据问题难度自动切换推理深度。这直接涉及**推理机制/自适应推理**研究。 | [Issue #4419](https://github.com/HKUDS/nanobot/issues/4419) |
| #4222 prompt caching 失效（已关） | Closed, 3 评论 | 长上下文场景下 prefix caching 被频繁破坏，导致成本与延迟上升。修复后对低上下文窗口模型尤为重要。 | [Issue #4222](https://github.com/HKUDS/nanobot/issues/4222) |
| #660 Node.js 依赖争议（已关） | Closed, 15 评论, 5 👍 | 社区对"ultra-lightweight"定位与运行时依赖膨胀的不满，偏向产品/工程而非研究。 | [Issue #660](https://github.com/HKUDS/nanobot/issues/660) |

**背后诉求分析**：社区最强烈的研究相关诉求是**让 NanoBot 更智能地分配推理资源**（#4419）以及**降低长上下文运行成本**（#4222、#4581、#4588）。这反映出用户正在将 NanoBot 用于更复杂、更长周期的任务，对推理效率与成本敏感。

---

## 5. Bug 与稳定性

按严重程度排列：

| 严重度 | Issue/PR | 描述 | 状态 |
|---|---|---|---|
| 🔴 高 | #4595 / #4596 | `apply_final_call_ids` 覆盖非文件编辑工具的正确 `tool_call.id`，导致会话持久化中毒，后续每次调用都失败。已有 fix PR #4596。 | Open，有 fix |
| 🔴 高 | #4592 / #4594 | shell guard 路径提取未识别 `=` 后的绝对路径（如 `curl --output=/etc/passwd`），可绕过 `restrictToWorkspace` 工作区隔离。已有 fix PR #4594。 | Open，有 fix |
| 🟡 中 | #4583 | 配置加载时工具键迁移对 null 节段无防护，可能引发迁移异常。 | Open，有 fix |
| 🟡 中 | #4584 | MCP server URL 中的凭证（userinfo/query token）在日志中未脱敏，存在凭证泄露风险。 | Open，有 fix |
| 🟡 中 | #4567 | 微信渠道未正确传递 `streaming` 配置，导致回退到非流式 API，部分上游 relay 丢失 `tool_use` 字段。 | Open |
| 🟢 低 | #4577 测试 PR | 为 bwrap sandbox 挂载 `/tmp` tmpfs 增加回归测试。 | Open |

**研究相关性说明**：#4595 属于**工具调用一致性与幻觉/错误累积**问题——错误的 tool_call id 会污染会话状态，导致模型在后续轮次中基于损坏的上下文继续推理，可能放大错误。#4592 属于**AI 代理安全边界**问题，与可靠性研究相关。

---

## 6. 功能请求与路线图信号

| 功能请求 | 研究相关性 | 纳入下一版本可能性 | 链接 |
|---|---|---|---|
| #4419 自动推理力度升级 | **推理机制/自适应推理** | 高。已有配置字段 `reasoningEffort`，只需扩展默认+升级两级逻辑，实现成本低。 | [Issue #4419](https://github.com/HKUDS/nanobot/issues/4419) |
| #4581 / #4588 上下文压缩与工具输出精简 | **长上下文理解/成本优化** | 极高。两个 PR 同时推进，分别针对 persisted subagent 公告与命令输出压缩，已形成完整方案。 | [PR #4581](https://github.com/HKUDS/nanobot/pull/4581) / [PR #4588](https://github.com/HKUDS/nanobot/pull/4588) |
| #4571 原生 A2A peer delegation | **多智能体协作/推理分发** | 中高。PR 已开，实现 agent registry、cross-delegation depth guard 等机制，是 #4179 的部分闭环。 | [PR #4571](https://github.com/HKUDS/nanobot/pull/4571) |
| #4291 subagent 可配置模型 preset | **训练/推理后对齐/模型路由** | 中高。已开 PR，允许子代理使用与父代理不同的模型 preset，涉及模型能力路由。 | [PR #4291](https://github.com/HKUDS/nanobot/pull/4291) |
| #4554 Dream 重复技能写保护 | **记忆/知识管理** | 中。PR 已开，通过写守卫防止 Dream 创建重复 skill，减少记忆膨胀。 | [PR #4554](https://github.com/HKUDS/nanobot/pull/4554) |
| #4589 Dream prompt 记忆卫生指令 | **记忆质量/幻觉抑制** | 中。纯 prompt 改动， net +6 行，旨在抑制 MEMORY.md 膨胀与事实腐烂。 | [PR #4589](https://github.com/HKUDS/nanobot/pull/4589) |

**视觉语言能力**：今日数据中**未出现**与视觉语言（VL）能力直接相关的 Issue 或 PR，说明该方向近期不是社区焦点。

---

## 7. 用户反馈摘要

### 真实痛点

- **长上下文成本高企**：用户持续反馈输入 token 与上下文膨胀问题，推动 #4581、#4588 两个独立优化 PR。
- **推理资源分配粗放**：#4419 反映用户希望模型"该深则深、该浅则浅"，避免统一高推理力度带来的成本浪费。
- **工具调用状态不可靠**：#4595 显示 streaming + 并行工具调用场景下，内部状态覆盖会导致会话级损坏。
- **安全隔离边界不完整**：#4592 暴露参数解析器对 `key=value` 形式的覆盖不足，实际生产环境存在逃逸风险。

### 使用场景

- 长周期、多轮 agent 协作任务（subagent、A2A delegation）。
- 成本敏感的低上下文窗口模型部署。
- 需要工作区隔离的代码/执行环境。

### 满意/不满意

- **满意**：社区对上下文缓存修复（#4222）、Webhook 扩展（#4502）、上下文压缩（#4581/4588）等主动优化响应积极。
- **不满意**：对项目"轻量"定位与实际依赖体积的质疑（#660）显示部分用户对工程简洁性有较高期待。

---

## 8. 待处理积压

以下长期未合并/未响应条目值得维护者优先关注：

| 条目 | 创建时间 | 最后更新 | 风险/提醒 | 链接 |
|---|---|---|---|---|
| #4293 pending_queue for subagent result injection in process_direct | 2026-06-11 | 2026-06-29 | 已开 18 天，影响 cron job 等直接调用场景下的子代理结果注入，可能导致任务完成状态丢失。 | [PR #4293](https://github.com/HKUDS/nanobot/pull/4293) |
| #4291 subagent 可配置模型 presets | 2026-06-11 | 2026-06-29 | 已开 18 天，是多智能体模型路由的重要能力，建议尽快 review。 | [PR #4291](https://github.com/HKUDS/nanobot/pull/4291) |
| #4554 Dream 重复技能写保护 | 2026-06-26 | 2026-06-29 | 相对较新，但与记忆膨胀直接相关，建议配合 #4589 一起 review。 | [PR #4554](https://github.com/HKUDS/nanobot/pull/4554) |

---

**总结**：NanoBot 今日在**推理效率、长上下文成本、工具调用可靠性、安全边界**四个研究相关方向均有实质动作，但 PR 积压较多，建议维护者优先 review #4581/#4588（上下文压缩）、#4595/#4596（tool_call id 损坏）、#4592/#4594（工作区隔离绕过）以及 #4419（自适应推理力度）。

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 项目日报（2026-06-30）

## 1. 今日速览

Hermes Agent 今日保持**高活跃度**：过去 24 小时 Issues 更新 50 条（47 活跃/新开，3 关闭），PR 更新 50 条（44 待合并，6 已合并/关闭），无新版本发布。社区讨论重心集中在**网关消息投递可靠性**、**多平台格式化一致性**、**桌面端稳定性**以及**配置/认证体验**上。研究相关议题中，视觉语言能力的 fallback 机制、reasoning_effort 参数透传、长上下文压缩与路由恢复等话题值得持续关注。整体项目健康度良好，但待合并 PR 积压较高（44 条），部分安全与稳定性修复已有关闭 PR。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

今日已合并/关闭的重要 PR 共 6 条，主要推进以下方向：

| PR | 作者 | 说明 |
|---|---|---|
| [#55299](https://github.com/NousResearch/hermes-agent/pull/55299) | liuhao1024 | 修复 `truncate_message()` 中代码围栏闭合检测，要求围栏标记后仅允许空白字符，符合 CommonMark 规范。 |
| [#55266](https://github.com/NousResearch/hermes-agent/pull/55266) | Stoltemberg | 修复 Windows 8.3 短文件名导致的媒体路由测试失败。 |
| [#55249](https://github.com/NousResearch/hermes-agent/pull/55249) | Stoltemberg | 为 Signal JSON-RPC 响应增加 16 MiB 内容上限，防止内存耗尽。 |
| [#55251](https://github.com/NousResearch/hermes-agent/pull/55251) | Stoltemberg | 为网关代理模式错误响应增加内容上限。 |
| #43196 / #55268 | — | Issues 关闭，涉及桌面 PTY 崩溃与 MoA aggregator 404 问题。 |

**研究相关进展**：代码块分片与消息截断的语义正确性得到加固，这对长上下文场景下的输出可靠性有直接帮助；Signal/代理响应体上限的引入属于 AI 系统对外部不可信输入的防御性加固，与系统可靠性研究相关。

---

## 4. 社区热点

### 评论最多的 Issues

1. **[#5257 feat: Generalized ACP client for multi-agent CLI orchestration](https://github.com/NousResearch/hermes-agent/issues/5257)**（13 评论，18 👍）  
   提出将现有 Copilot 专用 ACP 客户端泛化为通用 ACP 客户端，使 Hermes 能作为编排器驱动 Claude Code、Codex、Gemini CLI 等外部 agent。这反映了社区对**多 agent 协作协议与工具调用标准化**的强烈诉求，与 post-training 对齐和 agent 可靠性研究间接相关。

2. **[#4438 Rich Spreadsheet Skill (xlsx / csv)](https://github.com/NousResearch/hermes-agent/issues/4438)**（5 评论）  
   要求为 Excel/CSV 提供结构化抽象，减少 agent 每次从零推理库用法的负担。属于**工具使用能力与结构化 I/O** 的研究方向。

3. **[#35876 fix(vision): _resolve_single_provider kwargs regression — fallback_chain silently fails on Gemini quota errors](https://github.com/NousResearch/hermes-agent/issues/35876)**（4 评论）  
   视觉模块在 Gemini 触发 429 配额错误后，fallback chain 因 `kwargs` 转发失败而静默失效。直接涉及**视觉语言能力的鲁棒性与多 provider fallback 机制**。

4. **[#24039 Auxiliary fallback chain should reuse fallback_providers](https://github.com/NousResearch/hermes-agent/issues/24039)**（3 评论，2 👍）  
   指出存在两套互不知晓的 fallback 系统，建议统一配置。关系到**推理链路冗余设计与系统可靠性**。

5. **[#42405 Memory at capacity → 'replace' zero-match retry loop → no response](https://github.com/NousResearch/hermes-agent/issues/42405)**（3 评论）  
   记忆模块在容量上限时进入零匹配重试循环并静默挂起。属于**长上下文记忆管理与 agent 自我修正失败**的可靠性问题。

---

## 5. Bug 与稳定性

按严重程度排列：

### P1（高优先级）

- **[#42405 Memory at capacity → 'replace' zero-match retry loop → no response](https://github.com/NousResearch/hermes-agent/issues/42405)**  
  记忆替换失败导致无响应静默挂起，严重影响长会话可用性。**暂无 fix PR**。

### P2（中优先级）

- **[#35876 fix(vision): fallback_chain silently fails on Gemini quota errors](https://github.com/NousResearch/hermes-agent/issues/35876)**  
  视觉 fallback 在 Gemini 配额耗尽时静默失败。**暂无 fix PR**。

- **[#24039 Auxiliary fallback chain should reuse fallback_providers](https://github.com/NousResearch/hermes-agent/issues/24039)**  
  两套 fallback 系统配置割裂，可能导致冗余失效。**暂无 fix PR**。

- **[#51560 fallback_providers as JSON string silently empties the fallback chain](https://github.com/NousResearch/hermes-agent/issues/51560)**  
  CLI 设置将 fallback_providers 存为 JSON 字符串，解析器静默丢弃。**暂无 fix PR**。

- **[#55191 Desktop renderer crash-loops at ~128K-token compaction threshold](https://github.com/NousResearch/hermes-agent/issues/55191)**  
  macOS 桌面端在长上下文压缩阈值处渲染进程反复崩溃。**暂无 fix PR**。

- **[#55071 Gateway chat sanitizer leaks unexpected-status 401 auth envelopes](https://github.com/NousResearch/hermes-agent/issues/55071)**  
  网关未过滤 `unexpected status 401 Unauthorized` 原始认证错误，可能泄露到用户聊天界面。**暂无 fix PR**。

- **[#55265 Cron delivery to private chat forum-topics lands in General](https://github.com/NousResearch/hermes-agent/issues/55265)**  
  Telegram 私信论坛主题投递回归。**暂无 fix PR**。

- **[#50775 Visual ghosting/text overlapping on Telegram macOS during streaming](https://github.com/NousResearch/hermes-agent/issues/50775)**（4 👍）  
  流式更新导致 Telegram macOS 客户端出现文字残影/重叠。**暂无 fix PR**。

- **[#55305 Hermes Agent gateway on ZFS corrupts state.db with multiple connections](https://github.com/NousResearch/hermes-agent/issues/55305)**  
  ZFS + SQLite WAL 多连接下出现磁盘 I/O 错误，会话查询全部失败。**暂无 fix PR**。

- **[#55292 truncate_message treats code lines with trailing fence text as closing fences](https://github.com/NousResearch/hermes-agent/issues/55292)**  
  代码块截断时误将带尾随文本的围栏行识别为闭合。**已有 fix PR #55294 / #55299**。

- **[#55300 preserve peer routing across compression recovery](https://github.com/NousResearch/hermes-agent/pull/55300)**  
  长上下文压缩分裂后网关 peer 路由丢失，PR 提供修复与回归测试。

### P3（低优先级，数量较多，略举研究相关）

- **[#55276 reasoning_effort / thinking_budget silently dropped for custom and zai providers](https://github.com/NousResearch/hermes-agent/issues/55276)**  
  `reasoning_effort` / `reasoning_config` 对 `custom`、`zai` 等 provider 被静默丢弃。直接涉及**推理预算控制与 provider 一致性**，**暂无 fix PR**。

- **[#55296 WhatsApp formatter leaves literal asterisks for bold-italic markdown](https://github.com/NousResearch/hermes-agent/issues/55296)**  
  Markdown 加粗斜体转换顺序错误。**已有 fix PR #55298**。

- **[#55279 Microsoft Graph client buffers REST responses without a body cap](https://github.com/NousResearch/hermes-agent/issues/55279)**、**[#55284 Discord server tool reads REST bodies without a cap](https://github.com/NousResearch/hermes-agent/issues/55284)**  
  多个外部 REST 客户端无响应体上限，存在内存耗尽风险。**暂无 fix PR**。

---

## 6. 功能请求与路线图信号

| Issue/PR | 研究相关性 | 纳入下一版本可能性 |
|---|---|---|
| [#5257 Generalized ACP client](https://github.com/NousResearch/hermes-agent/issues/5257) | 多 agent 编排、工具协议标准化 | 高，讨论活跃且 👍 最多 |
| [#4438 Rich Spreadsheet Skill](https://github.com/NousResearch/hermes-agent/issues/4438) | 结构化工具使用、减少 agent 推理负担 | 中，需求明确但实现复杂 |
| [#47320 Portable handoff workflow](https://github.com/NousResearch/hermes-agent/pull/47320) | 长上下文管理、会话状态可迁移性 | 中，已有 PR 待审 |
| [#52136 Show /learn progress steps](https://github.com/NousResearch/hermes-agent/pull/52136) | 用户对齐、可解释性 | 中，PR 已开 |
| [#55233 Config flag to disable trigram FTS index](https://github.com/NousResearch/hermes-agent/issues/55233) | 长上下文存储、状态可扩展性 | 中，生产环境痛点 |

**研究信号**：社区正在从"agent 能做什么"转向"agent 如何稳定、可解释、可协作地完成任务"。ACP 泛化、handoff 工作流、/learn 进度可视化均指向**人机对齐与系统可控性**。

---

## 7. 用户反馈摘要

从 Issues 中提炼的真实痛点：

- **视觉/多模态可靠性**：Gemini 配额耗尽时视觉 fallback 静默失败，用户期望跨 provider 视觉能力有明确故障转移与错误提示（[#35876](https://github.com/NousResearch/hermes-agent/issues/35876)）。
- **长上下文脆弱性**：128K token 压缩阈值导致桌面端崩溃、压缩后 peer 路由丢失、记忆容量上限时无响应，反映长上下文管理仍是核心痛点（[#55191](https://github.com/NousResearch/hermes-agent/issues/55191)、[#55300](https://github.com/NousResearch/hermes-agent/pull/55300)、[#42405](https://github.com/NousResearch/hermes-agent/issues/42405)）。
- **推理参数不透明**：`reasoning_effort` 对部分 provider 被静默丢弃，用户难以控制模型推理深度与成本（[#55276](https://github.com/NousResearch/hermes-agent/issues/55276)）。
- **配置体验割裂**：fallback_providers 存在两套系统、JSON 字符串配置被静默忽略，显示配置抽象与验证机制需要统一（[#24039](https://github.com/NousResearch/hermes-agent/issues/24039)、[#51560](https://github.com/NousResearch/hermes-agent/issues/51560)）。
- **外部输入不可信**：多个网关/工具客户端无响应体上限，生产部署中存在 DoS 风险（[#55279](https://github.com/NousResearch/hermes-agent/issues/55279)、[#55284](https://github.com/NousResearch/hermes-agent/issues/55284)、[#55211](https://github.com/NousResearch/hermes-agent/issues/55211)）。

---

## 8. 待处理积压

以下 Issue/PR 长期活跃但尚未有关键进展，建议维护者优先关注：

| 条目 | 创建时间 | 当前状态 | 提醒原因 |
|---|---|---|---|
| [#5257 Generalized ACP client](https://github.com/NousResearch/hermes-agent/issues/5257) | 2026-04-05 | Open，13 评论 | 高赞路线图级功能，决定多 agent 架构方向 |
| [#4438 Rich Spreadsheet Skill](https://github.com/NousResearch/hermes-agent/issues/4438) | 2026-04-01 | Open，5 评论 | 工具使用抽象的基础建设 |
| [#35876 Vision fallback_chain regression](https://github.com/NousResearch/hermes-agent/issues/35876) | 2026-05-31 | Open，4 评论 | 视觉能力鲁棒性，直接影响多模态可靠性 |
| [#42405 Memory capacity silent hang](https://github.com/NousResearch/hermes-agent/issues/42405) | 2026-06-08 | Open，P1 | 高优先级但无 fix PR |
| [#55191 Desktop crash at 128K threshold](https://github.com/NousResearch/hermes-agent/issues/55191) | 2026-06-29 | Open，P2 | 长上下文产品稳定性关键问题 |
| [#47320 Portable handoff workflow](https://github.com/NousResearch/hermes-agent/pull/47320) | 2026-06-16 | Open PR | 长上下文/session 管理创新方向 |

---

**总结**：Hermes Agent 今日在工程稳定性（响应体上限、代码围栏解析、路由恢复）方面取得实质进展，但在视觉语言 fallback、推理预算透传、长上下文压缩与记忆管理等研究关键领域仍存在未修复问题。社区对多 agent 编排（ACP）和结构化工具能力的需求持续升温，建议维护者在处理高优先级 bug 的同时，对路线图级 Issue 给出明确回应。

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目日报 — 2026-06-30

## 1. 今日速览

过去24小时，PicoClaw 项目活跃度较低：Issues 与 PR 各更新 3 条，但无已合并 PR、无新版本发布。社区讨论集中在网关协议扩展（SimpleX/Tox/DeltaChat）、Bedrock 提示缓存优化、以及 Doubao Seed 模型工具调用输出泄漏问题。整体项目处于功能修补与集成适配阶段，核心推理/多模态能力未见显著进展。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

今日无已合并或已关闭的 PR，项目代码主线未发生推进。

- 3 条 PR 均处于待合并状态，分别涉及：DeltaChat 网关接入、AWS Bedrock Converse API 提示缓存、以及 per-turn token 用量上报。这些 PR 目前均未完成 review 或合并。

---

## 4. 社区热点

| 条目 | 类型 | 热度信号 | 链接 |
|---|---|---|---|
| #3093 [Feature] I need SimpleX or tox | Issue | 4 条评论，1 个 👍 | https://github.com/sipeed/picoclaw/issues/3093 |
| #3090 [BUG] Panel does not work on Safari on iOS versions below 16.4 | Issue | 3 条评论，已关闭 | https://github.com/sipeed/picoclaw/issues/3090 |
| #3063 feat: add deltachat gateway | PR | 网关扩展相关 | https://github.com/sipeed/picoclaw/pull/3063 |

**诉求分析：**
- 用户对去中心化/隐私导向的通信网关（SimpleX、Tox、DeltaChat）需求明确，反映 PicoClaw 作为桥接工具被用于多元化消息协议场景。
- iOS Safari 兼容性问题已关闭，说明前端兼容性仍是部分用户关注重点，但不属于研究相关议题。

---

## 5. Bug 与稳定性

| 严重度 | Issue | 描述 | 状态 | Fix PR |
|---|---|---|---|---|
| 中 | #3153 | Volcengine Doubao Seed 工具调用偶尔以原始 `<seed:tool_call>` 文本泄漏给用户，未被执行 | Open | 无 |

**研究相关性说明：** 该问题涉及 LLM 工具调用输出的解析与后处理可靠性，属于**模型输出结构化 / 幻觉类问题**的边缘案例——即模型生成了看似结构化的工具调用标记，但未被系统正确识别和执行，导致"伪输出"暴露给用户。建议关注是否与模型特定的 tool-call 包装格式匹配不完整有关。

---

## 6. 功能请求与路线图信号

| 条目 | 内容 | 纳入下一版本可能性 |
|---|---|---|
| #3093 | 增加 SimpleX 或 Tox 网关 | 中。已有 DeltaChat 网关 PR #3063 在推进，说明项目对去中心化消息网关持开放态度；SimpleX/Tox 可作为后续扩展。 |
| #3063 | DeltaChat 网关 | 较高。PR 已开启一段时间，属于新增功能+文档更新，若 review 通过较易合并。 |
| #3163 | Bedrock Converse prompt caching via cache points | 较高。属于云服务商 API 成本优化特性，工程价值明确。 |
| #3156 | 每轮对话 LLM token 用量上报 | 中。属于可观测性增强，对下游计费/监控有用，但需考虑隐私与协议兼容性。 |

---

## 7. 用户反馈摘要

- **痛点：** Doubao Seed 模型在工具调用场景下输出不稳定，存在原始工具调用标记泄漏问题，影响用户体验与系统可靠性。
- **使用场景：** 用户希望 PicoClaw 作为统一网关桥接更多去中心化/隐私通信协议（SimpleX、Tox、DeltaChat），暗示项目被用于跨平台消息集成。
- **兼容性：** 旧版 iOS Safari 前端兼容问题虽已关闭，但说明移动端 Web 面板仍有碎片化适配压力。

---

## 8. 待处理积压

| 条目 | 创建时间 | 最后更新 | 风险提示 |
|---|---|---|---|
| #3093 SimpleX/Tox 网关请求 | 2026-06-10 | 2026-06-29 | 已标记 stale，近 20 天无实质推进，社区有明确需求但无对应 PR |
| #3063 DeltaChat 网关 PR | 2026-06-08 | 2026-06-29 | 已开启 22 天，评论数未定义，可能存在 review 瓶颈 |
| #3153 Doubao Seed 工具调用泄漏 | 2026-06-22 | 2026-06-29 | 已标记 stale，影响模型输出可靠性，建议优先跟进 |

---

**健康度评估：** 今日项目活跃度偏低，无合并进展，多个 PR/Issue 进入 stale 状态。研究相关议题中，仅 #3153 涉及 LLM 输出结构化与工具调用可靠性，值得维护者优先关注。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目日报 · 2026-06-30

## 1. 今日速览

过去 24 小时 NanoClaw 仓库活跃度处于**中等偏低水平**：无新版本发布，无新增 Issue，仅有 7 条 PR 更新（5 条待合并、2 条已关闭/合并）。今日活动高度集中在**渠道集成与基础设施稳定性**层面，包括 Discord/Slack 适配器补齐、安全漏洞修复、语音播报策略迭代以及仪表盘状态推送。与研究关注的核心主题（视觉语言能力、推理机制、训练方法论、幻觉问题）**几乎无直接交集**，整体未出现模型能力或算法层面的显著进展。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

### 已关闭/合并的 PR

| PR | 作者 | 内容 | 研究/工程意义 |
|---|---|---|---|
| [#2883](https://github.com/nanocoai/nanoclaw/pull/2883) feat: voice-notify v3 意图分流 + kill-switch | tier2tech-tian | 将语音播报摘要从单一策略改为 5 类意图分流（action / silent / navigate / tech_status / notify），跳过代码块/长表格，突出行动项，保留技术汇报关键数据；新增 `VOICE_SUMMARY_VERSION=off` 运行时关闭开关 | 属于**输出形式化/摘要策略**的工程优化，可间接关联到多模态输出控制与可解释性，但未涉及底层视觉语言模型或推理机制 |
| [#2882](https://github.com/nanocoai/nanoclaw/pull/2882) fix(ncl): default messaging-groups create instance to channel_type | omri-maya | 修复 `ncl messaging-groups create` 因迁移 016 新增 `instance TEXT NOT NULL` 列但 CRUD 未声明导致的 `NOT NULL` 约束违反 | 纯 CLI/数据层回归修复 |

**整体推进评估**：今日合并内容以运维工具与渠道体验修复为主，未推动核心模型能力或研究议程。

---

## 4. 社区热点

今日无任何 Issue，PR 评论数与反应数均为 0，不存在典型"社区热点"。从 PR 主题分布看，维护者近期关注焦点为：

- **渠道生态扩展**：Discord 适配器（[#2884](https://github.com/nanocoai/nanoclaw/pull/2884)）、Slack Socket Mode 引导流程（[#2885](https://github.com/nanocoai/nanoclaw/pull/2885)）
- **安全加固**：会话目录符号链接逃逸（[#2880](https://github.com/nanocoai/nanoclaw/pull/2880)）
- **可观测性**：仪表盘状态推送（[#2871](https://github.com/nanocoai/nanoclaw/pull/2871)）

背后诉求可解读为：NanoClaw 正从"单一聊天代理框架"向"多通道、可部署、可监控的生产平台"演进，社区对**企业级集成与运维可靠性**的需求上升。

---

## 5. Bug 与稳定性

| 严重程度 | PR / 问题 | 状态 | 说明 |
|---|---|---|---|
| 🔴 **高** | [#2880](https://github.com/nanocoai/nanoclaw/pull/2880) fix(security): contain inbox symlink escapes in attachment writes | 待合并 | CWE-59：会话目录以可写方式挂载进 agent 容器，被攻破的 agent 可通过预置 symlink 导致宿主机任意文件写入。PR 在入站/出站文件写入路径均做了 containment |
| 🟡 **中** | [#2886](https://github.com/nanocoai/nanoclaw/pull/2886) fix: channel-registered new agents inherit the install's provider | 待合并 | 新聊天渠道注册时创建的 agent 组默认使用 Claude 内置 provider，单 provider 安装场景下会导致 401；修复后继承安装级 provider |
| 🟡 **中** | [#2882](https://github.com/nanocoai/nanoclaw/pull/2882) fix(ncl): default messaging-groups create instance to channel_type | 已关闭 | CLI 因 schema 迁移与 CRUD 定义不一致导致插入失败 |

无已报告的崩溃、回归或性能衰退 Issue。

---

## 6. 功能请求与路线图信号

今日无用户提交的功能请求 Issue。从已开放 PR 可推断的近期路线图信号：

| PR | 信号 |
|---|---|
| [#2884](https://github.com/nanocoai/nanoclaw/pull/2884) Discord channel adapter | 渠道矩阵继续扩张，覆盖 Discord Gateway DMs |
| [#2885](https://github.com/nanocoai/nanoclaw/pull/2885) Slack Socket Mode setup | 降低 Slack 私有化/防火墙内部署门槛 |
| [#2871](https://github.com/nanocoai/nanoclaw/pull/2871) dashboard pusher + OpenCode support | 强化可观测性与 IDE/开发工具生态集成 |

**研究相关信号**：无。未出现针对视觉语言理解、链式推理、RLHF/post-training 对齐、幻觉缓解的 PR 或 Issue。

---

## 7. 用户反馈摘要

今日无 Issue 评论数据，无法提炼真实用户痛点。建议维护者关注：当前社区互动指标（Issue/PR 评论、👍）均为 0，可能反映：
- 项目处于内部主导的功能冲刺期，外部用户反馈渠道尚未被激活；
- 或数据采集范围未覆盖讨论区（Discussions）与外部 Slack/Discord 社区。

---

## 8. 待处理积压

由于今日无新增 Issue 且未提供历史积压列表，无法识别长期未响应项。建议维护者优先审阅以下**已开放且存在明确风险/阻塞**的 PR：

1. [#2880](https://github.com/nanocoai/nanoclaw/pull/2880) — 安全漏洞修复，应尽快合并
2. [#2886](https://github.com/nanocoai/nanoclaw/pull/2886) — 渠道注册核心流程的 provider 继承问题
3. [#2885](https://github.com/nanocoai/nanoclaw/pull/2885) — Slack Socket Mode 引导流程补漏，影响主线功能完整性

---

## 研究视角附注

从本日 NanoClaw 动态来看，该项目当前阶段的重点是**工程化部署、渠道适配与安全加固**，而非多模态模型能力或后训练对齐研究。若研究目标是追踪视觉语言推理、长上下文、幻觉缓解等方向的最新进展，建议将 NanoClaw 的监控优先级调低，或扩展监控范围至其依赖库（如 `@chat-adapter/*`、底层 LLM provider 抽象层）以及相关的模型服务仓库。

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw 项目日报 · 2026-06-30

## 1. 今日速览

过去 24 小时 NullClaw 仓库活跃度较低，无新增 Issue，仅有 4 条 PR 更新，其中 1 条重复提交的 CLI REPL PR 被关闭，剩余 3 条待合并。整体研发活动集中在**开发者体验（CLI 交互）**与**工具调用基础设施**，未涉及视觉语言、推理机制、训练方法论或幻觉相关的核心研究议题。项目健康度平稳，但研究向进展信号微弱。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

### 已关闭 PR

- **#960** `fix(cli): handle arrow keys in agent REPL`  
  作者：vernonstinebaker  
  链接：https://github.com/nullclaw/nullclaw/pull/960  
  说明：该 PR 与今日新开的 #970 内容重复，已被关闭。其核心目标是为 `nullclaw agent` 交互式 REPL 引入无分配行编辑器并启用 POSIX raw-mode 输入，支持方向键、历史导航、光标移动、Home/End 等快捷键。关闭原因为避免重复，实际功能推进由 #970 承接。

### 待合并 PR（今日活跃）

- **#971** `feat(streaming): native tool calls during SSE streaming`  
  作者：vernonstinebaker  
  链接：https://github.com/nullclaw/nullclaw/pull/971  
  说明：将原生工具调用支持与流式传输路径解耦。此前，只要附加了流回调，agent 循环就会禁用原生工具，强制将工具降级为 prompt-injection 格式。该 PR 允许支持原生流式工具的 provider 在 SSE 流中直接发出工具调用，属于**推理执行路径与工具编排基础设施**的改进，对依赖流式交互的 agent 可靠性有正面意义。

- **#970** `fix(cli): handle arrow keys in agent REPL`  
  作者：vernonstinebaker  
  链接：https://github.com/nullclaw/nullclaw/pull/970  
  说明：#960 的替代版本，聚焦 CLI 交互体验修复，与研究核心能力无直接关联。

- **#956** `ci(deps): bump alpine from 3.23 to 3.24 in the docker-images group`  
  作者：dependabot[bot]  
  链接：https://github.com/nullclaw/nullclaw/pull/956  
  说明：Dependabot 发起的 Docker 基础镜像更新，属于常规依赖维护。

**整体推进评估**：今日项目在技术债务与开发者体验方面有所推进，#971 对 agent 工具调用架构有中等重要性，但未触及模型能力、对齐或幻觉等研究前沿。

---

## 4. 社区热点

今日无新增 Issue，PR 均无评论与点赞。最活跃的讨论点实质上是**重复提交的 CLI REPL PR（#960 / #970）**，反映出维护者在整理积压 PR 时的清理动作，而非社区需求爆发。

- #960 关闭：https://github.com/nullclaw/nullclaw/pull/960
- #970 替代：https://github.com/nullclaw/nullclaw/pull/970

背后诉求：CLI REPL 的可用性（方向键、历史记录）是终端用户的基础体验需求，但属于工程完善，而非研究能力扩展。

---

## 5. Bug 与稳定性

今日无新报告 Bug。唯一与稳定性相关的条目：

- **#970 / #960** — CLI REPL 中方向键等特殊输入被打印为控制字符，影响交互体验。  
  严重程度：低（用户体验问题，非功能崩溃）  
  状态：已有 fix PR（#970 待合并）  
  链接：https://github.com/nullclaw/nullclaw/pull/970

---

## 6. 功能请求与路线图信号

今日无用户提出的新功能请求。从现有 PR 可推断的路线图信号：

| PR | 信号 | 纳入下一版本可能性 |
|---|---|---|
| #971 原生流式工具调用 | 强化 agent 流式推理与工具编排能力 | 高 |
| #970 CLI REPL 交互修复 | 提升开发者体验 | 高 |
| #956 Alpine 升级 | 常规安全/依赖维护 | 高（低风险） |

未观察到与**视觉语言能力、推理机制、训练方法论、幻觉缓解**直接相关的功能信号。

---

## 7. 用户反馈摘要

今日无新增 Issue 评论，无法提炼用户痛点或使用场景。仓库处于低反馈周期。

---

## 8. 待处理积压

今日未出现新的长期未响应项。建议维护者关注：

- **#971** 作为今日唯一具有架构意义的 PR，建议优先审阅合并，以避免流式场景下工具调用降级带来的可靠性问题。  
  链接：https://github.com/nullclaw/nullclaw/pull/971

---

## 研究相关性总结

| 关注领域 | 今日信号 | 评估 |
|---|---|---|
| 视觉语言能力 | 无 | 无进展 |
| 推理机制 | #971 涉及流式推理中的工具调用路径 | 弱相关，属工程基础设施 |
| 训练方法论 | 无 | 无进展 |
| 幻觉相关问题 | 无 | 无进展 |

**结论**：2026-06-30 的 NullClaw 仓库活动以工程维护与开发者体验为主，研究向内容匮乏，建议在后续跟踪中重点关注模型能力、对齐与可靠性相关的 Issue/PR。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw 项目日报 — 2026-06-30

## 1. 今日速览

过去 24 小时 IronClaw 活跃度较高：Issues 更新 14 条（10 开/活跃、4 关闭），PR 更新 50 条（30 待合并、20 已合并/关闭），无新版本发布。工作重心集中在 **Reborn 架构的测试覆盖、认证/授权流程、WebUI v2 实时 QA 体系** 以及 **上下文/工具披露优化**。从研究视角看，与多模态推理、长上下文理解、post-training 对齐直接相关的内容有限；多数更新属于工程稳定性、产品化与测试基础设施范畴。项目健康度稳定，但存在若干与 **工具选择/调度可靠性、长工具链工作流失败、上下文窗口压力** 相关的信号值得追踪。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

### 已合并/关闭的重要 PR

| PR | 作者 | 核心内容 | 研究/工程意义 |
|---|---|---|---|
| [#5402](https://github.com/nearai/ironclaw/pull/5402) | henrypark133 | Reborn 集成测试框架新增 shared-persistence 组测：覆盖 approvals、auth failure、memory、secrets、extensions | 提升 Reborn 引擎在跨线程 e2e 场景下的可验证性，对 **AI 可靠性 / 工具执行安全性** 有支撑作用 |
| [#5050](https://github.com/nearai/ironclaw/pull/5050) | dependabot | react-router 7.9.1 → 7.15.1 | 常规依赖更新，影响 WebUI 路由稳定性 |
| [#5425](https://github.com/nearai/ironclaw/pull/5425) | henrypark133 | Reborn 多用户 RBAC 融合设计提案（仅设计，不新增 scope） | 与 **AI 安全/权限治理** 相关，但属产品设计文档 |
| [#5372](https://github.com/nearai/ironclaw/pull/5372) | ilblackdragon | 移植 Reborn WebUI 认证与审批 UX 测试覆盖 | 强化 approval gates、OAuth auth gates、tool execution visibility 的浏览器测试 |
| [#5371](https://github.com/nearai/ironclaw/pull/5371) | ilblackdragon | 移植 Reborn WebUI 聊天历史覆盖 | 覆盖 attachments、pending messages、SSE/history、DOM resource bounds |
| [#5423](https://github.com/nearai/ironclaw/pull/5423) | serrrfirat | QA7 routine 措辞变体兼容 | 提升 live QA 对模型输出自然语言变体的鲁棒性 |
| [#5422](https://github.com/nearai/ironclaw/pull/5422) | serrrfirat | 修复 `/canary` PR target 校验 | CI/CD 流程稳健性 |
| [#5406](https://github.com/nearai/ironclaw/pull/5406) | serrrfirat | Reborn live QA 使用 QA sheet 真实用户 prompt | 让 live QA 更贴近真实用户表达，减少 harness 预设指令偏差 |
| [#5414](https://github.com/nearai/ironclaw/pull/5414) | thisisjoshford | WebUI v2 Logs 文本可选中/复制 | 纯 UI 修复 |
| [#5392](https://github.com/nearai/ironclaw/pull/5392) | henrypark133 | Reborn 集成测试框架 slices 3–9：LibSql matrix、egress/HTTP matcher、MCP/OAuth/refresh | 显著扩展 Reborn 内部栈的测试矩阵 |

**整体判断**：今日合并工作以 **测试基础设施、认证/授权/审批流程、QA 自动化** 为主，功能推进偏“夯实底座”，而非新增模型能力。

---

## 4. 社区热点

今日 Issues/PRs 评论数普遍较低（多数为 0 或 1），未出现高讨论度条目。相对值得关注的活跃信号：

| 条目 | 类型 | 热度信号 | 背后诉求 |
|---|---|---|---|
| [#5413](https://github.com/nearai/ironclaw/issues/5413) | Issue (closed) | 1 评论，关联 #5378 | 工程侧希望 OAuth refresh 失败时**显式报错**而非静默吞掉，反映对**可观测性与调试效率**的诉求 |
| [#5411](https://github.com/nearai/ironclaw/issues/5411) | Issue (open) | 0 评论，但内容详实 | 维护者主动发布每日失败分类，体现对 **pinchbench 评估质量** 的重视 |

由于数据未提供 👍/评论具体数值，无法按传统“反应最多”排序。整体社区互动偏冷，以内部维护者/QA 驱动为主。

---

## 5. Bug 与稳定性

按严重程度排列（P1 → P3），重点关注与 **推理可靠性、工具链执行、状态一致性** 相关的问题：

### P1（严重）

| Issue | 描述 | 是否已有 fix PR | 与研究相关性 |
|---|---|---|---|
| [#5415](https://github.com/nearai/ironclaw/issues/5415) | 多工具 Google Sheets 工作流在 18–25 次工具调用后出现 **protocol violation** | 未明确 | **高**——长工具链 / 多步推理工作流的稳定性，直接关联 **长上下文理解与推理机制** |
| [#5420](https://github.com/nearai/ironclaw/issues/5420) | Routine 投递目标是全局每用户默认值，而非 per-routine；修改一个会改变全部 | 未明确 | 中——状态隔离缺陷，影响 agent 行为一致性 |

### P2（较重）

| Issue | 描述 | 是否已有 fix PR | 与研究相关性 |
|---|---|---|---|
| [#5417](https://github.com/nearai/ironclaw/issues/5417) | Hacker News 搜索时错误激活 `tech-debt-tracker` skill，而非 web search skill | 未明确 | **高**——**工具/技能选择错误**，属于推理机制与幻觉/误激活问题 |
| [#5416](https://github.com/nearai/ironclaw/issues/5416) | Google 连接状态报告错误，导致矛盾认证流程 | 未明确 | 中——状态幻觉/对话一致性 |
| [#5418](https://github.com/nearai/ironclaw/issues/5418) | 工具活动后对话消息顺序渲染错误 | 未明确 | 中——UI/交互一致性，可能掩盖真实执行顺序 |

### P3（一般）

| Issue | 描述 | 是否已有 fix PR | 与研究相关性 |
|---|---|---|---|
| [#5419](https://github.com/nearai/ironclaw/issues/5419) | 无法重命名 automation | 未明确 | 低——产品体验 |
| [#5426](https://github.com/nearai/ironclaw/issues/5426) | 创建 routine 时 system drive 不可用 | 未明确 | 低——环境/部署问题 |
| [#5421](https://github.com/nearai/ironclaw/issues/5421) | web search 在 ironclaw-reborn 下非零配置，且重复提示 NEAR AI auth | 未明确 | 中——工具激活与认证状态传递 |

### 已关闭 Bug

| Issue | 描述 | 关闭方式 |
|---|---|---|
| [#5413](https://github.com/nearai/ironclaw/issues/5413) | Reborn inline OAuth refresh 静默吞掉未应用的 refresh | 已关闭（可能已修复） |
| [#5196](https://github.com/nearai/ironclaw/issues/5196) | “Ask each time” 工具权限可能授权错误并触发重复审批流 | 已关闭 |
| [#5412](https://github.com/nearai/ironclaw/issues/5412) | WebUI v2 Logs 文本不可选/复制 | 由 [#5414](https://github.com/nearai/ironclaw/pull/5414) 修复 |

---

## 6. 功能请求与路线图信号

今日数据中没有典型的“用户功能请求”式 Issue，但以下 PR 揭示了产品/技术路线：

| PR | 路线信号 | 是否可能纳入下一版本 |
|---|---|---|
| [#5149](https://github.com/nearai/ironclaw/pull/5149) | **上下文管理 — 渐进式工具披露**（flag-gated，默认关闭）：每次调用不再发送全部 ~91 个 tool schemas，解决 25.8k tokens × ~4 次/轮导致 NEAR AI 120s 超时的问题 | **高概率**——直接缓解长上下文/高延迟痛点，且已标记为 feat(reborn) |
| [#5313](https://github.com/nearai/ironclaw/pull/5313) | `ironclaw_storage_stress` 存储压力测试工具：支持 libSQL/Postgres，输出 latency/throughput/error buckets | 中——基础设施/可观测性 |
| [#5394](https://github.com/nearai/ironclaw/pull/5394) | capability policy e2e（回应 #5385） | 中——权限/安全治理 |
| [#5362](https://github.com/nearai/ironclaw/pull/5362) | 加固 Slack pairing 激活流程 | 中——渠道集成稳定性 |
| [#5373](https://github.com/nearai/ironclaw/pull/5373) | 通用 channel proof-code pairing | 中——扩展渠道支持 |

**研究视角**：[#5149](https://github.com/nearai/ironclaw/pull/5149) 是最贴近 **长上下文理解、推理机制、训练后对齐** 的条目。它通过减少每轮 tool schema 的重复披露来降低 token 消耗和延迟，本质上是在做 **上下文压缩 / 工具检索策略** 的工程优化，可能为后续研究提供真实生产环境的上下文成本数据。

---

## 7. 用户反馈摘要

从 Issues 中提炼的真实痛点：

1. **长工具链工作流不可靠**  
   - [#5415](https://github.com/nearai/ironclaw/issues/5415)：18–25 次工具调用的 Google Sheets 流程稳定出现 protocol violation。  
   - 痛点：复杂多步骤任务的 **执行一致性与错误恢复** 不足。

2. **工具/技能选择错误**  
   - [#5417](https://github.com/nearai/ironclaw/issues/5417)：Hacker News 搜索误激活 `tech-debt-tracker`。  
   - 痛点：agent 的 **意图-技能匹配** 存在偏差，可能导致用户困惑或错误执行路径。

3. **状态报告与认证流程矛盾**  
   - [#5416](https://github.com/nearai/ironclaw/issues/5416)：Google 连接状态被错误报告为已连接。  
   - 痛点：agent 对 **自身状态/权限状态的“幻觉”** 会误导用户。

4. **配置/权限状态未正确传递**  
   - [#5421](https://github.com/nearai/ironclaw/issues/5421)：chat 已可用但 web search 仍要求 API key。  
   - 痛点：不同能力之间的 **认证/激活状态隔离** 导致体验断裂。

5. **自动化管理体验粗糙**  
   - [#5419](https://github.com/nearai/ironclaw/issues/5419)：无法重命名 automation；[#5420](https://github.com/nearai/ironclaw/issues/5420)：routine 投递目标全局共享。  
   - 痛点：自动化/例程的 **可管理性与隔离性** 不足。

---

## 8. 待处理积压

| Issue/PR | 创建时间 | 最后更新 | 说明 | 提醒 |
|---|---|---|---|---|
| [#4108](https://github.com/nearai/ironclaw/issues/4108) | 2026-05-27 | 2026-06-29 | Nightly E2E 持续失败，已持续一个多月 | 需优先定位失败根因，避免回归基线恶化 |
| [#4776](https://github.com/nearai/ironclaw/issues/4776) | 2026-06-11 | 2026-06-29 | Reborn 全局“Always Allow”工具设置 | 已有关闭状态但需确认是否完整落地 |
| [#5149](https://github.com/nearai/ironclaw/pull/5149) | 2026-06-23 | 2026-06-29 | 上下文管理 / 渐进式工具披露（XL PR，待合并） | 建议维护者优先审阅，潜在性能收益大 |
| [#5313](https://github.com/nearai/ironclaw/pull/5313) | 2026-06-26 | 2026-06-29 | storage stress harness（XL PR，待合并） | 基础设施类，建议评估是否阻塞其他存储相关修复 |
| [#5362](https://github.com/nearai/ironclaw/pull/5362) | 2026-06-26 | 2026-06-29 | Slack pairing 加固（XL PR，待合并） | 与 #5421/#5416 等认证问题可能相关 |

---

## 研究侧总结

- **视觉语言能力**：今日数据中无直接相关 Issue/PR。
- **推理机制**：[#5415](https://github.com/nearai/ironclaw/issues/5415)（长工具链失败）、[#5417](https://github.com/nearai/ironclaw/issues/5417)（技能误激活）、[#5149](https://github.com/nearai/ironclaw/pull/5149)（上下文/工具披露优化）是主要信号。
- **训练方法论**：无直接相关更新；测试基础设施（#5392、#5402）和 live QA 体系（#5406、#5423）属于评估/对齐基础设施。
- **幻觉相关问题**：[#5416](https://github.com/nearai/ironclaw/issues/5416)（错误报告 Google 连接状态）可归类为状态幻觉；[#5417](https://github.com/nearai/ironclaw/issues/5417) 可视为工具选择幻觉。

建议后续持续追踪 [#5149](https://github.com/nearai/ironclaw/pull/5149) 的合并进展，以及 [#5415](https://github.com/nearai/ironclaw/issues/5415)、[#5417](https://github.com/nearai/ironclaw/issues/5417) 的根因修复。

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目日报 | 2026-06-30

## 1. 今日速览

LobsterAI 项目在 6 月 29 日呈现**高活跃度**，单日合并/关闭 PR 达 39 条，并发布了一个正式版本（2026.6.29）。更新重心集中在 **OpenClaw 运行时稳定性、定时任务（cron）会话一致性、以及 UI 导航修复**，属于典型的发布日密集收尾。Issues 侧以产品交互 Bug 和中文本地化问题为主，研究相关性较低；整体项目健康度良好，但存在少量长期未处理的 stale issue 需要维护者关注。

---

## 2. 版本发布

### [LobsterAI 2026.6.29](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.6.29)

**发布日期**：2026-06-29  
**主要变更**：

| 类别 | 内容 | 相关 PR |
|------|------|---------|
| **OpenClaw 稳定性** | 将插件审批路由经过权限系统处理 | [#2217](https://github.com/netease-youdao/LobsterAI/pull/2217) |
| **Cowork UI** | 清理导航栏预览（navigation rail previews） | [#2218](https://github.com/netease-youdao/LobsterAI/pull/2218) |
| **OpenClaw 稳定性** | 保留用户 turn 缓存稳定性（user-turn cache stability） | [#2219](https://github.com/netease-youdao/LobsterAI/pull/2219) |

**完整 release note 在提供数据中被截断**，但从关联 PR 可推断本次版本为 **v2026.6.1 的补丁回滚/稳定性修复版本**，核心目标是修复 OpenClaw 集成中的身份/记忆加载错误和缓存序列化回归。

**迁移/升级注意事项**：
- 若从 2026.6.1 升级，建议检查 OpenClaw agent 的 `SOUL.md` / `IDENTITY.md` / `USER.md` / `MEMORY.md` 是否正确加载（参见 [#2227](https://github.com/netease-youdao/LobsterAI/pull/2227)）。
- 定时任务历史记录和 cron 存储格式有变更，旧版本 cron 数据会在启动时自动迁移（参见 [#2189](https://github.com/netease-youdao/LobsterAI/pull/2189)）。

---

## 3. 项目进展

今日合并/关闭的核心 PR 按技术主题分组如下：

### 3.1 OpenClaw 运行时与身份一致性
- **[#2227](https://github.com/netease-youdao/LobsterAI/pull/2227) fix(openclaw): keep agent bootstrap workspace separate from task cwd**
  - 修复 v2026.6.1 中 `runCwd` 被错误当作 `workspaceDir` 的问题，避免 agent 从用户项目目录加载 bootstrap/profile/memory 文件，导致 **agent 身份（persona）和长期记忆被破坏**。
- **[#2219](https://github.com/netease-youdao/LobsterAI/pull/2219) fix(openclaw): preserve user turn cache stability**
  - 回移植 OpenClaw 用户 turn 序列化缓存稳定性修复，新增 patch validator 和回归测试。
- **[#2220](https://github.com/netease-youdao/LobsterAI/pull/2220) fix(openclaw): preserve cron run follow-up history**
  - 保留定时任务运行后的本地 follow-up 消息，避免同步 cron 历史时重复或破坏性替换。
- **[#2185](https://github.com/netease-youdao/LobsterAI/pull/2185) fix(openclaw): include cwd in reply options patch**
  - 补全 OpenClaw v2026.6.1 补丁中缺失的 `GetReplyOptions.cwd` 字段。

### 3.2 定时任务（Cron）会话与状态
- **[#2189](https://github.com/netease-youdao/LobsterAI/pull/2189) fix(openclaw): migrate legacy cron storage on startup**
- **[#2190](https://github.com/netease-youdao/LobsterAI/pull/2190) fix(openclaw): sync cron run sessions**
- **[#2191](https://github.com/netease-youdao/LobsterAI/pull/2191) fix(scheduled-task): clarify startup state**

### 3.3 插件生态
- **[#2182](https://github.com/netease-youdao/LobsterAI/pull/2182) fix(openclaw): support upgraded im plugin installs**
- **[#2186](https://github.com/netease-youdao/LobsterAI/pull/2186) fix(openclaw): compile NIM plugin runtime entry**
- **[#2198](https://github.com/netease-youdao/LobsterAI/pull/2198) fix(im): preinstall OpenClaw QQ and Discord plugins**

### 3.4 测试与文档
- **[#2187](https://github.com/netease-youdao/LobsterAI/pull/2187) test: align OpenClaw metadata expectations**
  - 更新 renderer model defaults 测试以适配 **reasoning-capable model metadata**。
- **[#2184](https://github.com/netease-youdao/LobsterAI/pull/2184) docs(agents): update repository guidance**

### 3.5 发布合并
- **[#2228](https://github.com/netease-youdao/LobsterAI/pull/2228) release: promote 2026.6.29 release to main**
  - 将 `release/2026.6.29` 合并入 `main`，标志着本版本正式发布。

**整体推进评估**：今日进展以**修复和稳定化**为主，OpenClaw 作为核心 agent 运行时经历了关键回归修复，项目在产品可用性上向前迈进一步，但未见新的模型能力或推理架构突破。

---

## 4. 社区热点

由于提供的数据中 Issues/PRs 的 👍 和评论数普遍较低（多数为 0-2 条），今日社区讨论热度整体偏冷。相对值得关注的条目：

| 条目 | 热度指标 | 诉求分析 |
|------|---------|---------|
| [#2120](https://github.com/netease-youdao/LobsterAI/issues/2120) 建议 | 评论: 2 | 用户希望提升 **Claw 任务连续性**（预输入后续任务）、延长单次任务运行时长、优化技能界面 UI 布局。反映高分辨率屏幕和长时间监控场景下的产品体验痛点。 |
| [#2121](https://github.com/netease-youdao/LobsterAI/issues/2121) 对一个现象的疑问（怀疑是bug） | 评论: 2 | 用户观察到 **重复输出文本**，担心 token 浪费。这与模型生成行为或前端渲染有关，属于潜在的幻觉/重复生成问题信号。 |
| [#2131](https://github.com/netease-youdao/LobsterAI/issues/2131) LobsterAI 支持 hermes agent有计划吗？ | 评论: 2 | 用户关注 **agent 框架兼容性**，希望接入 Hermes agent。 |

> 注：PR 侧评论数均显示为 `undefined`，无法判断真实讨论热度。

---

## 5. Bug 与稳定性

按严重程度排列：

| 严重程度 | 问题 | 状态 | 是否有 fix PR |
|---------|------|------|--------------|
| 🔴 **高** | OpenClaw agent 从用户项目目录错误加载 identity/memory 文件，破坏 agent persona 和长期记忆 | 已修复 | [#2227](https://github.com/netease-youdao/LobsterAI/pull/2227) |
| 🔴 **高** | OpenClaw 用户 turn 序列化缓存不稳定 | 已修复 | [#2219](https://github.com/netease-youdao/LobsterAI/pull/2219) |
| 🟡 **中** | 定时任务运行历史同步时可能丢失/重复 follow-up 消息 | 已修复 | [#2220](https://github.com/netease-youdao/LobsterAI/pull/2220) |
| 🟡 **中** | 执行结果窗口滚动到顶端假死 | 开放 | [#2079](https://github.com/netease-youdao/LobsterAI/issues/2079) |
| 🟡 **中** | 重复输出文本 suspected token waste | 开放 | [#2121](https://github.com/netease-youdao/LobsterAI/issues/2121) |
| 🟢 **低** | 语言选择英文时，中文选项显示英文 | 开放（stale） | [#1389](https://github.com/netease-youdao/LobsterAI/issues/1389) |
| 🟢 **低** | 会话分享长图内容不全 | 开放（stale） | [#1386](https://github.com/netease-youdao/LobsterAI/issues/1386) |
| 🟢 **低** | 邮箱配置测试连通性无响应 | 开放（stale） | [#1388](https://github.com/netease-youdao/LobsterAI/issues/1388) |
| 🟢 **低** | 定时任务无法更新（偶现） | 开放（stale） | [#1390](https://github.com/netease-youdao/LobsterAI/issues/1390) |

---

## 6. 功能请求与路线图信号

| 功能请求 | 来源 | 纳入可能性评估 |
|---------|------|---------------|
| **Hermes agent 支持** | [#2131](https://github.com/netease-youdao/LobsterAI/issues/2131) | 中。OpenClaw 是 LobsterAI 的核心 agent 运行时，接入第三方 agent 框架需架构评估，但社区兼容性诉求明确。 |
| **任务预输入/队列化** | [#2120](https://github.com/netease-youdao/LobsterAI/issues/2120) | 中高。属于 Cowork/Claw 工作流连续性改进，与现有任务调度能力方向一致。 |
| **延长单次任务运行时长** | [#2120](https://github.com/netease-youdao/LobsterAI/issues/2120) | 高。监控/数据获取脚本场景的真实痛点，可能通过配置或超时策略调整实现。 |
| **技能界面 UI 三列布局（高分辨率屏）** | [#2120](https://github.com/netease-youdao/LobsterAI/issues/2120) | 中。纯前端体验优化，优先级取决于产品规划。 |

---

## 7. 用户反馈摘要

从今日 Issues 中提炼的真实用户信号：

- **长时间运行场景**：用户用 Claw 监控数据获取脚本时遇到 `terminated`，说明当前任务超时或运行时长限制对开发工作流造成中断（[#2120](https://github.com/netease-youdao/LobsterAI/issues/2120)）。
- **生成效率担忧**：用户注意到重复输出文本，担心 token 成本，反映对模型输出经济性的敏感（[#2121](https://github.com/netease-youdao/LobsterAI/issues/2121)）。
- **任务连续性**：用户希望在当前任务运行时预输入下一个任务，提升项目级自动化效率（[#2120](https://github.com/netease-youdao/LobsterAI/issues/2120)）。
- **UI 适配**：2560×1600 全屏下双列技能界面展示不友好，高分辨率设备适配不足（[#2120](https://github.com/netease-youdao/LobsterAI/issues/2120)）。
- **稳定性**：执行结果窗口滚动假死问题自 5 月底持续存在，影响基础交互体验（[#2079](https://github.com/netease-youdao/LobsterAI/issues/2079)）。

---

## 8. 待处理积压

以下 Issue 长期处于开放状态（stale），建议维护者优先审阅：

| Issue | 创建时间 | 最后更新 | 问题 | 链接 |
|-------|---------|---------|------|------|
| 语言选择英文时，中文选项显示英文 | 2026-04-03 | 2026-06-29 | 本地化一致性 | [#1389](https://github.com/netease-youdao/LobsterAI/issues/1389) |
| 会话分享长图内容不全 | 2026-04-03 | 2026-06-29 | 长上下文内容导出 | [#1386](https://github.com/netease-youdao/LobsterAI/issues/1386) |
| 邮箱配置测试连通性无响应 | 2026-04-03 | 2026-06-29 | 外部集成配置 | [#1388](https://github.com/netease-youdao/LobsterAI/issues/1388) |
| 定时任务无法更新（偶现） | 2026-04-03 | 2026-06-29 | 定时任务稳定性 | [#1390](https://github.com/netease-youdao/LobsterAI/issues/1390) |
| 执行结果窗口滚动到顶端假死 | 2026-05-30 | 2026-06-29 | 前端渲染/性能 | [#2079](https://github.com/netease-youdao/LobsterAI/issues/2079) |

---

## 研究相关性总结

从给定数据中，与研究主题直接相关的内容有限：
- **推理机制**：[#2187](https://github.com/netease-youdao/LobsterAI/pull/2187) 提到更新测试以适配 reasoning-capable model metadata，但无具体模型或方法披露。
- **幻觉/可靠性**：[#2121](https://github.com/netease-youdao/LobsterAI/issues/2121) 的重复输出问题可作为生成可靠性信号；OpenClaw 的缓存/记忆修复属于系统级可靠性改进。
- **长上下文理解**：[#1386](https://github.com/netease-youdao/LobsterAI/issues/1386) 会话分享长图内容不全，间接涉及长内容渲染，但与模型长上下文能力无关。
- **训练/后训练对齐**：今日数据中未见相关 PR 或 Issue。

如需进一步聚焦研究动态，建议追踪 LobsterAI 的模型元数据更新、OpenClaw agent 推理链路变更以及评测/对齐相关 PR。

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

# CoPaw 项目日报 · 2026-06-30

## 1. 今日速览

过去 24 小时 CoPaw（QwenPaw）社区保持高度活跃：Issues 更新 29 条（20 开/活跃，9 关闭），PR 更新 50 条（31 待合并，19 已合并/关闭），无新版本发布。整体活动集中在**上下文管理、工具调用治理、记忆系统与多模态降级**等核心推理链路，显示出项目正从功能扩展期向**可靠性加固与 AgentScope 2.0 架构迁移**深化。视觉语言相关讨论显著增加，包括纯文本模型的 vision fallback、MiniMax-M3 视觉审核误判、以及 Qwen-Image 工具安装问题。

---

## 2. 版本发布

无新版本发布。

> 注：v2.0.0-beta.1 安装验证任务仍在进行中（Issue #5571），但尚未标记为正式发布。

---

## 3. 项目进展

| PR | 状态 | 核心贡献 | 研究/技术意义 |
|---|---|---|---|
| [#5515](https://github.com/agentscope-ai/QwenPaw/pull/5515) | CLOSED | 升级 `@agentscope-ai/chat` 至 beta 并启用新聊天 UI 能力 | 前端交互层与 AgentScope 2.0 对齐 |
| [#5614](https://github.com/agentscope-ai/QwenPaw/pull/5614) | CLOSED | 更新上下文管理文档，以 scroll 策略替代 backpack 类比，移除 light context manager 旧引用 | **长上下文理解**：明确 scroll-based 上下文架构 |
| [#5601](https://github.com/agentscope-ai/QwenPaw/pull/5601) | CLOSED | 修复 Runtime 重构后第三方 IM 通道无法接收 tool-guard 审批通知的问题 | 工具治理与可靠性 |

**整体推进判断**：今日合并内容以文档对齐、UI 升级和通道治理为主，核心推理与上下文机制的多项修复仍处于待合并状态（见第 5、6 节）。

---

## 4. 社区热点

| 议题 | 链接 | 热度 | 核心诉求 |
|---|---|---|---|
| DeepSeek 前缀缓存命中率偏低（~95%） | [#3891](https://github.com/agentscope-ai/QwenPaw/issues/3891) | 5 评论，1 👍 | 降低 API 成本，优化长上下文/多轮场景下的缓存策略 |
| 工具调用结果卡片计数错误 | [#5624](https://github.com/agentscope-ai/QwenPaw/issues/5624) | 3 评论 | 前端状态与工具执行结果不一致，影响可解释性 |
| DeepSeek V4 thinking 模式 400 错误 | [#5573](https://github.com/agentscope-ai/QwenPaw/issues/5573) | 3 评论 | **推理机制**：OpenAI 兼容端点上 reasoning_content 与工具 schema 的兼容性 |
| MiniMax-M3 图片安全审核误判 | [#5505](https://github.com/agentscope-ai/QwenPaw/issues/5505) | 3 评论 | **视觉语言/幻觉**：安全审核错误被缓存为 `rejects_media=True`，导致后续视觉请求被剥离 |
| 工具结果大小硬上限（上下文爆炸防御） | [#5342](https://github.com/agentscope-ai/QwenPaw/issues/5342) | 3 评论 | **长上下文/可靠性**：LLM 调用失败时 hook 被跳过导致上下文无限膨胀 |

**背后诉求分析**：社区正从"功能可用"转向"成本可控、输出可信、异常可恢复"。缓存命中率、工具结果截断、视觉输入被错误剥离等问题，均指向**生产环境可靠性**。

---

## 5. Bug 与稳定性

按严重程度排列：

| 问题 | 严重度 | 状态 | Fix PR | 链接 |
|---|---|---|---|---|
| 工具结果大小无执行层硬上限，LLM 失败时导致上下文爆炸 | 🔴 高 | OPEN | [#5510](https://github.com/agentscope-ai/QwenPaw/pull/5510) 待合并 | [#5342](https://github.com/agentscope-ai/QwenPaw/issues/5342) |
| MiniMax-M3 视觉审核误判被缓存，后续图片请求被剥离（模型"幻觉"回答） | 🔴 高 | CLOSED | 未明确关联 | [#5505](https://github.com/agentscope-ai/QwenPaw/issues/5505) |
| DeepSeek V4 thinking 模式流式 reasoning_content 缺失、工具 schema null 类型未清洗 | 🟠 中 | OPEN | 无 | [#5573](https://github.com/agentscope-ai/QwenPaw/issues/5573) |
| 双 subagent 导致主 agent 无限快速轮询 | 🟠 中 | OPEN | 无 | [#4873](https://github.com/agentscope-ai/QwenPaw/issues/4873) |
| 工具调用结果卡片计数始终显示 1 | 🟡 中 | OPEN（重复报告） | [#5628](https://github.com/agentscope-ai/QwenPaw/pull/5628) 待合并 | [#5624](https://github.com/agentscope-ai/QwenPaw/issues/5624) / [#5626](https://github.com/agentscope-ai/QwenPaw/issues/5626) |
| Tool Guard 设为 OFF 仍触发审批 | 🟡 中 | OPEN | [#5623](https://github.com/agentscope-ai/QwenPaw/pull/5623) 待合并 | PR 自述 |
| Qwen-Image Tool 安装错误 | 🟡 中 | OPEN | 无 | [#5587](https://github.com/agentscope-ai/QwenPaw/issues/5587) |
| 自定义 ascend-vllm 模型无法连接 | 🟡 中 | OPEN | 无 | [#5584](https://github.com/agentscope-ai/QwenPaw/issues/5584) |
| functionDeclaration schema 中 `type: null` 导致部分中转模型无法处理 | 🟢 已修复 | CLOSED | [#5543](https://github.com/agentscope-ai/QwenPaw/issues/5543) 自身 | [#5543](https://github.com/agentscope-ai/QwenPaw/issues/5543) |

---

## 6. 功能请求与路线图信号

| 功能请求 | 链接 | 与研究主题关联 | 纳入下一版本可能性 |
|---|---|---|---|
| 纯文本模型支持图片自动转文字描述（vision fallback） | [#5615](https://github.com/agentscope-ai/QwenPaw/issues/5615) | **视觉语言能力、多模态推理、幻觉缓解** | 高：需求明确，已有 qclaw/codex 参考实现 |
| 记忆搜索支持专用 Reranker 两阶段检索 | [#5588](https://github.com/agentscope-ai/QwenPaw/issues/5588) | **长上下文理解、检索增强生成** | 中：技术方案清晰，依赖 reME service 启用 |
| 模型自动降级（配额耗尽/失败/超时 → 备选模型） | [#5572](https://github.com/agentscope-ai/QwenPaw/issues/5572) | **训练/推理方法论、可靠性** | 高：与 AgentScope 2.0 动态模型切换方向一致 |
| 对话记录断点保存机制 | [#5579](https://github.com/agentscope-ai/QwenPaw/issues/5579) | **长上下文、可靠性** | 中：需求强烈但实现复杂 |
| 工具结果执行层硬上限 | [#5342](https://github.com/agentscope-ai/QwenPaw/issues/5342) / [#5510](https://github.com/agentscope-ai/QwenPaw/pull/5510) | **上下文管理、可靠性** | 高：PR 已提交 |
| 暴露 native/scroll 上下文策略选择器 | [#5629](https://github.com/agentscope-ai/QwenPaw/pull/5629) | **长上下文理解** | 高：PR 已提交 |
| 自定义模型协议/端点 | [#5609](https://github.com/agentscope-ai/QwenPaw/issues/5609) | **模型接入方法论** | 中 |

---

## 7. 用户反馈摘要

**真实痛点：**

- **成本敏感**：DeepSeek 前缀缓存命中率 95% 仍被认为"偏低"，用户希望进一步压缩 5% 的缓存未命中成本（[#3891](https://github.com/agentscope-ai/QwenPaw/issues/3891)）。
- **视觉输入可靠性**：MiniMax-M3 一次审核失败即被永久标记为拒绝媒体，导致模型在"看不见图"的情况下继续回答，产生**事实性幻觉/输出不可信**（[#5505](https://github.com/agentscope-ai/QwenPaw/issues/5505)）。
- **上下文失控**：工具返回大结果时缺乏执行层硬上限，LLM 调用失败后上下文无限累积，引发级联故障（[#5342](https://github.com/agentscope-ai/QwenPaw/issues/5342)）。
- **模型生态碎片化**：自定义 vLLM/ascend-vllm、非标准 OpenAI 兼容端点、第三方中转站的适配问题频发（[#5584](https://github.com/agentscope-ai/QwenPaw/issues/5584)，[#5573](https://github.com/agentscope-ai/QwenPaw/issues/5573)，[#5609](https://github.com/agentscope-ai/QwenPaw/issues/5609)）。
- **长任务脆弱性**：自动化任务异常终止无日志、对话记录在宿主机重启/服务崩溃后丢失（[#5616](https://github.com/agentscope-ai/QwenPaw/issues/5616)，[#5579](https://github.com/agentscope-ai/QwenPaw/issues/5579)）。

**满意/中性：**

- 社区对 AgentScope 2.0 方向持期待态度，但关心动态模型切换与迁移时间表（[#5527](https://github.com/agentscope-ai/QwenPaw/issues/5527)）。

---

## 8. 待处理积压

| 议题/PR | 创建时间 | 状态 | 风险 | 链接 |
|---|---|---|---|---|
| 工具结果执行层硬上限 | 2026-06-20 | OPEN，PR #5510 待合并 | 级联故障、上下文爆炸 | [#5342](https://github.com/agentscope-ai/QwenPaw/issues/5342) |
| 双 subagent 无限轮询 | 2026-06-01 | OPEN | 资源耗尽、IM 侧无法中断 | [#4873](https://github.com/agentscope-ai/QwenPaw/issues/4873) |
| DeepSeek 前缀缓存优化 | 2026-04-27 | OPEN | 成本控制、用户体验 | [#3891](https://github.com/agentscope-ai/QwenPaw/issues/3891) |
| 模型自动降级 | 2026-06-26 | OPEN | 长任务可靠性 | [#5572](https://github.com/agentscope-ai/QwenPaw/issues/5572) |
| 对话记录断点保存 | 2026-06-27 | OPEN | 数据丢失 | [#5579](https://github.com/agentscope-ai/QwenPaw/issues/5579) |

**维护者关注建议**：优先合并 [#5510](https://github.com/agentscope-ai/QwenPaw/pull/5510)（上下文硬上限）与 [#5623](https://github.com/agentscope-ai/QwenPaw/pull/5623)（Tool Guard OFF 模式失效），二者直接影响生产稳定性；同时需对 [#5505](https://github.com/agentscope-ai/QwenPaw/issues/5505) 的视觉审核缓存误判给出根因修复，避免多模态场景下的持续性幻觉。

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目日报 — 2026-06-30

## 1. 今日速览

过去 24 小时 ZeroClaw 社区保持高度活跃：Issues 与 PR 各更新 50 条，无新版本发布。研究相关的核心进展集中在 **provider 消息序列化合规性**（OpenAI/Anthropic/Groq 工具调用格式修复）、**MCP 工具可用性与系统提示一致性**、以及 **SOP/技能运行时架构**演进。视觉语言相关 Issue #6841 已关闭，但 provider 层对多模态负载的处理仍是未完全收敛的风险点。整体项目健康度良好，但 P1 级 provider/runtime 缺陷数量偏高，需关注修复进度。

---

## 2. 版本发布

无。

---

## 3. 项目进展

### 已关闭/合并的重要 PR

| PR | 说明 | 研究意义 |
|---|---|---|
| [#8436](https://github.com/zeroclaw-labs/zeroclaw/pull/8436) | 文档修正：`max_history_messages` 硬上限与 whole-turn trim 并存 | 长上下文理解：明确历史截断机制，对上下文窗口管理有参考价值 |
| [#8441](https://github.com/zeroclaw-labs/zeroclaw/pull/8441) | Compatible provider 工具结果消息补充 `name` 字段（Groq 兼容） | 训练/推理机制：工具调用序列化合规，减少 provider 侧 400 错误 |

### 已关闭的重要 Issue

| Issue | 说明 | 研究意义 |
|---|---|---|
| [#2128](https://github.com/zeroclaw-labs/zeroclaw/issues/2128) | Cron/heartbeat 不再发送 `NO_REPLY` 字面文本 | 代理可靠性：减少无意义输出，改善人机交互边界 |
| [#8379](https://github.com/zeroclaw-labs/zeroclaw/issues/8379) | WhatsApp Web 被动群聊上下文（opt-in） | 长上下文/多轮：群聊消息作为被动上下文而非触发 turn |
| [#8327](https://github.com/zeroclaw-labs/zeroclaw/issues/8327) | `[IMAGE:data:...]` 图像标记在工具结果中被当作纯文本发送，导致 token 膨胀 | **视觉语言/多模态推理**：图像负载序列化问题，已关闭 |
| [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) | `vision_provider` 被静默忽略，入站图片被路由到 fallback provider | **视觉语言能力**：多模态路由配置失效，已关闭 |

---

## 4. 社区热点

### 评论最多的 Issues

| Issue | 评论 | 核心诉求 |
|---|---|---|
| [#5600](https://github.com/zeroclaw-labs/zeroclaw/issues/5600) | 11 | **Kimi-code provider 流式调用工具时 400 错误**：`thinking` 启用但 `reasoning_content` 缺失。直接关联**推理机制/思维链协议兼容性**。 |
| [#8054](https://github.com/zeroclaw-labs/zeroclaw/issues/8054) | 9 | **系统提示中工具可用性与实际请求不一致**：跨 channels/gateway/WebSocket/多模态/`/think` 入口的系统性修复。核心关注**幻觉/能力错配**——模型被错误告知"无工具可用"。 |
| [#6909](https://github.com/zeroclaw-labs/zeroclaw/issues/6909) | 6 | **Computer-use 桌面交互 RFC**：截图+鼠标/键盘控制，对标 OpenAI Codex/openclaw。属于**视觉语言能力/ embodied agent** 扩展。 |
| [#7800](https://github.com/zeroclaw-labs/zeroclaw/issues/7800) | 5 | ZeroCode TUI 帮助/键位在 macOS 上误导或无法到达 | 产品交互，非研究重点 |
| [#7218](https://github.com/zeroclaw-labs/zeroclaw/issues/7218) | 5 | A2A agent 发现协议（`.well-known/agent-card.json`） | 多智能体架构，与研究弱相关 |

### 热点分析

- **#5600** 和 **#7756** 共同揭示：reasoning 模型（OpenAI Responses/Anthropic/Kimi）与工具调用/MCP 的协议适配是当下最脆弱的环节，直接影响代理的**推理-行动一致性**。
- **#8054** 是 #7756 的后续，说明修复仅覆盖 direct runtime path，其他入口仍存在**系统提示-工具集不一致**，这是典型的**能力声明幻觉**风险源。

---

## 5. Bug 与稳定性

按严重程度排列：

### P1 / S1（工作流阻塞）

| Issue/PR | 描述 | 状态 | 研究关联 |
|---|---|---|---|
| [#5600](https://github.com/zeroclaw-labs/zeroclaw/issues/5600) | Kimi-code provider 流式 chat call tools 报 400：`reasoning_content` 缺失 | OPEN, accepted, P1 | 推理机制 |
| [#8054](https://github.com/zeroclaw-labs/zeroclaw/issues/8054) | 系统提示工具可用性与每轮有效工具不匹配（channels/gateway/WebSocket/多模态/`/think`） | OPEN, blocked, P1 | 幻觉/工具可用性 |
| [#7756](https://github.com/zeroclaw-labs/zeroclaw/issues/7756) | OpenAI Responses/Anthropic turns 上 native/MCP 工具不可用 | OPEN, P1 | 推理+工具调用 |
| [#8505](https://github.com/zeroclaw-labs/zeroclaw/issues/8505) | Telegram channel 无法配置 | OPEN | 非研究重点 |
| [#8334](https://github.com/zeroclaw-labs/zeroclaw/issues/8334) | `skills install/list/remove` 目标 data_dir 与多 agent runtime 不兼容 | OPEN, in-progress, P1 | 技能/训练方法论 |

### P2 / 中等严重

| Issue/PR | 描述 | 状态 | 研究关联 |
|---|---|---|---|
| [#7800](https://github.com/zeroclaw-labs/zeroclaw/issues/7800) | ZeroCode 帮助/键位误导或不可达 | OPEN | 非研究重点 |
| [#8410](https://github.com/zeroclaw-labs/zeroclaw/issues/8410) | Channel tasks 需要一等"故意不回复"结果 | OPEN, P2 | 代理行为边界/幻觉 |
| [#8327](https://github.com/zeroclaw-labs/zeroclaw/issues/8327) | 工具结果中 `[IMAGE:data:...]` 被当纯文本发送，token 膨胀 | CLOSED | 视觉语言/多模态 |
| [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) | `vision_provider` 被静默忽略 | CLOSED | 视觉语言 |
| [#8312](https://github.com/zeroclaw-labs/zeroclaw/issues/8312) | `fill-translations` 泄漏修复后残留 stale entries | OPEN, P1 | 数据完整性 |

### 已提交 fix PR 的 Bug

| PR | 对应 Issue | 说明 |
|---|---|---|
| [#8510](https://github.com/zeroclaw-labs/zeroclaw/pull/8510) | — | OpenAI-compatible 请求中 assistant tool-call message 的 `content` 从 `""` 改为省略/null |
| [#8508](https://github.com/zeroclaw-labs/zeroclaw/pull/8508) | — | MCP resources-as-context / pinning / named-prompt 渲染 |
| [#8496](https://github.com/zeroclaw-labs/zeroclaw/pull/8496) | #8054 | 集中化 deferred-MCP 访问策略为单一事实来源 |
| [#8441](https://github.com/zeroclaw-labs/zeroclaw/pull/8441) | — | Compatible provider 工具结果补充 `name` 字段 |
| [#7909](https://github.com/zeroclaw-labs/zeroclaw/pull/7909) | #7896 | 同上（Groq 工具调用需 `name`） |
| [#8148](https://github.com/zeroclaw-labs/zeroclaw/pull/8148) | — | Anthropic streaming request builder 中 `expect` 改为错误传播 |

---

## 6. 功能请求与路线图信号

| Issue/PR | 内容 | 纳入下一版本可能性 | 研究关联 |
|---|---|---|---|
| [#6909](https://github.com/zeroclaw-labs/zeroclaw/issues/6909) | Computer-use 桌面屏幕交互与输入控制 RFC | 高（已 accepted，对标竞品） | **视觉语言/embodied agent** |
| [#7218](https://github.com/zeroclaw-labs/zeroclaw/issues/7218) | A2A agent 发现协议 | 中 | 多智能体 |
| [#8170](https://github.com/zeroclaw-labs/zeroclaw/issues/8170) | 应用内升级与监督重启 | 中 | 非研究重点 |
| [#6140](https://github.com/zeroclaw-labs/zeroclaw/issues/6140) | 混合技能 + WASM 工具插件 | 高（v0.8.3 WASM plugin program 一部分） | **训练方法论/工具扩展** |
| [#7497](https://github.com/zeroclaw-labs/zeroclaw/issues/7497) | OCI 兼容容器注册表作为插件存储与发现机制 | 中 | 供应链/安全 |
| [#8135](https://github.com/zeroclaw-labs/zeroclaw/issues/8135) | Wasm-first plugin runtime，默认启用，能力强制，签名分发 | 高 | 安全/运行时 |
| [#8462](https://github.com/zeroclaw-labs/zeroclaw/issues/8462) | OTel LLM/Tool 内容运行时策略 | 中 | 可观测性/隐私 |
| [#7879](https://github.com/zeroclaw-labs/zeroclaw/issues/7879) | 有界 SKILL.md 反射用于技能创建 | 高（已 in-progress） | **训练方法论/技能学习** |
| [#8509](https://github.com/zeroclaw-labs/zeroclaw/pull/8509) | SOP 程序记忆 workshop | 高 | **长上下文/程序记忆** |
| [#8506](https://github.com/zeroclaw-labs/zeroclaw/pull/8506) | SOP 消费 CAS run claims | 高 | 执行一致性 |
| [#8461](https://github.com/zeroclaw-labs/zeroclaw/pull/8461) | 文件系统 SOP 事件源 | 高 | 事件驱动代理 |

**研究判断**：v0.8.3 的核心方向是 **WASM 插件运行时、SOP 程序记忆、provider 消息序列化合规**。其中 #6909 computer-use 是最具研究信号的视觉语言能力扩展。

---

## 7. 用户反馈摘要

从 Issues 中提炼的真实痛点：

- **Reasoning 模型工具调用不可靠**：Kimi/OpenAI/Anthropic 的 reasoning 路径与工具/MCP 适配存在多处断裂，用户遇到 400 错误、工具未传入、系统提示不一致等问题。
- **视觉语言配置"静默失败"**：`vision_provider` 被忽略、图像标记被当纯文本发送，说明多模态链路缺乏清晰的错误传播和验证。
- **Agent 行为边界模糊**：channel tasks 在"无需回复"时仍发送可见响应，反映**条件性沉默/无回复**这一代理可靠性需求尚未被一等支持。
- **技能与多 agent 运行时脱节**：`skills install` 目标路径与多 agent runtime 加载路径不一致，说明技能分发机制仍需统一。
- **长上下文/历史截断机制不透明**：文档与实际行为存在偏差（#8436），用户难以预测上下文窗口管理行为。

---

## 8. 待处理积压

长期未响应或需维护者重点关注的研究相关 Issue：

| Issue | 创建时间 | 最后更新 | 提醒原因 |
|---|---|---|---|
| [#5600](https://github.com/zeroclaw-labs/zeroclaw/issues/5600) | 2026-04-10 | 2026-06-29 | 已持续近 3 个月，P1，reasoning 模型流式工具调用阻塞 |
| [#7756](https://github.com/zeroclaw-labs/zeroclaw/issues/7756) | 2026-06-16 | 2026-06-29 | P1，OpenAI/Anthropic 工具可用性，已有部分修复但需跨入口统一 |
| [#8054](https://github.com/zeroclaw-labs/zeroclaw/issues/8054) | 2026-06-20 | 2026-06-29 | 状态 blocked，需维护者决策跨入口修复策略 |
| [#6909](https://github.com/zeroclaw-labs/zeroclaw/issues/6909) | 2026-05-25 | 2026-06-29 | Computer-use RFC，视觉语言/embodied agent 关键方向 |
| [#6140](https://github.com/zeroclaw-labs/zeroclaw/issues/6140) | 2026-04-26 | 2026-06-29 | 混合技能 + WASM 工具，v0.8.3 插件架构核心 |
| [#6074](https://github.com/zeroclaw-labs/zeroclaw/issues/6074) | 2026-04-24 | 2026-06-29 | 153 个 commit 被 bulk revert 后仍未恢复，技术债务风险 |

---

**总结**：今日 ZeroClaw 在研究相关议题上呈现"高活跃、高修复压力"特征。核心矛盾仍是 **reasoning 模型与工具调用生态的协议适配**，以及 **视觉语言/多模态负载在 provider 层的正确序列化**。SOP 程序记忆与 WASM 插件架构是 v0.8.3 的明确前进方向，值得持续跟踪。

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*