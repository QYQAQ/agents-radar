# Hugging Face 热门模型日报 2026-06-03

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-03 00:42 UTC

---

# Hugging Face 研究模型日报 | 2026-06-03

---

## 今日速览

本周 Hugging Face 热门模型中，**OCR 与文档理解领域**迎来重要更新：PaddlePaddle 发布 PaddleOCR-VL-1.6，基于 ERNIE4.5 架构强化视觉文档推理能力。**多模态推理**持续升温，NVIDIA LocateAnything-3B 和字节 Lance 分别推进开放域视觉定位与任意模态生成；Qwen3.6 系列（27B/35B MoE）在视觉语言任务中保持高下载量，显示开源 VLM 生态活跃。**长上下文与推理**方面，DeepSeek-V4-Pro 以 4571 点赞领跑，JetBrains Mellum2-Thinking 聚焦代码推理的显式思维链设计。值得注意的是，**后训练对齐与幻觉缓解**的直接对应模型仍显稀缺，但 DeepSeek-V4-Flash 的 MIT 许可证和 eval-results 标签暗示开源社区对可复现对齐的重视正在提升。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 185 | 4,003 | 基于 ERNIE4.5 的视觉语言 OCR 模型，延续 PaddleOCR 系列在中文文档/公式/版面分析的优势；对 HMER（手写数学表达式识别）和复杂文档结构理解研究具有直接工具价值。 |

