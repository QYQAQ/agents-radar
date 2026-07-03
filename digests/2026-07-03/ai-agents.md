# OpenClaw 生态日报 2026-07-03

> Issues: 191 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-03 00:29 UTC

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

# 个人 AI 助手 / 自主智能体开源生态横向对比（2026-07-03）

---

## 1. 生态全景

今日生态呈现**“头部项目高活跃、底层可靠性成焦点”**的态势。NanoBot、Hermes Agent、CoPaw 三个项目合计贡献了近 300 条 Issues/PRs 更新，围绕 tool-call 解析、长上下文压缩、视觉输入处理、模型 fallback 等 AI 可靠性工程展开。与此同时，PicoClaw、NanoClaw、Moltis 等项目以协议兼容、网关维护、系统提示调优为主，研究信号较弱。OpenClaw、IronClaw、LobsterAI、ZeroClaw 因摘要生成失败未能纳入评估；NullClaw、TinyClaw、ZeptoClaw 则处于静默状态。

---

## 2. 各项目活跃度对比

| 项目 | Issues 数 | PR 数 | 版本 / Release | 健康度评估 |
|---|---|---|---|---|
| **OpenClaw** | 数据不可用 | 数据不可用 | 未知 | 核心参照项目，摘要生成失败 |
| **NanoBot** | 97（94 活跃/新开，3 关闭） | 62（34 待合并，28 已合并/关闭） | 无 | **高活跃**，工具调用与记忆可靠性集中收尾 |
| **Hermes Agent** | 50（7 关闭） | 50（7 关闭/合并） | 无 | **高活跃**，平台、多模态与安全并进 |
| **PicoClaw** | 2（新/活跃） | 25（14 已合并/关闭） | `v0.3.1-nightly.20260702.2cf030d2` | 中低活跃，维护与网关适配为主 |
| **NanoClaw** | 4（全部 open） | 14（12 open，2 closed） | 无 | 中等活跃，产品与指令调优并行 |
| **NullClaw** | 0 | 0 | 无 | 休眠 |
| **IronClaw** | 数据不可用 | 数据不可用 | 未知 | 摘要生成失败 |
| **LobsterAI** | 数据不可用 | 数据不可用 | 未知 | 摘要生成失败 |
| **TinyClaw** | 0 | 0 | 无 | 休眠 |
| **Moltis** | 0 | 3（2 open，1 closed） | 无 | 低活跃，协议兼容维护 |
| **CoPaw / QwenPaw** | 24（16 活跃/新开，8 关闭） | 50（23 待合并，27 已合并/关闭） | `v2.0.0-beta.2` | **高活跃**，v2 beta 快速迭代但稳定性待打磨 |
| **ZeptoClaw** | 0 | 0 | 无 | 休眠 |
| **ZeroClaw** | 数据不可用 | 数据不可用 | 未知 | 摘要生成失败 |

---

## 3. 研究定位分析

| 项目 | 多模态推理 | 长上下文理解 | Post-training 对齐 / AI 可靠性 |
|---|---|---|---|
| **NanoBot** | 今日无直接信号 | **核心方向**：显式 retention planning、Dream 记忆压缩边界、记忆审计与 git diff 对齐 | **核心方向**：文本格式 tool call 解析、无效 tool result 隔离、MCP 错误承载、reasoning effort 自动升级、LLM 并行工具调用 |
| **Hermes Agent** | **核心方向**：`image_generate` 参考图输入、`computer_use` 视觉捕获 | 可配置记忆后端、LiteLLM 上下文长度检测 | LLM 将 `MEDIA:` 误写为 `FILE:` 的解析容错、提示注入假阳性、浏览器私有页面边界、网关会话隔离 |
| **PicoClaw** | 无 | 无 | **核心方向**：OpenAI 兼容流式响应中 Seed XML tool-call 残留提取与抑制（PR #3165） |
| **NanoClaw** | 无 | 全局记忆文件持久化、失效 “Global Memory” 指令清理 | 核心指令禁止最终消息重复 `send_message`、Codex provider 角色注入 |
| **CoPaw** | **核心方向**：视觉输入被误标为 `rejects_media` 的修复 | **核心方向**：`scroll` 上下文压缩避免折叠 active turn、摘要长度校验、记忆检索 reranker | LLM fallback、goal mode gate 控制流、消费者超时、技能元数据系统提示 |
| **Moltis** | 无 | 无 | 无（纯协议/provider 接入） |

