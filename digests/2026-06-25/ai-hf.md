# Hugging Face 热门模型日报 2026-06-25

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-25 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-06-25

## 今日速览

百度 **Unlimited-OCR** 以 732 点赞强势切入 OCR 赛道，标志着通用文档理解模型向"无限制"场景扩展的新趋势。GLM-5.2 系列（zai-org 原版 + unsloth GGUF 量化版）延续 MoE+DSA 架构热度，在长上下文推理效率上持续迭代。多模态领域呈现爆发态势：Kimi-K2.7-Code、MiniMax-M3、google/gemma-4-12B-it 及 diffusiongemma-26B-A4B-it 四款视觉语言模型同时上榜，显示统一架构（any-to-any / unified）正成为 VLM 主流设计范式。后训练对齐方面，微软 FastContext-1.0-4B-SFT 的"Explorer SubAgent"标签暗示 Agent 场景下的上下文对齐新方向。值得关注的是，Qwen 生态（3.5/3.6 系列）在量化社区微调中占据绝对主导地位，但专门面向幻觉缓解的模型仍显稀缺。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu / 732 / 45,687 | 百度开源的"无限制"OCR 模型，突破传统文档版面与长度约束，对 HMER（手写数学表达式识别）及复杂版面分析研究具有直接参考价值；`image-feature-extraction` 标签暗示其编码器设计可能支持下游文档理解任务的特征迁移。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 1,162 / 2,114,441 | Gemma 4 统一架构（`gemma4_unified` + `any-to-any`），原生支持图像-文本双向生成，为跨模态推理与视觉指令微调研究提供开源基座；高下载量反映社区对统一 VLM 的强烈需求。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai / 984 / 480,013 | Kimi K2.5 系列的代码专用多模态模型，结合 `compressed-tensors` 技术，适合研究视觉编码器在代码理解（如图表、UI 截图）中的表征效率与幻觉问题。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI / 1,228 / 143,093 | MiniMax-M3 作为国产多模态代表，其 `minimax_m3_vl` 架构在图文对话中的事实一致性表现值得深入研究，可能与幻觉缓解技术相关。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google / 1,060 / 1,036,328 | 扩散模型与 Gemma 结合的 26B/A4B MoE 架构，支持图像-文本交互生成，为研究生成式 VLM 的幻觉控制（扩散过程的可解释性）提供独特实验平台。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 2,205 / 3,769,369 | Qwen3.6 MoE 视觉模型的激进去审查微调版，极高下载量揭示社区对" uncensored"多模态模型的需求，但 `uncensored` 标签本身暗示安全对齐与幻觉风险的权衡张力，值得警惕研究。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai / 307 / 5,123 | Qwen3.5 架构的 1M 上下文视觉语言模型，Claude 风格对齐，直接关联长上下文多模态推理与跨模态信息整合的幻觉问题。 |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to / 147 / 4,644 | 基于 Qwen3.5 的 PDF 文档理解专用模型，填补通用 VLM 在结构化文档（表格、公式、版面）精细解析中的空白，OCR+多模态的交叉研究样本。 |
| **[Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF)** | Jackrong / 83 / 10,867 | Qwen3.6 27B 代码视觉模型的 GGUF 量化版，MTP（Multi-Token Prediction）兼容设计，适合研究高效推理下的代码相关视觉幻觉。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org / 2,351 / 57,186 | GLM-5.2 延续 `glm_moe_dsa`（Dynamic Sparse Attention）架构，在 MoE 框架下优化长上下文注意力效率，是研究稀疏注意力与长程推理机制的核心基线。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth / 347 / 76,971 | Unsloth 官方量化版本，保持长上下文能力的同时大幅降低推理成本，适合长上下文算法的广泛可及性研究。 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org / 157 / 445,304 | FP8 精度原生支持版本，高下载量验证社区对低精度长上下文推理的需求，为研究量化对长程依赖建模的影响提供数据点。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 5,046 / 2,052,463 | 本期点赞冠军，DeepSeek-V4 的 Pro 版本在推理效率与对话质量上持续领先，其 MoE 架构的长上下文路由机制是推理优化研究的重要参照。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI / 692 / 49,569 | 3B 规模的数学推理专用模型（`math` 标签），基于 Qwen2 架构，小模型强推理方向的代表，适合研究高效推理与计算资源受限场景下的数学幻觉。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai / 346 / 63,637 | 1M 上下文 Qwen3.5 的 GGUF 量化版，`reasoning` 标签明确指向长上下文中的链式推理能力，是研究扩展上下文与推理连贯性的实验载体。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 / 2,296 / 483,139 | Gemma-4 代码推理模型的社区融合微调版，高下载量反映代码推理的广泛需求，其 `reasoning` 与 `coding` 双标签适合研究结构化推理中的幻觉模式。 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 / 530 / 138,704 | Agentic 特化版本，`terminal` 标签暗示工具使用与执行反馈循环，直接关联 Agent 场景中的动作幻觉与自我修正机制研究。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft / 336 / 4,805 | 微软 4B 轻量长上下文模型，`Explorer SubAgent` 标签揭示其面向 Agent 探索任务的上下文优化目标，是研究 Agent 场景下高效上下文对齐的稀缺官方资源。 |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen / 143 / 223 | Qwen 官方 Agent 世界模型，35B/A3B MoE，虽下载量低但官方背书使其成为 Agent 多轮交互中上下文管理与幻觉传播的标准基线。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai / 124 / 4,402 | `abliterated`（消融/去限制）标签明确指向对齐干预研究，该模型通过移除特定安全对齐层探索代码模型的能力边界，为对齐强度与有用性权衡提供极端案例。 |
| **[poolside/Laguna-M.1](https://huggingface.co/poolside/Laguna-M.1)** | poolside / 95 / 2,913 | Poolside 的代码模型，`vllm`/`sglang` 部署优化标签，其训练后优化可能包含针对代码生成一致性的特殊对齐策略，值得追踪技术报告。 |

---

### 👁️ 幻觉缓解

*本期无直接标注"幻觉缓解"或"事实校准"的专门模型，但以下模型隐含相关技术或可作为研究平台：*

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 2,346 / 359,498 | NVIDIA 的开放词汇定位模型，`locateanything` 架构通过细粒度视觉-语言对齐实现指代表达理解，其定位机制可迁移至幻觉检测（视觉 grounding 作为事实验证信号）。 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 1,162 / 2,114,441 | 统一 any-to-any 架构的生成-理解闭环，为研究生成式 VLM 的自我验证与事实一致性约束提供可控实验环境。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)** | LiquidAI / 119 / 11,471 | 基于 LFM2.5 的嵌入模型，为长文档检索与 RAG 系统提供编码器基础，间接支撑幻觉缓解中的外部知识增强研究。 |
| **[LiquidAI/LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M)** | LiquidAI / 88 / 3,362 | ColBERT 晚期交互架构的 LFM2.5 实现，细粒度 token 级检索对文档级事实核查与幻觉定位具有独特优势。 |

