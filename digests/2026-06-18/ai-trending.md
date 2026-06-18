# AI 开源趋势日报 2026-06-18

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-06-18 00:40 UTC

---

# AI 开源趋势日报（2026-06-18）

## 研究方向：长上下文推理、OCR/HMER、多模态推理、Post-Training 对齐、幻觉缓解

---

## 第一步：过滤结果

基于研究方向，从 101 个仓库中筛选出 **23 个相关项目**，排除以下无关项目：
- 通用工具：前端框架（Penpot）、聊天机器人（Rocket.Chat、Chatwoot）、游戏（Unciv）、项目管理（Plane）、商业应用（Meshery、Nautilus Trader）
- 纯基础设施：通用网络栈（Iroh）、Android 工具（Universal Android Debloater）、教育平台（freeCodeCamp）
- 纯商业/金融应用：TradingAgents、OpenBB、stock analysis

---

## 第二步：分类体系

| 项目 | 主要分类 | 次要分类 |
|:---|:---|:---|
| PaddleOCR | 📄 OCR 与文档智能 | 🏗️ 基础设施 |
| llama_index | 📄 OCR 与文档智能 | 🏗️ 基础设施 |
| RAGFlow | 📄 OCR 与文档智能 | 🧠 长上下文与推理 |
| UI-TARS-desktop | 🎭 多模态推理 | 🧠 长上下文与推理 |
| Agent-Reach | 🎭 多模态推理 | 🧠 长上下文与推理 |
| TimesFM | 🧠 长上下文与推理 | — |
| rlm (Recursive Language Models) | 🧠 长上下文与推理 | 🏗️ 基础设施 |
| vLLM | 🏗️ 基础设施 | 🧠 长上下文与推理 |
| Transformers | 🏗️ 基础设施 | 🔧 Post-Training 与对齐 |
| OpenCompass | 🏗️ 基础设施 | 👁️ 幻觉与可靠性 |
| test-time scaling survey | 🧠 长上下文与推理 | 🔧 Post-Training 与对齐 |
| stable-pretraining | 🔧 Post-Training 与对齐 | 🏗️ 基础设施 |
| awesome-llm-unlearning | 🔧 Post-Training 与对齐 | 👁️ 幻觉与可靠性 |
| AwesomeOPD (On-Policy Distillation) | 🔧 Post-Training 与对齐 | 🧠 长上下文与推理 |
| cognee | 🧠 长上下文与推理 | 👁️ 幻觉与可靠性 |
| mem0 | 🧠 长上下文与推理 | 👁️ 幻觉与可靠性 |
| claude-mem | 🧠 长上下文与推理 | 👁️ 幻觉与可靠性 |
| graphify | 🧠 长上下文与推理 | 🏗️ 基础设施 |
| codebase-memory-mcp | 🧠 长上下文与推理 | 🏗️ 基础设施 |
| ECC (agent harness optimization) | 🔧 Post-Training 与对齐 | 🏗️ 基础设施 |
| caveman (token efficiency) | 🧠 长上下文与推理 | 🏗️ 基础设施 |
| DATAGEN | 🔧 Post-Training 与对齐 | 🏗️ 基础设施 |
| LEANN (RAG storage efficient) | 🧠 长上下文与推理 | 🏗️ 基础设施 |

---

## 第三步：报告正文

---

### 1. 今日速览

**今日最值得关注的动向：**

