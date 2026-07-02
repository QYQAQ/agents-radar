# OpenClaw 生态日报 2026-07-02

> Issues: 290 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-07-02 00:33 UTC

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

# 个人 AI 助手 / 自主智能体开源生态横向对比（2026-07-02）

---

## 1. 生态全景

当前开源生态已由“模型能力展示”转向“系统级可靠性建设”：高频活跃项目普遍不再单纯堆功能，而是把**长上下文压缩、记忆生命周期治理、工具 grounding 防幻觉、安全沙箱**作为核心基础设施。同时，视觉-语言交互（computer-use、artifact 预览）的成本控制与多 Agent 协同也被提上日程。整体看，生态呈现**“高热度、低收敛”**特征——Issue/PR 吞吐量大，但大量安全与稳定性问题仍处于开放或待合并状态。

---

## 2. 各项目活跃度对比

| 项目 | Issues 更新（开/关） | PRs 更新（开/关） | 版本发布 | 健康度评估 |
|---|---|---|---|---|
| **OpenClaw** | —（摘要生成失败） | — | — | **数据缺失**，作为核心参照当日无法评估 |
| **NanoBot** | 8（5/3） | 47（25/22） | 无 | **高**，工具推理与记忆治理快速迭代 |
| **Hermes Agent** | 50（45/5） | 50（38/12） | **v0.18.0** | **高**，发布大版本，但存在 P0 安全漏洞 |
| **PicoClaw** | 2（1/1） | 11 | 仅 nightly | **中**，网关稳定性小步修复，但多条高优 PR stale |
| **NanoClaw** | 6（全开放） | 12（6/6） | 无 | **中-低**，清理旧 PR 但新增多个高危部署 Bug |
| **NullClaw** | 1（开放） | 0 | 无 | **低**，维护空窗，仅构建兼容性问题 |
| **IronClaw** | 26（19/7） | 50 | 无 | **高**，可靠性与可解释性基建投入大 |
| **LobsterAI** | 4（3/1） | 25（4/21） | 无 | **中-高**，工程活跃但核心研究信号弱 |
| **CoPaw / QwenPaw** | 21（16/5） | 50（23/27） | 无 | **高**，长上下文与安全治理进展显著 |
| **ZeroClaw** | 50（46/4） | 50（45/5） | 无 | **高活跃、低收敛**，工程主导，开放积压大 |
| **TinyClaw** | 0 | 0 | 无 | **无活动** |
| **Moltis** | 0 | 0 | 无 | **无活动** |
| **ZeptoClaw** | 0 | 0 | 无 | **无活动** |

---

## 3. 研究定位分析

| 项目 | 多模态/视觉 | 长上下文/记忆 | 对齐/安全/可靠性 | 技术路线标签 |
|---|---|---|---|---|
| **NanoBot** | 无直接更新 | 记忆归档 provenance、提前 consolidation、上下文剪枝 | 沙箱逃逸修复、MCP deny-all 策略、鉴权对齐 | 本地优先 Agent + 记忆治理 + 安全加固 |
| **Hermes Agent** | computer-use 视觉 grounding、截图上下文压缩 | 消息与 computer-use token 膨胀治理 | 危险命令 regex denylist 绕过（P0） | 桌面消费级助手 + 模型路由 + 视觉成本控制 |
| **PicoClaw** | 通道级视觉/流式体验 | 网关状态生命周期 | XML 工具调用泄漏修复、exec deny 策略 | 轻量网关/桥接 + OpenAI 兼容层 |
| **NanoClaw** | 无 | QMD 语义对话搜索 | 部署安全/稳定性 | 容器化自托管平台 |
| **IronClaw** | 无直接更新 | 渐进式工具披露、系统提示可观测性 | 失败分类学、runner lease 超时、工具可见性 | 可靠性优先框架 + 可解释性接缝 |
| **LobsterAI** | artifact 多模态预览 | 技能 watch 性能瓶颈 | 任务中止恢复、MCP 分组 | 企业协同 AI cowork |
| **CoPaw**

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

**NanoBot 项目日报 · 2026-07-02**  
（研究视角：聚焦工具推理、长上下文、记忆可靠性与幻觉抑制，已剔除纯商业/集成无关项）

---

### 1. 今日速览

过去 24 小时 NanoBot 社区活跃度极高：Issues 更新 8 条（5 开/活跃，3 关闭），Pull Requests 更新 47 条（25 待合并，22 已合并/关闭），无新版本发布。从研究相关角度看，**今日没有视觉语言（VLM）能力或模型训练方法论的直接更新**，但项目在高频推进 **Agent 工具调用推理、记忆档案治理、长上下文压缩** 与 **安全边界** 等方向。值得关注的是，`edit_file`  wrong-occurrence 问题被首次以 benchmark 数据形式提出（#4634），并配套了强 line-guard PR（#4635），同时记忆系统通过来源归属（provenance）和提前 consolidation 降低幻觉与上下文噪声。

---

### 2. 版本发布

今日无新版本发布，本部分省略。

---

### 3. 项目进展

今日已关闭/合并的关键 PR 与 Issue 主要落在测试可复现性、安全加固与鉴权对齐：

