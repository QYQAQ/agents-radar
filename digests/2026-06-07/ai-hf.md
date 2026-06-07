# Hugging Face 热门模型日报 2026-06-07

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-07 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-07

## 今日速览

本周 Hugging Face 生态呈现**多模态统一化**与**长上下文推理**两大主线趋势。Google Gemma-4 系列以"any-to-any"架构实现原生多模态统一，标志着开源 VLM 向真正的跨模态推理迈进；PaddleOCR-VL-1.6 作为专业 OCR 模型持续迭代，ERNIE4.5 底座强化了文档理解能力；DeepSeek-V4 系列（含 Flash 变体）以超 500 万下载量领跑推理模型，其 MoE 架构与 post-training 优化值得关注。NVIDIA 密集发布 LocateAnything-3B 等定位模型及 Cosmos3 系列，显示视觉 grounding 与生成式世界模型的研究热度。值得注意的是，**幻觉缓解与对齐**虽未以独立标签出现，但 Step-3.7-Flash、Mellum2-Thinking 等模型的"vision-language"与"thinking"定位隐含了对输出可靠性的工程优化。

---

## 热门模型

### 📄 OCR 与文档模型（文本识别、版面分析、文档理解、公式识别）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle \| 👍258 \| ⬇8,365 | 基于 ERNIE4.5 的视觉语言 OCR 模型，延续 PaddleOCR 系列在中文文档、复杂版面及手写公式识别上的优势；**HMER 研究者可关注其 VL 架构对数学表达式的编码方式与端到端识别策略**。 |

> *本周 OCR/HMER 专项模型较少，但 Gemma-4、Step-3.7-Flash 等 VLM 的文档理解能力可能间接冲击专用 OCR 模型的研究定位，需关注通用 vs 专用的能力边界。*

