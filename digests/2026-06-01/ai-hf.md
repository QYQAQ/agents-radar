# Hugging Face 热门模型日报 2026-06-01

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-01 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-01

## 今日速览

今日 Hugging Face 生态中，**Qwen3.6 系列**持续主导多模态与长上下文赛道，旗舰模型 `Qwen3.6-27B` 与 MoE 变体 `35B-A3B` 合计下载量突破 700 万，显示其在视觉语言任务中的基础设施地位。OCR 领域迎来 **PaddleOCR-VL-1.6** 的重要迭代，基于 ERNIE4.5 架构强化文档级理解能力。字节跳动的 **Lance** 以 any-to-any 架构引发关注，或将成为统一多模态建模的新范式。值得关注的是，后训练对齐领域出现分化：社区微调版本（如 Uncensored 变体）下载量极高，但幻觉缓解的专门化模型仍显稀缺，暗示该方向存在研究空白。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 / 数据 | 说明 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle / ⭐117 / 📥2,731 | 基于 ERNIE4.5 的视觉语言 OCR 模型，升级文档级文本识别与版面分析能力，为 HMER（手写数学表达式识别）与复杂文档理解提供新的开源基线。 |

### 🎭 多模态与视觉语言

| 模型 | 作者 / 数据 | 说明 |
|:---|:---|:---|
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen / ⭐1,552 / 📥5,064,096 | Qwen3.6 系列核心视觉语言模型，支持图像-文本交错输入，在多模态推理基准上表现稳健，是 VLM 研究的必备参照基线。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb / ⭐1,082 / 📥444,679 | MiniCPM 系列最新迭代，以端侧友好参数规模实现高分辨率图像理解，为高效 VLM 架构与视觉编码器优化研究提供关键对比点。 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research / ⭐992 / 📥2,948 | 原生 any-to-any 架构模型，统一处理图像/视频/文本生成与理解，可能挑战现有"拼接式"多模态范式，值得跟踪其模态对齐机制。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind / ⭐208 / 📥57,248 | 基于 Qwen3.5 的视觉信息抽取模型，聚焦结构化文档解析，与 OCR 后处理流水线高度相关。 |
| **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** | Jackrong / ⭐190 / 📥37,241 | Qwen3.6 社区量化版本，支持 llama.cpp 部署，为资源受限场景下的多模态推理实验提供可行路径。 |

### 🧠 长上下文与推理模型

| 模型 | 作者 / 数据 | 说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / ⭐4,497 / 📥5,886,599 | DeepSeek-V4 专业版，以 MoE 架构实现超长上下文与复杂推理能力，是当前长上下文建模与推理效率研究的最重要开源模型之一。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai / ⭐1,319 / 📥3,483,641 | V4 系列的轻量推理优化版本，MIT 许可证开放，为推理加速与上下文压缩技术的对比实验提供便利。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth / ⭐578 / 📥926,440 | 集成 Multi-Token Prediction 的量化版本，MTP 机制对长序列生成效率的增益值得专门研究。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation / ⭐468 / 📥16,277 | 视频-文本理解模型，基于 Qwen3.5 扩展时序建模，是长上下文向视频维度延伸的探索样本。 |

### 🔧 Post-Training 与对齐

| 模型 | 作者 / 数据 | 说明 |
|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / ⭐1,156 / 📥2,439,402 | Qwen3.6 MoE 的激进去对齐化微调版本，异常高的下载量反映社区对"反向对齐"的需求，可作为对齐鲁棒性与安全机制研究的负面样本。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI / ⭐321 / 📥27,677 | Liquid 架构的 MoE 模型，声称优化了训练动态与收敛特性，其非 Transformer 架构的对齐行为值得独立验证。 |

### 👁️ 幻觉缓解

*本日榜单中未出现明确标注幻觉缓解或事实 grounding 的专门化模型，该方向存在显著的研究发布缺口。*

### 🏗️ 研究基础设施

| 模型 | 作者 / 数据 | 说明 |
|:---|:---|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia / ⭐92 / 📥105,608 | NVIDIA ModelOpt 优化的 FP4 量化版本，为大规模 VLM/MoE 的高效推理与显存优化提供工程基准。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric / ⭐467 / 📥0 | Qwen 系列对话模板的社区修正版本，提示模板工程是对齐质量与幻觉行为的隐性影响因素，此类工具对可复现研究至关重要。 |

---

## 研究生态信号

**Qwen3.6 与 DeepSeek-V4 形成双寡头格局**，两者合计占据多模态与长上下文领域的核心生态位，但技术路线分化明显：Qwen 侧重视觉-语言融合与端侧部署，DeepSeek 专注推理深度与上下文长度。值得注意的是，**"Uncensored" 类社区微调模型下载量达官方模型的 48%**（HauhauCS 版本 vs Qwen 官方），暗示现有对齐技术存在显著的可绕过性，或对幻觉缓解研究提出反向挑战。OCR 领域 PaddleOCR-VL 的 ERNIE4.5 升级显示**文档理解正从纯文本识别向视觉语言预训练迁移**，HMER 任务或需重新评估基线。开源权重在 VLM 领域已确立主导，但 any-to-any 架构（Lance）与视频理解（Marlin）仍处早期，存在方法论创新的窗口期。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔴 高** | **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | any-to-any 架构若经验证有效，将重塑多模态对齐的研究框架——无需为各模态组合单独设计投影层，统一训练目标可能缓解模态间的幻觉传播。建议优先测试其跨模态一致性（如图像描述与视频描述的 factual grounding 差异）。 |
| **🟡 高** | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | ERNIE4.5 基座的文档理解能力尚未经社区充分评测，其在复杂公式、表格结构、手写混合场景的表现可直接补充 HMER 研究的数据点，且与 Qwen3.6-VL 形成有价值的中文文档理解对比。 |
| **🟢 中** | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | 作为"对齐失败"的大规模样本，可通过系统对比其与官方 Qwen3.6 的幻觉率、知识边界与置信度校准行为，量化现有 RLHF/DPO 技术的实际效用边界，为更鲁棒的对齐目标函数设计提供实证动机。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*