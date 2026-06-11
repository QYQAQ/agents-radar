# AI 开源趋势日报 2026-06-11

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-06-11 00:37 UTC

---

# AI 开源趋势日报（2026-06-11）

## 研究方向聚焦：长上下文推理、OCR/HMER、多模态推理、Post-Training 对齐、幻觉缓解

---

## 一、今日速览

今日 GitHub 热榜显示 **Agent Skills 框架** 成为核心爆发点，Google、Addy Osmani 等相继开源 agent 技能库，暗示长上下文任务分解与工具调用正从研究走向工程标准化。**OCR/文档智能** 领域，PaddleOCR 持续领跑，LlamaIndex 明确将 OCR 与文档代理作为核心定位。值得关注的是 **LEANN**（97% 存储节省的端侧 RAG）和 **PageIndex**（无向量推理式 RAG）代表文档检索正经历范式变革。Post-training 领域虽无全新框架登榜，但 **LlamaFactory** 与 **OpenCompass** 等基础设施持续高活跃，而 **process reward models** 和 **test-time scaling** 专题仓库的出现标志着推理时对齐研究正在细化。

---

## 二、各维度热门项目

### 📄 OCR 与文档智能

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** | 81,755 | 将任意 PDF/图像转为结构化数据的轻量 OCR 工具包，支持 100+ 语言。今日 RAG 主题高活跃，其"桥接图像/PDF 与 LLM"的定位直接服务于多模态文档理解 pipeline |
| **[LlamaIndex](https://github.com/run-llama/llama_index)** | 50,067 | 自称为"领先的文档代理与 OCR 平台"，从通用 RAG 框架向文档智能深度演进，值得关注其 OCR 模块的技术路线 |
| **[PageIndex](https://github.com/VectifyAI/PageIndex)** | 32,854 | **无向量、基于推理的文档索引**，挑战传统向量 RAG 范式，对长文档 HMER/版面分析后的语义组织有启发意义 |
| **[RAGFlow](https://github.com/infiniflow/ragflow)** | 82,408 | 深度融合 RAG 与 Agent 能力，强调"为 LLM 构建优质上下文层"，其文档解析与深度理解模块涉及 OCR 与版面分析 |

---

### 🎭 多模态推理

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[transformers](https://github.com/huggingface/transformers)** | 161,484 | 支持文本、视觉、音频及多模态模型的统一框架，VLM 训练推理的基础设施核心 |
| **[lancedb/lancedb](https://github.com/lancedb/lancedb)** | 10,570 | 面向多模态 AI 的嵌入式检索库，"Search More; Manage Less" 暗示多模态向量管理的简化趋势 |
| **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | 72,055 | 统一高效微调 100+ LLMs & VLMs（ACL 2024），VLM post-training 的关键基础设施 |
| **[opencompass](https://github.com/open-compass/opencompass)** | 7,077 | 支持多模态模型（含 LLaVa、Qwen-VL 等）的评测平台，VLM 能力评估的必要工具 |

---

### 🧠 长上下文与推理

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 70,903 | 开源长程 SuperAgent 框架，支持分钟到小时的复杂任务，集成 memory、skill、subagent 等模块，**长上下文任务分解与推理的系统性工程方案** |
| **[LEANN](https://github.com/StarTrail-org/LEANN)** | 11,903 | 端侧 RAG 实现 97% 存储节省，长上下文场景下的高效检索与推理，个人设备部署的隐私优势 |
| **[vllm-project/vllm](https://github.com/vllm-project/vllm)** | 82,458 | 高吞吐、内存高效的 LLM 推理引擎，长上下文推理的关键基础设施 |
| **[testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io)** | 105 | **测试时扩展（Test-Time Scaling）综述仓库**，长上下文推理的核心技术方向，系统梳理 what/how/where/how well |
| **[Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)** | 167 | 过程奖励模型资源汇总，长程推理的逐步监督与信用分配机制 |

---

### 🔧 Post-Training 与对齐

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | 72,055 | 100+ 模型统一微调，涵盖 SFT、RLHF、DPO 等全系列对齐方法，post-training 的核心工作台 |
| **[Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)** | 167 | 过程奖励模型（PRM）全面收集，**超越结果监督的细粒度对齐**，OpenAI o1 类推理的核心技术 |
| **[stable-pretraining](https://github.com/galilai-group/stable-pretraining)** | 254 | 可靠、最小化、可扩展的基础模型预训练库，强调训练稳定性，对齐前序环节的关键 |
| **[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** | 609 | 在线策略蒸馏（On-Policy Distillation）资源，知识迁移与模型压缩中的对齐保持 |
| **[awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning)** | 596 | LLM 机器遗忘资源库，对齐的逆向操作——安全移除有害知识，与 RLHF 安全目标互补 |

---

### 👁️ 幻觉与可靠性

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[last30days-skill](https://github.com/mvanhorn/last30days-skill)** | 2,535 (+2,535 today) | **今日最热！** 跨 Reddit/X/YouTube/HN/Polymarket/网页的多源研究并综合 grounded summary，**主动事实核查与多源验证**的 agent 技能，直接对抗幻觉 |
| **[PageIndex](https://github.com/VectifyAI/PageIndex)** | 32,854 | 无向量推理式 RAG，减少检索噪声导致的幻觉，依赖结构化推理而非相似度匹配 |
| **[mem0ai/mem0](https://github.com/mem0ai/mem0)** | 58,284 | AI Agent 的通用记忆层，跨会话持久化，减少因上下文截断或记忆冲突产生的幻觉 |
| **[cognee](https://github.com/topoteretes/cognee)** | 17,766 | 自托管知识图谱引擎为 agent 提供长期记忆，图结构的事实关联有助于提升回答可信度 |

---

### 🏗️ 基础设施

| 项目 | Stars | 说明 |
|:---|:---|:---|
| **[transformers](https://github.com/huggingface/transformers)** | 161,484 | 多模态模型定义与训练的事实标准框架 |
| **[vllm-project/vllm](https://github.com/vllm-project/vllm)** | 82,458 | 生产级 LLM 推理服务，长上下文场景的性能优化关键 |
| **[OpenCompass](https://github.com/open-compass/opencompass)** | 7,077 | 100+ 数据集的多模型评测，幻觉检测与能力边界量化的基础设施 |
| **[tiny-llm](https://github.com/skyzh/tiny-llm)** | 4,267 | Apple Silicon 上的 LLM 推理服务课程，系统工程师视角的推理优化教育项目 |
| **[picollm](https://github.com/Picovoice/picollm)** | 311 | X-Bit 量化驱动的端侧推理，低资源场景下的模型部署 |

---

## 三、研究趋势信号分析

今日数据揭示三个关键趋势：**Agent Skills 的标准化**、**文档 RAG 的范式转移**、**推理时对齐的精细化**。

首先，Google Skills、agent-skills、pm-skills 等集中出现，表明长上下文复杂任务的解决正从"模型能力"转向"工程编排"——这与 deer-flow 的长程 SuperAgent 架构形成呼应，暗示研究社区需关注任务分解、工具调用与记忆管理的系统性整合。

其次，**PageIndex** 的"无向量推理式 RAG"与 **LEANN** 的"97% 存储节省"共同指向文档检索的去向量化趋势，对传统基于 embedding 的 RAG 构成挑战，OCR/版面分析后的结构化表示（如知识图谱、符号索引）可能重获重视。

第三，**test-time scaling** 和 **process reward models** 两个低星但高专业度的仓库出现，表明社区正将 post-training 对齐的注意力从"训练时"延伸至"推理时"——OpenAI o1 的技术路线正在开源社区扩散。这与 LlamaFactory 等训练基础设施的持续活跃形成互补，预示"训练+推理"双阶段优化的研究范式。

---

## 四、研究关注热点

- **[last30days-skill](https://github.com/mvanhorn/last30days-skill)** — **多源事实 grounding 的主动幻觉缓解机制**。跨平台信息聚合与综合验证的技能设计，可直接借鉴用于长上下文推理中的事实核查模块，与 RAG 系统的可信度校准高度相关。

- **[PageIndex](https://github.com/VectifyAI/PageIndex)** — **无向量推理式文档索引**。对 HMER/版面分析后的文档表示有颠覆性启发：若符号化结构（如阅读顺序、层级关系）可替代密集向量，OCR 后处理的价值将被重估。

- **[deer-flow](https://github.com/bytedance/deer-flow)** — **长程任务的层次化推理架构**。分钟到小时级任务的时间尺度、memory/skill/subagent 的模块化设计，为长上下文推理的实验平台提供了可直接扩展的工程基座。

- **[Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)** — **逐步监督的对齐新范式**。过程奖励模型是 o1 类推理的核心，资源汇总有助于快速进入该领域，与 DPO/RLHF 形成技术互补。

- **[LEANN](https://github.com/StarTrail-org/LEANN)** — **端侧长上下文 RAG 的极端效率优化**。97% 存储节省意味着长文档处理可在资源受限场景部署，对移动端/边缘端的多模态文档理解有直接影响。

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*