---

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google \| 👍616 \| ⬇315,131 | 原生 any-to-any 多模态模型，统一处理文本、图像、视频输入，12B 规模实现高效跨模态推理；**研究核心：其统一架构是否缓解了传统 VLM 的模态对齐幻觉，以及视觉 token 压缩对长文档理解的影响**。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google \| 👍377 \| ⬇84,549 | 基础版 any-to-any 模型，为研究社区提供 SFT/RLHF 前的对齐基线；**适合作为多模态 post-training 对齐与幻觉缓解研究的实验底座**。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth \| 👍421 \| ⬇458,174 | GGUF 量化版本，极高下载量反映边缘部署需求；**可研究量化对多模态 grounding 精度与幻觉率的损伤边界**。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia \| 👍1,451 \| ⬇111,078 | 3B 参数的视觉定位模型，支持开放式词汇的任意目标定位；**与 OCR 结合可探索"文本指代定位"（text-referred grounding）在文档理解中的应用**。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai \| 👍342 \| ⬇38,716 | 轻量视觉语言模型，"Flash"定位暗示推理效率优化；**需关注其 vision-language 融合机制在快速响应场景下的幻觉控制策略**。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS \| 👍1,487 \| ⬇2,771,843 | Qwen3.6 MoE 的激进去审查微调版，极高下载量反映社区需求；**"Uncensored"标签警示：研究其对齐移除后的多模态幻觉放大效应具有反向参考价值**。 |
| **[nvidia/PiD](https://huggingface.co/nvidia/PiD)** | nvidia \| 👍312 \| ⬇972 | 图像到图像超分辨率/修复模型；**可辅助 OCR 预处理中的低质量文档图像增强，但需评估生成式增强对文本保真度的影响**。 |

---

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai \| 👍4,681 \| ⬇5,510,611 | 本周绝对热门，V4 代 MoE 架构推理模型，超 550 万下载；**核心研究点：其长上下文窗口（推测 256K+）的 KV 缓存优化、数学推理中的思维链忠实度，以及作为后训练对齐基座的潜力**。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai \| 👍1,421 \| ⬇3,436,213 | 轻量推理版本，"Flash"通常对应投机解码或架构精简；**适合研究推理效率与输出质量（含幻觉率）的帕累托前沿**。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains \| 👍239 \| ⬇16,395 | "Thinking"标签明确指向推理增强，2.5B 激活参数的 MoE 设计；**研究重点：显式思维链生成对代码/数学场景幻觉的抑制效果，以及推理时的自我修正机制**。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI \| 👍533 \| ⬇95,440 | 液态神经网络（Liquid Neural Network）架构，1B 激活的 MoE；**独特卖点：连续时间表示对长序列建模的理论优势，可探索其上下文外推能力与位置编码幻觉问题**。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb \| 👍774 \| ⬇100,575 | 端侧小模型标杆，1B 规模强调长上下文与高效推理；**适合研究极小模型的知识边界与"过度自信"幻觉的关联**。 |

---

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc \| 👍711 \| ⬇161,627 | "HRM"可能指 Human Reward Model 或特定领域，1B 规模的 text-generation 定位；**需验证：是否为人机对齐的轻量奖励模型或偏好数据训练的对话模型，适合低成本对齐研究复现**。 |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** | nvidia \| 👍143 \| ⬇47,285 | Nemotron 3 系列超大规模模型，55B 激活的 550B MoE；**Nemotron 系列以合成数据生成与奖励建模著称，研究其对齐数据 pipeline 对输出可靠性的提升机制**。 |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia \| 👍117 \| ⬇17,225 | NVFP4 量化版本；**研究极端量化对奖励模型/策略模型对齐稳定性的影响，涉及训练后量化的校准问题**。 |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia \| 👍197 \| ⬇1,015,381 | NVIDIA 优化的 Qwen3.6 MoE 量化版，百万级下载；**NVIDIA 的 ModelOpt 工具链暗示了系统化的训练后优化流程，可拆解其量化-对齐联合策略**。 |

> *本周未见显式的 DPO/RLHF 独立发布，但 Nemotron 系列与 DeepSeek-V4 的"Pro"后缀暗示了对齐优化的工程投入，社区微调（如 HauhauCS 的"Uncensored"）则提供了对齐移除的对照样本。*

---

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| *[无直接标注模型]* | — | 本周无显式"幻觉缓解"标签模型，但以下模型隐含相关技术： |
| → **Gemma-4 系列** | 见上 | any-to-any 架构的视觉 grounding 机制可能减少"虚构视觉内容"的幻觉类型 |
| → **Mellum2-Thinking** | 见上 | 显式思维链提供可解释的置信度估计路径 |
| → **Step-3.7-Flash** | 见上 | vision-language 的 rapid grounding 或采用 early-exit 置信度过滤 |

> *幻觉缓解研究需从架构设计（grounding）、推理机制（thinking）、后训练（alignment）三维度间接追踪，当前开源社区仍缺乏专门的"幻觉检测-校准"工具模型。*

---

### 🏗️ 研究基础设施（上述领域的训练框架、评测套件、数据集工具）

| 模型 | 作者/指标 | 一句话说明 |
|:---|:---|:---|
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)** | ByteDance \| 👍149 \| ⬇223 | 图像-文本到视频渲染模型，Apache-2.0 开源；**作为可控视频生成的研究基座，其跨模态条件对齐机制可迁移至文档到视频的理解任务，低下载量提示早期技术验证阶段**。 |
| **[nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano)** / **[Super](https://huggingface.co/nvidia/Cosmos3-Super)** / **[Super-Text2Image](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image)** / **[Super-Image2Video](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video)** | nvidia | Cosmos3 系列世界模型，覆盖文本/图像/视频的多模态生成；**"Omni"标签暗示统一生成框架，研究其 tokenizer 设计对跨模态一致性的保障，以及世界模型作为幻觉检测仿真环境的潜力**。 |
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia \| 👍219 \| ⬇1,380 | 流式 ASR 模型，cache-aware 设计；**语音-文本对齐的实时性要求与文档 OCR 的流式处理（如手写公式连续识别）存在技术迁移空间**。 |

---

## 研究生态信号

**模型家族势头**：Google Gemma-4 以"any-to-any"挑战 Qwen/GPT-4o 的多模态霸权，开源权重+统一架构将加速 VLM 的 grounding 幻觉研究；DeepSeek-V4 延续"高性能+开源"路线，其 MoE 长上下文设计或成为推理模型的新基线。NVIDIA 密集布局 LocateAnything、Cosmos3、Nemotron3 三线，显示"视觉理解-世界模拟-对齐生成"的全栈野心。**开源 vs 闭源**：Gemma-4、DeepSeek-V4 等核心权重完全开源，但最优实现（如 NVIDIA 的 NVFP4 优化）仍依赖硬件绑定；社区微调（HauhauCS、unsloth）活跃，形成"基座开源-生态分层"格局。**后训练活动**：显式对齐模型减少，但"Uncensored"类微调反向证明对齐的脆弱性；Nemotron 系列的合成数据 pipeline 若开源，将极大推动低成本幻觉缓解研究。OCR 领域 PaddleOCR-VL 独撑专业门面，通用 VLM 的文档能力边界亟待系统评测。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | **OCR/HMER 研究的核心标的**。ERNIE4.5 底座的 VL 架构升级，需深入分析其（1）数学公式识别的端到端 vs 两阶段策略、（2）复杂文档版面的阅读顺序推理、（3）与 Gemma-4 等通用 VLM 在文档任务上的能力差距，为专用模型存续性提供实证。 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | **长上下文推理与对齐研究的基座首选**。建议构建"长文档理解+多步推理"的幻觉评测基准，探测其（1）扩展上下文中的注意力稀释导致的逻辑断裂、（2）MoE 路由的专家一致性对输出稳定性的影响、（3）作为奖励模型训练数据的生成质量。 |
| ⭐⭐☆ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **多模态 grounding 与 OCR 的交叉创新点**。3B 规模的开放词汇定位能力，可尝试与 OCR 引擎级联构建"文本感知定位-识别"系统，研究视觉 grounding 的坐标精度对后续文本解码准确性的传递效应，以及联合训练对两类幻觉的协同抑制。 |

---

*日报基于 2026-06-07 Hugging Face Hub 公开数据编制。模型链接、点赞与下载数为时点快照，建议结合论文与模型卡获取完整技术细节。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*