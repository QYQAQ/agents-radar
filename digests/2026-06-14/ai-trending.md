# AI 开源趋势日报 2026-06-14

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-06-14 00:35 UTC

---

# AI 开源趋势日报（2026-06-14）

**研究方向聚焦：长上下文推理、OCR/HMER、多模态推理、Post-Training 对齐、幻觉缓解**

---

## 1. 今日速览

今日热榜中，**NVIDIA SkillSpector**（+804 stars）作为 AI agent 安全扫描工具首次登榜，其技能漏洞检测机制与幻觉缓解中的可靠性校准存在方法论关联。**PaddleOCR**（82K stars）持续领跑 OCR/文档智能赛道，明确将"图像/PDF 与 LLM 的桥梁"作为定位，体现文档理解向多模态 RAG 的演进。**LMCache**（+238 today）以"最快 KV Cache 层"为卖点，直接服务于长上下文推理的内存瓶颈问题。值得关注的是，**caveman**（+72K stars）以"Claude Code skill 削减 65% token"的极端压缩策略，反映了长上下文场景下 token 效率优化的迫切需求。整体趋势显示：基础设施层（KV Cache、向量数据库）与文档智能层（OCR、知识图谱）正加速融合，为下一代多模态长上下文系统铺路。

---

## 2. 各维度热门项目

