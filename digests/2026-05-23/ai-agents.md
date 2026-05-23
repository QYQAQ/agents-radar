# OpenClaw 生态日报 2026-05-23

> Issues: 500 | PRs: 500 | 覆盖项目: 13 个 | 生成时间: 2026-05-23 00:30 UTC

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

## 1. 今日速览

OpenClaw 今日保持**极高活跃度**：24小时内 Issues 更新 500 条（433 活跃/新开，67 关闭），PR 更新 500 条（386 待合并，114 已合并/关闭），无新版本发布。项目正处于**密集迭代期**，核心聚焦在**认证安全加固**、**会话稳定性修复**、**多平台覆盖扩展**三大主线。社区对 Linux/Windows 桌面端（#75，105 评论）和预构建 Android APK（#9443）的跨平台诉求持续高涨，同时安全类 Issue（密钥掩码 #10659、隐私泄漏 #85240）获得快速响应，显示维护团队对生产就绪性的重视。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 今日合并/关闭的重要 PR

| PR | 作者 | 核心贡献 | 状态 |
|:---|:---|:---|:---|
| [#85554](https://github.com/openclaw/openclaw/pull/85554) | shakkernerd | **OpenAI 视频编辑路由修复**：将视频编辑请求正确路由至 `/v1/videos/edits` 端点，区分文本/图像生成视频与视频编辑场景 | ✅ 已合并 |
| [#84439](https://github.com/openclaw/openclaw/pull/84439) | TurboTheTurtle | **配置预检日志抑制**：替换全局 `process.stdout.write` 猴子补丁为异步作用域抑制，解决并发场景下日志干扰问题 | ✅ 已合并 |
| [#65212](https://github.com/openclaw/openclaw/pull/65212) | SYU8384 | **QMD 文件路径规范化**：修复直接文件路径被误作集合根目录的问题，提升内存索引健壮性 | ✅ 已合并 |
| [#81304](https://github.com/openclaw/openclaw/pull/81304) | MoerAI | **保留用户主模型设置**：修复设置向导应用认证时静默覆盖用户自定义默认模型的问题 | ✅ 已合并 |
| [#80882](https://github.com/openclaw/openclaw/pull/80882) | jameswniu | **WhatsApp 连接稳定性**：通过 presence keepalive 消除 ~30 分钟空闲断连问题，大幅降低重连频率 | ✅ 已合并 |
| [#85512](https://github.com/openclaw/openclaw/pull/85512) | jason-allen-oneal | **包下载安全加固**：`source=url` 场景下拒绝不安全 URL（禁止非 HTTPS、URL 凭据、私有/内部主机等） | ⏳ 待合并（需作者更新） |

### 架构级推进

- **运行时内部化**（[#85341](https://github.com/openclaw/openclaw/pull/85341)，steipete）：将原 Pi agent/runtime 实现内部化为 OpenClaw 自有 `src/agents/` 包，涉及 40+ 扩展的兼容性改造，是**项目独立品牌化的关键里程碑**
- **网关内存边界控制**（[#79068](https://github.com/openclaw/openclaw/pull/79068)，bryangauvin）：压紧 SessionManager 内存中的 transcript 保留量，解决长会话 OOM 问题

---

## 4. 社区热点

### 高讨论 Issue（评论数 TOP）

| Issue | 评论 | 👍 | 核心诉求 | 链接 |
|:---|:---|:---|:---|:---|
| **#75 Linux/Windows Clawdbot Apps** | 105 | 75 | **跨平台桌面端覆盖**：已有 macOS/iOS/Android，强烈需要 Linux/Windows 同等功能集 | [链接](https://github.com/openclaw/openclaw/issues/75) |
| #9443 预构建 Android APK | 24 | 1 | 降低 Android 使用门槛，无需自行编译 | [链接](https://github.com/openclaw/openclaw/issues/9443) |
| #44925 Subagent 完成静默丢失 | 14 | 0 | **可靠性**：超时/错误时无重试、无通知、无自动重启 | [链接](https://github.com/openclaw/openclaw/issues/44925) |
| #12602 Slack Block Kit 支持 | 13 | 0 | **交互体验**：富文本、CRM 摘要、数据库查询结果的可视化呈现 | [链接](https://github.com/openclaw/openclaw/issues/12602) |
| #10659 密钥掩码系统 | 12 | 4 | **安全**：防止 Agent 通过提示注入提取原始 API Key | [链接](https://github.com/openclaw/openclaw/issues/10659) |

### 热点分析

- **#75 的 75 个 👍 是今日最高社区信号**，反映企业/开发者部署场景对 Linux 服务器的刚性需求，以及 Windows 桌面用户的规模化增长
- **安全类 Issue 获得"钻石龙虾"评级**（#10659、#6731、#13583），表明安全评审流程已成为功能合并的硬性门槛

---

## 5. Bug 与稳定性

| 优先级 | Issue | 描述 | 影响 | Fix PR 状态 |
|:---|:---|:---|:---|:---|
| **P0** | [#85240](https://github.com/openclaw/openclaw/issues/85240) | **跨用户隐私泄漏**：`relevant-memories` 召回未按 `sender_id` 隔离 | 安全/隐私 | ✅ **当日关闭**（快速响应） |
| **P1** | [#85333](https://github.com/openclaw/openclaw/issues/85333) | `openclaw doctor --fix` 性能回归：55s → 229s+（会话快照路径遍历瓶颈） | 运维效率 | 🔍 调查中（需实时复现） |
| **P1** | [#55334](https://github.com/openclaw/openclaw/issues/55334) | `sessions.json` 无界增长导致网关 OOM（`skillsSnapshot` 重复存储） | 可用性/崩溃 | 🔍 待修复 |
| **P1** | [#44925](https://github.com/openclaw/openclaw/issues/44925) | Subagent 完成静默丢失（无重试/通知/自动重启） | 消息丢失 | 🔍 待修复 |
| **P1** | [#57901](https://github.com/openclaw/openclaw/issues/57901) | Safeguard 压缩忽略 `compaction.model` 配置，使用会话模型 | 配置失效 | 🔍 待修复（有关联 PR） |
| **P1** | [#52249](https://github.com/openclaw/openclaw/issues/52249) | ACP 父会话等待子完成时卡住，需手动刷新 | 会话状态 | 🔍 待修复 |
| **P1** | [#71992](https://github.com/openclaw/openclaw/issues/71992) | Control UI 每条助手回复重复显示（#5964/#39469 回归） | 用户体验 | 🔍 待修复 |
| **P1** | [#57019](https://github.com/openclaw/openclaw/issues/57019) | 会话写锁竞争：异步释放可能删除新获取的锁 | 数据一致性 | 🔍 待修复（有关联 PR） |
| **P2** | [#58479](https://github.com/openclaw/openclaw/issues/58479) | ✅ **已关闭**：Control UI 审批成功但 exec 未消费，生成新审批 ID | 回归/审批流 | ✅ 已关闭 |
| **P2** | [#53399](https://github.com/openclaw/openclaw/issues/53399) | 浏览器控制服务器挂起：`npx chrome-devtools-mcp` 在网关进程内 spawn 卡住 | 崩溃循环 | 🔍 需实时复现 |

### 稳定性专项

- **会话系统**是今日 Bug 最密集的领域（4/9 个 P1），涉及状态管理、锁机制、内存边界，反映分布式 Agent 编排的固有复杂性
- **性能回归 #85333** 值得警惕：`doctor` 工具是用户首选诊断手段，4-5x 减速将直接放大支持成本

---

## 6. 功能请求与路线图信号

| 功能 | Issue | 信号强度 | 纳入可能性分析 |
|:---|:---|:---|:---|
| **Linux/Windows 桌面端** | [#75](https://github.com/openclaw/openclaw/issues/75) | 🔥🔥🔥 极高 | 已有 macOS 实现基础，技术可行性高，但需维护者资源投入；105 评论+75👍 是压倒性社区信号 |
| **预构建 Android APK** | [#9443](https://github.com/openclaw/openclaw/issues/9443) | 🔥🔥 高 | CI/CD 发布流程扩展，成本较低，可能快速实现 |
| **密钥掩码系统** | [#10659](https://github.com/openclaw/openclaw/issues/10659) | 🔥🔥 高 | 安全团队已标记 `needs-security-review`，架构清晰，下一版本高概率纳入 |
| **Slack Block Kit** | [#12602](https://github.com/openclaw/openclaw/issues/12602) | 🔥🔥 高 | 企业 Slack 集成场景刚需，PR 就绪度取决于社区贡献 |
| **安全/不安全 ClawdBot 模式** | [#6731](https://github.com/openclaw/openclaw/issues/6731) | 🔥 中 | 涉及 Rust 重写提议，范围过大，更可能分解为沙箱配置项 |
| **原生密钥管理集成** (AWS Secrets Manager/Vault) | [#13610](https://github.com/openclaw/openclaw/issues/13610) | 🔥🔥 高 | 与 #10659 互补，企业部署刚需，技术路径清晰 |
| **会话快照 save/load** | [#13700](https://github.com/openclaw/openclaw/issues/13700) | 🔥 中 | 开发体验优化，实现成本中等 |
| **Vapi 语音通话提供商** | [#13337](https://github.com/openclaw/openclaw/issues/13337) | 🔥 中 | 语音插件扩展，已有 Bounty 声明（ShunsukeHayashi），社区驱动 |
| **Gemini 3.1 Flash-Lite GA 迁移** | [#80380](https://github.com/openclaw/openclaw/issues/80380) | 🔥🔥 高 | 模型版本例行更新，低阻力，预计快速合并 |

### 路线图推断

下一版本（2026.6.x）可能聚焦：**安全加固套件**（密钥掩码+原生 KMS+强制策略执行）、**跨平台客户端补齐**（Linux/Windows/Android）、**会话稳定性重构**（锁机制+内存边界+子代理可靠性）。

---

## 7. 用户反馈摘要

### 痛点

| 反馈来源 | 痛点 | 场景 |
|:---|:---|:---|
| #75, #9443 | **平台覆盖缺口** | "我们有 macOS/iOS/Android，但 Linux 服务器和 Windows 桌面用户被排除在外" |
| #44925 | **子代理可靠性黑洞** | "任务完成后结果消失，没有任何通知，用户以为还在处理" |
| #55334 | **网关内存泄漏** | "50-100 MB/min 增长，最终 OOM 杀死，生产环境不可接受" |
| #85240 | **隐私隔离失效** | "用户 A 的私人记忆被注入到用户 B 的对话中"（P0 安全） |
| #85333 | **诊断工具性能退化** | "`doctor --fix` 从 55 秒变成 229 秒，运维窗口被拉长" |
| #9637 | **TUI 无障碍缺失** | "屏幕阅读器用户被 emoji 和 Unicode 符号淹没" |

### 满意/期待

- **WhatsApp 稳定性修复 #80882** 获得隐性认可（无负面反馈，快速合并）
- **Codex 集成 #85533** 的 API Key 粘贴认证路径，解决 OAuth 令牌与 API Key 混淆的入门障碍
- **动态模型发现 #10687** 被标记为 `maintainer` 关注，反映 OpenRouter 等快速迭代目录的适配需求

---

## 8. 待处理积压

| Issue/PR | 创建时间 | 最后更新 | 风险 | 提醒 |
|:---|:---|:---|:---|:---|
| [#75](https://github.com/openclaw/openclaw/issues/75) Linux/Windows Apps | 2026-01-01 | 2026-05-23 | ⚠️ **5个月无实质进展**，社区耐心消耗 | 需产品决策：是否纳入 Q3 路线图或明确委托社区 Bounty？ |
| [#6731](https://github.com/openclaw/openclaw/issues/6731) Safe/Unsafe ClawdBot | 2026-02-02 | 2026-05-22 | ⚠️ Rust 重写提议范围失控 | 建议拆分为：1) 沙箱配置 2) 内存安全长期研究 |
| [#10687](https://github.com/openclaw/openclaw/issues/10687) 动态模型发现 | 2026-02-06 | 2026-05-23 | ⚠️ `maintainer` 标签但无 assignee | OpenRouter 目录日更，静态目录技术债务累积 |
| [#11665](https://github.com/openclaw/openclaw/issues/11665) Webhook 多回合会话 | 2026-02-08 | 2026-05-22 | ⚠️ 文档承诺与实际行为不符 | 影响 `/hooks/agent` 核心契约，需优先修复或更新文档 |
| [#83535](https://github.com/openclaw/openclaw/pull/83535) WhatsApp RTT 优化 | 2026-05-18 | 2026-05-23 | ⏳ XL 规模，状态为 waiting on author | 作者 vincentkoc 需响应维护者反馈，避免过期 |

---

*日报生成时间：2026-05-23 | 数据来源：OpenClaw GitHub 公开 API 与事件流*

---

## 横向生态对比

# 个人 AI 助手/自主智能体开源生态横向对比分析
**报告日期：2026-05-23**

---

## 1. 生态全景

个人 AI 助手开源生态正处于**从"对话工具"向"自主智能体平台"跃迁的关键节点**。头部项目（OpenClaw、ZeroClaw、IronClaw）日均 Issues/PR 处理量突破 50+，显示工程化密度极高；多模态能力（图像生成、语音通话、TTS）成为标配门槛，而非差异化卖点；MCP（Model Context Protocol）工具生态与跨平台客户端覆盖（Linux/Windows/Android）构成新一轮军备竞赛焦点。与此同时，**会话稳定性、数据可靠性、隐私隔离**等"基础工程"问题反复出现，揭示行业仍处于生产就绪性的攻坚期。

---

## 2. 各项目活跃度对比

| 项目 | Issues (24h) | PRs (24h) | 合并/关闭 | 待处理 | 新版本 | 健康度评估 |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **OpenClaw** | 500 (433活跃/67关闭) | 500 (386待合/114已合关) | 114 | 386 | ❌ 无 | 🔶 **极高活跃，合并瓶颈严重** — 18%合并率远低于健康线，P1 Bug修复响应存在结构性延迟 |
| **NanoClaw** | 28活跃 | 31 (3待合/28已合关) | 28 | 3 | ❌ 无 | 🟢 **高效流转** — 90%当日关闭率，但Apple Container技能三连崩暴露分支治理缺陷 |
| **Hermes Agent** | 50 (47活跃/3关闭) | 50 (41待合/9已合关) | 9 | 41 | ❌ 无 | 🔶 **高讨论密度，合并阻滞** — 41条PR待合并，3个P1无fix PR，SIGTERM处理系统性缺陷 |
| **IronClaw** | 23 (19活跃/4关闭) | 50 (36待合/14已合关) | 14 | 36 | ❌ 无 | 🟡 **Reborn架构冲刺期** — XL级PR密集，E2E持续12天失败阻塞发布信心 |
| **ZeroClaw** | 37 (30活跃/7关闭) | 50 (36待合/14已合关) | 14 | 36 | ❌ 无 | 🟢 **渠道稳定性优先** — WhatsApp S1故障当日解除，MCP工具过滤修复响应快 |
| **CoPaw** | 24 (17活跃/7关闭) | 23 (13待合/10已合关) | 10 | 13 | ❌ 无 | 🔶 **功能交付快，数据可靠性红灯** — P0级聊天记录消失12评论无PR，信任危机风险 |
| **Moltis** | 7 (1活跃/7关闭) | 9 (0待合/9已合关) | 9 | 0 | ❌ 无 | 🟢 **精益冲刺** — 100%当日合并，Docker部署链系统性修复，单点贡献集中 |
| **LobsterAI** | 1新/4积压 | 12 (9待合/12已合关) | 12 | 9 | ✅ 2026.5.22 | 🔶 **产品交付强，社区治理弱** — Subagent模块快速成熟，安全PR 45天零响应 |
| **NanoBot** | 7 | 20 (8待合/12已合关) | 12 | 8 | ❌ 无 | 🟢 **多模态+安全双轮驱动** — 图像生成三平台覆盖，心跳机制4个月技术债务待根治 |
| **PicoClaw** | 3新/7关闭 | 20 (8待合/12已合关) | 12 | 8 | 🔧 nightly | 🟡 **清理型活跃** — 积压stale问题集中处理，Agent间协作成v0.3.0核心叙事 |
| **NullClaw** | 0 | 4 (4待合/0已合关) | 0 | 4 | ❌ 无 | 🔴 **维护模式** — 46天Cron PR阻塞，零Issues活动，外部贡献者生态薄弱 |
| **TinyClaw** | — | — | — | — | — | ⚫ **无活动** |
| **ZeptoClaw** | — | — | — | — | — | ⚫ **无活动** |

---

## 3. OpenClaw 在生态中的定位

| 维度 | OpenClaw 表现 | 生态对比 |
|:---|:---|:---|
| **规模定位** | **绝对体量领导者** — 500 Issues/500 PR 日活，超第二名10倍 | Hermes/ZeroClaw/IronClaw 约50级；NanoClaw/Moltis 约30级；其余<25 |
| **技术路线** | **"全栈网关"模式** — 认证安全加固 + 会话稳定性 + 多平台覆盖三线并行 | ZeroClaw 侧重"终端优先"（TUI/Ratatui）；IronClaw 押注"Rust内核+Reborn架构"；NanoBot 走"AI操作系统"（CLI Apps生态） |
| **核心优势** | ① **安全评审硬度**（"钻石龙虾"评级机制，#10659/#85240当日关闭）；② **企业通道覆盖**（WhatsApp/Slack/Discord全矩阵）；③ **运行时内部化里程碑**（#85341剥离Pi依赖） | 对比：ZeroClaw的Dream Mode记忆巩固、IronClaw的Hooks框架性能优化、Moltis的语音通道完整性 |
| **结构性短板** | **合并吞吐瓶颈**（386待合/114已合=3.4:1）与 **P1修复延迟**（3/3无关联PR） | NanoClaw 90%关闭率、Moltis 100%当日合并形成鲜明反差 |
| **社区规模** | 105评论Issue（#75跨平台）为生态最高社区信号，但5个月无实质进展 | ZeroClaw #5849（11评论Dream Mode）、CoPaw #4620（12评论数据丢失）讨论深度接近，但响应速度更优 |

> **结论**：OpenClaw 是生态的**"基础设施锚点"**——最大流量、最全通道、最硬安全门槛，但工程效率与社区治理精细度已被中型项目超越，存在"大而不快"的风险。

---

## 4. 共同关注的技术方向

| 技术方向 | 涉及项目 | 具体诉求 | 紧迫程度 |
|:---|:---|:---|:---:|
| **跨平台桌面客户端（Linux/Windows）** | OpenClaw #75 (105评论, 75👍)、NanoClaw #2588-#2590、Hermes #20660/#30660 | macOS独占→全平台覆盖；ARM64边缘部署；Apple Container网络适配 | 🔥🔥🔥 |
| **MCP/工具生态治理** | ZeroClaw #6699 (S1)、IronClaw #3805-#3806、NanoBot #3963 (CLI Apps)、PicoClaw #2929 (Agent协作) | 工具过滤前缀匹配、WASM读写能力、Agent间一等通信协议 | 🔥🔥🔥 |
| **会话稳定性与数据可靠性** | OpenClaw #55334/#44925 (OOM/静默丢失)、CoPaw #4620 (P0数据消失)、Hermes #19471/#30636 (SIGTERM崩溃/state.db损坏)、NanoBot #3028 (心跳4个月未根治) | 长会话内存边界、子代理可靠性、聊天记录持久化、优雅关闭 | 🔥🔥🔥 |
| **多模态能力补齐** | NanoBot #3946/#3954 (Ollama/OpenAI图像生成)、Moltis #1041/#1043 (TTS格式适配)、OpenClaw #85554 (视频编辑路由) | 图像生成三平台覆盖、语音合成格式生态兼容、视频编辑 | 🔥🔥 |
| **隐私/安全加固** | OpenClaw #10659 (密钥掩码)、LobsterAI #1534/#1535 (日志脱敏/KV白名单, 45天未响应)、NanoBot #3928 (SSRF)、Hermes #30664 (路径遍历) | API Key防提取、渲染进程隔离、传输层错误保留 | 🔥🔥🔥 |
| **定时任务/自主执行** | NullClaw #783 (Cron, 46天阻塞)、IronClaw #3873 (Trigger Loop)、CoPaw #4434 (定时任务上下文隔离) | Agent脱离人工触发、按调度自主执行、审计追踪 | 🔥🔥 |
| **配置云同步/跨设备** | Hermes #20510 (6👍)、ZeroClaw #6817 (Session级参数覆盖) | 多设备工作流同步、无需daemon重载的动态调整 | 🔥🔥 |

---

## 5. 差异化定位分析

| 项目 | 功能侧重 | 目标用户 | 技术架构关键差异 |
|:---|:---|:---|:---|
| **OpenClaw** | 企业级多通道网关 + 安全合规 | 中大型企业、SaaS集成商 | TypeScript/Node网关核心；认证安全"钻石龙虾"评审；Pi运行时内部化 |
| **ZeroClaw** | 终端原生体验 + 记忆巩固 | 开发者、极客、自托管用户 | Rust核心；TUI(Ratatui)优先；Dream Mode本地优先+可选LLM反射；OTel可观测性 |
| **IronClaw** | Reborn架构 + 第三方技能生态 | 平台构建者、企业IT | Rust全栈；Hooks框架(信任原语)；WASM技能执行；Lane模块化交付 |
| **NanoBot** | "AI操作系统" + 多模态生产工具 | 自动化工程师、CLI用户 | CLI Apps生态(对接CLI-Anything)；BM25技能路由减60%提示；SSRF+命令确认安全基线 |
| **Hermes Agent** | 生产力套件集成 + 跨平台控制 | 知识工作者、多账户用户 | Kanban任务管理；Google/MS双生态；Docker镜像64%缩减；原生跨平台桌面控制 |
| **Moltis** | 语音通道完整性 + Docker自托管 | 语音交互场景、复杂基础设施用户 | Rust；Piper/OpenAI TTS双适配；Twilio电话通道；Vault加密可选禁用 |
| **LobsterAI** | Subagent协作 + 模型配置灵活性 | 多Agent协作开发者、企业用户 | Electron桌面端；SQLite持久化；Thinking块可视化；OpenClaw网关事件扩展 |
| **CoPaw** | 国内通道适配 + 插件生态 | 中国用户、微信/钉钉企业用户 | 微信/钉钉深度集成；MiniMax/DeepSeek国产模型适配；Tauri桌面端探索 |
| **NanoClaw** | Claude Code替代 + 多AI提供商中立 | 编码场景、Anthropic生态迁移者 | Apple Container战略路径；Codex完整支持；rtk token压缩；上下文窗口自省 |
| **PicoClaw** | 轻量级多Agent + 边缘部署 | IoT/ARM64场景、Telegram用户 | Go；Seahorse历史管理；Agent间spawn/delegate语义；论坛话题上下文保持 |
| **NullClaw** | 去中心化AI + 定时自治 | Web3开发者、成本敏感用户 | NEAR AI Cloud接入；Cron DB-backed调度；POSIX正确性修复 |

---

## 6. 社区热度与成熟度

### 快速迭代阶段（Feature Rush）

| 项目 | 特征 | 风险 |
|:---|:---|:---|
| **IronClaw** | Reborn架构四大主线并行，XL级PR密集，M1/M2近Beta | E2E 12天失败阻塞发布；子代理阻塞恢复缺陷 |
| **NanoClaw** | 28/31当日关闭，Codex/rtk/上下文自省三箭齐发 | Apple Container技能三连崩，分支治理失效 |
| **Moltis** | 9/9当日合并，penso单点爆发，Docker链系统修复 | 单点贡献集中，知识分散风险 |
| **LobsterAI** | Subagent从实验性→一级模块，3日内连续版本发布 | 安全PR 45天零响应；依赖升级50天堆积 |

### 质量巩固阶段（Stabilization）

| 项目 | 特征 | 关键债务 |
|:---|:---|:---|
| **ZeroClaw** | WhatsApp S1当日解除，MCP修复响应快，治理RFC启动 | 153 commit批量回滚28天未决；ARM64构建51天悬停 |
| **NanoBot** | 图像生成三平台覆盖完成，国际化9语言补全 | 心跳机制4个月未根治，防递归指令为权宜之计 |
| **PicoClaw** | 7个stale问题集中清理，nightly持续发布 | 8个待合PR评审带宽不足；Agent协作架构待验证 |

### 规模扩张与治理挑战（Scale Pain）

| 项目 | 特征 | 核心矛盾 |
|:---|:---|:---|
| **OpenClaw** | 500/500日活，安全评审硬度标杆 | 3.4:1待合/已合比率，"大而不快"；#75跨平台5个月无进展 |
| **Hermes Agent** | 50/50日活，功能扩张与稳定性并行 | 41待合PR，3个P1无fix PR，SIGTERM系统性缺陷 |
| **CoPaw** | 国内通道适配快，插件生态活跃 | P0数据丢失12评论无PR，信任根基动摇 |

### 停滞/维护模式

| 项目 | 特征 | 诊断 |
|:---|:---|:---|
| **NullClaw** | 零Issues，46天Cron PR阻塞，4PR全pending | 核心团队内部审查，外部生态未形成 |
| **TinyClaw/ZeptoClaw** | 24小时零活动 | 项目休眠或团队转移 |

---

## 7. 值得关注的趋势信号

### 信号一："Agent自主性"从噱头走向工程化
- **证据**：ZeroClaw Dream Mode 5阶段引擎（gather→reflect→consolidate→prune→sleep）、NullClaw Cron DB-backed调度、IronClaw Trigger Loop设计提案
- **价值**：开发者需关注**离线学习架构**与**任务调度可靠性**的交叉设计，而非仅追求即时响应

### 信号二：MCP成为事实标准，但工具治理严重滞后
- **证据**：ZeroClaw #6699（S1工具过滤失效）、IronClaw Lane 6 GitHub WASM能力、PicoClaw #2929（Agent间协作协议）
- **价值**：MCP生态爆发前夜，**前缀匹配、懒加载、版本协商**等"微协议"将成为兼容性瓶颈

### 信号三："精简主义"反噬技能膨胀
- **证据**：NanoBot #3958/#3959（反对weather内置）、mraad连续Issue、BM25路由减60%提示的PR #3865
- **价值**：Agent平台的**技能发现机制**比技能数量更重要，动态加载+按需路由是架构必选项

### 信号四：终端原生体验（TUI/CLI）复兴
- **证据**：ZeroClaw #6848（Ratatui大型PR）、NanoBot CLI Apps生态、NanoClaw Codex-only安装路径
- **价值**：GUI并非唯一答案，**开发者工作流嵌入**（IDE/终端/脚本）的Agent交互模式正在崛起

### 信号五：数据可靠性成为信任分水岭
- **证据**：CoPaw #4620（P0聊天记录消失）、OpenClaw #85240（跨用户隐私泄漏）、Hermes #30636（state.db三天坏三次）
- **价值**：Agent产品从"好玩"到"可用"的临界点在于**持久化契约**——用户必须确信"我的数据在"

### 信号六：国产模型适配成为区域化壁垒
- **证据**：CoPaw MiniMax/Gemma/DeepSeek专项修复、LobsterAI Qwen 3.6 Plus编码修正、OpenClaw Gemini 3.1 Flash-Lite迁移
- **价值**：全球化Agent平台需建立**模型能力声明机制**（非硬编码支持列表），否则每次模型迭代都是适配灾难

---

*报告基于2026-05-23各项目GitHub公开数据生成 | 分析师：AI智能体生态观察*

---

## 同赛道项目详细报告

<details>
<summary><strong>NanoBot</strong> — <a href="https://github.com/HKUDS/nanobot">HKUDS/nanobot</a></summary>

# NanoBot 项目动态日报 | 2026-05-23

---

## 1. 今日速览

NanoBot 今日保持**高活跃度**，24小时内20个PR流转（12条已合并/关闭，8条待审），7个Issues更新，显示社区与核心团队同步推进。核心工作集中在**WebUI体验优化**（locale补全、图片渲染、文件编辑计数修复）、**安全加固**（SSRF防护、危险命令确认）、**基础设施扩展**（Ollama图像生成、OpenAI/Codex图像生成、CLI Apps生态）三大方向。值得关注的是，长期悬而未决的**心跳机制重复创建定时任务**问题（Issue #3028）终于有关键PR #2364关闭，但方案采用"防递归指令注入"而非根本重构，后续仍需观察。整体项目健康度良好，合并节奏快，但待审PR中多个涉及架构级变更（BM25技能路由、Manifest LLM路由、长期记忆MECE重构），需要维护者投入评审资源。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭的关键PR（12条）

| PR | 作者 | 核心贡献 | 项目推进价值 |
|:---|:---|:---|:---|
| [#3946](https://github.com/HKUDS/nanobot/pull/3946) | HaisamAbbas | **Ollama原生图像生成支持** | 补齐本地部署关键能力，x/z-image-turbo等本地模型可用 |
| [#3954](https://github.com/HKUDS/nanobot/pull/3954) | ZegWe | **OpenAI/Codex图像生成支持** | 覆盖主流商业API，Codex订阅用户可通过Responses工具链生成图像 |
| [#3963](https://github.com/HKUDS/nanobot/pull/3963) | Re-bin | **CLI Apps生态接入** | 对接CLI-Anything注册表，nanobot向"AI操作系统"演进的关键一步 |
| [#3928](https://github.com/HKUDS/nanobot/pull/3928) | Hinotoi-agent | **SSRF安全加固：重定向目标验证** | 封堵`web_fetch`工具的重定向时间隙攻击，安全基线提升 |
| [#3937](https://github.com/HKUDS/nanobot/pull/3937) | yorkhellen | **危险命令用户确认机制** | `exec`工具执行rm/curl等高危操作前强制确认，降低误操作风险 |
| [#3960](https://github.com/HKUDS/nanobot/pull/3960) | chengyongru | **apply_patch重构：移除废弃patch模式** | 技术债务清理，工具接口简化，维护成本降低 |
| [#3961](https://github.com/HKUDS/nanobot/pull/3961) | Yuxin-Lou | **Responses API重复ID去重** | 修复Codex会话恢复失败问题，稳定性修复 |
| [#3929](https://github.com/HKUDS/nanobot/pull/3929) | HaisamAbbas | **图像生成HTTP层统一** | MiniMax/AIHubMix代码复用，Gemini baseURL文档补齐 |
| [#3962](https://github.com/HKUDS/nanobot/pull/3962) | yu-xin-c | **zh-TW/ja locale补全** | WebUI国际化覆盖度提升 |
| [#3964](https://github.com/HKUDS/nanobot/pull/3964) | yu-xin-c | **es/fr/id/ko/vi locale补全** | 多语言支持扩展至7种新语言 |
| [#3965](https://github.com/HKUDS/nanobot/pull/3965) | Re-bin | **Windows CI覆盖CLI Apps测试** | 跨平台兼容性保障，消除Unix假设 |
| [#3957](https://github.com/HKUDS/nanobot/pull/3957) | Re-bin | **WebUI文件编辑计数修复** | 消除误导性diff统计，UX打磨 |

**里程碑意义**：今日合并标志着NanoBot在**多模态能力**（图像生成三平台覆盖）、**安全基线**（SSRF+命令确认）、**生态扩展**（CLI Apps）三个战略方向同时取得进展，项目从"LLM对话工具"向"AI Agent平台"的定位升级清晰可见。

---

## 4. 社区热点

### 讨论最活跃的Issues

| 排名 | Issue | 评论数 | 热度分析 |
|:---|:---|:---|:---|
| 🔥1 | [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI首响应后对话关闭 | **6条** | **已关闭**。Debian网关+WebSocket配置场景下的连接稳定性问题，社区协作定位到WebSocket通道配置与token/stream设置的交互bug，修复验证周期5天，显示社区问题响应效率 |
| 2 | [#3846](https://github.com/HKUDS/nanobot/issues/3846) 多轮对话保留skill内容 | **4条** | **待解决**。核心诉求：当前`read_file`加载skill.md在单轮有效，多轮丢失上下文。用户提出设计级改进方案，涉及工具调用机制重构，👍1显示共鸣 |
| 3 | [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill`列出已禁用技能 | **4条** | **新Bug**。配置`disabledSkills`后UI仍显示，用户期望"lean and mean"的精简体验，与同日提出的[#3958](https://github.com/HKUDS/nanobot/issues/3958)（将weather移出内置）形成诉求组合——**用户反对技能膨胀** |

### 背后诉求分析

- **"精简主义"共识**：mraad连续两Issue（#3958/#3959）反映社区对内置技能过度膨胀的不满，与PR #3865 BM25技能路由（减少60%系统提示）的技术方向形成呼应
- **多轮对话可靠性**：#3846与#3028（心跳重复任务）共同指向**状态管理/上下文持久化**的架构短板
- **WebSocket生产就绪**：#3884的6条评论轨迹显示，从"配置疑问"到"确认bug"到"验证修复"，社区协作模式成熟

---

## 5. Bug 与稳定性

| 严重程度 | Issue/PR | 状态 | 详情 | Fix PR |
|:---|:---|:---|:---|:---|
| 🔴 **高** | [#3956](https://github.com/HKUDS/nanobot/issues/3956) Anthropic API 400错误（工具结果list格式） | **已关闭** | `read_file`读取图片后工具结果以list存储，回传Anthropic时格式不兼容导致会话永久中断 | 同日关闭，推测随#3961或相关PR修复 |
| 🔴 **高** | [#3028](https://github.com/HKUDS/nanobot/issues/3028) 心跳重复创建定时任务 | **仍Open** | 心跳触发时嵌套创建cron，导致问候语重复发送，且无法读取上下文。存在4个月，v0.15即存在 | [#2364](https://github.com/HKUDS/nanobot/pull/2364) 已关闭但方案为"防递归指令注入"，非根本修复；Issue仍Open说明问题未完全解决 |
| 🟡 **中** | [#3959](https://github.com/HKUDS/nanobot/issues/3959) `/skill`列出已禁用技能 | **Open** | 配置失效，UI与配置不一致 | 暂无 |
| 🟡 **中** | [#3884](https://github.com/HKUDS/nanobot/issues/3884) WebUI首响应后对话关闭 | **已关闭** | WebSocket连接异常断开 | 已修复 |
| 🟢 **低** | [#3957](https://github.com/HKUDS/nanobot/pull/3957) WebUI文件编辑计数误导 | **已合并** | 零值/未知diff统计误渲染 | [PR #3957](https://github.com/HKUDS/nanobot/pull/3957) |

**稳定性评估**：Anthropic API兼容性问题的快速关闭（创建即关闭）显示关键供应商集成有响应机制；但**心跳机制作为核心Agent特性，其定时任务重复问题4个月未根治**，需架构级重构而非指令层补丁，是当前最大技术债务。

---

## 6. 功能请求与路线图信号

| 需求 | 来源 | 成熟度 | 纳入下一版本概率 | 判断依据 |
|:---|:---|:---|:---|:---|
| **Ollama图像生成** | Issue #3941 + PR #3946 | ✅ 已合并 | 已发布 | 社区+官方双驱动，HaisamAbbas主导 |
| **OpenAI/Codex图像生成** | PR #3954 | ✅ 已合并 | 已发布 | 官方实现，测试覆盖完整 |
| **CLI Apps生态** | PR #3963 | ✅ 已合并 | 已发布 | Re-bin官方贡献，对接CLI-Anything注册表 |
| **BM25轻量技能路由** | PR #3865 | 🔄 待审 | **高** | 减少60%系统提示，解决技能膨胀痛点，与#3958/#3959诉求一致 |
| **长期记忆MECE重构** | PR #3952 | 🔄 待审 | **中高** | 解决记忆重复膨胀核心问题，chengyongru持续投入 |
| **Manifest LLM路由** | PR #3568 | 🔄 待审（近2月） | **中** | 外部贡献，需维护者评审资源，网关集成价值明确但优先级待确认 |
| **nanobot doctor诊断命令** | PR #3776 | 🔄 待审（9天） | **中高** | 10项自动化检查，降低支持成本，运维体验刚需 |
| **心跳推理与通知解耦** | PR #1443 | 🔄 待审（近3月） | **中** | 架构改进，但#3028未根治可能影响合并优先级 |
| **危险命令确认** | PR #3937 | ✅ 已合并 | 已发布 | 安全基线功能 |
| **天气技能移出内置** | Issue #3958 | 🆕 新提出 | **高** | 与BM25路由、技能精简趋势一致，实现成本低 |

**路线图信号**：下一版本（推测v0.16或v0.17）极可能聚焦**"技能系统重构"**（BM25路由+内置技能清理+多轮skill上下文保留）与**"记忆系统优化"**（MECE去重+Consolidator改进）。图像生成三平台覆盖已阶段性完成。

---

## 7. 用户反馈摘要

### 真实痛点

| 来源 | 痛点 | 场景 |
|:---|:---|:---|
| #3884 aurel-appsthru | **WebSocket连接不稳定** | Debian网关生产部署，首响应后对话断开，影响服务可用性 |
| #3028 jermeyhu | **心跳机制"假智能"** | 期望"偶尔关心"的上下文感知问候，实际变成固定时间机械重复，且无法读取对话历史 |
| #3959 mraad | **配置与UI不一致** | 明确禁用weather技能，/skill仍列出，破坏"精简"承诺的信任感 |
| #3846 mkitsdts | **多轮对话技能失效** | 复杂任务需要跨轮引用skill定义，当前机制迫使重复加载 |

### 满意点

- **图像生成扩展快**：Ollama本地支持从Issue提出到PR合并仅2天（#3941→#3946），显示官方对多模态的重视
- **国际化响应及时**：yu-xin-c连续补全9种语言locale，WebUI全球化体验提升

### 不满意/担忧

- **技术债务处理轻量**：#3028心跳问题4个月，关闭的PR #2364用"防递归指令"绕过而非重构定时任务调度，用户可能担忧根本问题复发
- **技能系统方向摇摆**：内置技能持续增加（weather等），与社区"lean and mean"期望冲突

---

## 8. 待处理积压

### 需维护者优先关注

| 类型 | 条目 | 积压时间 | 风险 | 建议动作 |
|:---|:---|:---|:---|:---|
| **架构级Bug** | [#3028](https://github.com/HKUDS/nanobot/issues/3028) 心跳重复任务 | **42天** | Agent核心特性不可靠，影响用户信任 | 评估PR #1443（解耦推理与通知）+ 要求定时任务调度层重构方案 |
| **长期待审PR** | [#3568](https://github.com/HKUDS/nanobot/pull/3568) Manifest LLM路由 | **23天** | 外部贡献者流失风险，网关生态扩展受阻 | 分配评审人，或明确路线图优先级 |
| **长期待审PR** | [#1443](https://github.com/HKUDS/nanobot/pull/1443) 心跳解耦 | **82天** | 与#3028关联，架构改进停滞 | 结合#3028统一评审，确定是否替代#2364方案 |
| **设计级Issue** | [#3846](https://github.com/HKUDS/nanobot/issues/3846) 多轮skill保留 | **8天** | 技能系统扩展瓶颈 | 关联PR #3865 BM25路由，统一设计评审 |
| **待审PR** | [#3952](https://github.com/HKUDS/nanobot/pull/3952) 长期记忆MECE | **2天** | 高价值但复杂度高 | 优先评审，记忆膨胀直接影响大用户场景 |

---

*日报基于 GitHub 公开数据生成，时间范围：2026-05-22 UTC*

</details>

<details>
<summary><strong>Hermes Agent</strong> — <a href="https://github.com/nousresearch/hermes-agent">nousresearch/hermes-agent</a></summary>

# Hermes Agent 项目动态日报 | 2026-05-23

---

## 1. 今日速览

Hermes Agent 今日维持**极高活跃度**，24小时内产生 **50 条 Issues 更新**（47 条新开/活跃，仅 3 条关闭）与 **50 条 PR 更新**（41 条待合并，9 条已合并/关闭）。社区讨论密度显著，无新版本发布。核心矛盾集中在**网关稳定性**（SIGTERM/SIGKILL 事件循环丢失、`state.db` 损坏）与**平台适配完整性**（WhatsApp 静默响应、Discord/Telegram 身份校验缺失）。同时，国际化（中文 Dashboard）、跨平台桌面控制（Windows/Linux/macOS）及配置云同步等长期需求持续发酵，项目处于**功能扩张与稳定性攻坚并行**的阶段。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭的重要 PR

| PR | 作者 | 进展说明 | 链接 |
|:---|:---|:---|:---|
| **#30671** [CLOSED] i18n: dashboard full Chinese (Simplified) translation | 125938899 | 完整中文 Dashboard 翻译 PR 被关闭（可能因范围过大或策略调整），作者已拆分出更聚焦的 #30672 | [PR #30671](https://github.com/NousResearch/hermes-agent/pull/30671) |
| **#30664** [CLOSED] fix(kanban): harden scratch workspace cleanup | HushUr2Pups8008 | **安全修复**：强化 Kanban scratch 工作区清理，防止路径遍历与误删，标记为 P1 安全级别 | [PR #30664](https://github.com/NousResearch/hermes-agent/pull/30664) |
| **#30665** [CLOSED] feat(kanban): add kanban.default_workspace config option | orlandoburli | 功能被重新提交为 #30668，原 PR 关闭（配置层变更策略调整） | [PR #30665](https://github.com/NousResearch/hermes-agent/pull/30665) |
| **#24661** [CLOSED] fix(gateway): bridge gateway_restart_notification from config.yaml | briandevans | 网关重启通知配置桥接修复，解决配置静默失效问题 | [PR #24661](https://github.com/NousResearch/hermes-agent/pull/24661) |

### 关键推进中的 PR

| PR | 作者 | 推进价值 | 链接 |
|:---|:---|:---|:---|
| **#30660** feat(computer_use): enable Windows via cua-driver-rs | f-trycua | **跨平台桌面控制突破**：解除 macOS 独占限制，Windows 支持落地，补全 #20660 长期 PR 的关键拼图 | [PR #30660](https://github.com/NousResearch/hermes-agent/pull/30660) |
| **#30663** feat(skills): deterministic runtime skill bundles + L1 compact context | hfm77788 | **核心架构优化**：确定性每轮技能预加载 + 上下文压缩分层，直接影响 agent 响应质量与 token 成本 | [PR #30663](https://github.com/NousResearch/hermes-agent/pull/30663) |
| **#27437** build(docker): multi-stage build — 5.6GB → 2GB, 100s → 10s startup | nthrow | **部署体验质变**：镜像体积缩减 64%，启动时间从 100s 降至 10s，云原生场景关键优化 | [PR #27437](https://github.com/NousResearch/hermes-agent/pull/27437) |
| **#26358** fix(gateway): force-release HTTP clients on shutdown | briandevans | **稳定性修复**：网关重启后子 agent 卡死 12+ 分钟的问题，强制释放 HTTP 连接池 | [PR #26358](https://github.com/NousResearch/hermes-agent/pull/26358) |

**整体评估**：今日合并量偏低（关闭 PR 多因策略调整而非合并），但**待合并队列中积压了大量高价值 PR**，尤其是跨平台支持、Docker 优化、网关稳定性等方向，项目处于"蓄力期"，合并吞吐瓶颈值得关注。

---

## 4. 社区热点

### 讨论最活跃的 Issues

| 排名 | Issue | 评论 | 👍 | 核心诉求 | 链接 |
|:---|:---|:---:|:---:|:---|:---|
| 1 | **#7237** [CLOSED] Response truncated due to output length limit | 33 | 4 | **长文本生成截断**——CLI/网关场景下输出长度限制导致响应中断，用户急需流式输出或分段机制 | [Issue #7237](https://github.com/NousResearch/hermes-agent/issues/7237) |
| 2 | **#19471** `--profile` gateway crash loop after SIGTERM→SIGKILL | 4 | 0 | **生产级稳定性**：事件循环丢失导致网关崩溃重启循环，P1 优先级 | [Issue #19471](https://github.com/NousResearch/hermes-agent/issues/19471) |
| 3 | **#15602** google-workspace skill: add multi-account support | 4 | 9 | **企业用户刚需**：多 Google 账户切换，个人/工作场景隔离 | [Issue #15602](https://github.com/NousResearch/hermes-agent/issues/15602) |
| 4 | **#5254** Tool calls repeating when using LM-Studio | 3 | 0 | **第三方兼容性**：LM Studio 本地模型工具调用碎片化，与 OpenAI Codex 同类问题 | [Issue #5254](https://github.com/NousResearch/hermes-agent/issues/5254) |
| 5 | **#30555** Parent session's messages should get persisted before compressed | 3 | 0 | **数据持久化**：上下文压缩前丢失父会话消息，影响长对话连续性 | [Issue #30555](https://github.com/NousResearch/hermes-agent/issues/30555) |

### 热点分析

- **#7237 的 33 条评论**反映长文本生成是高频痛点，虽已关闭但解决方案（流式/分段）未在数据中明确，需追踪是否真正解决
- **#15602 的 9 个 👍** 是今日最高，多账户支持具有明确的付费/企业场景价值
- **#19471 的 P1 标注 + 网关核心组件**表明生产稳定性仍是信任构建的关键障碍

---

## 5. Bug 与稳定性

按严重程度排序：

| 优先级 | Issue | 描述 | 影响范围 | Fix PR 状态 | 链接 |
|:---|:---|:---|:---|:---|:---|
| **P1** | **#19471** | `--profile` gateway SIGTERM→SIGKILL 后事件循环丢失，进入崩溃重启循环 | 网关核心 / 生产部署 | ❌ 无 | [Issue #19471](https://github.com/NousResearch/hermes-agent/issues/19471) |
| **P1** | **#30636** | `state.db` 在 launchd 高负载关机时因 SIGTERM 损坏（macOS） | 数据持久化 / macOS 用户 | ❌ 无 | [Issue #30636](https://github.com/NousResearch/hermes-agent/issues/30636) |
| **P1** | **#30623** | `hermes -z` oneshot 模式在 non-TTY 管道下静默退出（exit 0），API 未调用 | CLI / SSH/cron/自动化 | ❌ 无 | [Issue #30623](https://github.com/NousResearch/hermes-agent/issues/30623) |
| **P2** | **#23975** | 上下文压缩被网关消息中断，降级为 fallback summary marker | 上下文质量 / 网关并发 | ❌ 无 | [Issue #23975](https://github.com/NousResearch/hermes-agent/issues/23975) |
| **P2** | **#18362** | `/busy` 命令标记为 `cli_only`，Telegram/网关用户无法使用（与 onboarding 提示矛盾） | 网关 UX / 平台一致性 | ✅ **#18366** 待合并 | [Issue #18362](https://github.com/NousResearch/hermes-agent/issues/18362) |
| **P2** | **#30653** | model picker 忽略 `key_env`，自定义 provider 显示"0 models listed" | 配置系统 / 模型选择 | ❌ 无 | [Issue #30653](https://github.com/NousResearch/hermes-agent/issues/30653) |
| **P2** | **#30626** | `hermes gateway run` 仅读取启动时 `active_profile`，忽略实时切换 | 网关配置 / 多 profile | ❌ 无 | [Issue #30626](https://github.com/NousResearch/hermes-agent/issues/30626) |
| **P2** | **#30586** | macOS launchd domain 硬编码 `gui/`，SSH-only/无控制台用户无法使用 | macOS 部署 / 服务器场景 | ❌ 无 | [Issue #30586](https://github.com/NousResearch/hermes-agent/issues/30586) |
| **P2** | **#30601** | MCP tool results 含 `EmbeddedResource` 时被静默丢弃 | 工具系统 / MCP 集成 | ❌ 无 | [Issue #30601](https://github.com/NousResearch/hermes-agent/issues/30601) |
| **P2** | **#30565** | Discord 工具集在 `.env` 中配置 `DISCORD_BOT_TOKEN` 时不可用 | 工具发现 / 环境加载顺序 | ❌ 无 | [Issue #30565](https://github.com/NousResearch/hermes-agent/issues/30565) |

**稳定性评估**：**3 个 P1 无 fix PR**，均为网关/CLI 核心路径的崩溃或静默失败，生产可用性受严重威胁。SIGTERM 信号处理（#19471、#30636）存在系统性缺陷，建议维护者优先集中资源。

---

## 6. 功能请求与路线图信号

| Issue/PR | 方向 | 纳入可能性 | 信号强度 | 链接 |
|:---|:---|:---|:---|:---|
| **#15602** google-workspace 多账户支持 | 企业/生产力集成 | ⭐⭐⭐⭐⭐ 高 | 9 👍，明确痛点，有现有 OAuth 架构可参考 | [Issue #15602](https://github.com/NousResearch/hermes-agent/issues/15602) |
| **#20510** 跨设备云同步配置 | 用户生态锁定 | ⭐⭐⭐⭐⭐ 高 | 6 👍，多设备工作流刚需，竞品差异化点 | [Issue #20510](https://github.com/NousResearch/hermes-agent/issues/20510) |
| **#2988** XMPP + OMEMO 加密支持 | 开源/隐私优先用户 | ⭐⭐⭐⭐☆ 中高 | 7 👍，与现有 WhatsApp/Signal 专有协议形成互补 | [Issue #2988](https://github.com/NousResearch/hermes-agent/issues/2988) |
| **#25979** Microsoft 365 Outlook skill | 生产力套件完整性 | ⭐⭐⭐⭐☆ 中高 | 作者已有生产实现，愿 upstream，与 #15602 形成 Google/MS 双生态 | [Issue #25979](https://github.com/NousResearch/hermes-agent/issues/25979) |
| **#30652** 动态模型路由（按任务复杂度） | 成本优化/性能 | ⭐⭐⭐⭐☆ 中高 | 新提交，切中"简单查询用大模型浪费"的普遍痛点 | [Issue #30652](https://github.com/NousResearch/hermes-agent/issues/30652) |
| **#30640** Cursor SDK (Composer 2.5) 集成 | AI 编码工具链 | ⭐⭐⭐☆☆ 中 | 两阶段设计清晰，但依赖外部 SDK 稳定性 | [Issue #30640](https://github.com/NousResearch/hermes-agent/issues/30640) |
| **#24415** OpenRouter 作为 STT provider | 统一 API 密钥管理 | ⭐⭐⭐☆☆ 中 | 降低多 key 管理成本，OpenRouter 用户自然延伸 | [Issue #24415](https://github.com/NousResearch/hermes-agent/issues/24415) |
| **#30587** Kanban 自适应重试 + 模型升级 | 调度系统智能化 | ⭐⭐⭐☆☆ 中 | 与 #30652 模型路由有协同潜力 | [Issue #30587](https://github.com/NousResearch/hermes-agent/issues/30587) |

**路线图信号**：生产力工具的多账户/多云生态（Google + Microsoft）与跨设备同步是**明确的商业化/用户留存杠杆**；隐私协议（XMPP）则是**社区差异化**的关键。动态模型路由可能改变成本结构，值得架构层面提前预留接口。

---

## 7. 用户反馈摘要

### 真实痛点

| 场景 | 来源 Issue | 情绪 |
|:---|:---|:---|
| **"我明确告诉 bot 不要回复，它却发了诊断垃圾信息到群聊"** — WhatsApp 群组中静默处理是基本礼仪 | #28208, #18848 | 😤 挫败 |
| **"SSH 远程执行 hermes -z 什么都没输出，exit 0，调试了 3 小时才发现是 TTY 检测问题"** | #30623 | 😤 极度挫败 |
| **"onboarding 说可以用 /busy，Telegram 里却找不到"** — 文档与实现不一致 | #18362 | 😕 困惑 |
| **"state.db 三天坏三次，日志里全是 SIGTERM"** — 数据丢失恐惧 | #30636 | 😰 焦虑 |
| **"个人和工作 Google 账户只能二选一，每天都要重新 OAuth"** | #15602 | 😤 重复劳动 |

### 满意/期待点

- **"已有生产实现的 Outlook skill，愿意贡献"** — 社区贡献意愿强（#25979）
- **"Docker 镜像从 5.6GB 降到 2GB，启动 10 秒"** — 基础设施优化获得认可（#27437）
- **中文 Dashboard 翻译 PR 快速迭代** — 国际化响应积极（#30671 → #30672）

### 核心矛盾

> **"功能越丰富，生产越脆弱"** — 用户在拥抱新平台（WhatsApp/Signal/Discord）的同时，遭遇网关崩溃、数据损坏、配置不生效等基础稳定性问题，信任损耗可能抵消功能增益。

---

## 8. 待处理积压

### 需维护者优先关注

| Issue/PR | 积压时长 | 风险 | 行动建议 | 链接 |
|:---|:---|:---|:---|:---|
| **#7237** Response truncated | ~43 天 | 33 条评论后关闭，但方案未明，可能复发 | 确认关闭原因，若未解决应 reopen | [Issue #7237](https://github.com/NousResearch/hermes-agent/issues/7237) |
| **#5254** LM-Studio 工具调用重复 | ~48 天 | 第三方本地模型生态增长，兼容性问题扩大 | 与 Codex #7517 对标，制定工具调用序列化标准 | [Issue #5254](https://github.com/NousResearch/hermes-agent/issues/5254) |
| **#2988** XMPP + OMEMO | ~59 天 | 开源社区信任资产，长期被专有协议挤压 | 评估集成成本，或标记 "help wanted" | [Issue #2988](https://github.com/NousResearch/hermes-agent/issues/2988) |
| **#20660** 原生跨平台桌面控制 | ~17 天 | #30660 已补 Windows，但 PR 未合并，架构分散 | 协调 #20660 与 #30660，避免重复实现 | [PR #20660](https://github.com/NousResearch/hermes-agent/pull/20660) |
| **#29302** API Server session controls | ~3 天 | 移动/ web 客户端生态依赖此接口 | 加速 review，与 capabilities 发现机制联动 | [PR #29302](https://github.com/NousResearch/hermes-agent/pull/29302) |

### 合并瓶颈警示

- **41 条 PR 待合并** vs **9 条关闭/合并**，合并比率 **18%**，远低于健康项目的 40-50%
- **P1 Bug 无关联 PR** 的比例过高（3/3），表明严重问题的修复响应存在结构性延迟

---

*日报生成时间：2026-05-23 | 数据来源：NousResearch/hermes-agent GitHub 公开数据*

</details>

<details>
<summary><strong>PicoClaw</strong> — <a href="https://github.com/sipeed/picoclaw">sipeed/picoclaw</a></summary>

# PicoClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

PicoClaw 今日呈现**高活跃度清理态势**：24小时内关闭7个Issue和12个PR，同时新增3个活跃Issue与8个待合并PR。项目团队集中处理了积压的stale问题，特别是Matrix频道过滤、语音转录传递、消息时间戳等长期悬而未决的bug。 nightly构建持续发布，但功能层面以依赖更新和稳定性修复为主，重大新功能仍在PR队列中等待评审。整体健康度良好，清理效率显著，但待合并PR数量（8个）提示评审带宽可能存在瓶颈。

---

## 2. 版本发布

### 🔧 Nightly Build: v0.2.8-nightly.20260522.5bbebb5f
- **发布时间**：2026-05-22
- **类型**：自动化构建（可能不稳定）
- **变更范围**：自 v0.2.8 以来的 main 分支累积变更
- **Full Changelog**: https://github.com/sipeed/picoclaw/compare/v0.2.8...main

> ⚠️ **注意事项**：此为自动化构建，生产环境使用需谨慎。当前稳定版仍为 v0.2.8。

---

## 3. 项目进展

### ✅ 今日合并/关闭的关键 PR

| PR | 作者 | 核心贡献 | 关联Issue |
|:---|:---|:---|:---|
| [#2788](https://github.com/sipeed/picoclaw/pull/2788) | LiusCraft | **为 Session API 消息添加独立 `created_at` 时间戳** — 解决前端消息时间显示不准确的历史问题 | [#2787](https://github.com/sipeed/picoclaw/issues/2787) |
| [#2827](https://github.com/sipeed/picoclaw/pull/2827) | Ashid332 | **修复 Matrix `allow_from` 过滤器完全失效问题** — 根因是MXID含冒号导致canonical ID解析错误 | [#2815](https://github.com/sipeed/picoclaw/issues/2815) |
| [#2822](https://github.com/sipeed/picoclaw/pull/2822) | bogdanovich | **子代理工具反馈清理机制** — 同步子任务完成后自动清理session-scoped反馈，避免Telegram消息残留 | [#2785](https://github.com/sipeed/picoclaw/issues/2785) |
| [#2794](https://github.com/sipeed/picoclaw/pull/2794) | bogdanovich | **保留异步跟进消息的原始路由上下文** — 修复async tool回调丢失channel/chat_id元数据问题 | — |
| [#2791](https://github.com/sipeed/picoclaw/pull/2791) | bogdanovich | **Telegram论坛话题上下文保持** — 确保最终回复投递到正确话题而非默认线程 | — |
| [#2789](https://github.com/sipeed/picoclaw/pull/2789) | bogdanovich | **工具反馈编辑节流可配置化** — 新增 `animation_interval_secs` 和 `max_staleness_secs` 配置项 | — |
| [#2930](https://github.com/sipeed/picoclaw/pull/2930) | lc6464 | **安全更新：升级 golang.org/x/net 至 v0.55.0** — 修复 `govulncheck` 报告的 HTML解析漏洞 | — |
| [#2914](https://github.com/sipeed/picoclaw/pull/2914) | lxowalle | **请求级上下文策略** — 通过 `turn_profile` 控制每轮对话的历史、系统上下文、技能提示和工具包含 | — |

**整体推进评估**：今日关闭的PR以**通道稳定性（Matrix/Telegram）**和**开发者体验（时间戳、可配置性）**为核心，修复了多个影响生产使用的边缘案例。v0.2.8 的补丁级改进已就绪，但尚未发布正式补丁版本。

---

## 4. 社区热点

### 🔥 讨论最活跃的议题

| 排名 | Issue/PR | 互动量 | 核心诉求分析 |
|:---|:---|:---|:---|
| 1 | [#2625](https://github.com/sipeed/picoclaw/issues/2625) WhatsApp预编译构建支持 | 6评论, 👍1 | **ARM64边缘部署痛点**：Raspberry Pi Zero 2用户需要开箱即用的WhatsApp通道，当前需自行编译导致更新困难。诉求背后是**IoT/边缘场景对二进制分发的强烈需求** |
| 2 | [#2785](https://github.com/sipeed/picoclaw/issues/2785) 飞书工具反馈仅显示首条消息 | 3评论 | **企业IM通知体验**：separate_messages=false时通知中心信息不完整，影响办公场景可用性 |
| 3 | [#2744](https://github.com/sipeed/picoclaw/issues/2744) Android v0.2.8数据访问故障 | 3评论 | **移动端稳定性**：Termux/Android用户的tab数据完全不可访问，阻塞移动办公场景 |

**深层信号**：社区对**多平台二进制分发**（ARM64+Android）、**企业IM集成深度**（飞书/钉钉）、**移动端可用性**的诉求正在累积，可能成为v0.3.0的优先级方向。

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | Fix PR | 影响范围 |
|:---|:---|:---|:---|:---|
| 🔴 **高** | [#2744](https://github.com/sipeed/picoclaw/issues/2744) Android v0.2.8 Tab数据完全不可访问 | **已关闭** | 未明确 | Android/Termux全量用户 |
| 🟡 **中** | [#2817](https://github.com/sipeed/picoclaw/issues/2817) 语音转录成功但LLM收到`[voice]`占位符 | **已关闭(stale)** | 未明确 | Groq Whisper用户 |
| 🟡 **中** | [#2816](https://github.com/sipeed/picoclaw/issues/2816) Matrix发送者身份未注入agent上下文 | **已关闭(stale)** | 未明确 | Matrix通道用户 |
| 🟡 **中** | [#2815](https://github.com/sipeed/picoclaw/issues/2815) Matrix `allow_from`过滤器完全失效 | **已关闭** | [#2827](https://github.com/sipeed/picoclaw/pull/2827) | Matrix安全过滤场景 |
| 🟢 **低** | [#2787](https://github.com/sipeed/picoclaw/issues/2787) Session消息缺乏独立时间戳 | **已关闭** | [#2788](https://github.com/sipeed/picoclaw/pull/2788) | 前端/历史展示 |

> **稳定性评估**：今日关闭的bug多为历史积压，实际修复率约60%（3/5有明确PR）。Android数据访问问题关闭但无关联PR，需确认是否为重复issue或隐性修复。

---

## 6. 功能请求与路线图信号

| 功能请求 | 状态 | 纳入可能性评估 | 关键障碍 |
|:---|:---|:---|:---|
| [#2929](https://github.com/sipeed/picoclaw/issues/2929) **Agent间一等通信协议**（cooperative workflows） | 🆕 新开 | ⭐⭐⭐⭐⭐ **高** | 架构设计复杂，需协调`spawn`/`subagent`/`delegate`现有语义 |
| [#2625](https://github.com/sipeed/picoclaw/issues/2625) WhatsApp预编译ARM64构建 | 开放 | ⭐⭐⭐⭐☆ **中高** | CI/CD构建矩阵扩展，技术门槛低但维护成本高 |
| [#2351](https://github.com/sipeed/picoclaw/issues/2351) Skill二进制依赖预验证 | 开放(stale) | ⭐⭐⭐☆☆ **中** | 需设计运行时检测与prompt注入的联动机制 |
| [#2820](https://github.com/sipeed/picoclaw/issues/2820) 非破坏性session重置（保留Seahorse历史） | 已关闭(stale) | ⭐⭐⭐☆☆ **中** | 与现有`/clear`语义冲突，需CLI/协议层重新设计 |

**路线图信号**：Agent间协作（[#2929](https://github.com/sipeed/picoclaw/issues/2929)）是今日唯一**全新**的功能请求，且与项目已有`spawn`/`subagent`/`delegate`能力高度相关，极可能成为v0.3.0的核心叙事。相关PR [#2838](https://github.com/sipeed/picoclaw/pull/2838)（frontmatter工具策略过滤）已为agent策略控制打下基础。

---

## 7. 用户反馈摘要

### 😤 核心痛点

| 场景 | 来源 | 具体表述 |
|:---|:---|:---|
| **边缘部署更新困难** | [#2625](https://github.com/sipeed/picoclaw/issues/2625) | *"default arm64 build does not have WhatsApp support included, making it hard to rapidly update PicoClaw"* |
| **移动端完全不可用** | [#2744](https://github.com/sipeed/picoclaw/issues/2744) | Android v0.2.8 Tab数据访问彻底断裂 |
| **企业IM通知信息残缺** | [#2785](https://github.com/sipeed/picoclaw/issues/2785) | 飞书通知中心仅显示首条工具调用消息 |
| **语音工作流断裂** | [#2817](https://github.com/sipeed/picoclaw/issues/2817) | *"LLM receives `[voice]` with a stale `media://` reference"* — 转录成功但传递失败 |

### 🙂 满意点

- **多agent架构获认可**：[#2929](https://github.com/sipeed/picoclaw/issues/2929) 提出者明确肯定 *"PicoClaw now supports multiple agents with separate workspaces, identities, tools, and turns"*
- **Seahorse上下文管理**：用户依赖其历史持久化能力，但希望有更细粒度的重置控制（[#2820](https://github.com/sipeed/picoclaw/issues/2820)）

---

## 8. 待处理积压

### ⚠️ 需维护者关注的高价值PR/Issue

| 项目 | 创建时间 | 当前状态 | 风险说明 |
|:---|:---|:---|:---|
| [#2856](https://github.com/sipeed/picoclaw/pull/2856) **媒体附件与Telegram富文本投递** | 2026-05-11 | 🟡 开放, 无评论 | **11天无评审** — 核心功能PR，阻塞message工具的多媒体扩展 |
| [#2838](https://github.com/sipeed/picoclaw/pull/2838) **Frontmatter工具策略过滤** | 2026-05-09 | 🟡 开放, 无评论 | **13天无评审** — agent安全控制基础设施，与[#2929](https://github.com/sipeed/picoclaw/issues/2929)协作需求相关 |
| [#2877](https://github.com/sipeed/picoclaw/pull/2877) **Tirith预执行安全扫描** | 2026-05-15 | 🟡 开放(stale) | 安全增强PR，替代已关闭的#1932，需确认设计方向 |
| [#2662](https://github.com/sipeed/picoclaw/pull/2662) **提供商文档统一** | 2026-04-24 | 🟡 开放 | **28天无评审** — 文档债，影响新用户接入体验 |
| [#2351](https://github.com/sipeed/picoclaw/issues/2351) **Skill二进制依赖预验证** | 2026-04-05 | 🔴 开放(stale) | **47天无响应** — 导致LLM幻觉"我能截图"但实际无依赖，损害信任 |

**建议行动**：优先评审 [#2856](https://github.com/sipeed/picoclaw/pull/2856) 和 [#2838](https://github.com/sipeed/picoclaw/pull/2838)，两者构成v0.2.9功能 release 的核心；对 [#2351](https://github.com/sipeed/picoclaw/issues/2351) 需明确是接受设计还是关闭，避免无限期stale。

---

*日报生成时间：2026-05-23 | 数据来源：GitHub API / sipeed/picoclaw*

</details>

<details>
<summary><strong>NanoClaw</strong> — <a href="https://github.com/qwibitai/nanoclaw">qwibitai/nanoclaw</a></summary>

# NanoClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

NanoClaw 今日呈现**高强度开发态势**：24小时内 **28 个 PR 完成合并/关闭**，仅 3 个待合并，代码流转效率极高。核心工作围绕 **Apple Container 技能修复**（3 个关联 Issue 集中爆发）、**多通道稳定性**（WhatsApp/Signal/Telegram 均有修复）以及 **AI 运行时优化**（上下文窗口暴露、会话转储轮转）展开。社区活跃度显著，但 Apple Container 技能分支与主线的严重脱节暴露出技能系统版本治理的结构性风险，需维护者紧急介入。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 🔧 核心运行时修复（3 项）

| PR | 作者 | 关键进展 |
|:---|:---|:---|
| [#2586](https://github.com/nanocoai/nanoclaw/pull/2586) | IamAdamJowett | **会话转储轮转机制**：解决长期运行 hub 会话的 `jsonl` 文件无限膨胀问题，防止 base64 图片块阻塞 agent `Read` 操作，直接影响多 agent 协作稳定性 |
| [#2573](https://github.com/nanocoai/nanoclaw/pull/2573) | matt1995ai | **上下文窗口可视化**：agent 首次获得自身 context-window 使用率的内省能力（`X / Y (Z%)`），可自主规划工作节奏，降低 token 耗尽导致的意外中断 |
| [#2567](https://github.com/nanocoai/nanoclaw/pull/2567) | floflo11 | **本地记忆修复**：`CLAUDE.local.md` 正确注入 per-group 记忆，修复"注释声称自动加载但实际未生效"的文档与实现不一致问题 |

### 📱 通道生态加固（5 项）

| PR | 作者 | 关键进展 |
|:---|:---|:---|
| [#2552](https://github.com/nanocoai/nanoclaw/pull/2552) | IamAdamJowett | WhatsApp `@<phone>` 提及渲染 + 关闭竞态条件导致凭证擦除的双重修复 |
| [#2553](https://github.com/nanocoai/nanoclaw/pull/2553) | IamAdamJowett | 新增 `whatsapp-formatting` 容器技能，强制 agent 使用协议正确的 `@<phone-digits>` 语法 |
| [#2584](https://github.com/nanocoai/nanoclaw/pull/2584) | snymanpaul | Signal 认证适配 signal-cli 0.13+ 的 JSON 字段变更（`account` → `number`） |
| [#2579](https://github.com/nanocoai/nanoclaw/pull/2579) | cfis | WhatsApp 401 强制登出时立即清除凭证，避免重启死循环 |
| [#2578](https://github.com/nanocoai/nanoclaw/pull/2578) | sumsumai | Telegram 认领链接功能 |

### 🛠️ 开发者体验与基础设施（4 项）

| PR | 作者 | 关键进展 |
|:---|:---|:---|
| [#2580](https://github.com/nanocoai/nanoclaw/pull/2580) | chiptoe-svg | **完整 Codex-only 安装支持**：Codex 作为 AI 编码 CLI + 唯一 agent 提供商 + OneCLI 凭证管理，技能目录与 persona 与 Claude Code 原生体验对齐 |
| [#2571](https://github.com/nanocoai/nanoclaw/pull/2571) | ira-at-work | 新增 `/add-rtk` 技能，集成 [rtk](https://github.com/rtk-ai/rtk) CLI 代理，宣称 60-90% token 节省 |
| [#2572](https://github.com/nanocoai/nanoclaw/pull/2572) | bromleymindfulness | Rootless Podman 双 bug 修复（`--user` UID 映射 + 挂载权限） |
| [#2566](https://github.com/nanocoai/nanoclaw/pull/2566) | Hinotoi-agent | 安全加固：渠道注册审批流程的作用域限制，防止权限提升 |

### 🔒 安全与权限（2 项）

| PR | 作者 | 关键进展 |
|:---|:---|:---|
| [#2566](https://github.com/nanocoai/nanoclaw/pull/2566) | Hinotoi-agent | 渠道审批目标作用域限定，scoped admin 只能连接其授权管理的 agent group |
| [#2563](https://github.com/nanocoai/nanoclaw/pull/2563) | kky | `--assistant-name` 限定至注册的 group 范围 |

**整体评估**：项目今日在**运行时可靠性**（会话管理、内存注入）、**多通道成熟度**（WhatsApp/Signal/Telegram 并行修复）、**基础设施多样性**（Codex/Podman/Apple Container）三个维度均有实质推进，代码合并速度（28/31 = 90% 当日关闭率）反映维护团队响应积极。

---

## 4. 社区热点

> **注**：数据中所有 PR 评论数均显示 `undefined`，Issues 评论数均为 0，无法按传统"评论最多"排序。以下基于 Issue/PR 关联密度和主题紧迫性分析。

### 🔥 最热区域：Apple Container 技能集中崩溃（3 个关联 Issue，0 评论但极高紧迫性）

| 条目 | 链接 | 核心诉求分析 |
|:---|:---|:---|
| **#2588** - `skill/apple-container` 分支与主线严重不同步 | [Issue #2588](https://github.com/nanocoai/nanoclaw/issues/2588) | **技能系统版本治理缺陷**：分支引用已删除 API、不存在的模块、假设已废弃的 Node+tsc 运行时。用户执行文档记载的 `/convert-to-apple-container` 技能将**立即失败**。诉求：建立技能分支的持续集成/兼容性检查机制 |
| **#2589** - `host.docker.internal` 在 Apple Container microVM 内无法解析 | [Issue #2589](https://github.com/nanocoai/nanoclaw/issues/2589) | **Apple Silicon 容器网络适配缺失**：Apple Container 不支持 Docker 的 host 解析惯例，也不支持 `--add-host` 注入。诉求：为 Apple Container 提供 OneCLI 代理 URL 的替代解析策略（如硬编码网关 IP 或 socket 代理） |
| **#2587** - Dockerfile 残留 `npm run build` 与 bun 迁移冲突 | [Issue #2587](https://github.com/nanocoai/nanoclaw/issues/2587) | **构建系统迁移遗漏**：`skill/apple-container` 分支的 Dockerfile 仍使用 npm，而主线的 `agent-runner` 已迁移至 bun（`"start": "bun src/index.ts"`）。诉求：统一技能分支的构建脚本与主线运行时对齐 |

**背后诉求**：Apple Container 是 NanoClaw 面向 macOS 用户的战略部署路径，但技能系统的**分支维护模型**存在结构性漏洞——技能分支缺乏自动同步主线的机制，导致文档与实现脱节、用户首次体验即失败。

### 📊 次热区域：Node 生态调试摩擦

| 条目 | 链接 | 核心诉求分析 |
|:---|:---|:---|
| **#2590** - "I just hate Node apps" — Ubuntu 调试依赖地狱 | [Issue #2590](https://github.com/nanocoai/nanoclaw/issues/2590) | **非容器开发路径支持不足**：用户被迫在 Node 22 ↔ SQLite wrapper ↔ gyp 编译错误间周旋，情绪表达强烈（"hate"）。诉求：提供**官方非容器调试指南**或简化原生依赖（如预编译 SQLite 二进制） |

---

## 5. Bug 与稳定性

| 严重程度 | Issue/PR | 描述 | 状态 |
|:---|:---|:---|:---|
| 🔴 **Critical** | [#2588](https://github.com/nanocoai/nanoclaw/issues/2588) | `skill/apple-container` 分支完全不可用，文档技能路径 100% 失败 | ❌ **无 fix PR**，需维护者紧急重建分支 |
| 🔴 **Critical** | [#2587](https://github.com/nanocoai/nanoclaw/issues/2587) | 同上分支的 Dockerfile 构建失败（npm vs bun） | ❌ **无 fix PR** |
| 🟡 **High** | [#2589](https://github.com/nanocoai/nanoclaw/issues/2589) | Apple Container 网络解析失败，阻断 OneCLI 代理通信 | ❌ **无 fix PR** |
| 🟡 **High** | [#2555](https://github.com/nanocoai/nanoclaw/issues/2555) → [#2556](https://github.com/nanocoai/nanoclaw/pull/2556) | `<messages>` 批处理信封导致 Claude Agent SDK 返回合成 stub 而非调用 API | ✅ **已修复**（PR #2556 合并） |
| 🟡 **High** | [#2581](https://github.com/nanocoai/nanoclaw/issues/2581) → [#2584](https://github.com/nanocoai/nanoclaw/pull/2584) | signal-cli 0.13+ 字段名变更导致认证向导无限循环 | ✅ **已修复**（PR #2584 合并） |
| 🟢 **Medium** | [#2590](https://github.com/nanocoai/nanoclaw/issues/2590) | Ubuntu 原生调试依赖地狱（Node 22 + SQLite + gyp） | ❌ **无 fix PR**，需文档或构建优化 |
| 🟢 **Medium** | PR [#2579](https://github.com/nanocoai/nanoclaw/pull/2579) | WhatsApp 401 后凭证残留导致重启死循环 | ✅ **已修复** |
| 🟢 **Medium** | PR [#2572](https://github.com/nanocoai/nanoclaw/pull/2572) | Rootless Podman 双 bug 阻断容器运行 | ✅ **已修复** |

**稳定性评估**：已关闭的 bug 修复响应极快（当日 PR 当日合并），但 **Apple Container 技能的三连崩**构成显著的产品可靠性风险，且尚无修复动作。

---

## 6. 功能请求与路线图信号

| 来源 | 功能方向 | 纳入可能性评估 |
|:---|:---|:---|
| PR [#2580](https://github.com/nanocoai/nanoclaw/pull/2580) | **Codex 作为一等公民**：完整替代 Claude Code 的安装路径 | ⭐⭐⭐⭐⭐ **已合并**，成为官方支持的第二 AI 提供商 |
| PR [#2571](https://github.com/nanocoai/nanoclaw/pull/2571) | **rtk 集成**：开发命令的 token 压缩代理 | ⭐⭐⭐⭐⭐ **已合并**，成本优化成为显性卖点 |
| PR [#2573](https://github.com/nanocoai/nanoclaw/pull/2573) | **Agent 上下文自省**：context-window 使用率暴露 | ⭐⭐⭐⭐⭐ **已合并**，增强 agent 自主性 |
| PR [#2578](https://github.com/nanocoai/nanoclaw/pull/2578) | Telegram 认领链接 | ⭐⭐⭐⭐☆ **已合并**，通道功能补全 |
| PR [#2593](https://github.com/nanocoai/nanoclaw/pull/2593) | 默认 agent 共享会话模式 | ⭐⭐⭐⭐☆ **已合并**，多 agent 协作体验优化 |
| Issue [#2590](https://github.com/nanocoai/nanoclaw/issues/2590) | 非容器调试支持 / 简化原生依赖 | ⭐⭐⭐☆☆ 用户痛点明确，需维护者决策是否支持非容器路径 |
| Issue [#2589](https://github.com/nanocoai/nanoclaw/issues/2589) | Apple Container 网络适配方案 | ⭐⭐⭐⭐⭐ **阻断性需求**，预计紧急修复 |

**路线图信号**：项目正从"Claude Code 专属"向**多 AI 提供商中立平台**演进（Codex 完整支持），同时强化**成本控制**（rtk）和**多通道覆盖**（WhatsApp/Signal/Telegram 并行）。Apple Container 的修复将是近期关键里程碑。

---

## 7. 用户反馈摘要

### 😤 痛点（直接引用）

> *"I just hate Node apps. Trying to debug the app in Ubuntu, I keep getting missing dependencies hell."*
> — [whiletrue111](https://github.com/nanocoai/nanoclaw/issues/2590)，Issue #2590

**场景**：非 Docker 环境下的开发调试  
**根因**：Node 版本切换（18 → 22）、SQLite wrapper 的 gyp 编译依赖、缺乏官方原生调试文档  
**情绪强度**：高（"hate" 直接表达挫败）

### 🔧 隐性痛点（从 Issue 描述推断）

| 来源 | 痛点 | 场景 |
|:---|:---|:---|
| snymanpaul 三连 Issue (#2587-#2589) | Apple Container 技能"文档可用，实际不可用" | macOS 用户按官方指引部署，遭遇构建失败、网络失败、API 不存在三重打击 |
| crookies PR [#2521](https://github.com/nanocoai/nanoclaw/pull/2521) | 多通道监控需要解析转储文件，但 XML 缺少 `from-channel`/`from-type` 元数据 | 生产环境运维（Telegram + Discord 双通道） |

### ✅ 满意度区域

- **PR 合并速度**：28/31 当日关闭，贡献者体验流畅
- **Codex 支持**：为非 Anthropic 生态用户提供完整替代路径
- **WhatsApp 修复**：提及渲染 + 凭证安全双管齐下，通道可靠性提升

---

## 8. 待处理积压

| 条目 | 创建时间 | 最后更新 | 风险说明 |
|:---|:---|:---|:---|
| [PR #2521](https://github.com/nanocoai/nanoclaw/pull/2521) - XML 消息属性扩展 | 2026-05-17 | 2026-05-22 | **5 天未合并**，多通道运维刚需，评论 `undefined` 可能掩盖了审查讨论 |
| [Issue #2588](https://github.com/nanocoai/nanoclaw/issues/2588) | 2026-05-22 | 2026-05-22 | **Apple Container 完全不可用**，战略功能阻断，需维护者当日响应 |
| [Issue #2589](https://github.com/nanocoai/nanoclaw/issues/2589) | 2026-05-22 | 2026-05-22 | 同上，网络层修复依赖 #2588 的分支重建 |
| [Issue #2587](https://github.com/nanocoai/nanoclaw/issues/2587) | 2026-05-22 | 2026-05-22 | 同上，构建层修复依赖分支重建 |
| [Issue #2590](https://github.com/nanocoai/nanoclaw/issues/2590) | 2026-05-22 | 2026-05-22 | 开发者体验痛点，非阻断但影响社区增长 |

**维护者行动建议**：
1. **紧急**：重建 `skill/apple-container` 分支，建立与主线的自动同步机制（如 weekly rebase + CI）
2. **高优**：审查 PR #2521，补全多通道元数据支持
3. **中优**：回应 Issue #2590，明确是否支持非容器调试路径，或提供预编译依赖方案

---

*日报生成时间：2026-05-23 | 数据来源：NanoClaw GitHub (github.com/qwibitai/nanoclaw)*

</details>

<details>
<summary><strong>NullClaw</strong> — <a href="https://github.com/nullclaw/nullclaw">nullclaw/nullclaw</a></summary>

# NullClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

NullClaw 今日活跃度**偏低**，过去24小时无 Issues 活动，4条 PR 均处于待合并状态，无新版本发布。项目呈现**"维护模式"特征**——社区讨论沉寂，但技术债务清理与功能扩展仍在持续推进。值得关注的是，两条由核心贡献者 vernonstinebaker 提交的修复 PR 均于昨日更新，显示底层稳定性优化仍在进行；同时 NEAR AI Cloud 新提供商的接入和 Cron 子代理引擎两大功能线并行开发，项目技术栈正向外扩展。

---

## 2. 版本发布

**无**

---

## 3. 项目进展

**今日无合并/关闭的 PR**，全部 4 条 PR 处于 OPEN 状态等待审查。以下是各 PR 当前推进状态：

| PR | 方向 | 技术价值 | 阻塞风险 |
|:---|:---|:---|:---|
| [#783](https://github.com/nullclaw/nullclaw/pull/783) Cron 子代理引擎 | 重大功能 | 引入完整 DB-backed 任务调度系统，含历史追踪、队列工作器、原子操作、多作业类型支持 | **高**——创建已逾 6 周（2026-04-07），体积大、涉及安全加固，审查周期长 |
| [#922](https://github.com/nullclaw/nullclaw/pull/922) NEAR AI Cloud 提供商 | 生态扩展 | 新增 OpenAI-compatible 提供商，含模型目录解析、完整 onboarding 链路 | 中——刚创建 2 天，需验证 API 兼容性 |
| [#891](https://github.com/nullclaw/nullclaw/pull/891) Curl 传输错误保留 | 稳定性修复 | 健康探针不再吞掉 DNS/连接/TLS 等底层错误，运维可观测性提升 | 低——范围聚焦，作者 vernonstinebaker 有维护者权限 |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) POSIX nanosleep 修复 | 性能/正确性修复 | 线程睡眠从协程 yield 改为真实 OS 挂起，避免空转 CPU | 低——同理，技术债清理 |

**整体评估**：项目处于**"蓄力期"**——功能扩展（Cron、NEAR AI）与底层修复并行，但缺乏审查动力导致代码无法落地。6 周未合并的 #783 已成为事实上的技术瓶颈。

---

## 4. 社区热点

**今日无活跃讨论**。全部 4 条 PR 评论数均为 `undefined`（数据异常或确实零评论），👍 反应数均为 0。

**潜在热点分析**（基于 PR 内容推测社区诉求方向）：

| PR | 背后诉求 | 目标用户群 |
|:---|:---|:---|
| [#783](https://github.com/nullclaw/nullclaw/pull/783) | **定时任务自治**——用户需要 AI Agent 脱离人工触发、按调度自主执行，且需审计追踪 | 企业级部署、自动化运维场景 |
| [#922](https://github.com/nullclaw/nullclaw/pull/922) | **去中心化 AI 基础设施**——NEAR 生态用户希望直接调用链上/链下 AI 算力，降低 OpenAI 依赖 | Web3/区块链开发者、成本敏感用户 |
| [#891](https://github.com/nullclaw/nullclaw/pull/891) | **可观测性刚需**——生产环境故障排查时，"Unknown Error" 不可接受 | SRE、平台工程师 |
| [#878](https://github.com/nullclaw/nullclaw/pull/878) | **资源效率**——高并发场景下协程 yield 导致 CPU 空转，影响托管成本 | 云原生部署用户 |

> **异常信号**：零评论、零反应反映社区参与度极低，或项目主要依赖核心团队内部审查，未形成外部贡献者生态。

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | PR | 状态 | 影响范围 |
|:---|:---|:---|:---|:---|
| 🔶 **中高** | POSIX 系统 `thread.sleep` 实际未挂起 OS 线程，导致 CPU 空转 | [#878](https://github.com/nullclaw/nullclaw/pull/878) | **待合并** | 所有 Linux/macOS 生产部署，高并发场景资源成本上升 |
| 🔶 **中高** | 健康探针吞掉 Curl 传输层错误（DNS/连接/TLS/超时等），返回模糊错误 | [#891](https://github.com/nullclaw/nullclaw/pull/891) | **待合并** | 所有使用 OpenAI-compatible 提供商路径的部署，故障排查困难 |

**无今日新报 Bug**，上述两项均为历史技术债务的主动修复。

---

## 6. 功能请求与路线图信号

| 功能方向 | 载体 | 成熟度 | 纳入下一版本概率 | 判断依据 |
|:---|:---|:---|:---|:---|
| **Cron 调度子代理** | [#783](https://github.com/nullclaw/nullclaw/pull/783) | 代码完整，文档/测试待审 | **高（若审查通过）** | 功能闭环度高（DB + Worker + CLI + 安全），6 周投入表明战略优先级 |
| **NEAR AI Cloud 提供商** | [#922](https://github.com/nullclaw/nullclaw/pull/922) | 刚提交，需兼容性验证 | **中** | 提供商接入模式已成熟（OpenAI-compatible），但需维护者评估生态价值 |
| **更多去中心化 AI 提供商** | 无直接 PR | 需求隐含于 #922 | **低-中** | 单一 PR 不足以证明路线图转向，需观察是否形成提供商接入浪潮 |

**路线图信号**：NullClaw 正从"单一云 AI 编排"向**"多基础设施自治代理平台"**演进——Cron 解决"何时执行"，NEAR AI 解决"在哪执行"。

---

## 7. 用户反馈摘要

**今日无 Issues 评论可提炼**。

从 PR 内容反向推断的**隐含用户画像与痛点**：

| 用户类型 | 痛点 | 对应 PR |
|:---|:---|:---|
| **平台运维者** | "Agent 定时任务跑没跑？跑成什么样了？出错了谁通知？" | #783（历史表 + 告警路由） |
| **Web3 开发者** | "我想用 NEAR 的 AI 算力，但 NullClaw 只认 OpenAI" | #922 |
| **生产环境 SRE** | "节点健康检查报红，日志里只有 `ProviderError: unknown`，根本没法定位" | #891 |
| **成本优化工程师** | "同样并发数，NullClaw 部署 CPU 占用比竞品高 30%" | #878 |

> **满意度盲区**：零 Issues 可能意味着用户基数小、或问题通过其他渠道（Discord/Slack）反馈，GitHub 未成为主要支持入口。

---

## 8. 待处理积压

| 风险等级 | 项目 | 创建时间 | 最后更新 | 问题 | 行动建议 |
|:---|:---|:---|:---|:---|:---|
| 🔴 **紧急** | [#783](https://github.com/nullclaw/nullclaw/pull/783) Cron 子代理 | 2026-04-07 | 2026-05-22 | **阻塞 46 天**，功能庞大易冲突，作者 yanggf8 持续更新显示维护意愿 | 维护者需启动分段审查（security hardening → core engine → CLI），或明确拒绝理由 |
| 🟡 **关注** | 整体 PR 审查队列 | — | — | 4 条 PR 全部 pending，无合并节奏 | 建议建立 SLA：修复类 PR 3 天内响应，功能类 PR 2 周内初评 |

**健康度指标警示**：
- **合并速率**：过去 24h 为 0，过去 46 天 #783 为 0
- **Issue 响应率**：无数据（零 Issues）
- **外部贡献者参与度**：4 条 PR 中 2 条来自 vernonstinebaker（疑似核心维护者），1 条 yanggf8，1 条 PierreLeGuen（首次贡献？），**外部贡献占比 25%**

---

*日报生成时间：2026-05-23 | 数据来源：GitHub API 快照 | 下次建议关注：#783 审查启动信号、#922 兼容性测试结果*

</details>

<details>
<summary><strong>IronClaw</strong> — <a href="https://github.com/nearai/ironclaw">nearai/ironclaw</a></summary>

# IronClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

IronClaw 昨日（5月22日-23日）呈现**极高活跃度**，50个PR更新（36个待合并）、23个Issue更新（19个新开/活跃），无新版本发布。核心工作集中在 **Reborn 架构的四大主线并行推进**：身份认证/授权体系（OAuth、凭证生命周期）、Hooks 框架优化、Google 扩展生态（Gmail/Calendar）、以及 WebUI Beta 基础设施。项目处于**密集功能交付期**，多个 XL 级大型 PR 同时推进，显示团队对 Reborn 里程碑的强承诺。

---

## 2. 版本发布

**无新版本发布**（0 releases）

---

## 3. 项目进展

### 已合并/关闭的关键 PR

| PR | 作者 | 核心贡献 | 项目推进意义 |
|:---|:---|:---|:---|
| [#3878](https://github.com/nearai/ironclaw/pull/3878) | hanakannzashi | `RebornProductAuthServices` 统一合成接缝：整合产品认证流、安全手动令牌交互、凭证设置/账户、提供商交换及清理 | 🔐 **认证架构里程碑**：Reborn 产品认证首次拥有统一的合成入口，本地开发自动获得内存认证栈，生产环境可注入持久化后端 |
| [#3863](https://github.com/nearai/ironclaw/pull/3863) | serrrfirat | Reborn 技能资产访问与执行适配器最终章：作用域技能包资产读取器 + 第一方技能执行适配器 | 🧩 **技能栈闭环**：完成 Reborn 技能系统的资产渐进披露和执行层，为第三方技能生态奠定基础 |
| [#3837](https://github.com/nearai/ironclaw/pull/3837) | henrypark133 | Google Suite 扩展设计规范：Google Calendar (9 capabilities) + Gmail (6 capabilities) | 📋 **生态蓝图发布**：确立 `ironclaw_oauth` + `ironclaw_native_extensions` 双 crate 架构，指导后续 6 个 Phase 实现 |

### 已关闭的关键 Issue

| Issue | 说明 |
|:---|:---|
| [#3803](https://github.com/nearai/ironclaw/issues/3803) | Reborn Lane 3 完成：密钥/出口基质通过生产工具合成完成布线 |
| [#3611](https://github.com/nearai/ironclaw/issues/3611) | WebChat v2 原生路由最小实现达成 |
| [#3626](https://github.com/nearai/ironclaw/issues/3626) | WebUI 调用方与线程作用域绑定至 canonical TurnScope |
| [#3625](https://github.com/nearai/ironclaw/issues/3625) | WebUI 幂等性与已接受消息账本完成 |

**整体进展评估**：Reborn 的 M1（WebUI 产品表面）和 M2（入站工作流）模块接近 Beta 就绪；M4（主机内核）的密钥/出口/认证基础设施完成核心合成；Google 扩展生态进入密集实现期（Phase 2-6 同步推进）。

---

## 4. 社区热点

### 讨论最活跃的 Issues（按评论数排序）

| 排名 | Issue | 评论 | 核心诉求分析 |
|:---|:---|:---|:---|
| 1 | [#3702](https://github.com/nearai/ironclaw/issues/3702) Reborn 二进制 E2E 测试框架重构计划 | 4 | **质量基础设施焦虑**：作者 henrypark133 系统审计 88 个 `tests/*.rs` 文件后，发现 Rust 集成测试与 Reborn 主代理循环存在 parity gap，要求建立不依赖本地规划文档的独立 GitHub 可追溯测试策略。反映社区对 Reborn 快速迭代下测试覆盖率的担忧 |
| 2 | [#3803](https://github.com/nearai/ironclaw/issues/3803) [已关闭] Lane 3 密钥/出口合成 | 2 | **生产就绪压力**：关闭前讨论聚焦于 PR 合并后的"收尾验证"——如何将现有密钥存储、授权调度、生产构建器 PR 合并后完成实际布线验证 |
| 3 | [#3798](https://github.com/nearai/ironclaw/issues/3798) Reborn 代理循环的子代理生成设计 | 2 | **架构设计共识**：提出 `builtin.spawn_subagent` 的阻塞/非阻塞/后台三模式，需在 `ironclaw_turns`、`ironclaw_loop_support` 等多 crate 间协调状态机。显示子代理作为核心抽象的设计成熟度需求 |
| 4 | [#3094](https://github.com/nearai/ironclaw/issues/3094) 添加审批/授权交互服务 [P0] | 2 | **UX 安全边界**：要求将阻塞运行状态转换为适配器/UI 安全的交互流，避免成为"第二个 auth 系统"。P0 标签显示这是阻塞 Beta 的关键路径 |

### 热点 PR 集群：Hooks 框架优化（#3573 后续）

| PR | 说明 | 社区信号 |
|:---|:---|:---|
| [#3914](https://github.com/nearai/ironclaw/pull/3914) | 批量补充 #3573 评审中 5 个仅测试的延迟项 | 代码已正确，仅需测试固化契约——显示代码质量文化 |
| [#3913](https://github.com/nearai/ironclaw/pull/3913) | 延迟能力输入解析至谓词实际需要时（HIGH 性能优化） | **性能敏感场景**：文件 blob 等昂贵输入的惰性求值，避免"安装单个 hook 导致致命开销" |
| [#3912](https://github.com/nearai/ironclaw/pull/3912) | 强制身份 newtype 在构造时验证（MEDIUM 安全加固） | 消除 `pub struct Foo(pub String)` 的直接字段可访问性，防止手工构造的非法输入 |
| [#3911](https://github.com/nearai/ironclaw/pull/3911) | 恢复 hook 激活时的批量能力调度（HIGH 性能优化） | **关键性能回归修复**：原实现将 `invoke_capability_batch` 降级为 N 次顺序调用，"安装单个 hook 使批量调用性能不可接受" |

**诉求分析**：Hooks 框架作为 Reborn 的信任原语和扩展机制，社区对其**性能开销极度敏感**（两个 HIGH 优先级优化），同时强调**安全不变量必须通过类型系统强制**而非约定。

---

## 5. Bug 与稳定性

| 严重程度 | 问题 | 状态 | 说明 |
|:---|:---|:---|:---|
| 🔴 **高** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E 失败 | **开放，无 fix PR** | 5月10日创建，5月22日仍更新失败。`Full E2E / E2E (v2-engine)` 任务失败，commit `030cfeb`。这是**持续 12 天的回归**，阻塞 v2 引擎的发布信心 |
| 🟡 **中** | [#3875](https://github.com/nearai/ironclaw/issues/3875) 阻塞生成子代理：父代理在子完成后无法恢复 | **开放，关联 draft PR #3872** | E2E 测试暴露的真实集成缺口：子代理在 `reborn-planned-state` 下运行完成后，父代理的阻塞调用未正确恢复。这是 **#3798 Phase 4 的阻塞缺陷** |
| 🟡 **中** | [#3871](https://github.com/nearai/ironclaw/issues/3871) `executor.rs` 分解追踪 | **开放，无 PR** | 架构债：`executor.rs` 已超大型文件指南，#3868 的新增子代理处理使其更臃肿。标记为"不阻塞 Phase 1 合同"，但技术债务累积 |

**稳定性评估**：Nightly E2E 持续失败是**最大红灯**，需立即优先级处理；子代理阻塞恢复问题是 Reborn 核心抽象的可靠性缺陷，影响多代理协作场景。

---

## 6. 功能请求与路线图信号

| 功能需求 | 来源 | 实现状态 | 纳入下一版本概率 |
|:---|:---|:---|:---|
| **Trigger Loop：定时（cron）触发 Reborn 代理工作流** | [#3873](https://github.com/nearai/ironclaw/issues/3873) henrypark133 | 仅设计提案 | ⭐⭐⭐⭐☆ 高：架构清晰（合成入站消息 → 标准 TurnScope），V1 限定 cron 降低范围风险 |
| **安全用户作用域工具安装** | [#3905](https://github.com/nearai/ironclaw/issues/3905) serrrfirat | 需求分析阶段 | ⭐⭐⭐⭐⭐ 极高：直接关联 Reborn 已有 `/system/skills`、`/tenant-shared/skills`、`/skills` 三层模型，是生态扩展的必要基础 |
| **GitHub WASM 读/写能力路径** | [#3806](https://github.com/nearai/ironclaw/issues/3806) | PR [#3910](https://github.com/nearai/ironclaw/pull/3910) 测试路由已开，PR [#3909](https://github.com/nearai/ironclaw/pull/3909) 只读包已开 | ⭐⭐⭐⭐⭐ 极高：Lane 6 明确依赖项已就绪，PR 并行推进 |
| **Notion MCP 能力路径** | [#3805](https://github.com/nearai/ironclaw/issues/3805) | 等待 Lane 3/5 前置 | ⭐⭐⭐⭐☆ 高：Lane 5 明确排在 secrets/auth 合成之后 |
| **Google 扩展生态（Calendar + Gmail）** | 设计 #3837，PR #3894-#3898 | Phase 2-6 同步 PR 开放 | ⭐⭐⭐⭐⭐ 极高：6 个 Phase PR 同日开放，显示集中冲刺 |
| **ironclaw-bridge：本地文件/MCP 桥接守护进程** | [#2117](https://github.com/nearai/ironclaw/issues/2117) henrypark133 | 长期开放（4月7日） | ⭐⭐⭐☆☆ 中：云托管部署的痛点真实，但依赖隧道系统重构，风险标记 medium |

---

## 7. 用户反馈摘要

> 注：以下从 Issue/PR 描述和评论中提炼，反映贡献者视角的"用户"（开发者/集成者）痛点

| 维度 | 反馈 | 来源 |
|:---|:---|:---|
| **😫 痛点** | "安装单个 hook 使批量调用性能不可接受" —— Hooks 框架的生产性能焦虑 | #3911, #3913 |
| **😫 痛点** | "当 IronClaw 托管在云端时，用户无法访问笔记本电脑上的本地文件" —— 云-本地数据鸿沟 | #2117 |
| **😫 痛点** | "令牌值不得通过聊天转录、模型可见消息、产品投影、日志或工具输出传递" —— 安全传输的零信任要求 | #3882 |
| **🎯 场景** | "每天早上8点，总结我的未读邮件" —— 定时自动化代理工作流 | #3873 |
| **✅ 认可** | "代码已正确；延迟仅关于用测试覆盖固化文档化契约" —— 测试优先文化 | #3914 |
| **⚠️ 担忧** | "不要创建第二个 auth 系统或假装拥有非 turn 延续" —— 架构边界清晰性要求 | #3888, #3889 |

---

## 8. 待处理积压

| 风险等级 | 项目 | 创建日期 | 最后更新 | 阻塞原因 | 建议行动 |
|:---|:---|:---|:---|:---|:---|
| 🔴 **紧急** | [#3447](https://github.com/nearai/ironclaw/issues/3447) Nightly E2E 失败 | 2026-05-10 | 2026-05-22 | 持续 12 天，v2-engine 任务失败 | **立即分配专人**：这是发布信心的基础设施红线 |
| 🟡 **高** | [#3094](https://github.com/nearai/ironclaw/issues/3094) 审批/授权交互服务 [P0] | 2026-04-29 | 2026-05-22 | 父 issue #2987 庞大，auth 侧已在 #3865/#3878/#3879 清理，但审批侧仍待 #3888/#3889 | 确认 #3888/#3889 合并后是否可关闭，或需进一步拆分 |
| 🟡 **高** | [#3280](https://github.com/nearai/ironclaw/issues/3280) ProductWorkflow 和 InboundTurnService 外观 [P0] | 2026-05-06 | 2026-05-22 | 依赖 11 个相关 issue，协调复杂 | 检查 #3888 的 `ProductAuthTurnGateResumeDispatcher` 是否覆盖部分范围 |
| 🟡 **高** | [#3702](https://github.com/nearai/ironclaw/issues/3702) 二进制 E2E 测试框架 | 2026-05-16 | 2026-05-22 | 需要 88 个测试文件的系统分类和 29 个核心文件的深度审计 | 考虑分配独立"测试基础设施"冲刺，避免与功能开发资源冲突 |
| 🟢 **中** | [#2117](https://github.com/nearai/ironclaw/issues/2117) ironclaw-bridge | 2026-04-07 | 2026-05-22 | 范围大（size: L）、风险 medium、隧道系统重构依赖 | 评估是否与 Docker 沙箱命令传输 (#3900) 共享进程执行基础设施 |

---

## 附录：快速链接

- **项目主页**: https://github.com/nearai/ironclaw
- **今日活跃 Issues 列表**: https://github.com/nearai/ironclaw/issues?q=is%3Aissue+updated%3A2026-05-22
- **今日活跃 PR 列表**: https://github.com/nearai/ironclaw/pulls?q=is%3Apr+updated%3A2026-05-22

---

*日报生成时间：2026-05-23 | 数据来源：GitHub API 概览与公开 Issue/PR 元数据*

</details>

<details>
<summary><strong>LobsterAI</strong> — <a href="https://github.com/netease-youdao/LobsterAI">netease-youdao/LobsterAI</a></summary>

# LobsterAI 项目动态日报 | 2026-05-23

> **项目地址**: [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)

---

## 1. 今日速览

LobsterAI 今日呈现**高强度交付状态**，过去24小时内完成 **12 个 PR 的合并/关闭**（含 1 个版本发布），仅 **1 个新 Issue** 开启，社区活跃度集中于工程执行层面而非讨论层面。核心团队（`btc69m979y-dotcom`、`fisherdaddy`）主导了 **Subagent 会话系统的全面重构与稳定性修复**，从 UI 渲染、数据持久化到侧边栏交互完成闭环。同时积压的 **5 个依赖升级 PR** 和 **3 个 stale 社区 PR** 仍未获 maintainer 响应，技术债务与社区贡献吸纳存在隐忧。

---

## 2. 版本发布

### [LobsterAI 2026.5.22](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.5.22)

| 属性 | 详情 |
|:---|:---|
| **发布日期** | 2026-05-22 |
| **发布者** | `fisherdaddy` |
| **关联 PR** | [#2038](https://github.com/netease-youdao/LobsterAI/pull/2038) |

### 核心变更

| 特性 | 说明 | 作者 |
|:---|:---|:---|
| **Subagent 会话侧边栏与详情视图** | 新增独立的子代理会话侧边栏，支持详情页展示，复用主对话渲染管线 | [@btc69m979y-dotcom](https://github.com/btc69m979y-dotcom) |
| **模型自定义参数 + Thinking 块展示** | 支持模型级自定义参数配置，新增推理过程（thinking block）的可视化展示 | [@btc69m979y-dotcom](https://github.com/btc69m979y-dotcom) |

### 迁移与兼容性评估

- **无明确破坏性变更**：本次发布以功能新增和体验优化为主
- **数据层注意**：Subagent 消息已迁移至独立 SQLite 表 `subagent_messages`（见 [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034)），首次访问旧会话将触发懒加载回填
- **依赖状态**：Electron 42.x、React 19.x、Vite 8.x 的升级 PR 仍待合并（[#1277](https://github.com/netease-youdao/LobsterAI/pull/1277)、[#1764](https://github.com/netease-youdao/LobsterAI/pull/1764)、[#1766](https://github.com/netease-youdao/LobsterAI/pull/1766)），当前版本可能基于较旧依赖基线

---

## 3. 项目进展

### 已合并/关闭的关键 PR（按技术领域分组）

#### 🔷 Subagent 系统重构（6 PRs）—— 今日最大工程主题

| PR | 状态 | 核心贡献 | 技术深度 |
|:---|:---|:---|:---|
| [#2034](https://github.com/netease-youdao/LobsterAI/pull/2034) | **CLOSED** | Subagent 会话消息持久化至本地 SQLite，支持懒加载回填 | ⭐⭐⭐ 数据层架构 |
| [#2030](https://github.com/netease-youdao/LobsterAI/pull/2030) | **CLOSED** | 提取可复用的 `ConversationTurnsView` 组件，统一主会话与子代理渲染管线 | ⭐⭐⭐ 前端架构 |
| [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | **CLOSED** | 修复子代理同步缺失工具结果、侧边栏高亮状态、空态与错误处理 | ⭐⭐ 稳定性 |
| [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | **CLOSED** | 简化侧边栏行展示、修复重复覆盖问题（`toolCallId` 替代 `agentId`）、补全工具结果 | ⭐⭐ 数据一致性 |
| [#2027](https://github.com/netease-youdao/LobsterAI/pull/2027) | **CLOSED** | 侧边栏折叠态切换、可拖拽标题栏、Mac 窗口控件防重叠 | ⭐⭐ 交互细节 |
| [#2038](https://github.com/netease-youdao/LobsterAI/pull/2038) | **CLOSED** | **版本发布汇总** — 上述特性的集成发布 | — |

> **工程意义**：Subagent 从"实验性功能"升级为具备完整数据生命周期、统一渲染层、生产级交互体验的**一级模块**，标志着 LobsterAI 在多 Agent 协作架构上迈出关键一步。

#### 🔧 配置与模型层修复（3 PRs）

| PR | 状态 | 修复内容 |
|:---|:---|:---|
| [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | **CLOSED** | 自定义模型切换错误修复 |
| [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | **CLOSED** | 浏览器配置失效修复 |
| [#2035](https://github.com/netease-youdao/LobsterAI/pull/2035) | **CLOSED** | Qwen 3.6 Plus 编码方案修正 |

#### 🎨 UI/IM 优化（2 PRs）

| PR | 状态 | 内容 |
|:---|:---|:---|
| [#2037](https://github.com/netease-youdao/LobsterAI/pull/2037) | **CLOSED** | IM 相关文案优化 |
| [#2028](https://github.com/netease-youdao/LobsterAI/pull/2028) | **CLOSED** | UI 更新 |

---

## 4. 社区热点

> **警示**：今日社区 PR 与 Issues 的**评论数与互动量极低**，"热点"更多指向**长期未获响应的积压项**，反映社区参与度与维护者带宽的错配。

### 实际讨论量最高的条目

| 排名 | 条目 | 评论数 | 核心诉求 | 状态分析 |
|:---|:---|:---:|:---|:---|
| 1 | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) — OpenClaw gateway 事件扩展请求 | **1** | 要求 `agent:turn`/`agent:loop` 事件以实现实时落盘 | ⚠️ **全新开启**，架构级需求，涉及跨项目（OpenClaw）协调 |
| 2 | 其余所有 PR/Issues | **0-undefined** | — | 无实质讨论 |

### 长期积压的"沉默热点"（stale PRs，今日被更新但未获 review）

| PR | 作者 | 创建时间 | 核心价值 | 风险 |
|:---|:---|:---:|:---|:---|
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | `leedalei` | 2026-04-07 | 主题色选择器 UX 重构（紧凑圆圈替代网格） | 设计方向可能已被内部方案覆盖 |
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | `MaoQianTu` | 2026-04-07 | 本地使用统计面板（SQLite 聚合查询） | 功能实用，但数据隐私合规需 review |
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) | `kayo5994` | 2026-04-07 | **安全修复**：API 代理日志脱敏（防 API Key 泄露） | 🔴 **高危安全项**，45天无响应 |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) | `kayo5994` | 2026-04-07 | **安全修复**：渲染进程 KV Store 键白名单（防越权访问敏感配置） | 🔴 **高危安全项**，45天无响应 |

> **诉求分析**：社区贡献者 `kayo5994` 连续提交两个安全加固 PR，均涉及纵深防御（渲染进程隔离、日志脱敏），但长期未获 maintainer 关注。今日依赖 bot PR 的批量更新反而触发了这些 stale PR 的"更新时间"刷新，形成尴尬的"被关注假象"。

---

## 5. Bug 与稳定性

### 今日已修复（✅ 有 fix PR）

| 严重程度 | 问题 | 修复 PR | 影响范围 |
|:---|:---|:---|:---|
| 🔶 **高** | 自定义模型切换报错 | [#2032](https://github.com/netease-youdao/LobsterAI/pull/2032) | 使用自定义 API 模型的用户 |
| 🔶 **高** | 浏览器配置失效 | [#2031](https://github.com/netease-youdao/LobsterAI/pull/2031) | 依赖内置浏览器的 Agent 工作流 |
| 🔷 **中** | Subagent 同步缺失工具结果/工具输入 | [#2033](https://github.com/netease-youdao/LobsterAI/pull/2033) | 多 Agent 协作场景 |
| 🔷 **中** | Subagent 重复覆盖（`agentId` 碰撞） | [#2029](https://github.com/netease-youdao/LobsterAI/pull/2029) | 同 Agent 多次调用场景 |
| 🔷 **中** | Subagent 生成错误未被回填路径检测 | [#2033](https://github.com/netease-youdou/LobsterAI/pull/2033) | 错误处理与调试体验 |

### 今日新报告（⚠️ 待评估）

| 严重程度 | 问题 | 来源 | 状态 |
|:---|:---|:---|:---|
| 🔶 **高** | OpenClaw gateway 缺乏 `agent:turn`/`agent:loop` 事件，阻碍实时落盘 | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | 待回应，需跨项目协调 |

### 潜在回归风险

- **Subagent 数据迁移**：`subagent_messages` 新表的懒加载回填机制（[#2034](https://github.com/netease-youdao/LobsterAI/pull/2034)）在极端情况下（大量历史会话）可能引发首次访问卡顿
- **渲染管线统一**：`ConversationTurnsView` 组件化（[#2030](https://github.com/netease-youdao/LobsterAI/pull/2030)）虽提升复用性，但主会话与子代理的边界条件差异可能引入边缘 case

---

## 6. 功能请求与路线图信号

### 来自今日 Issue 的明确信号

| 需求 | 来源 | 技术可行性 | 纳入概率评估 |
|:---|:---|:---:|:---|
| **OpenClaw 事件扩展**：`agent:turn` / `agent:loop` 广播事件 | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | 中（需上游协议支持） | **高** — 与当前 Subagent 实时化方向一致，作者 `woxinsj` 疑似内部开发者 |
| **实时落盘机制**：基于上述事件的持久化触发 | [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) | 高（依赖事件实现） | **高** — 产品体验刚需 |

### 来自 stale PR 的潜在功能

| 需求 | 来源 | 障碍 | 纳入概率评估 |
|:---|:---|:---|:---|
| 本地使用统计面板 | [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) | 需 review 数据聚合逻辑与隐私合规 | 中 — 功能实用但非紧急 |
| 主题色选择器 UX 重构 | [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) | 可能已有内部设计方案 | 低 — 易被替代 |

### 版本发布暗示的路线图

`2026.5.22` 版本聚焦 **Subagent 体验闭环** + **模型配置灵活性**，下一迭代可能延伸至：
- Subagent 的**实时状态同步**（与 [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036) 呼应）
- **Thinking 块的可交互性**（当前仅展示，未来可能支持展开/折叠/引用）

---

## 7. 用户反馈摘要

> **数据局限**：今日仅 1 个 Issue 含 1 条评论，样本极小。以下结合近期 Subagent 相关 PR 的 Summary 推断用户场景痛点。

### 明确反馈（来自 [#2036](https://github.com/netease-youdao/LobsterAI/issues/2036)）

| 用户 | 痛点 | 场景 |
|:---|:---|:---|
| `woxinsj` | 缺乏 Agent 轮次结束的事件通知，无法实现**实时落盘** | 需要可靠审计日志、断点续传、或外部系统同步的企业/专业用户 |

### 推断反馈（来自修复 PR 的"问题-解决"映射）

| 原有问题 | 推断用户痛点 | 修复后体验 |
|:---|:---|:---|
| Subagent 消息不持久化 | 重复访问子代理会话需重新网络加载，延迟高、离线不可用 | 二次访问秒开，支持离线回顾 |
| 工具结果/输入不显示 | 无法追溯子代理具体执行了哪些工具、参数是什么 | 完整透明的过程可观测性 |
| 侧边栏高亮状态错乱 | 导航层级混乱，"我在哪"的认知负担 | 状态与视觉反馈一致 |
| Mac 窗口控件重叠返回按钮 | 高频误触关闭/最小化窗口 | 符合 macOS 人机界面规范 |

### 满意度信号

- **正向**：Subagent 从"能用"到"好用"的迭代密度高，团队响应迅速
- **负向**：安全加固类社区贡献长期未获回应，外部贡献者体验受损

---

## 8. 待处理积压

### 🔴 安全类 — 最高优先级

| PR | 创建时间 | 闲置天数 | 风险说明 | 行动建议 |
|:---|:---:|:---:|:---|:---|
| [#1534](https://github.com/netease-youdao/LobsterAI/pull/1534) — API 代理日志脱敏 | 2026-04-07 | **45天** | API Key、Token、对话内容明文写入日志文件，本地文件泄露即导致凭证暴露 | 立即安排 security review，优先合入 |
| [#1535](https://github.com/netease-youdao/LobsterAI/pull/1535) — 渲染进程 KV Store 白名单 | 2026-04-07 | **45天** | 渲染进程可读写 `auth_tokens`、`github_copilot_github_token` 等敏感键，XSS/渲染层漏洞可导致凭证窃取 | 同上，与安全架构评估同步进行 |

### 🟡 依赖升级类 — 技术债务

| PR | 创建时间 | 闲置天数 | 阻塞风险 | 行动建议 |
|:---|:---:|:---:|:---|:---|
| [#1766](https://github.com/netease-youdao/LobsterAI/pull/1766) — Vite 5→8 | 2026-04-20 | **32天** | 构建工具大版本滞后，安全补丁与性能优化无法获取 | 评估 breaking changes 后批量合并 |
| [#1764](https://github.com/netease-youdao/LobsterAI/pull/1764) — React 18→19 | 2026-04-20 | **32天** | 同上，React 19 的并发特性与类型变化需适配 | 与 Vite 升级协同测试 |
| [#1763](https://github.com/netease-youdao/LobsterAI/pull/1763) — @vitejs/plugin-react 4→6 | 2026-04-20 | **32天** | 与 Vite 升级耦合 | 同上 |
| [#1765](https://github.com/netease-youdao/LobsterAI/pull/1765) — Headless UI 1→2 | 2026-04-20 | **32天** | 组件库 API 变更可能影响可访问性实现 | 回归测试无障碍功能 |
| [#1277](https://github.com/netease-youdao/LobsterAI/pull/1277) — Electron 40→42 | 2026-04-02 | **50天** | Chromium 内核滞后，安全漏洞暴露面扩大 | 评估 Electron 42 的 breaking changes（如原生模块 ABI） |

### 🟢 功能体验类 — 社区贡献吸纳

| PR | 创建时间 | 闲置天数 | 价值 | 行动建议 |
|:---|:---:|:---:|:---|:---|
| [#1533](https://github.com/netease-youdao/LobsterAI/pull/1533) — 本地使用统计 | 2026-04-07 | **45天** | 用户数据洞察，提升产品粘性 | 确认与内部数据埋点方案是否冲突 |
| [#1531](https://github.com/netease-youdao/LobsterAI/pull/1531) — 主题色选择器 | 2026-04-07 | **45天** | 设置页视觉简化 | 设计团队确认方向，或礼貌关闭并说明 |

---

## 附录：数据健康度仪表盘

| 指标 | 数值 | 评估 |
|:---|:---:|:---|
| 24h PR 吞吐量 | 12 关闭 / 9 待合并 | ✅ 高执行效率 |
| 社区 PR review 响应率（>30天） | 0%（5个 stale PR 均未处理） | 🔴 严重滞后 |
| 安全相关 PR 响应率 | 0%（2个安全 PR 均 45天未响应） | 🔴 高危 |
| Issue 首次响应时间 | 待观察（#2036 刚创建） | ⏳ 待定 |
| 版本发布频率 | 近3日内连续发布（5.19 → 5.22） | ✅ 敏捷交付 |

---

> **分析师备注**：LobsterAI 核心团队展现了极强的**功能交付能力**，Subagent 模块的快速迭代体现了产品化决心。但**社区治理与健康度存在明显短板**——安全加固贡献长期搁置、依赖升级堆积、外部 PR 缺乏反馈闭环，这些结构性问题若不及时改善，将影响开源

</details>

<details>
<summary><strong>TinyClaw</strong> — <a href="https://github.com/TinyAGI/tinyagi">TinyAGI/tinyagi</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>Moltis</strong> — <a href="https://github.com/moltis-org/moltis">moltis-org/moltis</a></summary>

# Moltis 项目动态日报 | 2026-05-23

> **项目**: moltis-org/moltis | **日期**: 2026-05-23 | **分析周期**: 过去24小时

---

## 1. 今日速览

Moltis 今日呈现**高强度迭代态势**：24小时内 **9个PR全部完成合并/关闭**，**7个Issue同步关闭**，仅余1个新UI问题待处理。核心贡献者 `penso` 单日输出8个PR，覆盖语音合成、文档访问、文件附件、电话通道、沙箱安全等关键模块，显示团队正处于**功能完善与Bug清扫的冲刺阶段**。Docker部署场景成为今日修复重点，反映生产环境适配需求迫切。无新版本发布，但代码主干快速演进。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 🔧 核心功能落地（5项）

| PR | 功能/修复 | 技术要点 | 关联Issue |
|:---|:---|:---|:---|
| [#1044](https://github.com/moltis-org/moltis/pull/1044) | **Agent本地文档访问** | 四层回退机制：环境变量 → 打包文档 → 源码文档 → 内嵌兜底；生成配置模板引用 | [#1028](https://github.com/moltis-org/moltis/issues/1028) |
| [#1042](https://github.com/moltis-org/moltis/pull/1042) | **Web UI任意文件附件** | 非图片附件上传至session媒体存储，传递MIME类型与字节大小元数据，渲染文件卡片 | [#1036](https://github.com/moltis-org/moltis/issues/1036) |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) | **Vault加密可选禁用** | `auth.vault_enabled`配置项；解密后切换需认证API，覆盖env/SSH/渠道密钥等 | — |
| [#1043](https://github.com/moltis-org/moltis/pull/1043) | **Piper TTS WAV元数据** | 区分`AudioFormat::Pcm`与`WAV`，非PCM请求自动包装WAV头 | [#1029](https://github.com/moltis-org/moltis/issues/1029) |
| [#1041](https://github.com/moltis-org/moltis/pull/1041) | **OpenAI TTS格式适配** | OpenAI兼容服务强制MP3，非OpenAI保留OGG/Opus避免质量损失 | [#1030](https://github.com/moltis-org/moltis/issues/1030) |

### 🐛 Docker/部署稳定性（3项）

| PR | 问题域 | 修复策略 |
|:---|:---|:---|
| [#1040](https://github.com/moltis-org/moltis/pull/1040) | 沙箱媒体文件读取 | 挂载主机读取失败时回退容器内读取；`docker cp` stderr分类避免空tar流 | [#977](https://github.com/moltis-org/moltis/issues/977), [#1037](https://github.com/moltis-org/moltis/issues/1037) |
| [#1035](https://github.com/moltis-org/moltis/pull/1035) | 沙箱浏览器Profile挂载 | 运行时扫描Docker/Podman容器自动检测主机数据挂载 | [#977](https://github.com/moltis-org/moltis/issues/977) |
| [#1034](https://github.com/moltis-org/moltis/pull/1034) | Twilio电话语音收集 | `SpeechResult`/`Digits`优先于`CallStatus=in-progress`解析；增加回归测试 | [#1032](https://github.com/moltis-org/moltis/issues/1032) |

### 📦 依赖维护（1项）

| PR | 内容 |
|:---|:---|
| [#1039](https://github.com/moltis-org/moltis/pull/1039) | OpenSSL 0.10.79 → 0.10.80（安全/兼容性更新）|

**整体评估**：今日PR矩阵覆盖**开发者体验**（文档、附件）、**语音通道完整性**（TTS格式、电话交互）、**部署可靠性**（Docker沙箱）三大战略方向，项目成熟度显著提升。

---

## 4. 社区热点

### 讨论最活跃：Issue #977 — Docker沙箱浏览器崩溃
- **链接**: [moltis-org/moltis#977](https://github.com/moltis-org/moltis/issues/977)
- **数据**: 5条评论，0👍，创建16天后关闭
- **诉求分析**: Proxmox+LXC+Docker嵌套环境下的浏览器沙箱故障，涉及容器套娃、socket挂载、命名卷等多重复杂因素。用户`TLA020`提供了详尽的环境描述与错误日志，体现**企业级自托管用户**的典型痛点——基础设施越复杂，Moltis的部署适配越具挑战。

### 次活跃：Issue #1028 — Agent默认访问Moltis文档
- **链接**: [moltis-org/moltis#1028](https://github.com/moltis-org/moltis/issues/1028)
- **数据**: 2条评论，0👍，3天快速闭环
- **诉求分析**: 用户`IlyaBizyaev`（同时也是多个Issue报告者）提出Agent应"开箱即用"访问本地文档，而非依赖外部网络。这反映**离线/隐私敏感场景**的强烈需求，PR #1044 的四层回退设计直接回应了这一诉求。

> **社区信号**：活跃贡献者`IlyaBizyaev`兼具"用户+准贡献者"双重角色，24小时内提交4个Issue（3个已关闭），是高质量反馈源。

---

## 5. Bug 与稳定性

| 优先级 | Issue | 状态 | 根因 | Fix PR | 影响范围 |
|:---|:---|:---|:---|:---|:---|
| 🔴 **高** | [#977](https://github.com/moltis-org/moltis/issues/977) Docker沙箱浏览器失败 | ✅ 已关闭 | 容器内文件路径解析与挂载可见性 | #1040, #1035 | Docker部署用户 |
| 🟡 **中** | [#1030](https://github.com/moltis-org/moltis/issues/1030) OpenAI TTS强制opus | ✅ 已关闭 | 硬编码`response_format: opus`，Speaches服务不兼容 | #1041 | 使用OpenAI兼容TTS服务的用户 |
| 🟡 **中** | [#1032](https://github.com/moltis-org/moltis/issues/1032) Twilio电话无响应 | ✅ 已关闭 | Twilio gather事件解析顺序错误，`CallStatus`优先于语音结果 | #1034 | 电话通道用户 |
| 🟡 **中** | [#1037](https://github.com/moltis-org/moltis/issues/1037) Docker中send_image/send_document失败 | ✅ 已关闭 | 沙箱文件读取路径解析错误 | #1040 | Docker部署的媒体发送功能 |
| 🟢 **低** | [#1045](https://github.com/moltis-org/moltis/issues/1045) 浅色模式代码块无高亮 | ⏳ **开放** | UI主题样式问题 | — | 浅色模式用户 |

**稳定性态势**：**4/5 Bug已修复**，剩余#1045为纯UI问题，无功能阻塞。Docker部署链路的系统性修复（#1040+#1035）消除了近期最高频的故障模式。

---

## 6. 功能请求与路线图信号

| 来源 | 需求 | 实现状态 | 纳入可能性 |
|:---|:---|:---|:---|
| [#1028](https://github.com/moltis-org/moltis/issues/1028) | Agent本地文档OOTB访问 | ✅ PR #1044 已合并 | **已纳入**，将成为默认行为 |
| [#1029](https://github.com/moltis-org/moltis/issues/1029) | Piper TTS内部处理音频转换 | ✅ PR #1043 已合并 | **已纳入**，WAV格式支持完善 |
| [#1036](https://github.com/moltis-org/moltis/issues/1036) | Web UI任意文件附件 | ✅ PR #1042 已合并 | **已纳入**，扩展多模态能力 |
| [#1033](https://github.com/moltis-org/moltis/pull/1033) | Vault加密可选禁用 | ✅ 已合并 | **已纳入**，降低部署门槛 |

**路线图推断**：近期版本（预计`20260525.x`或`20260601.x`）将聚焦：
1. **部署简化**（Vault可选、Docker自动检测）
2. **语音通道完善**（TTS格式生态兼容、电话交互稳定）
3. **Agent能力增强**（本地文档、文件附件处理）

---

## 7. 用户反馈摘要

### 😤 痛点
| 场景 | 反馈来源 | 核心不满 |
|:---|:---|:---|
| Docker嵌套部署 | #977 | "Failed to create /data/browse..."——沙箱在复杂容器环境中可靠性差 |
| 电话交互断裂 | #1032 | "Agent问候后永不响应"——Twilio集成存在关键路径Bug |
| 第三方TTS兼容 | #1030 | Speaches等OpenAI兼容服务因opus格式被拒绝 |

### 😊 满意/期待
| 场景 | 反馈来源 | 积极信号 |
|:---|:---|:---|
| 文档本地化 | #1028 | 用户主动提出并快速实现，体现需求响应效率 |
| 文件附件扩展 | #1036 | 从"仅图片"到"任意文件"的能力扩展受期待 |

### 🔍 使用模式洞察
- **自托管为主**：Issues中Docker、Proxmox、LXC等关键词高频出现，用户群体偏向技术自主型
- **语音通道活跃**：TTS/电话相关Issue占比高，语音交互是核心使用场景
- **多服务集成**：Speaches（TTS）、Twilio（电话）、OpenAI兼容API等生态整合需求强烈

---

## 8. 待处理积压

| Issue | 创建时间 | 状态 | 风险 | 建议动作 |
|:---|:---|:---|:---|:---|
| [#1045](https://github.com/moltis-org/moltis/issues/1045) 浅色模式代码块无高亮 | 2026-05-22 | ⏳ 开放 | 🟢 低 | 前端样式修复，可标记`good first issue`吸引社区贡献 |
| — | — | — | — | 当前积压健康，无长期未响应关键Issue |

**维护者提醒**：今日关闭7个Issue后，项目开放Issue总量显著下降。建议关注：
1. **#1045** 的快速分配（纯前端，修复成本低）
2. **#977类Docker复杂环境**是否有衍生场景未覆盖
3. **penso** 单点贡献集中度较高，需考虑知识分散与reviewer负载

---

> **日报生成依据**: GitHub Issues/PRs 元数据与摘要内容 | **数据截止**: 2026-05-23 00:00 UTC

</details>

<details>
<summary><strong>CoPaw</strong> — <a href="https://github.com/agentscope-ai/CoPaw">agentscope-ai/CoPaw</a></summary>

# CoPaw 项目动态日报 | 2026-05-23

> **项目**: CoPaw (github.com/agentscope-ai/CoPaw)  
> **数据周期**: 2026-05-22 至 2026-05-23  
> **报告日期**: 2026-05-23

---

## 1. 今日速览

CoPaw 今日保持**高活跃度**，24小时内产生 **24 条 Issues 更新**（17 新开/活跃，7 关闭）和 **23 条 PR 更新**（13 待合并，10 已合并/关闭），无新版本发布。社区聚焦三大主题：**聊天历史数据可靠性**（#4620 获 12 条评论成为今日最热）、**多模型兼容性修复**（Gemini/Gemma 参数映射、MiniMax XML 解析、DeepSeek think 标签），以及**开发者体验优化**（可定制斜杠菜单、插件生命周期钩子）。整体项目健康度良好，修复闭环率约 30%（7/24 Issues 关闭），但核心数据丢失类 Bug 尚未有 PR 跟进需重点关注。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭的重要 PR（10 条）

| PR | 作者 | 核心贡献 | 关联 Issue |
|:---|:---|:---|:---|
| [#4621](https://github.com/agentscope-ai/QwenPaw/pull/4621) | qbc2016 | **修复 Gemini/Gemma 模型崩溃**：将 `max_tokens` 正确映射为 `max_output_tokens`，解决 pydantic ValidationError 被误分类为 `MODEL_UNAUTHORIZED_ACCESS` 的问题 | [#4605](https://github.com/agentscope-ai/QwenPaw/issues/4605) |
| [#4627](https://github.com/agentscope-ai/QwenPaw/pull/4627) | hongxicheng | **修复 WeChat 跨请求 Token 污染**：将实例级 `_context_token_invalid` 标志改为请求级元数据标志，避免单次请求 Token 失效阻塞后续所有请求（含定时任务） | [#4612](https://github.com/agentscope-ai/QwenPaw/issues/4612), [#4618](https://github.com/agentscope-ai/QwenPaw/pull/4618) |
| [#4600](https://github.com/agentscope-ai/QwenPaw/pull/4600) | hongxicheng | **修复钉钉中文文件名乱码**：RFC 8089 file:// URL 中的百分号编码中文文件名未解码，导致上传文件显示为 `%E7%99%BE...` | [#4586](https://github.com/agentscope-ai/QwenPaw/issues/4586) |
| [#4434](https://github.com/agentscope-ai/QwenPaw/pull/4434) | weixizi | **定时任务上下文隔离**：新增 "Clear Before Run" 选项，执行前静默重置对话上下文，防止历史累积干扰自动化任务 | [#4432](https://github.com/agentscope-ai/QwenPaw/issues/4432), [#4162](https://github.com/agentscope-ai/QwenPaw/issues/4162) |
| [#4626](https://github.com/agentscope-ai/QwenPaw/pull/4626) | Osier-Yi | **修复 QwenPaw Pet 连续对话卡死**：阻塞事件错误推进序列高水位标记，导致后续 `query.received` 被丢弃为"过期"状态 | - |
| [#4623](https://github.com/agentscope-ai/QwenPaw/pull/4623) | zhaozhuang521 | **技能市场页面样式优化**：替换菜单图标、代码与性能优化 | - |
| [#4618](https://github.com/agentscope-ai/QwenPaw/pull/4618) | hongxicheng | ~~WeChat Token 失效跳过机制（已被 #4627 替代）~~ | - |
| [#4636](https://github.com/agentscope-ai/QwenPaw/pull/4636) | DICKQI | ~~可定制斜杠菜单（关闭，由 #4637 替代）~~ | - |
| [#4395](https://github.com/agentscope-ai/QwenPaw/pull/4395) | aqilaziz | 安全模块工具守卫单元测试覆盖 | - |

**整体推进评估**：今日合并 PR 覆盖**模型兼容性**（Gemini 参数映射）、**通道稳定性**（WeChat/钉钉）、**自动化可靠性**（定时任务上下文隔离）三大核心领域，均为生产环境高频痛点。hongxicheng 单日贡献 3 个修复 PR，成为今日最活跃贡献者。

---

## 4. 社区热点

### 🔥 讨论最活跃的 Issues/PRs

| 排名 | 条目 | 评论数 | 热度分析 |
|:---|:---|:---|:---|
| **1** | [#4620 [Bug] Chat history disappeared](https://github.com/agentscope-ai/QwenPaw/issues/4620) | **12** | **数据丢失类严重 Bug**，用户反馈切换会话后聊天记录随机消失，"存在已久"。作者 duwey 提供截图证据，社区高度关切但**尚无 PR 修复**。涉及 v1.1.8.post1，影响用户信任根基 |
| **2** | [#4051 [Question] DeepSeek think 内容解析](https://github.com/agentscope-ai/QwenPaw/issues/4051) | **10** | 已关闭。DeepSeek V4 Flash 的 `<thinking>` 标签内容未被正确解析为回复，导致"无响应"。历时 16 天解决，反映模型适配层对新兴模型特性跟进滞后 |
| **3** | [#4474 [Question] 支持 ChatGPT-5.5 吗？](https://github.com/agentscope-ai/QwenPaw/issues/4474) | **8** | 用户配置后无法使用，配置截图显示模型选择 UI 问题。OpenAI 新模型支持滞后，文档/配置引导不足 |
| **4** | [#4607 [Bug] NO_PROXY 环境变量未生效](https://github.com/agentscope-ai/QwenPaw/issues/4607) | **6** | 企业内网环境高频问题，代理配置绕过失败影响部署 |

**诉求洞察**：社区核心焦虑集中在**数据可靠性**（#4620）和**模型兼容性时效性**（#4474, #4051）。用户期望 CoPaw 作为 AI 助手基础设施，在"不丢数据"和"快速跟进新模型"上达到生产级标准。

---

## 5. Bug 与稳定性

### 按严重程度排列

| 严重程度 | Issue | 描述 | 状态 | Fix PR |
|:---|:---|:---|:---|:---|
| 🔴 **P0-数据丢失** | [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620) | 聊天历史随机消失，切换会话后无法找回原始消息 | **OPEN，12 评论，无 PR** | ❌ 无 |
| 🟠 **P1-崩溃/功能阻断** | [#4625](https://github.com/agentscope-ai/QwenPaw/issues/4625) | MiniMax-M2.5 返回 XML 格式思考过程，导致指令执行中断、问答失败 | OPEN，4 评论 | ❌ 无 |
| 🟠 **P1-功能阻断** | [#4556](https://github.com/agentscope-ai/QwenPaw/issues/4556) | 语音转写忽略配置的 Whisper API，强制使用浏览器原生 Speech API | OPEN，4 评论 | ❌ 无 |
| 🟡 **P2-功能异常** | [#4607](https://github.com/agentscope-ai/QwenPaw/issues/4607) | `NO_PROXY` 环境变量配置后仍走代理 | OPEN，6 评论 | ❌ 无 |
| 🟡 **P2-功能异常** | [#4616](https://github.com/agentscope-ai/QwenPaw/issues/4616) | "梦境觉醒"任务报错，未配置 WeChat 却触发 WeChat 通道错误 | OPEN，3 评论 | ❌ 无 |
| 🟡 **P2-UI 不一致** | [#4619](https://github.com/agentscope-ai/QwenPaw/issues/4619) | Web UI 语言/暗模式按钮垂直对齐、下拉箭头样式不一致 | OPEN，1 评论 | ❌ 无 |
| 🟢 **P3-已修复** | [#4605](https://github.com/agentscope-ai/QwenPaw/issues/4605) | Gemini/Gemma `max_tokens` 参数校验失败崩溃 | ✅ CLOSED | [#4621](https://github.com/agentscope-ai/QwenPaw/pull/4621) |
| 🟢 **P3-已修复** | [#4612](https://github.com/agentscope-ai/QwenPaw/issues/4612) | WeChat `send_file_to_user` 图片发送不稳定/虚假成功 | ✅ CLOSED | [#4627](https://github.com/agentscope-ai/QwenPaw/pull/4627) |
| 🟢 **P3-已修复** | [#4586](https://github.com/agentscope-ai/QwenPaw/issues/4586) | 钉钉发送图片中文文件名百分号编码 | ✅ CLOSED | [#4600](https://github.com/agentscope-ai/QwenPaw/pull/4600) |

**稳定性评估**：P0 级数据丢失 Bug（#4620）无修复进展是最大风险点；MiniMax 生态兼容性（#4625, #3707）存在系统性问题，需模型适配层专项优化。

---

## 6. 功能请求与路线图信号

### 高潜力功能请求（已有 PR 或强信号）

| 功能 | Issue/PR | 状态 | 纳入下一版本可能性 |
|:---|:---|:---|:---|
| **可定制斜杠命令菜单** | [#4633](https://github.com/agentscope-ai/QwenPaw/issues/4633) → [#4637](https://github.com/agentscope-ai/QwenPaw/pull/4637) | PR 已开，作者即需求提出者 | **高** — 实现完整，社区驱动 |
| **插件生命周期钩子** | [#4613](https://github.com/agentscope-ai/QwenPaw/issues/4613) → [#4638](https://github.com/agentscope-ai/QwenPaw/pull/4638) | PR 已开，first-time contributor | **高** — 插件生态基础设施 |
| **插件 ZIP 导出/下载** | [#4628](https://github.com/agentscope-ai/QwenPaw/pull/4628) | PR 已开 | **中高** — 备份/迁移刚需 |
| **MCP 管理增强（市场/健康检查/密钥验证）** | [#4630](https://github.com/agentscope-ai/QwenPaw/pull/4630) | PR 已开 | **中高** — MCP 生态关键能力 |
| **Tauri 2.x 桌面端支持** | [#3813](https://github.com/agentscope-ai/QwenPaw/pull/3813) | 长期 OPEN，4 月提出 | **中** — 架构级变更，需持续投入 |
| **DataPaw 数据分析插件（12 BI skills）** | [#4622](https://github.com/agentscope-ai/QwenPaw/pull/4622) | PR 已开，first-time contributor | **中** — 垂直场景扩展 |

### 待观察需求（无 PR）

| 功能 | Issue | 核心痛点 |
|:---|:---|:---|
| 按模型独立配置重试/并发限流 | [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624) | 多厂商模型配额差异大，全局配置成为瓶颈 |
| 远程 Playwright 浏览器端点 | [#4617](https://github.com/agentscope-ai/QwenPaw/issues/4617) | 资源共享、避免重复安装 |
| WebUI 移动端响应式设计 | [#4635](https://github.com/agentscope-ai/QwenPaw/issues/4635) | 现有渠道仅基础对话，无法管理配置 |
| 桌面端窗口大小位置记忆 | [#4634](https://github.com/agentscope-ai/QwenPaw/issues/4634) | 每次启动重置为 1280×800 |

---

## 7. 用户反馈摘要

### 😤 核心痛点

> **"I think it's a critical bug and existed for a long time."** — duwey, [#4620](https://github.com/agentscope-ai/QwenPaw/issues/4620)

- **数据可靠性焦虑**：聊天记录消失"存在已久"，用户截图证明对话存在但 UI 不显示，严重侵蚀信任
- **模型适配滞后**：ChatGPT-5.5 配置无效、DeepSeek think 标签解析错误、MiniMax XML 格式不兼容 — 新模型/新特性跟进慢
- **企业部署障碍**：`NO_PROXY` 不生效、钉钉中文文件名乱码、WeChat 图片发送不稳定 — 内网/国内通道场景打磨不足
- **开发者体验断层**：缺少多行文本写入工具（#4632），Skill 开发、脚本持久化受阻；20+ 内置命令仅 4-5 个在快捷菜单暴露

### 👍 满意/认可

- 定时任务"Clear Before Run"功能被快速合并（[#4434](https://github.com/agentscope-ai/QwenPaw/pull/4434)），用户认可"防止历史累积干扰"的设计
- 插件系统扩展性获积极使用（LightRAG 知识库、DataPaw BI），但钩子机制缺失限制深度集成

### 🔍 典型使用场景

| 场景 | 代表 Issue | 规模信号 |
|:---|:---|:---|
| 多模型混合生产环境 | [#4624](https://github.com/agentscope-ai/QwenPaw/issues/4624) MiniMax M2.7 + M2.5 并发 | 企业级，关注配额与稳定性 |
| 跨平台自动化通知 | [#4521](https://github.com/agentscope-ai/QwenPaw/issues/4521) HTTP API → WeChat 个人号 | 个人/小团队，替代传统通知系统 |
| 桌面端日常助手 | [#4634](https://github.com/agentscope-ai/QwenPaw/issues/4634), [#4631](https://github.com/agentscope-ai/QwenPaw/issues/4631) | 对窗口管理、图标细节敏感 |
| ACP 外部 Agent 编排 | [#4611](https://github.com/agentscope-ai/QwenPaw/issues/4611) | 进阶用户，探索多 Agent 协作 |

---

## 8. 待处理积压

### ⚠️ 需维护者重点关注

| Issue/PR | 创建时间 | 当前状态 | 风险说明 |
|:---|:---|:---|:---|
| [#4620 Chat history disappeared](https://github.com/agentscope-ai/QwenPaw/issues/4620) | 2026-05-22 | **OPEN，12 评论，无 PR，P0** | 数据丢失类 Bug 若 48 小时内无响应，将引发社区信任危机 |
| [#3984 context_check splits user/assistant pairs](https://github.com/agentscope-ai/QwenPaw/issues/3984) | 2026-04-30 | OPEN，3 评论，22 天 | 上下文压缩导致孤儿消息，与 #4620 可能同源，需关联分析 |
| [#3707 MiniMax M2.7 图片识别硬编码为 False](https://github.com/agentscope-ai/QwenPaw/issues/3707) | 2026-04-22 | CLOSED 但 #4625 同类问题再现 | 模型能力声明机制需系统性重构，非个案修复 |
| [#3813 Tauri 桌面端支持](https://github.com/agentscope-ai/QwenPaw/pull/3813) | 2026-04-24 | OPEN，Under Review，29 天 | 架构级 PR 长期悬置，影响桌面端路线图清晰度 |
| [#4464 python_e2e 迁移至 CoPaw](https://github.com/agentscope-ai/QwenPaw/pull/4464) | 2026-05-17 | OPEN，6 天 | 测试基础设施，阻塞质量门禁升级 |

---

> **日报生成说明**：本报告基于 GitHub 公开数据自动分析，所有链接可点击验证。建议维护者优先处理 #4620（数据丢失）并评估 #3984 与 #4620 的关联性。

</details>

<details>
<summary><strong>ZeptoClaw</strong> — <a href="https://github.com/qhkm/zeptoclaw">qhkm/zeptoclaw</a></summary>

过去24小时无活动。

</details>

<details>
<summary><strong>ZeroClaw</strong> — <a href="https://github.com/zeroclaw-labs/zeroclaw">zeroclaw-labs/zeroclaw</a></summary>

# ZeroClaw 项目动态日报 | 2026-05-23

## 1. 今日速览

ZeroClaw 今日保持**高强度开发节奏**，24小时内 Issues 更新 37 条（30 活跃/7 关闭）、PR 更新 50 条（36 待合并/14 已合并关闭），无新版本发布。项目核心关注点集中在 **MCP 工具过滤修复**、**WhatsApp 协议兼容性恢复**、**TUI 终端界面集成**三大主线，同时"Dream Mode"记忆巩固功能进入实质性 PR 阶段。社区治理层面，工作流标签自动化 RFC 引发讨论，反映项目规模扩大后的组织需求。

---

## 2. 版本发布

**无新版本发布**

---

## 3. 项目进展

### 已合并/关闭的重要 PR

| PR | 作者 | 核心贡献 | 关联 Issue |
|:---|:---|:---|:---|
| [#6706](https://github.com/zeroclaw-labs/zeroclaw/pull/6706) | alexandme | **WhatsApp Web 协议修复**：将 `wa-rs*` 0.2 升级至 `whatsapp-rust` 0.6，恢复 2026-04-24 服务端协议变更后的消息收发能力 | [#6246](https://github.com/zeroclaw-labs/zeroclaw/issues/6246) |
| [#6838](https://github.com/zeroclaw-labs/zeroclaw/pull/6838) | puneetdixit200 | **Doctor 诊断工具修复**：`zeroclaw doctor models` 现在正确读取配置的 provider 凭据，解决自定义 provider 模型列表获取失败问题 | [#6756](https://github.com/zeroclaw-labs/zeroclaw/issues/6756) |
| [#6009](https://github.com/zeroclaw-labs/zeroclaw/pull/6009) | alexandme | **OTel 可观测性增强**：工具调用 span 新增 `gen_ai.tool.*` 语义约定属性，包含 `tool_call_id`、`arguments`、`result`，支持完整链路追踪 | [#5980](https://github.com/zeroclaw-labs/zeroclaw/issues/5980) |
| [#6804](https://github.com/zeroclaw-labs/zeroclaw/pull/6804) | vernonstinebaker | **部署脚本改进**：`zeroclaw.service` 模板用户名参数化，移除硬编码 `pi`，支持非 Raspberry Pi 标准用户名的板级部署 | — |
| [#6814](https://github.com/zeroclaw-labs/zeroclaw/pull/6814) | Project516 | **CI 标签修复**：`labeler.yml` 排除 `.github` 目录中非 CI 相关文件的误标 | [#6748](https://github.com/zeroclaw-labs/zeroclaw/pull/6748) |
| [#6769](https://github.com/zeroclaw-labs/zeroclaw/pull/6769) | Project516 | **文档修复**：`philosophy.md` 中 5 处损坏的 GitHub issue 链接格式修正 | — |
| [#6748](https://github.com/zeroclaw-labs/zeroclaw/pull/6748) | Project516 | **资源优化**：24 张图片/SVG 资产无损压缩，减小仓库体积 | — |

**整体推进评估**：WhatsApp 渠道 S1 级阻断故障彻底解除，自定义 provider 的运维体验闭环完成，可观测性基础设施向 OpenTelemetry 语义标准对齐。TUI 大型集成 PR [#6848](https://github.com/zeroclaw-labs/zeroclaw/pull/6848) 待合并，将成为 v0.8.0 里程碑的关键交付。

---

## 4. 社区热点

### 讨论最活跃的 Issues

| 排名 | Issue | 评论 | 核心诉求 |
|:---|:---|:---|:---|
| 🔥1 | [#5849 Dream Mode — 周期性记忆巩固与反思学习](https://github.com/zeroclaw-labs/zeroclaw/issues/5849) | 11 | **长期记忆架构的范式升级**：社区期望 ZeroClaw 具备"离线学习"能力，在空闲时段自动整合日间交互、更新知识结构，而非仅依赖即时 RAG。该功能被标记为 `risk: high` + `priority:p1`，已有 PR [#6693](https://github.com/zeroclaw-labs/zeroclaw/pull/6693) 实现 5 阶段引擎（gather→reflect→consolidate→prune→sleep） |
| 🔥2 | [#6246 WhatsApp Web 协议升级后消息中断](https://github.com/zeroclaw-labs/zeroclaw/issues/6246) | 6 | **企业级渠道稳定性**：WhatsApp 作为核心商业渠道，服务端协议变更的响应速度直接影响用户信任。已关闭并验证修复 |
| 🔥3 | [#6699 `tool_filter_groups` 对真实 MCP 工具无效](https://github.com/zeroclaw-labs/zeroclaw/issues/6699) | 6 | **MCP 生态工具治理**：配置层与运行层的语义断裂——`AgentConfig` 正确解析但 dispatch 时前缀匹配逻辑错误，同时与 `deferred_loading` 无集成。PR [#6861](https://github.com/zeroclaw-labs/zeroclaw/pull/6861) 已提交修复 |

### 治理层面 RFC

[#6808 Work Lanes, Board Automation, and Label Cleanup](https://github.com/zeroclaw-labs/zeroclaw/issues/6808)（4 评论）—— 维护者 Audacity88 提出轻量级 PR 分道机制、board 自动化标签规则，回应项目规模扩张后的协作摩擦。信号：ZeroClaw 正从"精英小团队"向"结构化开源组织"过渡。

---

## 5. Bug 与稳定性

| 严重程度 | Issue | 状态 | 修复 PR | 影响范围 |
|:---|:---|:---|:---|:---|
| **S1 - workflow blocked** | [#6699](https://github.com/zeroclaw-labs/zeroclaw/issues/6699) `tool_filter_groups` MCP 前缀匹配失效 | `status:accepted` | [#6861](https://github.com/zeroclaw-labs/zeroclaw/pull/6861) OPEN | 所有使用 MCP 工具过滤的 agent 配置实际失效，skill 工具被误过滤 |
| **S1 - workflow blocked** | [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) WhatsApp 渠道 QR 码不显示 | `status:accepted` | 待确认 | 新用户无法完成 WhatsApp 渠道 onboarding |
| **S1 - workflow blocked** | [#6841](https://github.com/zeroclaw-labs/zeroclaw/issues/6841) `vision_provider` 被静默忽略，图片路由至 fallback | `status:accepted` | 无 | 多模态配置失效，视觉理解能力降级 |
| **S1 - workflow blocked** | [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844) Slack `bot_token` 不支持环境变量注入 | `status:accepted` | 无 | 重复回归（#6237 修复后复发），安全部署实践受阻 |
| **S1 - workflow blocked** | [#6036](https://github.com/zeroclaw-labs/zeroclaw/issues/6036) Termux/Android 无限工具调用循环 | `status:blocked` `needs-author-action` | 无 | 移动端/边缘部署核心障碍，需复现信息 |
| **S2 - degraded behavior** | [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836) `setup.bat --minimal` 构建体积 26MB 而非预期 6MB | `status:accepted` | 无 | Windows 最小化部署文档与实际不符 |
| **S2 - degraded behavior** | [#6856](https://github.com/zeroclaw-labs/zeroclaw/issues/6856) `show_tool_calls` 在 schema v3 渠道配置中缺失 | 新上报 | 无 | 渠道调试可见性降级（v2→v3 迁移遗漏） |

**稳定性评估**：WhatsApp 主协议故障已解除，但渠道层（QR、Slack token、多模态路由）连续出现 S1 级配置/集成问题，显示 v0.8.0 配置 schema 变更的迁移工具链存在盲区。MCP 工具过滤的修复 PR 需优先 review。

---

## 6. 功能请求与路线图信号

| 功能 | Issue/PR | 成熟度 | 纳入下一版本概率 |
|:---|:---|:---|:---|
| **Dream Mode 记忆巩固** | [#5849](https://github.com/zeroclaw-labs/zeroclaw/issues/5849) + [#6693](https://github.com/zeroclaw-labs/zeroclaw/pull/6693) | PR 已提交，5 阶段引擎实现，本地优先+可选 LLM 反射 | **高** — v0.8.0 核心卖点 |
| **TUI Agent Chat 终端界面** | [#6824](https://github.com/zeroclaw-labs/zeroclaw/issues/6824) + [#6848](https://github.com/zeroclaw-labs/zeroclaw/pull/6848) | 大型集成 PR 待合并，Ratatui 基础聊天已实现 | **高** — 依赖 #6848 merge |
| **Runtime RPC + Unix Socket 传输** | [#6837](https://github.com/zeroclaw-labs/zeroclaw/issues/6837) | `size: XL`，`status:in-progress`，绕过 HTTP/WS 网关的 daemon 直连 | **中** — 架构基础设施，可能 v0.8.x |
| **Session 级运行时参数覆盖** | [#6817](https://github.com/zeroclaw-labs/zeroclaw/issues/6817) | `status:in-progress`，无需 daemon 重载的模型/温度动态调整 | **中** — 与 #6837 协同 |
| **ACP 协议 diff/文件提案扩展** | [#6820](https://github.com/zeroclaw-labs/zeroclaw/issues/6820) | `status:in-progress`，TUI/Web 侧-by-side diff 审批 | **中** — TUI 体验增强 |
| **MemoryStrategy trait 解耦** | [#6850](https://github.com/zeroclaw-labs/zeroclaw/issues/6850) | 新 RFC，抽象记忆策略层与存储后端 | **低-中** — 架构债务，长期 |
| **Telegram 自定义 WebAPI 端点** | [#6807](https://github.com/zeroclaw-labs/zeroclaw/issues/6807) | `status:accepted`，区域性网络受限场景 | **中** — 渠道扩展 |
| **Signal  outbound 表情反应** | [#6840](https://github.com/zeroclaw-labs/zeroclaw/pull/6840) | PR 待合并，`needs-author-action` | **中** — 渠道体验对齐 |

---

## 7. 用户反馈摘要

### 痛点

| 来源 | 反馈 | 场景 |
|:---|:---|:---|
| [#6246](https://github.com/zeroclaw-labs/zeroclaw/issues/6246) alexandme | "WhatsApp Web 配对成功但消息不流通" | 企业客服机器人，协议升级后生产环境静默失效 |
| [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) MushiTheMoshi | "WhatsApp 渠道不显示 QR 码，无法完成 onboarding" | 新用户首次部署，阻塞在第一步 |
| [#6844](https://github.com/zeroclaw-labs/zeroclaw/issues/6844) mgstoyanov | "Slack bot_token 必须写死在配置，不能用环境变量" | 安全合规部署（12-factor），回归问题引发挫败 |
| [#6836](https://github.com/zeroclaw-labs/zeroclaw/issues/6836) rockswang | "按文档最小构建，结果 26MB 不是 6MB" | Windows 资源受限环境，文档信任度受损 |
| [#6036](https://github.com/zeroclaw-labs/zeroclaw/issues/6036) aichixiguaj | "Android/Termux 上 agent 进入无限循环，重复相同消息" | 移动端边缘计算，Termux 开发者场景 |

### 满意/期待

| 来源 | 反馈 |
|:---|:---|
| [#5849](https://github.com/zeroclaw-labs/zeroclaw/issues/5849) Svtter | 对"Dream Mode"概念高度认同，期望"轻量级后台进程，整合日间记忆、反思交互" |
| [#6847](https://github.com/zeroclaw-labs/zeroclaw/issues/6847) MushiTheMoshi | "Best tool out there. Wishing way more stars." — 产品认可与增长期待 |
| [#6253](https://github.com/zeroclaw-labs/zeroclaw/issues/6253) singlerider | Skills 系统 v0.7.6 追踪器主动征集社区输入，反映开放治理姿态 |

---

## 8. 待处理积压

| Issue/PR | 创建时间 | 当前状态 | 风险 | 提醒 |
|:---|:---|:---|:---|:---|
| [#6074](https://github.com/zeroclaw-labs/zeroclaw/issues/6074) 153 commits 批量回滚审计 | 2026-04-24 | `status:in-progress` `help wanted` | **高** — 技术债务 | 28 天未关闭，需明确恢复优先级或放弃清单；153 个 commit 的逐个评估工作量巨大，建议维护者拆分里程碑 |
| [#5187](https://github.com/zeroclaw-labs/zeroclaw/pull/5187) ARM64 Docker 构建目标 | 2026-04-02 | `needs-author-action` | **高** — 边缘/IoT 部署 | 51 天悬停，跨平台编译方案成熟但作者未响应 rebase 请求；建议维护者接管或关闭 |
| [#6243](https://github.com/zeroclaw-labs/zeroclaw/issues/6243) 流式解码错误后 ZeroClaw 挂起 | 2026-04-30 | `status:blocked` `r:needs-repro` | **中** — 稳定性 | 23 天等待复现，GPU 50% 占用线索未跟进；建议添加诊断日志模板引导用户 |
| [#6036](https://github.com/zeroclaw-labs/zeroclaw/issues/6036) Termux 无限循环 | 2026-04-23 | `status:blocked` `needs-author-action` | **高** — 移动端 | 30 天等待复现，Android 开发者场景增长中；建议维护者提供 Termux 调试指南 |

---

*日报生成时间：2026-05-23 | 数据来源：ZeroClaw GitHub 仓库公开活动*

</details>

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*