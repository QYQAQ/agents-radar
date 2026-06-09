# Hugging Face 热门模型日报 2026-06-09

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-09 00:30 UTC

---

# Hugging Face 研究模型日报 | 2026-06-09

## 今日速览

本周 Hugging Face 热门模型中，**多模态统一架构**成为最显著趋势：Google Gemma-4 系列以"any-to-any"范式强势登顶，NVIDIA LocateAnything-3B 在视觉 grounding 任务上获得极高下载量，而 **PaddleOCR-VL-1.6** 作为 OCR 领域罕见进入热门榜的模型，标志着文档理解正加速向视觉语言融合演进。DeepSeek-V4 系列（Pro/Flash）凭借 MoE 架构和极高下载量持续主导长上下文推理场景，但本周**幻觉缓解与对齐专用模型明显缺位**，社区仍需关注通用模型的可信输出能力。量化与边缘部署（GGUF/QAT）成为基础设施标配，Unsloth 生态几乎垄断了高效推理的中间层。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 277 | 9,924 | 基于 ERNIE4.5 的 OCR 视觉语言模型，将传统 OCR 管道升级为端到端文档理解；**与 HMER 研究直接相关**——其 VL 架构为手写公式识别提供了可迁移的编码器-解码器范式，且 PaddleOCR 生态的版面分析模块历来是数学文档处理的基础工具。 |

> **领域观察**：本周 OCR/HMER 专用模型仅 PaddleOCR-VL-1.6 入榜，传统文本识别模型（如 TrOCR、Nougat）缺席热门榜，暗示文档理解正被通用 VLM 吸收，但公式识别的细粒度定位能力仍是未被充分解决的瓶颈。

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,617 | 121,594 | 轻量级视觉 grounding 模型，支持开放式目标定位与指代表达理解；**与多模态推理/幻觉缓解高度相关**——其精确空间定位能力可作为 VLM 的"视觉锚定"模块，减少语言模型在目标指代上的幻觉。 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 750 | 554,173 | 统一 any-to-any 架构，原生支持图像/文本交错输入与输出；**多模态推理核心基准**——其统一表示为跨模态信息融合与冲突检测提供了研究平台，直接关联视觉语言推理的可解释性。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 450 | 117,509 | Gemma-4 基座模型，无指令微调；**对齐研究关键素材**——作为 post-training 的"干净起点"，可用于对比 SFT/RLHF 前后多模态对齐效果，或构建幻觉评测的受控实验。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,553 | 3,036,465 | 激进去审查化的 Qwen3.6 MoE VLM；**对齐研究的负面案例**——其"Uncensored/Aggressive"标签揭示了安全对齐与有用性之间的张力，为 RLHF 的奖励黑客（reward hacking）和价值观对齐研究提供极端样本。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 351 | 45,535 | 阶跃星辰的视觉语言轻量模型；**多模态效率研究**——在 VLM 压缩与推理加速维度上与 Gemma-4 形成对照，适合跨架构的效率-精度权衡分析。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 695 | 1,186,648 | 带 Multi-Token Prediction 的量化 VLM；**长上下文推理基础设施**——MTP 机制与 GGUF 量化的结合，为研究投机解码（speculative decoding）在多模态长序列上的效果提供了现成工具。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** / **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** / **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 500/146/100 | 645,263/121,399/87,455 | Gemma-4 系列量化变体；**多模态部署与校准研究**——QAT 与标准量化的并行发布，支持量化对视觉特征表示损伤的对比实验。 |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 97 | 52,386 | 官方 QAT 量化版本；**对齐可复现性**——官方与第三方（Unsloth）量化方案的同场竞技，为后训练量化对对齐质量的影响提供 A/B 测试条件。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,720 | 5,399,597 | DeepSeek V4 完整版 MoE 模型（总参数 550B 级，激活约 55B）；**长上下文推理的当前标杆**——其 MLA 注意力机制与专家路由设计是研究长序列记忆、推理路径可解释性的核心对象，极高下载量反映学术与工业界的广泛采用。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,446 | 3,262,529 | V4 轻量加速版；**推理效率与成本研究**——与 Pro 版形成精度-延迟光谱，适合研究动态推理深度、早退机制（early exit）在长上下文任务上的应用。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 548 | 135,131 | 液态神经网络（Liquid Neural Network）MoE 架构；**长上下文的新范式**——其连续时间隐状态机制在理论上更适合变长序列建模，为超越 Transformer 的长程依赖研究提供替代基线。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 259 | 17,448 | 显式"思考"模式的代码/推理模型；**推理过程显式化**——其 Thinking 标签暗示链式推理（CoT）的内化，为研究推理时的幻觉检测（如验证中间步骤的事实性）提供结构化输出。 |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** / **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia | 165/145 | 55,910/66,219 | NVIDIA 超大规模 Nemotron 3 及 NVFP4 量化版；**长上下文训练基础设施**——与 DeepSeek-V4 同级的 MoE 规模，但 NVIDIA 官方量化格式（NVFP4）的发布，为研究自定义浮点格式对长序列数值稳定性的影响提供独特条件。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 726 | 163,953 | HRM（Human Reward Modeling）对齐的 1B 文本模型；**本周唯一直接标注"对齐"方法的模型**——其 HRM 标签暗示替代 RLHF 的人类反馈建模路径，为研究偏好学习的数据效率与标注成本提供新视角。 |

