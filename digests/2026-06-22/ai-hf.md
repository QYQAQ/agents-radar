# Hugging Face 热门模型日报 2026-06-22

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-22 00:37 UTC

---

# Hugging Face 研究模型日报 | 2026-06-22

## 今日速览

本周 Hugging Face 热门模型显示**多模态统一架构**成为主流趋势：Google 的 `gemma-4-12B-it` 以 any-to-any 架构打破模态边界，MiniMax-M3 和 Kimi-K2.7-Code 推动视觉语言模型向代码推理渗透。Qwen3.6 系列（35B-A3B 及其衍生版本）在 MoE 架构与视觉能力融合上表现突出，下载量突破 500 万。值得注意的是，**文档理解专用模型**如 `datalab-to/lift` 聚焦 PDF 解析，而 `microsoft/FastContext-1.0-4B-SFT` 针对长上下文场景进行 SFT 优化，显示后训练对齐在特定垂直领域的深化。幻觉缓解方面虽无直接冠名模型，但 DeepSeek-V4-Pro 的高下载量（261万）反映社区对可靠推理基础模型的持续需求。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 107 | 516 | 基于 Qwen3.5 的 PDF 文档理解模型，直接针对版面分析与文本提取优化，是 OCR+VLM 融合路线的典型代表，适合作为文档智能基线 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,126 | 1,815,370 | **any-to-any 统一架构**，原生支持图像-文本双向生成，为跨模态对齐研究提供开源基座；Gemma 4 系列的高下载量验证统一多模态范式的社区接受度 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,177 | 104,076 | 专用 multimodal 架构，定位 image-text-to-text，适合研究商业级 VLM 的设计取舍与开源复现差距 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 945 | 363,308 | 视觉-代码联合推理模型，image-feature-extraction 标签提示其视觉编码器可能针对代码截图/图表优化，是 HMER（手写数学表达式识别）向通用视觉推理扩展的参考 |
| **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen | 2,195 | 5,148,673 | **本周下载量冠军**，MoE 架构+视觉能力，conversational 标签表明多轮对话中的跨模态上下文对齐值得关注 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,078 | 3,966,691 | 激进去对齐化微调版本，高下载量（近400万）揭示**对齐与能力的张力**：研究其幻觉率变化对安全对齐方法论有反向验证价值 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong | 275 | 190,993 | MTP（Multi-Token Prediction）+ 视觉的 GGUF 量化实践，适合研究推理效率与多模态能力的边缘部署权衡 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,034 | 762,861 | Diffusion + Gemma 的图像生成-理解统一架构，为"生成式理解"这一反幻觉方向提供新范式：通过生成能力增强视觉理解的自洽性 |
| **[unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF)** | unsloth | 150 | 42,837 | Unsloth 优化的量化版本，关注压缩后视觉编码器的性能保持率，对多模态模型的高效推理研究有直接价值 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,999 | 2,611,991 | **点赞数最高**，conversational 能力突出，DeepSeek 系列以推理深度著称，适合作为长上下文推理与复杂问题求解的基准对照 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 261 | 2,593 | **显式针对长上下文优化的 SFT 模型**，"Explorer SubAgent" 标签暗示检索增强的上下文管理机制，是研究高效长上下文架构的关键样本 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 560 | 20,277 | 3B 级数学专用模型，基于 Qwen2，小参数推理模型的能力边界与蒸馏效率研究素材 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,081 | 358,677 | 社区微调版 Gemma 4，coding+reasoning 双标签，高点赞反映代码推理的社区热度，可作为开源后训练效果的对比基线 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 271 | 21,730 | "agentic+terminal" 标签指向工具使用与自主推理，3.5x-tau2 可能指推理温度或上下文缩放系数，适合研究推理可控性 |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim | 101 | 36,421 | MTP + "pi-tune" 可能指渐进式或参数高效微调，研究多 token 预测与长序列建模的协同 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 474 | 19,551 | Cohere2 MoE 架构的代码特化版，商业实验室的 mini 模型策略与社区大模型路线的对比研究价值 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 261 | 2,593 | **SFT 标签明确**，针对长上下文的监督微调方法论，SubAgent 架构可能涉及多智能体对齐策略 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,078 | 3,966,691 | "Aggressive" 去对齐化实验，**反向研究素材**：通过对比原始 Qwen3.6 与该版本，可量化安全对齐对通用能力/幻觉的影响 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 1,813 | 27,413 | GLM 系列的 MoE+DSA（Dynamic Sparse Attention）架构，官方版本的对话对齐质量可作为中文场景对齐基准 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org | 120 | 217,361 | FP8 量化官方版，高下载量显示低精度推理的工业需求，研究量化对对齐后模型行为一致性的影响 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,034 | 762,861 | **生成式理解架构**：通过扩散模型的生成能力实现视觉理解的自验证，内在机制可能缓解 VLM 的"幻觉描述"问题 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,240 | 241,845 | **定位精度导向**，image-feature-extraction 强调空间 grounding，显式位置预测相比自由文本生成在幻觉控制上更具优势 |
| **[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,999 | 2,611,991 | DeepSeek 系列以推理过程可解释性著称，链式推理的显式化是缓解幻觉的核心路径之一 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 研究相关性 |
|:---|:---|---:|---:|:---|
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 224 | 32,260 | Unsloth 优化框架的 GLM 5.2 实现，关注其量化与微调工具链对 MoE 模型的支持成熟度 |
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI | 90 | 7,726 | 液体神经网络（Liquid Neural Networks）的嵌入模型，时序连续性机制可能为长上下文表示提供新思路 |
| **[poolside/Laguna-M.1](https://huggingface.co/poolside/Laguna-M.1)** | poolside | 83 | 2,580 | vLLM/SGLang 双后端支持，推理基础设施优化对长上下文/多模态模型的实际部署研究有工具价值 |

---

## 研究生态信号

**Qwen 家族主导多模态开源生态**：Qwen3.6 系列（官方+衍生）占据本周下载量前三席中的两席，MoE+视觉的架构选择成为事实标准，但其密集衍生版本（GGUF、Uncensored、MTP 等）也暴露社区对"官方对齐"的不满足——这本身是后训练对齐研究的张力信号。Google Gemma 4 的 any-to-any 架构与 DiffusionGemma 的生成-理解统一，代表大厂向"反幻觉"原生架构的探索。值得警惕的是，**直接标注"幻觉缓解"的模型缺失**，该方向仍停留在技术报告层面而非模型发布层面；HauhauCS 的激进去对齐版本高下载量（近400万）甚至暗示社区存在"对齐疲劳"。长上下文方面，Microsoft FastContext 的显式 SFT 优化与 SubAgent 架构，标志着该领域从"预训练加长"转向"后训练增效"的方法论转变。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **★★★** | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | 罕见的长上下文**专用 SFT 模型**，4B 参数规模允许全量微调实验复现；"Explorer SubAgent" 暗示的检索-生成协同机制，是缓解长上下文幻觉的可解释路径。建议对比其与 Qwen3.6-35B 在长文档 QA 上的幻觉率-召回率权衡曲线。 |
| **★★☆** | **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | **生成式理解**的反直觉架构：用扩散模型的迭代去噪过程替代自回归生成，可能从根本上改变 VLM 的"幻觉产生机制"——自回归的累积错误 vs 扩散的全局约束。适合设计视觉问答中的事实一致性评测，验证其相比自回归 VLM 的幻觉缓解幅度。 |
| **★★☆** | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **反向工程价值**：近400万下载量的激进去对齐版本，与官方 Qwen3.6-35B-A3B 构成天然对照组。可系统测量：① 安全对齐移除后的幻觉类型迁移（从事实幻觉转向价值幻觉？）② MoE 路由模式的变化 ③ 多模态 grounding 精度的衰减。这对"对齐是否损害真实能力"的争议提供实证数据。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*