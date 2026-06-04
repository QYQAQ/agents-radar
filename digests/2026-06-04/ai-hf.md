# Hugging Face 热门模型日报 2026-06-04

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-04 00:42 UTC

---

# Hugging Face 研究模型日报 | 2026-06-04

## 今日速览

本周 Hugging Face 生态呈现**多模态统一化**与**长上下文推理**双主线并进态势。Google Gemma-4 系列以"any-to-any"架构打破模态边界，标志着统一多模态模型进入实用阶段；PaddleOCR-VL-1.6 的发布显示 OCR 领域正从纯文本识别向视觉-语言深度融合演进，HMER 研究者可关注其公式理解能力。DeepSeek-V4 系列凭借 MoE 架构与极高下载量持续主导开源推理模型赛道，而 Step-3.7-Flash、Qwen3.6 等国产模型在视觉-语言对齐方面形成密集迭代。值得注意的是，"Thinking"类模型（如 Mellum2-Thinking）与 MTP（Multi-Token Prediction）变体的涌现，暗示 post-training 阶段的能力激发正成为差异化竞争焦点。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle / 213⭐ / 4,829↓ | 基于 ERNIE4.5 的 OCR 视觉语言模型，将传统 OCR 与文档理解统一为 image-text-to-text 范式，对 HMER 中公式结构解析与版面分析研究有直接参考价值。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 168⭐ / 463↓ | **any-to-any 统一架构**，原生支持图像-文本双向生成，为多模态推理研究提供开源基线，可探索其跨模态表征对齐机制与幻觉传播路径。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google / 112⭐ / 10↓ | Gemma-4 基座版本，适合研究统一多模态预训练策略，对比 it 版可分析指令微调对视觉 grounding 的影响。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 1,159⭐ / 78,925↓ | 定位-理解联合模型，feature-extraction 标签提示其视觉编码器可能具备细粒度空间感知，适用于视觉 grounding 与指代表达理解研究。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai / 231⭐ / 17,965↓ | 国产 vision-language MoE 模型，Flash 变体暗示效率优化，可研究其多模态 MoE 路由机制与视觉 token 压缩策略。 |
| **[stepfun-ai/Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)** | stepfun-ai / 102⭐ / 41,522↓ | 量化部署版本，高下载量反映边缘端多模态需求，适合研究模型压缩对视觉推理能力的保留度。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 1,346⭐ / 2,602,333↓ | **极高下载量的社区微调版**，"Aggressive"去对齐标签使其成为研究后训练移除安全约束对多模态幻觉影响的天然实验对象。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth / 629⭐ / 1,016,595↓ | MTP（Multi-Token Prediction）量化版，高下载量验证该训练目标在视觉-语言任务中的实用性，可探索 MTP 对多模态推理速度的增益。 |
| **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong / 209⭐ / 175,269↓ | 另一 MTP 变体，"Qwopus"暗示章鱼式多能力融合，适合对比不同社区实现的多模态 MTP 策略差异。 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research / 1,021⭐ / 3,309↓ | ByteDance 统一多模态生成模型（图像+视频），any-to-any 架构与 Gemma-4 形成开源-工业对照，可研究其模态桥接层设计。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation / 510⭐ / 18,315↓ | **video-text-to-text** 小模型，基于 Qwen3.5，为长视频理解研究提供轻量基线，可探索时序推理与幻觉的权衡。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 4,597⭐ / 5,811,046↓ | **本周最高点赞与下载**，MoE 架构的推理旗舰，其长上下文处理与数学推理能力为长文本 HMER 公式链式推导提供强基座。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai / 1,384⭐ / 3,542,202↓ | 高效推理变体，MIT 许可证与 eval-results 标签增强研究可复现性，适合长上下文效率-性能帕累托前沿研究。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains / 181⭐ / 6,938↓ | **显式"Thinking"标签**，JetBrains 代码模型引入推理时显式思考链，可研究结构化中间表示对长程依赖推理的增益。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI / 478⭐ / 60,171↓ | LFM（Liquid Foundation Model）系列，非 Transformer 架构（SSM 类），为长上下文建模提供替代路径，可对比注意力与状态空间在序列推理中的差异。 |
| **[LiquidAI/LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)** | LiquidAI / 174⭐ / 87,045↓ | 边缘部署版本，高下载量反映非 Transformer 长上下文架构的工业需求。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc / 545⭐ / 155,558↓ | HRM（Human Resource Model?）命名暗示特定领域优化，1B 规模适合研究小模型长上下文能力涌现条件。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 1,346⭐ / 2,602,333↓ | **对齐研究的"反面教材"**：激进移除安全对齐的社区微调版，其极高下载量揭示开源生态中"去 RLHF"趋势，可量化分析偏好模型移除对多模态诚实性的影响。 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains / 181⭐ / 6,938↓ | "Thinking"变体暗示推理时计算扩展作为对齐替代路径，可探索 test-time scaling 与 RLHF 的互补性。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 1,159⭐ / 78,925↓ | 显式定位机制可约束视觉注意力至真实图像区域，其 feature-extraction 设计可能包含空间置信度校准，适用于研究 grounding 作为幻觉缓解手段。 |
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle / 213⭐ / 4,829↓ | OCR 任务对事实准确性要求极高，其 ERNIE4.5 基座的视觉-语言对齐策略可为文档级幻觉缓解提供参考。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 4,597⭐ / 5,811,046↓ | 大规模 MoE 的推理一致性：可研究专家路由的确定性对输出稳定性的影响，以及长上下文中的事实漂移问题。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者/点赞/下载 | 研究相关性说明 |
|:---|:---|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia / 154⭐ / 470,059↓ | **NVFP4 量化格式**，NVIDIA Model Optimizer 官方实现，为长上下文模型的高效推理与评测提供标准化压缩基线，高下载量验证其工具价值。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth / 123⭐ / 0↓ | Unsloth 优化的 Gemma-4 GGUF，虽下载为零但代表统一多模态模型的边缘部署前沿，可跟踪其后续作为多模态 RAG 基础设施的潜力。 |

