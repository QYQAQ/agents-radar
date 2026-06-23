# Hugging Face 热门模型日报 2026-06-23

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-23 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-23

## 今日速览

本周 Hugging Face 生态呈现**多模态统一化**与**长上下文推理**双轮驱动趋势。Google Gemma-4 系列以"any-to-any"架构引领视觉语言模型向统一模态融合演进，MiniMax-M3 和 Kimi-K2.7-Code 持续推动 VLM 在代码与推理场景的边界扩展。OCR 领域出现百度 Unlimited-OCR 的轻量发布，暗示文档理解正向"无限制"长文档处理转型。后训练对齐方面，DeepSeek-V4-Pro 以 5000+ 点赞稳居榜首，其 MoE 架构与对话优化为 RLHF 研究提供重要基座。值得关注的是，GLM-5.2 系列（含 FP8/GGUF 变体）和 Qwen3.6 生态的密集发布，反映出开源社区在推理效率与模型压缩方向的活跃微调活动。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 156 / 47 | **HMER/文档理解关键新模型**。百度提出的"无限制"OCR 架构，突破传统文档长度与版面约束，对超长数学文档、跨页公式识别及手写混合版面分析具有直接研究价值，亟需关注其视觉编码器设计是否支持二维结构感知。 |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 125 / 1,821 | 基于 Qwen3.5 的 PDF 文档理解模型，专注版面结构化提取。与 OCR 流水线后端衔接紧密，适合研究文档级 VLM 的段落定位、表格还原及公式区域检测的联合优化。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,139 / 1,912,198 | **any-to-any 架构里程碑**。Gemma-4 统一图文理解与生成，其 12B 规模的可控实验特性使其成为研究跨模态对齐、视觉指令微调及多模态幻觉缓解的理想基座。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,208 / 119,967 | 新兴 VLM 架构，image-text-to-text 任务表现突出。其多模态融合机制对研究视觉-语言联合表征、跨模态注意力路由及推理时的模态一致性验证具有参考意义。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 962 / 412,778 | 代码专用多模态模型，支持图像特征提取与压缩张量技术。对研究视觉代码理解（如图表转代码、UI 截图生成）及长代码上下文中的跨模态推理至关重要。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,291 / 247,517 | **视觉定位核心模型**。NVIDIA 的图像特征提取与定位模型，3B 规模的开放权重使其成为研究指代表达理解（REC）、视觉 grounding 及 OCR-VQA 中空间推理优化的关键工具。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,049 / 874,368 | 扩散模型与语言模型融合架构，26B-A4B 的稀疏激活设计。对研究文本到图像生成中的语义保真度、生成式多模态幻觉及扩散先验与 LLM 的对齐机制具有独特价值。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong | 281 / 214,630 | 基于 Qwen3.6 的视觉-代码模型，MTP（Multi-Token Prediction）与 GGUF 量化结合。适合研究高效多模态推理、代码生成中的视觉上下文利用及量化对跨模态性能的影响。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,113 / 4,078,305 | **高下载量多模态 MoE**，"Uncensored"标签暗示激进的对齐移除实验。对研究安全对齐的逆向分析、多模态越狱机制及幻觉与约束条件的 trade-off 具有警示性研究价值。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 5,012 / 2,421,858 | **本周绝对核心，长上下文推理标杆**。DeepSeek-V4 的 MoE 架构与 2.4M+ 下载验证其工程成熟度，是研究长文本推理效率、专家路由动态及大规模对话后训练的首选基座。 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,030 / 33,589 | **GLM 系列重大更新**，glm_moe_dsa 标签暗示动态稀疏注意力机制。对研究长上下文的高效注意力变体、MoE 在中文推理场景的优化及DSA（Dynamic Sparse Attention）与标准稀疏模式的对比实验至关重要。 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org | 133 / 334,716 | FP8 量化版本的 GLM-5.2，下载量远超基础版（334K vs 33K），反映工业界对低精度长上下文推理的强烈需求。研究 FP8 对长序列数值稳定性、注意力累积误差及推理一致性的影响。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 253 / 41,846 | Unsloth 优化的 GGUF 格式，支持本地高效部署。适合研究极端量化（Q4/Q5）下长上下文模型的保持率、KV Cache 压缩与推理幻觉的关联。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,168 / 414,734 | **高点赞社区微调**，fable5+composer2.5 的复合后训练标签。对研究多阶段 SFT 的累积效应、代码推理能力的迁移及长代码上下文（>128K）的 GGUF 适配具有参考性。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 289 / 3,498 | **微软官方长上下文 SFT 模型**，"FastContext"与"Explorer SubAgent"标签明确指向高效上下文检索与代理式长文档处理。4B 规模适合研究轻量级长上下文架构及子代理分解策略。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 609 / 32,385 | 3B 数学推理模型，基于 Qwen2。小规模强推理特性使其成为研究蒸馏效率、长思维链（long CoT）的上下文利用模式及数学幻觉来源的理想实验对象。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 126 / 842 | "Mythos"与"1M"暗示百万级上下文与叙事推理能力。9B 规模的 1M 上下文实验对研究极端长文本的位置编码外推、注意力衰减及长距离依赖的一致性具有探索价值。 |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim | 106 / 52,774 | MTP（Multi-Token Prediction）+ π-tune 微调，GGUF 部署。对研究投机解码与长上下文生成的速度-质量 trade-off、并行预测头对推理一致性的影响具有方法论意义。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 382 / 50,314 | **复合后训练的极端案例**：fable5→composer2.5→agentic 的三阶段演进，3.5x-tau2 暗示温度缩放或采样策略优化。对研究多轮 RLHF 的奖励黑客累积、agentic 能力与安全对齐的冲突具有典型分析价值。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 481 / 21,078 | Cohere 的 MoE 代码模型，conversational 标签强调对话式代码交互。适合研究代码领域的指令对齐、执行反馈集成（如代码解释器的 RL）及编程助手的诚实性校准。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 133 / 6,633 | 上述模型的 GGUF 量化版，Claude-Mythos 的命名暗示风格迁移或蒸馏自 Claude。对研究大规模教师模型的知识蒸馏、量化对对齐信号（如 RLHF 奖励模型输出）的保留具有参考性。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[lordx64/Qwable-v1](https://huggingface.co/lordx64/Qwable-v1)** | lordx64 | 162 / 3,733 | 基于 Qwen3.5-MoE 的实验性模型，image-text-to-text 与 text-generation 双任务标签。其"Qwable"命名与低下载量暗示早期探索性工作，可能包含新颖的置信度估计或拒绝机制，值得挖掘其技术报告。 |
| **[Mia-AiLab/Qwable-3.6-27b](https://huggingface.co/Mia-AiLab/Qwable-3.6-27b)** | Mia-AiLab | 125 / 23,958 | Qwable 系列的 27B 规模扩展，transformers/GGUF 双格式。与 v1 形成规模对比实验，适合研究模型规模与幻觉率的关系、MoE 路由置信度与事实准确性的相关性。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞/下载 | 研究相关性说明 |
|:---|:---|:---|:---|
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI | 100 / 8,822 | 液态神经网络（LFM）的嵌入模型，350M 参数。其连续时间架构对研究长文档的动态语义编码、RAG 检索中的时序一致性及嵌入空间的事实聚合机制具有独特方法论价值。 |
| **[LiquidAI/LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M)** | LiquidAI | 78 / 2,202 | 基于 LFM2.5 的 ColBERT 后期交互模型。与标准 Embedding 形成对比，适合研究 token 级交互对长文档事实精确定位的影响、ColBERT 架构在幻觉缓解 RAG 中的效率优化。 |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia | 629 / 34,860 | NVIDIA 流式 ASR 模型，cache-aware 架构。虽非直接文本模型，但其流式处理与缓存机制对研究长音频-文本对齐、实时多模态幻觉检测及增量式事实验证具有跨域启发。 |

---

## 研究生态信号

**Qwen3.6/Gemma-4/GLM-5.2 三足鼎立**：本周 Qwen3.6 生态（HauhauCS、bytkim、Jackrong、Mia-AiLab 等）呈现爆发式社区微调，Gemma-4 以 Google 官方 any-to-any 架构引领模态统一，GLM-5.2 则凭借 DSA 动态稀疏注意力在长上下文效率方向形成差异化。三者共同指向**视觉语言模型的开源化加速**——但核心视觉编码器与预训练数据仍闭源，形成"开放权重、封闭能力"的新范式。

**OCR 领域出现结构性缺口**：仅百度 Unlimited-OCR 与 datalab-to/lift 两篇文档模型，且下载量极低（47/1,821），与传统 OCR 的工业成熟度形成反差。这可能暗示**文档理解正被 VLM 通用能力吸收**，专用 OCR 模型向"无限制"长文档+版面理解转型，HMER 等细粒度任务需主动嫁接 VLM 后端。

**后训练对齐的"军备竞赛"化**：yuxinlu1 的复合版本命名（fable5+composer2.5+agentic+3.5x-tau2）揭示社区微调的深度叠加趋势，但多阶段 SFT/RLHF 的奖励黑客与能力遗忘缺乏系统研究。HauhauCS 的"Uncensored-Aggressive"与主流安全模型的并存，反映出**对齐强度作为可调维度的实验化**。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔥 首要** | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | OCR/HMER 领域罕见的新架构尝试，"Unlimited"宣称需验证其是否突破传统二维注意力在超长文档上的二次复杂度瓶颈。极低下载量（47）意味着尚未被社区充分检验，存在首发研究窗口。建议优先测试其在数学公式密集文档、跨页表格及手写印刷混合场景的表现，对比 Qwen3.6-VL 等通用模型的专用性优势。 |
| **🔥 核心** | **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** + **[FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)/[GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | **长上下文推理的完整实验矩阵**。DSA（Dynamic Sparse Attention）机制的技术细节亟待解析，基础版/FP8/GGUF 的三级量化对比为研究精度-长度-幻觉的 trade-off 提供天然实验组。建议设计长文本（100K-1M）的事实一致性追踪任务，量化不同精度下的注意力漂移与事实遗忘模式。 |
| **🔥 延伸** | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **轻量级长上下文代理的架构创新**。"Explorer SubAgent"暗示子代理分解与上下文检索的联合优化，4B 规模使学术机构可复现。适合作为 GLM-5.2/DeepSeek-V4 的对比基线，研究"单模型长上下文" vs "多代理上下文分解"在幻觉缓解、计算效率及用户可控性上的优劣。 |

---

*日报基于 2026-06-23 Hugging Face Hub 公开数据生成，模型描述与标签分析可能存在推断成分，建议结合官方技术报告验证。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*