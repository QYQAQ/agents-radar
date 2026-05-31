# AI 开源趋势日报 2026-05-31

> 数据来源: GitHub Trending + GitHub Search API | 生成时间: 2026-05-31 00:33 UTC

---

# AI 开源趋势日报（2026-05-31）

> **研究方向聚焦**：长上下文推理、OCR/HMER、多模态推理、Post-Training 对齐、幻觉缓解

---

## 1. 今日速览

今日 Trending 榜单中，**文档解析与长上下文基础设施**成为核心亮点：`run-llama/liteparse` 以 925 今日新增 stars 登顶，Rust 重写的高性能文档解析器直接服务于 RAG 与 OCR 下游任务；`microsoft/markitdown` 持续高热度（+2470），推动 Office 文档向结构化 Markdown 的转换标准化。多模态与语音生成领域，`OpenBMB/VoxCPM` 提出 Tokenizer-Free TTS 架构，为端到端语音-文本统一建模提供新范式。Post-training 与 Agent 对齐方面，`anthropics/claude-code` 及其 Skills 生态（+592/+454）标志着**Agent 能力通过可组合技能（Skills）进行模块化对齐**的工程化趋势。值得注意的是，**世界模型预训练基础设施**（`galilai-group/stable-worldmodel`、`stable-pretraining`）首次进入热榜，暗示长上下文推理与物理世界建模的交叉正在加速。

---

## 2. 各维度热门项目

