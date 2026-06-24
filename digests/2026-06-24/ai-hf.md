# Hugging Face 热门模型日报 2026-06-24

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-24 00:29 UTC

---

# Hugging Face 研究模型日报 | 2026-06-24

## 今日速览

本周 Hugging Face 生态呈现多模态推理与长上下文能力快速迭代态势。**DeepSeek-V4-Pro** 以 5,030 点赞领跑，其 MoE 架构与对话能力对长上下文研究具有重要参考价值；**nvidia/LocateAnything-3B** 和 **google/diffusiongemma-26B-A4B-it** 分别代表视觉定位与统一多模态架构的前沿探索；OCR 领域 **baidu/Unlimited-OCR** 首次进入热榜，暗示文档理解正成为新的开源竞争焦点。值得注意的是，Qwen3.6 系列衍生模型（含 GGUF 量化变体）大量涌现，反映社区对可部署的多模态推理模型的强烈需求。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 472 / 8,396 | 百度开源的通用 OCR 模型，支持无限制长度文本识别；对 HMER（手写数学公式识别）和复杂版面分析研究具有直接参考价值，其 `image-feature-extraction` 架构值得深入解析 |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 135 / 3,216 | 基于 Qwen3.5 的 PDF 文档理解模型；对文档级 OCR 与结构化信息抽取的联合训练研究有启发意义 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,156 / 3,955,016 | Qwen3.6 MoE 视觉模型的社区微调版，极高的下载量反映其作为多模态基座的实用性；对视觉语言对齐与安全性-性能权衡研究具有警示意义 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,315 / 274,025 | NVIDIA 开源的视觉定位模型，支持任意目标的细粒度空间理解；对视觉 grounding 与多模态推理的融合架构设计有直接借鉴价值 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,055 / 948,996 | Diffusion-Gemma 统一架构，将扩散模型与语言模型结合；对多模态生成-理解一体化架构及幻觉缓解的联合优化研究具有范式意义 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,220 / 131,057 | MiniMax 多模态模型，专注图文理解；其 `minimax_m3_vl` 架构对国产 VLM 技术路线对比研究有参考价值 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 975 / 447,920 | Kimi K2.5 系列的代码专用多模态变体，支持图像特征提取；对代码生成中的视觉输入理解与长上下文代码推理研究相关 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,154 / 1,991,703 | Gemma 4 统一架构的 any-to-any 模型，支持任意模态输入输出；对统一多模态架构的 scaling law 与模态对齐研究至关重要 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai | 212 / 1,856 | 基于 Qwen3.5 的社区多模态模型，1M 上下文声称；对长上下文多模态模型的实际能力边界验证有研究价值 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 5,030 / 2,245,489 | DeepSeek V4 专业版，MoE 架构支持超长上下文推理；当前长上下文与复杂推理研究的最强开源基座之一，其 `deepseek_v4` 架构对上下文压缩与稀疏激活研究有直接价值 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,195 / 40,127 | GLM-5.2 采用 MoE+DSA（Dynamic Sparse Attention）架构，专为长上下文设计；对高效注意力机制与长序列建模研究具有核心参考价值 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org | 149 / 395,290 | GLM-5.2 的 FP8 量化版本，高下载量反映部署需求；对长上下文模型的量化精度损失与推理效率权衡研究有实用意义 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 300 / 55,820 | Unsloth 优化的 GLM-5.2 GGUF 版本，支持本地长上下文推理；对长模型边缘部署与推理加速研究相关 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 664 / 41,170 | 3B 参数数学推理专用模型，基于 Qwen2；对小模型数学推理能力与模型压缩的 scaling law 研究有参考价值 |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim | 111 / 65,765 | Qwen3.6 27B 的 MTP（Multi-Token Prediction）微调版；对推理加速与投机解码在多模态场景的应用研究有启发 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 321 / 4,391 | 微软 4B 长上下文 SFT 模型，"Explorer SubAgent" 架构；对高效上下文检索与子代理任务分解机制研究有直接价值 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,237 / 456,117 | Gemma 4 的多阶段指令微调变体（coder+fable+composer），极高下载量；对多任务后训练的组合策略与灾难性遗忘缓解研究具有典型案例价值 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 445 / 96,459 | 上述模型的 agentic 增强版，引入工具使用与终端交互能力；对 agent 对齐与工具调用安全性的后训练方法研究相关 |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 112 / 3,320 | "abliterated" 版本即安全对齐移除版，与原版形成对照；对对齐技术的鲁棒性与对抗性移除研究具有伦理与技术双重警示价值 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 186 / 27,218 | 基于 Claude 风格对齐的 Qwen3.5 量化版；对蒸馏式偏好对齐与跨模型知识迁移研究有参考价值 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 1,055 / 948,996 | 扩散-语言统一架构，扩散模型的渐进生成特性天然具备不确定性量化能力；对生成式幻觉的显式建模与可解释性研究具有独特优势 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 321 / 4,391 | 子代理架构支持检索增强的上下文验证；对 RAG 增强的事实性校验与长文档幻觉缓解机制研究相关 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞/下载 | 研究相关性 |
|:---|:---|:---|:---|
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI | 114 / 10,117 | LFM 2.5 系列嵌入模型，基于液态神经网络架构；对新型架构在长文本表示与检索中的效率对比研究有探索价值 |
| **[LiquidAI/LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M)** | LiquidAI | 87 / 2,534 | 同上系列的 ColBERT 晚期交互模型；对多模态检索中的细粒度交互机制研究相关 |

---

## 研究生态信号

**Qwen 生态持续主导开源多模态**：Qwen3.5/3.6 系列衍生模型占据本周热榜 30% 以上，涵盖从 9B 到 35B 的 MoE 架构，且社区微调活跃度极高（HauhauCS、empero-ai、bytkim 等），表明其已成为事实上的开源多模态研究基座。**Gemma 4 统一架构** 的发布（google/gemma-4-12B-it 及大量社区微调版）标志着"any-to-any" 统一多模态成为新范式，但社区"abliterated"版本的并行流行也暴露了对齐技术的脆弱性。OCR 领域百度入局开源尚属早期，但 Unlimited-OCR 的 `image-feature-extraction` 定位暗示其与 VLM 的融合趋势。值得关注的是，**长上下文与推理能力的结合**（GLM-5.2 的 DSA、DeepSeek-V4-Pro 的 MoE、FastContext 的子代理）正成为差异化竞争核心，而 FP8/GGUF 等量化格式的高下载量反映研究社区对"可验证的长上下文"（即本地可部署）的迫切需求。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | DSA（Dynamic Sparse Attention）机制是长上下文效率研究的前沿实现，其 MoE 架构与稀疏注意力的结合对探索"无限上下文"的近似方法具有直接实验价值；建议对比其 FP8 版本的精度-长度权衡曲线 |
| ⭐⭐⭐ | **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | 扩散模型与自回归语言模型的统一架构为幻觉缓解提供了新视角——扩散的迭代去噪过程可显式建模不确定性，建议探索其在多模态事实性验证中的应用，或与 RAG 结合构建可校准的生成系统 |
| ⭐⭐☆ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | "Explorer SubAgent" 架构是长上下文检索与生成的模块化尝试，4B 规模适合学术研究资源；建议验证其在长文档问答中的幻觉率，并与端到端长上下文模型进行效率-准确性帕累托分析 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*