1. **递归语言模型（RLM）推理库首次登榜** — [alexzhang13/rlm](https://github.com/alexzhang13/rlm) 作为通用即插即用推理框架，支持多种沙箱环境，直接对应长上下文推理中的递归/分层处理范式，是近期学术热点（如 CoT 压缩、推理时计算扩展）的工程落地。

2. **多模态 Agent 基础设施持续升温** — [bytedance/UI-TARS-desktop](https://github.com/bytedance/bytedance/UI-TARS-desktop)（+150 stars）和 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)（+1161 stars）显示视觉-语言-行动（VLA）一体化 Agent 栈成为社区焦点，与 GPT-4o、Claude 4 等多模态模型发布形成共振。

3. **测试时缩放（Test-Time Scaling）成为显学** — 专门综述仓库 [testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) 登榜，印证"推理时计算扩展"已从研究前沿进入社区知识整理阶段，与 o1/o3、DeepSeek-R1 等模型发布直接相关。

4. **OCR/文档智能与 RAG 深度融合** — [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 和 [RAGFlow](https://github.com/infiniflow/ragflow) 持续活跃，显示文档结构化解构向多模态 RAG 的演进趋势，对 HMER（手写数学表达式识别）等细粒度任务有直接支撑价值。

5. **记忆与幻觉缓解的工程化** — [cognee](https://github.com/topoteretes/cognee)、[mem0](https://github.com/mem0ai/mem0) 等"AI 记忆平台"集中出现，反映长上下文场景下的事实一致性（factuality）和幻觉问题正从算法研究转向系统架构层解决。

---

### 2. 各维度热门项目

#### 📄 OCR 与文档智能

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** | 82,820 | — | 百度开源的轻量级 OCR 工具包，支持 100+ 语言，将 PDF/图像转为结构化数据，直接服务于 LLM 的文档理解输入层；在 RAG 场景中与多模态模型对接价值显著 |
| **[RAGFlow](https://github.com/infiniflow/ragflow)** | 83,035 | — | 深度融合"深度文档理解"与 RAG 引擎，内置版面分析、表格解析、OCR 后处理，是解决 HMER 等复杂文档推理任务的端到端基础设施 |
| **[llama_index](https://github.com/run-llama/llama_index)** | 50,200 | — | 定位为"文档 Agent 与 OCR 平台"，其多模态索引和解析管道对长文档的分层理解、跨页推理有直接支撑 |

#### 🎭 多模态推理

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** | — | +150 | 字节开源的多模态 AI Agent 桌面栈，连接前沿视觉-语言模型与 Agent 基础设施，实现 GUI 感知、视觉推理与行动执行的闭环，是 VLM 落地关键工程 |
| **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** | 33,163 | +1161 | 赋予 AI Agent"看见整个互联网"的能力，跨平台多模态信息获取（Twitter/Reddit/YouTube/B 站/小红书），零 API 费用，对多模态训练数据收集和开放域 VQA 有独特价值 |

#### 🧠 长上下文与推理

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[rlm](https://github.com/alexzhang13/rlm)** | — | +43 | **今日首现**：递归语言模型（Recursive Language Models）通用推理库，支持多种沙箱环境，实现长序列的分层压缩与递归处理，直接对应长上下文建模的学术前沿 |
| **[TimesFM](https://github.com/google-research/timesfm)** | — | +606 | Google 时间序列基础模型，今日获高关注；其长序列预测能力（上下文窗口扩展）与长上下文推理技术栈共享位置编码、注意力优化等底层方法 |
| **[cognee](https://github.com/topoteretes/cognee)** | 17,885 | — | 开源 AI 记忆平台，基于知识图谱实现跨会话持久记忆，解决长上下文中的信息遗忘和上下文截断问题，支持自托管 |
| **[mem0](https://github.com/mem0ai/mem0)** | 58,803 | — | "AI Agent 的通用记忆层"，实现跨会话的上下文保持与检索，对长对话中的一致性推理和事实追溯至关重要 |
| **[claude-mem](https://github.com/thedotmack/claude-mem)** | 82,995 | — | 捕获 Agent 会话全轨迹，AI 压缩后注入未来会话，是长上下文工程中"上下文注入"与"记忆蒸馏"的具体实现 |
| **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | — | +371 | 高性能代码知识图谱 MCP 服务器，毫秒级索引、亚毫秒查询，99% token 削减，展示长上下文场景下的结构化记忆压缩工程 |
| **[caveman](https://github.com/JuliusBrussee/caveman)** | 74,088 | — | Claude Code 技能：通过"洞穴人式"极简表达削减 65% token，是长上下文推理中的显式上下文压缩/语义摘要策略 |
| **[LEANN](https://github.com/StarTrail-org/LEANN)** | 12,202 | — | MLSys 2026 工作：97% 存储节省的端侧 RAG，对长上下文部署的内存效率有突破性贡献 |

#### 🔧 Post-Training 与对齐

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[stable-pretraining](https://github.com/galilai-group/stable-pretraining)** | 264 | — | 可靠、极简、可扩展的基础模型预训练库，聚焦训练稳定性，是对齐阶段前"预训练-微调"连续性的工程保障 |
| **[awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning)** | 598 | — | LLM 机器遗忘资源库，直接服务于对齐中的安全对齐、有害知识消除，与幻觉缓解中的"知识边界"控制相关 |
| **[AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** | 651 | — | 在线策略蒸馏（On-Policy Distillation）综述，连接 SFT/RLHF 与高效推理，是对齐后模型压缩与推理加速的关键技术 |
| **[ECC](https://github.com/affaan-m/ECC)** | 217,296 | — | Agent  harness 性能优化系统，整合技能、本能、记忆、安全与研究优先开发，是多目标对齐（能力+安全+效率）的系统化框架 |
| **[DATAGEN](https://github.com/starpig1129/DATAGEN)** | 1,755 | — | AI 驱动多 Agent 研究助手，自动化假设生成、数据分析与报告撰写，其合成数据生成能力可服务于对齐数据构造与偏好数据扩充 |

#### 👁️ 幻觉与可靠性

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[cognee](https://github.com/topoteretes/cognee)** | 17,885 | — | 知识图谱驱动的持久记忆，通过显式图结构实现事实 grounding，减少生成式幻觉 |
| **[mem0](https://github.com/mem0ai/mem0)** | 58,803 | — | 跨会话记忆层确保事实一致性，避免模型因上下文截断而产生的"虚构"信息 |
| **[claude-mem](https://github.com/thedotmack/claude-mem)** | 82,995 | — | 全轨迹捕获与压缩注入，实现长期事实追溯，对抗时间维度上的幻觉累积 |
| **[graphify](https://github.com/safishamsi/graphify)** | 68,717 | — | 将代码/文档/图像/视频统一转为可查询知识图谱，多源信息交叉验证降低单一模态幻觉风险 |

#### 🏗️ 基础设施

| 项目 | Stars | 今日新增 | 一句话说明 |
|:---|:---|:---|:---|
| **[vLLM](https://github.com/vllm-project/vllm)** | 83,195 | — | 高吞吐、内存高效的 LLM 推理引擎，其 PagedAttention 技术是长上下文推理（大 KV Cache）的核心基础设施 |
| **[Transformers](https://github.com/huggingface/transformers)** | 161,676 | — | 模型定义框架，持续集成最新长上下文（如 Longformer, Mamba, Ring Attention）与多模态架构 |
| **[OpenCompass](https://github.com/open-compass/opencompass)** | 7,099 | — | 大模型评测平台，覆盖 100+ 数据集，是幻觉检测、长上下文评估、多模态基准测试的系统性工具 |
| **[test-time scaling survey](https://github.com/testtimescaling/testtimescaling.github.io)** | 105 | — | **今日首现**：测试时缩放综述仓库，系统整理"what/how/where/how well"，是推理增强研究的社区知识枢纽 |
| **[rlm](https://github.com/alexzhang13/rlm)** | — | +43 | 递归模型推理基础设施，提供多种沙箱支持，是长上下文推理算法的可复现平台 |

---

### 3. 研究趋势信号分析

**社区关注焦点正从"模型能力展示"转向"推理效率与可靠性系统"。** 今日热榜中，[rlm](https://github.com/alexzhang13/rlm) 的首次出现标志递归/分层推理架构进入工程化阶段，这与近期 Google DeepMind 的 Mixture of Depths、Meta 的 Multi-Token Prediction 等研究形成技术共振——核心矛盾从"能否处理长上下文"转向"如何高效压缩与选择性激活"。

**测试时缩放（Test-Time Scaling）成为显学。** [testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) 的登榜并非偶然，而是 o1/o3、DeepSeek-R1、Kimi k1.5 等"推理模型"发布后的社区知识整理需求爆发。这预示着 2026 年的研究重心：预训练规模竞赛趋缓，**推理时计算分配策略**（如 best-of-N, tree search, self-consistency）成为新战场。

**多模态 Agent 栈与 OCR/RAG 的融合深化。** [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) 和 [Agent-Reach](https://github.com/Panniantong/Agent-Reach) 的高热度，反映 VLM 从"看图说话"进入"视觉驱动行动"阶段。这对 HMER 研究有直接启示：数学公式识别不再是孤立 OCR 任务，而需嵌入"理解-推理-验证"的 Agent 闭环中，与 [RAGFlow](https://github.com/infiniflow/ragflow) 的"深度文档理解"能力结合。

**记忆基础设施涌现，指向幻觉缓解的系统化路径。** [cognee](https://github.com/topoteretes/cognee)、[mem0](https://github.com/mem0ai/mem0)、[claude-mem](https://github.com/thedotmack/claude-mem) 等记忆层项目集中出现，表明社区正从"提示工程对抗幻觉"转向"架构层事实 grounding"。这与学术界的 RAG 增强生成、知识图谱注入、检索增强推理（RAR）等方向高度一致。

**对齐研究的工具链细化。** [stable-pretraining](https://github.com/galilai-group/stable-pretraining) 和 [AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) 显示，post-training 阶段的前端（预训练稳定性）和后端（策略蒸馏压缩）均在工具化，中间的对齐阶段（RLHF/DPO）虽无新库登榜，但 [ECC](https://github.com/affaan-m/ECC) 的"多目标 harness 优化"暗示对齐目标正从单一"人类偏好"扩展至效率、安全、可解释性的多维度平衡。

---

### 4. 研究关注热点

- **🔥 [rlm](https://github.com/alexzhang13/rlm) — 递归语言模型推理库**
  - **相关性**：直接对应长上下文推理的核心难题——序列二次方复杂度与注意力稀释。RLM 通过递归分解实现线性或次线性扩展，是 Transformer 架构替代方案（如 RWKV, Mamba, xLSTM）之外的互补路径。建议关注其沙箱设计对 HMER 等需要层次化结构理解任务的适配性。

- **🔥 [test-time scaling survey](https://github.com/testtimescaling/testtimescaling.github.io) — 测试时缩放综述**
  - **相关性**：系统整理推理时计算扩展的"what/how/where/how well"，是连接对齐（RLHF/DPO 训练偏好）与推理（部署时策略）的关键桥梁。对幻觉缓解尤为重要：更多推理时计算 → 更高自我一致性 → 更低幻觉率。建议跟踪其覆盖的 verification-based decoding 方法。

- **🔥 [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) — 多模态 Agent 桌面栈**
  - **相关性**：字节开源的 VLA（Vision-Language-Action）基础设施，展示多模态模型从感知到行动的闭环。对 HMER 研究的启示：数学公式识别可嵌入"视觉感知 → 符号推理 → 验证执行"的 Agent 流程，而非孤立 OCR。建议关注其视觉编码器与推理引擎的接口设计。

- **🔥 [cognee](https://github.com/topoteretes/cognee) / [mem0](https://github.com/mem0ai/mem0) — AI 记忆平台**
  - **相关性**：长上下文场景下的幻觉缓解需要**显式记忆机制**而非隐式参数存储。知识图谱（cognee）和向量记忆（mem0）分别代表"结构化"与"语义"两种 grounding 路径，对需要精确事实追溯的数学推理（如 HMER 后的公式验证）有直接应用价值。

- **🔥 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) + [RAGFlow](https://github.com/infiniflow/ragflow) — OCR-文档智能-RAG 融合**
  - **相关性**：HMER 研究的工程瓶颈常在于"识别后如何利用"。RAGFlow 的深度文档理解管道将 OCR 输出（含公式）结构化接入 LLM 推理，是解决"识别-理解-推理"断层的端到端方案。建议关注其对复杂版面（多栏、嵌套表格、行间公式）的解析策略。

---

*报告完成。如需对特定项目展开技术深度分析，或追踪后续 star 增长与 release 动态，可进一步补充。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*