# Hugging Face 热门模型日报 2026-06-20

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-20 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-20

## 今日速览

本周 Hugging Face 热门模型呈现多模态统一架构与长上下文推理的深度融合趋势。Google 的 **gemma-4-12B-it** 以"any-to-any"范式突破传统模态边界，**MiniMax-M3** 和 **Kimi-K2.7-Code** 持续推动视觉语言模型的代码推理能力。值得注意的是，**DeepSeek-V4-Pro** 以近 5000 点赞领跑，其 MoE 架构与对话能力对后训练对齐研究具有重要参考价值；**Microsoft FastContext-1.0-4B-SFT** 虽规模精简，但明确指向长上下文压缩与探索性子代理机制，与长上下文推理研究直接相关。整体生态中，Qwen3.6 家族微调版本激增，反映社区对开源权重进行偏好对齐和领域适配的活跃需求。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,096 | 1,590,882 | **统一多模态架构标杆**：原生 any-to-any 设计，支持图像-文本双向生成，为 OCR/HMER 的统一编码器研究与跨模态表示学习提供基础模型。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,133 | 67,836 | **MoE 视觉语言模型**：image-text-to-text 任务标签，结合 MoE 架构与多模态输入，适合研究视觉推理中的专家路由机制与计算效率权衡。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 909 | 274,865 | **代码视觉推理模型**：支持图像输入的代码生成，对 HMER 中的公式→LaTeX 结构化生成、屏幕截图理解等 OCR 下游任务有直接迁移价值。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,194 | 228,669 | **视觉定位基础模型**：image-feature-extraction 导向，3B 参数实现高效视觉定位，为文档版面分析、公式空间定位等 OCR 细粒度任务提供编码器基础。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,010 | 601,208 | **扩散语言模型**：将扩散机制引入语言生成，其迭代去噪过程与视觉-文本联合建模对多模态幻觉缓解（逐步修正生成）具有方法论启发。 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio | 325 | 190,639 | **超大规模开放 VLM**：397B 总参数（MoE），巴西政府开源，为研究多语言/多文化场景下的 OCR 与文档理解提供独特数据分布。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,007 | 3,730,978 | **高下载量社区 VLM**：uncensored + vision 标签，反映社区对去除安全对齐约束后的原生多模态能力探索，是研究对齐强度与幻觉关系的极端案例。 |
| **[unsloth/MiniMax-M3-GGUF](https://huggingface.co/unsloth/MiniMax-M3-GGUF)** | unsloth | 107 | 24,354 | **量化部署版本**：GGUF 格式降低研究门槛，便于在资源受限环境下验证 MiniMax-M3 的视觉推理与长上下文组合能力。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,969 | 3,015,772 | **本周最热开源模型**：DeepSeek V4 系列，conversational 标签，MoE 架构，在长上下文推理与代码任务上表现突出，是研究推理时计算扩展与后训练对齐的理想基座。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 229 | 1,437 | **长上下文压缩研究专用**：明确标注 "Explorer SubAgent"，4B 参数聚焦上下文压缩与子代理探索机制，与长上下文推理中的信息检索、层级注意力研究直接相关。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 458 | 12,148 | **轻量数学推理模型**：Qwen2 基座 + math 标签，3B 规模验证小模型推理能力，适合研究推理能力的涌现阈值与蒸馏效率。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 1,845 | 268,102 | **代码推理社区微调**：Gemma-4 基座融合 Fable5/Composer2.5，GGUF 格式便于本地验证长代码上下文中的推理连贯性。 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 1,532 | 11,871 | **GLM 新一代架构**：glm_moe_dsa 标签，双向注意力与 MoE 结合，其长文本双向编码特性对文档级 OCR 理解有结构优势。 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org | 105 | 93,927 | **FP8 量化版本**：高下载量表明研究社区对高效长上下文推理的需求，适合量化精度与推理稳定性研究。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 178 | 8,392 | **社区量化适配**：unsloth 优化版本，降低 GLM-5.2 长上下文实验的硬件门槛。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 229 | 1,437 | **SFT 对齐的上下文模型**：SFT 后缀明确标注监督微调来源，"Explorer SubAgent" 暗示对齐目标为探索性行为，是研究对齐目标与能力涌现关系的明确案例。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU | 406 | 588,753 | **激进对齐移除实验**：名称中 "Uncensored" + "Heretic" + 超高下载量，构成研究对齐移除后模型行为（包括幻觉、有害输出）的自然实验样本。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,007 | 3,730,978 | **社区对齐对抗样本**："Aggressive" 对齐移除策略，与官方版本形成对比，可直接用于量化研究不同对齐强度对多模态幻觉的影响。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 458 | 17,693 | **Cohere MoE 对齐版本**：coherent2_moe + conversational 标签，商业实验室的对齐实践，适合对比开源/闭源对齐策略差异。 |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim | 86 | 8,138 | **MTP 多 token 预测微调**：pi-tune 暗示特定对齐策略，MTP 训练目标与对齐结合，研究多目标优化中的对齐稳定性。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,010 | 601,208 | **扩散机制缓解幻觉**：迭代去噪生成过程天然具备"自我修正"特性，与传统自回归模型的单向幻觉累积形成对比，为幻觉缓解提供新范式。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,194 | 228,669 | **空间定位增强事实性**：视觉定位能力为生成内容提供空间锚点，可扩展为"所见即所得"的幻觉检测机制， grounding 生成与事实验证的结合点。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 909 | 274,865 | **代码执行验证**：代码生成任务具备可执行验证特性，是研究"可验证幻觉"（verifiable hallucination）与自我修正机制的理想场景。 |

### 📄 OCR 与文档模型（文本识别、版面分析、文档理解、公式识别）

> *注：本周热门模型中缺乏直接标注 OCR/HMER 的专用模型，但以下多模态模型具备强 OCR 迁移潜力*

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,096 | 1,590,882 | **统一架构的 OCR 潜力**：any-to-any 支持图像→文本原生编码，无需专用 OCR 编码器，可直接评估端到端文档理解、公式识别能力，挑战传统 HMER 流水线。 |
| **[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 909 | 274,865 | **代码公式双任务**：代码与数学公式结构相似性高，其视觉-代码推理能力可直接迁移至 LaTeX 公式生成与手写公式识别。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,194 | 228,669 | **版面分析基础**：空间定位能力可扩展至文档元素检测（标题、表格、公式区域），作为 OCR 前处理模块。 |

### 🏗️ 研究基础设施（上述领域的训练框架、评测套件、数据集工具）

> *注：本周以终端模型为主，基础设施模型较少，以下识别具备工具属性的发布*

| 模型 | 作者 | 点赞 | 下载 | 说明 |
|:---|:---|---:|---:|:---|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth | 318 | 202,867 | **高效推理基础设施**：unsloth 优化降低扩散语言模型研究门槛，便于快速验证扩散机制在幻觉缓解中的效果。 |
| **[unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF)** | unsloth | 141 | 33,667 | **VLM 量化工具链**：压缩-tensors 标签，支持长上下文 VLM 的本地部署验证。 |

---

## 研究生态信号

**Qwen3.6 家族成为社区对齐实验的核心载体**：本周出现至少 4 个 Qwen3.6 微调版本（HauhauCS Aggressive、DavidAU Heretic、bytkim MTP、Mia-AiLab Qwable），总下载量超 430 万，反映开源权重作为"对齐沙盒"的集中趋势。Google Gemma-4 以 any-to-any 架构推动多模态统一，可能削弱专用 OCR 编码器的必要性，但 HMER 的细粒度结构理解仍需验证。视觉语言模型呈现"开源权重 + 闭源训练"的混合态势：MiniMax、Kimi、DeepSeek 发布开源权重，但核心训练数据与对齐细节未公开，幻觉缓解研究面临可复现性挑战。值得注意的是，**uncensored/对齐移除模型获得极高下载量**（HauhauCS 370 万、DavidAU 59 万），暗示研究社区对"对齐税"（alignment tax）与原生能力边界的强烈兴趣，但也带来伦理研究风险。

---

## 值得探索

1. **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** — 明确指向长上下文压缩与探索性子代理机制，4B 小参数便于快速迭代，是验证"上下文分层注意力"与"推理时计算扩展"假设的理想基座。其 SFT 标签也为研究对齐如何塑造长上下文行为提供切入点。

2. **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** — 扩散机制与语言生成的结合是全新范式，其迭代去噪过程可形式化为"逐步幻觉修正"，建议对比评估其与自回归模型在数学公式生成（HMER）中的事实一致性差异。

3. **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** — 作为"极端对齐移除"的高下载量社区模型，可与官方 Qwen3.6 形成系统对照，量化测量对齐强度与多模态幻觉率、代码推理准确率的权衡关系，但需严格伦理审查。

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*