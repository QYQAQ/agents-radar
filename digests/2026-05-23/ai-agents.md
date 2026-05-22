# OpenClaw 生态日报 2026-05-23

> Issues: 500 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-05-22 16:02 UTC

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

# OpenClaw 项目动态日报 | 2026-05-23

---

## 1. 今日速览

OpenClaw 今日维持极高社区活跃度，24小时内 **500 条 Issues 更新**（新开/活跃 428，关闭 72）与 **500 条 PR 更新**（待合并 422，已合并/关闭 78），表明项目处于密集开发期。v2026.5.20 版本刚发布，包含执行安全路径清理与 Discord 语音会话跟随两项关键变更。社区讨论焦点集中在 **会话状态一致性**（session-state）、**消息投递可靠性**（message-delivery）及 **多平台适配**（Telegram/iMessage/Feishu）三大领域。值得关注的是，P1 级 Bug 占比显著，涉及内存泄漏、认证绕过、消息截断等核心稳定性问题，维护者审查队列压力较大。

---

## 2. 版本发布

### [v2026.5.20](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20) — 2026.5.20

| 维度 | 详情 |
|:---|:---|
| **发布日期** | 2026-05-20 |
| **变更类型** | 安全加固 + 功能增强 |

#### 破坏性变更（Breaking Changes）

**Exec approvals 安全路径清理**
- **移除**旧的 `cat SKILL.md && printf ... && <skill-wrapper>` 兼容路径
- **强制要求**：skill 文件必须通过 `read` 工具加载，仅真实的 skill 可执行文件获得自动允许
- **迁移影响**：依赖旧 allowlist 兼容路径的自定义 skill 将失效，需迁移至标准 `read` 工具模式
- **安全等级提升**：消除通过 shell 拼接绕过 skill 沙箱的攻击面

#### 功能增强

**Discord 语音会话跟随**
- 语音会话现可跟随已配置的 Discord 用户进入语音频道，提升多频道协作体验

---

## 3. 项目进展

### 今日合并/关闭的关键 PR

