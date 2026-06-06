# Hugging Face 热门模型日报 2026-06-06

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-06 00:33 UTC

---

# Hugging Face 研究模型日报 | 2026-06-06

---

## 今日速览

本周 Hugging Face 热门模型中，**OCR/文档理解**领域迎来重要更新：PaddlePaddle 发布 PaddleOCR-VL-1.6，基于 ERNIE4.5 架构强化视觉文档理解能力。**多模态推理**方面，Google Gemma-4 系列以 any-to-any 架构实现统一模态处理，NVIDIA LocateAnything-3B 聚焦开放域视觉定位。长上下文与推理模型持续活跃，DeepSeek-V4-Pro 以 4657 点赞领跑，其 MoE 架构与推理优化值得关注。后训练对齐领域可见 Qwen3.6 衍生模型的高度活跃，Unsloth 量化版本下载量破百万，反映社区对高效部署对齐模型的强烈需求。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle | 245 | 6,881 | 基于 ERNIE4.5 的视觉语言 OCR 模型，整合文本识别与文档理解，与 HMER/文档版面分析研究直接相关，ERNIE 系列在中文文档场景有成熟生态 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,375 | 101,823 | 开放域视觉定位模型，支持任意目标的自然语言指代定位，与多模态推理中的细粒度视觉-语言对齐研究高度相关 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 545 | 142,851 | Google 统一 any-to-any 架构的指令微调版本，原生支持图像-文本-音频跨模态输入输出，是研究统一多模态表征的重要基线 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 336 | 53,525 | Gemma-4 基础版本，any-to-any 统一架构为研究模态融合与解耦机制提供开源权重 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth | 374 | 296,410 | Gemma-4 的高性能量化版本，下载量领先反映社区对可部署多模态模型的需求，适合端侧多模态推理研究 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai | 332 | 27,948 | 阶跃星辰视觉语言模型，专注高效推理，适合研究视觉语言模型的速度-精度权衡 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,451 | 2,687,304 | **本周下载量冠军**，Qwen3.6 MoE 视觉模型的激进去对齐版本，点赞与下载反差揭示社区对" uncensored "多模态模型的复杂态度，是对齐研究的负面案例样本 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | unsloth | 665 | 1,092,323 | Qwen3.6 多 token 预测量化版，MTP 机制可提升多模态序列生成效率，适合研究视觉语言生成的解码优化 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | **4,657** | **5,562,821** | **双料冠军**，DeepSeek V4 专业版，MoE 架构结合深度推理优化，是研究长上下文推理与高效推理机制的核心基线 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai | 1,412 | 3,473,265 | V4 轻量高速版本，MIT 许可证更开放，适合研究推理模型的蒸馏与高效化 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** | LiquidAI | 526 | 82,709 | 液态神经网络 MoE 架构，非 Transformer 的长上下文建模新路径，对研究替代架构的上下文外推能力有启发 |
| **[JetBrains/Mellum2-12B-A2.5B-Thinking](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking)** | JetBrains | 224 | 14,709 | JetBrains 代码推理模型，显式"Thinking"模式支持长链推理，适合研究代码域的推理过程监督 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb | 770 | 91,235 | 端侧小模型新标杆，1B 参数级别实现可用推理能力，是研究模型压缩与推理保留的重要参考 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,451 | 2,687,304 | 激进去对齐的社区微调版，点赞高但下载量异常突出，反映对齐"逆向工程"的地下需求，是对齐鲁棒性研究的反面教材 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 702 | 159,014 | 专注人力资源管理的对齐模型，垂直领域 SFT 案例，适合研究任务特定对齐的泛化边界 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,375 | 101,823 | 视觉定位任务天然要求输出与图像像素严格对齐，其定位-描述联合训练机制可为视觉幻觉缓解提供思路 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 545 | 142,851 | any-to-any 架构的模态双向绑定设计，理论上可减少单模态幻觉，适合研究跨模态事实一致性 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 191 | 822,125 | NVIDIA ModelOpt 优化的 NVFP4 量化格式，下载量高，是研究后训练量化与部署工具链的关键参考 |
| **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)** / **[NVFP4版](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)** | nvidia | 117 / 107 | 9,125 / 7,419 | Nemotron 3 Ultra 550B/55B 激活的 MoE 巨模型，NVIDIA 官方后训练优化版本，适合研究超大规模模型的对齐与效率 |

---

## 研究生态信号

**Qwen 家族主导开源多模态生态**：Qwen3.6 系列衍生模型（Unsloth 量化、NVIDIA 优化、社区微调）占据下载量前列，表明其已成为事实上的开源多模态基座。Gemma-4 的 any-to-any 统一架构代表 Google 的技术路线，但社区采用度尚不及 Qwen。**视觉语言模型的"对齐张力"凸显**：HauhauCS 的"Uncensored"版本下载量远超官方版本，揭示开源对齐的脆弱性——后训练对齐易被逆向，这对幻觉缓解研究提出新挑战：如何构建更鲁棒的对齐机制？**OCR/文档领域相对沉寂**：PaddleOCR-VL-1.6 是唯一专注文档的模型，且下载量偏低，说明视觉文档理解尚未进入主流多模态竞赛，存在研究空白。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | 唯一专注 OCR/文档理解的模型，ERNIE4.5 架构在中文文档场景有独特优势。建议研究其视觉编码器与文本解码器的交互机制，对比 Qwen-VL、Gemma-4 在公式识别、版面分析等 HMER 任务上的表现，填补当前多模态研究中文档理解的空白 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | 开源推理模型的标杆，MoE 架构 + 深度推理优化的组合。重点研究其长上下文推理中的注意力模式，以及推理链的事实一致性——可设计实验探测其数学推理中的幻觉率，与 Flash 版本对比分析推理深度与幻觉的权衡关系 |
| ⭐⭐☆ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | 开放域视觉定位的轻量方案，3B 参数实现灵活定位。研究价值在于：其"定位-描述"联合任务可视为视觉幻觉缓解的代理任务——输出必须与像素严格对应，可借鉴其训练目标设计来约束 VLM 的视觉 grounding，减少"虚构物体"类幻觉 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*