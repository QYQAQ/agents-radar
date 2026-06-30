# AI 开源趋势日报 2026-06-30

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-06-30 00:33 UTC

---

# AI 开源趋势日报（2026-06-30）

## 研究方向聚焦：长上下文推理、OCR/HMER、多模态推理、Post-training 对齐、幻觉缓解

---

## 一、今日速览

今日 Trending 榜单中，与核心研究方向直接相关的项目相对有限，但 **OCR/文档智能** 与 **长上下文/RAG 基础设施** 仍是社区关注重点。**PaddleOCR** 作为文档结构化入口持续高热，**RAGFlow** 与 **LlamaIndex** 在长上下文检索与文档 Agent 方向保持活跃。多模态与后训练对齐领域在今日热榜中未出现显著新开源模型或基准，但主题搜索中 **minimind** 的小模型训练范式、**OpenCompass** 评测平台以及 **test-time scaling** 综述仓库值得研究者关注。整体趋势显示：社区正将注意力从通用聊天机器人转向 **垂直场景的智能体 harness、长上下文记忆与文档理解基础设施**。

---

## 二、各维度热门项目

### 📄 OCR 与文档智能（文本识别、版面分析、PDF 解析、HMER）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 84,244 | 将任意 PDF/图像转为结构化数据的轻量 OCR 工具包，支持 100+ 语言，是文档理解与大模型结合的关键入口。 |
| [tesseract](https://github.com/tesseract-ocr/tesseract) | 75,010 | 经典开源 OCR 引擎，仍是 HMER 与文档识别基线对比的重要参考。 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 83,874 | 深度融合 RAG 与 Agent 能力的开源引擎，强调深度文档理解与可解释检索。 |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 50,510 | 领先的文档 Agent 与 OCR 平台，提供复杂文档解析与索引 pipeline。 |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | 33,512 | 面向无向量、推理驱动 RAG 的文档索引方案，对长文档结构化检索有研究价值。 |
| [graphify](https://github.com/safishamsi/graphify) | 74,377 | 将代码、文档、论文、图像、视频等多源数据构建为可查询知识图，适用于多模态文档理解研究。 |

### 🎭 多模态推理（视觉语言模型、视觉问答、跨模态对齐）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [Hugging Face Transformers](https://github.com/huggingface/transformers) | 162,026 | 文本、视觉、音频与多模态模型的统一框架，VLM 研究与部署的核心基础设施。 |
| [LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 72,783 | 支持 100+ LLM/VLM 统一高效微调，是多模态对齐与 SFT 的重要工具。 |
| [lancedb](https://github.com/lancedb/lancedb) | 10,761 | 面向多模态 AI 的开发者友好型检索库，支持图像-文本混合检索。 |
| [OpenHands](https://github.com/OpenHands/OpenHands) | 78,706 | AI 驱动开发平台，涉及代码-自然语言多模态推理与长程任务执行。 |

### 🧠 长上下文与推理（上下文扩展、推理框架、思维链）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) | 107 | Test-Time Scaling 综述仓库，系统梳理 LLM 推理阶段扩展方法，与长上下文推理密切相关。 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 75,453 | 长时程 SuperAgent harness，支持沙盒、记忆、子代理与消息网关，适合长程推理研究。 |
| [claude-mem](https://github.com/thedotmack/claude-mem) | 85,074 | 跨会话持久化上下文记忆，对长对话与长上下文一致性有直接影响。 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 59,713 | AI Agent 通用记忆层，支持跨会话长期记忆，是长上下文研究的关键组件。 |
| [cognee](https://github.com/topoteretes/cognee) | 25,662 | 自托管知识图引擎，为 Agent 提供持久长期记忆，适用于长上下文知识整合。 |
| [headroom](https://github.com/headroomlabs-ai/headroom) | 53,891 | 压缩工具输出、日志与 RAG 块后再输入 LLM，降低长上下文 token 消耗。 |

### 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化、推理增强）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [LlamaFactory](https://github.com/hiyouga/LlamaFactory) | 72,783 | 统一高效微调框架，覆盖 SFT/RLHF/DPO 等对齐方法，是后训练研究的主力工具。 |
| [OpenCompass](https://github.com/open-compass/opencompass) | 7,135 | 大模型评测平台，支持多种模型与 100+ 数据集，对齐效果评估的重要基准工具。 |
| [minimind](https://github.com/jingyaogong/minimind) | 52,341 | 2 小时从 0 训练 64M 参数小 LLM，适合快速验证 SFT/对齐算法与教学研究。 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 223,493 | Agent harness 性能优化系统，涵盖技能、本能、记忆、安全与研究优先开发，涉及后训练行为塑造。 |

### 👁️ 幻觉与可靠性（事实 grounding、幻觉检测、可信度校准）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [RAGFlow](https://github.com/infiniflow/ragflow) | 83,874 | 通过可解释引用与深度文档解析缓解生成幻觉，是 RAG 幻觉缓解的代表性系统。 |
| [graphify](https://github.com/safishamsi/graphify) | 74,377 | 构建结构化知识图以支撑事实 grounding，降低多源信息融合时的幻觉风险。 |
| [OpenCompass](https://github.com/open-compass/opencompass) | 7,135 | 提供多维度评测能力，可用于幻觉检测与可信度校准的基准研究。 |

### 🏗️ 基础设施（上述领域的训练框架、推理引擎、评测工具）

| 项目 | Stars | 一句话说明 |
|---|---|---|
| [Hugging Face Transformers](https://github.com/huggingface/transformers) | 162,026 | 多模态模型定义与训练的核心框架，贯穿 OCR/VLM/对齐全链路。 |
| [vLLM](https://github.com/vllm-project/vllm) | 84,840 | 高吞吐、低显存 LLM 推理引擎，长上下文模型 serving 的关键基础设施。 |
| [OpenCompass](https://github.com/open-compass/opencompass) | 7,135 | LLM/VLM 评测平台，是长上下文、OCR、多模态与对齐研究的标准化评估工具。 |
| [PyTorch](https://github.com/pytorch/pytorch) | 101,216 | 深度学习基础框架，支撑上述所有方向的研究与训练。 |
| [TensorFlow](https://github.com/tensorflow/tensorflow) | 196,106 | 另一主流 ML 框架，在产业界 OCR/多模态部署中仍有重要地位。 |
| [cupy](https://github.com/cupy/cupy) | +352 today | GPU 上的 NumPy/SciPy，加速数值计算与部分视觉/OCR 预处理。 |

---

## 三、研究趋势信号分析

今日热榜呈现出明显的 **"Agent 化"与"垂直化"** 趋势，但多数项目属于通用 Agent harness 或商业应用（如投资研究、交易、视频编辑），与核心研究方向的直接关联较弱。真正值得研究者关注的是底层基础设施的演进：**PaddleOCR、RAGFlow、LlamaIndex** 等文档理解工具持续获得高星，说明 OCR/文档智能仍是连接非结构化数据与大模型的关键瓶颈；**vLLM、Transformers、LlamaFactory** 构成后训练与多模态研究的工具链基座。

值得注意的是，**test-time scaling 综述仓库** 首次以较低星数进入主题搜索，反映出社区对推理阶段扩展方法的系统性关注，这与长上下文推理、思维链优化及幻觉缓解均有交集。此外，**minimind** 的小模型训练范式为快速验证对齐算法提供了低成本实验平台。然而，今日数据中 **未见专门面向 HMER、多模态幻觉检测、RLHF/DPO 新算法或长上下文基准的新开源项目登榜**，表明这些细分研究方向仍处于工具沉淀期，存在显著的研究空白与开源机会。

---

## 四、研究关注热点

- **PaddleOCR / RAGFlow / LlamaIndex 文档理解 trio**
  三者分别覆盖 OCR 识别、RAG 引擎与文档 Agent 编排，是研究 **OCR+LLM、版面分析、HMER 与长文档问答** 的核心参考栈。建议关注其在复杂表格、公式、多栏文档上的解析能力边界。

- **Test-Time Scaling 综述与实现**
  [testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io) 系统梳理了 LLM 推理扩展的 what/how/where/how well，对 **长上下文推理、CoT 优化、自我修正与幻觉缓解** 有直接启发，可作为新研究切入点的文献入口。

- **deer-flow / mem0 / cognee 长程记忆架构**
  长上下文不仅依赖模型长度扩展，更依赖 **外部记忆与知识图**。这些项目提供了可运行的长程 Agent 记忆方案，适合研究 **上下文压缩、记忆检索与跨会话一致性**。

- **LlamaFactory + OpenCompass 对齐评测闭环**
  后训练研究需要高效的微调工具与可靠的评测基准。LlamaFactory 支持多种对齐算法，OpenCompass 覆盖多维度评测，二者组合可用于 **DPO/RLHF 在变长上下文与多模态任务上的效果验证**。

- **headroom / PageIndex 长上下文成本优化**
  长上下文推理的 token 成本是实际部署瓶颈。headroom 的上下文压缩与 PageIndex 的无向量推理索引，为研究 **高效长上下文检索与生成** 提供了工程化思路。

---

*报告基于 2026-06-30 GitHub Trending 与主题搜索数据生成，聚焦长上下文推理、OCR/HMER、多模态推理、post-training 对齐与幻觉缓解方向。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*