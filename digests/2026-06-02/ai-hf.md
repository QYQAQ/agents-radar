# Hugging Face 热门模型日报 2026-06-02

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-02 00:37 UTC

---

# Hugging Face 研究模型日报 | 2026-06-02

---

## 今日速览

今日 Hugging Face 热门模型中，**OCR/文档理解**领域迎来 PaddlePaddle 的 `PaddleOCR-VL-1.6` 更新，基于 ERNIE4.5 架构强化了视觉-语言文档理解能力。**多模态推理**方面，Qwen3.6 系列持续扩张，27B 基础版与 35B MoE 版双双上榜，nvidia 推出的 NVFP4 量化版本值得关注。长上下文与推理模型中，`DeepSeek-V4-Pro` 以 4530 点赞领跑，MIT 许可证的 `DeepSeek-V4-Flash` 下载量突破 350 万，显示开源推理模型的强劲势头。值得注意的是，**幻觉缓解与对齐**相关显式标签模型仍较少，但 `openai/privacy-filter` 的 token-classification 架构为事实 grounding 提供了基础设施思路。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle / 👍156 / ⬇3,190 | 基于 ERNIE4.5 的视觉-语言 OCR 模型，延续 PaddleOCR 系列在中文文档理解的优势；**HMER 研究者可关注其公式-文本混合版面解析能力及视觉编码器与文本解码器的对齐机制**。 |