**技术路线差异**：
- **NanoBot** 走“deep agent 可靠性”路线：聚焦 tool-use 格式、记忆压缩与推理调度，偏工程化治理。
- **Hermes Agent** 走“平台级多模态 + 安全隔离”路线：视觉工具、浏览器边界、网关会话是其差异化。
- **CoPaw** 走“模型驱动的上下文与记忆”路线：上下文压缩、fallback、reranker 更贴近大模型应用层研究。
- **PicoClaw / NanoClaw** 属于轻量级/网关型实现，研究集中在输出格式与系统提示稳定性。

---

## 4. 共同关注的技术方向

| 方向 | 涉及项目 | 具体诉求 |
|---|---|---|


---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 研究动态日报 · 2026-07-03

**数据来源**：GitHub `HKUDS/nanobot` · 统计窗口：2026-07-02 至 2026-07-03（UTC）

---

## 1. 今日速览

NanoBot 在过去 24 小时内保持极高开发活跃度：Issues 更新 **97 条**（新开/活跃 94，已关闭 3），Pull Requests 更新 **62 条**（待合并 34，已合并/关闭 28），无新版本发布。从多模态推理、长上下文理解、post-training 对齐与 AI 可靠性视角审视，今日焦点集中在 **agent 工具调用可靠性**（文本格式 tool call 解析、无效 tool result 隔离、MCP 错误承载）、**长上下文与记忆管理**（显式 retention planning、Dream 记忆压缩边界、记忆审计与 git diff 对齐）以及**推理机制**（reasoning effort 自动升级、LLM 并行工具调用调度）。值得注意的是，本批次数据中未出现与视觉-语言/多模态能力直接相关的 issue 或 PR。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

今日唯一被关闭/合并的重要批次修复是 **PR #4648**（`Fix validated issue batch`），由 `hamb1y` 提交，集中修复了 13 个已验证 issue：[#4078](https://github.com/HKUDS/nanobot/issues/4078)、[#4076](https://github.com/HKUDS/nanobot/issues/4076)、[#4075](https://github.com/HKUDS/nanobot/issues/4075)、[#4072](https://github.com/HKUDS/nanobot/issues/4072)、[#4068](https://github.com/HKUDS/nanobot/issues/4068)、[#4064](https://github.com/HKUDS/nanobot/issues/4064)、[#4061](https://github.com/HKUDS/nanobot/issues/4061)、[#4058](https://github.com/HKUDS/nanobot/issues/4058)、[#4055](https://github.com/HKUDS/nanobot/issues/4055)、[#4604](https://github.com/HKUDS/nanobot/issues/4604)、[#4378](https://github.com/HKUDS/nanobot/issues/4378)、[#4544](https://github.com/HKUDS/nanobot/issues/4544)、[#4136](https://github.com/HKUDS/nanobot/issues/4136)。

该批次覆盖 SSRF 安全、消息 outbound 授权、Dream 记忆管理、工具调用解析、Matrix 流隔离等关键稳定性维度，是近期在主分支上降低 agent 幻觉传播风险与工具执行边界错误的一次集中收尾。

---

## 4. 社区热点