### 📄 OCR 与文档智能（文本识别、版面分析、PDF 解析、HMER）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[run-llama/liteparse](https://github.com/run-llama/liteparse)** | ⭐925 today | Rust 高性能开源文档解析器，针对 LLM/RAG 场景优化，直接提升 OCR 后结构化文本的提取速度与准确性，是长文档理解链路的瓶颈突破点 |
| **[microsoft/markitdown](https://github.com/microsoft/markitdown)** | ⭐0 (+2470 today) | 微软官方文件转 Markdown 工具，统一 Office/PDF 等格式的结构化输出，为下游 HMER 和文档理解模型提供标准化输入 |
| **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** | ⭐79,079 [topic:rag] | 工业级轻量 OCR 工具包，支持 100+ 语言，直接衔接 LLM 的文档结构化流水线，在 RAG 场景中作为多模态文档理解的前置模块 |
| **[run-llama/llama_index](https://github.com/run-llama/llama_index)** | ⭐49,782 [topic:rag] | 明确标注为"document agent and OCR platform"，其 OCR 与文档索引能力的演进直接影响长文档 RAG 的检索精度 |

### 🎭 多模态推理（视觉语言模型、视觉问答、跨模态对齐）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)** | ⭐0 (+779 today) | VoxCPM2：Tokenizer-Free 多语言 TTS，消除文本-语音分词壁垒，为端到端语音-语言多模态统一建模提供新架构，与 VLM 的音频扩展直接相关 |
| **[OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS)** | ⭐0 (+62 today) | 高保真长语音合成与多说话人对话系统，支持实时流式 TTS，其"长形式语音稳定性"技术可迁移至长视频-音频联合推理场景 |
| **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** | ⭐71,724 [topic:llm] | 统一高效微调 100+ LLMs & VLMs（ACL 2024），是多模态模型 post-training 的核心基础设施，支持视觉-语言联合 SFT/DPO |

### 🧠 长上下文与推理（上下文扩展、推理框架、思维链）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[galilai-group/stable-worldmodel](https://github.com/galilai-group/stable-worldmodel)** | ⭐0 (+318 today) | 可复现世界模型研究平台，长上下文物理推理的基础环境，其"稳定性"设计直接关联长序列记忆与一致性推理 |
| **[galilai-group/stable-pretraining](https://github.com/galilai-group/stable-pretraining)** | ⭐238 [topic:llm-model] | 可靠、极简、可扩展的基础模型预训练库，明确支持 world models，其长序列稳定训练技术对上下文扩展研究至关重要 |
| **[FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch)** | ⭐0 (+327 today) | 从零训练 LLM 的完整教程，涵盖数据到文本生成全流程，包含长上下文位置编码与推理时扩展的实践 |
| **[testtimescaling/testtimescaling.github.io](https://github.com/testtimescaling/testtimescaling.github.io)** | ⭐99 [topic:llm-model] | "Test-Time Scaling in LLMs" 综述仓库，系统梳理推理时计算扩展策略，是长上下文推理优化的核心理论资源 |
| **[thinkwee/AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL)** | ⭐1,467 [topic:llm-model] | Agentic RL 前沿资源汇总，探索强化学习驱动的长程推理与工具调用，与长上下文决策直接相关 |

### 🔧 Post-Training 与对齐（RLHF、DPO、SFT、偏好优化、推理增强）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | ⭐0 (+592 today) | Agentic 编码工具，其"通过自然语言命令执行例行任务"的能力依赖于后训练对齐的指令跟随与工具使用优化 |
| **[anthropics/skills](https://github.com/anthropics/skills)** | ⭐0 (+454 today) | Anthropic 官方 Agent Skills 仓库，**模块化能力注入**的代表，体现通过可组合技能进行 post-training 能力扩展的新范式 |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | ⭐0 (+908 today) / ⭐199,292 [topic:llm] | "Agent harness 性能优化系统"，聚焦 Skills、Instincts、Memory、Security 的 research-first 开发，是对齐工程化的前沿实践 |
| **[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)** | ⭐530 [topic:llm-model] | On-Policy Distillation 资源汇总，探索在线策略蒸馏作为高效 post-training 对齐方法，替代传统 RLHF 的样本效率瓶颈 |
| **[open-compass/opencompass](https://github.com/open-compass/opencompass)** | ⭐7,047 [topic:llm-model] | 大模型评测平台，覆盖 100+ 数据集，是对齐效果评估与幻觉检测的基础设施 |

### 👁️ 幻觉与可靠性（事实 grounding、幻觉检测、可信度校准）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** | ⭐79,754 [topic:rag] | 跨会话持久上下文系统，通过 AI 压缩与相关性注入实现记忆回溯，直接缓解长对话中的事实漂移与幻觉累积 |
| **[mem0ai/mem0](https://github.com/mem0ai/mem0)** | ⭐57,159 [topic:rag] | AI Agent 通用记忆层，通过显式记忆管理减少参数化知识依赖，从源头降低幻觉风险 |
| **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** | ⭐35,982 [topic:rag] [EMNLP2025] | 轻量快速 RAG，通过图结构增强检索增强的事实 grounding 能力，缓解生成幻觉 |
| **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** | ⭐32,342 [topic:vector-db] | "Vectorless, Reasoning-based RAG"，摒弃向量近似检索，以推理驱动的精确文档索引提升事实准确性 |
| **[cognee/cognee](https://github.com/topoteretes/cognee)** | ⭐17,593 [topic:vector-db] | 6 行代码实现的 Agent 记忆控制平面，通过结构化记忆管理增强生成可靠性 |

### 🏗️ 基础设施（上述领域的训练框架、推理引擎、评测工具）

| 项目 | Stars / 今日新增 | 一句话说明 |
|:---|:---|:---|
| **[vllm-project/vllm](https://github.com/vllm-project/vllm)** | ⭐81,448 [topic:llm] | 高吞吐内存高效 LLM 推理引擎，长上下文场景的 KV Cache 优化核心基础设施 |
| **[0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)** | ⭐7,469 [topic:llm-model] | Rust 模块化 LLM 应用框架，支持可扩展的推理流水线构建 |
| **[skyzh/tiny-llm](https://github.com/skyzh/tiny-llm)** | ⭐4,216 [topic:llm-model] | Apple Silicon 上的 LLM 推理服务课程，构建类 vLLM + Qwen 系统，含长上下文推理优化实践 |
| **[EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning)** | ⭐2,238 [topic:llm-model] | ICL 与提示工程前沿资源，涵盖上下文学习中的位置偏差、长示例序列优化等关键问题 |

---

## 3. 研究趋势信号分析

今日热榜释放出三个与研究高度相关的信号。**第一，文档解析的"工程化重构"**：`liteparse` 以 Rust 重写文档解析，`markitdown` 由微软背书推动格式标准化，二者共同指向 OCR/文档理解链路中**前置解析模块的性能瓶颈**正在被系统性攻克，这对 HMER 等依赖精确版面分析的任务具有直接增益。**第二，Agent 能力的"模块化对齐"范式**：Anthropic Skills 生态（`claude-code` + `skills` + `ECC`）表明，post-training 对齐正从"端到端微调"转向"可组合技能注入"，`ECC` 提出的 "Instincts" 概念可能对应隐式偏好建模的新层次。**第三，世界模型与长上下文的融合**：`stable-worldmodel` 与 `stable-pretraining` 同期出现，结合 `testtimescaling` 综述的登榜，暗示社区正将**推理时计算扩展**从纯语言任务迁移至物理世界建模，这对多模态长上下文推理（如视频-语言联合推理）具有先导意义。此外，`VoxCPM2` 的 Tokenizer-Free 架构若与视觉编码器结合，可能催生真正的端到端多模态统一模型。

---

## 4. 研究关注热点

- **`run-llama/liteparse` [🔗](https://github.com/run-llama/liteparse)** — Rust 高性能文档解析器，直接解决长文档 RAG/OCR 流水线的解析瓶颈，其结构化输出设计可作为 HMER 任务的标准化输入接口，建议关注其与版面分析模型的集成潜力

- **`anthropics/skills` + `ECC` [🔗](https://github.com/anthropics/skills) [🔗](https://github.com/affaan-m/ECC)** — Agent Skills 的模块化对齐范式，`ECC` 的 "Instincts" 与 "Memory" 机制可能蕴含新的偏好学习架构，值得深入分析其是否隐式实现了某种形式的在线 DPO 或人类反馈累积

- **`galilai-group/stable-worldmodel` + `stable-pretraining` [🔗](https://github.com/galilai-group/stable-worldmodel) [🔗](https://github.com/galilai-group/stable-pretraining)** — 世界模型预训练基础设施首次进入热榜，其"稳定性"技术（如长序列梯度控制、记忆一致性机制）可能直接迁移至长上下文语言模型的训练，建议跟踪其技术报告

- **`testtimescaling/testtimescaling.github.io` [🔗](https://github.com/testtimescaling/testtimescaling.github.io)** — Test-Time Scaling 系统综述，涵盖推理时计算扩展的 what/how/where/how-well，是长上下文推理优化的理论地图，建议作为研究入口梳理该领域与 Chain-of-Thought、Self-Consistency 的关联

- **`VectifyAI/PageIndex` [🔗](https://github.com/VectifyAI/PageIndex)** — "Vectorless, Reasoning-based RAG" 挑战了向量检索的事实准确性瓶颈，其推理驱动的文档索引机制可能为幻觉缓解提供新思路，即通过显式推理路径替代隐式相似度匹配，增强生成内容的可溯源性

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*