---

## 研究生态信号

**Qwen 生态主导社区微调，Gemma-4 统一架构引领 VLM 范式。** Qwen3.5/3.6 系列在 GGUF 量化社区中形成绝对垄断（Qwythos、Qwopus、HauhauCS 等），反映其开源权重在可定制性上的优势，但过度集中于"uncensored"微调可能稀释安全对齐研究资源。Google Gemma-4 的 `unified`/`any-to-any` 设计标志着 VLM 从"拼接式"（独立编码器+投影）向"原生统一"的架构跃迁，这与 OCR/HMER 领域对端到端文档理解的需求高度契合。微软 `FastContext` 的 SubAgent 标签、Qwen `AgentWorld` 的命名，共同指向"Agent 上下文管理"作为后训练对齐的新兴子领域。然而，**专门面向幻觉缓解的模型或数据集仍严重缺位**，当前幻觉研究主要依赖通用模型的自我验证或 RAG 外挂，缺乏像 Unlimited-OCR 之于文档领域那样的"专门解"。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | OCR/HMER 领域的"无限制"宣称需要严格验证：其在手写公式、复杂版面、极端长文档上的实际表现如何？编码器设计是否支持特征提取后的下游微调？可作为文档理解基础模型的基准测试对象，亦是检验当前 OCR 幻觉（如版面还原错误、公式符号误识别）的典型案例库。 |
| ⭐⭐⭐ | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | 统一 any-to-any 架构是研究多模态幻觉的理想平台：图像生成→文本理解的双向循环是否加剧或缓解幻觉传播？`gemma4_unified` 的注意力机制在跨模态事实一致性上是否有内在约束？其 2M+ 下载量确保实验可复现性。 |
| ⭐⭐⭐ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | 4B 轻量模型+Explorer SubAgent 的罕见组合，为研究资源受限场景下的 Agent 对齐提供官方基线。可深入探究：SFT 阶段如何编码"探索-利用"权衡？SubAgent 的上下文分割策略对长程任务幻觉有何影响？微软技术报告的潜在价值高。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*