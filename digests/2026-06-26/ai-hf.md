# Hugging Face 热门模型日报 2026-06-26

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-26 00:35 UTC

---

# Hugging Face 研究模型日报 | 2026-06-26

## 今日速览

本周 Hugging Face 生态呈现**多模态文档理解**与**长上下文推理**双轨并进的态势。百度发布的 **Unlimited-OCR** 以近 9 万下载量成为 OCR 领域焦点，其"无限制"文档处理能力直指复杂版面分析痛点；**MiniMax-M3** 与 **Kimi-K2.7-Code** 分别代表视觉语言与代码多模态的前沿进展，后者突破 50 万下载验证工业需求。后训练对齐方面，**HauhauCS** 系列通过 QAT 量化与"去审查"微调持续活跃，而 **GLM-5.2** 的 MoE+DSA 架构与 **DeepSeek-V4-Pro** 的 5061 点赞登顶，标志着长上下文推理模型正从架构创新走向规模化应用。值得关注的是，**datalab-to/lift** 等 PDF 专用模型涌现，暗示文档智能正从通用 VLM 向垂直场景精细化演进。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | baidu | 890 | 70,743 | 百度开源的"无限制"OCR 模型，突破传统文本行识别局限，支持任意复杂版面、多栏混排与图文交织场景；**与 HMER/文档理解研究高度相关**，其 feature-extraction 标签暗示可提取结构化文档表征，为公式识别与版面分析提供新基线。 |
| **[datalab-to/lift](https://huggingface.co/datalab-to/lift)** | datalab-to | 152 | 5,189 | 基于 Qwen3.5 架构的 PDF 专用理解模型，针对学术论文与技术文档优化；**研究相关性**：直接服务于文档智能中的数学公式、表格、图表联合解析任务，可作为 HMER 系统的文档级预处理模块。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 1,241 | 154,350 | MiniMax 第三代多模态模型，采用专用 `minimax_m3_vl` 架构；**研究相关性**：视觉语言融合的新架构范式，其高下载量验证多模态推理的工业需求，为跨模态对齐与视觉指令微调研究提供对比基线。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 992 | 502,106 | Kimi K2.5 系列的代码特化多模态模型，支持图像输入的编程任务；**研究相关性**：突破 50 万下载的代码-视觉联合推理模型，其 `image-feature-extraction` 与 `compressed-tensors` 标签暗示高效视觉编码，对多模态推理中的表征压缩与幻觉缓解有直接借鉴。 |
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,176 | 2,187,644 | Gemma 4 统一架构的指令微调版本，官方标注 `any-to-any` 任务类型；**研究相关性**：Google 官方统一多模态基座，其 218 万下载量为开源 VLM 研究提供最大公约数基线，any-to-any 范式对跨模态对齐研究具有范式意义。 |
| **[HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced)** | HauhauCS | 83 | 15,128 | 对 Gemma-4-12B 实施 QAT（量化感知训练）与"平衡去审查"的社区微调版；**研究相关性**：QAT 量化与多模态能力的兼容性探索，为边缘部署场景下的视觉语言模型后训练对齐提供实践参考。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,363 | 407,838 | NVIDIA 开源的 3B 参数视觉定位模型，支持任意物体的自然语言定位；**研究相关性**：视觉 grounding 的轻量化解法，其 `image-feature-extraction` 能力可作为多模态推理中的空间感知模块，缓解 VLM 的指代幻觉问题。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 2,234 | 3,520,206 | Qwen3.6 MoE 架构的激进"去审查"微调版，本周下载量超 350 万居首；**研究相关性**：MoE 多模态模型的后训练对齐极端案例，其 `vision` 标签与超高下载量反映社区对"开放"多模态权重的需求，但对齐安全性与幻觉风险的权衡值得批判性研究。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | zai-org | 2,476 | 67,107 | 智谱 GLM-5.2，采用 `glm_moe_dsa` 架构（MoE + Dynamic Sparse Attention）；**研究相关性**：DSA 动态稀疏注意力机制直接针对长上下文效率瓶颈，其 2,476 点赞居首表明长上下文架构创新受高度关注，为长序列推理的注意力机制研究提供新范式。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 5,061 | 1,878,217 | DeepSeek V4 专业版，本周点赞数登顶（5,061）；**研究相关性**：长上下文推理的旗舰基座，其 `conversational` 标签与近 200 万下载量验证其在复杂推理任务中的可靠性，可作为长上下文幻觉评估的强基准。 |
| **[microsoft/FastContext-1.0-4B-SFT](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)** | microsoft | 345 | 5,276 | 微软 4B 参数快速上下文模型，基于 Qwen3 的 SFT 版本；**研究相关性**："FastContext"命名暗示长上下文处理的效率优化，其 `Explorer SubAgent` 标签揭示子代理架构，为长文本分块推理与层级注意力研究提供轻量参考。 |
| **[WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)** | WeiboAI | 715 | 51,717 | 3B 参数数学推理专用模型，基于 Qwen2 架构；**研究相关性**：小参数规模的数学推理优化，直接关联推理增强与思维链研究，其 `math` 标签与中等下载量表明垂直推理场景的实用需求。 |
| **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)** / **[GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)** | empero-ai | 390 / 476 | 10,160 / 134,294 | Qwen3.5 架构的 1M 长上下文微调系列，命名融合"Claude"与"Mythos"暗示长文本叙事理解；**研究相关性**：1M 上下文窗口的社区实践，GGUF 版本 13 万下载量验证长上下文本地部署需求，为超长序列的注意力衰减与位置编码研究提供测试平台。 |
| **[Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)** | Qwen | 239 | 3,389 | 官方 Qwen3.5 MoE 的 Agent 特化版，35B 激活 3B；**研究相关性**：MoE 架构与 Agent 推理的结合，多工具调用场景下的长上下文状态维护，为 Agent 系统中的幻觉累积与一致性验证研究提供官方基线。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)** | yuxinlu1 | 2,363 | 495,813 | Gemma-4 的多版本融合微调（Fable5 + Composer2.5），GGUF 量化版；**研究相关性**：社区"融合微调"（model merging）的典型实践，高下载量反映后训练组合优化的有效性，为 DPO/SFT 的多策略融合研究提供案例。 |
| **[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)** | yuxinlu1 | 614 | 165,187 | 上述模型的 Agentic 增强 v2 版，引入 `tau2` 温度参数与 `3.5x` 规模因子；**研究相关性**：后训练中的超参数系统探索（temperature scaling + 模型扩展），`agentic` 与 `terminal` 标签指向工具调用对齐，为 RLHF 中的探索-利用权衡研究提供实证。 |
| **[huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-coder-fable5-composer2.5-v1-abliterated)** | huihui-ai | 127 | 4,874 | "Abliterated"（消融/去限制）版本的 Gemma-4 代码融合模型；**研究相关性**：`abliterated` 标签代表对齐移除（alignment erasure）的后训练技术，直接关联 AI 安全与可控性研究，其视觉能力（`image-text-to-text`）扩展了多模态对齐审查的维度。 |
| **[nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)** | nvidia | 340 | 4,602,255 | NVIDIA 官方 NVFP4 精度优化的 Qwen3.6 MoE；**研究相关性**：本周最高下载量（460 万），`Model Optimizer` 与 `ModelOpt` 标签代表后训练量化与部署优化，为对齐模型的边缘部署与推理效率研究提供基础设施参考。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 1,176 | 2,187,644 | （同上，any-to-any 统一架构）**幻觉相关性**：Google 官方统一多模态基座的指令对齐版本，其大规模部署为研究多模态幻觉（如视觉指代错误、描述不一致）提供可控实验平台。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 2,363 | 407,838 | （同上，视觉定位模型）**幻觉相关性**：显式视觉 grounding 机制是缓解 VLM 空间幻觉的核心路径，其 3B 轻量设计证明定位精度与参数效率可兼得，为"grounding for hallucination reduction"研究提供直接工具。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| **[unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF)** | unsloth | 384 | 88,915 | Unsloth 社区对 GLM-5.2 的 GGUF 量化适配；**研究相关性**：Unsloth 作为高效微调框架的代表，其量化版本为长上下文模型的低成本实验提供基础设施，支持研究者快速验证 MoE+DSA 架构的下游任务表现。 |
| **[deepreinforce-ai/Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)** | deepreinforce-ai | 80 | 0 | 新兴研究组织的 35B 模型 GGUF 版，MIT 许可；**研究相关性**：`endpoints_compatible` 标签暗示 API 标准化努力，零下载量反映新组织冷启动，但 MIT 许可与基础设施标签值得关注开源模型服务标准化研究。 |