---

## 研究生态信号

**Qwen/Gemma 双寡头格局成型**：Qwen3.6 系列（含 NVFP4、MTP、Uncensored 等 5+ 变体）与 Gemma-4 的 any-to-any 架构形成开源多模态的两大技术路线——前者深耕 MoE 效率与社区微调生态，后者押注统一模态原生融合。国产模型（Step、DeepSeek、Qwen）在 vision-language 对齐上的密集迭代，正缩小与 GPT-4o 类的体验差距。值得关注的是，**"Uncensored-Aggressive"类模型的病毒式传播**（260 万下载）暴露开源对齐的脆弱性：RLHF/DPO 构建的安全边界可被轻易逆向，这要求幻觉缓解研究需从"训练时对齐"转向"推理时验证"与"可证明的 grounding"机制。OCR 领域 PaddleOCR-VL 的升级显示，传统文档理解正被 VLM 范式重构，HMER 研究者需警惕纯符号识别路线被端到端视觉推理取代的风险。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | **统一多模态基线的里程碑**：any-to-any 架构首次在 12B 规模验证模态完全统一的可行性，可直接用于探究（1）跨模态幻觉的传递机制、（2）视觉 token 与文本 token 的联合推理时扩展、（3）OCR/HMER 任务中端到端 vs 流水线架构的优劣对比。其开源权重允许拆解视觉编码器与语言核心的对齐层。 |
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | **OCR→文档 VLM 的范式迁移样本**：ERNIE4.5 基座与 image-text-to-text 任务的结合，使其成为研究"传统 OCR 后处理（版面分析、公式结构解析）能否被视觉-语言预训练隐式学习"的理想平台。建议对比其在复杂数学公式识别上与专用 HMER 模型（如 CAN、SATRN）的误差模式差异。 |
| ⭐⭐☆ | **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | **显式推理结构的对齐实验床**："Thinking"标签暗示模型输出包含结构化中间步骤，这为研究（1）推理链的忠实性（faithfulness）、（2）长程逻辑一致性验证、（3）推理时计算作为幻觉缓解手段提供了可控接口。代码领域的严谨性要求使其比通用对话模型更适合校准置信度研究。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*