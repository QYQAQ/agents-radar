# Hugging Face 热门模型日报 2026-06-08

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-08 00:36 UTC

---

# Hugging Face 研究模型日报 | 2026-06-08

## 今日速览

本周 Hugging Face 生态呈现**多模态统一架构加速收敛**与**OCR-文档理解深度整合**两大趋势。Google Gemma-4 系列以 any-to-any 架构强势入局，原生支持图文交错输入输出；PaddleOCR-VL-1.6 标志传统 OCR 工具链向视觉语言范式跃迁。DeepSeek-V4 系列延续 MoE 架构优势，V4-Pro 与 V4-Flash 分别占据推理质量与效率两极。NVIDIA 密集发布 LocateAnything-3B 空间定位模型及 Cosmos3 多模态生成家族，显示其在视觉 grounding 与物理世界建模的雄心。值得注意的是，"Uncensored" 微调模型（如 HauhauCS/Qwen3.6-35B-A3B-Uncensored）下载量异常高企，反映社区对后训练对齐策略透明度的迫切需求。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6) | PaddlePaddle | 266 | 9,084 | **OCR 向视觉语言范式演进的关键节点**：基于 ERNIE4.5 的端到端文档理解模型，将传统 OCR 检测-识别-理解的三段式流程压缩为统一 VL 推理，对 HMER（手写数学表达式识别）和复杂版面分析研究具有直接参考价值。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 1,523 | 115,556 | **空间定位与视觉 grounding 的轻量级突破**：3B 参数实现开放词汇图像定位，支持任意描述指向图像区域，为多模态推理中的视觉引用机制（visual referring）和幻觉缓解的 spatial grounding 验证提供新基线。 |
| [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | google | 687 | 434,969 | **原生 any-to-any 多模态架构**：Gemma-4 统一处理文本、图像、视频输入与交错输出，其 12B 规模在效率-能力权衡点上极具研究价值，尤其适合作为多模态对齐与指令遵循的实验平台。 |
| [google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B) | google | 410 | 99,655 | **any-to-any 基座模型**：与 it 版本形成对照组，便于研究 SFT/RLHF 对多模态对齐的具体影响，是 post-training 方法学的理想载体。 |
| [unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF) | unsloth | 449 | 568,158 | **Gemma-4 的高效推理变体**：GGUF 量化版本下载量反超原版，反映社区对边缘部署多模态模型的强烈需求，为量化对多模态幻觉影响的实证研究提供素材。 |
| [stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) | stepfun-ai | 348 | 43,196 | **国产高效视觉语言模型**：Step 系列在中文场景文档理解表现突出，其 Flash 变体的推理效率优化策略值得与 Gemma-4、Qwen-VL 系列进行跨架构对比。 |
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 1,521 | 2,923,564 | **"去对齐"模型的极端案例**：下载量登顶揭示社区对安全对齐机制的反弹，其"Aggressive"去毒策略可作为反向样本，研究过度/不足对齐对多模态幻觉的双向影响。 |
| [unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF) | unsloth | 120 | 85,842 | **QAT 量化多模态模型**：量化感知训练保留的 any-to-any 能力，为研究低精度推理对跨模态对齐稳定性的影响提供可控实验条件。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking) | JetBrains | 249 | 16,924 | **显式推理链的代码智能模型**："Thinking" 标签表明其内置 Chain-of-Thought 机制，12B 激活 2.5B 的 MoE 架构在代码长上下文推理中的效率表现，对推理-计算权衡研究具有启发。 |
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,696 | 5,515,325 | **MoE 推理巅峰**：V4 系列延续 DeepSeek 在数学与代码推理的统治力，其 550B 总量/55B 激活的极端稀疏设计，为长上下文推理的 KV Cache 优化与专家路由机制研究提供顶级基准。 |
| [deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | deepseek-ai | 1,434 | 3,347,429 | **高效推理变体的架构创新**：与 Pro 版本形成完整谱系，其 Flash 版本的推测解码或蒸馏策略值得拆解，对推理加速中的幻觉控制机制有独立研究价值。 |
| [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) | LiquidAI | 540 | 118,326 | **液态神经网络架构的 MoE 演进**：非 Transformer 架构（液态/状态空间）与 MoE 的结合，为长上下文建模的替代路径提供实证，其 1B 激活参数的效率声称需经长序列基准检验。 |
| [openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B) | openbmb | 779 | 114,329 | **端侧长上下文极致压缩**：1B 规模声称实现超越参数量的长文本能力，其 MiniCPM 系列的端侧优化技术对边缘设备上的文档级 OCR 理解场景有直接应用价值。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B) | sapientinc | 718 | 162,822 | **人力资源领域的垂直对齐模型**：特定领域（HRM）的 post-training 对齐案例，其领域适应方法（可能是 DPO 或 RLHF 变体）可作为研究垂直领域对齐与通用能力保持权衡的样本。 |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | nvidia | 156 | 49,784 | **Nemotron 对齐 pipeline 的旗舰输出**：NVIDIA 开源的完整 post-training 流程（含合成数据生成）的产物，其对齐方法论（HelpSteer 等）是研究工业级 RLHF 实现的重要参考。 |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4) | nvidia | 131 | 39,864 | **NVFP4 量化对齐模型**：与 BF16 版本对照，可研究量化对对齐后模型偏好稳定性的影响，是 post-training 与模型压缩交叉领域的实验素材。 |
| [nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | nvidia | 200 | 1,185,362 | **NVIDIA ModelOpt 优化的 MoE 模型**：官方量化工具链与 Qwen MoE 的结合，其优化后的对齐表现（如 MT-Bench 稳定性）可评估硬件-算法协同优化的边界。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 1,523 | 115,556 | **视觉 grounding 作为幻觉缓解工具**：通过显式空间定位约束生成内容，其 "locate-then-verify" 机制可直接嵌入 VLM 的幻觉检测流程，是 grounding for hallucination reduction 的前沿实践。 |
| [PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6) | PaddlePaddle | 266 | 9,084 | **OCR 结果的视觉可验证性**：端到端架构减少传统 OCR 级联错误，其 ERNIE4.5 基座的文档级理解能力可降低"识别正确但理解错误"的语义幻觉。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [nvidia/Cosmos3-Nano](https://huggingface.co/nvidia/Cosmos3-Nano) / [Cosmos3-Super](https://huggingface.co/nvidia/Cosmos3-Super) / [Cosmos3-Super-Text2Image](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image) / [Cosmos3-Super-Image2Video](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video) | nvidia | 193/153/123/114 | 29,697/24,002/5,075/4,515 | **物理世界多模态生成的开源基础设施**：Cosmos3 家族覆盖文本-图像-视频-3D 的全模态生成，其 Nano/Super 分级为研究者提供可控规模的物理一致性评测平台，对多模态幻觉的"物理合理性"维度评估具有独特价值。 |
| [nvidia/PiD](https://huggingface.co/nvidia/PiD) | nvidia | 317 | 1,082 | **扩散模型超分辨率工具**：作为图像生成后处理的基础设施，其保真度增强能力可嵌入多模态生成 pipeline 的幻觉缓解环节。 |

---

## 研究生态信号

**Gemma-4 与 Qwen3.6 形成开源多模态双极格局**：Google 以 any-to-any 统一架构挑战 GPT-4o 的封闭生态，而 Qwen 系列通过活跃的社区微调（含争议性的"Uncensored"变体）维持高频迭代。OCR 领域出现**工具链范式转移**——PaddleOCR-VL 标志从"检测-识别-NLU"流水线向端到端视觉语言的跃迁，这对 HMER 等需精细结构理解的子领域提出新方法论命题。后训练对齐呈现**硬件-算法深度耦合**趋势：NVIDIA 以 Nemotron + ModelOpt + NVFP4 构建全栈开源方案，将量化、对齐、推理优化打包为可复现流程。值得警惕的是，"Uncensored"模型下载量与点赞数的倒挂（HauhauCS 模型下载 292 万但点赞 1521，低于 LocateAnything-3B 的 15.2 万下载/1523 点赞），暗示**对齐研究存在显著的发表-应用鸿沟**，社区对安全机制的实用性质疑亟待学理回应。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | **幻觉缓解的方法论突破**：将视觉 grounding 从"能力"转化为"验证机制"。研究者可探索将其空间定位输出作为 VLM 生成内容的忠实度检验器，构建 "grounding-based hallucination detector"，解决当前 VLM 幻觉评估缺乏细粒度视觉证据的核心痛点。其 3B 规模亦便于在学术资源下复现与扩展。 |
| ⭐⭐⭐ | [PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6) | **OCR/HMER 的范式转型样本**：传统 OCR 工具链（检测→识别→版面分析→语义理解）的端到端替代方案。研究者可对比其在复杂数学公式、手写混合文档上的结构保持能力，验证"统一 VL 推理是否优于模块化专家级联"这一核心命题，对 HMER 领域的模型架构选择具有直接决策参考价值。 |
| ⭐⭐☆ | [JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking) | **推理效率与可解释性的平衡实验**：显式 "Thinking" 机制与 MoE 稀疏激活的结合，为研究"推理过程透明度"与"计算成本"的帕累托前沿提供独特样本。特别适合探索：长代码上下文中的 CoT 忠实度、专家路由模式与推理步骤的关联性，以及推理链长度对最终答案幻觉率的影响。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*