### 📄 OCR 与文档智能

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [PaddleOCR/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 82,109 | 将任意 PDF/图像转为结构化数据的轻量 OCR 工具包，支持 100+ 语言，直接桥接图像/PDF 与 LLM，是文档理解多模态流水线的核心组件 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 50,111 | 明确自称为"领先的文档 agent 与 OCR 平台"，其文档解析与索引能力是长上下文 RAG 系统的关键基础设施 |
| [safishamsi/graphify](https://github.com/safishamsi/graphify) | 66,727 | 将代码、SQL、文档、论文、图像、视频统一转为可查询知识图谱，多模态文档的结构化表示与 HMER 中的符号关系建模高度相关 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 132,384 | 大规模网页搜索与抓取 API，为文档智能提供原始多模态数据入口，其结构化输出是下游 OCR/解析的前置依赖 |

### 🎭 多模态推理

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [huggingface/transformers](https://github.com/huggingface/transformers) | 161,567 | 文本/视觉/音频/多模态模型的统一框架，VLM（如 LLaVA、Qwen-VL）的训练推理基础设施，多模态对齐的核心依赖 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 10,595 | "面向多模态 AI 的开发者友好嵌入式检索库"，支持图像-文本联合检索，是 VLM 外部记忆的关键组件 |
| [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | 27,171 | 基于 AI 的网页抓取器，将非结构化网页内容转为结构化数据，涉及视觉理解与文本推理的跨模态协同 |

### 🧠 长上下文与推理

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [LMCache/LMCache](https://github.com/LMCache/LMCache) | +238 today | "最快的 KV Cache 层"，直接解决长上下文推理的内存瓶颈与首 token 延迟，是 100K+ 上下文窗口落地的工程关键 |
| [cognee/cognee](https://github.com/topoteretes/cognee) | 17,815 | 开源 AI 记忆平台，为 agent 提供跨会话的持久长期记忆与自托管知识图谱引擎，长上下文的外部化扩展方案 |
| [claude-mem/claude-mem](https://github.com/thedotmack/claude-mem) | 82,143 | 跨会话持久上下文捕获与压缩注入，用 AI 压缩历史会话并选择性召回，是长上下文"无限记忆"的工程实现 |
| [caveman](https://github.com/JuliusBrussee/caveman) | 72,175 | Claude Code skill 以"洞穴人"极简语法削减 65% token，极端的长上下文 token 效率优化策略，对上下文窗口受限场景有启发意义 |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 27,922 | 高级 RAG 技术集，含长上下文分块、重排序、查询重写等策略，是长上下文推理系统设计的实践参考 |

### 🔧 Post-Training 与对齐

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [open-compass/opencompass](https://github.com/open-compass/opencompass) | 7,082 | LLM 评测平台，覆盖 100+ 数据集的对齐效果评估，是 RLHF/DPO/SFT 后模型验证的基础设施 |
| [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) | 624 | On-Policy Distillation 资源列表，探索在线策略蒸馏作为对齐替代路径，与 RLHF 的样本效率优化直接相关 |
| [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) | 598 | LLM 机器遗忘资源库，涉及安全对齐中的知识擦除与有害输出抑制，是对齐技术的反向操作 |
| [testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) | 105 | Test-Time Scaling 综述仓库，探索推理阶段计算扩展作为对齐替代方案，与 DeepSeek-R1 等推理增强模型的 post-training 策略相关 |

### 👁️ 幻觉与可靠性

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +804 today | AI agent 技能安全扫描器，检测漏洞、恶意模式与安全风险，首次将"技能级"可靠性验证引入 agent 生态，与幻觉缓解中的事实 grounding 机制互补 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 58,492 | AI agent 的通用记忆层，通过记忆一致性维护减少上下文冲突导致的幻觉，是可靠性增强的架构层方案 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 82,657 | "融合前沿 RAG 与 Agent 能力"，其可解释检索链路是幻觉缓解的事实 grounding 基础 |

### 🏗️ 基础设施

| 项目 | Stars | 一句话说明 |
|:---|:---|:---|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 82,776 | 高吞吐、内存高效的 LLM 推理引擎，PagedAttention 技术支撑长上下文批处理，是多模态/长模型部署的核心 |
| [ollama/ollama](https://github.com/ollama/ollama) | 174,072 | 本地运行 Kimi-K2.6、GLM-5.1、DeepSeek 等模型的工具，支持长上下文与多模态模型的边缘化部署 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 44,762 | 云原生向量数据库，支持十亿级向量 ANN 搜索，多模态/长上下文 RAG 的存储基础设施 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 32,172 | 高性能大规模向量搜索引擎，下一代 AI 的向量存储层，支持多模态嵌入的混合检索 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 16,323 | 对象与向量统一存储，支持向量搜索与结构化过滤的组合，多模态数据的语义索引基础设施 |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | 7,610 | Rust 模块化 LLM 应用框架，类型安全的 agent 编排，对齐后模型的可靠部署框架 |

---

## 3. 研究趋势信号分析

今日数据呈现三个明确的研究信号。**第一，长上下文工程化进入"内存优化"深水区**：LMCache 的 KV Cache 加速与 caveman 的极端 token 压缩并存，说明社区在"扩展窗口长度"与"提升窗口效率"两条路径同步推进，这与 Kimi-K2.6 等 200K+ 上下文模型的发布形成呼应。**第二，OCR 与文档智能正从"识别工具"向"LLM 桥梁"转型**：PaddleOCR 的自我定位升级、llama_index 的"OCR 平台"宣称，以及 graphify 的多模态知识图谱化，显示文档理解正在融入端到端多模态推理流水线，HMER 领域的符号-结构联合建模可借鉴此趋势。**第三，对齐与可靠性评估出现"技能级"粒度**：NVIDIA SkillSpector 首次将安全扫描下沉到 agent 技能层，OpenCompass 持续扩展评测覆盖，表明 post-training 对齐的效果验证正从模型级向应用级细化，这对幻觉缓解的细粒度评估方法论有启发。值得注意的是，Test-Time Scaling 综述（105 stars）虽星数不高，但代表了推理阶段计算扩展作为对齐替代路径的新兴研究方向，值得追踪。

---

## 4. 研究关注热点

- **LMCache（长上下文推理基础设施）**  
  直接针对 KV Cache 的内存与速度瓶颈，是 100K+ 上下文模型落地的工程瓶颈突破点。与长上下文推理研究中的上下文压缩、滑动窗口注意力等技术形成互补，建议关注其与 vLLM 的集成方案。

- **PaddleOCR + graphify（文档智能→多模态知识图谱）**  
  PaddleOCR 的"图像/PDF-LLM 桥梁"定位与 graphify 的多模态统一知识图谱，共同指向 OCR/HMER 的下游应用范式转变：从孤立识别任务转向支持多步推理的结构化知识表示。HMER 领域的符号关系抽取可借鉴此流水线设计。

- **NVIDIA SkillSpector（幻觉缓解的可靠性层）**  
  虽属安全扫描工具，但其"技能级漏洞检测"方法论与幻觉检测中的细粒度事实验证（fine-grained fact verification）高度相关。建议探索将其模式识别机制迁移至模型输出的可信度校准。

- **Test-Time Scaling 综述（Post-Training 对齐的替代路径）**  
  105 stars 的新登榜项目，系统梳理推理阶段计算扩展（如推理时搜索、验证器集成）作为 RLHF/DPO 的替代或补充。与 DeepSeek-R1、OpenAI o1 系列的技术路线一致，对偏好优化研究的方法论拓展有参考价值。

- **cognee / claude-mem（长上下文的外部记忆架构）**  
  两者分别代表"自托管知识图谱记忆"与"AI 压缩会话记忆"两种长期记忆方案，是长上下文"无限扩展"的架构创新。与当前研究中探讨的 Memory-Augmented LLM、Hierarchical Attention 等方向直接相关，可作为长上下文系统设计的工程参考。

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*