---

## 研究生态信号

**Qwen 家族**在本周期呈现绝对主导态势：官方 Qwen3.5/3.6 系列覆盖从 9B 到 35B MoE 的全尺度，社区衍生（HauhauCS、yuxinlu1、Jackrong）形成繁荣的"后训练生态"。**Gemma-4** 作为 Google 统一多模态架构的新旗舰，正以 12B 规模快速积累社区微调（fable5/composer2.5 等融合实验），其 `any-to-any` 官方定位与社区的 `uncensored/abliterated` 变体形成张力。视觉语言领域，**开源权重已显著压制闭源趋势**：MiniMax-M3、Kimi-K2.7-Code 等原"半闭源"厂商全面拥抱 Hugging Face，而 NVIDIA 通过 LocateAnything、NVFP4 优化等从基础设施层强化开源生态。文档理解方面，**垂直细分**成为明确趋势：Unlimited-OCR 的"无限制"定位与 lift 的 PDF 专精，标志着通用 VLM 向"文档智能"子领域的专业化下沉；幻觉缓解尚未出现独立标签模型，但 LocateAnything 的 grounding 机制与 Kimi-K2.7-Code 的 compressed-tensors 暗示"效率+精度"双驱动的隐式幻觉控制路径。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)** | **HMER 研究的直接扩展**。传统公式识别局限于单行/单栏文本，而"无限制"版面分析是数学公式嵌入复杂文档（论文、教材、试卷）的必经瓶颈。其 feature-extraction 输出可作为 HMER 系统的结构化输入，探索"文档级→公式级"级联架构的误差传播与联合优化。 |
| ⭐⭐⭐ | **[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)** | **长上下文推理的架构创新源头**。Dynamic Sparse Attention（DSA）在 MoE 框架下的实现细节尚未公开，但其 2,476 点赞与官方背书使其成为研究长序列注意力效率的必跟基线。建议对比其与 Qwythos-1M 在长文本数学证明、代码依赖分析等任务上的注意力模式可视化，验证稀疏机制对推理一致性的影响。 |
| ⭐⭐☆ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **幻觉缓解的轻量化路径**。3B 参数实现视觉 grounding，与 35B+ VLM 形成数量级效率差异。建议将其 grounding 输出作为约束条件接入多模态解码过程，验证"显式定位→隐式描述"的幻觉抑制效果，探索小模型辅助大模型的事实校验范式。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*