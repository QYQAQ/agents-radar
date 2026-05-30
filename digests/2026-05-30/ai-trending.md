# AI 开源趋势日报 2026-05-30

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-05-30 00:32 UTC

---

# AI 开源趋势日报（2026-05-30）

> 分析师视角：长上下文推理 · OCR/HMER · 多模态推理 · Post-Training 对齐 · 幻觉缓解

---

## 1. 今日速览

今日趋势呈现**"反幻觉"与"文档智能"双主线爆发**：`stop-slop`/`taste-skill` 等"去AI味"技能文件获数千星标，反映社区对**生成内容可信度校准**的迫切需求；`markitdown` 与 `liteparse` 推动**文档解析基础设施**向 Markdown-native 进化，直接服务 OCR→LLM 的 pipeline；`stable-worldmodel` 首次登榜，标志**世界模型可复现评测**成为新兴基础设施；`bytedance/deer-flow` 作为长时程 Agent 框架持续高活跃，其记忆-技能-沙箱架构与长上下文研究深度耦合。多模态领域未见新模型发布，但 `PaddleOCR` 在 RAG 主题下的高星表明**视觉文档理解仍是落地瓶颈**。

---

## 2. 各维度热门项目

### 📄 OCR 与文档智能（文本识别、版面分析、PDF 解析、HMER）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | ⭐0 / +1873 today | 微软官方文档转 Markdown 工具，将 Office/PDF 转为 LLM 可消费的结构化文本，是 OCR→LLM pipeline 的关键标准化环节 |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | ⭐0 / +701 today | Rust 编写的高速开源文档解析器，LlamaIndex 生态核心组件，直接支撑多模态 RAG 中的文档理解吞吐 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | ⭐78,963 / — [topic:rag] | 轻量 OCR 工具包，支持 100+ 语言，明确定位为"bridge the gap between images/PDFs and LLMs"，是 HMER 与版面分析的基础引擎 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | ⭐32,323 / — [topic:vector-db] | **"Vectorless, Reasoning-based RAG"** 的文档索引方案，跳过传统向量化直接基于推理检索，对版面复杂文档的语义理解有范式革新意义 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | ⭐49,763 / — [topic:rag] | 定位"document agent and OCR platform"，将 OCR 与 Agent 能力融合，是多模态文档智能的集成框架 |

---

### 🎭 多模态推理（视觉语言模型、视觉问答、跨模态对齐）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [huggingface/transformers](https://github.com/huggingface/transformers) | ⭐161,051 / — [topic:llm] | 多模态模型（VLM、语音-文本）的核心定义框架，今日虽未新增但持续承载 Qwen-VL、Gemma-3V 等模型的推理与微调 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | ⭐10,441 / — [topic:vector-db] | "Developer-friendly OSS embedded retrieval library for **multimodal AI**"，原生支持图像-文本联合检索，服务 VLM 的 memory layer |

> **注**：今日无纯 VLM 新模型或视觉推理框架登榜，多模态热度集中于**文档-语言跨模态**（OCR+RAG）而非端到端视觉理解。

---

