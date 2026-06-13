# Hugging Face 热门模型日报 2026-06-13

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-13 00:38 UTC

---

# Hugging Face 研究模型日报 | 2026-06-13

## 今日速览

本周 Hugging Face 热门模型呈现**多模态统一化**与**推理能力强化**两大趋势。Google Gemma-4 系列以 "any-to-any" 架构成为视觉语言研究的核心基础设施，其原生图像-文本交错处理能力为文档理解（OCR）和视觉推理提供了新的基线。DeepSeek-V4-Pro 以近 4800 点赞领跑，其 MoE 架构与对话优化设计对后训练对齐研究具有重要参考价值。NVIDIA LocateAnything-3B 的开放下载量突破 14.9 万，标志着视觉定位与细粒度理解成为多模态研究的热点。值得注意的是，Moonshot Kimi-K2.7-Code 虽下载量为零，但其长上下文代码推理能力值得关注。Unsloth 对 Gemma-4 系列的 GGUF/QAT 量化生态迅速跟进，为边缘部署与高效推理研究提供了工具链支持。

---

## 热门模型（按研究相关性分类）

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 研究相关性 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 967⭐ / 911,544↓ |
| | | **原生 any-to-any 架构**，支持图像-文本交错输入与统一输出，为文档理解、视觉推理和跨模态对齐研究提供开源强基线。其高下载量反映社区对统一多模态架构的强烈需求。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)** | google | 527⭐ / 198,271↓ |
| | | **基础版 any-to-any 模型**，去除指令微调后更适合研究者的**后训练实验**（SFT/RLHF/DPO），可对比分析指令对齐对多模态能力的影响。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia | 1,925⭐ / 149,206↓ |
| | | **视觉定位与细粒度理解模型**，3B 参数实现高效定位，与 OCR/文档理解中的**区域级文本识别**和**版面分析**高度相关，可探索视觉-语言对齐的粒度问题。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | google | 614⭐ / 20,669↓ |
| | | **扩散模型与语言模型融合**，26B 激活 4B 的稀疏架构，为**视觉生成与理解统一**研究提供新路径，相关于多模态推理中的生成式理解范式。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)** | moonshotai | 337⭐ / 0↓ |
| | | **长上下文代码多模态模型**，K2.7 系列以超长上下文著称，虽下载量为零（可能为预览版），但其**代码+视觉的长程推理**能力对文档级理解研究极具价值。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)** | MiniMaxAI | 252⭐ / 442↓ |
| | | **MiniMax 第三代视觉语言模型**，低下载量但架构迭代值得关注，可追踪其多模态对齐策略与幻觉控制机制。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 1,722⭐ / 2,393,894↓ |
| | | **社区激进微调版本**，极高下载量反映"去对齐"需求，但恰恰是**对齐研究的对照样本**——可分析过度安全对齐与性能权衡，以及幻觉缓解的边界条件。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)** / **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)** / **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)** | unsloth | 570⭐/206⭐/148⭐ / 836,531↓/208,889↓/221,174↓ |
| | | **Gemma-4 量化生态**，QAT 量化保持多模态性能，为**高效推理与边缘部署**研究提供工具，支持长上下文模型的资源优化实验。 |
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)** | huihui-ai | 147⭐ / 8,013↓ |
| | | **"Abliterated" 去对齐版本**，移除拒绝机制，可作为**RLHF 对齐效果消融实验**的现成对照，研究安全对齐对多模态幻觉的影响。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)** | Jackrong | 116⭐ / 0↓ |
| | | **Qwen 系视觉代码模型 GGUF 化**，MTP（Multi-Token Prediction）与视觉结合，探索**代码生成中的多模态推理**与长上下文效率。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 研究相关性 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,796⭐ / 3,384,418↓ |
| | | **本周最热模型**，DeepSeek V4 Pro 的 MoE 架构与**对话优化**设计，其推理能力与长上下文处理为**后训练对齐与幻觉缓解**研究提供强基线，可分析其 RLHF 策略与事实性校准机制。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)** | CohereLabs | 335⭐ / 4,054↓ |
| | | **Cohere MoE 代码模型**，"Mini" 但保持性能，适合研究**高效架构下的推理能力**与代码领域的幻觉问题（如幻觉 API 调用）。 |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)** / **[nex-agi/Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini)** | nex-agi | 223⭐/180⭐ / 2,551↓/2,839↓ |
| | | **Qwen3.5 MoE 衍生模型**，Pro/mini 对比适合**规模-性能-幻觉权衡**研究，其视觉-文本任务标签暗示多模态推理尝试。 |
| **[XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)** | XiaomiMiMo | 97⭐ / 2,607↓ |
| | | **小米 Agent 模型 FP4 量化版**，"DFlash" 可能指动态推理，与**Agent 幻觉**（工具调用错误、规划幻觉）研究直接相关。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 研究相关性 |
|:---|:---|:---|
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)** | OBLITERATUS | 254⭐ / 43,578↓ |
| | | **Gemma-4 的"去对齐"社区版本**，与官方 it 版形成**完美对照组**，可系统研究安全对齐对多模态性能、幻觉率和有用性的影响。 |
| **[google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf)** | google | 133⭐ / 175,635↓ |
| | | **官方 QAT 量化版本**，验证后训练量化对**对齐稳定性**的影响，研究量化是否破坏 RLHF 优化的奖励模型分布。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

