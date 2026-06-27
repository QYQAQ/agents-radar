# Hugging Face 热门模型日报 2026-06-27

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-27 00:33 UTC

---

# Hugging Face 研究模型日报 | 2026-06-27

---

## 今日速览

本周 Hugging Face 生态呈现**多模态文档理解**与**后训练对齐**的双重爆发态势。百度开源的 **Unlimited-OCR** 以 1,040 点赞领跑 OCR 领域，标志着通用端到端文档识别进入新阶段；MiniMax 的 **MiniMax-M3** 与 NVIDIA 的 **LocateAnything-3B** 分别推动视觉语言模型向细粒度定位与多模态推理纵深发展。值得注意的是，**HauhauCS** 的 Uncensored 系列（Qwen3.6-35B-A3B、Gemma4-12B-QAT）以极高下载量揭示社区对**后训练去对齐（de-alignment）**与**量化感知训练（QAT）**的旺盛需求，而 **datalab-to/lift** 专注 PDF 结构化理解，为学术文档解析提供了轻量替代方案。长上下文方面，**Qwythos-9B-Claude-Mythos-5-1M** 以 1M 上下文窗口成为研究极端长度推理的潜在基准。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu / 1,040⭐ / 134,146↓ | 百度开源的通用 OCR 端到端模型，支持"无限"长度文本行识别，直接对标传统分页式 OCR 范式，为 HMER（手写数学表达式识别）与复杂版面分析提供统一编码器-解码器架构，是文档理解基础模型研究的关键基线。 |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to / 158⭐ / 6,054↓ | 基于 Qwen3.5 的 PDF 图像-文本理解模型，专注学术论文与结构化文档的细粒度解析，为科研文献自动化处理与公式-表格联合提取提供轻量级开源方案，适合作为文档 VLM 的下游微调起点。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI / 1,246⭐ / 169,951↓ | MiniMax 第三代多模态模型，采用原生多模态架构（非拼接式），在视觉问答与图文推理上展现强跨模态对齐能力，其视觉-语言联合训练策略对研究模态间表示统一具有参考价值。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia / 2,383⭐ / 494,756↓ | NVIDIA 开源的细粒度视觉定位模型，支持自然语言指代表达下的任意目标定位，3B 参数实现高效推理，为视觉语言模型中的**空间推理幻觉**问题提供可解释的定位监督信号，是 VLM  grounding 研究的重要工具。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 2,263⭐ / 3,453,492↓ | 基于 Qwen3.6-35B-A3B MoE 的激进去对齐版本，移除安全微调层以暴露原始模型分布，**极高下载量**反映社区对"对齐税"研究的关注，可作为**幻觉缓解**与**对齐鲁棒性**的负向基线或红队测试平台。 |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS / 91⭐ / 23,772↓ | Gemma-4 12B 的量化感知训练（QAT）去对齐版本，结合 **4-bit 量化精度保持**与**平衡式去对齐**，为研究后训练量化与对齐干扰的交互效应提供独特实验载体。 |
| **[Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-Compat-MTP-GGUF)** | Jackrong / 93⭐ / 35,027↓ | 支持多模态（MTP）的 Qwen3.6 代码兼容版 GGUF，融合视觉理解与代码生成，适合研究**图文混合编程场景**下的跨模态推理与工具使用幻觉。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | empero-ai / 446⭐ / 20,346↓ | 9B 参数实现 **1M 令牌上下文窗口**，采用 Claude 风格的推理模式蒸馏，是长上下文**推理效率**与**注意力机制可扩展性**研究的理想小型化实验平台。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai / 583⭐ / 486,810↓ | 上述模型的 GGUF 量化版，极高下载量验证社区对**长上下文本地部署**的迫切需求，为研究量化对远距离依赖建模的影响提供数据点。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI / 731⭐ / 54,638↓ | 3B 参数数学推理专用模型，基于 Qwen2 架构优化，展现小模型在**结构化思维链**任务上的潜力，为研究推理能力的规模效率权衡提供对照。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft / 355⭐ / 5,735↓ | 微软 4B 参数快速上下文处理模型，专为"Explorer SubAgent"场景设计，探索**动态上下文压缩**与**检索增强推理**的边界，是长上下文效率优化的前沿尝试。 |
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org / 2,589⭐ / 83,589↓ | 智谱 GLM-5.2 采用 MoE+DSA（Dynamic Sparse Attention）架构，在保持全模态能力的同时扩展上下文，其**稀疏注意力机制**对长上下文计算复杂度研究具有方法论意义。 |
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth / 410⭐ / 107,553↓ | Unsloth 社区优化的 GLM-5.2 量化版，支持高效本地推理，为验证 MoE 架构在消费级硬件上的长上下文可行性提供工具。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 / 2,398⭐ / 516,333↓ | Gemma-4 12B 的多阶段合成数据微调版（Fable5+Composer2.5），展现**合成数据驱动的 SFT** 在代码推理上的强大效果，其训练配方对研究数据课程与能力涌现具有参考价值。 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 / 684⭐ / 186,663↓ | 上述模型的 agentic 增强版，引入工具使用与终端交互能力，v2-3.5x-tau2 的命名暗示**温度参数或采样策略的系统化调优**，为研究后训练中的探索-利用权衡提供案例。 |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai / 135⭐ / 5,445↓ | 对 yuxinlu1 版本的**消融对齐（abliteration）**处理，移除特定行为模式的同时保留代码能力，是研究**选择性对齐擦除**与**能力保持**冲突的精细实验。 |
| **[deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)** / **[GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)** / **[9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)** / **[9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)** / **[397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B)** | deepreinforce-ai / 121-230⭐ / 1,005-3,002↓ | 完整 Ornith 系列覆盖 9B 至 397B（MoE），基于 Qwen3.5 架构经深度后训练优化，MIT 许可证与端点兼容性强调**可部署性**，其规模谱系为研究后训练扩展律（post-training scaling laws）提供独特数据。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)** | nvidia / 707⭐ / 56,434↓ | NVIDIA Nemotron 3.5 系列的流式 ASR 模型，虽非直接文本生成模型，但其**流式解码架构**与**实时置信度校准**机制对研究语音-文本转录中的**时间维度幻觉**（如虚构未发音内容）具有借鉴意义。 |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen / 320⭐ / 13,186↓ | 通义千问官方 Agent 世界模型，35B-A3B MoE 架构专为多步工具调用与规划优化，内置**自我验证与重规划**机制，是研究**工具使用幻觉**与**行动-观察循环中的事实保持**的重要基线。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 / 点赞 / 下载 | 一句话说明 |
|:---|:---|:---|
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia / 361⭐ / 4,812,629↓ | NVIDIA 官方 NVFP4 精度优化版 Qwen3.6，**极高下载量**验证社区对硬件-软件协同优化的需求，其 ModelOpt 工具链为研究**量化训练与推理一致性**提供生产级基础设施。 |
| **[nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4)** | nvidia / 87⭐ / 441↓ | GLM-5.2 的 NVFP4 版本，与上述模型共同构成 NVIDIA 的**低精度原生模型生态**，为研究 4-bit 浮点格式对 MoE 稀疏激活模式的保真度影响提供实验条件。 |

