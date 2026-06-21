# Hugging Face 热门模型日报 2026-06-21

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-21 00:37 UTC

---

# Hugging Face 研究模型日报 | 2026-06-21

## 今日速览

本周 Hugging Face 生态呈现显著的**多模态统一化**与**推理增强**趋势：Google 发布 Gemma-4 系列原生 any-to-any 架构，标志着视觉-语言融合进入统一建模阶段；DeepSeek-V4-Pro 以近 5000 点赞领跑，其 MoE 架构与对话能力为长上下文推理研究提供重要基线；Kimi-K2.7-Code 与 MiniMax-M3 在视觉编码器-语言模型对齐方面表现突出；值得关注的是 `datalab-to/lift` 作为专门的 PDF 文档理解模型出现，以及 `microsoft/FastContext-1.0-4B-SFT` 明确聚焦长上下文 SFT 训练，直接服务于后训练对齐研究。GGUF 量化生态持续繁荣，但研究者需警惕 uncensored 微调模型在幻觉缓解评估中的数据污染风险。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to<br>👍 86 \| ⬇️ 0 | 基于 Qwen3.5 的 PDF 文档理解专用模型，直接面向 OCR 后处理与版面分析任务，零下载量表明刚发布，适合作为文档智能研究的早期基线 |

### 🎭 多模态与视觉语言

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google<br>👍 1,106 \| ⬇️ 1,696,240 | **原生 any-to-any 架构**，统一处理图像-文本-文本生成，为跨模态表征对齐研究提供官方基准；Gemma-4 系列的技术报告值得深入分析其视觉编码器设计 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI<br>👍 1,159 \| ⬇️ 85,771 | 闭源厂商 MiniMax 的开源 M3 视觉语言模型，标签明确为 `minimax_m3_vl`，适合对比研究商业 VLM 与开源方案在视觉指令跟随上的差距 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai<br>👍 929 \| ⬇️ 317,963 | Kimi 系列代码专用 VLM，支持图像特征提取与压缩张量，其 `compressed-tensors` 标签暗示视觉 token 压缩机制，对高效多模态推理研究有直接价值 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia<br>👍 2,216 \| ⬇️ 235,606 | NVIDIA 开源的 3B 定位模型，专注于视觉 grounding 与空间推理，高点赞反映社区对精确视觉定位的需求，可作为幻觉缓解中"指代一致性"的评测工具 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio<br>👍 327 \| ⬇️ 190,694 | 397B 参数的 Qwen3.5-MoE 开源巨模型，政府背景机构的发布值得关注其训练数据与对齐策略的透明度 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong<br>👍 269 \| ⬇️ 168,502 | 集成 MTP（Multi-Token Prediction）的代码视觉模型，GGUF 格式便于研究多 token 预测在视觉-代码联合推理中的效果 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU<br>👍 411 \| ⬇️ 587,521 | **高度复杂的微调模型**，融合"Thinking"与多源蒸馏，但"Uncensored"标签警示其在安全对齐与幻觉评估中可能存在系统性偏差，适合作为**对齐失败案例**研究 |

### 🧠 长上下文与推理模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai<br>👍 4,985 \| ⬇️ 2,797,050 | **本周绝对热度冠军**，DeepSeek-V4 架构的 Pro 版本，MoE 设计支持高效长上下文推理，其近 280 万下载量表明已成为开源推理研究的事实标准 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org<br>👍 1,686 \| ⬇️ 19,683 | GLM 系列最新版，采用 MoE+DSA（Dynamic Sparse Attention）架构，DSA 机制对长上下文注意力效率研究有直接参考价值 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI<br>👍 511 \| ⬇️ 16,270 | 3B 规模的数学专用推理模型，基于 Qwen2 架构，小参数高效推理方向适合资源受限场景下的推理能力研究 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft<br>👍 244 \| ⬇️ 1,998 | **微软官方长上下文 SFT 模型**，基于 Qwen3 的 4B 参数实验品，标签含"Explorer SubAgent"，明确服务于长上下文代理研究，是后训练阶段扩展上下文窗口的珍贵参考 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1<br>👍 1,983 \| ⬇️ 312,332 | 社区融合微调版 Gemma-4，结合 Fable5 与 Composer2.5，高下载量反映社区对代码推理增强的需求，但融合来源复杂需谨慎评估 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1<br>👍 183 \| ⬇️ 6,307 | 同一系列的 agentic 变体，引入"terminal"标签与 3.5x 推理缩放，适合研究工具使用与推理链长度对幻觉的交互影响 |

