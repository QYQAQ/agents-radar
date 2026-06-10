# Hugging Face 热门模型日报 2026-06-10

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-10 00:36 UTC

---

# Hugging Face 研究模型日报 | 2026-06-10

## 今日速览

今日 Hugging Face 热门模型榜单中，**Google Gemma-4 系列**以原生 any-to-any 架构强势占据多模态赛道，其统一的多模态设计对 OCR 与文档理解研究具有直接价值。**PaddleOCR-VL-1.6** 作为唯一专注 OCR 的模型上榜，标志着文档智能向视觉语言融合的持续演进。NVIDIA 在视觉定位（LocateAnything-3B）和语音流式识别（Nemotron-3.5-ASR）双线布局，显示多模态基础设施的成熟化。DeepSeek-V4-Pro 以压倒性下载量（430万+）巩固开源推理模型领导地位，而 Step-3.7-Flash 与 HauhauCS 的 Qwen3.6 变体则反映视觉语言模型在后训练对齐与社区微调层面的活跃生态。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle / 280 / 10,139 | 基于 ERNIE4.5 的 OCR 视觉语言模型，将传统 OCR 与 VLM 架构深度融合，对 HMER（手写数学表达式识别）、版面分析与文档理解研究具有直接参考价值，代表中文 OCR 生态向端到端多模态转型的关键节点。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 810 / 581,354 | 原生 any-to-any 统一架构，支持图像-文本-文本自由交互，其多模态融合机制为 OCR 嵌入、文档视觉问答及跨模态信息整合提供新的基线范式，是研究多模态统一表示的重要载体。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 1,729 / 123,922 | 视觉定位专用模型，实现开放词汇的细粒度空间定位，对文档版面元素定位、图表区域检测及 OCR 后处理中的空间推理具有技术迁移价值。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai / 358 / 46,729 | 高效视觉语言模型，优化推理速度与多模态理解平衡，适合作为资源受限场景下文档理解、图像描述与视觉推理的基准模型。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 1,593 / 2,983,909 | 社区激进微调版 Qwen3.6 MoE VLM，极高下载量反映社区对视觉语言模型后训练对齐的旺盛需求，其"Uncensored"标签暗示安全对齐与能力释放之间的张力，是研究 RLHF 边界与幻觉缓解的对照样本。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** / **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** / **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth / 531 / 660,140; 171 / 127,332; 114 / 96,059 | Unsloth 对 Gemma-4 系列的量化与 GGUF 适配覆盖 12B 至 26B-A4B MoE 规模，大幅降低多模态模型研究门槛，其 QAT（量化感知训练）版本对边缘部署场景下的 OCR/VQA 精度保持具有方法论意义。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS / 135 / 8,106 | 社区对 Gemma-4 的"去限制"微调版本，与官方对齐版本形成对比，可用于研究安全训练对多模态推理能力的影响及幻觉缓解机制的有效性评估。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 4,740 / 4,302,553 | 当前开源推理模型标杆，MoE 架构实现高效长上下文处理，其数学与代码推理能力为 HMER 公式推导、长文档逻辑分析提供强基座，是研究长上下文推理机制与可扩展性的核心参考。 |
| **[LiquidAI/LFM2.5-8B-A1B-1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI / 572 / 137,138 | 液态神经网络架构的 MoE 变体，非 Transformer 结构在长序列建模上的替代路径，为突破注意力机制复杂度瓶颈、实现高效长上下文 OCR 与文档理解提供新范式。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains / 272 / 17,571 | 显式"Thinking"模式的代码推理模型，其结构化思维链机制可迁移至数学公式推导与多步文档推理场景，是研究推理过程可解释性的重要对象。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** / **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google / 479 / 122,464; 114 / 63,049 | 基础版与官方 QAT 量化版 Gemma-4，any-to-any 架构原生支持长序列多模态输入，官方量化策略为研究长上下文模型压缩与精度权衡提供权威基准。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc / 733 / 133,351 | 专注人力资源管理的 1B 规模对齐模型，虽领域特定，但其高效 SFT/RLHF 实践为小规模专业化 OCR/文档模型的后训练流程提供可复用的数据与方法论参考。 |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** / **[nex-agi/Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini)** | nex-agi / 160 / 783; 110 / 748 | 基于 Qwen3.5-MoE 的社区微调系列，展示 MoE 架构在多模态后训练中的灵活性，Pro/mini 双版本策略为研究模型规模与对齐效果的缩放规律提供对照。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs / 155 / 1,784 | Cohere2-MoE 架构的代码对齐模型，其偏好优化与能力专项训练技术可迁移至结构化数据（表格、代码块）的 OCR 后理解与格式化任务。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** / **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia / 174 / 56,864; 152 / 71,818 | NVIDIA 旗舰 Nemotron-H 系列提供 BF16 与 NVFP4 双精度格式，其 Nemotron 架构以高事实一致性著称，Ultra 规模的 RLHF 对齐强度为研究大模型幻觉缓解的规模化效应提供极端案例；NVFP4 格式对量化校准与置信度估计的影响值得深入探索。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano)** | nvidia / 214 / 36,739 | Cosmos3 Omni 系列基础组件，支持多模态数据生成与理解管道，其扩散架构与 tokenizer 设计可作为文档图像合成、OCR 数据增强及多模态评测基准构建的基础设施。 |
| **[google/magenta-realtime-2](https://huggingface.co/google/magenta-realtime-2)** | google / 164 / 18,216 | 实时音频生成模型，TFLite 部署优化经验可迁移至移动端 OCR 引擎的实时推理优化，跨模态实时处理的技术栈具有方法论借鉴价值。 |

---

## 研究生态信号

**Gemma-4 家族崛起与多模态统一化**：Google 以 any-to-any 架构强势定义下一代多模态基座标准，Unsloth 等社区力量的快速量化适配形成"官方-社区"双轨生态，显著降低研究门槛。Qwen 系列（Step-3.7、Nex-N2、HauhauCS 微调版）则代表中文-全球视觉语言模型的另一极，MoE 架构成为 2026 年多模态扩展的共识路径。

**开源权重主导推理与 OCR 研究**：DeepSeek-V4-Pro 的 430 万下载量验证开源推理模型的研究基础设施地位；PaddleOCR-VL 作为唯一上榜 OCR 专用模型，暗示文档理解正快速被通用 VLM 吸收，专用 OCR 模型需向更深层的视觉-语言-知识融合演进以维持独立价值。

**后训练对齐的社区分化与"去限制"实验**：HauhauCS"Uncensored"与 OBLITERATUS"OBLITERATED"等激进微调版本的高热度，反映研究社区对安全对齐成本（能力损失、幻觉模式变化）的主动探索，为可控幻觉缓解与对齐可逆性研究提供天然实验场。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔥 首要** | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | 当前榜单中唯一专注 OCR 的模型，ERNIE4.5 基座与 PaddleOCR 生态的融合代表文档智能的技术前沿。建议重点探究：其视觉编码器对复杂版面（表格、公式、手写体）的表征机制；与 Gemma-4 等通用 VLM 在文档理解任务上的能力边界对比；以及作为 HMER 研究基线的可行性。 |
| **🔥 核心** | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | any-to-any 统一架构为 OCR 与多模态推理研究提供新范式。关键探索点：原生多模态融合是否优于传统"OCR 引擎+VLM"级联方案；长上下文下的多页文档推理一致性；以及官方对齐版本与社区"去限制"版本的幻觉模式差异分析。 |
| **🔥 对照** | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** + **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | 组合研究开源推理模型的对齐光谱：DeepSeek-V4-Pro 代表高强度 RLHF 后的"稳定"状态，HauhauCS 版本代表社区干预后的"释放"状态。通过对比两者在数学公式推理、图文事实一致性等任务上的幻觉率与校准置信度，可量化评估后训练对齐对多模态推理的真实影响，为幻觉缓解技术的定向优化提供实证基础。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*