| 热点 Issue/PR | 研究相关性 | 背后诉求 |
|---|---|---|
| **[#4657](https://github.com/HKUDS/nanobot/issues/4657) Nanobot Radar Finding** | 项目健康度/可靠性 | 维护者视角的 13 个已验证 bug/安全/重构债跟踪，无 PR 覆盖，是优先级仪表盘。 |
| **[#4419](https://github.com/HKUDS/nanobot/issues/4419) Automatic reasoning effort escalation** | 推理机制 | 用户希望根据 prompt 复杂度或失败信号自动切换 `reasoningEffort` 档位，以降低推理成本或提升困难任务成功率。 |
| **[#2937](https://github.com/HKUDS/nanobot/issues/2937) Embedding-based context compression / semantic retrieval pipeline** | 长上下文理解 | 对现有 token-budget

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 研究动态日报（2026-07-03）

> **说明**：本报告已按“多模态推理、长上下文理解、post-training 对齐、AI 可靠性”四个研究维度过滤，剔除了定价、商业、纯 UI 皮肤等一般性产品更新。

---

## 1. 今日速览

- **活跃度**：过去 24 小时共有 **100 条仓库更新**（Issues 50 条、PRs 50 条），7 个 Issue 与 7 个 PR 已关闭/合并，**无新版本发布**。
- **研究焦点**：今日与研究相关的议题集中在 **视觉-语言能力**（image_generate 参考图、computer_use 视觉捕获）、**推理可靠性**（LLM 将 `MEDIA:` 误写为 `FILE:`、提示注入防御误伤合法操作）、**记忆与长上下文架构**（可配置记忆后端、LiteLLM 上下文长度检测），以及 **AI 可靠性/安全**（浏览器私有页面边界、网关会话隔离）。
- **整体判断**：项目维护活跃度极高，但当天大部分更新仍偏向平台集成、部署稳定性与工具修复，基础研究突破信号有限；可靠性工程（会话状态、提示注入、视觉工具边界）是当前最突出的研究-工程交叉点。

---

## 2. 版本发布

**无。** 过去 24 小时未发布新版本。

---

## 3. 项目进展

### 已合并/关闭的重要 PR

| PR/Issue | 内容 | 研究/工程意义 |
|---|---|---|
| [PR #37725](https://github.com/NousResearch/hermes-agent/pull/37725) | 隔离网关会话上下文与进程级环境变量 | 提升多会话/多租户推理可靠性，避免会话状态污染 |
| [PR #38404](https://github.com/NousResearch/hermes-agent/pull/38404) | 支持 macOS `launchd` 托管网关的重启路径 | 部署可靠性 |
| [PR #37724](https://github.com/NousResearch/hermes-agent/pull/37724) | `delegate_task` 子代理超时诊断增强 | 长链路推理的可观测性提升 |
| [Issue #53773](https://github.com/NousResearch/hermes-agent/issues/53773) | TUI WebSocket 在长时 `delegate_task` 中断问题（已关闭） | 长上下文/长任务交互稳定性 |
| [Issue #57390](https://github.com/NousResearch/hermes-agent/issues/57390) | `STEER_CHANNEL_NOTE` 导致提示注入假阳性的自我放大循环（已关闭，标记为 #36934 重复） | 对齐/安全机制误触发 |
| [Issue #21562](https://github.com/NousResearch/hermes-agent/issues/21562) | `image_generate` 不支持参考图输入（已关闭） | 多模态生成能力缺口 |

### 已进入代码审查的关键 PR

| PR | 内容 | 相关研究主题 |
|---|---|---|
| [PR #25897](https://github.com/NousResearch/hermes-agent/pull/25897) | 将 LLM 常误用的 `FILE:` 识别为 `MEDIA:` 的别名 | **模型幻觉 / 推理输出解析** |
| [PR #57423](https://github.com/NousResearch/hermes-agent/pull/57423) | Webhook 每交付会话在运行真正结束时关闭 | 长上下文会话生命周期 |
| [PR #57417](https://github.com/NousResearch/hermes-agent/pull/57417) | 网关多路复用 profile 路由隔离 | 安全边界与多租户可靠性 |
| [PR #57421](https://github.com/NousResearch/hermes-agent/pull/57421) | ACP 通道传递 `agent.disabled_toolsets` | 工具使用可控性 |
| [PR #57418](https://github.com/NousResearch/hermes-agent/pull/57418) | ACP 通道传递模型 fallback 链 | 推理失败恢复机制 |
| [PR #57383](https://github.com/NousResearch/hermes-agent/pull/57383) | 禁止在私有页面执行 Camofox 输入操作 | 浏览器工具的安全

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

**PicoClaw 研究视角日报 — 2026-07-03**

> 本摘要已按“多模态推理、长上下文理解、post-training 对齐、AI 可靠性”方向进行过滤。多数条目为配置、依赖、聊天网关或安全补丁，与研究主线关联度较低；仅少数条目涉及大模型 API 兼容与输出可靠性。

---

### 1. 今日速览

- 今日仓库活跃度中等：新增/活跃 Issue 2 条、PR 25 条（14 条已合并/关闭），并发布一个自动 Nightly 构建。
- 从研究视角看，活动集中在基础设施与工程维护：配置迁移、Matrix 长连接重连、依赖升级、前端工具链等。
- 唯一与 AI 可靠性直接相关的是仍在开放的 PR #3165：它修复 OpenAI 兼容流式响应中 **Seed XML tool-call 残留** 被用户看到的问题，并提取结构化 tool call。
- 没有涉及多模态视觉-语言、长上下文训练、post-training 对齐或模型幻觉治理的新 Issue/PR。
- 整体判断：项目健康度以维护为主，研究/模型层面的进展有限。

---

### 2. 版本发布

**Nightly Build: `v0.3.1-nightly.20260702.2cf030d2`**  
- 类型：自动化每日构建，标注为“可能不稳定，谨慎使用”。  
- 变更范围：未提供研究相关 Release Notes，完整变更对比见 `v0.3.1...main`。  
- 研究提示：该版本未发布模型能力、训练方法或评估基准的更新。  
- 链接：https://github.com/sipeed/picoclaw/compare/v0.3.1...main

---

### 3. 项目进展

**已合并/关闭（非研究主线，但提升系统可靠性与安全）**

- **PR #3063** — 新增 DeltaChat 网关（聊天协议集成）。  
  https://github.com/sipeed/picoclaw/pull/3063
- **PR #3160** — 拒绝跨站 launcher 初始密码设置请求，增强认证安全。  
  https://github.com/sipeed/picoclaw/pull/3160
- **PR #3161** — 修复 `exec` 自定义 allow 规则绕过 deny 模式的问题。  
  https://github.com/sipeed/picoclaw/pull/3161
- **PR #3158** — 增加沙箱文件系统 Windows 路径回归测试。  
  https://github.com/sipeed/picoclaw/pull/3158
- 大量依赖升级已合并（eslint、react-i18next、shadcn、typescript-eslint、Vite plugin、Anthropic SDK、Go crypto 等）。

**研究相关进展**

- **PR #3165（开放，stale）** — 在 OpenAI 兼容层中恢复 Volcengine Doubao Seed 的 `<seed:tool_call>` XML 块为结构化 tool call，并**从用户可见内容中剥离残留 XML**，同时抑制流式 chunk 中的泄漏。  
  - 研究意义：属于 **AI 输出可靠性 / tool-use 推理机制** 的修复，可减少“模型内部标记泄露到用户界面”的类幻觉现象。  
  - 链接：https://github.com/sipeed/picoclaw/pull/3165

---

### 4. 社区热点

今日 Issue/PR 的评论数和反应数均为 0 或未定义，未形成明显研究热点。

- **Issue #3206** — v2→v3 配置迁移报错：新安装仍被误判存在未知字段 `build_info`、`session.dm_scope`。  
  链接：https://github.com/sipeed/picoclaw/issues/3206
- **Issue #3203** — Matrix `/sync` 长轮询在断网/服务器重启后无重连，进程静默存活导致 systemd 无法重启。  
  链接：https://github.com/sipeed/picoclaw/issues/3203

> 研究视角：这两条都是工程运维问题，未触发对模型能力、训练数据或幻觉的讨论。

---

### 5. Bug 与稳定性

| 严重度 | 问题 | 状态 | 是否有 fix PR | 研究相关性 |
|---|---|---|---|---|
| 🔴 高 | **Issue #3203**：Matrix sync 循环无重连，网络/服务器中断后静默死亡 | 开放 | 否 | 无 |
| 🟡 中 | **Issue #3206**：v2→v3 配置迁移误报未知字段，导致 `picoclaw status` 失败 | 开放 | 否 | 无 |
| 🟡 中 | **PR #3171**：LINE 通道 `sync.Map` 类型断言缺少 `ok` 检查，可能 panic | 开放（PR 即 fix） | 是 | 无 |
| 🟢 低 | **PR #3161**：`exec` 自定义 allow 规则绕过 deny 模式 | 已修复 | 已合并 | 无 |
| 🟢 低 | **PR #3158**：沙箱文件系统 Windows 路径处理回归测试 | 已合并 | 已合并 | 无 |

- 链接：  
  - Issue #3203：https://github.com/sipeed/picoclaw/issues/3203  
  - Issue #3206：https://github.com/sipeed/picoclaw/issues/3206  
  - PR #3171：https://github.com/sipeed/picoclaw/pull/3171

---

### 6. 功能请求与路线图信号

- **未发现**与下列方向相关的功能请求或设计讨论：  
  - 视觉-语言多模态能力  
  - 长上下文建模/推理机制  
  - post-training 对齐/RLHF/DPO  
  - 幻觉检测、归因、评估或输出可信度机制

- **间接信号**：GitHub Copilot SDK 连续升级（PR #3177 已合并、PR #3207 开放）表明 PicoClaw 在持续接入代码助手生态，但这属于 AI 应用集成，而非模型研究。  
  - PR #3207：https://github.com/sipeed/picoclaw/pull/3207

---

### 7. 用户反馈摘要

从今日 Issue 提炼的真实痛点：

1. **配置迁移体验不佳**：新安装即遭遇“未知字段”错误，说明向后兼容/schema 验证存在缺陷。  
2. **网关服务稳定性差**：Matrix 长连接中断后无自愈，运维监控难以感知。  
3. **使用场景**：用户主要在运行聊天/IM 网关（Matrix、Line、DeltaChat 等），未出现对大模型输出质量、幻觉或视觉能力的反馈。

> 研究相关反馈：无。当前用户声音集中在工程部署与运维，而非模型能力。

---

### 8. 待处理积压

以下开放条目已有一段时间未关闭，建议维护者优先关注：

- **PR #3165**（2026-06-24 起开放，已 stale）  
  - 内容：OpenAI 兼容层 Seed XML tool-call 提取与残留抑制。  
  - 研究重要性：直接关联 AI 输出可靠性、tool-use 结构化和类幻觉泄漏。  
  - 链接：https://github.com/sipeed/picoclaw/pull/3165

- **PR #3171**（2026-06-25 起开放）  
  - 内容：LINE 通道 `sync.Map` 类型断言安全修复。  
  - 链接：https://github.com/sipeed/picoclaw/pull/3171

- **Issue #3203 / #3206**（2026-07-02 报告）  
  - 尚无修复 PR，影响基本可用性。  
  - 链接：https://github.com/sipeed/picoclaw/issues/3203  
  - 链接：https://github.com/sipeed/picoclaw/issues/3206

---

**总结**：PicoClaw 今日以维护性更新为主，研究层面仅有 PR #3165 值得关注。建议后续跟踪该 PR 是否被合并，以及是否会出现针对模型幻觉、多模态或长上下文的新 Issue/PR。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

**NanoClaw 项目研究动态日报（2026-07-03）**

---

## 1. 今日速览

过去 24 小时 NanoClaw 仓库共有 **4 条 Issues**（全部 open）和 **14 条 PRs**（12 open / 2 closed），无新版本发布。整体活跃度中等，但新增内容主要集中在 WhatsApp/Signal 通道适配、定时任务、模板与容器配置等产品/工程领域。从**多模态推理、长上下文理解、post-training 对齐与 AI 可靠性**的研究视角看，今日可纳入摘要的信号较少，仅见系统提示（core-instructions）输出规范与 Codex provider 角色注入两类相关改动。当前仓库没有与视觉语言能力、显式推理机制或训练方法论直接相关的 Issue/PR。

---

## 2. 版本发布

- **无新 Release**。

---

## 3. 项目进展

### 今日已合并/关闭的 PR
- **PR #2890** `feat(templates): local template loader, ncl --template, and docs` — 已关闭，完成模板加载器第一阶段。  
  https://github.com/qwibitai/nanoclaw/pull/2890
- **PR #2771** `perf(container): configurable --shm-size (default 1g) + --init for agent containers` — 已关闭，优化容器运行时参数。  
  https://github.com/qwibitai/nanoclaw/pull/2771

### 研究相关的进行中的 PR
- **PR #2910** 正在尝试修正核心指令：禁止模型在最终消息块里重复 `send_message` 的内容。  
  https://github.com/qwibitai/nanoclaw/pull/2910
- **PR #2908** 正在为 Codex provider 增加 persona prepend 与无 git 依赖的 skill 发现。  
  https://github.com/qwibitai/nanoclaw/pull/2908

> 注：今日已关闭的 PR 均为产品/基础设施方向，不直接涉及研究议题。

---

## 4. 社区热点

今日没有形成集中研究讨论。Issues 中：
- **#2916** 仅为打招呼/测试信息，无实质内容。  
  https://github.com/qwibitai/nanoclaw/issues/2916
- 讨论热度最高的是工程类 Bug：**#2911**（WhatsApp Cloud 与原生 WhatsApp 适配器 key 冲突）与 **#2912**（同一用户在不同 WhatsApp 路径下 ID 不一致），属于多通道身份一致性，**不属视觉语言或推理机制研究范畴**。

---

## 5. Bug 与稳定性

按严重程度排序，今日研究相关 Bug 优先列出：

### 研究/AI 可靠性相关
1. **PR #2910** — `[High]` 核心指令未明确禁止模型在 final message block 中重复 `send_message` 的内容，可能导致输出重复、工具调用与最终消息混淆，属于“输出格式幻觉/指令泄露”类风险。  
   https://github.com/qwibitai/nanoclaw/pull/2910
2. **PR #2824** — `[Medium]` 主种子提示中仍残留失效的 “Global Memory” 指令，存在导致模型行为漂移或误读上下文的隐患。  
   https://github.com/qwibitai/nanoclaw/pull/2824
3. **PR #2823** — `[Medium]` `groups/global/CLAUDE.md` 被主机每次启动时删除，说明全局记忆文件未能持久化，影响长上下文/记忆一致性。  
   https://github.com/qwibitai/nanoclaw/pull/2823

### 产品/工程类 Bug（仅做稳定性记录）
- **Issue #2911** — `[High]` WhatsApp Cloud 与 Baileys 适配器注册到同一 key `whatsapp`，导致消息路由错配。  
  https://github.com/qwibitai/nanoclaw/issues/2911
- **Issue #2912** — `[Medium]` 同一 WhatsApp 用户在不同接入路径下生成不同 ID，权限/成员关系无法跨路径复用。  
  https://github.com/qwibitai/nanoclaw/issues/2912
- **PR #2915** — `[Medium]` 重复性调度任务去重缺失，导致同系列任务 fork 出重复实例。  
  https://github.com/qwibitai/nanoclaw/pull/2915
- **PR #2689** — `[Medium]` Signal DM 平台 ID 与 `isMention` 标志不一致，导致首条消息丢失。  
  https://github.com/qwibitai/nanoclaw/pull/2689

---

## 6. 功能请求与路线图信号

- **无视觉语言、多模态或模型训练方法相关的新功能请求。**
- **Issue #

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

⚠️ 摘要生成失败。

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis 项目日报（2026-07-03）

> 研究视角筛选：今日数据中 **0 条 Issues**、**0 条 Releases**、**3 条 PRs**。经筛选，3 条 PR 均属于基础设施/产品工程（WhatsApp 协议适配、第三方 LLM Provider 接入），**未涉及视觉语言能力、推理机制、训练方法论或幻觉相关研究议题**。以下按项目健康度维度报告，研究相关条目标记为“无”。

---

## 1. 今日速览

- 过去 24 小时内项目活跃度较低：无 Issues 新增、无 Release、仅 3 条 PR 更新。
- 3 条 PR 中 2 条待合并（Open）、1 条已关闭（Merged/Closed）。
- 所有变更集中在 WhatsApp 网关协议升级（LID 地址迁移）与第三方 LLM 路由服务 Requesty 的接入，属于兼容性维护与生态扩展。
- **研究相关性**：无新增视觉语言、推理、训练或幻觉相关研究内容。

---

## 2. 版本发布

无新版本发布。

---

## 3. 项目进展

| PR | 状态 | 内容 | 研究相关性 |
|---|---|---|---|
| [PR #1144](https://github.com/moltis-org/moltis/pull/1144) | Open | 将 `whatsapp-rust` 从 0.5 升级至 0.6，并通过 `[patch.crates-io]` 锁定到 `oxidezap/whatsapp-rust#943` 的合并提交，以支持 LID-native 地址。 | 无（基础设施/协议兼容） |
| [PR #1143](https://github.com/moltis-org/moltis/pull/1143) | Open | 新增 Requesty 作为 OpenAI 兼容 Provider，采用与现有 `openrouter` 类似的表驱动方式接入。 | 无（Provider 生态扩展） |
| [PR #1116](https://github.com/moltis-org/moltis/pull/1116) | Closed | 修复 WhatsApp 中向 @lid 隐私聊天发送回复时消息被静默丢弃的问题：通过 PN JID 重写确保投递。 | 无（网关消息投递修复） |

**整体推进评估**：项目在产品稳定性与第三方生态适配上持续维护，但今日无研究能力或算法层面的实质进展。

---

## 4. 社区热点

- 无活跃讨论。所有 PR 评论数为未显示/0，点赞数为 0。
- 未出现高互动 Issues 或 PR。

---

## 5. Bug 与稳定性

- **[PR #1116](https://github.com/moltis-org/moltis/pull/1116) 已关闭（已修复）**：WhatsApp 网关向隐私启用用户的 @lid 聊天发送回复时出现静默丢消息、无送达回执。
  - 严重程度：中高（影响消息送达，用户侧无反馈）。
  - 状态：已有 fix PR 并关闭。
- 无今日新报告的 Bug、崩溃或回归问题。

---

## 6. 功能请求与路线图信号

- 无用户新功能请求（0 Issues）。
- 从现有 PR 可推断的信号：
  - **Provider 多元化**：[PR #1143](https://github.com/moltis-org/moltis/pull/1143) 接入 Requesty，表明项目可能在扩展 LLM 路由兼容面。
  - **WhatsApp 协议持续维护**：[PR #1144](https://github.com/moltis-org/moltis/pull/1144) 跟进 LID 地址迁移，显示对隐私/地址模型变更的响应。
- 以上均为产品/工程方向，与研究路线图无直接关联。

---

## 7. 用户反馈摘要

- 无可用用户反馈（无新增 Issues、无 PR 评论）。

---

## 8. 待处理积压

- 今日数据未显示长期未响应的重要 Issue 或 PR。
- 当前待维护者关注的新开 PR：
  - [PR #1144](https://github.com/moltis-org/moltis/pull/1144)：WhatsApp Rust 依赖升级，涉及协议地址迁移，建议优先审阅。
  - [PR #1143](https://github.com/moltis-org/moltis/pull/1143)：新 Provider 接入，需审查兼容性与配置规范。

---

**结论**：从研究视角看，Moltis 今日无视觉语言、推理、训练或幻觉相关进展；项目健康度表现为稳定的产品维护状态，但社区活跃度偏低。

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

**CoPaw / QwenPaw 研究动态日报 — 2026-07-03**

> **筛选说明**：本报告已过滤 UI/UX、前端复制、渠道配置、移动端适配、发布工程、账号限流等与研究关联较弱的条目，聚焦 **视觉语言、推理机制、训练/对齐方法、幻觉与可靠性**。

---

## 1. 今日速览

过去 24 小时 CoPaw（仓库实际路径为 `agentscope-ai/QwenPaw`）活跃度极高：**24 条 Issues（16 活跃/新开、8 关闭）** 与 **50 条 PRs（23 待合并、27 已合并或关闭）**。研究层面的核心信号来自 **v2.0.0-beta.2** 的上下文压缩策略：社区已复现 `scroll` 压缩在任务中途“折叠当前 turn”，导致模型回复旧消息，呈现典型的长上下文幻觉/失忆现象。同时，视觉输入被误判为媒体能力失败、LLM 调用失败回退、记忆检索重排序、工具调用死循环等议题构成了今日的可靠性主线。整体项目推进较快，但 v2.0 beta 的稳定性仍需大量打磨。

---

## 2. 版本发布

### v2.0.0-beta.2（早期 Beta）

- **性质**：QwenPaw 2.0.0 的第二个 beta 版本，仍在活跃开发中，**不建议用于生产**。
- **主要变更**：What's Changed 中仅披露了 `feat(cli): add cron up...`（CLI 增加 cron 相关能力），其余内容在数据中未完整展示。
- **风险与迁移建议**：
  - 明确声明可能包含 **breaking changes** 与不稳定行为。
  - 生产环境应继续使用 v1.1.x 稳定线；v2.0 beta 建议在隔离实例/容器内测试。
  - 升级前备份 `agent.json` 与 `history.db`，因 beta 可能存在配置与数据格式兼容风险。

> 链接：[v2.0.0-beta.2 Release](https://github.com/agentscope-ai/QwenPaw/releases/tag/v2.0.0-beta.2)

---

## 3. 项目进展

### 已合并/关闭的研究相关 PR

| PR | 贡献 | 研究意义 |
|---|---|---|
| **#5533** | 避免把 provider 内容安全审核错误（如 MiniMax `new_sensitive` / `(1026)` 含 `image` 字段）误判为模型“拒绝媒体输入”。 | **视觉语言能力**：防止错误地给模型标记 `rejects_media=True`，保护多模态视觉输入能力。 |
| **#5287** | 自动上下文压缩生成的摘要若超出 `SummarySchema` 的 `maxLength`，不再导致 `jsonschema` 校验崩溃。 | **长上下文/推理机制**：提升上下文压缩的鲁棒性，减少长对话进程异常中断。 |
| **#5727** | 修复 `_filter_by_scope` 与 `goal mode` gate 架构，使 `/goal` 模式下的通用处理器能正确评估。 | **推理机制**：修复控制流/作用域过滤缺陷，改善任务目标导向的推理链路。 |
| **#5676** | 系统提示未列出可用技能元数据（已关闭）。 | **训练/对齐**：提示工程层面的 agent skill 发现能力改进，与官方 skill 指南对齐。 |

### 待合并的重要研究相关 PR

| PR | 状态 | 研究意义 |
|---|---|---|
| **#5747** | 待合并 | 保护 `scroll` 上下文压缩中的 active turn，避免任务被错误折叠。 |
| **#5749** | 待合并 | 为消费者处理增加 300s 超时并自动停止 typing 指示器，防止 agent 挂起。 |
| **#5597** | 待合并 | 支持 per-agent 与全局 LLM model fallback，提升模型调用可靠性。 |
| **#5692** | 审阅中 | 在 reme0.4 记忆检索后增加 reranker 重排序，改进记忆 recall 质量。 |

---

## 4.

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