> *注：本周无直接标注"幻觉缓解"的模型，但以下模型隐含相关研究价值*

| 模型 | 作者/数据 | 研究相关性 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | google | 967⭐ / 911,544↓ |
| | | **any-to-any 架构的幻觉风险**：统一生成-理解模型需验证视觉输入是否减少**语言幻觉**（如虚构图像内容），或引入新型**跨模态幻觉**。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,796⭐ / 3,384,418↓ |
| | | 高下载量的 MoE 对话模型，其**事实性校准机制**值得拆解，可对比分析其拒绝行为与过度自信模式。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 研究相关性 |
|:---|:---|:---|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)** | unsloth | 214⭐ / 17,666↓ |
| | | **Unsloth 量化生态的扩散模型支持**，为**高效多模态训练/推理框架**研究提供工具，降低扩散+语言联合训练的门槛。 |

---

## 研究生态信号

**Gemma-4 家族成为多模态研究新基础设施**：Google 以 any-to-any 统一架构强势切入，官方与社区（Unsloth、OBLITERATUS、huihui-ai）形成完整生态，覆盖从全精度到 QAT/GGUF 量化的全链路，标志着**开源视觉语言模型进入"统一架构+社区衍生"的新阶段**。NVIDIA LocateAnything-3B 的高下载量（14.9万）验证**细粒度视觉定位**从研究概念走向工程需求，与 OCR 中的区域级文本识别直接衔接。值得注意的是，**"去对齐"社区版本异常活跃**（HauhauCS、OBLITERATUS、huihui-ai），极高下载量揭示对齐研究中的"过度安全-性能"张力，为幻觉缓解研究提供了反向验证样本。闭源方面，Moonshot Kimi-K2.7-Code 与 MiniMax-M3 保持架构神秘感，但开源权重（Gemma-4、DeepSeek-V4-Pro）在下载量上占据绝对主导，**开源生态在视觉语言领域已形成自我强化的工具链**。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)** | **多模态统一架构的基准研究**：any-to-any 设计允许直接对比"分离编码器"（如 CLIP+LLM）与"统一架构"在文档理解、公式识别（OCR/HMER）中的幻觉差异，且可复用其 91 万下载量的社区反馈进行错误分析。 |
| ⭐⭐⭐ | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **细粒度视觉定位与 OCR 的交叉**：3B 参数实现开放域定位，可探索将其视觉定位能力迁移至**版面分析、表格结构识别、公式区域检测**，解决当前文档 OCR 中"检测到文本但定位不准"的痛点。 |
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | **长上下文对齐与幻觉的规模化研究**：作为本周最热模型，其 MoE 架构下的 RLHF 策略、事实性校准机制值得拆解，可设计实验验证其**长文档理解中的事实一致性**与**跨段落推理的幻觉率**。 |

---

*日报生成日期：2026-06-13 | 数据来源：Hugging Face Hub 周点赞排序*

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*