| PR | 作者 | 状态 | 核心贡献 |
|:---|:---|:---|:---|
| [#85391](https://github.com/openclaw/openclaw/pull/85391) | vincentkoc | **已关闭** | macOS 嵌套 gateway 祖先检测 — 解决 `openclaw update` 自毁问题（关联 [#85120](https://github.com/openclaw/openclaw/issues/85120)） |
| [#85036](https://github.com/openclaw/openclaw/pull/85036) | manhhai999 | **已关闭** | 越南语 Control UI 本地化 — 覆盖 v2026.5.18 全平台仪表板 |
| [#52570](https://github.com/openclaw/openclaw/issues/52570) | jalehman | **已关闭** | 恢复 tsgo 绿色构建 — 修复 provider-entry/onboarding 类型漂移 |
| [#51947](https://github.com/openclaw/openclaw/issues/51947) | SidU | **已关闭** | DM 主动发送路由修复 — 解决多会话用户消息错发问题 |
| [#68944](https://github.com/openclaw/openclaw/issues/68944) | WaMaSeDu | **已关闭** | CLI WebSocket 握手挂起修复 — 解除 gateway 连接死锁 |

**整体推进评估**：今日合并量（78/500 PRs）相对偏低，大量高价值 PR 仍卡在 `needs proof` 或 `waiting on author` 状态。核心架构层面，会话生命周期管理（yield/pause/reset）和跨平台消息投递可靠性取得实质进展，但 **审查带宽瓶颈** 明显。

---

## 4. 社区热点

### 讨论最活跃的 Issues（按评论数排序）

| 排名 | Issue | 评论 | 核心诉求 | 标签信号 |
|:---|:---|:---:|:---|:---|
| 1 | [#48788](https://github.com/openclaw/openclaw/issues/48788) 集中式文件名编码工具 | **17** | 东亚语言（中日韩）Content-Disposition 多编码统一处理，拒绝"打地鼠"式补丁 | `impact:data-loss`, `needs-product-decision` |
| 2 | [#48183](https://github.com/openclaw/openclaw/issues/48183) Feishu 监视器内存泄漏 | **17** | 生产环境 httpServers Map 清理不完整，要求 graceful shutdown 等待确认 | `impact:message-loss`, `diamond lobster` |
| 3 | [#50090](https://github.com/openclaw/openclaw/issues/50090) 社区 Skill 生态 & ClawHub | **14** | 从"承诺"到"实践"的鸿沟：Driftnet 碎片化、SKILL.md 标准、可发现性 | `impact:security`, `needs-security-review` |
| 4 | [#29387](https://github.com/openclaw/openclaw/issues/29387) agentDir bootstrap 文件静默忽略 | **13** | 配置分层歧义：agentDir vs workspace 优先级文档与实现不一致 | `P1`, `impact:session-state` |
| 5 | [#53628](https://github.com/openclaw/openclaw/issues/53628) `${XDG_CONFIG_HOME}` 未展开 | **12** | Docker 环境变量插值标准合规（POSIX/XDG） | `impact:data-loss` |

### 背后诉求分析

- **国际化深度适配**：不仅是翻译，而是编码、路径、环境变量的全栈本地化（[#48788](https://github.com/openclaw/openclaw/issues/48788), [#53628](https://github.com/openclaw/openclaw/issues/53628)）
- **企业级可观测性**：内存泄漏、会话僵尸、状态竞争等生产环境问题优先于新功能（[#48183](https://github.com/openclaw/openclaw/issues/48183), [#48573](https://github.com/openclaw/openclaw/issues/48573)）
- **生态治理焦虑**：社区贡献的技能缺乏统一标准，存在"公地悲剧"风险（[#50090](https://github.com/openclaw/openclaw/issues/50090)）

---

## 5. Bug 与稳定性

### P1 级（生产阻断）

| Issue | 症状 | 影响域 | Fix PR 状态 |
|:---|:---|:---|:---|
| [#84516](https://github.com/openclaw/openclaw/issues/84516) | Codex 长回复静默截断于 ~1000-1100 字符 | message-loss | ❌ 无 |
| [#29387](https://github.com/openclaw/openclaw/issues/29387) | agentDir bootstrap 文件被静默忽略 | session-state, security | ❌ 无 |
| [#54531](https://github.com/openclaw/openclaw/issues/54531) | 消息未回发至来源频道（TG/Discord/WA） | session-state, message-loss | ❌ 无 |
| [#44202](https://github.com/openclaw/openclaw/issues/44202) | Apple Silicon 本地嵌入崩溃于 ggml-metal | crash-loop | ❌ 无 |
| [#48003](https://github.com/openclaw/openclaw/issues/48003) | Steer 模式未向主会话注入消息 | session-state, message-loss | ❌ 无 |
| [#57019](https://github.com/openclaw/openclaw/issues/57019) | 会话写锁竞争：释放可删除新获取的锁 | session-state, data-loss | ❌ 无（[#57019](https://github.com/openclaw/openclaw/issues/57019) 自身为 fix PR）|
| [#85126](https://github.com/openclaw/openclaw/issues/85126) | Control UI 自动选择错误 authProfileOverride | auth-provider | ❌ 无 |
| [#51396](https://github.com/openclaw/openclaw/issues/51396) | clearUnboundScopes 无条件剥离 operator 作用域 | security, auth-provider | ❌ 无 |
| [#51871](https://github.com/openclaw/openclaw/issues/51871) | Control UI Cron 作业仪表板空白（回归） | crash-loop | ❌ 无 |
| [#51593](https://github.com/openclaw/openclaw/issues/51593) | Moonshot 工具调用 ID 重复导致 HTTP 400 | crash-loop | ❌ 无 |

### P2 级（显著影响）

| Issue | 症状 | 特殊标记 |
|:---|:---|:---|
| [#51429](https://github.com/openclaw/openclaw/issues/51429) | **硬编码路径 `/Users/wangtao` 被合并发布** | 供应链/流程安全事件 |
| [#48573](https://github.com/openclaw/openclaw/issues/48573) | 嵌入式运行会话状态泄漏—僵尸代理 | `diamond lobster` |
| [#54253](https://github.com/openclaw/openclaw/issues/54253) | RISC-V64 系统 LLM 请求失败 | 架构兼容性 |
| [#45740](https://github.com/openclaw/openclaw/issues/45740) | gh-issues skill 未过滤注入子代理提示 | `impact:security` |
| [#49876](https://github.com/openclaw/openclaw/issues/49876) | Cron 会话工具失败时产生幻觉输出而非干净失败 | 信任与安全 |

### 回归问题集群

- **2026.3.13 引入**：Control UI Cron 显示 ([#51871](https://github.com/openclaw/openclaw/issues/51871))、Steer 模式中断 ([#48003](https://github.com/openclaw/openclaw/issues/48003))、clearUnboundScopes 认证破坏 ([#51396](https://github.com/openclaw/openclaw/issues/51396))
- **2026.3.12 引入**：Control UI 渐进卡顿 ([#45698](https://github.com/openclaw/openclaw/issues/45698))、OPENCLAW_HOME 嵌套目录 ([#45765](https://github.com/openclaw/openclaw/issues/45765))

---

## 6. 功能请求与路线图信号

### 高可行性（已有 PR 或明确路径）

| 功能 | Issue/PR | 信号强度 | 下一版本可能性 |
|:---|:---|:---:|:---|
| **自适应会话重置**（daily + idle 语义） | [#71400](https://github.com/openclaw/openclaw/pull/71400) | ⭐⭐⭐⭐⭐ | **高** — PR 已 `ready for maintainer look` |
| **自动快速模式截止**（auto fast mode） | [#85104](https://github.com/openclaw/openclaw/pull/85104) | ⭐⭐⭐⭐⭐ | **高** — 多平台覆盖，proof supplied |
| **TTS 跳过表情符号** | [#78172](https://github.com/openclaw/openclaw/pull/78172) | ⭐⭐⭐⭐☆ | **中高** — 体验优化，无破坏性 |
| **iOS Realtime-2 通话模式** | [#85131](https://github.com/openclaw/openclaw/pull/85131) | ⭐⭐⭐⭐☆ | **中** — 依赖 Apple 审核节奏 |
| **Workboard 仪表板插件** | [#85367](https://github.com/openclaw/openclaw/pull/85367) | ⭐⭐⭐⭐☆ | **中** — XL 规模，需架构审查 |

### 架构级提案（长期）

| 功能 | Issue | 核心挑战 |
|:---|:---|:---|
| **多会话架构**（共享 LLM + 隔离会话 + 公共知识库） | [#48874](https://github.com/openclaw/openclaw/issues/48874) | 资源隔离与共享的边界设计 |
| **Skill 优先级配置** | [#50199](https://github.com/openclaw/openclaw/issues/50199) | 重叠技能的选择规则与冲突解决 |
| **YAML 配置格式支持** | [#45758](https://github.com/openclaw/openclaw/issues/45758) | 配置迁移与双格式维护成本 |
| **可配置文件权限**（多用户容器） | [#56263](https://github.com/openclaw/openclaw/issues/56263) | 安全默认与灵活性的平衡 |

---

## 7. 用户反馈摘要

### 🔴 核心痛点

| 场景 | 原声引用 | 关联 Issue |
|:---|:---|:---|
| **"我的数据去哪了"** | "agentDir 里的 SOUL.md 完全没效果，只有 workspace 目录有效" | [#29387](https://github.com/openclaw/openclaw/issues/29387) |
| **"升级即崩溃"** | "升级到 2026.3.12 后仪表板越来越卡直到完全卡住" | [#45698](https://github.com/openclaw/openclaw/issues/45698) |
| **"消息石沉大海"** | "响应在 Gateway UI 可见，但手机上永远收不到" | [#54531](https://github.com/openclaw/openclaw/issues/54531) |
| **"幻觉比失败更可怕"** | "工具失败时 LLM 编造合理输出并交付给用户" | [#49876](https://github.com/openclaw/openclaw/issues/49876) |
| **"谁把个人路径合进去了"** | "这位 wangtao 是谁？居然 hardcode 了工作路径" | [#51429](https://github.com/openclaw/openclaw/issues/51429) |

### 🟡 摩擦与困惑

- **Docker 环境变量**：`.env` 中 `XDG_CONFIG_HOME` 不被解释，与宿主机行为不一致 ([#53628](https://github.com/openclaw/openclaw/issues/53628))
- **安装脚本安全性**：`curl \| bash` 时 stdin 被交互提示窃取，导致安装中断 ([#82918](https://github.com/openclaw/openclaw/pull/82918))
- **文档领先于发布**：`IsolatedSessions` 在文档中但不在 2026.3.13 中 ([#48920](https://github.com/openclaw/openclaw/issues/48920))

### 🟢 积极反馈

- **跨平台野心受认可**：RISC-V64 用户主动测试，期待完整支持 ([#54253](https://github.com/openclaw/openclaw/issues/54253))
- **社区生态期待**：ClawHub 愿景被认同，但呼吁"从承诺到实践"的具体行动 ([#50090](https://github.com/openclaw/openclaw/issues/50090))

---

## 8. 待处理积压

### 超期未响应的高价值项（>60 天，P1/P2，有活跃讨论）

| Issue | 创建 | 最后更新 | 天数 | 风险 |
|:---|:---|:---|:---:|:---|
| [#29387](https://github.com/openclaw/openclaw/issues/29387) agentDir bootstrap 忽略 | 2026-02-28 | 2026-05-22 | **83** | 配置模型根本性歧义 |
| [#44202](https://github.com/openclaw/openclaw/issues/44202) Apple Silicon 嵌入崩溃 | 2026-03-12 | 2026-05-22 | **72** | Apple Silicon 用户流失 |
| [#48003](https://github.com/openclaw/openclaw/issues/48003) Steer 模式失效 | 2026-03-16 | 2026-05-22 | **68** | 核心交互模式回归 |
| [#48183](https://github.com/openclaw/openclaw/issues/48183) Feishu 内存泄漏 | 2026-03-16 | 2026-05-22 | **68** | 生产环境稳定性 |
| [#48573](https://github.com/openclaw/openclaw/issues/48573) 嵌入式僵尸会话 | 2026-03-17 | 2026-05-22 | **67** | 状态泄漏累积效应 |
| [#48788](https://github.com/openclaw/openclaw/issues/48788) 文件名编码架构 | 2026-03-17 | 2026-05-22 | **67** | 国际化技术债务 |
| [#50090](https://github.com/openclaw/openclaw/issues/50090) ClawHub 生态 | 2026-03-19 | 2026-05-22 | **65** | 社区增长瓶颈 |

### 审查队列瓶颈

| PR | 状态 | 阻塞原因 |
|:---|:---|:---|
| [#71400](https://github.com/openclaw/openclaw/pull/71400) 自适应会话重置 | `ready for maintainer look` | **缺乏维护者带宽** |
| [#80046](https://github.com/openclaw/openclaw/pull/80046) CLI 工具生命周期桥接 | `ready for maintainer look` | **缺乏维护者带宽** |
| [#84366](https://github.com/openclaw/openclaw/pull/84366) Doctor 会话修复结构化 | `needs proof` | 需要行为验证 |
| [#85104](https://github.com/openclaw/openclaw/pull/85104) 自动快速模式 | `ready for maintainer look` | **缺乏维护者带宽** |

---

## 附录：数据健康度指标

| 指标 | 数值 | 评估 |
|:---|:---|:---|
| Issue 日关闭率 | 14.4% (72/500) | ⚠️ 偏低，积压增长 |
| PR 日合并率 | 15.6% (78/500) | ⚠️ 偏低，审查瓶颈 |
| P1 占比 | ~15% | 🔴 高，需紧急分流 |
| `needs-maintainer-review` 标签密度 | 高 | 🔴 核心瓶颈 |
| `clawsweeper:no-new-fix-pr` 标签密度 | 极高 | 🔴 修复循环停滞 |

**建议行动**：优先扩充维护者审查带宽，或建立 P1 快速通道机制；对 `diamond lobster`/`platinum hermit` 高评级 Issue 实施每周强制盘点。

---

*日报生成时间：2026-05-23 | 数据来源：GitHub openclaw/openclaw*

---

## 横向生态对比

# 个人 AI 助手/自主智能体开源生态横向对比分析报告

**分析日期**: 2026-05-23 | **数据来源**: GitHub 公开活动流

---

## 1. 生态全景

个人 AI 助手开源生态正处于**"基础设施定型"与"场景分化"并行的关键节点**。头部项目（OpenClaw、IronClaw、ZeroClaw）日均 200-500 条 Issues/PR 的吞吐量表明市场热度极高，但审查带宽瓶颈普遍——平均合并率仅 10-16%，大量高价值贡献卡在队列中。技术层面，**多模态扩展**（图像/语音/视频生成）、**企业通道深度集成**（WeChat/钉钉/飞书/Slack）和**子智能体编排**成为共同冲刺方向，而**会话状态一致性**与**生产级可观测性**仍是全生态的稳定性短板。值得关注的是，"去 Claude 中心化"（NanoClaw）与"终端原生重构"（ZeroClaw TUI）两条差异化路线正在形成对 OpenClaw 主导格局的挑战。

---

## 2. 各项目活跃度对比

| 项目 | Issues (24h) | PRs (24h) | 合并/关闭率 | 版本发布 | 健康度评估 |
|:---|:---|:---|:---|:---|:---|
| **OpenClaw** | 500 (关72) | 500 (合78) | 14.4% / 15.6% | v2026.5.20 | 🔴 **承压** — P1 占比 15%，审查瓶颈严重，积压 83 天+ |
| **IronClaw** | 26 (关7) | 50 (合21) | 27% / 42% | 无 | 🟡 **冲刺期** — XL PR 占比 55%，E2E 持续失败 12 天 |
| **NanoBot** | 7 (关4) | 17 (合12) | 57% / 71% | 无 | 🟢 **健康** — 关键 bug 当日修复，但 #3028 心跳问题 42 天未修 |
| **Hermes Agent** | 50 (关6) | 50 (合5) | 12% / 10% | 无 | 🔴 **高危** — 3 个 P1 零响应，技能安装完全失效事故 |
| **PicoClaw** | 6 (关6) | 22 (合9) | 100% / 41% | v0.2.8-nightly | 🟢 **稳健** — 陈旧积压清理高效，核心 PR #2906 待审 |
| **NanoClaw** | 6 (全新开) | 18 (合8) | 0% / 44% | 无 | 🟡 **扩张期** — MCP 工具爆发式增长，Apple Container 技术债爆发 |
| **NullClaw** | 0 | 3 (合0) | — / 0% | 无 | 🟠 **停滞** — 46 天零合并，核心 PR 自我审查瓶颈 |
| **LobsterAI** | 1 (新开) | 21 (合12) | 0% / 57% | 2026.5.22 | 🟢 **优秀** — 子代理三层重构当日闭环，安全 PR stale 7 周 |
| **Moltis** | 4 (关2) | 7 (合4) | 50% / 57% | 无 | 🟢 **巩固期** — Docker/语音系统性修复，社区参与度低 |
| **CoPaw** | 23 (活跃16) | 20 (合9) | 0% / 45% | 无 | 🟡 **活跃** — 企业通道密集修复，#4620 聊天历史丢失 P0 未修 |
| **ZeroClaw** | 18 (关1) | 23 (合2) | 5.6% / 8.7% | 无 | 🟡 **重构期** — TUI 8 个 Issue 批量创建，3 个 P1 无 Fix PR |
| **TinyClaw** | 0 | 0 | — | 无 | ⚪ **休眠** |
| **ZeptoClaw** | 0 | 0 | — | 无 | ⚪ **休眠** |

---

## 3. OpenClaw 在生态中的定位

### 核心优势
| 维度 | 具体表现 |
|:---|:---|
| **规模碾压** | 日均 1000 条 Issues+PR 更新，社区体量约为第二名 IronClaw 的 10 倍 |
| **通道覆盖广度** | Telegram/Discord/iMessage/Feishu/Slack/WhatsApp 全矩阵支持，企业 IM 适配最深 |
| **安全基础设施** | v2026.5.20 的 Exec approvals 路径清理体现对 skill 沙箱的持续投入 |
| **生态标准制定** | SKILL.md 规范、ClawHub 愿景虽受质疑，但仍是事实上的技能分发标准 |

### 技术路线差异
| 对比项 | OpenClaw | 挑战者路线 |
|:---|:---|:---|
| **运行时模型** | 进程级隔离 + 容器化 skill | NanoClaw 推"容器技能"商业模式；IronClaw 推 Rust 原生 TEE |
| **交互范式** | 聊天优先，WebUI 为主 | ZeroClaw 押注 TUI 终端原生；LobsterAI 深耕子代理协作 UI |
| **模型依赖** | Claude 深度集成 | NanoClaw 执行"去 Claude 中心化"，Codex 全链路替代 |
| **配置哲学** | 约定优于配置，agentDir/workspace 分层 | PicoClaw 推"请求级上下文策略"极致可控 |

### 社区规模对比
- **绝对数量**: OpenClaw 的 Issues/PR 吞吐量 = IronClaw × 20 = NanoBot × 60
- **质量效率**: 合并率 15.6% 低于 NanoBot (71%)、PicoClaw (41%)，**"大而不快"**
- **响应 SLA**: P1 问题 83 天未响应（#29387），Hermes Agent 3 个 P1 零回复，均显著劣于 LobsterAI/NanoBot 的"当日闭环"

---

## 4. 共同关注的技术方向

| 技术方向 | 涉及项目 | 具体诉求 | 紧迫程度 |
|:---|:---|:---|:---|
| **会话状态一致性** | OpenClaw (#29387, #54531, #48003), CoPaw (#4620, #3984), NanoBot (#3028) | 历史消息不丢失、上下文压缩不"孤儿"、Steer 模式消息注入可靠 | 🔴 **P0** |
| **企业通道可靠性** | OpenClaw (Feishu 内存泄漏 #48183), CoPaw (WeChat/DingTalk 3 个 PR), ZeroClaw (WhatsApp/Slack 2 个 P1), Moltis (Twilio #1032) | Token 失效不跨请求污染、中文文件名编码正确、环境变量支持合规密钥管理 | 🔴 **P0** |
| **多模态扩展** | NanoBot (Ollama/OpenAI/Codex 图像生成), NanoClaw (Edna/Veo 3.1 视频), ZeroClaw (vision_provider #6841) | 图像生成全提供商覆盖、视频生成入站、视觉输入不被静默忽略 | 🟡 **P1→P0** |
| **子智能体编排** | IronClaw (4 阶段 spawn #3868-3872), LobsterAI (6 PR 三层重构), OpenClaw (多会话架构 #48874) | 子代理消息持久化、父恢复机制、回合级事件广播、去重键设计 | 🟡 **P1** |
| **生产可观测性** | OpenClaw (Feishu 内存泄漏 #48183), PicoClaw (LLM 重试 #629), LobsterAI (#2036 实时落盘) | 回合级生命周期事件、指数退避重试、graceful shutdown 等待确认 | 🟡 **P1** |
| **国际化深度** | OpenClaw (中日韩编码 #48788), NanoBot (7 语种补全), Hermes Agent (11 语言 PR #30492) | 不仅是翻译，而是 Content-Disposition 编码、路径、环境变量的全栈本地化 | 🟢 **P2** |

---

## 5. 差异化定位分析

| 项目 | 核心功能侧重 | 目标用户 | 技术架构关键差异 |
|:---|:---|:---|:---|
| **OpenClaw** | 通用个人助手 + 技能市场 | 技术爱好者、中小企业 | Node.js 单体，进程隔离，Claude 优先 |
| **IronClaw** | NEAR 生态 AI 基础设施 | Web3/区块链开发者 | Rust 原生，TEE 可信执行，Reborn 架构迁移中 |
| **NanoBot** | 轻量可扩展聊天框架 | 自托管爱好者、开发者 | 模块化设计，"lean and mean"哲学，技能动态路由 |
| **Hermes Agent** | 多平台网关 + 插件生态 | 重度 IM 用户、自动化需求 | Tlon/Matrix 去中心化网络，TUI 交互，插件标准化 |
| **PicoClaw** | 可控多 Agent 流水线 | 复杂工作流编排者 | Go 运行时，请求级上下文策略，论坛主题级精细化 |
| **NanoClaw** | 营销自动化 + MCP 工具链 | 商业用户、垂直场景 | 容器技能商业模式，"去 Claude"多模型战略 |
| **LobsterAI** | 子代理协作 + 思维链可视化 | 知识工作者、企业团队 | Electron 桌面，SQLite 本地优先，惰性回填策略 |
| **Moltis** | 语音电话 + Docker 部署 | 客服自动化、电话场景 | 浏览器沙箱 + Twilio 语音，Vault 可选化 |
| **CoPaw** | 企业 IM 深度集成 + 插件市场 | 中国企业、钉钉/微信用户 | Python 后端，Cron 任务上下文管理，Tauri 桌面推进中 |
| **ZeroClaw** | 终端原生 TUI + 多智能体 | 开发者、CLI 重度用户 | Rust，Unix socket RPC，ACP 协议，ephemeral 模式 |

---

## 6. 社区热度与成熟度分层

### 🔥 快速迭代阶段（日均 20+ PR，功能扩张）
| 项目 | 迭代主题 | 风险信号 |
|:---|:---|:---|
| **IronClaw** | Reborn 架构冲刺，Google Extensions + Subagent 双轨 | E2E 持续失败，XL PR 债务累积 |
| **NanoClaw** | MCP 工具爆发，Codex 替代，视频生成 | Apple Container 分支与主线脱节，技术债 |
| **ZeroClaw** | TUI 全栈从零构建，8 个关联 Issue 批量创建 | 3 个 P1 无响应，长期 PR 审查瓶颈 |

### 🛠️ 质量巩固阶段（修复主导，稳定性优先）
| 项目 | 巩固重点 | 待突破点 |
|:---|:---|:---|
| **LobsterAI** | 子代理三层重构当日闭环 | 安全 PR stale 7 周，回合级事件待响应 |
| **NanoBot** | WebUI 性能 + 多模态全覆盖 | #3028 心跳问题 42 天，技能可见性状态不一致 |
| **Moltis** | Docker 沙箱 + 语音可靠性 | 社区参与度极低，零 👍 零评论 |
| **PicoClaw** | 陈旧积压清理，运行时策略引擎 | 核心 PR #2906 背压处理待审 |

### ⚠️ 承压/停滞阶段
| 项目 | 核心问题 | 建议干预 |
|:---|:---|:---|
| **OpenClaw** | 审查带宽瓶颈，P1 占比过高 | 建立快速通道，扩充维护者 |
| **Hermes Agent** | 3 个 P1 零响应，技能安装完全失效 | 立即 hotfix，建立 48h SLA |
| **CoPaw** | #4620 聊天历史丢失长期存在 | 优先分配核心开发者 |
| **NullClaw** | 46 天零合并，自我审查瓶颈 | 引入外部 reviewer，拆分大型 PR |
| **TinyClaw/ZeptoClaw** | 24h 零活动 | 评估项目存续状态 |

---

## 7. 值得关注的趋势信号

### 信号一："终端原生"复兴 —— AI 交互范式分化
> **ZeroClaw TUI 8 个 Issue 批量创建** + **IronClaw WebUI v2 收尾** + **LobsterAI 桌面子代理** 形成"三足鼎立"：浏览器不再是默认答案。对开发者的启示：CLI/TUI 场景（服务器运维、气隙环境、开发者工作流）存在被低估的体验升级空间，Unix socket 直连、ephemeral 守护进程等基础设施值得投入。

### 信号二："去中心化模型"战略 —— 降低单一厂商锁定
> **NanoClaw Codex 全链路替代**（4 个关联 PR）+ **NanoBot Ollama 原生图像生成** + **Moltis NEAR AI Cloud provider** 共同指向：Claude/OpenAI 不再是唯一基础设施。对开发者的启示：多 provider 抽象层（如 NanoClaw 的 `AI-coding-CLI 选择器`）将成为框架级标配，模型切换的"热插拔"能力比单一模型优化更具长期价值。

### 信号三："企业通道即产品" —— IM 集成从功能变为核心竞争力
> **CoPaw hongxicheng 单日 3 个 WeChat/DingTalk 修复** + **OpenClaw Feishu 内存泄漏 68 天未修** + **ZeroClaw Slack 环境变量回归** 的对比表明：通道稳定性直接决定企业采纳。对开发者的启示：Token 失效机制、中文编码、环境变量合规等"无聊但关键"的细节，是区分玩具与生产工具的分水岭。

### 信号四："子智能体"从概念到工程化
> **LobsterAI 6 PR 完成数据层→架构层→表现层三层重构** + **IronClaw 4 阶段 spawn 草案** + **OpenClaw 多会话架构 #48874** 显示：2026 Q2 是"子代理工程化"的关键窗口。对开发者的启示：回合级事件广播、消息去重键设计、父恢复机制等底层协议，将在未来 6 个月成为框架竞争的新战场。

### 信号五："技能生态治理"焦虑 —— 从数量到质量
> **OpenClaw #50090 ClawHub "从承诺到实践"** + **NanoBot #3958 Weather 技能外迁示例** + **Hermes Agent #30482 官方技能安装完全失效** 共同暴露：技能分发面临"公地悲剧"。对开发者的启示：SKILL.md 标准执行、官方技能 CI 保障、可发现性基础设施（评分/分类/搜索）是生态健康度的领先指标，比新增技能数量更重要。

---

*报告生成时间：2026-05-23 | 分析师：AI 智能体与个人 AI 助手开源生态技术分析师*

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 项目动态日报 | 2026-05-23

## 1. 今日速览

NanoBot 今日保持**高活跃度**，24 小时内 17 个 PR 流转（12 条已合并/关闭，5 条待审），7 个 Issues 更新（4 条关闭）。项目核心进展集中在 **WebUI 性能优化**（侧边栏批量渲染、可折叠导航）、**多模态能力扩展**（Ollama/OpenAI/Codex 图像生成）以及 **AI 基础设施加固**（长期记忆去重、Kimi/Moonshot API 兼容性修复）。社区对"技能系统瘦身"和"CLI 生态扩展"展现出明确诉求，已有对应 PR 进入评审阶段。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 🔧 已合并/关闭的关键 PR（12 条）

| PR | 作者 | 核心贡献 | 影响评估 |
|:---|:---|:---|:---|
| [#3946](https://github.com/HKUDS/nanobot/pull/3946) | HaisamAbbas | **Ollama 原生图像生成支持** — 新增 `OllamaImageGenerationClient`，对接 `/api/generate` 端点，支持本地 x/z-image-turbo 等模型 | ⭐⭐⭐ 填补本地部署关键缺口，回应 Issue #3941 |
| [#3954](https://github.com/HKUDS/nanobot/pull/3954) | ZegWe | **OpenAI & Codex 图像生成支持** — 通过 Responses API `image_generation` 工具路由 Codex 订阅用户的 OAuth 图像生成 | ⭐⭐⭐ 完成主流图像提供商全覆盖 |
| [#3964](https://github.com/HKUDS/nanobot/pull/3964) | yu-xin-c | **WebUI 国际化补全** — 填充 es/fr/id/ko/vi 5 个语种的缺失 locale 键（认证、图像生成、会话控制等） | ⭐⭐ 全球化体验完整性提升 |
| [#3962](https://github.com/HKUDS/nanobot/pull/3962) | yu-xin-c | **zh-TW & ja 本地化补全** — 同步补充繁体中文、日语的同等覆盖 | ⭐⭐ 与 #3964 形成完整 i18n 闭环 |
| [#3961](https://github.com/HKUDS/nanobot/pull/3961) | Yuxin-Lou | **Responses API 去重修复** — 转换后的 replay item ID 唯一化，防止 Codex 恢复会话时因重复 `rs_*` ID 拒绝请求 | ⭐⭐⭐ 阻断性 bugfix，关联 #3633 |
| [#3940](https://github.com/HKUDS/nanobot/pull/3940) | agbocsardi | **Kimi 推理参数冲突修复** — 移除 Moonshot API 下 `reasoning_effort` 与 `thinking` 的冗余并发，解决 `kimi-k2.5/k2.6` 400 错误 | ⭐⭐⭐ 关键兼容性修复，关联 Issue #3939 |
| [#3928](https://github.com/HKUDS/nanobot/pull/3928) | Hinotoi-agent | **SSRF 安全加固** — `web_fetch` 重定向目标二次校验，封堵内部网络跳转漏洞 | ⭐⭐⭐ 安全等级提升 |
| [#3929](https://github.com/HKUDS/nanobot/pull/3929) | HaisamAbbas | **图像提供商 HTTP 层统一** — MiniMax/AIHubMix 接入共享 HTTP helper，明确 Gemini base URL 配置 | ⭐⭐ 技术债清理 |
| [#3960](https://github.com/HKUDS/nanobot/pull/3960) | chengyongru | **`apply_patch` 精简重构** — 移除废弃的 unified-diff `patch` 模式，仅保留结构化 `edits` | ⭐⭐ API 简化，降低维护成本 |
| [#3957](https://github.com/HKUDS/nanobot/pull/3957) | Re-bin | **WebUI 文件编辑计数器修复** — 消除无可靠 diff 数据时的误导性计数，清理幽灵编辑占位 | ⭐⭐ 用户体验打磨 |
| [#3953](https://github.com/HKUDS/nanobot/pull/3953) | Re-bin | **侧边栏性能优化** — 大批量聊天历史分批渲染 + Cmd/Ctrl+K 搜索快捷键 | ⭐⭐⭐ 大规模用户核心痛点 |
| [#3951](https://github.com/HKUDS/nanobot/pull/3951) | Re-bin | **可折叠侧边栏重构** — 统一 DOM 结构避免 collapse 时图标漂移，固定主题切换按钮 | ⭐⭐ 交互细节优化 |

### 📊 整体推进度量

| 维度 | 进展 |
|:---|:---|
| **多模态能力** | 图像生成从"部分支持"跃升至"全提供商覆盖"（Ollama/OpenAI/Codex/MiniMax/Gemini 等） |
| **WebUI 工程** | 性能（大数据量渲染）、国际化（7 语种）、交互（导航/搜索）三线并进 |
| **API 兼容性** | 修复 2 个阻断级第三方 API 冲突（Anthropic 400、Moonshot 400） |
| **安全基线** | 封堵 1 个 SSRF 漏洞，重定向链全链路校验 |

---

## 4. 社区热点

### 🔥 讨论最活跃：Issue #3884 — WebUI 首条响应后会话自动关闭
- **链接**: [HKUDS/nanobot#3884](https://github.com/HKUDS/nanobot/issues/3884)
- **数据**: 6 条评论，0 👍，创建于 2026-05-17，关闭于 2026-05-22
- **诉求分析**: 用户在 Debian 网关+WebSocket 配置下遭遇会话中断，涉及 token 启用/禁用、stream 模式等多重变量组合。社区协作定位过程显示 **WebSocket 连接稳定性** 仍是自托管场景的脆弱环节，配置矩阵的测试覆盖不足。

### 🔥 新晋高关注：Issue #3959 — `/skill` 命令列出已禁用技能
- **链接**: [HKUDS/nanobot#3959](https://github.com/HKUDS/nanobot/issues/3959)
- **数据**: 4 条评论，0 👍，创建于 2026-05-22，仍开放
- **诉求分析**: 用户配置 `disabledSkills: ["weather"]` 后，`/skill` 仍列出 weather，暴露 **技能可见性与实际可用性状态不一致** 的设计缺陷。与同日提出的 #3958（将 weather 移出内置）形成呼应，社区对"技能系统瘦身"有强烈共识。

### 🔥 功能请求：Issue #3958 — Weather Skill 应转为示例而非内置
- **链接**: [HKUDS/nanobot#3958](https://github.com/HKUDS/nanobot/issues/3958)
- **数据**: 0 评论，0 👍，创建于 2026-05-22
- **诉求分析**: "lean and mean" 哲学驱动，用户希望核心保持精简，边缘功能通过示例文件夹可选安装。这与 PR #3963（CLI Apps 生态）的方向一致——**从"内置一切"转向"可插拔市场"**。

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | Fix PR | 链接 |
|:---|:---|:---|:---|:---|
| 🔴 **阻断** | Anthropic API 400：工具结果含 list 内容（如图片读取）导致永久错误 | **已修复** | #3956（同日关闭，推测已合入） | [#3956](https://github.com/HKUDS/nanobot/issues/3956) |
| 🔴 **阻断** | Moonshot `kimi-k2.5/k2.6` 拒绝同时包含 `thinking` + `reasoning_effort` 的请求 | **已修复** | #3940 | [#3939](https://github.com/HKUDS/nanobot/issues/3939) |
| 🟡 **高** | WebUI 首条响应后会话关闭（WebSocket 场景） | **已关闭** | 未明确关联 PR，推测在 WebUI 系列 PR 中间接修复 | [#3884](https://github.com/HKUDS/nanobot/issues/3884) |
| 🟡 **高** | 心跳机制重复创建定时任务，导致问候语重复发送、上下文丢失 | **开放** | ❌ 无 | [#3028](https://github.com/HKUDS/nanobot/issues/3028) |
| 🟢 **中** | `/skill` 列出已禁用技能，状态同步失效 | **开放** | ❌ 无（与 #3958 相关，可能合并处理） | [#3959](https://github.com/HKUDS/nanobot/issues/3959) |

> **风险评估**: #3028 心跳重复任务为 **v0.15 回归问题**，影响用户体验（骚扰式重复消息），且存在 1 个月以上，建议优先分配。

---

## 6. 功能请求与路线图信号

| 需求 | 来源 | 成熟度 | 纳入可能性 | 关键信号 |
|:---|:---|:---|:---|:---|
| **CLI Apps 生态/市场** | PR #3963 | 🔶 PR 评审中 | **高** | 作者 Re-bin 为核心贡献者，MVP 含安装/更新/卸载/测试全生命周期，对接 CLI-Anything 注册表 |
| **BM25-lite 技能路由** | PR #3865 | 🔶 开放 6 天，持续更新 | **中高** | 系统 prompt 降本 ~60%（3000+ tokens → top-5 技能），性能收益明确，需评估准确率回归 |
| **`nanobot doctor` 诊断命令** | PR #3776 | 🔶 开放 8 天 | **中** | 10 项自动化健康检查覆盖配置/权限/网络/API，运维体验提升，但非核心路径 |
| **Manifest LLM 路由支持** | PR #3568 | 🔶 开放 23 天 | **中低** | 网关型提供商接入，长期未获合并，可能因优先级或架构审查搁置 |
| **Ollama 图像生成** | Issue #3941 → PR #3946 | ✅ **已合并** | — | 本地部署刚需，24 小时内从需求到交付 |
| **Weather 技能外迁示例** | Issue #3958 | 🔴 刚提出 | **高** | 与 #3959 bug 联动，"lean and mean" 哲学获维护者认同，预计快速响应 |

**路线图推断**: 下一版本（推测 v0.16）核心主题可能是 **"可扩展性"** — CLI Apps 市场 + 技能动态路由 + 内置功能瘦身，形成"核心精简、生态繁荣"的架构转型。

---

## 7. 用户反馈摘要

### 💬 真实痛点

| 场景 | 来源 | 情绪 |
|:---|:---|:---|
| "心跳问候每天 9:00/14:00/19:00 重复发送，并没有达到读取上下文的需求" | #3028 | 😤 挫败 — 功能设计违背预期，且长期未修 |
| "配置 disabledSkills 后 /skill 仍列出 weather，感觉配置无效" | #3959 | 😕 困惑 — 状态反馈不透明 |
| "Gateway as service on Debian + WebSocket，conversation closes after first response" | #3884 | 😰 焦虑 — 自托管稳定性存疑 |
| "MEMORY.md 里'用户用中文交流'出现 10 次以上" | #3952 | 😩 冗余疲劳 — 记忆系统需智能去重 |

### ✅ 满意信号

- Ollama 图像生成从 Issue 提出到 PR 合并 **仅 2 天**，社区响应速度获认可
- WebUI 侧边栏性能优化系列（#3951/#3953/#3957）显示对大规模用户的持续关注

---

## 8. 待处理积压

| 项目 | 年龄 | 风险 | 行动建议 |
|:---|:---|:---|:---|
| **Issue #3028** 心跳重复创建定时任务 | 🔴 **42 天** | v0.15 回归，用户骚扰体验，关联长期记忆上下文丢失 | 立即分配，优先级 P1 |
| **PR #3568** Manifest LLM 路由支持 | 🔴 **23 天** | 网关生态位竞争，长期搁置可能流失贡献者 | 明确拒绝或提供合并时间表 |
| **PR #3865** BM25-lite 技能路由 | 🟡 **7 天** | 性能收益显著但需准确率验证，社区期待高 | 安排 benchmark 评审，2 周内决策 |
| **PR #3776** nanobot doctor | 🟡 **9 天** | 运维体验提升，但非紧急 | 可纳入下一版本规划，明确 milestone |

---

> **健康度评分**: 🟢 活跃（PR/Issue 流转快，关键 bug 当日修复）| 🟡 需关注（#3028 长期未修，技能系统状态一致性债务）| 整体趋势 **向上**

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 项目动态日报

**日期**: 2026-05-23  
**项目**: [NousResearch/hermes-agent](https://github.com/Nousresearch/hermes-agent)  
**数据周期**: 过去 24 小时

---

## 1. 今日速览

Hermes Agent 昨日保持**极高活跃度**，Issues 和 PR 各更新 50 条，但**合并/关闭率偏低**（Issues 关闭率 12%，PR 合并/关闭率仅 10%），显示社区贡献活跃但代码审查吞吐存在瓶颈。无新版本发布，项目处于 v0.14.0 的密集修 bug 周期。值得关注的是，单日出现 3 个 P1 级严重 Bug（技能安装完全失效、Telegram 网关路由断裂、Codex 响应状态误映射），以及 2 个 P2 级基础设施问题（Docker 镜像依赖缺失、Matrix 网关加密包缺失），稳定性压力显著上升。国际化和插件扩展生态（TTS/STT/LLM 提供商）成为功能开发主线。

---

## 2. 版本发布

**无新版本发布**

当前最新版本仍为 v0.14.0（commit `ba9964ff0`, 2026-05-21）。

---

## 3. 项目进展

### 已合并/关闭的 PR（5 条中的关键项）

| PR | 作者 | 内容 | 影响 |
|:---|:---|:---|:---|
| [#30495](https://github.com/NousResearch/hermes-agent/pull/30495) | ilonagaja509-glitch | 修复 emoji 扫描器误拦截 ZWJ 字符（零宽连接符） | 解决 #12673，恢复完整 emoji 支持 |
| [#30496](https://github.com/NousResearch/hermes-agent/pull/30496) | ilonagaja509-glitch | 网关进度消息去重键改为截断前原文 | 修复 #24298，避免长命令前缀相同导致的误去重 |

**整体评估**: 昨日合并 PR 数量极少（仅 2 条可见关闭，且均为小型修复），45 个待合并 PR 堆积，**代码审查管道明显拥堵**。功能型 PR（如 i18n、新提供商接入、Tlon 适配扩展）均处于等待状态，v0.14.x 的迭代节奏受限于维护者带宽。

---

## 4. 社区热点

### 🔥 讨论最活跃的 Issues

| 排名 | Issue | 评论 | 核心诉求 |
|:---|:---|:---|:---|
| 1 | [#26847](https://github.com/NousResearch/hermes-agent/issues/26847) xAI OAuth 403 错误 | **15 评论** | **付费用户权益争议**：标准 SuperGrok 订阅者（$30/月）被 xAI 后端错误拒绝，文档声称全层级支持但实际强制 Heavy-only，用户要求澄清服务边界或修复后端策略 |
| 2 | [#2706](https://github.com/NousResearch/hermes-agent/issues/2706) 响应截断问题 | 11 评论 | 长期存在的输出长度限制问题，昨日关闭，社区关注自动回滚机制的可靠性 |
| 3 | [#29125](https://github.com/NousResearch/hermes-agent/issues/29125) Claude CLI 兼容性 | 9 评论 | **生态互操作性**：用户期望通过 Claude CLI 直接调用 Hermes，但认证流程断裂，反映"AI 工具链拼接"场景的需求张力 |

### 诉求分析

- **#26847** 背后是 **B2C 订阅商业模式的技术-商业脱节**：xAI 的 OAuth 策略与文档承诺不一致，Hermes 作为中间层被迫承担用户投诉压力，需与 xAI 协调或明确降级方案。
- **#29125** 反映 **"CLI 统一入口"趋势**：用户不希望记忆多个工具的认证方式，期望 Hermes 成为底层引擎、Claude CLI 作为交互前端，这要求更标准化的 MCP/插件协议支持。

---

## 5. Bug 与稳定性

### P1（严重）— 需立即响应

| Issue | 描述 | 状态 | Fix PR |
|:---|:---|:---|:---|
| [#30482](https://github.com/NousResearch/hermes-agent/issues/30482) | **官方技能安装完全失效**：skills index 中 81 个官方技能的 `repo` 字段为空，所有 `official/<skill>` 安装失败 | 新报，无回复 | ❌ 无 |
| [#30411](https://github.com/NousResearch/hermes-agent/issues/30411) | **Telegram DM 路由断裂**：`_recover_telegram_topic_thread_id()` 导致消息被错误 pin 到旧话题，自动重命名失效 | 新报，无回复 | ❌ 无 |
| [#27988](https://github.com/NousResearch/hermes-agent/issues/27988) | **Codex 响应状态误映射**：Azure Foundry 上 `final_answer` 被错误标记为 `incomplete`，导致提前终止 | 5 天前，1 评论 | ❌ 无 |
| [#17182](https://github.com/NousResearch/hermes-agent/issues/17182) | **配置迁移破坏性重置**：`terminal.cwd` 和 `auxiliary.*.model` 在升级后被清空 | 24 天前，1 评论 | ❌ 无 |

### P2（高优先级）

| Issue | 描述 | 状态 | Fix PR |
|:---|:---|:---|:---|
| [#30399](https://github.com/NousResearch/hermes-agent/issues/30399) | **Docker 镜像缺失 Matrix 加密依赖**：`mautrix[encryption]` 未预装，只读 rootfs 无法补救 | 新报 | ✅ [#30504](https://github.com/NousResearch/hermes-agent/pull/30504) 已开 |
| [#16703](https://github.com/NousResearch/hermes-agent/issues/16703) | **Docker-out-of-Docker 代码执行失败**：`docker version` 检测在 DooD 场景下失效 | 26 天前，3 评论 | ❌ 无 |
| [#7069](https://github.com/NousResearch/hermes-agent/issues/7069) | **本地 LLM 无限重试循环**：prefill 超 stream timeout 后进入死循环 | 43 天前，3 评论 | ❌ 无 |
| [#30417](https://github.com/NousResearch/hermes-agent/issues/30417) | **Dispatcher 三级韧性缺陷**：确定性崩溃循环、SQLite I/O 锁、归档父任务静默提升子任务 | 新报，2 评论 | ❌ 无 |

### P3（一般）

| Issue | 描述 | Fix PR |
|:---|:---|:---|
| [#30218](https://github.com/NousResearch/hermes-agent/issues/30218) | SSH 下 OSC 11 颜色响应泄漏到 CLI 输入 | ❌ 无 |
| [#30083](https://github.com/NousResearch/hermes-agent/issues/30083) | TUI Ask 工具不支持粘贴 | ❌ 无 |
| [#28844](https://github.com/NousResearch/hermes-agent/issues/28844) | Kanban 数据库初始化顺序错误（索引先于列存在） | ❌ 无 |

**稳定性健康度**: ⚠️ **承压**。4 个 P1 中 3 个为新报且无任何修复响应，#30482 是**服务可用性事故**（核心功能完全失效），#30411 影响 Telegram 网关核心路由逻辑。Docker 镜像的依赖管理出现系统性漏洞（#30399、#30504 关联）。

---

## 6. 功能请求与路线图信号

| 需求 | Issue/PR | 纳入可能性 | 判断依据 |
|:---|:---|:---|:---|
| **11 语言国际化** | PR [#30492](https://github.com/NousResearch/hermes-agent/pull/30492) | ⭐⭐⭐⭐⭐ 高 | 已完整实现，覆盖 17 个文件、11 种语言，只差合并 |
| **ntfy 消息推送** | Issue [#13866](https://github.com/NousResearch/hermes-agent/issues/13866) + PR [#4043](https://github.com/NousResearch/hermes-agent/pull/4043) | ⭐⭐⭐⭐⭐ 高 | 自托管/气隙场景刚需，PR 已开 53 天，功能完整 |
| **STT 插件扩展点** | PR [#30493](https://github.com/NousResearch/hermes-agent/pull/30493) | ⭐⭐⭐⭐☆ 高 | 镜像 TTS 插件架构，设计一致，易于审查 |
| **Ambient LLM 提供商** | PR [#30111](https://github.com/NousResearch/hermes-agent/pull/30111) | ⭐⭐⭐⭐☆ 高 | 带加密证明的 AI 基础设施差异化卖点 |
| **云配置同步** | Issue [#20510](https://github.com/NousResearch/hermes-agent/issues/20510) | ⭐⭐⭐☆☆ 中 | 6 👍 社区支持强，但涉及安全架构，需设计评审 |
| **Kanban 指派人为下拉菜单** | Issue [#30437](https://github.com/NousResearch/hermes-agent/issues/30437) | ⭐⭐⭐☆☆ 中 | UI 改进，实现简单，但优先级可能被核心稳定性压制 |
| **"璇玑"基因网络自进化** | Issue [#30428](https://github.com/NousResearch/hermes-agent/issues/30428) | ⭐☆☆☆☆ 低 | 高度抽象的研究提案，缺乏与现有架构的对接路径，更可能作为独立 fork |

**路线图信号**: 插件生态标准化（TTS→STT→image_gen→transcription）和国际化是 v0.15.0 的明确方向；自托管消息推送（ntfy）补齐了企业/隐私场景的最后一块拼图。

---

## 7. 用户反馈摘要

### 核心痛点

| 场景 | 来源 | 情绪 |
|:---|:---|:---|
| **"升级即破坏"恐惧** | #17182: 配置迁移重置关键字段 | 😤 愤怒 |
| **Docker 镜像"半成品"体验** | #30399, #16703, #18482: 依赖缺失、权限错误、DooD 不支持 | 😤 愤怒 |
| **第三方服务策略不透明** | #26847: 付费后仍 403，文档与实现脱节 | 😤 愤怒 |
| **多配置文件隔离失效** | #4587, #30444: 进程 kill 和 resume 提示跨 profile 污染 | 😠 沮丧 |
| **TUI 粘贴体验断裂** | #24860, #30083: Ctrl+V 和图片粘贴均不支持 | 😠 沮丧 |

### 满意点

- **插件扩展机制受认可**：#26241（FAL 迁移）、#30493（STT 扩展点）显示开发者愿意基于插件架构贡献
- **多平台网关覆盖广**：Telegram、Discord、Matrix、Slack、飞书、企业微信均有支持，尽管个别有 bug

### 关键使用场景

> "运行 Hermes 在 NAS/私有 VPS/气隙环境" — #13866  
> "PC 和笔记本之间同步配置" — #20510  
> "通过 Claude CLI 统一入口使用 Hermes 引擎" — #29125

---

## 8. 待处理积压

### 长期未响应的高价值项

| Issue/PR | 创建时间 | 天数 | 风险 |
|:---|:---|:---|:---|
| PR [#4043](https://github.com/NousResearch/hermes-agent/pull/4043) ntfy 适配 | 2026-03-30 | **54 天** | 功能完整但无人审查，社区自托管需求被阻塞 |
| Issue [#7069](https://github.com/NousResearch/hermes-agent/issues/7069) 无限重试循环 | 2026-04-10 | **43 天** | 本地 LLM 核心体验问题，3 评论无维护者介入 |
| PR [#25345](https://github.com/NousResearch/hermes-agent/pull/25345) Android 浏览器移交 | 2026-05-14 | **9 天** | 移动端场景，已 rebase 待审 |
| PR [#26300](https://github.com/NousResearch/hermes-agent/pull/26300) Tlon 适配扩展 | 2026-05-15 | **8 天** | 去中心化社交网络集成，设计复杂需专门 review |
| Issue [#4587](https://github.com/NousResearch/hermes-agent/issues/4587) 多 profile 安全性 | 2026-04-02 | **51 天** | 架构级缺陷，3 评论无方案，影响企业多租户场景 |

### 维护者行动建议

1. **立即**: 指派 #30482（技能安装失效）和 #30411（Telegram 路由）的修复责任人，考虑 hotfix
2. **本周**: 合并 #30504（Docker 依赖修复）和 #30492（i18n），释放社区贡献动能
3. **本月**: 建立 P1/P2 问题的 48 小时首次响应 SLA，当前多个严重 bug 零回复损害项目信誉

---

*日报生成基于 GitHub 公开数据，未包含私有讨论或安全披露内容。*

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

PicoClaw 今日呈现**高活跃度维护态势**：6 条陈旧 Issue 被集中清理，22 条 PR 中有 9 条完成合并/关闭，13 条待审阅。项目发布 `v0.2.8-nightly.20260522` 夜间构建，持续迭代节奏稳定。值得注意的是，社区贡献者 `bogdanovich` 的 5 条 Telegram 相关 PR 被批量关闭，可能反映维护策略调整或功能合并路径变化。整体健康度良好，但需关注核心功能 PR #2906（消息总线背压处理）的审阅进度。

---

## 2. 版本发布

### 🌙 Nightly Build: v0.2.8-nightly.20260522.5bbebb5f

| 属性 | 详情 |
|:---|:---|
| 发布日期 | 2026-05-22 |
| 构建类型 | 自动化夜间构建（可能不稳定） |
| 对比基准 | [v0.2.8...main](https://github.com/sipeed/picoclaw/compare/v0.2.8...main) |

**⚠️ 注意事项**：此为自动化构建，建议仅用于测试环境，生产环境请等待正式版本。

**迁移建议**：当前稳定版仍为 v0.2.8，夜间构建包含 main 分支最新提交，主要覆盖近期合并的 Telegram 修复、会话时间戳、请求上下文策略等特性。

---

## 3. 项目进展

### ✅ 今日合并/关闭的重要 PR

| PR | 作者 | 核心贡献 | 状态 |
|:---|:---|:---|:---|
| [#2921](https://github.com/sipeed/picoclaw/pull/2921) | dependabot[bot] | 升级 `gronx` 定时任务库 1.19.7 → 1.20.0 | 已关闭 |
| [#2923](https://github.com/sipeed/picoclaw/pull/2923) | dependabot[bot] | 升级 LINE Bot SDK v8 8.19.0 → 8.20.0 | 已关闭 |
| [#2914](https://github.com/sipeed/picoclaw/pull/2914) | lxowalle | **新增请求级上下文策略** (`agents.defaults.turn_profile`)，支持按 turn 控制历史、系统上下文、技能提示和工具调用 | 已关闭 |
| [#2812](https://github.com/sipeed/picoclaw/pull/2812) | moltenbot000 | 根目录 Dockerfile（AI 辅助生成，经人工审阅） | 已关闭 |
| [#2779](https://github.com/sipeed/picoclaw/pull/2779) | bogdanovich | Telegram 论坛主题级触发器覆盖 (`group_trigger` 按 topic 配置) | 已关闭 |
| [#2778](https://github.com/sipeed/picoclaw/pull/2778) | bogdanovich | `working_summary` 工具反馈样式（聊天频道进度提示） | 已关闭 |
| [#2777](https://github.com/sipeed/picoclaw/pull/2777) | bogdanovich | 抑制定时任务的后台反馈消息（避免 cron 任务干扰聊天） | 已关闭 |
| [#2776](https://github.com/sipeed/picoclaw/pull/2776) | bogdanovich | 修复 Telegram 主题回复的 typing 状态清理 | 已关闭 |
| [#2772](https://github.com/sipeed/picoclaw/pull/2772) | bogdanovich | 保留 Telegram 论坛主题的 `message` 工具路由 | 已关闭 |

**关键里程碑**：
- **运行时策略引擎**：PR #2914 的合并标志着 PicoClaw 获得细粒度 turn 级上下文控制能力，为多 Agent 协作和资源优化奠定基础
- **Telegram 生态完善**：7 条 PR 覆盖论坛主题、消息路由、反馈抑制等场景，Telegram 渠道成熟度显著提升

---

## 4. 社区热点

### 🔥 讨论最活跃的 Issues

| 排名 | Issue | 评论数 | 核心诉求 | 状态 |
|:---|:---|:---:|:---|:---|
| 1 | [#629](https://github.com/sipeed/picoclaw/issues/629) LLM 调用失败未重试 | **15** | 长任务中 HTTP 500 导致挂死，需指数退避重试机制 | ✅ 已关闭 |
| 2 | [#2775](https://github.com/sipeed/picoclaw/issues/2775) 子 Agent 继承根 AGENT.md 致角色混淆 | 4 | 多 Agent 架构中 `Planner`/`Builder` 等子角色应加载独立系统提示 | ✅ 已关闭 |
| 3 | [#2702](https://github.com/sipeed/picoclaw/issues/2702) 群聊历史缺少发送者归因 | 4 | Discord 等多用户频道中，历史消息需保留 `sender_id` 避免上下文混淆 | ✅ 已关闭 |

**诉求分析**：
- **可靠性焦虑**（#629）：生产环境长任务稳定性是核心痛点，15 条评论反映社区对 LLM 调用韧性的高度关注
- **多 Agent 架构成熟度**（#2775）：用户正在构建复杂 Agent 流水线，但角色隔离机制不足制约了架构扩展
- **多用户场景精细化**（#2702）：从单用户对话向群组/团队协作演进，会话管理需支持身份维度

---

## 5. Bug 与稳定性

| 严重程度 | Issue | 描述 | Fix PR | 状态 |
|:---|:---|:---|:---|:---|
| 🔴 **高** | [#629](https://github.com/sipeed/picoclaw/issues/629) | LLM 调用失败（HTTP 500）无重试，长任务永久挂死 | 未明确关联 | ✅ 已关闭（需验证修复方案） |
| 🟡 **中** | [#2798](https://github.com/sipeed/picoclaw/issues/2798) | Telegram PDF 附件导致流/会话中断（OpenClaw 正常，PicoClaw 特有） | [#2856](https://github.com/sipeed/picoclaw/pull/2856) 媒体附件支持 | ✅ 已关闭 |
| 🟡 **中** | [#2795](https://github.com/sipeed/picoclaw/issues/2795) | 对话历史仅显示最后一条用户消息（会话压缩过度） | 未明确关联 | ✅ 已关闭 |
| 🟡 **中** | [#2787](https://github.com/sipeed/picoclaw/issues/2787) | 消息缺少独立时间戳，全部使用 `session.updated` | [#2788](https://github.com/sipeed/picoclaw/pull/2788) | ✅ 已关闭 |
| 🟡 **中** | [#2702](https://github.com/sipeed/picoclaw/issues/2702) | 群聊默认会话作用域历史消息无发送者标识 | 未明确关联 | ✅ 已关闭 |

**稳定性评估**：今日关闭的 6 条 Issue 均为陈旧积压，涉及核心可靠性（重试）、数据准确性（时间戳、历史完整性）、渠道兼容性（Telegram PDF）。建议维护者确认 #629 的具体修复提交，该问题直接影响生产可用性。

---

## 6. 功能请求与路线图信号

| 需求来源 | 功能方向 | 成熟度信号 | 纳入可能性 |
|:---|:---|:---|:---|
| PR [#2914](https://github.com/sipeed/picoclaw/pull/2914) | 请求级上下文策略 | ✅ 已合并 | **v0.2.9 核心功能** |
| PR [#2788](https://github.com/sipeed/picoclaw/pull/2788) | 单消息时间戳 | 🔄 待合并 | 高（前端刚需） |
| PR [#2856](https://github.com/sipeed/picoclaw/pull/2856) | 媒体附件与富文本消息 | 🔄 待合并 | 高（解决 #2798） |
| PR [#2838](https://github.com/sipeed/picoclaw/pull/2838) | AGENT.md 工具策略过滤器（allow/deny/glob） | 🔄 待合并 | 中高（多 Agent 安全） |
| Issue [#2775](https://github.com/sipeed/picoclaw/issues/2775) | 子 Agent 独立角色提示 | ❓ 无关联 PR | 中（架构级需求） |

**路线图预测**：v0.2.9 可能聚焦**运行时可控性**（上下文策略 + 工具过滤）与**消息系统完善**（时间戳 + 媒体）。多 Agent 角色隔离（#2775）虽需求明确，但涉及架构调整，可能排期至 v0.3.x。

---

## 7. 用户反馈摘要

### 😫 核心痛点

| 场景 | 反馈来源 | 具体表现 |
|:---|:---|:---|
| **长任务可靠性** | #629 评论 | "Run a long task → Server may return HTTP 500 sometimes → Task **hang without retry**" — 生产环境不可接受 |
| **调试透明度** | #2787, #2795 | 前端被迫用不准确的时间戳、用户看不到完整历史，**数据层与表现层脱节** |
| **多 Agent 角色混乱** | #2775 | 所有子 Agent 自认是根 Agent，**"不是各自的角色"**，导致输出风格/职责错位 |
| **Telegram 兼容性** | #2798 | 同一 PDF 在 OpenClaw 正常、PicoClaw 崩溃，**渠道实现质量参差** |

### 👍 满意方向

- Docker 支持（#2812）：开发者部署门槛降低
- Telegram 论坛主题精细化（#2772-#2779）：复杂群组场景可用性提升

---

## 8. 待处理积压

### ⚠️ 需维护者重点关注

| PR/Issue | 积压天数 | 风险 | 行动建议 |
|:---|:---:|:---|:---|
| [#2906](https://github.com/sipeed/picoclaw/pull/2906) **消息总线背压处理** | 2 天 | 🔴 **高** — 生产负载下 goroutine 泄漏、无限阻塞 | 优先审阅，关联 improvement-report.md 第 3 项 |
| [#2662](https://github.com/sipeed/picoclaw/pull/2662) 提供商文档统一 | 29 天 | 🟡 中 — 文档债务累积 | 分配文档维护者 |
| [#2838](https://github.com/sipeed/picoclaw/pull/2838) 工具策略过滤器 | 12 天 | 🟡 中 — 安全相关，多 Agent 场景刚需 | 评估与 #2914 的协同 |
| [#2856](https://github.com/sipeed/picoclaw/pull/2856) 媒体附件支持 | 11 天 | 🟡 中 — 阻塞 #2798 类问题彻底解决 | 测试覆盖 Telegram PDF 场景 |

**健康度警示**：13 条待合并 PR 中，Dependabot 占 6 条（46%），核心功能 PR 审阅周期偏长。建议建立 P1/P2 优先级标签，避免基础设施改进淹没在依赖更新中。

---

*本日报基于 GitHub 公开数据生成，时间范围：2026-05-22 至 2026-05-23*

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目动态日报 | 2026-05-23

---

## 1. 今日速览

NanoClaw 今日呈现**高活跃度、多线程并行推进**态势。过去24小时内，6条全新 Issues 全部聚焦 Apple Container 与 Signal 认证通道的稳定性缺陷，显示 macOS 部署路径正经历集中压力测试；18条 PR 更新中 8 条完成合并/关闭，核心贡献者 `shakhruz` 的 8 个历史 PR 批量落地，涵盖 MCP 工具生态（Gmail/Calendar/Todoist/文件发送）与容器技能集。与此同时，`chiptoe-svg` 主导的 Codex 替代方案（对抗 Claude Code 单一依赖）形成 4 个关联 PR 的完整技术栈，`snymanpaul` 则同步推进 Signal 通道的兼容性修复。项目处于**功能扩张期与基础设施债务偿还期叠加**的阶段，Apple Container 分支的技术债问题尤为突出。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭 PR（8 条）

| PR | 作者 | 核心贡献 | 项目推进意义 |
|:---|:---|:---|:---|
| [#1781](https://github.com/nanocoai/nanoclaw/pull/1781) | shakhruz | **Composio MCP 托管 OAuth**：以 `COMPOSIO_API_KEY` 环境变量切换 Gmail/Calendar 的 OAuth 模式，替代手动 GCP 配置；降级时回退至 legacy npx 方案 | 大幅降低终端用户配置门槛，MCP 生态从"开发者工具"向"产品化"跃迁 |
| [#1780](https://github.com/nanocoai/nanoclaw/pull/1780) | shakhruz | **5 个容器技能**：client-profile（客户画像）、design-avatar（头像生成）、telegram-ads（Telegram 广告）、olx-research/olx-ad-generator（OLX 平台研究+广告生成） | 首次规模化覆盖营销自动化场景，验证"容器技能"商业模式可行性 |
| [#1757](https://github.com/nanocoai/nanoclaw/pull/1757) | shakhruz | **send_file MCP 工具**：容器向聊天会话回传文件，图片内联渲染、其他类型作为文档附件，自动路径解析 `/workspace/group/...` → host | 补齐容器 agent 与用户交互的最后一块拼图，多模态输出闭环 |
| [#1756](https://github.com/nanocoai/nanoclaw/pull/1756) | shakhruz | **router XML 格式补全 message id**：`formatMessages()` 输出 `<message id="...">`，使 `react_to_message` MCP 工具可精准引用历史消息 | 修复消息引用系统的根基缺陷，反应类交互可靠性提升 |
| [#1749](https://github.com/nanocoai/nanoclaw/pull/1749) | shakhruz | **agent-runner 缓存全文件校验**：从仅检查 `index.ts` mtime 扩展至所有 `.ts` 文件，消除子模块修改后的静默陈旧问题 | 消除一类隐蔽的开发-生产不一致 bug，容器热更新机制健全化 |
| [#1747](https://github.com/nanocoai/nanoclaw/pull/1747) | shakhruz | **Todoist MCP 集成**：任务列表、搜索、创建、更新、完成 | 个人生产力工具链补全，与 Google Calendar MCP 形成"时间+任务"双轴 |
| [#1737](https://github.com/nanocoai/nanoclaw/pull/1737) | shakhruz | **Google Calendar MCP 集成**：事件的 CRUD 操作 | 企业场景日历自动化基础能力 |
| [#1735](https://github.com/nanocoai/nanoclaw/pull/1735) | shakhruz | **Apple Container 三 bug 修复**：凭证代理 wiring、环境变量加载、launchd PATH 修复 | 首次打通 macOS Apple Container 端到端路径（/setup → /convert-to-apple-container → Telegram 消息可达）|

**整体评估**：今日合并批次标志着 NanoClaw 从"Claude 专属生态"向**多模型、多平台、多场景**的泛化 AI Agent 基础设施演进。MCP 工具数量从 0 扩展至 6+（Gmail/Calendar/Todoist/Composio/Telegram Scanner/send_file），容器技能从原型进入垂直行业（营销）验证。

---

## 4. 社区热点

### 最活跃讨论集群：Apple Container 技术债爆发（6 条 Issues 中的 4 条）

| Issue | 链接 | 热度分析 |
|:---|:---|:---|
| [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) | `skill/apple-container` 分支与主线严重脱节 | **结构性危机信号**：分支引用已删除 API、导入不存在模块、假设已废弃的 Node+tsc 运行时（主线已迁移至 bun）。`/convert-to-apple-container` 技能文档化存在但**实际不可运行**，用户信任损耗风险 |
| [#2587](https://github.com/nanocoai/nanoclaw/issues/2587) | Dockerfile 残留 `npm run build`，agent-runner 无 build script | **迁移遗漏**：主线 bun 迁移后，技能分支构建脚本未同步更新，CI/CD 或分支管理流程存在盲区 |
| [#2589](https://github.com/nanocoai/nanoclaw/issues/2589) | `host.docker.internal` 在 microVM 内不可解析 | **平台抽象泄漏**：Apple Container 网络模型与 Docker Desktop 假设冲突，且不支持 `--add-host` 注入，需重新设计服务发现机制 |
| [#2583](https://github.com/nanocoai/nanoclaw/issues/2583) | `launchctl kickstart -k` 对未加载 plist 静默无操作 | **可靠性陷阱**：服务重启语义在 macOS 上未覆盖"冷启动"场景，错误处理缺失 |

**背后诉求**：macOS 开发者群体（尤其 Apple Silicon 原生部署需求）正在快速增长，但项目对 Apple Container 的维护投入明显滞后于主线迭代。`shakhruz` 的 #1735 虽修复了 3 个阻塞点，但未解决分支同步的根本流程问题。

---

## 5. Bug 与稳定性

| 严重程度 | Issue/PR | 描述 | Fix PR 状态 |
|:---|:---|:---|:---|
| **🔴 P0 - 功能完全不可用** | [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) | `skill/apple-container` 分支与主线 API 不兼容，`/convert-to-apple-container` 立即失败 | ❌ 无 Fix PR，需分支重构或废弃 |
| **🔴 P0 - 功能完全不可用** | [#2587](https://github.com/nanocoai/nanoclaw/issues/2587) | Dockerfile 构建失败，agent-runner 无 `build` script | ❌ 无 Fix PR，单行修复即可 |
| **🟡 P1 - 平台特性缺失** | [#2589](https://github.com/nanocoai/nanoclaw/issues/2589) | Apple Container 内无法解析 `host.docker.internal`，OneCLI 代理 URL 失效 | ❌ 无 Fix PR，需设计替代方案（如 Unix socket、固定 IP） |
| **🟡 P1 - 静默失败/状态不一致** | [#2583](https://github.com/nanocoai/nanoclaw/issues/2583) | `restartService` 对未加载服务静默无操作，用户误以为已重启 | ❌ 无 Fix PR，需改为 `launchctl bootstrap` 或前置 load 检查 |
| **🟡 P1 - 死锁/无超时** | [#2582](https://github.com/nanocoai/nanoclaw/issues/2582) | `signal-auth listAccounts` 在 signal-cli daemon 持有锁时死锁 | ❌ 无 Fix PR，需添加 `spawnSync` timeout 或异步化 |
| **🟢 P2 - 兼容性断裂** | [#2581](https://github.com/nanocoai/nanoclaw/issues/2581) | signal-cli ≥0.13 JSON 字段 `account` → `number` 变更，误判为未认证 | ✅ **[#2584](https://github.com/nanocoai/nanoclaw/pull/2584)** 已提交，待合并 |
| **🟢 P2 - 认证状态残留** | [#2579](https://github.com/nanocoai/nanoclaw/pull/2579) | WhatsApp 401 强制登出后，磁盘凭证未清理，重启后重复失败 | ✅ PR 已提交，待合并 |

**稳定性健康度**：Signal 通道处于**兼容性阵痛期**（CLI 工具升级导致字段变更、锁机制冲突），WhatsApp 通道存在**认证状态机缺陷**。Apple Container 为**系统性技术债**，非单点修复可解决。

---

## 6. 功能请求与路线图信号

| 方向 | 载体 | 信号强度 | 纳入下一版本概率 |
|:---|:---|:---|:---|
| **Codex 作为一等公民** | [#2580](https://github.com/nanocoai/nanoclaw/pull/2580) 完整 Codex-only 安装、[#2474](https://github.com/nanocoai/nanoclaw/pull/2474) AI-coding-CLI 选择器、[#2361](https://github.com/nanocoai/nanoclaw/pull/2361) Codex provider 契约、[#2337](https://github.com/nanocoai/nanoclaw/pull/2337) 技能目录泛化 | ⭐⭐⭐⭐⭐ | **极高**（4 个关联 PR 形成完整技术栈，已覆盖安装、provider、技能发现、凭证管理全链路） |
| **Telegram 官方通道** | [#2585](https://github.com/nanocoai/nanoclaw/pull/2585) grammy 库集成，支持文本/媒体/命令/输入指示器 | ⭐⭐⭐⭐⭐ | **极高**（PR 完整度高，含单元测试；与现有 Telegram Scanner MCP 形成互补——前者是通道，后者是工具） |
| **视频生成（Edna/Veo 3.1）** | [#2532](https://github.com/nanocoai/nanoclaw/pull/2532) 生成+拼接+入站媒体（Slack） | ⭐⭐⭐⭐☆ | **高**（有正式技术计划文档 `docs/plans/2026-05-17-001-feat-edna-video-generation-plan.md`，但代码量较大，审核周期可能较长） |
| **会话 transcript 生命周期管理** | [#2586](https://github.com/nanocoai/nanoclaw/pull/2586) 超大/旧会话 transcript 轮转 | ⭐⭐⭐⭐☆ | **高**（解决长期运行生产环境的磁盘与性能瓶颈，问题描述清晰，方案符合 SDK 设计模式） |
| **chat-sdk-bridge 文本变换补全** | [#2523](https://github.com/nanocoai/nanoclaw/pull/2523) `transformOutboundText` 覆盖 `ask_question` 和 card 路径 | ⭐⭐⭐☆☆ | **中**（修复类 PR，跟随现有模式扩展，技术债务清偿性质） |

**路线图判断**：项目正执行**"去 Claude 中心化"**战略，Codex 替代方案从实验性进入产品化阶段；通道层从 Signal/WhatsApp 双寡头向 **Telegram 三足鼎立**扩展；媒体能力从文本/图片向**视频生成**跃迁。

---

## 7. 用户反馈摘要

### 真实痛点（从 Issues 提炼）

| 场景 | 痛点 | 情绪强度 |
|:---|:---|:---|
| **macOS 开发者尝试 Apple Container 部署** | "按文档执行 `/convert-to-apple-container`，结果立即失败" → 分支与主线脱节、构建脚本不存在、网络解析失败 | 😤 **挫败感极高**，文档与代码不一致是最具破坏性的体验 |
| **Signal 长期用户升级 CLI** | "signal-cli 升级后一直提示未认证，重新链接也无效" → JSON 字段变更导致误判 | 😠 **困惑与重复劳动**，工具升级不应破坏现有认证状态 |
| **Signal 服务维护者** | "重启命令看起来执行了，实际服务没起来" → `launchctl kickstart` 静默失败 | 😐 **信任侵蚀**，运维操作缺乏反馈 |

### 满意点（从合并 PR 反推）

- MCP 工具链的"零配置 OAuth"（Composio）降低企业采用门槛
- 容器技能的垂直场景覆盖（营销自动化）显示生态活力
- 文件发送与消息引用修复补齐交互完整性

---

## 8. 待处理积压

| 类型 | 项目 | 创建时间 | 当前状态 | 风险提示 |
|:---|:---|:---|:---|:---|
| **长期 Open PR** | [#2523](https://github.com/nanocoai/nanoclaw/pull/2523) chat-sdk-bridge 文本变换 | 2026-05-17 | 5 天未合并，今日有更新 | 中等风险，修复类 PR，可能因审核队列积压 |
| **长期 Open PR** | [#2361](https://github.com/nanocoai/nanoclaw/pull/2361) Codex provider 契约收紧 | 2026-05-09 | 14 天未合并 | **高风险**，阻塞 #2580 等下游 PR 的代码质量基准 |
| **长期 Open PR** | [#2337](https://github.com/nanocoai/nanoclaw/pull/2337) 技能目录泛化 | 2026-05-07 | 16 天未合并 | **高风险**，同样阻塞 Codex 全链路，跨 provider 兼容性基础设施 |
| **技术债集群** | Apple Container 分支（#2588/#2587/#2589） | 2026-05-22 | 全新报告，无 Fix PR | **紧急**，macOS 部署路径名义上存在、实际上不可用，建议维护者评估是否冻结该技能直至主线同步流程建立 |
| **安全/可靠性** | [#2582](https://github.com/nanocoai/nanoclaw/issues/2582) signal-auth 死锁 | 2026-05-21 | 有诊断，无 PR | 生产环境 Signal 通道可能在特定时序下完全卡死 setup 流程 |

---

**日报生成时间**：2026-05-23  
**数据来源**：NanoClaw GitHub 仓库（github.com/qwibitai/nanoclaw）公开活动流

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw 项目动态日报 | 2026-05-23

> **项目地址**: [github.com/nullclaw/nullclaw](https://github.com/nullclaw/nullclaw)

---

## 1. 今日速览

NullClaw 今日活跃度**偏低**，过去24小时无 Issues 更新，无版本发布，3条 PR 均处于待合并状态且最新更新集中在 5月21-22日。项目当前呈现**"维护窗口期"特征**——社区讨论沉寂，但核心贡献者仍在推进技术债务清理（POSIX 线程调度、网络传输错误处理）和 Cron 子系统重大功能开发。整体健康度需关注 PR 合并节奏：3条 PR 平均已开放 **37 天**，存在明显的代码审查瓶颈。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

**今日无合并/关闭的 PR**

以下 3 条 PR 持续开放中，代表项目当前三条并行推进线：

| PR | 方向 | 开放天数 | 最新活动 | 链接 |
|:---|:---|:---|:---|:---|
| #891 | 网络层稳定性修复 | 18 天 | 5-22 更新 | [nullclaw/nullclaw#891](https://github.com/nullclaw/nullclaw/pull/891) |
| #878 | 运行时线程调度修复 | 23 天 | 5-22 更新 | [nullclaw/nullclaw/pull/878](https://github.com/nullclaw/nullclaw/pull/878) |
| #783 | Cron 子系统重大功能 | 46 天 | 5-21 更新 | [nullclaw/nullclaw/pull/783](https://github.com/nullclaw/nullclaw/pull/783) |

**技术进展分析**：
- **#891** 解决 OpenAI 兼容 provider 的健康探针场景下，curl 传输层错误被过度聚合的问题，将 `CurlDnsError`、`CurlConnectError`、`CurlTimeout` 等 8 类错误直接透传——这对生产环境故障定位至关重要
- **#878** 修复 `std_compat.thread.sleep()` 在 POSIX 系统下使用协作式 yield 而非真正挂起 OS 线程的问题，涉及 NullClaw 托管运行时与宿主调度器的边界正确性
- **#783** 是近两个月最大的功能增量，包含 DB 持久化调度器、运行历史、JSON CLI 输出、安全加固，但 46 天未合并暗示审查复杂度或设计争议

> **整体推进评估**：代码层面有实质改进，但**合并吞吐量为零**，项目处于"开发活跃、集成停滞"状态。

---

## 4. 社区热点

**今日无活跃讨论**

3 条开放 PR 的社区互动指标均为 **0 评论、0 👍**，呈现典型的**核心维护者驱动（maintainer-driven）模式**，缺乏社区参与。特别值得关注：

- **#783** 作为大型功能 PR（作者 yanggf8 非 vernonstinebaker），46 天零评论可能表明：
  - 功能范围过大，审查者难以切入
  - Cron 子系统非当前用户刚需，社区缺乏反馈动力
  - 或项目治理模式偏向核心维护者私下审查

[nullclaw/nullclaw#783](https://github.com/nullclaw/nullclaw/pull/783)

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | Fix PR |
|:---|:---|:---|:---|
| 🔴 **高** | POSIX 下 `thread.sleep()` 未真正挂起 OS 线程，可能导致 CPU 空转与调度器资源浪费 | **开放 23 天** | [#878](https://github.com/nullclaw/nullclaw/pull/878) |
| 🟡 **中高** | Provider 健康探针将 curl 传输错误聚合为泛化错误，掩盖 DNS/连接/TLS/超时等具体故障根因 | **开放 18 天** | [#891](https://github.com/nullclaw/nullclaw/pull/891) |

**风险评估**：#878 的调度器问题在 AI Agent 长时间运行场景下可能引发资源泄漏，建议优先合并。

---

## 6. 功能请求与路线图信号

**来自开放 PR 的功能信号**：

| 功能 | 来源 | 纳入可能性 | 判断依据 |
|:---|:---|:---|:---|
| Cron 子代理引擎（DB 调度、历史追踪、多任务类型） | #783 | **中** | 功能完整但审查停滞，若维护者认可架构可能随 0.x 版本发布 |
| JSON CLI 输出（`cron list --json`, `cron schedule --json`） | #783 | **高** | 属于可独立拆分的增强，通常阻力较小 |
| 时区偏移支持（per-job TZ） | #783 | **中** | 依赖核心调度器设计是否冻结 |
| 安全加固（未详述具体措施） | #783 | **待定** | 摘要未展开，需审查可见 |

**缺失信号**：今日无用户主动提出的 Issues 功能请求，社区需求输入渠道似乎不畅。

---

## 7. 用户反馈摘要

**今日无可用用户反馈数据**（0 Issues，0 PR 评论）

> ⚠️ **健康度警示**：连续 24 小时零 Issues 活动对活跃开源项目属异常。可能原因：
> - 项目用户基数尚小或处于早期采用者阶段
> - 文档/示例充分降低了支持负担
> - 社区反馈渠道未有效建立（如 Discord/Discourse 分流）
> - 或数据采集存在盲区

建议维护者关注外部社区（如 Hacker News、Reddit r/localLLaMA、Discord）的提及情况。

---

## 8. 待处理积压

| PR/Issue | 开放天数 | 风险 | 行动建议 |
|:---|:---|:---|:---|
| [#783 feat(cron)](https://github.com/nullclaw/nullclaw/pull/783) | **46 天** | 代码陈旧、冲突累积、贡献者流失 | 立即拆分审查：将 JSON CLI 输出、DB schema、调度器核心、安全加固拆分为独立 PR |
| [#878 fix(compat)](https://github.com/nullclaw/nullclaw/pull/878) | **23 天** | 运行时稳定性缺陷持续暴露 | 优先合并，POSIX 路径已验证，Windows/WASI 回退路径保留现有行为，风险可控 |
| [#891 fix(providers)](https://github.com/nullclaw/nullclaw/pull/891) | **18 天** | 生产排障能力受损 | 安排网络层代码审查，错误枚举设计需确认与现有 provider 生态兼容 |

**维护者关注提醒**：vernonstinebaker 作为核心维护者同时是 #891/#878 的作者，可能存在**自我审查瓶颈**（无外部 reviewer）。建议：
1. 明确指定第二位维护者负责审查
2. 对 #783 引入 yanggf8 进行同步沟通，避免大型 PR 沉默死亡

---

*日报生成时间：2026-05-23 | 数据来源：NullClaw GitHub 公开 API*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw 项目动态日报 | 2026-05-23

> **项目定位**: NEAR AI 开源的 AI 智能体与个人 AI 助手运行时框架，当前处于 **Reborn 架构大规模迁移期**

---

## 1. 今日速览

IronClaw 今日呈现 **极高强度开发态势**：24 小时内 50 个 PR 更新（29 个待合并）、26 个 Issue 更新（19 个活跃），**零版本发布**。核心信号是 **Reborn 架构进入"功能冲刺+系统整合"双轨并行阶段**：一方面 Google Extensions 6 阶段流水线（#3893-#3898）全面铺开，另一方面子智能体（Subagent）spawn 机制四阶段草案（#3868-#3872）同步推进，显示团队正在并行攻克"外部工具生态"与"内部编排能力"两大战略支柱。WebUI Beta 的 M1-M4 模块 Issues 密集关闭，表明前端产品化进入收尾。风险点在于 XL 级 PR 占比过高，可能带来集成债务。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭的关键 PR

| PR | 作者 | 核心贡献 | 项目推进意义 |
|:---|:---|:---|:---|
| [#3861](https://github.com/nearai/ironclaw/pull/3861) | serrrfirat | Reborn 技能激活选择器（Skill Activation Selector） | **智能体能力编排基础设施成型**：支持 `/skill` 命令显式激活、技能上下文源切换、激活状态持久化，为"技能即插件"生态奠定运行时基础 |
| [#3761](https://github.com/nearai/ironclaw/pull/3761) | serrrfirat | 事件流管理器切片（EventStreamManager） | **产品级实时交互能力落地**：传输无关的流管理、订阅准入控制、延迟/重基流项、显式脱敏，支撑 WebUI v2 SSE 输出与多租户隔离 |

### 已关闭的关键 Issue（Reborn WebUI Beta 模块收尾）

| Issue | 模块 | 关闭意义 |
|:---|:---|:---|
| [#3013](https://github.com/nearai/ironclaw/issues/3013) | M3-agentloop-turns | **TurnCoordinator 内核服务上线**：线程/轮次准入控制、单运行强制执行，解除 Reborn 后组切换阻塞 |
| [#3623](https://github.com/nearai/ironclaw/issues/3623) | M2-inbound-workflow | **BeforeInboundPolicy 接缝完成**：WebChat v2 用户消息策略检查/拒绝/重写能力到位 |
| [#3611](https://github.com/nearai/ironclaw/issues/3611) | M1-webui-product | **原生 WebChat v2 路由集实现**：创建线程、发送消息、获取时间线等最小路由就绪 |
| [#3626](https://github.com/nearai/ironclaw/issues/3626) | M2-inbound-workflow | **调用者-线程作用域绑定**：认证 WebUI 调用者 → 规范 TurnScope 转换完成 |
| [#3625](https://github.com/nearai/ironclaw/issues/3625) | M2-inbound-workflow | **幂等性保障**：客户端动作 ID / 幂等键防止重复提交，消息账本机制就位 |
| [#3610](https://github.com/nearai/ironclaw/issues/3610) | M4-host-kernel | **类型化文件系统错误保留**：`ProcessError::Filesystem(String)` 反模式消除，下游分类可靠性提升 |
| [#3039](https://github.com/nearai/ironclaw/issues/3039) | - | **最终集成 PR 审查清单关闭**：Reborn-integration → staging 的验证流程标准化 |

> **整体里程碑判断**: WebUI Beta 的 M1-M4 模块 **7 个 P0 Issue 全部关闭**，标志 **Reborn 产品表面迁移完成"最小可用"阈值**，团队可转向 Google Extensions 与 Subagent 两大新战线。

---

## 4. 社区热点

### 讨论最活跃的 Issues（按评论数排序）

| 排名 | Issue | 评论 | 核心诉求分析 |
|:---|:---|:---|:---|
| 1 | [#3013](https://github.com/nearai/ironclaw/issues/3013) TurnCoordinator | 8 | **架构治理诉求**：Reborn 切换阻塞器的系统性解决，社区关注"后组迁移"的技术债务清理节奏 |
| 2 | [#3031](https://github.com/nearai/ironclaw/issues/3031) 产品表面迁移 EPIC | 7 | **路线图透明化诉求**：用户/运营者行为兼容性的保障范围，依赖 DAG 可视化（gist 链接）降低认知门槛 |
| 3 | [#3702](https://github.com/nearai/ironclaw/issues/3702) 二进制 E2E 测试框架 | 4 | **质量基础设施诉求**：88 个 Rust 测试文件审计后，社区要求"不依赖内部文档"的独立 GitHub 可追踪计划 |
| 4 | [#3623](https://github.com/nearai/ironclaw/issues/3623) BeforeInboundPolicy | 3 | **产品安全诉求**：WebUI beta 关键路径的策略检查能力，从 #3280 拆分体现"最小可交付"优先级管理 |

### 反应信号（👍）

| Issue | 👍 | 信号 |
|:---|:---|:---|
| [#2117](https://github.com/nearai/ironclaw/issues/2117) ironclaw-bridge 本地文件/MCP 桥接守护进程 | 1 | **唯一非零点赞**：云托管场景下的本地文件访问是真实用户痛点，但 4 月 7 日创建以来进展缓慢，存在需求-交付落差 |

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | Fix PR | 分析 |
|:---|:---|:---|:---|:---|
| 🔴 **高** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E 失败 | 开放，5 月 10 日创建，昨日更新 | **无** | **持续 12 天的夜间 E2E 失败**，v2-engine 作业失败，提交 `030cfeb` 引入的回归尚未定位。阻塞发布信心，需立即响应 |
| 🟡 **中** | [#3875](https://github.com/nearai/ironclaw/issues/3875) Subagent 阻塞 spawn 父恢复失败 | 开放，昨日新建 | #3872 (Draft) | 子智能体完成后父运行无法恢复，Phase 4 验证暴露的**真实集成缺口**，设计文档 #3798 未覆盖的边界情况 |
| 🟡 **中** | [#3871](https://github.com/nearai/ironclaw/issues/3871) executor.rs 分解 | 开放，昨日新建 | **无** | 架构债务：#3868 增加子智能体处理后，executor.rs 超出大文件指导阈值，**技术债务主动追踪** |
| 🟢 **低** | 多个 WebUI Beta 模块 Issue 关闭伴随的类型化错误、幂等性等 | 已关闭 | 已合并 | 预防性修复，无生产影响 |

> **稳定性健康度评估**: ⚠️ **黄色预警**。Nightly E2E 持续失败是最大风险信号，与当前 XL 级 PR 爆发形成"速度-质量"张力。Subagent 集成缺口显示复杂异步生命周期设计的固有挑战。

---

## 6. 功能请求与路线图信号

### 已进入实现阶段（高纳入概率）

| 功能 | 载体 | 阶段 | 下一版本判断 |
|:---|:---|:---|:---|
| **Google Extensions 全栈** | #3893-#3898（6 个 Phase PR） | Phase 1-6 并行开放 | **极大概率 vNext**：OAuth 底基、Calendar 9 能力、Gmail 6 能力、原生扩展脚手架，形成完整生产力工具链 |
| **子智能体 Spawn** | #3868-#3872（4 个 Phase Draft PR）+ #3798 设计 | Phase 1-4 草案 | **高概率 vNext**：设计文档已合并，四阶段流水线清晰，但 #3875 集成缺口可能延迟 |
| **Reborn 预算/成本管控** | #3899 | 端到端跟进 #3841 | **高概率 vNext**：usage 令牌、成本归集、预算执行器，商业化基础设施 |
| **触发循环（Cron）** | #3873 | 新建 | **中概率 vNext+1**：V1 仅定时触发，设计相对独立，可后置 |

### 设计阶段（路线图信号）

| 功能 | Issue | 信号强度 |
|:---|:---|:---|
| **Slack ProductAdapter MVP** | [#3857](https://github.com/nearai/ironclaw/issues/3857) | 强：预配置凭证、DM/提及支持、异步回复，企业场景刚需 |
| **WebUI v2 静态移植** | [#3886](https://github.com/nearai/ironclaw/issues/3886) | 强：ArtemSirobaba 分支接入，#3815 入口契约已就绪 |

### 长期需求（存在落差）

| 功能 | Issue | 落差分析 |
|:---|:---|:---|
| **本地文件/MCP 桥接** | [#2117](https://github.com/nearai/ironclaw/issues/2117) | 4 月 7 日创建，唯一 👍>0 的需求，但无关联 PR，云-端协同场景被 Reborn 基础设施优先级压制 |

---

## 7. 用户反馈摘要

> 基于 Issue 评论与 PR 描述的**间接用户信号**提炼（直接用户反馈渠道未在数据中体现）

| 维度 | 信号 | 来源 |
|:---|:---|:---|
| **痛点** | 云托管无法访问本地文件（Obsidian 仓库、项目目录） | #2117 问题陈述 |
| **痛点** | Reborn 迁移期间行为兼容性焦虑 | #3031 "preserve current IronClaw user/operator behavior" |
| **诉求** | 测试框架独立可追踪，不依赖内部文档 | #3702 "stand alone on GitHub without requiring access to local planning docs" |
| **满意** | WebUI Beta 路由/幂等性/作用域绑定快速交付 | M1-M4 模块 7 个 Issue 密集关闭 |
| **不满意** | Nightly E2E 可靠性不足 | #3447 持续 12 天失败，无修复响应 |
| **场景** | 企业微信（WeCom）独立通道 | #2394 PR 描述中的 Bot-first 场景 |
| **场景** | NEAR 生态内容摘要技能 | #3892 社区贡献技能，显示开发者生态萌芽 |

---

## 8. 待处理积压

| 风险等级 | 事项 | 滞留时间 | 关键性 | 提醒 |
|:---|:---|:---|:---|:---|
| 🔴 **紧急** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E 失败 | **12 天** | 发布阻塞 | 夜间测试持续失败将侵蚀 Reborn 迁移信心，需指定 owner 每日跟进 |
| 🟡 **高** | [#2117](https://github.com/nearai/ironclaw/issues/2117) 本地文件桥接 | **46 天** | 用户痛点唯一 👍 | 云-端协同是差异化场景，建议评估是否纳入 Q3 路线图 |
| 🟡 **高** | [#3702](https://github.com/nearai/ironclaw/issues/3702) 二进制 E2E 框架 | **6 天** | 质量基础设施 | 88 测试文件审计后的行动计划，需明确里程碑 |
| 🟡 **高** | [#3871](https://github.com/nearai/ironclaw/issues/3871) executor.rs 分解 | 新建 | 架构债务 | 建议在 Subagent Phase 合并前完成，避免债务累积 |
| 🟢 **中** | [#2394](https://github.com/nearai/ironclaw/pull/2394) WeCom 通道 | **39 天** | 企业场景 | XL 级高风� PR，需评估与 Reborn 原生通道战略的兼容性 |

---

## 附录：今日数据面板

| 指标 | 数值 | 趋势判断 |
|:---|:---|:---|
| Issues 更新 | 26（新开/活跃 19，关闭 7） | 📈 活跃，关闭率 27% |
| PRs 更新 | 50（待合并 29，已合并/关闭 21） | 📈 极高吞吐，合并率 42% |
| XL 级 PR 占比 | 11/20 展示 = **55%** | ⚠️ 大变更集中，集成风险 |
| 版本发布 | 0 | — |
| 评论数>0 的 Issue | 10/26 = 38% | 讨论深度适中 |

> **明日关注**: #3893-#3898 Google Extensions 流水线合并节奏、#3872 Subagent Phase 4 Draft 转正式、#3447 E2E 修复响应。

---

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目动态日报 | 2026-05-23

> **项目**: [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)  
> **日期**: 2026-05-23  
> **分析师**: AI 智能体与个人 AI 助手领域开源项目分析师

---

## 1. 今日速览

LobsterAI 今日呈现**高强度迭代态势**，24 小时内 21 个 PR 流转（12 条已合并/关闭），并发布 **2026.5.22 版本**，核心聚焦**子代理（Subagent）会话体验重构**与**模型配置灵活性提升**。社区活跃度极高，开发团队（`btc69m979y-dotcom`、`fisherdaddy`）当日密集交付 11 个功能/修复 PR，显示产品进入快速打磨期。唯一新 Issue 指向 OpenClaw gateway 的事件广播机制缺失，属于架构层深度需求。整体项目健康度：**优秀**，但需关注 5 个积压近两个月的安全/体验 PR 未获响应。

---

## 2. 版本发布

### [LobsterAI 2026.5.22](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.5.22) 🆕

| 属性 | 详情 |
|:---|:---|
| **发布日期** | 2026-05-22 |
| **发布者** | `fisherdaddy` |
| **版本类型** | 功能迭代版本 |

#### 核心变更

| PR | 作者 | 功能说明 |
|:---|:---|:---|
| [#2011](https://github.com/netease-youdao/LobsterAI/pull/2011) | `btc69m979y-dotcom` | **子代理会话侧边栏与详情视图** — 新增独立的子代理会话侧边栏导航，支持详情页独立展示 |
| [#2019](https://github.com/netease-youdao/LobsterAI/pull/2019) | `btc69m979y-dotcom` | **模型自定义参数 + 思维链（Thinking Block）展示** — 允许用户配置模型级自定义参数，并在 UI 中可视化模型的推理过程 |

#### 破坏性变更与迁移注意
- **无明确破坏性变更**；子代理会话数据采用**惰性回填（lazy backfill）**策略，旧会话首次点击时自动持久化至本地 DB，无需用户手动迁移。
- 模型自定义参数功能需配合支持 `thinking` 能力的模型版本使用。

---

## 3. 项目进展

### 今日合并/关闭的关键 PR（12 条）

#### 🔥 子代理（Subagent）架构重构 — 6 条 PR 形成完整交付闭环

| PR | 作者 | 状态 | 技术价值 |
|:---|:---|:---|:---|
| [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034) | `btc69m979y-dotcom` | ✅ 已合并 | **子代理消息本地持久化** — 新建 `subagent_messages` SQLite 表，首次网关获取后缓存，后续零网络加载 |
| [#2030](https://github.com/netease-youdao/LobsterAI/pull/2030) | `btc69m979y-dotcom` | ✅ 已合并 | **渲染管道复用** — 提取 `ConversationTurnsView` 通用组件，子代理后端输出完整 `CoworkMessage` 格式，终结简单 Markdown 渲染 |
| [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | `btc69m979y-dotcom` | ✅ 已合并 | **同步与状态修复** — 补全工具结果/工具输入显示、侧边栏高亮状态、空态与错误处理 |
| [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | `btc69m979y-dotcom` | ✅ 已合并 | **去重与样式优化** — `toolCallId` 替代 `agentId` 作为唯一键，解决同 agent 多实例冲突；简化侧边栏视觉 |
| [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) | `btc69m979y-dotcom` | ✅ 已合并 | **交互体验打磨** — 侧边栏折叠态 toggle、可拖拽 header、Mac 窗口控件防重叠 |
| [#2038](https://github.com/netease-youdao/LobsterAI/pull/2038) | `fisherdaddy` | ✅ 已合并 | **版本发布汇总** — 正式打包 2026.5.19/2026.5.22 双版本内容 |

#### 🔧 模型与配置修复 — 3 条 PR

| PR | 作者 | 状态 | 修复内容 |
|:---|:---|:---|:---|
| [#2035](https://github.com/netease-youdao/LobsterAI/pull/2035) | `fisherdaddy` | ✅ 已合并 | Qwen 3.6 Plus 编码方案修正 |
| [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | `fisherdaddy` | ✅ 已合并 | 自定义模型切换错误修复 |
| [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | `fisherdaddy` | ✅ 已合并 | 浏览器配置失效修复 |

#### ✨ 体验优化 — 2 条 PR

| PR | 作者 | 状态 | 内容 |
|:---|:---|:---|:---|
| [#2037](https://github.com/netease-youdao/LobsterAI/pull/2037) | `fisherdaddy` | ✅ 已合并 | IM 相关文案优化 |
| [#2028](https://github.com/netease-youdao/LobsterAI/pull/2028) | `fisherdaddy` | ✅ 已合并 | UI 更新 |

**整体评估**：子代理功能从"能用"跃迁至"好用"，完成**数据层（持久化）→ 架构层（管道复用）→ 表现层（UI/UX）**的三层重构，是近两周最大功能交付。

---

## 4. 社区热点

> 今日无高评论数议题，所有 PR 评论数均为 `undefined`（未触发讨论或机器人 PR）。唯一活跃讨论见 **Issue #2036**。

### [Issue #2036](https://github.com/netease-youdao/LobsterAI/issues/2036): OpenClaw gateway 事件广播机制需求

| 属性 | 详情 |
|:---|:---|
| **作者** | `woxinsj` |
| **状态** | 🟢 OPEN |
| **评论** | 1 |
| **诉求** | 要求 OpenClaw gateway 增加 `agent:turn` 或 `agent:loop` 事件，实现主循环每轮结束后自动广播，以支持**实时落盘** |

**深度分析**：此需求暴露当前子代理/多轮协作架构的**观测性缺口**。实时落盘是生产级 AI Agent 系统的关键可靠性需求（防止崩溃丢数据、支持断点恢复），但现有事件体系仅覆盖完整会话粒度，缺乏**回合级（turn-level）**生命周期钩子。该 Issue 与今日密集交付的子代理功能形成呼应——子代理消息已能本地持久化，但**网关层的事件驱动架构**尚未对齐，可能制约企业级部署。

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | Fix PR | 影响范围 |
|:---|:---|:---|:---|:---|
| 🔶 **中** | 子代理会话同步缺失工具结果与工具输入显示 | ✅ 已修复 | [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | 子代理详情页数据完整性 |
| 🔶 **中** | 子代理去重逻辑缺陷（`agentId` 冲突） | ✅ 已修复 | [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | 多子代理同 agent 场景 |
| 🔶 **中** | 自定义模型切换错误 | ✅ 已修复 | [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | 模型配置灵活性 |
| 🔶 **中** | 浏览器配置失效 | ✅ 已修复 | [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | 浏览器工具集成 |
| 🔷 **低** | Qwen 3.6 Plus 编码方案异常 | ✅ 已修复 | [#2035](https://github.com/netease-youdao/LobsterAI/pull/2035) | 特定模型兼容性 |

> 今日无**高严重**崩溃或安全漏洞报告。所有已知问题均当日闭环，修复响应速度优秀。

---

## 6. 功能请求与路线图信号

### 已释放信号（来自今日 Release）

| 功能 | 成熟度 | 下一版本预期 |
|:---|:---|:---|
| 子代理会话独立侧边栏 + 详情视图 | 🟢 已发布 | 持续优化，可能增加会话搜索/过滤 |
| 模型自定义参数配置 | 🟢 已发布 | 参数模板预设、参数校验规则 |
| 思维链（Thinking Block）可视化 | 🟢 已发布 | 支持折叠/展开、推理过程高亮 |

### 待响应架构需求

| 来源 | 需求 | 纳入可能性 |
|:---|:---|:---|
| [Issue #2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | OpenClaw gateway 回合级事件广播 | **高** — 与子代理可靠性直接相关，可能触发 2026.5.25+ 版本 |

### 积压 PR 中的潜在功能

| PR | 功能 | 状态 | 纳入评估 |
|:---|:---|:---|:---|
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | 本地会话使用统计面板 | 🟡 stale (4/7) | 中 — 数据看板需求明确，但需与现有埋点体系整合 |
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | 主题色选择器 UI 重构 | 🟡 stale (4/7) | 低 — 体验优化，非核心路径 |

---

## 7. 用户反馈摘要

> 今日仅 **Issue #2036** 含用户主动反馈，以下为提炼：

| 维度 | 内容 |
|:---|:---|
| **痛点** | 子代理/多轮协作场景下，缺乏**细粒度生命周期事件**，导致无法可靠实现实时数据持久化 |
| **使用场景** | 长时运行的 Agent 任务，需防崩溃丢数据、支持断点恢复与外部系统同步 |
| **不满意** | 当前 `agent:complete` 等事件粒度太粗，"拿到事件后才能真正做到实时落盘"暗示现有方案存在**可靠性窗口期** |
| **深层诉求** | 企业级部署所需的**可观测性（Observability）**与**可靠性（Reliability）**基线 |

> 注：今日密集交付的子代理功能尚未看到终端用户反馈，建议维护者在下一版本周期主动收集子代理使用体验。

---

## 8. 待处理积压

### ⚠️ 高优先级关注：安全相关 PR（2 条，stale 近 7 周）

| PR | 作者 | 创建时间 | 风险说明 | 行动建议 |
|:---|:---|:---|:---|:---|
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) | `kayo5994` | 2026-04-07 | **API 代理日志泄露凭证与完整响应体** — 当前 `info` 级别日志记录完整 URL、Header、Body，API Key/Bearer Token/对话内容持久化至本地日志文件 | **立即评审合并**；安全红线问题，虽为本地应用但涉及企业场景合规风险 |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | `kayo5994` | 2026-04-07 | **渲染进程 KV Store IPC 无键白名单** — 渲染进程可任意读写 `auth_tokens`、`enterprise_config` 等敏感键，削弱纵深防御 | **立即评审合并**；与 #1534 形成安全加固组合，建议同版本发布 |

### 体验优化 PR（1 条）

| PR | 作者 | 创建时间 | 说明 |
|:---|:---|:---|:---|
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | `leedalei` | 2026-04-07 | 主题色选择器 UI 重构，代码侵入性低（单文件改动），建议择期合并 |

### 功能增强 PR（1 条）

| PR | 作者 | 创建时间 | 说明 |
|:---|:---|:---|:---|
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | `MaoQianTu` | 2026-04-07 | 本地使用统计面板，需确认与现有数据收集策略的兼容性 |

### 依赖升级 PR（5 条，待合并）

| PR | 内容 | 风险 |
|:---|:---|:---|
| [#1766](https://github.com/netease-youdao/LobsterAI/pull/1766) | Vite 5.4.21 → 8.0.13（跨 major 版本） | ⚠️ 需验证构建链与插件兼容性 |
| [#1765](https://github.com/netease-youdao/LobsterAI/pull/1765) | @headlessui/react 1.7.19 → 2.2.10 | 中 — UI 组件行为变更需回归测试 |
| [#1764](https://github.com/netease-youdao/LobsterAI/pull/1764) | react-dom 18.3.1 → 19.2.6 | ⚠️ React 19 并发特性可能影响渲染时序 |
| [#1763](https://github.com/netease-youdao/LobsterAI/pull/1763) | @vitejs/plugin-react 4.7.0 → 6.0.1 | 配合 Vite 升级 |
| [#1277](https://github.com/netease-youdao/LobsterAI/pull/1277) | Electron 40.2.1 → 42.1.0 + electron-builder 升级 | ⚠️ Electron major 升级涉及原生模块重编译、API 废弃 |

> **维护者行动建议**：安全 PR #1534/#1535 建议优先于依赖升级处理；Electron/Vite/React 三连 major 升级建议单独规划回归测试周期，避免与子代理功能迭代耦合。

---

## 附录：今日数据看板

| 指标 | 数值 | 环比评估 |
|:---|:---|:---|
| PR 处理量 | 21（12 关闭/合并，9 待处理） | 🔺 活跃 |
| Issue 新增 | 1（架构需求） | 正常 |
| 版本发布 | 1 | 高频迭代 |
| 安全积压 | 2 PR（stale 7 周） | ⚠️ 需关注 |
| 依赖升级积压 | 5 PR（含 3 major 升级） | ⚠️ 需规划 |

---

*日报基于 GitHub 公开数据生成，未包含私有讨论或内部工单信息。*

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis 项目动态日报 | 2026-05-23

## 1. 今日速览

Moltis 今日保持**高活跃度**，24小时内 7 个 PR 流动（4 闭 3 开）、4 个 Issue 更新（2 闭 2 开），无新版本发布。核心进展集中在 **Docker 环境稳定性修复**（3 个相关 PR 闭环）和 **电话语音交互质量提升**（Twilio 语音收集修复、TTS 格式兼容）。项目显示健康的维护节奏：penso 作为核心贡献者单日合并 4 个 PR，但社区参与度偏低（所有 Issue/PR 均无 👍 反应，评论数极少），开源生态的社区互动仍是短板。

---

## 2. 版本发布

**无新版本发布**（最新版本仍为 20260518.01）

---

## 3. 项目进展

### 已合并/关闭 PR（4 条）

| PR | 作者 | 核心贡献 | 项目推进价值 |
|:---|:---|:---|:---|
| [#1035](https://github.com/moltis-org/moltis/pull/1035) `fix(sandbox): auto-detect docker host data mounts` | penso | 自动检测 Docker/Podman 容器的主机数据挂载，解决沙箱路径解析和浏览器配置文件挂载问题 | **基础设施层突破**：消除 Docker 部署的手动挂载配置，降低部署门槛；为 #977 等 Docker 相关 bug 提供系统性根因修复 |
| [#1034](https://github.com/moltis-org/moltis/pull/1034) `fix(telephony): dispatch Twilio gather speech` | penso | 修复 Twilio 语音收集解析顺序，确保 `SpeechResult`/`Digits` 优先于 `CallStatus=in-progress` 处理；新增回归测试和调试日志 | **关键用户体验修复**：直接解决 #1032 "电话接通后无响应"的生产级故障，提升语音交互可靠性 |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) `Allow disabling vault encryption at rest` | penso | 新增 `auth.vault_enabled` 配置项，支持运行时通过 API/UI 安全禁用 vault（自动解密所有敏感数据后再切换） | **运维灵活性**：满足合规场景下的加密可选需求，降低小型部署的复杂度 |
| [#1039](https://github.com/moltis-org/moltis/pull/1039) `chore(deps): bump openssl` | dependabot | OpenSSL Rust 绑定 0.10.79 → 0.10.80 | 安全补丁，依赖健康度维护 |

**整体迈进评估**：今日合并 PR 覆盖 **部署稳定性**（Docker 挂载）、**核心功能可靠性**（电话语音）、**运维灵活性**（Vault 可选化）三个维度，属于典型的"质量巩固日"，为近期频繁的 Docker/语音相关投诉提供系统性修复。

---

## 4. 社区热点

| 条目 | 热度指标 | 诉求分析 |
|:---|:---|:---|
| [#977](https://github.com/moltis-org/moltis/issues/977) `[Bug]: Browser sandbox fails when Moltis runs in Docker` | 5 评论，0 👍，已关闭 | **Docker 部署的浏览器沙箱兼容性** — 这是过去两周最高频的问题类别。用户 TLA020 在 Proxmox LXC + Docker 嵌套环境中遇到沙箱创建失败，触发深度排查。该 Issue 的关闭标志着 Docker 沙箱问题进入系统性修复阶段 |
| [#1032](https://github.com/moltis-org/moltis/issues/1032) `[Bug]: Phone (Twilio) call: the agent greets me but never responds to what I say` | 0 评论，0 👍，已关闭 | **生产级语音交互阻断性 bug** — 用户 karlmdavis 的预检清单显示其严格遵循报告规范，但零评论即关闭，说明维护者快速定位并修复。反映语音电话场景的用户期望与实际稳定性之间的差距 |

**社区互动短板**：所有条目均无 👍 反应，Issue #1037、#1036 零评论，PR 评论数均为 `undefined`（可能数据缺失或确实无评论）。社区参与度显著低于代码活跃度。

---

## 5. Bug 与稳定性

| 严重程度 | Issue/PR | 描述 | Fix 状态 |
|:---|:---|:---|:---|
| 🔴 **阻断性** | [#1032](https://github.com/moltis-org/moltis/issues/1023) | Twilio 电话：Agent 问候后无响应（语音收集未触发） | ✅ **已修复** via [#1034](https://github.com/moltis-org/moltis/pull/1034) |
| 🟡 **高** | [#977](https://github.com/moltis-org/moltis/issues/977) | Docker 内浏览器沙箱创建失败 | ✅ **已修复** via [#1035](https://github.com/moltis-org/moltis/pull/1035) |
| 🟡 **高** | [#1037](https://github.com/moltis-org/moltis/issues/1037) `[OPEN]` | `send_image` / `send_document` 在 Docker 中失败 | 🔄 **Fix PR 待合并** [#1040](https://github.com/moltis-org/moltis/pull/1040) |
| 🟢 **中** | [#1041](https://github.com/moltis-org/moltis/pull/1041) `[OPEN]` | TTS 使用 opus 格式导致 OpenAI 兼容服务器（如 Speaches）不兼容 | 🔄 **Fix PR 待合并** — 切换为 MP3 格式 |

**模式识别**：Docker 环境构成当前最大稳定性风险集群（3/4 的 bug 相关），建议维护者将 Docker 兼容性测试纳入 CI 核心路径。

---

## 6. 功能请求与路线图信号

| 条目 | 类型 | 纳入可能性评估 |
|:---|:---|:---|
| [#1036](https://github.com/moltis-org/moltis/issues/1036) `[Feature]: Support arbitrary inbound file attachments in the web UI` | 功能请求 | **高** — 与 [#1037](https://github.com/moltis-org/moltis/issues/1037)/[#1040](https://github.com/moltis-org/moltis/pull/1040) 的媒体文件处理形成需求-修复对，Web UI 文件上传是 Docker 部署场景的自然延伸 |
| [#1031](https://github.com/moltis-org/moltis/pull/1031) `[OPEN] Add NEAR AI Cloud provider` | 新 Provider | **中高** — 扩展 TEE（可信执行环境）支持的 AI 提供商，符合企业级部署趋势；代码完整度较高（含模型发现、文档、本地化），但需 review 安全模型 |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) `Allow disabling vault encryption at rest` | 运维灵活性 | **已合并** — 为轻量级部署铺路，可能预示后续"简化安装模式"的产品方向 |

**路线图信号**：Docker 体验优化（#1035→#1040→#1036）形成连贯叙事，可能指向 **"一键 Docker 部署"** 的正式发布；语音/电话功能（#1034、#1041）持续打磨，暗示 telephony 模块正从 MVP 向生产级演进。

---

## 7. 用户反馈摘要

### 痛点
- **Docker 部署"最后一公里"断裂**：用户 IlyaBizyaev（#1037）、TLA020（#977）均遇到 Docker 特定功能失效，说明文档中的 Docker 指南与实际运行时行为存在差距
- **语音电话"伪接通"体验**：karlmdavis（#1032）遭遇 Agent 问候后沉默，对用户信任造成即时损害——这比完全无法拨通更糟

### 使用场景
- **嵌套虚拟化环境**：Proxmox LXC → Docker 的部署路径（#977）显示用户追求资源效率，但增加了沙箱复杂度
- **OpenAI 兼容生态兼容**：Speaches 等自托管 TTS 服务（#1041）反映用户倾向于避免厂商锁定

### 满意度暗示
- 快速修复闭环（#1032 24小时内关闭）→ 维护响应速度获认可
- 零评论、零反应 → 用户可能"沉默地满意"或尚未形成社区参与习惯

---

## 8. 待处理积压

| 条目 | 创建时间 | 风险/提醒 |
|:---|:---|:---|
| [#1031](https://github.com/moltis-org/moltis/pull/1031) `Add NEAR AI Cloud provider` | 2026-05-21 | **新 Provider 集成 PR 已滞留 2 天**，涉及 TEE 安全模型审查，建议优先安排安全/架构 review 避免社区贡献者流失 |
| [#1040](https://github.com/moltis-org/moltis/pull/1040) `Fix sandbox media file reads in Docker` | 2026-05-22 | 关联开放 Issue #1037，建议 48 小时内合并以阻断 Docker 媒体功能故障的投诉增量 |
| [#1041](https://github.com/moltis-org/moltis/pull/1041) `fix(gateway): use mp3 for chat voice generation` | 2026-05-22 | TTS 兼容性修复，影响 OpenAI 兼容生态用户，建议与 #1031 错开 review 资源 |

---

*日报基于 GitHub 公开数据生成，时间范围：2026-05-22 至 2026-05-23 UTC*

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw 项目动态日报 | 2026-05-23

## 1. 今日速览

CoPaw（QwenPaw）今日保持**高活跃度**，24小时内产生23条Issue更新（16条新开/活跃）和20条PR更新（9条已合并/关闭），无新版本发布。社区聚焦三大主题：**聊天历史与上下文管理稳定性**（#4620、#3984）、**多模型兼容性扩展**（MiniMax/Gemini/ChatGPT-5.5）、以及**WeChat/DingTalk等企业级通道的可靠性修复**。首次贡献者参与积极，4个PR来自新贡献者，项目生态健康度良好。

---

## 2. 版本发布

**无新版本发布** | 最新版本仍为 v1.1.8.post1

---

## 3. 项目进展

### 今日已合并/关闭的重要 PR（9条）

| PR | 作者 | 核心贡献 | 关联Issue |
|:---|:---|:---|:---|
| [#4600](https://github.com/agentscope-ai/QwenPaw/pull/4600) | hongxicheng | **修复DingTalk中文文件名编码问题**：`send_file_to_user` 发送图片时中文文件名被percent-encoded的bug | [#4586](https://github.com/agentscope-ai/QwenPaw/issues/4586) |
| [#4627](https://github.com/agentscope-ai/QwenPaw/pull/4627) | hongxicheng | **重构WeChat token失效机制**：将实例级`_context_token_invalid`标志改为请求级meta标志，解决跨请求干扰问题 | [#4612](https://github.com/agentscope-ai/QwenPaw/issues/4612) |
| [#4621](https://github.com/agentscope-ai/QwenPaw/pull/4621) | qbc2016 | **修复Gemini/Gemma模型参数兼容**：将`max_tokens`映射为`max_output_tokens`，解决pydantic ValidationError崩溃 | [#4605](https://github.com/agentscope-ai/QwenPaw/issues/4605) |
| [#4434](https://github.com/agentscope-ai/QwenPaw/pull/4434) | weixizi | **Cron任务上下文自动清理**：新增"Clear Before Run"选项，防止历史会话干扰定时任务 | [#4432](https://github.com/agentscope-ai/QwenPaw/issues/4432) |
| [#4597](https://github.com/agentscope-ai/QwenPaw/pull/4597) | hongxicheng | **修复WeChat API发送虚假成功**：`/api/messages/send` 在iLink API拒绝时正确返回失败，而非`{"success": true}` | [#4521](https://github.com/agentscope-ai/QwenPaw/issues/4521) |
| [#4618](https://github.com/agentscope-ai/QwenPaw/pull/4618) | hongxicheng | **WeChat token失效快速修复**（被#4627替代）：首次实现context_token无效时跳过后续发送 | - |
| [#4626](https://github.com/agentscope-ai/QwenPaw/pull/4626) | Osier-Yi | **修复QwenPaw-Pet连续对话卡死**：解决"Done"状态下事件序列号错乱导致消息被丢弃 | - |
| [#4623](https://github.com/agentscope-ai/QwenPaw/pull/4623) | zhaozhuang521 | **Skill市场页面UI优化**：替换菜单图标、代码与性能优化 | - |
| [#4395](https://github.com/agentscope-ai/QwenPaw/pull/4395) | aqilaziz | **安全模块测试覆盖**：为`tool_guard.utils`添加单元测试，覆盖工具权限解析优先级、拒绝规则等 | - |

**整体推进评估**：今日合并PR集中在**企业通道可靠性**（DingTalk/WeChat）和**模型兼容性**（Gemini/Gemma）两大硬骨头，hongxicheng 单日贡献3个关键修复，通道层稳定性显著改善。Cron任务上下文管理完成闭环（Issue→PR→合并）。

---

## 4. 社区热点

### 🔥 讨论最活跃的议题

| 排名 | Issue/PR | 评论数 | 热度分析 |
|:---|:---|:---|:---|
| 1 | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) **聊天历史消失** | 12评论 | **核心痛点**：用户切换session后历史消息随机丢失，作者duwey明确标记"critical bug and existed for a long time"。社区高度共鸣，长期存在的稳定性隐患 |
| 2 | [#4051](https://github.com/agentscope-ai/QwenPaw/issues/4051) DeepSeek think内容解析 | 10评论 | 已关闭，但反映**推理模型输出格式适配**的普遍挑战——DeepSeek V4 flash的`<thinking>`标签内容未被正确提取，导致"空回复" |
| 3 | [#4474](https://github.com/agentscope-ai/QwenPaw/issues/4474) ChatGPT-5.5支持询问 | 8评论 | 用户急于跟进OpenAI最新模型，配置失败。信号：**模型适配滞后于市场热点**，需建立更敏捷的模型支持机制 |

**背后诉求洞察**：
- **数据可靠性 > 新功能**：#4620的12条评论无👍但讨论密集，说明用户将聊天历史视为"底线需求"，丢失即信任崩塌
- **推理模型时代的新适配层**：#4051和#4625（MiniMax XML格式）共同指向——随着o3、DeepSeek-R、MiniMax等"思维链"模型普及，**思考过程解析**成为新的兼容性战场

---

## 5. Bug 与稳定性

| 优先级 | Issue | 严重程度 | 状态 | 修复PR | 影响范围 |
|:---|:---|:---|:---|:---|:---|
| 🔴 P0 | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) 聊天历史随机消失 | **数据丢失/核心功能崩溃** | 开放，12评论 | ❌ 无 | 所有使用session切换的用户 |
| 🔴 P0 | [#3984](https://github.com/agentscope-ai/QwenPaw/issues/3984) context_check拆分user/assistant对 | **UI orphaned消息/上下文逻辑错误** | 开放，3评论 | ❌ 无 | 启用上下文压缩的用户 |
| 🟡 P1 | [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625) MiniMax-M2.5 XML思考格式不兼容 | **问答中断/技能无法执行** | 开放，4评论 | ❌ 无 | MiniMax M2.5用户 |
| 🟡 P1 | [#4556](https://github.com/agentscope-ai/QwenPaw/issues/4556) 语音转写绕过Whisper配置 | **配置失效/隐私泄露风险**（浏览器原生API可能上传至Google） | 开放，4评论 | ❌ 无 | 配置自托管Whisper的用户 |
| 🟡 P1 | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) NO_PROXY环境变量不生效 | **代理绕过失败/企业内网不可用** | 开放，6评论 | ❌ 无 | 企业代理环境用户 |
| 🟢 P2 | [#4619](https://github.com/agentscope-ai/QwenPaw/issues/4619) Web UI视觉不一致 | 体验瑕疵 | 开放，1评论 | ❌ 无 | 所有Web用户 |
| 🟢 P2 | [#4616](https://github.com/agentscope-ai/QwenPaw/issues/4616) Dream awakening任务错误 | 特定功能错误 | 开放，3评论 | ❌ 无 | 使用dream awakening功能 |

**关键风险**：#4620与#3984可能**同源**——context_check的压缩逻辑不仅导致UI孤儿消息，可能在某些边界条件下直接丢弃历史。建议维护者优先排查`context_check` → `GET /chats/{chat_id}` 的数据流。

---

## 6. 功能请求与路线图信号

| 功能请求 | 提出者 | 技术方向 | 纳入可能性评估 |
|:---|:---|:---|:---|
| [#4632](https://github.com/agentscope-ai/QwenPaw/issues/4632) **多行文本写入工具** | kuangren3 | 基础设施/Agent能力补齐 | ⭐⭐⭐⭐⭐ **高** — 阻塞Skill开发、代码持久化等核心工作流，社区刚需 |
| [#4613](https://github.com/agentscope-ai/QwenPaw/issues/4613) **Plugin Agent Hook机制** (`register_agent_hook`) | carlos999-hqsama | 插件系统扩展 | ⭐⭐⭐⭐⭐ **高** — 已有LightRAG知识库插件实践，PR #4628同作者贡献插件导出功能，生态建设积极 |
| [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624) **按模型独立配置重试/限流** | shit6 | 多模型生产治理 | ⭐⭐⭐⭐☆ **中高** — 生产环境多模型混用的真实痛点，MiniMax不同型号配额差异大 |
| [#4617](https://github.com/agentscope-ai/QwenPaw/issues/4617) **远程Playwright浏览器端点** | MCQSJ | 浏览器工具云原生化 | ⭐⭐⭐⭐☆ **中高** — 与browserless等SaaS集成趋势，节省本地资源 |
| [#4634](https://github.com/agentscope-ai/QwenPaw/issues/4634) **窗口大小位置记忆** | mengxindada | Desktop体验优化 | ⭐⭐⭐☆☆ **中** — 体验优化，PR #3813 Tauri桌面支持推进中可能自然覆盖 |
| [#4633](https://github.com/agentscope-ai/QwenPaw/issues/4633) **自定义Slash命令快捷菜单** | DICKQI | 交互效率 | ⭐⭐⭐☆☆ **中** — 20+内置命令发现性问题，配置化实现成本较低 |

**路线图信号**：PR [#4630](https://github.com/agentscope-ai/QwenPaw/pull/4630)（MCP管理增强：市场、健康检查、密钥验证）与 [#4622](https://github.com/agentscope-ai/QwenPaw/pull/4622)（DataPaw数据分析插件）显示项目正向**MCP生态集成**和**垂直领域插件**两个方向扩展。

---

## 7. 用户反馈摘要

### 😤 核心痛点
> *"Switch to a session and sometimes cannot find all chat history. I think it's a critical bug and existed for a long time."* — duwey, [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620)

> *"配置了环境变量NO_PROXY，好像没生效，依然会走代理"* — MaoJianwei, [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607)

> *"全局统一的LLM自动重试和并发限流配置，已经无法适配多模型混合使用的场景"* — shit6, [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624)

### 🎯 使用场景
- **企业IM集成**：WeChat/DingTalk通道用于内部通知、客服自动化，对"发送成功但用户未收到"极度敏感（#4521、#4612、#4586）
- **多模型策略路由**：生产环境同时使用MiniMax M2.7/M2.5、DeepSeek、Gemini等，需要差异化配额管理
- **插件化知识库**：LightRAG等RAG系统通过插件接入，需要更底层的Agent生命周期Hook

### ✅ 满意点
- Cron任务上下文清理功能获认可（#4432/#4434），解决定时任务历史干扰问题
- 社区响应速度：WeChat相关问题24小时内连续出3个修复PR（#4618→#4627→#4597）

---

## 8. 待处理积压

| Issue/PR | 创建时间 | 最后更新 | 积压天数 | 风险说明 |
|:---|:---|:---|:---|:---|
| [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) Tauri 2.x桌面应用支持 | 2026-04-24 | 2026-05-22 | **28天** | 重大架构变更，影响#4634等桌面体验需求，需维护者决策是否纳入v1.2 |
| [#4464](https://github.com/agentscope-ai/QwenPaw/pull/4464) E2E测试迁移 | 2026-05-17 | 2026-05-22 | 6天 | 测试基础设施，关联#4467（967个单元测试），质量门禁关键 |
| [#4467](https://github.com/agentscope-ai/QwenPaw/pull/4467) 安全+Agent单元测试（967 tests） | 2026-05-17 | 2026-05-22 | 6天 | CI升级至L1 hard gate，阻塞后续安全相关合并 |
| [#4565](https://github.com/agentscope-ai/QwenPaw/pull/4565) 统一访问控制系统 | 2026-05-20 | 2026-05-22 | 3天 | 企业级功能，涉及所有通道的权限重构，代码量大需仔细review |
| [#3707](https://github.com/agentscope-ai/QwenPaw/issues/3707) MiniMax M2.7图片识别支持 | 2026-04-22 | 2026-05-22 | **31天** | 已关闭但方案为硬编码修改，需确认是否真正合入main |

**维护者行动建议**：
1. **紧急**：#4620 聊天历史消失需分配核心开发者，可能与#3984合并调查
2. **本周**：#3813 Tauri桌面支持需明确里程碑，多个桌面体验Issue依赖于此
3. **持续**：hongxicheng的通道修复模式值得文档化，形成WeChat/DingTalk等企业通道的故障响应SOP

---

*日报生成时间：2026-05-23 | 数据来源：GitHub agentscope-ai/QwenPaw*

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

ZeroClaw 今日呈现**高强度开发态势**，24小时内产生 **18 条 Issue 更新**（17 活跃/新开，仅 1 关闭）和 **23 条 PR 更新**（21 待合并，2 已合并/关闭）。核心信号是 **TUI（终端用户界面）成为绝对焦点**——维护者 `singlerider` 单日批量创建 8 个关联 Issue，涵盖 RPC 传输、ACP 桥接、聊天界面、UX 设计等全栈模块，显示该项目正从纯服务端向"服务端 + 原生终端客户端"双轨架构跃迁。社区侧有 3 个 P1 级 Bug 报告（WhatsApp QR、Slack 环境变量、多模态 vision_provider），通道稳定性仍是用户痛点。整体健康度：**开发活跃度高，但 Bug 积压与长期 PR 审查瓶颈需关注**。

---

## 2. 版本发布

**无新版本发布**。

---

## 3. 项目进展

### 已关闭/合并项

| 类型 | 编号 | 标题 | 意义 |
|:---|:---|:---|:---|
| **Issue 关闭** | [#5890](https://github.com/zeroclaw-labs/zeroclaw/issues/5890) | RFC: Multi-agent UX flow — design | **核心架构决策落地**：多智能体 UX 流 RFC 历经 7 天讨论期、核心团队 2/3 多数投票后正式接受，为后续多智能体协作奠定设计基础。待提取至 `docs/proposals/` |
| **PR 关闭** | [#6549](https://github.com/zeroclaw-labs/zeroclaw/pull/6549) | feat(providers/claude-code): add vision input support | 为 Claude Code 提供程序添加视觉输入支持的大型 PR 被关闭，原因未明示（可能因作者无响应或方案重构），视觉能力扩展遇阻 |
| **PR 关闭** | [#6849](https://github.com/zeroclaw-labs/zeroclaw/pull/6849) | 本地合并 | 标签覆盖全项目模块的巨型合并 PR，疑似误操作或测试用，无实际代码价值 |

### 关键推进方向

- **TUI 生态系统全面启动**：`singlerider` 创建的 8 个关联 Issue（#6821-#6827, #6837）形成完整技术栈——从目录重构、RPC 传输、文件上传协议、会话覆盖、 ephemeral 守护进程模式到 ACP 桥接和聊天界面，显示 TUI 并非实验性项目而是**一级产品战略**
- **Runtime RPC 层**（[#6837](https://github.com/zeroclaw-labs/zeroclaw/issues/6837)）：Unix socket 传输让 TUI 绕过 HTTP/WS 网关直连守护进程，降低延迟、支持无网络环境部署（如 enclave）
- **ACP 协议扩展**（[#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820)）：diff 展示与文件提案消息类型，解决 AI 编辑审批中的"黑盒"问题，提升用户信任

---

## 4. 社区热点

### 讨论最活跃的 Issues

| 排名 | Issue | 评论数 | 核心诉求 |
|:---|:---|:---|:---|
| 🔥1 | [#5890](https://github.com/zeroclaw-labs/zeroclaw/issues/5890) RFC: Multi-agent UX flow | 10 | **多智能体编排的设计范式**：社区关注如何让多个 Agent 协作而不互相干扰，UX 流如何可视化 |
| 2 | [#6808](https://github.com/zeroclaw-labs/zeroclaw/issues/6808) RFC: Work Lanes, Board Automation | 3 | **治理效率**：贡献者 `Audacity88` 提出轻量级 PR 通道、自动标签清理，反映项目规模扩大后的维护负担 |
| 3 | [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) WhatsApp QR 不显示 | 2 | **即时通讯通道的 onboarding 体验**：用户 `MushiTheMoshi` 明确阻塞，赞项目同时抱怨 Stars 太少 |

### 背后诉求分析

- **多智能体是下一个竞争壁垒**：#5890 的高参与度表明，单 Agent 工具已同质化，多 Agent 协作是差异化关键
- **维护者成为瓶颈**：#6808 的提出暗示现有手工流程（标签、看板）已无法支撑贡献量，需自动化
- **"Best tool out there" 与 Stars 不成正比**：用户认可技术价值但担忧社区可持续性，暗示需加强运营

---

## 5. Bug 与稳定性

| 严重度 | Issue | 状态 | 描述 | Fix PR |
|:---|:---|:---|:---|:---|
| **S1 - 工作流阻塞** | [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) WhatsApp 通道 QR 码不显示 | 已接受，无 stale | 新用户无法完成 WhatsApp  onboarding，完全阻断 | ❌ 无 |
| **S1 - 工作流阻塞** | [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) `vision_provider` 被静默忽略，图片路由至 fallback | 已接受，无 stale | 多模态配置失效，视觉能力不可用 | ❌ 无 |
| **S1 - 工作流阻塞** | [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844) Slack `bot_token` 不支持环境变量 | 已接受，无 stale | 安全合规场景（密钥管理、CI/CD）受阻，#6237 复发 | ❌ 无（原修复 commit `5c2bfdc` 未彻底解决）|
| S2 - 降级行为 | [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836) `setup.bat --minimal` 构建体积 26MB 而非 6MB | 已接受，无 stale | Windows 最小构建承诺未兑现，文档与实现脱节 | ❌ 无 |

**稳定性评估**：3 个 P1 级 Bug 集中在**通道集成层**（WhatsApp、Slack、多模态），显示通道抽象层存在系统性质量缺口。Slack 环境变量问题为**回归缺陷**（#6237 声称已修），需根因分析。无关联 Fix PR，修复响应存在滞后风险。

---

## 6. 功能请求与路线图信号

### 高优先级新功能

| Issue | 提出者 | 纳入下一版本概率 | 判断依据 |
|:---|:---|:---|:---|
| [#6850](https://github.com/zeroclaw-labs/zeroclaw/issues/6850) `MemoryStrategy` trait 解耦记忆策略与存储后端 | `fanchanghu` | ⭐⭐⭐⭐⭐ | 架构债务清理，与 TUI 无直接冲突，社区呼声高 |
| [#6827](https://github.com/zeroclaw-labs/zeroclaw/issues/6827) 支持 jina.ai 作为 `web_search` 提供程序 | `phrozen` | ⭐⭐⭐⭐⭐ | 零成本集成（10M 免费请求），增强工具生态，已标记 `in-progress` |
| [#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820) ACP 协议扩展：diff/文件提案消息类型 | `singlerider` | ⭐⭐⭐⭐⭐ | TUI 核心依赖，已部分实现（"What's already shipped"）|
| [#6837](https://github.com/zeroclaw-labs/zeroclaw/issues/6837) Runtime RPC 调度层与 Unix socket 传输 | `singlerider` | ⭐⭐⭐⭐⭐ | TUI 基础设施，XL 规模，已启动 |
| [#6818](https://github.com/zeroclaw-labs/zeroclaw/issues/6818) `--ephemeral` 守护进程模式 | `singlerider` | ⭐⭐⭐⭐☆ | 边缘/无服务器部署刚需，实现简单 |

### 路线图信号

- **TUI 作为 v0.90 或 v1.0 的标志性功能**：8 个关联 Issue 的批量创建非偶然，预计将在未来 2-4 周进入密集实现期
- **记忆系统重构**：#6850 的 `MemoryStrategy` trait 与现有 `status:in-progress` 的 #6826（TUI Tracker）并行，可能构成"终端原生 + 可插拔记忆"的双卖点
- **通道即产品**：Lark/Feishu 的审批与 cron 投递（PR #6852, #6851）显示企业 IM 集成优先级上升

---

## 7. 用户反馈摘要

### 真实痛点

> *"after com[pleting]... whatsapp channel not showing QR"* — `MushiTheMoshi`, [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847)

**Onboarding 脆性**：通道配置流程缺乏诊断工具，用户卡在"无反馈"状态。

> *"setup.bat --minimal produces ~26 MB build instead of ~6 MB"* — `rockswang`, [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836)

**文档可信度危机**：官方文档承诺与实现不符，损害 Windows 开发者信任。

> *"slack bot_token needs to be in the configuration and cannot be supplied by environment variable"* — `mgstoyanov`, [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844)

**安全合规缺口**：云原生/企业用户无法使用外部密钥管理（Vault、K8s secrets）。

### 满意与认可

> *"Best tool out there. Wishing way more stars."* — `MushiTheMoshi`

**技术口碑与社区规模不匹配**：产品能力强但 GitHub Stars 增长缓慢，可能因：
- 缺乏终端用户可感知的"杀手级演示"
- 文档/官网 SEO 不足
- 未进入 Hacker News、Product Hunt 等流量入口

---

## 8. 待处理积压

### 长期无响应的高风险 PR

| PR | 创建时间 | 最后更新 | 状态 | 风险 |
|:---|:---|:---|:---|:---|
| [#5779](https://github.com/zeroclaw-labs/zeroclaw/pull/5779) TOTP 门控 shell 命令（安全关键） | 2026-04-15 | 2026-05-22 | `needs-author-action`, `needs-maintainer-review` | **38天悬停**，安全功能停滞，作者与维护者双向阻塞 |
| [#5987](https://github.com/zeroclaw-labs/zeroclaw/pull/5987) Nix flake 支持 | 2026-04-22 | 2026-05-22 | `needs-author-action` | **31天**，Nix 社区无法使用，重复劳动风险 |
| [#5652](https://github.com/zeroclaw-labs/zeroclaw/pull/5652) Anthropic/Bedrock 原生扩展思考 | 2026-04-11 | 2026-05-22 | `needs-author-action` | **42天**，推理能力差异化功能，竞争对手可能抢先 |
| [#5187](https://github.com/zeroclaw-labs/zeroclaw/pull/5187) ARM64 Docker 目标 | 2026-04-02 | 2026-05-22 | `needs-author-action` | **51天**，Apple Silicon / ARM 服务器部署受阻 |
| [#6611](https://github.com/zeroclaw-labs/zeroclaw/pull/6611) 文件轮转 crate | 2026-05-13 | 2026-05-22 | `status:blocked`, `needs-author-action` | 10天但已标记阻塞，XL 规模，可能依赖其他重构 |

### 维护者行动建议

1. **立即**：指派 #5779 审查者或关闭并重新设计——安全功能不应无限期悬停
2. **本周**：批量处理 `needs-author-action` 标签 PR，明确"需要作者做什么"的具体评论
3. **建立 SLA**：对 `risk: high` + `needs-author-action` 超 14 天的 PR 自动触发维护者复审

---

*本日报基于 ZeroClaw GitHub 公开数据生成，所有链接指向 github.com/zeroclaw-labs/zeroclaw。*

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*