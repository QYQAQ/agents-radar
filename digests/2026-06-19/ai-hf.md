# Hugging Face 热门模型日报 2026-06-19

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-19 00:42 UTC

---

# Hugging Face 研究模型日报 | 2026-06-19

## 今日速览

本周 Hugging Face 热门模型呈现**多模态统一架构**与**长上下文推理**双主线并进态势。Google Gemma-4 系列以"any-to-any"统一范式引发关注，其 12B 统一模型在 OCR/文档理解场景具备端到端潜力；MiniMax-M3 与 Kimi-K2.7-Code 持续推动视觉语言模型的代码与推理边界；DeepSeek-V4-Pro 以近 300 万下载量巩固 MoE 架构在高效推理领域的地位；Microsoft FastContext-1.0-4B-SFT 直接瞄准长上下文压缩与对齐，而 Nvidia LocateAnything-3B 的空间定位能力为视觉 grounding 与幻觉缓解提供新工具。值得注意的是，GGUF 量化生态（unsloth 等）正加速多模态模型的边缘部署研究。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 点赞 1,085 / 下载 1,309,625 | **统一架构里程碑**：原生 "any-to-any" 设计，单模型处理图文音视频，对 OCR→文档理解→结构化输出的端到端研究具有范式意义，消除传统级联误差累积。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI / 点赞 1,098 / 下载 56,162 | **MoE 多模态推理**：image-text-to-text 任务标签结合高下载量，其视觉-语言联合表征可能隐含数学/公式理解能力，值得 OCR+HMER 场景迁移测试。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai / 点赞 883 / 下载 229,156 | **代码视觉推理**：image-feature-extraction 与压缩张量技术结合，在代码图表、LaTeX 渲染图的理解上可能超越纯文本模型，对 HMER 有间接启发。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 点赞 2,162 / 下载 183,093 | **空间 grounding 利器**：image-feature-extraction 定位任意对象，直接服务于视觉语言模型的**幻觉缓解**——通过显式坐标约束减少"编造"对象位置。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google / 点赞 1,002 / 下载 527,080 | **扩散+语言统一**：diffusion_gemma 架构将图像生成与理解耦合，对"生成式 OCR"（如手写公式合成、文档增强）及多模态对齐研究有独特价值。 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio / 点赞 324 / 下载 190,501 | **超大规模 MoE 开源**：397B 总参数量级公开，qwen3_5_moe 架构为多模态 scaling law 与对齐稳定性研究提供罕见实验素材。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong / 点赞 249 / 下载 122,175 | **MTP 多模态代码**：Multi-Token Prediction 与 vision 标签结合，可能优化代码图表中的序列化理解，GGUF 格式便于本地 OCR 流水线集成。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 点赞 1,969 / 下载 3,420,052 | **对齐研究的"反面教材"**：极高下载量的 uncensored 微调版本，为**幻觉缓解与安全性对齐**研究提供对比基线——分析移除安全对齐后的幻觉模式。 |
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth / 点赞 307 / 下载 164,209 | **扩散模型边缘化**：GGUF 量化使 26B 扩散-语言模型可本地运行，为文档图像生成式修复、公式去噪等 OCR 增强任务降低研究门槛。 |
| **[unsloth/MiniMax-M3-GGUF](https://huggingface.co/unsloth/MiniMax-M3-GGUF)** | unsloth / 点赞 103 / 下载 22,659 | **MoE 多模态轻量化**：agent 标签暗示工具调用能力，结合 vision 可探索"视觉感知→外部 OCR API→结果验证"的幻觉缓解代理架构。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS / 点赞 350 / 下载 96,805 | **统一模型的对齐消融**：gemma4_unified 架构的"obliterated"变体，与官方版本形成对照，研究统一架构的对齐鲁棒性与幻觉边界。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU / 点赞 394 / 下载 529,069 | **极端融合实验**：多重源模型蒸馏+uncensored+thinking 标签，为**多源对齐冲突导致的幻觉**研究提供复杂案例，IMatrix 量化技术本身亦值得评估。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 / 点赞 1,703 / 下载 211,424 | **代码推理社区微调**：gemma4+coder+reasoning 标签组合，高点赞反映社区对轻量推理模型的需求，GGUF 便于长上下文代码文档的本地推理测试。 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org / 点赞 1,340 / 下载 4,307 | **GLM 统一预训练**：glm_moe_dsa 架构延续自回归+自编码混合范式，其双向注意力对长文档的 OCR 后结构化理解（如表格重建）有理论优势。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI / 点赞 405 / 下载 6,589 | **小参数数学推理**：3B 规模+math 标签，探索极小模型的推理涌现，对 OCR 后公式验证的轻量部署有参考价值。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft / 点赞 203 / 下载 957 | **长上下文压缩对齐**：qwen3 基座+SFT+Explorer SubAgent 标签，直接瞄准**长上下文推理的效率与对齐**，"SubAgent"暗示分层注意力机制，对文档级 OCR 的长序列处理有关键意义。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 点赞 4,956 / 下载 2,948,726 | **MoE 推理标杆**：deepseek_v4 架构+近 300 万下载，其 MLA 注意力与专家路由机制是长上下文高效推理的核心研究对象，Pro 版本的对齐质量直接影响下游 OCR 应用可靠性。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs / 点赞 448 / 下载 15,285 | **cohere2_moe 代码专注**：coheret 架构的代码特化版本，对代码文档（Jupyter、LaTeX 源码）的 OCR 后语义恢复有专门优化潜力。 |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** | nex-agi / 点赞 327 / 下载 6,640 | **qwen3_5_moe 双任务**：同时标注 image-text-to-text 与 text-generation，探索统一架构在多模态与纯文本推理间的平衡，对 OCR 管道的模态切换有启发。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth / 点赞 122 / 下载 305 | **GLM 轻量化实验**：glm_moe_dsa 的 GGUF 实现，便于验证双向注意力在长文档 OCR 结构化中的实际收益与量化损失。 |
| **[zai-org/GLM-5.2-FP8](https://huggingface.co/zai-org/GLM-5.2-FP8)** | zai-org / 点赞 90 / 下载 24,967 | **FP8 精度前沿**：官方 FP8 权重发布，为研究低精度训练对长上下文稳定性与幻觉率的影响提供标准测试点。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft / 点赞 203 / 下载 957 | **SFT 长上下文对齐**：重复强调——"Explorer SubAgent" 可能代表新型分层 RLHF 架构，对长文档理解中的**偏好对齐**（如摘要忠实度）有直接应用。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 点赞 1,969 / 下载 3,420,052 | **对齐移除的规模化实验**：3.4M 下载的 uncensored 模型，为研究**DPO/RLHF 的必要性边界**、以及移除对齐后的幻觉激增模式提供大规模用户行为数据。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU / 点赞 394 / 下载 529,069 | **多源蒸馏对齐冲突**：融合 Claude/Opus/Qwen 等多源监督信号，"Thinking"标签暗示推理时对齐，为**多教师蒸馏中的偏好冲突与幻觉传播**研究提供极端案例。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 点赞 2,162 / 下载 183,093 | **视觉 grounding 反幻觉**：显式空间定位能力可作为 VLM 的**外部验证器**——当模型声称"图中包含某公式"时，LocateAnything 可强制要求提供坐标证据，实现可验证的 OCR 输出。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google / 点赞 1,002 / 下载 527,080 | **生成-理解闭环校准**：扩散模型的重构误差可作为"感知一致性"指标，用于检测 VLM 对文档图像的**幻觉描述**（若重构失败则模型可能"编造"内容）。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 点赞 1,969 / 下载 3,420,052 | **幻觉基线构建**：系统对比 uncensored 与官方对齐版本的输出差异，可量化安全对齐机制对**事实准确性 vs 拒绝率**的 trade-off，为校准置信度研究提供数据。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF)** | unsloth / 点赞 134 / 下载 29,287 | **量化生态基础设施**：unsloth 持续扩展 GGUF 至多模态压缩模型，其压缩-推理工具链是 OCR/HMER 模型边缘部署的关键依赖。 |
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth / 点赞 307 / 下载 164,209 | **扩散模型边缘化**：同上，26B 扩散-语言模型的 GGUF 化使"生成式文档增强"研究可在消费级硬件开展。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth / 点赞 122 / 下载 305 | **双向注意力轻量化**：GLM 架构的 GGUF 实现，为验证其长文档处理优势提供低成本入口。 |
| **[unsloth/MiniMax-M3-GGUF](https://huggingface.co/unsloth/MiniMax-M3-GGUF)** | unsloth / 点赞 103 / 下载 22,659 | **MoE 多模态边缘代理**：agent 标签+GGUF 格式，支持"本地视觉感知→API 调用→结果验证"的幻觉缓解代理原型快速搭建。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth / 点赞 652 / 下载 918,431 | **统一架构边缘化**：any-to-any 原型的 GGUF 版本，近百万下载验证社区对端侧多模态 OCR 的强烈需求。 |

---

## 研究生态信号

**Gemma-4 统一架构**正挑战 Qwen-MoE 的多模态主导地位，Google 以"any-to-any"原生设计试图终结级联 OCR→VLM 的误差链，但社区微调（yuxinlu1、OBLITERATUS）显示对齐鲁棒性仍是开放问题。**MiniMax-M3 / Kimi-K2.7-Code** 代表闭源能力的开源化追赶，而 **DeepSeek-V4-Pro** 的 MoE 效率与 **Microsoft FastContext** 的显式长上下文 SFT 形成技术路线竞争。值得注意的是，**uncensored 微调生态**（HauhauCS、DavidAU）的爆发式增长（累计近 400 万下载）正在制造大规模"反事实"实验场——研究者既可利用其分析对齐失效的幻觉模式，也需警惕其污染评测基准。Nvidia LocateAnything 的空间 grounding 与 diffusiongemma 的生成-理解闭环，则为幻觉缓解提供了**可验证性**与**一致性**两类新工具。GGUF 量化生态（unsloth 主导）已覆盖所有主流架构，使边缘端 OCR 研究的基础设施趋于成熟。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **长上下文对齐的显式架构**："Explorer SubAgent" 标签暗示分层/稀疏注意力机制，是理解长文档 OCR 中"注意力坍塌"与幻觉关联的关键实验对象。4B 规模便于消融研究，SFT 阶段的对齐策略可直接对比 RLHF 与纯监督的上下文忠实度差异。 |
| ⭐⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*