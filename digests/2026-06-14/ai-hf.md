# Hugging Face 热门模型日报 2026-06-14

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-14 00:35 UTC

---

# Hugging Face 研究模型日报 | 2026-06-14

## 今日速览

本周 Hugging Face 生态呈现**多模态统一架构加速收敛**与**后训练对齐技术活跃**两大趋势。Google Gemma-4 系列以"any-to-any"范式成为视觉语言研究的核心基座，衍生出大量微调与量化变体；Moonshot Kimi-K2.7-Code 和 MiniMax-M3 持续推动长上下文多模态推理边界；值得关注的是，"abliterated/uncensored"类后训练模型数量显著增加，反映对齐与安全性研究的博弈张力。DiffusionGemma 将扩散模型与 LLM 统一，为视觉推理的幻觉缓解提供了新架构思路。NVIDIA LocateAnything-3B 的开放则标志着视觉 grounding 任务向轻量高效方向演进。

---

## 热门模型

### 🎭 多模态与视觉语言（VLM、视觉编码器、跨模态模型、图文理解）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**<<br>google \| 995⭐ \| 1,005,883⬇️ | **Gemma-4 统一架构的指令调优版本**，"any-to-any"原生支持图文互生，本周下载量破百万。研究相关性：其统一编码器-解码器设计为 OCR 与文档理解提供了端到端基座，且开源权重允许深入分析多模态融合机制与幻觉来源。 |
| **[google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)**<<br>google \| 533⭐ \| 207,338⬇️ | **Gemma-4 基础预训练模型**，同上架构但无指令对齐。研究相关性：适合作为多模态预训练策略、表示对齐和跨模态迁移研究的纯净基线。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**<<br>google \| 705⭐ \| 92,080⬇️ | **扩散模型与 Gemma LLM 的统一架构**，26B 参数支持图像-文本联合生成。研究相关性：将扩散过程的迭代特性引入 VLM，为**视觉推理中的幻觉缓解**提供了新路径——扩散的逐步去噪机制可显式建模不确定性。 |
| **[moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**<<br>moonshotai \| 515⭐ \| 1,689⬇️ | **Kimi K2.5 系列的代码特化多模态模型**，支持图像特征提取与长上下文代码理解。研究相关性：其"image-feature-extraction"标签暗示视觉编码器与语言模型的解耦设计，适合研究**视觉-代码跨模态对齐**及长上下文中的注意力模式。 |
| **[MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**<<br>MiniMaxAI \| 413⭐ \| 1,031⬇️ | **MiniMax 第三代多模态大模型**，明确标注 multimodal 与 image-text-to-text。研究相关性：国产闭源模型的开源权重释放，为对比研究不同多模态架构设计（如 ViT vs CNN 编码器）提供了稀缺样本。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**<<br>nvidia \| 1,959⭐ \| 69,443⬇️ | **轻量级视觉定位模型**，3B 参数实现开放词汇目标定位。研究相关性：视觉 grounding 是**幻觉缓解的关键前置技术**——精确的物体定位可减少 VLM 的"指鹿为马"式幻觉，其高效架构适合移动端部署研究。 |
| **[ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R)**<<br>ByteDance \| 235⭐ \| 426⬇️ | **图像-文本到视频生成模型**，Bernini 渲染器架构。研究相关性：多模态生成的时空一致性要求极高，是研究**长序列多模态幻觉累积**的理想对象；Apache-2.0 许可便于学术复现。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**<<br>HauhauCS \| 1,761⭐ \| 2,411,202⬇️ | **Qwen3.6 MoE 架构的激进去对齐版本**，35B/A3B 激活参数，带 vision 能力。研究相关性：本周下载量冠军，其"uncensored"标签揭示了**对齐与能力之间的张力**——研究者可对比原始 Qwen3.6 与去对齐版本，量化安全训练对多模态推理能力的抑制程度。 |
| **[Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)**<<br>Jackrong \| 157⭐ \| 11,291⬇️ | **Qwen 系 27B 代码视觉模型的 GGUF 量化版**，支持 MTP（Multi-Token Prediction）。研究相关性：MTP 训练目标与视觉输入的结合，为研究**视觉-代码联合推理的解码效率**及量化对多模态性能的影响提供了实验素材。 |
| **[prefeitura-rio/Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**<<br>prefeitura-rio \| 110⭐ \| 5,943⬇️ | **397B 总参数的 Qwen3.5 MoE 开放权重**，巴西政府背景。研究相关性：超大规模 MoE 的多模态对话能力，适合研究**专家路由机制在视觉-语言任务中的 specialization 模式**。 |
| **[unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)**<<br>unsloth \| 580⭐ \| 872,895⬇️ | **Gemma-4-12B-it 的 GGUF 高效推理版本**。研究相关性：量化对多模态模型的**视觉编码精度与语言幻觉率**的影响尚缺乏系统研究，此变体提供了低资源实验入口。 |
| **[unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF)**<<br>unsloth \| 213⭐ \| 227,830⬇️ | **QAT（量化感知训练）版 Gemma-4**，比 PTQ 更保留精度。研究相关性：QAT 在视觉-语言联合表征上的效果，是**多模态模型压缩与幻觉控制**交叉领域的空白点。 |
| **[unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF)**<<br>unsloth \| 151⭐ \| 260,757⬇️ | **26B 激活参数的 MoE 版 Gemma-4 QAT 量化**。研究相关性：MoE + QAT + 多模态的三重组合，为研究**稀疏激活与量化噪声在视觉推理中的交互效应**提供了独特配置。 |

### 🧠 长上下文与推理模型（扩展上下文 LLM、推理增强模型、数学模型）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**<<br>deepseek-ai \| 4,813⭐ \| 3,250,404⬇️ | **本周点赞与下载双冠王**，DeepSeek V4 专业版，延续 MLA 注意力与 DeepSeekMoE 架构。研究相关性：其长上下文效率与推理成本优势，为**超长文档的 OCR 后处理与多页版面分析**提供了可扩展的基座；开源权重允许复现其推理时扩展（inference-time scaling）技术。 |
| **[CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**<<br>CohereLabs \| 355⭐ \| 6,533⬇️ | **Cohere2 MoE 架构的轻量代码模型**。研究相关性：MoE 在代码长上下文中的专家分化模式，可迁移研究至**文档结构理解（如 HTML/LaTeX 解析）的专家 specialization**。 |
| **[nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro)**<<br>nex-agi \| 236⭐ \| 3,092⬇️ | **Qwen3.5 MoE 的 N2 系列专业版**，支持 image-text-to-text。研究相关性：其长上下文能力与视觉输入的结合，适合研究**多页文档的跨页推理与信息整合**。 |
| **[nex-agi/Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini)**<<br>nex-agi \| 193⭐ \| 3,760⬇️ | **Nex-N2 轻量版**，同上架构缩小规模。研究相关性：小规模 MoE 的长上下文效率边界，对**边缘设备上的文档理解**有参考价值。 |
| **[XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)**<<br>XiaomiMiMo \| 106⭐ \| 3,590⬇️ | **小米 MiMo V2 的 FP4 超低精度版本**，支持 agent 任务。研究相关性：FP4 精度下的**长上下文稳定性与工具调用可靠性**，是推理模型在极端量化下的行为研究前沿。 |

### 🔧 Post-Training 与对齐（RLHF/DPO/SFT 模型、偏好微调模型、对齐-focused 发布）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated)**<<br>huihui-ai \| 152⭐ \| 8,270⬇️ | **Gemma-4-12B-it 的"abliterated"（去对齐）版本**，保留多模态能力但移除安全限制。研究相关性：明确的"abliterated"标签使其成为**对齐技术逆向工程**的珍贵样本——可系统对比原始 it 版本，量化安全训练对视觉-语言对齐的干预程度。 |
| **[OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)**<<br>OBLITERATUS \| 277⭐ \| 50,289⬇️ | **Gemma-4-12B 的激进去对齐变体**，带 GGUF 支持。研究相关性：与 huihui-ai 版本形成**去对齐强度的梯度对比**，适合研究不同强度安全移除对多模态推理一致性的影响。 |
| **[Jiunsong/supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**<<br>Jiunsong \| 818⭐ \| 98,892⬇️ | **26B 激活参数的 Gemma-4 MoE 去对齐版本**，高社区热度。研究相关性：MoE 架构的去对齐后，**专家路由模式是否发生变化**——安全相关专家是否被抑制或重组，是新颖的对齐机制研究问题。 |

### 📄 OCR 与文档模型（文本识别、版面分析、文档理解、公式识别）

> *本周无直接标注 OCR/HMER/文档理解的专用模型上榜，但以下模型具备强相关能力：*

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**<<br>（见上文） | **当前最接近"原生文档理解"的统一架构**，其 any-to-any 能力隐含对文档图像的端到端处理。研究相关性：需验证其**数学公式识别（HMER）与复杂版面分析**的零样本能力，可替代专用 OCR 模型的程度。 |
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**<<br>（见上文） | **扩散机制对精细文本渲染的潜力**，Ideogram 系列已证明扩散模型在文本生成图像中的字形控制能力。研究相关性：逆向思考——扩散的迭代修正机制可能提升**手写公式识别与低质量文档 OCR** 的鲁棒性。 |

### 👁️ 幻觉缓解（事实 grounded 模型、校准置信度模型、RAG 增强模型）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**<<br>（见上文） | **扩散架构的隐式不确定性建模**。研究相关性：与传统自回归 VLM 的"一次性预测"不同，扩散的迭代去噪过程可**显式暴露模型在各步的置信度变化**，为幻觉检测提供新的内部信号。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**<<br>（见上文） | **视觉 grounding 作为幻觉前置抑制**。研究相关性：精确的物体定位可**锚定 VLM 的注意力至真实视觉区域**，减少"虚构物体"类幻觉；其开放词汇能力支持动态事实核查。 |

### 🏗️ 研究基础设施（训练框架、评测套件、数据集工具）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**<<br>unsloth \| 246⭐ \| 42,885⬇️ | **Unsloth 对 DiffusionGemma 的 GGUF 适配**。研究相关性：Unsloth 的优化技术（如梯度检查点、LoRA 融合）向扩散-语言统一模型的迁移，为**高效微调多模态幻觉缓解模型**提供了工具链。 |
| **[bosonai/higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b)**<<br>bosonai \| 414⭐ \| 32,162⬇️ | **Higgs 多模态系列的 TTS 版本**，基于 Qwen3 架构。研究相关性：其"higgs_multimodal_qwen3"标签暗示**音频-文本-视觉的三模态统一**可能，为跨模态幻觉的一致性研究提供了未来基座。 |
| **[google/magenta-realtime-2](https://huggingface.co/google/magenta-realtime-2)**<<br>google \| 187⭐ \| 7,331⬇️ | **实时音频生成模型**，TFLite 部署。研究相关性：实时约束下的**流式多模态生成质量与幻觉控制**，是时间敏感场景（如实时字幕、语音助手）的关键研究维度。 |

---

## 研究生态信号

**Gemma-4 家族已形成事实上的多模态研究操作系统**：Google 以 any-to-any 架构统一图文音视频，Unsloth 迅速提供全系列量化工具，社区则衍生出大量去对齐变体——这种"基座-工具-对抗"的三层生态，标志着开源多模态进入**可编程、可干预、可审计**的新阶段。与此同时，**"uncensored/abliterated"模型的爆发式增长**（本周 4 个，占相关模型 30%）揭示了对齐研究的深层张力：安全训练的技术细节愈发不透明，倒逼研究者通过逆向工程理解其机制。闭源方面，Moonshot、MiniMax 仅释放权重而非训练数据，与 DeepSeek 的全栈开源形成对比；NVIDIA 则选择轻量高效路线（3B 参数）切入视觉 grounding，暗示**边缘部署与实时幻觉抑制**将成为下一竞争焦点。OCR/HMER 专用模型本周缺席热门榜，但 Gemma-4 的统一架构可能正在**吸收并替代**传统文档理解 pipeline——这一"功能融合"趋势值得警惕性验证。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| **🔥 最高** | **[google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)** | **架构级创新**：首个大规模扩散-语言统一模型，其迭代生成机制为幻觉研究提供了全新的**过程监督（process supervision）**入口——可在去噪各步插入幻觉检测，而非仅在最终输出判断。建议优先验证其在 HMER 任务上的零样本能力，以及扩散步数与识别精度的 trade-off。 |
| **🔥 高** | **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | **幻觉缓解的前置技术**：视觉 grounding 的精度直接决定 VLM 的"所见即所得"程度。建议将其作为**外部工具接入 Gemma-4**，量化 grounding 辅助对图文问答幻觉率的降低幅度，探索"感知-认知"解耦的混合架构。 |
| **🔥 高** | **[huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Hui

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*