### 🔧 Post-Training 与对齐

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS<br>👍 2,040 \| ⬇️ 3,812,636 | **本周下载量异常突出**（380万+），"Aggressive"与"Uncensored"标签表明极端的对齐移除操作，可作为**研究安全对齐失效机制**的负面样本，但绝不可作为正面基线 |
| **[bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF](https://huggingface.co/bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF)** | bytkim<br>👍 97 \| ⬇️ 20,465 | "pi-tune"暗示 π 值优化或策略迭代微调，MTP 与特定微调方法结合，适合探索多 token 预测与 RL 类后训练的协同效应 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs<br>👍 467 \| ⬇️ 18,783 | Cohere 官方 MoE 代码模型，Cohere 在偏好对齐（如 North 系列）有技术积累，值得追踪其 DPO/RLHF 策略细节 |

### 👁️ 幻觉缓解

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google<br>👍 1,022 \| ⬇️ 673,464 | **Diffusion + Gemma 的生成式 VLM**，扩散解码机制天然支持逐步去噪的"思维链"可视化，可能为可解释性驱动的幻觉检测提供新路径 |
| **[unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF)** | unsloth<br>👍 146 \| ⬇️ 37,260 | Unsloth 量化版本保留 `compressed-tensors` 特性，压缩视觉表征可能引入的幻觉模式值得系统评估 |

### 🏗️ 研究基础设施

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth<br>👍 205 \| ⬇️ 22,586 | Unsloth 对 GLM-5.2 的 GGUF 转换，其量化策略对长上下文模型的 KV 缓存压缩有直接影响，是推理效率研究的工具层参考 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org<br>👍 115 \| ⬇️ 138,174 | 官方 FP8 权重发布，低精度训练/推理与长上下文稳定性的权衡是新兴研究方向 |
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI<br>👍 81 \| ⬇️ 6,128 | 液态神经网络（Liquid Neural Networks）的 Embedding 模型，非 Transformer 架构的表征学习为长序列建模提供替代路径 |

---

## 研究生态信号

**Qwen/Gemma 双寡头格局固化，但对齐安全出现"两极化"张力。** Qwen3.5/3.6 与 Gemma-4 占据本周多模态与推理模型的绝对主流，从 3B 到 400B+ 的密集覆盖使二者成为事实上的开源研究基础设施。然而，HauhauCS、DavidAU 等发布的 "Aggressive Uncensored" 微调模型下载量畸高（380万+），与微软、Google 的官方对齐模型形成尖锐对比，暗示开源社区存在**系统性安全微调需求未被满足**或**评估标准分裂**的深层问题。视觉语言领域，原生 any-to-any（Gemma-4）与拼接式 VLM（Qwen-VL 系）的技术路线竞争进入白热化，扩散式生成（DiffusionGemma）可能打破自回归垄断。文档理解方面，专用模型 `lift` 的出现填补了 Qwen-VL 通用架构在 PDF 结构化解析上的细分空白，但 OCR/HMER 垂直领域仍缺乏像 Nougat 级别的突破性开源模型。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | 微软官方罕见地公开了**长上下文 SFT 的中间产物**，4B 规模可控，"Explorer SubAgent" 架构细节若随技术论文释放，将直接填补"如何通过后训练有效扩展上下文"的方法论空白，建议优先申请模型权限并监控关联论文 |
| ⭐⭐⭐ | **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | 扩散架构用于多模态对话的**首次大规模开源尝试**，其逐步去噪过程与思维链推理的类比关系、以及扩散模型在事实一致性（减少幻觉）上的理论优势，使其成为跨架构对比研究的战略级资源 |
| ⭐⭐☆ | **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | 零下载量的新鲜发布，专注 PDF 的 `image-text-to-text` 定位明确，若其训练数据包含学术文献的公式与表格标注，可能成为 OCR/HMER 领域被低估的基线模型，建议验证其在标准 benchmark（如 IM2LATEX-100K、PubTabNet）上的表现 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*