---

## 研究生态信号

**Qwen 家族主导多模态与后训练创新**：Qwen3.5/3.6 架构成为本周最活跃的研究基座，覆盖视觉语言（lift、Ornith）、极端去对齐（HauhauCS）、长上下文（Qwythos）及硬件协同优化（NVIDIA NVFP4）等多元方向，显示其模块化设计对研究社区的强吸引力。**Gemma-4 12B 则成为合成数据 SFT 与消融对齐的实验田**，yuxinlu1 与 huihui-ai 的连续迭代揭示社区对"训练配方透明化"的渴求。视觉语言领域呈现**开源权重追赶闭源能力**的态势：MiniMax-M3 与 LocateAnything-3B 在特定维度（原生多模态、细粒度定位）展现差异化竞争力，但 1M 上下文与复杂推理仍由 Claude 蒸馏版（Qwythos）间接代表。值得注意的是，**"Uncensored"标签的爆发式增长**（HauhauCS 系列合计超 350 万下载）不仅是社区需求信号，更暗示**对齐研究亟需更精细的评估框架**——当前简单二分法（对齐/未对齐）已无法刻画模型行为的连续谱系。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | **端到端 OCR 的范式转变**：传统 HMER 与文档理解依赖检测-识别分阶段流水线，Unlimited-OCR 的"无限长度"单阶段设计可能重塑版面分析的基础假设。建议验证其在复杂数学公式（多行、嵌套结构）上的零样本表现，并与 Nougat、GOT-OCR2 进行错误模式对比分析，探究其是否真正消除了分阶段累积误差。 |
| ⭐⭐⭐ | **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** | **1M 上下文的小型化实验平台**：极端长上下文研究长期受限于 API 访问与闭源黑箱，9B 参数+1M 窗口的开源权重使**本地可控实验**成为可能。建议构建"针在干草堆中"的变体测试（如多跳推理、长距离指代消解），量化其注意力稀疏模式，并探索 KV Cache 压缩对远距离依赖的破坏阈值。 |
| ⭐⭐☆ | **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | **选择性对齐擦除的精细案例**：相较于 HauhauCS 的"Aggressive"全面去对齐，该版本的"abliterated"标签暗示**靶向移除特定行为模式**而保留代码能力。建议系统对比其与原版、全面去对齐版在代码正确性、有害输出率、以及**特定能力维度（如数学证明 vs. 系统入侵代码）**的精细差异，为"对齐可逆性"与"能力-安全权衡"提供实证数据。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*