> **领域警示**：本周热门榜中 **RLHF/DPO/SFT 专用模型极度稀缺**，HRM-Text-1B 是唯一明确聚焦后训练对齐的模型。主流多模态模型（Gemma-4、DeepSeek-V4）的对齐细节未公开，社区面临"黑盒对齐"的复现困境。

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| *本周无直接标注"幻觉缓解"的热门模型* | — | — | — | — |

> **关键缺口**：幻觉缓解作为活跃研究领域，在热门模型榜中完全缺席。现有模型的幻觉控制能力依赖于通用对齐（如 Gemma-4-it、DeepSeek-V4 的指令微调），但无专用的事实 grounding、置信度校准或 RAG 增强架构进入本周热门。研究者需关注：**LocateAnything-3B 的视觉锚定机制**可作为幻觉缓解的间接工具，**HRM-Text-1B 的人类奖励建模**或隐含真实性偏好，但两者均未显式优化幻觉指标。

---

### 🏗️ 研究基础设施

| 模型/工具 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano)** / **[nvidia/Cosmos3-Super](https://huggingface.co/nvidia/Cosmos3-Super)** | nvidia | 203/157 | 34,104/27,548 | NVIDIA Cosmos 3 世界模型系列（Nano/Super）；**多模态生成的物理一致性研究**——其 Omni 架构支持视频/图像/3D 的统一生成，为研究生成式模型的时空一致性幻觉（如物理规律违背）提供评测平台。 |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia | 287 | 3,957 | 流式 ASR 模型，支持缓存感知推理；**长上下文语音研究**——其流式架构的缓存机制可迁移至长文档语音输入的实时处理，与 OCR-VL 结合可构建语音-文档联合理解管道。 |

---

## 研究生态信号

**Gemma-4 与 Qwen3.6 构成多模态双寡头，但开源权重仍滞后于架构创新。** Google 以 "any-to-any" 统一范式强势定义视觉语言模型的接口标准，而 Qwen 生态（含大量社区微调变体）凭借 MoE 效率与中文优化占据应用层。值得注意的是，**OCR 领域出现"被 VLM 吸收"的风险信号**——PaddleOCR-VL-1.6 虽入榜，但其 ERNIE4.5 基座表明文档理解已完全嵌入通用多模态框架，传统专用 OCR 模型（如基于 CRNN/Transformer 的纯文本识别）在热门榜消失。幻觉缓解与对齐领域则呈现**研究活跃但模型发布冷清**的错位：社区论文量持续增长，却无专用模型进入本周 Top 30，暗示该方向可能过度依赖评测基准（如 HalluBench、FACTOR）而缺乏可部署的解决方案，或主流模型的"足够好"幻觉控制已满足大部分应用需求，抑制了专用模型的市场空间。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **幻觉缓解的模块化插件**：其开放式视觉 grounding 能力可接入任意 VLM 作为"事实核查器"——当模型生成涉及空间位置的描述时，LocateAnything 可提供像素级验证，直接支持"视觉事实性"的量化评测。建议研究：将该模型与 Gemma-4 级联，构建指代表达理解的幻觉检测管道。 |
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | **HMER 的迁移学习基座**：ERNIE4.5 的视觉编码器在文档结构理解上的预训练，为手写数学公式识别提供了超越纯文本 OCR 的上下文建模能力。建议研究：在该模型上注入 HMER 专用数据集（如 CROHME、HME100K），对比端到端微调与两阶段（检测+识别）范式的公式定位精度，尤其关注长公式序列的解码稳定性。 |
| ⭐⭐☆ | **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | **对齐方法的替代路径验证**：HRM（Human Reward Modeling）若确为替代 PPO/DPO 的新范式，其 1B 规模适合快速复现与消融。建议研究：在相同偏好数据集上对比 HRM 与标准 RLHF 的奖励过优化（reward over-optimization）倾向，尤其测量模型在分布外查询上的幻觉率差异，验证 HRM 是否更鲁棒。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*