- **测试与可复现性**
  - [PR #3982](https://github.com/HKUDS/nanobot/pull/3982) / [PR #4631](https://github.com/HKUDS/nanobot/pull/4631)：新增 scripted agent runner 测试框架，可捕获 provider 请求并断言完整对话 transcript，覆盖 tool call → tool result → final response 的完整推理循环。
  - [PR #3983](https://github.com/HKUDS/nanobot/pull/3983) / [PR #4630](https://github.com/HKUDS/nanobot/pull/4630)：为 runner 增加对非可执行 finish reason（`refusal`/`content_filter`/`error`）下不调用工具的回归测试。
  - [PR #4193](https://github.com/HKUDS/nanobot/pull/4193) / [PR #4628](https://github.com/HKUDS/nanobot/pull/4628)：新增 memory lifecycle 测试框架，覆盖从 archived summary 到 `history.jsonl` 与 GitStore 的持久化路径。

- **安全与稳定性**
  - [Issue #4434](https://github.com/HKUDS/nanobot/issues/4434)（已关闭）：修复 MCP `enabledTools: []` deny-all 策略被绕过、导致资源/prompts 仍暴露给模型的安全漏洞。
  - [Issue #4490](https://github.com/HKUDS/nanobot/issues/4490)（已关闭）：OpenAI 兼容 API 在绑定到所有接口时要求鉴权，与 WS gateway 的现有策略拉齐。
  - [Issue #4615](https://github.com/HKUDS/nanobot/issues/4615)（已关闭）：修复 `CronService` 在 `os.fsync()` 父目录时 gateway 启动崩溃的问题。
  - [PR #4119](https://github.com/HKUDS/nanobot/pull/4119) / [PR #4629](https://github.com/HKUDS/nanobot/pull/4629)：修复相对路径 symlink 导致 exec 命令逃出工作区的沙箱逃逸。

---

### 4. 社区热点

| 条目 | 评论/状态 | 核心诉求 |
|------|----------|---------|
| [Issue #4604](https://github.com/HKUDS/nanobot/issues/4604) Anthropic OAuth | 3 评论 / 开放 | 用户希望不依赖 Console API key 即可接入 Claude，相关实现已在 [PR #4632](https://github.com/HKUDS/nanobot/pull/4632) 提出。 |
| [Issue #4615](https://github.com/HKUDS/nanobot/issues/4615) gateway fsync 崩溃 | 2 评论 / 已关闭 | 跨平台文件系统行为差异导致启动失败，已迅速修复。 |
| [Issue #4434](https://github.com/HKUDS/nanobot/issues/4434) MCP 安全绕过 | 2 评论 / 已关闭 | 对“空 allowlist = 完全拒绝”的语义有明确预期，但实现存在 bypass，影响 AI 系统可靠性。 |
| [Issue #4634](https://github.com/HKUDS/nanobot/issues/4634) edit_file 错误定位 | 0 评论 / 开放（但配套 PR #4635） | benchmark 显示“edit 错位置”是主导失败模式，对工具调用推理有重要研究意义。 |

---

### 5. Bug 与稳定性

按严重程度排列：

1. **严重**
   - [Issue #4434](https://github.com/HKUDS/nanobot/issues/4434)：MCP `enabledTools: []` 拒绝策略被绕过，模型可访问本不应暴露的资源与 prompts。**已关闭/修复。**
   - [Issue #4490](https://github.com/HKUDS/nanobot/issues/4490) / [PR #4490](https://github.com/HKUDS/nanobot/pull/4490)：OpenAI 兼容 API 监听所有接口时缺乏鉴权，存在未授权访问风险。**已关闭/修复。**
   - [PR #4629](https://github.com/HKUDS/nanobot/pull/4629)（修复中）：`exec` 命令通过相对 symlink 逃出工作区。**已有 fix PR，开放待合并。**

2. **高**
   - [Issue #4615](https://github.com/HKUDS/nanobot/issues/4615)：gateway 启动时 `CronService` 对父目录 `fsync()` 触发 OSError。**已关闭/修复。**

3. **中**
   - [Issue #4637](https://github.com/HKUDS/nanobot/issues/4637)：Telegram 长 markdown 消息被拆分后，除最后一段外的 trunk 无法渲染。**开放，尚无 fix PR。**

---

### 6. 功能请求与路线图信号

以下方向与工具推理、记忆可靠性、长上下文管理高度相关，预计会进入后续版本或已处于开发收尾：

- **工具调用与推理链**
  - [Issue #4634](https://github.com/HKUDS/nanobot/issues/4634) / [PR #4635](https://github.com/HKUDS/nanobot/pull/4635)：通过 `line_hint`、`target_line`、`target_start_line` 等多维定位机制，抑制 `edit_file` 的 wrong-occurrence 错误。
  - [PR #4623](https://github.com/HKUDS/nanobot/pull/4623)：支持 subagent spawn 时按次覆盖模型，为多模型推理与成本/能力分级提供可能。
  - [PR #4624](https://github.com/HKUDS/nanobot/pull/4624)：subagent `aggregated` 结果模式，将多个子任务结果合并后一次性返回，改善长上下文中的多 Agent 协作。

- **记忆、幻觉与来源归属**
  - [PR #4621](https://github.com/HKUDS/nanobot/pull/4621)：在 Consolidator 归档时引入来源上下文与用户确认规则，抑制错误事实与重复记忆的累积。
  - [PR #4626](https://github.com/HKUDS/nanobot/pull/4626)：可选 eager memory consolidation，将已完成的对话片段提前归档，降低后续推理窗口噪声。
  - [PR #4627](https://github.com/HKUDS/nanobot/pull/4627)：修复 consolidation 时丢失 delivery context 的问题，保证 replay window 与 `Session.get_history()` 边界一致。

- **长上下文与效率**
  - [PR #4581](https://github.com/HKUDS/nanobot/pull/4581)：prune 低价值上下文载荷，对持久化 subagent 公告、重复 tool results 进行压缩，适配 tight context budget。

- **产品/集成**
  - [Issue #4612](https://github.com/HKUDS/nanobot/issues/4612) OpenAI Responses API、[#4604](https://github.com/HKUDS/nanobot/issues/4604) / [#4632](https://github.com/HKUDS/nanobot/pull/4632) Anthropic OAuth。

---

### 7. 用户反馈摘要

- **工具执行准确性**：[Issue #4634](https://github.com/HKUDS/nanobot/issues/4634) 指出，在离线编辑 benchmark 中，`edit_file` 的 “old_text 匹配成功但修改了错误位置” 是主导失败模式，严重影响代码 Agent 的推理可靠性。
- **记忆与事实一致性**：[PR #4621](https://github.com/HKUDS/nanobot/pull/4621) 反映用户/维护者意识到 archive 阶段缺乏来源约束会导致错误事实被反复固化，需通过 provenance 与 source-discipline 规则抑制幻觉。
- **上下文管理**：[PR #4581](https://github.com/HKUDS/nanobot/pull/4581) 与 [PR #4626](https://github.com/HKUDS/nanobot/pull/4626) 显示长上下文与对话历史噪声已成为可扩展性瓶颈，需要主动剪枝与提前归档。
- **安全预期

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 项目研究动态日报（2026-07-02）

> **分析师注**：本报告已从 50 条 Issues 和 50 条 PRs 中过滤掉 Slack/Telegram/Discord/iMessage/Desktop/字体/TTS 等一般产品/商业更新，重点聚焦**视觉语言能力、推理机制、训练方法论、幻觉/可靠性**四个研究维度。当日与核心模型研究直接相关的内容相对稀疏，多数信号集中在 Agent 执行层的安全、鲁棒性与上下文效率上。

---

## 1. 今日速览

- 项目在 24 小时内活跃度高：Issues 更新 50 条（45 开放/活跃、5 关闭），PRs 更新 50 条（38 待合并、12 已合并/关闭），并发布 **v0.18.0** 大版本。
- **研究相关信号有限**：没有直接涉及模型训练、视觉语言基准、RLHF 或幻觉评估的 issue/PR；主要进展在 **computer-use 视觉 grounding 的鲁棒性**、**上下文/Token 膨胀治理**、**模型路由与安全护栏**。
- 社区最热议的是**默认 16K token 消耗**、**Linux/WSL 下 computer-use 崩溃**、**每轮任务感知模型路由**三个话题。
- 安全方面出现一条 **P0 级** issue：危险命令的 regex denylist 可通过简单 shell 转义绕过，存在静默 RCE 风险。

---

## 2. 版本发布

### v0.18.0 — *The Judgment Release*（2026-07-01）
- **发布链接**：https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.1
- **版本号**：`v2026.7.1` / `v0.18.0`
- **发布说明当前提供的数据被截断**，仅能看到如下规模指标：
  - ~1,720 commits
  - 998 merged PRs
  - 2,215 files changed
  - ~251,000 insertions / ~41,000 deletions
  - 949 issues closed
  - 370+ community contributors
- **研究视角**：版本代号 *The Judgment Release* 暗示可能与评估、对齐或安全裁决机制相关，但具体新增的视觉语言能力、推理框架或幻觉评测工具细节在提供的摘录中未出现。建议查阅完整 Release Notes 以确认是否有模型/评估相关的 Breaking Changes。

---

## 3. 项目进展

### 已合并/关闭的 PRs（研究相关）

| PR | 说明 | 与研究的相关性 |
|---|---|---|
| [#28271](https://github.com/NousResearch/hermes-agent/pull/28271) | 为 `custom_providers` 增加 `ssl_verify` 字段，支持自签名 HTTPS | 偏部署/infra，对私有化模型推理端点接入有意义 |
| [#48891](https://github.com/NousResearch/hermes-agent/pull/48891) | 为 `custom_providers` 增加 `ssl_ca_cert` 字段，支持按 provider 配置 CA bundle | 同上，提升本地/私有模型推理的可靠性 |

### 处于待合并阶段、具有研究意义的 PRs

| PR | 核心内容 | 研究意义 |
|---|---|---|
| [#56706](https://github.com/NousResearch/hermes-agent/pull/56706) | **限制消息与 computer-use 的 token 膨胀**：为 Telegram/Feishu 等消息平台增加确定性 fast-path、工具结果预算、UI 验证与深度诊断预算；默认压缩 `computer_use` 输出（截图写入文件而非直接塞入上下文） | 直接关联**长上下文理解**与**视觉-语言交互的成本控制**，可能减少多轮工具调用导致的上下文漂移 |
| [#56709](https://github.com/NousResearch/hermes-agent/pull/56709) / [#56707](https://github.com/NousResearch/hermes-agent/pull/56707) | 修复 `computer_use` 在 Linux/WSL 下因 `list_windows` 返回 `pid: null` 或 `window_id: null` 导致的 `TypeError` | **视觉-语言/计算机

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目研究动态日报（2026-07-02）

> **筛选说明**：本日报聚焦于与 LLM 推理链路、模型输出可靠性、工具调用解析、流式生成与系统稳定性相关的研究/工程信号。纯 UI/依赖升级/商业产品更新已做降权或省略。

---

## 1. 今日速览

- 过去 24 小时项目活跃度中等，新增 2 条 Issues、11 条 PRs，仅 1 个自动化 nightly 版本。
- 研究相关进展集中在 **LLM 网关稳定性**、**模型输出解析（工具调用 XML 泄漏）** 与 **推理体验（流式输出、模型降级链）** 三个方向。
- 值得关注的是 **PR #3165** 针对 Volcengine Doubao Seed 的 `<seed:tool_call>` XML 块在 OpenAI 兼容层泄漏问题进行了修复，这属于模型输出与幻觉/格式控制交叉的研究信号。
- 一个高优先级稳定性问题 **Issue #3164**（Android/Termux 上 gateway 启动即崩溃）目前仍为 OPEN，尚无 fix PR。
- 整体健康度：代码活跃度尚可，但存在多条 **stale PR** 未合并，且模型级/多模态研究内容较少。

---

## 2. 版本发布

- **nightly: v0.3.1-nightly.20260701.2cf030d2**
  - 这是一个自动化 nightly 构建，明确标注 **可能不稳定，谨慎使用**。
  - 未提供独立的变更说明，完整 diff 见：[`v0.3.1...main`](https://github.com/sipeed/picoclaw/compare/v0.3.1...main)。
  - **迁移/使用注意**：nightly 不建议用于生产；若涉及 OpenAI 兼容层、工具调用或 Pico 生命周期相关实验，建议等待基于当前 main 的稳定 tag。

---

## 3. 项目进展

今日关闭/合并的重要 PR：

- **PR #3116 — `fix(pico): complete turn.done lifecycle signaling`**（已关闭）
  - 补全了 Pico 通道的 `turn.done` 生命周期信号，修复了请求 ID 在排队 steering/follow-up 消息中丢失、以及部分情况下 `turn.done` 未触发等问题。
  - 对多轮/流式 LLM 交互的会话边界一致性有直接帮助。
  - [https://github.com/sipeed/picoclaw/pull/3116](https://github.com/sipeed/picoclaw/pull/3116)

- **PR #2975 — `feat(telegram): treat reply to bot message as mention in group chats`**（已关闭）
  - 在 Telegram 群聊中，将“回复机器人消息”视为 @提及，扩展了触发机器人的交互路径。
  - 属于多模态/对话交互的通道行为研究，但模型层影响有限。
  - [https://github.com/sipeed/picoclaw/pull/2975](https://github.com/sipeed/picoclaw/pull/2975)

---

## 4. 社区热点

- **Issue #3164 — Process hooks crash gateway on Android/Termux**
  - 唯一带有 1 条评论的活跃 Issue，反映用户在移动端/Termux 部署时，JSON-RPC over stdio 的 hook 机制导致 gateway 启动 2 秒内崩溃。
  - 背后是“边缘设备运行 LLM gateway”与进程间通信可靠性的诉求。
  - [https://github.com/sipeed/picoclaw/issues/3164](https://github.com/sipeed/picoclaw/issues/3164)

- **Issue #3201 — Support streaming output for QQ channel**
  - 新功能请求，要求 QQ 通道支持实时增量输出（token-by-token），目前仅 Telegram 和 Pico WebSocket 实现 `StreamingCapable`。
  - 反映用户对低延迟、流式生成体验的持续关注。
  - [https://github.com/sipeed/picoclaw/issues/3201](https://github.com/sipeed/picoclaw/issues/3201)

---

## 5. Bug 与稳定性

| 严重度 | 问题 | 状态 | 是否有 Fix PR | 说明 |
|--------|------|------|---------------|------|
| **高** | Issue #3164：Android/Termux 上 process hooks 导致 gateway 崩溃 | OPEN | 否 | 影响边缘部署，最小可复现示例也会崩溃 |
| 中 | PR #3161：`exec` 的 deny 模式在匹配自定义 allow 规则时被跳过 | OPEN（stale） | 是（待合并） | 可导致安全策略被绕过 |
| 中 | PR #3160：跨站点 launcher 密码设置请求未被拒绝 | OPEN（stale） | 是（待合并） | 安全/CSRF 相关 |
| 低 | PR #3158：sandbox fs Windows 路径处理缺乏回归测试 | OPEN（stale） | 是（测试 PR） | 跨平台路径一致性 |

- 已修复的稳定性问题：PR #3116（Pico `turn.done` 生命周期）。

---

## 6. 功能请求与路线图信号

- **Issue #3201 — QQ 通道流式输出**
  - 若纳入下一版本，将进一步统一各 IM 通道的流式推理体验，对低延迟 LLM 应用有研究价值。
  - [https://github.com/sipeed/picoclaw/issues/3201](https://github.com/sipeed/picoclaw/issues/3201)

- **PR #3200 — 可配置默认模型 fallback 链**
  - 在 Web UI 中支持设置默认模型、添加/排序降级模型并持久化。
  - 与模型可靠性、推理成本控制、自动降级策略相关，属于部署层研究信号。
  - [https://github.com/sipeed/picoclaw/pull/3200](https://github.com/sipeed/picoclaw/pull/3200)

- **PR #3165 — 恢复 Volcengine Doubao Seed `<seed:tool_call>` XML 工具调用**
  - 从 OpenAI 兼容响应内容中解析 XML 工具调用，并**从用户可见内容与流式 chunk 中剥离**。
  - 直接对应“模型输出格式泄漏 / 伪工具调用内容”这一类幻觉/可靠性问题。
  - [https://github.com/sipeed/picoclaw/pull/3165](https://github.com/sipeed/picoclaw/pull/3165)

---

## 7. 用户反馈摘要

- **边缘部署痛点**：Issue #3164 表明有用户尝试在 Android/Termux 运行 gateway，但 JSON-RPC stdio hook 机制导致启动即崩溃，阻碍了低成本/移动化部署。
- **流式体验需求**：Issue #3201 说明 QQ 用户希望获得与 Telegram/Pico WebSocket 一致的实时增量输出，减少等待完整响应的延迟。
- **工具调用可靠性**：PR #3165 反馈出模型（Doubao Seed）通过 OpenAI 兼容接口返回的 XML 工具调用会泄漏到用户可见内容，需要在网关层做后处理。
- **多轮交互一致性**：PR #3116 解决了 Pico 通道中 `turn.done` 信号不完整的问题，影响多轮对话状态管理。

---

## 8. 待处理积压

以下 Issue/PR 已长期未合并/未响应，建议维护者优先关注：

- **PR #3165** — Seed XML 工具调用恢复与泄漏抑制（OpenAI 兼容层，stale）
- **PR #3161** — `exec` deny 模式与自定义 allow 规则的安全策略冲突（stale）
- **PR #3160** — 跨站点 launcher 设置请求防护（stale）
- **PR #3158** — sandbox fs Windows 路径回归测试（stale）
- **Issue #3164** — Android/Termux gateway 崩溃（stale，无 fix PR）
- **依赖升级 PR #3104 / #3103 / #3100** — shadcn / typescript-eslint / vite-plugin-react（均为 stale，与研究关联度低）

---

**总体评估**：PicoClaw 今日在研究相关的工程改进上以小步修复为主，重点在模型输出解析安全与网关交互稳定性。然而高优先级崩溃问题（Issue #3164）和多条 stale 安全/可靠性 PR 仍需尽快处理，否则将影响项目健康度。

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目日报（2026-07-02）

> **研究视角说明**：今日 6 条 Issue 与 12 条 PR 全部集中在部署运维、消息通道与容器管理层面。在指定的研究主题——视觉语言能力、推理机制、训练方法论、幻觉抑制——没有直接相关条目。因此本报告以“项目健康度与工程可靠性”为主线，并标注与长上下文/对话记忆相关的少量信号。

---

## 1. 今日速览

- 过去 24 小时活跃度中等偏高：新建 6 条 Issue 且全部未关闭；PR 共 12 条更新，其中 6 条已关闭/合并，6 条仍待审。
- **无新版本发布**，项目未进入发布窗口。
- 新增 Issue 高度集中在首次部署与稳定性：OneCLI 默认网络绑定失效、消息被静默吞掉、webhook 端口冲突导致整个 host 崩溃、`.env` 配置项被忽略。
- 所有 Issue/PR 的公开评论数与点赞数均为 0，社区互动指标冷清，但问题本身的严重等级较高。
- **整体健康度**：中等偏下。今日合并了若干旧 PR 和一项关键 WhatsApp 内存泄漏修复，但多个“首次使用即失败”的高危 bug 同时浮现，需要尽快 triage。

---

## 2. 版本发布

无。

---

## 3. 项目进展（今日已关闭/合并的 PR）

| PR | 作者 | 核心内容 | 项目意义 |
|---|---|---|---|
| [#2905](https://github.com/nanocoai/nanoclaw/pull/2905) | ankushchadha | 修复 WhatsApp 重连时未关闭旧 Baileys socket 导致的内存泄漏 | 提升消息通道长期运行稳定性 |
| [#2677](https://github.com/nanocoai/nanoclaw/pull/2677) | shrwnsan | 调度前脚本失败时重试一次并附带诊断信息 | 增强 agent 任务调度鲁棒性 |
| [#1257](https://github.com/nanocoai/nanoclaw/pull/1257) | shrwnsan | 支持自定义 Anthropic-compatible API endpoint（如 z.ai） | 增加模型/服务商接入灵活性 |
| [#1716](https://github.com/nanocoai/nanoclaw/pull/1716) | shrwnsan | 新增 `/check-contribution` 运营技能，自动做 PR 前检 | 降低社区贡献门槛与审查成本 |
| [#1693](https://github.com/nanocoai/nanoclaw/pull/1693) | shrwnsan | 新增 `/add-backup` 工具技能，自动备份状态数据 | 提升自托管用户数据安全性 |
| [#1597](https://github.com/nanocoai/nanoclaw/pull/1597) | shrwnsan | 新增 QMD 技能，用于语义化对话搜索 | 对话记忆与长上下文检索能力的小幅增强 |

**整体判断**：今日关闭了多条 2026 年 3–6 月提交的技能与基础设施 PR，显示维护者正在进行积压清理；但功能层面的进展仍属于“运营/连接/部署工具”，而非模型能力本身的突破。

---

## 4. 社区热点

由于所有条目的评论数与点赞数均为 0，没有“讨论最活跃”的条目。从 **严重程度和用户阻塞面** 看，以下 Issue 是社区当前最关注的痛点：

- **[#2903](https://github.com/nanocoai/nanoclaw/issues/2903)**：全新安装后 OneCLI gateway 因绑定地址（127.0.0.1 vs 10.0.0.1 docker bridge）不匹配导致 agent 永久无响应。
- **[#2902](https://github.com/nanocoai/nanoclaw/issues/2902)**：消息投递失败后仅写日志，不向用户返回任何错误，造成“静默吞消息”。
- **[#2900](https://github.com/nanocoai/nanoclaw

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

**NullClaw 项目日报 — 2026-07-02**  
（从研究视角看，今日仓库活动属于工程/构建类问题，与视觉语言、推理机制、训练方法或幻觉问题无直接关联。）

---

### 1. 今日速览
- 过去 24 小时内，NullClaw 仓库仅有 **1 条 Issue 更新**，无 Pull Request 合并/关闭，也无新版本发布。  
- 整体活跃度显著偏低，社区处于维护空窗期。  
- 唯一活跃的讨论是 Android/Termux（aarch64）平台上 `zig build` 构建失败的问题，属于交叉编译/构建系统兼容性 Bug，不涉及模型能力或算法研究。  
- 当前没有可见的代码迭代、功能推进或研究相关进展。  
- 项目健康度短期受困于“构建入口受阻”：对使用移动/Termux 环境的开发者来说，无法完成编译直接影响参与门槛。  

---

### 2. 版本发布
无。  
仓库链接：[https://github.com/nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)

---

### 3. 项目进展
今日无合并或关闭的 PR，未观察到新功能、修复或重构推进。  
仓库链接：[https://github.com/nullclaw/nullclaw/pulls](https://github.com/nullclaw/nullclaw/pulls)

---

### 4. 社区热点
- **Issue #868** — `[bug] zig build fails on Android/Termux (aarch64) with AccessDenied on options.zig linkat`  
  - 作者：NOTJuangamer10  
  - 创建：2026-04-23，更新：2026-07-01  
  - 评论数：6，👍：0  
  - 链接：[https://github.com/nullclaw/nullclaw/issues/868](https://github.com/nullclaw/nullclaw/issues/868)  
- **背后诉求**：用户希望在 Android/Termux 这一受限环境中完成 NullClaw 的 Zig 构建；`linkat` 临时文件链接失败通常与 Termux 文件系统/权限限制或 Zig 工具链在该平台上的行为差异有关。讨论反映出“移动设备作为开发环境”的兼容性需求。

---

### 5. Bug 与稳定性
| 严重程度 | 标题 | 状态 | 是否有 fix PR | 链接 |
|---|---|---|---|---|
| 中-高 | `zig build` 在 Android/Termux aarch64 上失败（`options.zig linkat` 报 `AccessDenied`） | 开放 | 否 | [Issue #868](https://github.com/nullclaw/nullclaw/issues/868) |

- **影响范围**：使用 Termux 在 aarch64 Android 设备上编译 NullClaw 的用户。  
- **根因线索**：Zig 构建系统在写入 `options.zig` 临时文件并通过 `linkat` 链接到目标位置时失败，可能与 Termux 对 `linkat` 系统调用的支持或目录权限有关。  
- **研究相关性**：无；属于构建系统与平台兼容性。

---

### 6. 功能请求与路线图信号
今日无新功能请求或可被识别的路线图信号。  
Issue/PR 查询链接：[https://github.com/nullclaw/nullclaw/issues](https://github.com/nullclaw/nullclaw/issues)

---

### 7. 用户反馈摘要
来自 Issue #868 的真实反馈：  
- **痛点**：在 Android/Termux 环境中无法通过 `zig build -Doptimize=ReleaseSmall` 完成编译。  
- **使用场景**：希望在移动设备（小米 Redmi Note 9 / LineageOS 22.2）上直接构建和运行 NullClaw。  
- **不满意之处**：构建系统对受限/非标准 Linux 环境（Termux）的兼容性不足，且问题已开放两个多月仍未解决。  

---

### 8. 待处理积压
- **Issue #868**（创建于 2026-04-23，已活跃逾两个月）是今日唯一需要维护者关注的积压项。  
  - 链接：[https://github.com/nullclaw/nullclaw/issues/868](https://github.com/nullclaw/nullclaw/issues/868)  
  - 建议维护者提供：Termux 环境复现步骤、对 Zig 0.16.0 在该平台已知限制的判断，以及是否需要绕过 `linkat` 的构建系统补丁。

---

**研究视角备注**：今日 NullClaw 的 GitHub 数据完全未涉及视觉语言能力、推理机制、训练后对齐或幻觉相关议题。如需跟踪这些研究方向，建议关注仓库中带有 `model`、`multimodal`、`reasoning`、`training`、`hallucination` 等标签的 Issue/PR，或查看官方文档/论文发布渠道。

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

**IronClaw 项目研究动态日报**  
*日期：2026-07-02 | 数据来源：nearai/ironclaw GitHub*

---

### 1. 今日速览

过去 24 小时 IronClaw 活跃度极高，共更新 **26 个 Issues**（19 个开放/活跃、7 个关闭）和 **50 个 PRs**，但**无新版本发布**。从研究视角看，最值得关注的信号是项目正从“功能堆砌”转向“可解释、可调试、长上下文可控”的 Agent 可靠性建设：首次出现系统性的 **Daily failure taxonomy**（[#5495](https://github.com/nearai/ironclaw/issues/5495)），对模型路由错误、多工具工作流失败、runner lease 超时等失效模式进行归类；同时，**渐进式工具披露**（[#5149](https://github.com/nearai/ironclaw/pull/5149)）和**系统提示可观测性接缝**（[#5481](https://github.com/nearai/ironclaw/pull/5481)）持续推进，直接对应长上下文压缩与模型推理可见性。然而，P1/P2 级 QA 缺陷密集，尤其是多工具 routine 的 lease 超时、运行失败后线程不可见、对话历史累积导致前端延迟

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目日报（2026-07-02）

> 本日报已从研究视角（视觉语言、推理机制、训练方法、幻觉抑制）对原始 GitHub 数据做了过滤。整体而言，本日工程活跃度较高，但**没有直接涉及上述四个核心研究主题的 Issue/PR**，主要进展集中在 Agent 协同（cowork）、MCP 工具集成、artifact 多模态预览与系统稳定性。

---

## 1. 今日速览

- 过去 24 小时共更新 **25 个 PR**（21 已合并/关闭，4 待合并）、**4 个 Issue**（3 个活跃/开放，1 个关闭），**无新版本发布**。
- 工程活跃度较高，但研究信号较弱：没有涉及模型训练、视觉语言理解、推理架构或幻觉抑制的核心工作。
- 与多模态/长上下文/Agent 推理最相关的**弱信号**包括：子 Agent 产物可视化（PR #2249）、任务中止后的计划恢复（PR #2247）、技能文件 watch 性能瓶颈（Issue #2243）以及 MCP 工具生态扩展（PR #2244、Issue #2239）。

---

## 2. 版本发布

省略（本日无新版本发布）。

---

## 3. 项目进展（研究相关筛选）

- **子 Agent 产物面板（PR #2249）**  
  在 artifact 面板新增 Subagents 标签，支持从 turn chips 右侧打开详情，避免替换主会话页。这是多 Agent 协同可视化的工程基础，但未触及核心推理机制。  
  [netease-youdao/LobsterAI#2249](https://github.com/netease-youdao/LobsterAI/pull/2249)

- **任务中止与计划恢复（PR #2247）**  
  将计划恢复延迟到 OpenClaw 运行生命周期结束后，防止会话文件锁冲突；将 OpenClaw 失败 finals 视为系统错误而非拟议计划。属于 Agent 执行可靠性改进。  
  [netease-youdao/LobsterAI#2247](https://github.com/netease-youdao/LobsterAI/pull/2247)

- **MCP 工具集成：企查查与分组服务器管理（PR #2244）**  
  新增 Qichacha 授权与多 MCP 服务器分组管理，扩展外部工具/知识源接入能力，对工具增强型推理有间接意义。  
  [netease-youdao/LobsterAI#2244](https://github.com/netease-youdao/LobsterAI/pull/2244)

- **Artifact 自动预览（PR #2248）**  
  在最新 assistant turn 完成后自动按本地服务、文档、HTML、视频、图片优先级打开预览，并修复图片替换后 tab 未同步问题。属于多模态交互体验，而非视觉语言模型研究。  
  [netease-youdao/LobsterAI#2248](https://github.com/netease-youdao/LobsterAI/pull/2248)

---

## 4. 社区热点

- **趋势判断：编程工具与 Agent 的边界融合（Issue #2239）**  
  作者建议 LobsterAI 向“OpenClaw 化”演进，通过 MCP 深度联动 CodeBuddy/OpenCode 等编程工具。这属于产品生态/战略层面的讨论，与工具增强型 Agent 规划推理仅有间接关系。  
  [netease-youdao/LobsterAI#2239](https://github.com/netease-youdao/LobsterAI/issues/2239)

- **技能文件 watch 性能瓶颈（Issue #2243）**  
  用户报告 174 个技能导致 watch 机制频繁触发快照刷新，造成大量

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

**CoPaw（QwenPaw）研究动态日报 — 2026-07-02**  
*数据来源：agentscope-ai/QwenPaw | 统计窗口：过去 24 小时*

---

### 1. 今日速览

过去 24 小时项目活跃度极高：**Issues 21 条**（新开/活跃 16，关闭 5）、**PRs 50 条**（待合并 23，已合并/关闭 27），**无新版本发布**。与研究相关的核心主线集中在：  
- **长上下文可靠性**：上下文压缩、工具结果截断、输入框长度限制；  
- **推理机制可控性**：`reasoning_content` 是否回传模型的开关；  
- **记忆检索增强**：ReMe 0.4 引入 reranker；  
- **系统提示与技能注入**：修复可用技能未注入导致的调用失败/幻觉；  
- **执行层对齐与安全**：governance strict mode、沙箱、browser tool 资源回收。  

关键进展：Headroom 可选上下文压缩层（#5063）与工具结果硬上限（#5342）已被关闭，显示社区在“控制上下文爆炸”方面取得实质性防御性进展。

---

### 2. 版本发布

**无**（过去 24 小时未发布新版本）。

---

### 3. 项目进展（研究相关已关闭/重要待合并）

| 编号 | 类型 | 研究意义 | 链接 |
|------|------|----------|------|
| **#5063** | 已关闭 Issue | 集成 Headroom 作为可选上下文压缩层，宣称可降低工具输出、对话历史、RAG chunk 等 60–95% token；对长上下文理解与成本治理有直接意义。 | https://github.com/agentscope-ai/QwenPaw/issues/5063 |
| **#5342** | 已关闭 Issue | 在执行层对工具结果大小设置 hard cap，防止 `post_acting` 钩子因 LLM 失败被跳过时引发上下文爆炸级联故障。 | https://github.com/agentscope-ai/QwenPaw/issues/5342 |
| **#5523** | 已关闭 Issue | `spawn_subagent` 在 Runtime 2.0 工具注册表中缺失，已修复；关系到多 Agent 协作与运行时工具发现可靠性。 | https://github.com/agentscope-ai/QwenPaw/issues/5523 |
| **PR #5457** | 已合并 | 限制 `send_file_to_user` 文件大小，减少大文件通过用户通道反向注入上下文的风险。 | https://github.com/agentscope-ai/QwenPaw/pull/5457 |


</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目日报（2026-07-02）

> **数据范围**：过去 24 小时 GitHub Issues 50 条（新开/活跃 46，已关闭 4）/ PR 50 条（待合并 45，已合并/关闭 5）/ 新 Releases 0 个。  
> **研究视角说明**：ZeroClaw 仓库本质是**智能体编排与运行时框架**（agent runtime/framework），而非基础模型或视觉语言研究项目。因此今日数据中直接对应“视觉语言、训练方法论”的基础研究条目极少；本报告会如实标注每项内容的“研究相关性”，并重点提取与**推理机制、长上下文/记忆、工具幻觉/ grounding、post-training 对齐（SOP/Skill）** 相关的信号，跳过一般产品/商业更新。

---

## 1. 今日速览

- 今日仓库活跃度极高（46 个活跃 Issue + 45 个开放 PR），但**工程落地与集成稳定性占绝对主导**，无新版本发布，仅依赖审计机器人关闭了一个过期告警（#8585）。
- 核心聚集在四类问题：**MCP/工具可见性与接入可靠性**、**Web Dashboard 会话中断与 SOP 发现失败**、**运行时安全加固**（zip 炸弹/密钥）、**持久化记忆与自主目标模式**。
- 与研究主题最接近的进展包括：目标模式（goal mode）实现 PR #8393、持久记忆存储 seam PR #8570、SOP 程序化记忆 workshop PR #8509、Mixture-of-Agents 虚拟提供者提案 #8568，以及上下文压缩 RFC #7673。
- **视觉语言与模型训练方法论**：今日未出现直接相关 Issue/PR；仅有 #8360 的“provider-side multimodal payload handling”作为跟踪项被提及，但无具体更新。
- **幻觉/grounding 相关**：间接体现在 MCP 工具“已连接却不可见”的 grounding 断裂（#8193、#8302）、SOP 配置无法被运行时加载（#8563）、以及 `.ignore`/workspace 文件保护 RFC #8424。

---

## 2. 版本发布

无新版本发布。  
相关链接：[ZeroClaw Releases](https://github.com/zeroclaw-labs/zeroclaw/releases)

---

## 3. 项目进展

今日仓库关闭/合并数量有限，主要进展来自仍在推进的大型 PR，而非已合并的代码：

| 类型 | 编号 | 内容 | 研究相关性 |
|------|------|------|------------|
| PR | [#8570](https://github.com/zeroclaw-labs/zeroclaw/pull/8570) | `feat(memory): epic A durable store seam` — 将持久化记忆统一到一个 `Memory` trait 后，新增可撤销 supersede、写时去重、价值感知预算与策略门控。 | 高：长上下文/记忆管理、智能体一致性 |
| PR | [#8393](https://github.com/zeroclaw-labs/zeroclaw/pull/8393) | `feat(runtime): implement goal mode` — 实现 RFC #8303 的持久目标模式控制平面（生命周期记录、目标规格、暂停/取消/预算耗尽）。 | 高：自主推理、任务规划、agent loop |
| PR | [#8508](https://github.com/zeroclaw-labs/zeroclaw/pull/8508) | `feat(mcp): resources-as-context, pinning, and named-prompt rendering` — MCP 资源作为上下文注入、固定与具名提示渲染。 | 中：工具上下文 grounding、减少幻觉 |
| PR | [#8509](https://github.com/zeroclaw-labs/zeroclaw/pull/8509) | `feat(sop): add procedural memory workshop` — 允许智能体创建、检查、拒绝、隔离并显式应用 SOP 提案。 | 高：post-training 对齐、可解释策略学习 |
| PR | [#8551](https://github.com/zeroclaw-labs/zeroclaw/pull/8551) | `feat(plugins): channel host bindings` — 为 WASM 插件提供 `wasi:http`、入站队列与配置 jail，使网络通道可作为签名插件交付。 | 低：架构/安全 |
| PR | [#8561](https://github.com/zeroclaw-labs/zeroclaw/pull/8561) | `feat(channels/telegram): add multi_message streaming mode` — 按 agent turn 边界切分 Telegram 流式输出。 | 低：UX |

**整体判断**：项目正朝“更可控的自主运行”推进——目标模式、持久记忆、SOP 程序记忆三者共同构成中长期智能体对齐与可靠性的基础设施。

---

## 4. 社区热点

| 编号 | 讨论热度 | 核心诉求 | 研究/工程关联 |
|------|----------|----------|---------------|
| [#8193](https://github.com/zeroclaw-labs/zeroclaw/issues/8193) | 13 评论，P1 | MCP 工具在 Gateway 侧可见，但 TUI 会话接收不到，导致工作流阻塞 | **工具 grounding 断裂**，可视为“模型/运行时认为工具存在但前端无法使用”的幻觉类不一致 |
| [#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) | 13 评论 | RFC：Work Lanes、看板自动化与标签清理 | 治理流程，与研究产出效率相关但非直接 |
| [#8226](https://github.com/zeroclaw-labs/zeroclaw/issues/8226) | 5 评论 | 支持 per-agent 自定义环境变量与 secrets，解决多租户下 MCP 实例身份冲突 | 安全/多租户，间接影响智能体可靠性 |
| [#8568](https://github.com/zeroclaw-labs/zeroclaw/issues/8568) | 1 评论，👍0 | **RFC：Mixture-of-Agents (MoA) 虚拟模型提供者** — 多参考模型并行输出，聚合器/裁判模型综合 | **高：推理集成与模型协作机制** |
| [#8303](https://github.com/zeroclaw-labs/zeroclaw/issues/8303) | 3 评论，👍1 | **RFC：Goal mode for bounded autonomous session work** — 用户目标驱动直到完成/暂停/取消/预算耗尽 | **高：自主推理、任务规划、预算控制** |

**背后诉求**：社区既在追“更快接入外部工具/模型”，也在强烈要求“可控的自主运行与多模型协作”——这是从“能跑”到“可靠跑”的转换信号。

---

## 5. Bug 与稳定性

按严重程度排列，标注是否有修复 PR：

| 严重度 | 编号 | 问题 | 修复 PR / 状态 |
|--------|------|------|----------------|
| S1 | [#8193](https://github.com/zeroclaw-labs/zeroclaw/issues/8193) | MCP tools/tool_search 在 TUI 会话中缺失，Gateway 侧可见 | 开放，accepted |
| S1 | [#8553](https://github.com/zeroclaw-labs/zeroclaw/issues/8553) | Agent 无法将环境变量用作 `http_request` secrets | 开放 |
| S1 | [#8559](https://github.com/zeroclaw-labs/zeroclaw/issues/8559) | 退出 Web Dashboard 聊天窗口后 Agent 停止工作 | 开放 |
| S1 | [#8563](https://github.com/zeroclaw-labs/zeroclaw/issues/8563) | Web Dashboard 聊天会话中 Agent 无法使用已配置的 SOP | 开放 |
| S2 | [#8554](https://github.com/zeroclaw-labs/zeroclaw/issues/8554) | Skill ZIP 解压器对 zip-bomb 膨胀无上限 | [#8574](https://github.com/zeroclaw-labs/zeroclaw/pull/8574) / [#8548](https://github.com/zeroclaw-labs/zeroclaw/pull/8548) 已提交 |
| S1 | [#6891](https://github.com/zeroclaw-labs/zeroclaw/issues/6891) | Scheduled Jobs 编辑接口 422 错误 | 开放 |
| S2 | [#8302](https://github.com/zeroclaw-labs/zeroclaw/issues/8302) | Web Dashboard 工具列表不显示已配置 MCP 服务器发现的工具 | 开放，in-progress |

**研究视角**：S1 级问题集中在“工具/策略/环境在运行时不可见”——这会直接放大**工具幻觉**和**策略不一致**风险；#8554 的 zip-bomb 修复则关乎外部 skill 供应链的稳健性。

---

## 6. 功能请求与路线图信号

| 编号 | 方向 | 纳入下一版本可能性 | 研究相关性 |
|------|------|---------------------|------------|
| [#8568](https://github.com/zeroclaw-labs/zeroclaw/issues/8568) | MoA 虚拟模型提供者 | 中（刚提交，需架构评审） | **高：多模型推理聚合** |
| [#8303](https://github.com/zeroclaw-labs/zeroclaw/issues/8303) / [#8393](https://github.com/zeroclaw-labs/zeroclaw/pull/8393) | Goal mode 自主目标工作 | 高（已 accepted，PR 在推进） | **高：自主推理、任务规划、预算/安全边界** |
| [#7673](https://github.com/zeroclaw-labs/zeroclaw/issues/7673) | 原生上下文压缩（CompressionDecorator） | 中（blocked，需作者更新） | **高：长上下文理解、成本/质量权衡** |
| [#8570](https://github.com/zeroclaw-labs/zeroclaw/pull/8570) | 持久记忆统一 seam | 高（PR 已提交） | **高：长上下文记忆、策略一致性** |
| [#8509](https://github.com/zeroclaw-labs/zeroclaw/pull/8509) | SOP 程序化记忆 workshop | 高（PR 已提交） | **高：post-training 对齐、可解释策略** |
| [#8424](https://github.com/zeroclaw-labs/zeroclaw/issues/8424) | `.ignore` 工作区文件保护机制 | 中（blocked） | 中：减少敏感信息泄露，间接降低错误 grounding |
| [#7497](https://github.com/zeroclaw-labs/zeroclaw/issues/7497) | OCI 容器仓库作为 WASM 插件分发机制 | 低（blocked，需维护者评审） | 低：架构/供应链 |

---

## 7. 用户反馈摘要

从 Issues 中提炼的真实痛点：

1. **工具可见性 != 工具可用性**：用户反复报告 MCP 已连接、工具已发现，

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*