> *本周 OCR 专项模型仅 1 个上榜，但 PaddleOCR-VL 的 VL 化升级标志传统 OCR 框架向多模态文档理解的范式迁移，值得跟踪其公式识别与版面分析能力。*

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 962 | 61,604 | 开放域视觉定位模型，支持自然语言描述定位图像任意目标；对细粒度视觉语言对齐、指代表达理解与幻觉缓解研究有关键意义——定位精度直接关联 VLM 输出的空间事实性。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,275 | 2,573,320 | Qwen3.6 35B MoE 的激进去审查微调版，极高下载量反映社区对开源 VLM 可定制性的需求；**研究警示**：此类模型的"幻觉/安全幻觉"边界模糊化，为后训练对齐与价值校准研究提供反面案例与干预靶点。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 216 | 12,932 | 阶跃星辰轻量 VLM，聚焦高效视觉语言推理；其 Flash 版本暗示长上下文视觉序列的压缩处理，对长视频/长文档多模态理解有参考意义。 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 1,011 | 3,192 | 任意模态到任意模态（any-to-any）生成模型，统一处理图像/视频/文本的跨模态转换；为研究多模态表征对齐、模态间信息忠实度（幻觉缓解的核心维度）提供新架构范式。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 609 | 982,631 | Unsloth 优化的 Qwen3.6 27B 多模态思维预测（MTP）量化版，MTP 机制可显式建模视觉-语言推理的中间步骤，利于分析多模态推理链中的幻觉累积。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,577 | 5,243,648 | Qwen3.6 系列主力 VLM，开源权重+高下载量巩固其开源多模态基础设施地位；适合作为多模态幻觉评测、长上下文视觉理解的对照基线。 |
| **[Kwai-Keye/Keye-VL-2.0-30B-A3B](https://huggingface.co/Kwai-Keye/Keye-VL-2.0-30B-A3B)** | Kwai-Keye | 99 | 964 | 快手 KeyeVL2 系列 30B MoE，强调特征提取效率；低下载但技术标签明确，适合研究工业界 VLM 的稀疏激活与视觉编码器设计。 |
| **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong | 196 | 155,959 | 社区 MTP 量化衍生版，验证 Qwen3.6 MTP 架构的可迁移性；适合边缘部署场景下的多模态推理一致性研究。 |
| **[stepfun-ai/Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)** | stepfun-ai | 95 | 39,258 | Step-3.7-Flash 的 llama.cpp 量化版，MoE 结构的边缘部署尝试；研究 MoE 路由稳定性与量化误差的交叉影响。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,571 | 5,829,042 | DeepSeek V4 专业版，开源权重+极高社区热度；其长上下文能力与推理效率为长文本数学证明、代码推理等需要扩展上下文窗口的研究提供顶级基线。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,364 | 3,525,218 | V4 轻量版，MIT 许可证+公开 eval-results；开源友好的许可与评测透明性使其成为可复现的长上下文推理与后训练对齐研究的理想平台。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 440 | 47,742 | 液态神经网络（Liquid Neural Network）MoE 架构，8B 激活 1B；非 Transformer 的长程依赖建模机制为超越注意力瓶颈的上下文扩展研究提供独特视角。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 127 | 799 | JetBrains 代码模型显式思维版，12B 激活 2.5B；Thinking 标签表明链式思维显式化设计，适合研究代码生成中的推理忠实度与"过度思考"型幻觉。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb | 734 | 57,683 | MiniCPM 系列第五代 1B 小模型，端侧长文本能力持续迭代；小参数规模下的长上下文压缩技术对资源受限场景的推理研究有直接价值。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 469 | 153,029 | HRM（Human Resource Management?）文本模型，标签信息有限但下载活跃；需验证其是否涉及结构化长文档理解或特定领域推理。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 494 | 17,616 | 视频-文本到文本模型，基于 Qwen3.5 架构；视频时序理解天然需要长上下文建模，其 2B 规模的效率设计适合长视频推理的轻量研究。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[openai/privacy-filter](https://huggingface.co/openai/privacy-filter)** | openai | 1,593 | 300,247 | OpenAI 发布的隐私信息 token 分类过滤器，transformers.js 支持；虽非传统对齐模型，但其**基于分类的后训练干预机制**（识别并处理敏感 token）与 RLHF 安全层的训练逻辑同源，为可控生成研究提供轻量参考实现。 |

> *本周直接标注 RLHF/DPO/SFT 的模型稀缺，但以下模型隐含对齐信号：DeepSeek-V4-Flash 的 eval-results 标签暗示评测驱动的迭代；HauhauCS 的"Uncensored-Aggressive"微调反向证明价值对齐的必要性；Qwen3.6 MTP 的思维预测机制可视为推理阶段的对齐干预。*

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| *[间接相关] 见多模态与推理类别* | — | — | — | 本周无直接标注"幻觉缓解"的专项模型，但 **LocateAnything-3B** 的空间 grounding 能力、**Lance** 的跨模态忠实度、**MTP 系列** 的显式思维链均为幻觉研究的关键技术路径。 |

> **研究空白提示**：社区对"幻觉缓解"作为独立发布标签的重视不足，该领域仍多依附于 VLM/LLM 的附属能力。建议关注 **PaddleOCR-VL-1.6** 的文档事实性、**DeepSeek-V4-Flash** 的评测透明度作为间接切入点。

---

### 🏗️ 研究基础设施

| 模型/工具 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 137 | 313,480 | NVIDIA ModelOpt 优化的 NVFP4 量化版 Qwen3.6 MoE；为大规模 VLM 的高效推理与对齐训练提供压缩基础设施，降低幻觉评测与长上下文实验的计算门槛。 |
| **[nvidia/PiD](https://huggingface.co/nvidia/PiD)** | nvidia | 263 | 646 | 扩散超分辨率模型，图像到图像；虽非核心研究方向，但其感知质量优化技术可迁移至文档图像增强，提升 OCR/VLM 的输入质量从而间接缓解感知幻觉。 |
| **[nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano)** / **[Super](https://huggingface.co/nvidia/Cosmos3-Super)** / **[Super-Image2Video](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video)** / **[Super-Text2Image](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image)** | nvidia | 97-109 | 517-9,071 | NVIDIA Cosmos3 系列多模态生成基础设施，覆盖文本/图像/视频的全向（omni）生成；为研究生成式多模态模型的幻觉（生成事实性、时序一致性）提供可控实验平台。 |
| **[LiquidAI/LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)** | LiquidAI | 160 | 70,865 | LFM2.5 的 llama.cpp 边缘部署版；液态神经网络的边缘适配为研究非标准架构的端侧对齐与推理稳定性提供独特环境。 |
| **[prism-ml/bonsai-image-ternary-4B-gemlite-2bit](https://huggingface.co/prism-ml/bonsai-image-ternary-4B-gemlite-2bit)** | prism-ml | 100 | 41 | 三值/1.58-bit 极端量化文本到图像模型；极低比特下的生成质量与幻觉控制为模型压缩与保真度的权衡研究提供极限案例。 |

---

## 研究生态信号

**Qwen3.6 家族**本周以 4 个变体（官方 27B、MTP-GGUF、NVFP4、社区 Uncensored/ MTP 衍生）占据多模态基础设施核心，其 **MTP（Multi-Token Prediction）** 机制正成为开源社区显式化推理过程的事实标准，这对幻觉的可解释性研究是积极信号。**DeepSeek-V4** 双版本（Pro/Flash）以 MIT 许可证+公开评测巩固开源长上下文推理的领导力，与 Step-3.7、KeyeVL 等闭源/半开放工业模型形成对照。OCR 领域 **PaddleOCR-VL** 的 ERNIE4.5 升级显示中文文档理解的技术自主性，但国际关注度（185 点赞）远低于生成模型，反映文档理解的"基础设施化"认知——必要但缺乏光环。**幻觉缓解的直接研究工具仍稀缺**，社区更多通过 grounding（LocateAnything）、思维链显式化（MTP/Thinking）、评测透明（eval-results）间接逼近，专项的"事实校准"或"RAG 增强"模型未见上榜，提示该方向的开源产品化仍有缺口。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **视觉 grounding 是幻觉缓解的前置技术**。开放域任意目标定位能力可直接用于 VLM 输出的空间事实性验证（"模型说图中左侧有猫，定位模块能否支持？"），建议探索其与 Qwen3.6/DeepSeek-V4 的级联架构，构建"生成-定位-校验"的闭环幻觉检测系统。 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | **MIT 许可证 + eval-results 标签 = 可复现对齐研究的理想载体**。相比 Pro 版，Flash 的轻量性适合长上下文场景下的 RLHF/DPO 迭代实验，公开评测结果便于建立幻觉/事实性基准；建议以其为基座，构建领域特定的后训练对齐数据集（如科学文献、法律文档的长文本忠实度）。 |
| ⭐⭐☆ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | **HMER 与复杂文档理解的直接工具升级**。ERNIE4.5 架构的 VL 化值得验证其在手写公式、表格结构、多栏版面等经典 OCR 难题上的进步；建议与 Qwen3.6-VL 进行文档理解的事实性对比（如"模型是否正确提取了表格第三行的数值？"），量化 OCR 错误向 VLM 幻觉的传导效应。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*