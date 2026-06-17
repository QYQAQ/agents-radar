# Hugging Face 热门模型日报 2026-06-17

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-17 00:38 UTC

---

# Hugging Face 研究模型日报 | 2026-06-17

---

## 今日速览

今日 Hugging Face 热门模型中，**多模态统一架构**成为最显著趋势：Google 的 Gemma-4 系列以"any-to-any"范式打破模态边界，MiniMax-M3 和 Kimi-K2.7-Code 推动视觉语言模型的代码推理能力，而 Qwen3.6 系列（尤其是 35B-A3B MoE 变体）持续主导开源多模态生态。值得注意的是，**长上下文与推理**领域出现 DeepSeek-V4-Pro 和微软 FastContext-1.0-4B-SFT 等专门优化上下文效率的模型，但**OCR/HMER 专用模型仍显稀缺**，视觉语言模型的文档理解能力多隐含于通用 VLM 中。后训练对齐方面，CohereLabs North-Mini-Code-1.0 和各类"Uncensored"微调模型反映了开源社区对偏好微调和安全对齐的活跃实验，却也暴露出**幻觉缓解与对齐质量之间的张力**。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

> ⚠️ **本日无专门 OCR/HMER 模型进入热门榜**。以下模型的视觉编码器能力可间接支持文档理解研究：

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | Google / 点赞 944 / 下载 375,974 | 扩散式 Gemma 多模态模型，将扩散生成与语言理解统一；其图像-文本联合表征可能为**公式生成与识别**提供新的逆向推理路径（从文本生成公式图像，再验证结构一致性）。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai / 点赞 800 / 下载 102,206 | 支持图像输入的代码模型，可处理截图中的代码/表格/公式；**HMER 研究者可测试其数学公式图像→LaTeX 的转换精度**，评估隐式 OCR 能力。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS / 点赞 1,887 / 下载 2,716,651 | 激进微调的 Qwen3.6 视觉 MoE；Uncensored 标签暗示**安全对齐被削弱**，但高下载量使其成为研究**对齐移除后幻觉行为**的对照样本。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | Google / 点赞 1,053 / 下载 1,223,383 | **首个"any-to-any"统一架构**，支持图像、文本、音频任意模态输入输出；对 OCR 研究的意义在于其**统一 tokenizer 可能实现像素级文本嵌入**，消除传统 OCR 管道的模态转换损耗。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI / 点赞 1,010 / 下载 25,064 | 新兴 VLM 系列，标签含"agent"与"multimodal"；低下载/点赞比暗示早期阶段，适合研究**新架构的涌现能力曲线**与训练数据配比。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | NVIDIA / 点赞 2,101 / 下载 98,698 | 3B 参数的视觉定位模型，**空间推理与细粒度视觉理解**的核心基座；对文档版面分析研究可直接迁移其定位机制至文本区域检测。 |
| **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen / 点赞 2,135 / 下载 3,360,615 | 官方 MoE 视觉语言模型，**开源社区事实标准**；其 3.36M 下载量证明生态成熟度，是验证 OCR/VLM 基准的首选基线。 |
| **[unsloth/MiniMax-M3-GGUF](https://huggingface.co/unsloth/MiniMax-M3-GGUF)** | unsloth / 点赞 92 / 下载 18,206 | MiniMax-M3 的量化版本，标签"agent"突出；适合研究**端侧多模态推理的幻觉敏感性**与量化对视觉特征保真度的影响。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | DeepSeek / 点赞 4,895 / 下载 2,829,747 | **今日最高点赞模型**，V4 架构延续 MLA 注意力优化；对长上下文研究的关键价值在于其**推理阶段的 KV Cache 压缩机制**与上下文外推能力的可解释性分析。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | Microsoft / 点赞 159 / 下载 192 | 明确标注"Explorer SubAgent"的轻量级上下文模型；**极低下载量但高度针对性**，是研究"上下文效率 vs 推理深度"权衡的实验平台。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI / 点赞 172 / 下载 0 | 基于 Qwen2 的数学专用模型，零下载显示未正式发布；标签"math"指向**形式化推理与数学证明**的专门优化，适合 HMER 下游任务的符号推理增强。 |
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 / 点赞 1,160 / 下载 60,921 | 社区融合的代码推理模型，融合 Fable5/Composer2.5 技术；标签"reasoning"与"gguf"并存，适合研究**结构化推理（如代码→公式转换）的量化鲁棒性**。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs / 点赞 412 / 下载 12,129 | Cohere2 MoE 架构的代码对齐模型；作为**主流实验室的后训练公开样本**，其 SFT/DPO 数据配比与偏好模型构建方法具有方法论参考价值。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS / 点赞 335 / 下载 76,044 | 对 Gemma-4 的"去对齐"激进微调；**对齐研究的负面样本**，可用于量化分析安全微调移除后模型在视觉输入上的置信度校准漂移。 |
| **[DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF](https://huggingface.co/DavidAU/Qwen3.6-40B-Claude-4.6-Opus-Deckard-Heretic-Uncensored-Thinking-NEO-CODE-Di-IMatrix-MAX-GGUF)** | DavidAU / 点赞 370 / 下载 366,279 | 极端命名的多层融合模型，集成 Claude 风格对齐与"Heretic"去约束；**对齐研究的混沌实验体**，适合分析多源偏好信号冲突时的行为涌现。 |

---

### 👁️ 幻觉缓解

> ⚠️ **无直接标注"幻觉缓解"的模型**，但以下模型的架构选择隐含相关设计：

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | Google / 点赞 944 / 下载 375,974 | 扩散模型的**迭代去噪机制天然提供多步验证机会**，其图像生成过程可反向用于"视觉事实核查"——生成与输入图像的残差可作为幻觉检测信号。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | NVIDIA / 点赞 2,101 / 下载 98,698 | 显式空间定位要求**视觉主张与像素位置绑定**，其 grounding 机制可直接转化为"可验证的视觉声明"，降低开放式生成的幻觉风险。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth / 点赞 287 / 下载 120,435 | Unsloth 优化的扩散量化版本；其**4-bit 量化下的扩散稳定性**是部署研究的关键基准，影响多模态幻觉检测系统的实时可行性。 |
| **[unsloth/Kimi-K2.7-Code-GGUF](https://huggingface.co/unsloth/Kimi-K2.7-Code-GGUF)** | unsloth / 点赞 119 / 下载 16,817 | Kimi 系列的社区量化版，标签"compressed-tensors"；适合作为**长上下文模型压缩与推理效率**的标准化测试平台。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** | unsloth / 点赞 633 / 下载 1,009,602 | Gemma-4 any-to-any 的 GGUF 实现，百万级下载；**多模态统一架构的端侧部署基础设施**，是验证"模态转换是否引入幻觉"的理想工具。 |

---

## 研究生态信号

**Qwen 家族**以 Qwen3.6-35B-A3B 及其衍生微调模型（HauhauCS、DavidAU、Jackrong 等）形成绝对主导，官方+社区的双重生态使其成为多模态对齐研究的"默认实验平台"。**Gemma-4** 的 any-to-any 架构代表 Google 对模态统一的技术赌注，但社区微调（如 OBLITERATED）暴露其**安全对齐的脆弱性**。DeepSeek-V4-Pro 延续长上下文效率路线，与微软 FastContext 形成"大参数 vs 小参数"的上下文研究两极。值得注意的是，**专门 OCR/HMER 模型仍缺席热门榜**，文档理解需求被通用 VLM 吸收，这可能暗示：要么该领域已成熟为"隐含能力"，要么**细粒度文本识别仍是未被解决的开放问题**，需要研究者从通用 VLM 中剥离评估。幻觉缓解方面，"Uncensored"微调模型的泛滥（HauhauCS、DavidAU、OBLITERATUS）实际上构成了**大规模的对齐消融实验**，为系统研究"对齐如何影响事实性"提供了意外丰富的数据。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | **any-to-any 架构的 OCR 原生潜力**：传统 OCR 管道（图像→文本→理解）的模态转换损耗可被统一 tokenizer 消除。建议设计"像素级文本识别"探针实验，验证其是否内建字符级视觉感知，这将决定未来 OCR 研究是否需要独立编码器。 |
| ⭐⭐⭐ | **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | **长上下文效率的极端案例**：4B 参数+SFT 标签+Explorer SubAgent 架构，是研究"上下文长度与推理深度权衡"的最小可行实验平台。特别适合验证 HMER 中长公式序列的上下文需求下限，以及压缩注意力机制对符号结构保持的影响。 |
| ⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **视觉定位→文档版面分析的迁移**：3B 参数实现的高精度空间定位，可直接微调用于文本区域检测、公式边界框定位、表格结构识别。其 NVIDIA 官方背书意味着训练代码与数据管道可能后续开源，值得提前建立评估基准。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*