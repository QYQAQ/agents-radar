# Hugging Face 热门模型日报 2026-06-15

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-15 00:37 UTC

---

# Hugging Face 研究模型日报 | 2026-06-15

## 今日速览

本周 Hugging Face 生态呈现**多模态统一架构加速收敛**的显著趋势：Google Gemma-4 系列以"any-to-any"范式强势占据下载榜首（累计超 240 万下载），其原生视觉-语言统一设计对 OCR 和文档理解研究具有直接价值；DeepSeek-V4-Pro 以近 5000 点赞领跑推理模型赛道，MoE 架构与后训练优化值得对齐研究者深入分析；MiniMax-M3 和 Kimi-K2.7-Code 等国产 VLM 持续活跃，反映长上下文多模态推理的激烈竞争；值得注意的是，基于 Qwen3.6 的激进微调版本（如 Uncensored-HauhauCS-Aggressive）下载量异常高企，暗示**对齐与安全性研究**在开源社区面临严峻挑战。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google / 点赞 1,008 / 下载 1,084,405 | **any-to-any 统一架构**：原生支持图像-文本交错输入与输出，非拼接式 VLM 设计，对研究真正的多模态推理机制（而非视觉-语言"嫁接"）具有范式意义；OCR 和文档理解可直接利用其统一编码器。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google / 点赞 542 / 下载 213,502 | 基础版 any-to-any 模型，适合研究**预训练阶段的多模态表征对齐**，对比 it 版可分析指令微调对视觉 grounding 的影响。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google / 点赞 792 / 下载 198,912 | **扩散模型与语言模型统一**：26B 参数、A4B 激活的 MoE 架构，将扩散生成与文本推理融合，对研究多模态生成中的幻觉缓解（生成内容与指令的一致性）提供新框架。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI / 点赞 487 / 下载 6,643 | 国产多模态大模型，标签明确标注 `multimodal`，其长上下文视觉推理能力待评测，适合作为**对比基线**研究不同 VLM 架构的上下文效率。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai / 点赞 626 / 下载 15,145 | Kimi K2.5 系列迭代，支持 `image-feature-extraction` 与代码任务，对研究**视觉-代码联合推理**（如图表转代码、UI 理解）具有工具价值。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 点赞 2,000 / 下载 75,201 | 3B 参数高效定位模型，**视觉 grounding 专用**，对研究细粒度视觉引用（如文档中的区域定位、公式位置检测）提供轻量解决方案。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth / 点赞 597 / 下载 926,372 | Gemma-4 的高性能量化版本，近百万下载验证其部署价值，适合研究**量化对多模态推理精度的影响**及边缘端 OCR 应用。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 点赞 1,805 / 下载 2,516,709 | **对齐研究的负面样本**：下载量破 250 万的"去审查"微调版，揭示开源社区对安全对齐的规避需求，对研究**RLHF 脆弱性、越狱机制及防御性对齐**具有警示意义。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong / 点赞 179 / 下载 33,720 | Qwen3.6 视觉-代码模型，MTP（Multi-Token Prediction）架构，适合研究**多模态代码生成中的长程依赖与幻觉问题**。 |
| **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong / 点赞 303 / 下载 175,472 | v2 迭代版本，下载量显著增长，可对比分析 MTP 改进对视觉-语言一致性的影响。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU / 点赞 336 / 下载 375,966 | 极端融合微调案例（命名即揭示其"缝合"性质），对研究**多教师蒸馏中的知识冲突与幻觉放大**具有解剖价值。 |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** | unsloth / 点赞 232 / 下载 255,424 | QAT（量化感知训练）版本，对比标准 GGUF 可研究**量化训练对多模态对齐精度的保持度**。 |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth / 点赞 157 / 下载 317,261 | 26B MoE 的 QAT 量化版，适合研究**大规模多模态模型的高效部署与推理一致性**。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai / 点赞 4,832 / 下载 3,075,369 | **本周绝对焦点**：V4 代 MoE 架构，300 万+下载，对研究**长上下文推理的效率优化、推理时计算扩展及后训练对齐**具有核心参考价值；其"Pro"后缀暗示强化推理能力。 |
| **[silx-ai/Quasar-Preview](https://huggingface.co/silx-ai/Quasar-Preview)** | silx-ai / 点赞 71 / 下载 307 | 标签明确 `quasar_long`，**专注长上下文**的预览模型，虽早期但架构方向值得关注，适合跟踪研究。 |
| **[XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)** | XiaomiMiMo / 点赞 113 / 下载 4,108 | 小米 Agent 模型，FP4 量化 + DFlash 推理加速，对研究**长上下文 Agent 推理的实时性与准确性权衡**有场景价值。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs / 点赞 368 / 下载 9,932 | `cohere2_moe` 架构，Cohere 对齐团队出品，研究**MoE 架构的代码专用对齐策略**（如过程奖励模型）的理想对象。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS / 点赞 297 / 下载 60,949 | "OBLITERATED"即系统提示擦除，对研究**基础模型与对齐模型的行为边界、对齐 tax 及恢复方法**提供实验素材。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 / 点赞 161 / 下载 6,219 | 多模型融合微调（Fable5 + Composer2.5），对研究**多教师 SFT 中的知识选择与冲突消解**具有案例价值。 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)** | prefeitura-rio / 点赞 271 / 下载 112,371 | 397B 总参数的 Qwen3.5 MoE 开放版，政府背景开源，对研究**大规模 MoE 的民主化对齐与公共利益导向 RLHF** 具有政策研究意义。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth / 点赞 261 / 下载 80,118 | Unsloth 对 DiffusionGemma 的 GGUF 适配，其量化工具链对研究**多模态模型的高效微调基础设施**有直接工具价值。 |