### 🧠 长上下文与推理（上下文扩展、推理框架、思维链）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | ⭐69,960 / — [topic:llm] | 开源长时程 SuperAgent，通过 sandboxes/memories/subagents 处理分钟至小时级任务，其**消息网关与分层记忆机制**直接对应长上下文压缩与推理调度研究 |
| [galilai-group/stable-worldmodel](https://github.com/galilai-group/stable-worldmodel) | ⭐0 / +362 today | **首次登榜**：世界模型可复现研究平台，为长程推理提供标准化评测基础设施，与"test-time scaling"研究形成互补 |
| [testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) | ⭐99 / — [topic:llm-model] | 测试时扩展（Test-Time Scaling）综述仓库，系统梳理"what, how, where, and how well"，是长上下文推理优化的核心理论资源 |
| [thinkwee/AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL) | ⭐1,461 / — [topic:llm-model] | Agentic RL 综述，涵盖长程决策中的信用分配与推理增强，连接 LLM 推理与强化学习范式 |

---

### 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化、推理增强）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | ⭐71,700 / — [topic:llm] | 统一高效微调框架（ACL 2024），支持 100+ LLMs/VLMs 的 SFT/RLHF/DPO，是对齐研究的**标准实验工具** |
| [open-compass/opencompass](https://github.com/open-compass/opencompass) | ⭐7,047 / — [topic:llm-model] | LLM 评测平台，覆盖 100+ 数据集与多种对齐后模型，为 post-training 效果验证提供**可复现基准** |
| [galilai-group/stable-pretraining](https://github.com/galilai-group/stable-pretraining) | ⭐238 / — [topic:llm-model] | 稳定预训练库，与 stable-worldmodel 同属 GalilAI 研究线，关注**训练稳定性与可扩展性**，是对齐前基础能力保障 |
| [EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) | ⭐2,237 / — [topic:llm-model] | 上下文学习与提示工程资源库，涵盖 ICL 中的隐式偏好学习，与 SFT 数据构造策略直接相关 |

---

### 👁️ 幻觉与可靠性（事实 grounding、幻觉检测、可信度校准）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | ⭐0 / **+2062 today** | **今日增速最高**："给 AI 好品味"技能文件，阻止生成"无聊、通用的 slop"，本质是**生成质量与幻觉内容的风格层过滤** |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | ⭐0 / +617 today | 去除 AI 写作痕迹的技能文件，与 taste-skill 形成**反幻觉/反模式化生成**的社区运动，反映对模型过度自信输出的修正需求 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | ⭐81,524 / — [topic:rag] | RAG 引擎强调"superior context layer for LLMs"，通过检索增强**事实 grounding**，是工程化缓解幻觉的主流路径 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | ⭐79,615 / — [topic:rag] | 跨会话持久记忆，AI 压缩历史上下文并注入未来会话，解决**长程一致性幻觉**（如自我矛盾） |
| [safishamsi/graphify](https://github.com/safishamsi/graphify) | ⭐56,173 / — [topic:rag] | 将代码/文档/图像转为知识图谱，通过**结构化关系约束**减少生成中的事实编造 |

---

### 🏗️ 基础设施（训练框架、推理引擎、评测工具）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | ⭐81,382 / — [topic:llm] | 高吞吐 LLM 推理引擎，PagedAttention 优化长上下文 KV Cache，是长文本推理的**核心基础设施** |
| [ollama/ollama](https://github.com/ollama/ollama) | ⭐172,620 / — [topic:llm] | 本地模型部署工具，今日新增 Kimi-K2.5/GLM-5 支持，**长上下文模型（128K+）的终端可及性**关键推手 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | ⭐184,643 / — [topic:llm] | Agent 基础设施平台，其"agent harness"概念被 ECC/deer-flow 等继承，是**自主推理系统的工程底座** |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | ⭐7,459 / — [topic:llm-model] | Rust 模块化 LLM 应用框架，强调**可扩展架构**，适合构建对齐与推理的定制化 pipeline |

---

## 3. 研究趋势信号分析（282字）

今日热榜释放三个明确信号：**① 文档解析标准化加速**：`markitdown`（+1873）与 `liteparse`（+701）的爆发，表明社区正从"能解析"转向"统一格式、高效吞吐"，OCR→Markdown→LLM 成为事实标准，这对 HMER 研究的落地转化提出更高工程要求。**② "反 slop"运动兴起**：`taste-skill`（+2062）与 `stop-slop`（+617）并非技术框架，而是**偏好表达的社区化**——用户通过 skill file 直接干预模型行为，这与 RLHF/DPO 中"人类偏好建模"形成自下而上的呼应，暗示 post-training 对齐需更多关注**风格可信度**维度。**③ 世界模型与测试时扩展基础设施化**：`stable-worldmodel` 首登榜（+362），配合 test-time scaling 综述仓库，显示长上下文推理的研究重心正从"模型架构"转向"可复现评测+推理策略优化"。值得警惕的是，纯多模态（VLM）项目今日缺位，视觉-语言端到端研究可能处于发布真空期或转向文档-语言这一更务实的交叉地带。

---

## 4. 研究关注热点

- **`taste-skill` / `stop-slop` 的偏好学习机制**  
  理由：社区自发形成的"反 AI 味"技能文件，本质是**细粒度偏好标注**的分布式生产。可研究：如何将这些 skill file 转化为 DPO 的偏好对？其风格约束是否与事实性存在 trade-off？  
  → 关联：幻觉缓解 × post-training 对齐

- **`PageIndex` 的 vectorless RAG 范式**  
  理由：跳过向量化直接基于推理的文档检索，对**版面复杂、公式密集**的学术文档（HMER 场景）可能突破传统 embedding 的语义丢失瓶颈。  
  → 关联：OCR/HMER × 长上下文推理

- **`stable-worldmodel` + `stable-pretraining` 的 GalilAI 研究线**  
  理由：首次出现的"稳定"主题研究组合，针对世界模型训练中的**发散、不可复现**问题，其方法论可能迁移至长上下文模型的稳定 SFT。  
  → 关联：长上下文 × 基础设施

- **`deer-flow` 的分层记忆架构**  
  理由：字节开源的长时程 Agent 明确区分 sandboxes/memories/skills 三层，其**消息网关**设计可作为长上下文压缩与检索的实验平台。  
  → 关联：长上下文 × 推理框架

- **`claude-mem` 的跨会话一致性机制**  
  理由：AI 压缩历史上下文并选择性注入，直接对应**长程一致性幻觉**（如角色设定漂移、事实前后矛盾）的缓解策略，可抽象为通用评估基准。  
  → 关联：幻觉缓解 × 长上下文

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*