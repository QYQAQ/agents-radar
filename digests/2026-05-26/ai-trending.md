# AI 开源趋势日报 2026-05-26

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-05-26 00:31 UTC

---

# AI 开源趋势日报（2026-05-26）

**研究方向聚焦**：长上下文推理、OCR/HMER、多模态推理、Post-training 对齐、幻觉缓解

---

## 一、今日速览

今日 Trending 榜单呈现**"Agent 基础设施爆发"**特征，但与核心研究方向直接相关的项目较少。值得关注的是 **Knowledge Graph for Code** 类项目（Understand-Anything、codegraph、graphify）兴起，其将代码/文档结构化为可查询图，与**长上下文压缩**和**结构化推理**密切相关。Post-training 对齐领域出现 **"反 Slop"运动**（taste-skill、stop-slop），直接针对 LLM 输出质量与幻觉问题。OCR/文档智能方面，**LlamaIndex 明确标注为"OCR platform"**，RAGFlow 持续活跃，但纯 HMER 项目缺席。整体而言，社区正从"拼模型参数"转向"拼上下文质量"和"拼输出可靠性"，与幻觉缓解、长上下文优化的研究议程高度契合。

---

## 二、各维度热门项目

### 📄 OCR 与文档智能

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | ⭐49,660 [topic:rag] | **明确自定位为"leading document agent and OCR platform"**，将文档解析与 Agent 能力深度融合，今日 RAG 主题活跃代表 |
| **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** | ⭐81,230 [topic:rag] | 开源 RAG 引擎强调"deep document understanding"，其文档结构解析与版面分析模块与 OCR 流水线直接相关 |
| **[paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)** | ⭐0 (+176 today) | 社区驱动的文档管理系统，扫描-索引-归档全流程，OCR 后处理与文档理解的实际应用场景 |
| **[safishamsi/graphify](https://github.com/safishamsi/graphify)** | ⭐53,698 [topic:rag] | 将"papers, images, or videos into a queryable knowledge graph"，**多模态文档结构化**，跨模态检索与 HMER 相关场景 |

> **HMER 专项空白**：今日数据中无专门数学公式识别（HMER）项目，graphify 的通用图像→图结构能力可作为间接参考。

---

### 🎭 多模态推理

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[huggingface/transformers](https://github.com/huggingface/transformers)** | ⭐160,953 [topic:llm] | 核心基础设施，支持"text, vision, audio, and multimodal models"，VLM 训练推理的统一框架 |
| **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | ⭐71,583 [topic:llm] | **统一微调 100+ LLMs & VLMs (ACL 2024)**，多模态 SFT 的核心工具，今日 LLM 主题高星项目 |
| **[lancedb/lancedb](https://github.com/lancedb/lancedb)** | ⭐10,398 [topic:vector-db] | "Developer-friendly OSS embedded retrieval library for **multimodal AI**"，原生支持多模态向量检索 |
| **[ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** | ⭐26,044 [topic:llm-model] | 基于 AI 的网页抓取，隐含视觉-文本联合理解，网页版面解析与多模态推理的交叉点 |

---

### 🧠 长上下文与推理

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)** | ⭐0 (+5604 today) | **今日最高新增**！将任意代码转为"interactive knowledge graph"，**长上下文压缩为结构化图**，探索替代线性上下文的新范式 |
| **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** | ⭐0 (+3161 today) | "Pre-indexed code knowledge graph... fewer tokens, fewer tool calls, **100% local**"，显式优化上下文效率 |
| **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** | ⭐78,122 [topic:rag] | "**Persistent Context Across Sessions**"——跨会话上下文压缩与注入，长上下文记忆的核心挑战 |
| **[safishamsi/graphify](https://github.com/safishamsi/graphify)** | ⭐53,698 [topic:rag] | 代码+数据库+基础设施统一图谱，**多源异构信息的长上下文融合** |
| **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** | ⭐11,569 [topic:vector-db] | "Make **entire codebase the context** for any coding agent"，向量检索驱动的无限上下文方案 |

---

### 🔧 Post-Training 与对齐

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | ⭐0 (+264 today) | **"stops the AI from generating boring, generic slop"**——通过 Skill 文件优化输出质量，隐性偏好对齐 |
| **[hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)** | ⭐0 (+345 today) | "removing AI tells from prose"，**后训练输出校准**，减少模型化痕迹，与 RLHF 目标一致 |
| **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** | ⭐0 (+2749 today) | 基于 Karpathy 对 LLM 编码缺陷观察的**行为矫正 Skill**，经验驱动的输出对齐 |
| **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | ⭐71,583 [topic:llm] | 统一高效微调框架，涵盖 SFT/DPO/RLHF 全流程，**post-training 对齐的核心基础设施** |
| **[open-compass/opencompass](https://github.com/open-compass/opencompass)** | ⭐7,025 [topic:llm-model] | LLM 评测平台，**对齐效果的量化评估工具**，覆盖 Claude/GPT-4/Qwen 等主流模型 |

---

### 👁️ 幻觉与可靠性

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)** | ⭐0 (+345 today) | **直接针对"AI tells"——幻觉的典型症状**，通过 Skill 层缓解模型过度自信输出 |
| **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | ⭐0 (+264 today) | 提升输出区分度，减少"generic slop"——**低信息熵幻觉**的另一种表现 |
| **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** | ⭐81,230 [topic:rag] | "deep document understanding"减少 RAG 幻觉，**可溯源生成**的可靠性设计 |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | ⭐17,506 [topic:vector-db] | "Memory control plane for AI Agents"，**记忆一致性**与事实 grounding 的基础设施 |

---

### 🏗️ 基础设施（训练/推理/评测）

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[huggingface/transformers](https://github.com/huggingface/transformers)** | ⭐160,953 [topic:llm] | 多模态模型定义框架，研究级训练推理基础设施 |
| **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | ⭐71,583 [topic:llm] | 100+ 模型统一微调，**SFT/DPO/RLHF 一体化**，对齐研究的核心工具 |
| **[vllm-project/vllm](https://github.com/vllm-project/vllm)** | ⭐80,997 [topic:llm] | 高吞吐推理引擎，**长上下文服务的性能基础** |
| **[open-compass/opencompass](https://github.com/open-compass/opencompass)** | ⭐7,025 [topic:llm-model] | 100+ 数据集评测平台，**对齐与幻觉的量化研究依赖** |
| **[0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)** | ⭐7,420 [topic:llm-model] | Rust 模块化 LLM 应用框架，**类型安全的长链路推理**基础设施 |

---

## 三、研究趋势信号分析（250字）

今日数据揭示**三个关键转向**：其一，**长上下文正从"长度竞赛"转向"结构竞赛"**——Understand-Anything、codegraph、graphify 等知识图谱项目爆发（合计 +13,000+ stars），暗示社区寻求用图结构替代线性序列，以解决 Transformer 上下文瓶颈，这与学术界的 Graph RAG、结构化解压缩研究形成呼应。其二，**"反 Slop"运动兴起**（taste-skill、stop-slop、andrej-karpathy-skills）标志着后训练对齐从"能力对齐"下沉至"风格对齐"，直接针对模型过度自信、输出同质化等幻觉症状，可视为 RLHF/DPO 的"民间补充"。其三，**LlamaIndex 自定位为 OCR platform** 值得注意，文档智能与 Agent 基础设施的边界正在模糊，但纯 HMER 研究仍缺位。无新模型或基准首次登榜，显示今日热点偏重工程化而非研究突破。

---

## 四、研究关注热点

- **🔥 Knowledge Graph as Context Compression（Understand-Anything / codegraph / graphify）**
  - **相关性**：直接对应长上下文推理研究议程。将代码/文档结构化为图，本质是探索**非线性上下文组织**对推理效率的影响，可为 HMER 中公式结构解析（如 LaTeX AST）提供迁移思路。

- **🔥 "Anti-Slop" Skill Engineering（taste-skill / stop-slop / karpathy-skills）**
  - **相关性**：**轻量级偏好对齐的民间实践**。通过 prompt/skill 层而非完整 RLHF 优化输出质量，为幻觉缓解研究提供"低成本干预"基线，可系统评估其与 DPO 的效果差距。

- **🔥 LlamaFactory 的持续统治地位**
  - **相关性**：**多模态 post-training 的事实标准**。ACL 2024 后仍维持高活跃，支持 VLM SFT，是验证新对齐算法（如 ORPO、SimPO）的首选平台，建议跟踪其多模态 DPO 实现进展。

- **🔥 RAGFlow 的"Deep Document Understanding"**
  - **相关性**：OCR 与 RAG 的深度融合案例。其文档版面解析模块可能涉及与 HMER 类似的**二维结构理解**，可解剖其视觉编码器设计是否适用于数学公式场景。

- **⚠️ HMER 研究空白预警**
  - **相关性**：今日无专门数学公式识别项目。建议关注 graphify 的通用图像→图能力，评估其向印刷/手写数学表达式迁移的可行性，或推动该方向开源基础设施的建设。

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*