---

## 研究生态信号

**Gemma-4 统一架构**正成为多模态研究的事实标准，其 any-to-any 设计模糊了传统 VLM 的"视觉编码器+投影层"边界，可能重塑 OCR 和文档理解的模型选型逻辑。Qwen3.6 生态呈现**极端两极化**：官方版本与大量"Uncensored"微调版并行流通，后者下载量常超官方，反映开源对齐的**防御-攻击不对称性**加剧——攻击方（越狱微调）的边际成本远低于防御方（安全 RLHF）。MoE 架构已从效率选项演变为能力标配（DeepSeek-V4、Gemma-4-A4B、Qwen3.5/3.6-MoE），但其在视觉-语言任务中的**专家分配可视化与可解释性**仍是研究空白。国产模型（MiniMax、Kimi、DeepSeek、Qwen）在视觉-代码-长上下文交叉领域形成集群优势，而欧美厂商（Google、Cohere、NVIDIA）更聚焦架构统一与效率工具。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | **多模态统一架构的基准锚点**：原生 any-to-any 设计使其成为检验"拼接式 VLM 是否必要"的理想对照；可系统评测其在文档 OCR、表格理解、公式识别等任务上的 zero-shot 能力，并与 Qwen-VL、InternVL 等拼接架构对比幻觉率。 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | **推理与对齐的前沿交汇**：V4 代的 MoE 路由机制、推理时扩展策略及 Pro 版本的后训练优化（推测为 RL 增强）均待解剖；其开源权重允许复现长上下文推理的注意力模式，对研究"推理长度与幻觉概率的关联"至关重要。 |
| ⭐⭐☆ | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **对齐研究的"对抗样本库"**：250 万+下载量的"去审查"模型并非单纯伦理问题，而是研究 RLHF 脆弱性的活体标本——可通过对比其与官方 Qwen3.6 的权重差异、输出分布偏移，定位安全对齐的"单点故障"，并反向设计更鲁棒的对齐目标函数。 |

---

*日报基于 2026-06-15 Hugging Face Hub 周点赞排序数据生成。模型链接均为直接可访问的 HuggingFace URL。*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*