### 🎭 多模态与视觉语言

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen / 👍1,567 / ⬇5,154,729 | Qwen3.6 系列核心 VLM，支持 image-text-to-text 对话；**多模态推理研究者可深入分析其视觉-语言对齐策略及跨模态幻觉模式**。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb / 👍1,088 / ⬇459,188 | MiniCPM 系列最新 VLM，以端侧高效部署为卖点；**适合研究轻量化多模态架构中的信息瓶颈与幻觉压缩问题**。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 👍792 / ⬇35,783 | 定位-理解联合的 3B 视觉语言模型；**空间推理与视觉 grounding 研究的重要基线，可延伸至文档元素定位任务**。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth / 👍593 / ⬇952,188 | Unsloth 优化的 Qwen3.6 多 token 预测量化版；**MTP 机制对多模态序列生成的加速效果值得 ablation 研究**。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai / 👍191 / ⬇9,256 | 阶跃星辰的轻量 VLM；**需关注其训练数据构成与后对齐方法，评估中文场景下的幻觉率**。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind / 👍215 / ⬇59,010 | 基于 Qwen3.5 的视觉信息抽取模型；**文档结构化抽取任务中，可研究其视觉感知与结构化输出的对齐质量**。 |
| **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong / 👍183 / ⬇139,952 | 社区 MTP 量化版本；**开源后训练变体为研究量化对多模态推理损伤提供了实验素材**。 |
| **[stepfun-ai/Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)** | stepfun-ai / 👍84 / ⬇37,533 | Step-3.7 的 llama.cpp 适配版；**边缘部署场景下幻觉行为的系统性评测尚属空白**。 |
| **[Kwai-Keye/Keye-VL-2.0-30B-A3B](https://huggingface.co/Kwai-Keye/Keye-VL-2.0-30B-A3B)** | Kwai-Keye / 👍88 / ⬇784 | 快手 KeyeVL2 系列 MoE VLM；**30B-A3B 的稀疏激活架构对长视频-文档理解的效率-效果权衡具研究价值**。 |

### 🧠 长上下文与推理模型

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 👍4,530 / ⬇5,851,826 | DeepSeek V4 旗舰推理模型，本周点赞冠军；**长上下文推理研究需重点分析其上下文压缩机制与远距离依赖保持策略**。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai / 👍1,341 / ⬇3,511,636 | MIT 许可证的轻量推理版；**开源许可使其成为长上下文对齐与幻觉评测的理想可控基线**。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI / 👍391 / ⬇37,893 | 液态神经网络架构的 8B MoE 模型；**非 Transformer 架构的长序列建模能力对上下文扩展研究具范式意义**。 |
| **[LiquidAI/LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)** | LiquidAI / 👍143 / ⬇55,212 | LFM2.5 的 GGUF 量化版；**液态神经元的量化鲁棒性与长上下文稳定性尚未被充分研究**。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 👍1,218 / ⬇2,533,393 | 高下载量的"去审查"社区微调版；**极端后训练干预对多模态安全对齐与幻觉边界的影响值得批判性研究**。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb / 👍689 / ⬇45,698 | 超轻量 1B 文本模型；**极小规模下的长上下文外推能力可作为效率研究的极端案例**。 |

### 🔧 Post-Training 与对齐

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[openai/privacy-filter](https://huggingface.co/openai/privacy-filter)** | openai / 👍1,578 / ⬇316,092 | 基于 token-classification 的隐私信息检测过滤器；**其分类头架构与置信度校准机制可直接迁移至事实性检测的对齐层设计**。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc / 👍439 / ⬇149,543 | 人力资源领域的专用文本模型；**垂直领域 SFT 中的偏好数据构建与领域幻觉抑制策略具借鉴价值**。 |

### 👁️ 幻觉缓解

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| *（本日无显式标注幻觉缓解的模型，以下为间接相关）* | | |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research / 👍1,002 / ⬇3,041 | 统一多模态生成模型（any-to-any）；**跨模态生成中的自洽性约束机制可作为幻觉缓解的生成式验证基线**。 |

### 🏗️ 研究基础设施

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia / 👍121 / ⬇171,588 | NVIDIA ModelOpt 优化的 NVFP4 量化版；**极低精度量化对 VLM 注意力模式与幻觉敏感性的影响需系统性基准测试**。 |
| **[prism-ml/bonsai-image-ternary-4B-gemlite-2bit](https://huggingface.co/prism-ml/bonsai-image-ternary-4bit-gemlite-2bit)** | prism-ml / 👍89 / ⬇0 | 三值/1.58-bit 图像生成模型；**极端量化下的生成忠实度可作为幻觉缓解的"压力测试"环境**。 |

---

## 研究生态信号

**Qwen 生态持续主导多模态开源格局**：Qwen3.6 系列在 30 个热门模型中占据 5 席（含社区衍生版），覆盖 27B 密集、35B MoE、MTP 变体及多种量化格式，形成完整研究矩阵。**DeepSeek V4 双版本策略**（Pro/Flash）以 MIT 许可证打破开源-闭源边界，Flash 版 351 万下载量表明研究社区对可控基线的强烈需求。OCR 领域 PaddleOCR-VL 的 ERNIE4.5 升级显示**文档理解正向通用 VLM 架构收敛**，专用 OCR 模型与通用 VLM 的能力边界模糊化。值得关注的是，**显式标注"幻觉缓解"或"对齐"的模型仍属稀缺**，相关研究多隐含于 VLM 发布中，社区尚未形成标准化评测共识；HauhauCS 的"激进去审查"版高下载量（253 万）反向提示**安全对齐与性能释放的张力已成为后训练研究的核心矛盾**。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | 当前列表中唯一明确聚焦文档视觉-语言理解的模型。基于 ERNIE4.5 的架构升级使其成为 HMER 与版面分析研究的最新基线；建议重点评测其在数学公式、表格结构、手写体混合场景中的**跨模态对齐精度**与**结构化输出幻觉率**。 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | MIT 许可证 + 351 万下载量 = 当前最可及的高性能推理基线。建议设计**长上下文事实保持评测协议**（如 distant claim verification），探究其 Flash 架构（推测为蒸馏或稀疏变体）在扩展上下文中的**注意力漂移模式**与**校准误差累积**。 |
| ⭐⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | 3B 规模的定位-理解联合模型为**高效视觉 grounding** 提供了研究窗口。建议将其视觉定位机制迁移至文档领域，评估"指代消解"能力对**OCR 结果的空间校正**与**版面元素关系推理**的增益，同时检验小尺度 VLM 的幻觉边界。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*