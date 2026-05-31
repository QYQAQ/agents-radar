# Hugging Face 热门模型日报 2026-05-31

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-31 00:33 UTC

---

# Hugging Face 研究模型日报 | 2026-05-31

---

## 今日速览

本周 Hugging Face 生态呈现**多模态推理与长上下文深度融合**的显著趋势：Qwen3.6 系列（27B/35B-A3B MoE）持续主导视觉语言模型榜单，其 MTP 多令牌预测架构为长上下文推理效率研究提供重要基座；PaddleOCR-VL-1.6 的发布标志着 OCR 领域从纯文本识别向**视觉-语言联合文档理解**的关键跃迁；DeepSeek-V4 系列以 Flash 变体探索推理效率与对齐质量的平衡；MiniCPM-V-4.6 与 MiniCPM5-1B 形成端侧多模态与轻量文本模型的互补布局，为边缘设备上的幻觉缓解与可控生成研究开辟新场景。值得关注的是，"Uncensored" 与 "Fixed-Chat-Templates" 等社区微调模型的热度攀升，反映出 post-training 对齐与对话安全性的研究需求正从学术机构向社区生态扩散。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | PaddlePaddle<br>👍 107 / ⬇️ 2,294 | 基于 ERNIE4.5 的 OCR 视觉语言模型，将传统文本识别与文档级视觉理解统一，为 HMER（手写数学表达式识别）和复杂版面分析提供端到端研究基线，其 PaddleOCR 生态的延续性便于对比实验设计。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** | Qwen<br>👍 1,954 / ⬇️ 5,728,121 | Qwen3.6 MoE 架构的旗舰视觉语言模型，激活参数仅 3B 却实现 35B 级性能，为**多模态推理效率与幻觉缓解的权衡研究**提供理想实验平台，其对话式 image-text-to-text 能力支持复杂视觉问答的对齐实验。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen<br>👍 1,537 / ⬇️ 4,971,730 | 密集架构的视觉语言基线，与 35B-A3B MoE 变体形成**架构对比研究**的黄金组合，便于分析专家路由机制对多模态幻觉的影响。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb<br>👍 1,074 / ⬇️ 433,156 | 端侧优化的视觉语言模型，以极小参数规模实现可部署的多模态推理，是**资源受限场景下幻觉缓解与高效对齐**的关键研究对象，其 MiniCPM 系列版本迭代支持纵向追踪。 |
| **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)** | nvidia<br>👍 494 / ⬇️ 18,327 | 定位驱动的图像-文本模型，特征提取与空间理解结合，为**视觉 grounding 减少对象幻觉**提供技术路径，NVIDIA 的硬件协同优化经验具参考价值。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind<br>👍 203 / ⬇️ 53,338 | 基于 Qwen3.5 的视觉文档信息抽取模型，**结构化输出与视觉理解的结合**使其成为文档级幻觉检测与可控生成的实用工具。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS<br>👍 1,103 / ⬇️ 2,227,885 | 社区激进去审查微调版本，高下载量反映**安全对齐与有用性权衡**的研究需求，可作为红队测试与对齐鲁棒性分析的反面教材。 |
| **[stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)** | stepfun-ai<br>👍 134 / ⬇️ 3,400 | Step 系列视觉语言模型的效率优化变体，Flash Attention 架构与视觉编码的结合为**长视觉序列推理**提供新思路。 |
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research<br>👍 981 / ⬇️ 2,856 | 任意模态到任意模态（any-to-any）的生成模型，图像/视频统一生成能力使其成为**跨模态一致性幻觉**研究的独特样本。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** / **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** / **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** | unsloth / Jackrong<br>👍 567/172/186 / ⬇️ 877,938/105,264/33,167 | MTP（Multi-Token Prediction）GGUF 量化版本集群，**多令牌预测与视觉语言模型的结合**是新兴研究方向，社区量化生态的繁荣为端侧多模态部署与推理加速研究提供便利。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai<br>👍 4,463 / ⬇️ 5,918,111 | 本周点赞与下载双冠，V4 架构的上下文扩展与推理增强设计使其成为**长上下文推理能力评估**的核心基线，Pro 版本的对齐质量值得与社区微调版本对比分析。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai<br>👍 1,303 / ⬇️ 3,427,926 | Flash 变体探索推理效率边界，MIT 许可证与公开评测结果便于复现，为**长上下文场景下的推理-效率帕累托前沿**研究提供数据点。 |
| **[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)** / **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)** | tencent<br>👍 433/1,091 / ⬇️ 3,833/16,805 | 混元翻译模型的 MoE 与密集双版本，**多语言长序列理解**与 Hy v3 架构的推理优化，为跨语言文档级幻觉传播研究提供工具。 |
| **[LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** / **[LiquidAI/LFM2.5-8B-A1B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF)** | LiquidAI<br>👍 275/123 / ⬇️ 17,084/23,685 | 液态神经网络（Liquid Neural Networks）的 MoE 实现，**连续时间架构与离散 Transformer 的对比**对长上下文记忆机制研究具有理论启发，边缘部署版本扩展应用场景。 |
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc<br>👍 418 / ⬇️ 138,118 | HRM（Human Reasoning Model）架构的轻量文本模型，高下载量暗示其在**推理链生成与上下文压缩**方面的实用价值，适合作为长上下文研究的效率对照。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation<br>👍 454 / ⬇️ 15,780 | 基于 Qwen3.5 的视频-文本模型，**长视频序列理解**是视觉语言长上下文的新兴前沿，2B 参数规模便于快速实验迭代。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric<br>👍 460 / ⬇️ 0 | 专注修复 Qwen 系列对话模板的技术债务，**模板工程作为对齐基础设施**的被忽视价值获社区认可，为系统性研究对话格式对 RLHF/DPO 效果的影响提供切入点。 |
| **[openai/privacy-filter](https://huggingface.co/openai/privacy-filter)** | openai<br>👍 1,570 / ⬇️ 304,691 | 令牌级隐私分类器，OpenAI 罕见开源的**安全对齐工具**，其 ONNX/Transformers.js 多格式部署为隐私-效用权衡的后训练研究提供标准化评估手段。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb<br>👍 606 / ⬇️ 28,793 | MiniCPM 第五代文本基座，极小参数下的**可控生成与事实 grounding** 能力，与 MiniCPM-V-4.6 配合可研究纯文本 vs 视觉增强对幻觉率的影响。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者/指标 | 研究相关性 |
|:---|:---|:---|
| **[pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)** | pyannote<br>👍 2,073 / ⬇️ 9,771,170 | 音频说话人分离的工业级 pipeline，**多说话人长音频的时序一致性**研究可借鉴其评估方法论，对多模态长上下文中的时序幻觉检测有启发。 |

---

## 研究生态信号

**Qwen 家族持续主导多模态开源生态**，3.6 系列通过 MoE（35B-A3B）与密集（27B）双轨架构、MTP 多令牌预测、以及官方-社区-量化（GGUF/MLX）的三层分发体系，形成了罕见的**全链路研究友好型模型矩阵**。这与 DeepSeek-V4 的 MIT 开源策略形成呼应，表明顶级中文模型团队正将"开源权重+完整生态"作为核心竞争力。OCR 领域出现关键转折：PaddleOCR-VL-1.6 从传统检测-识别两阶段迈向视觉语言统一建模，与 NuExtract3 等信息抽取模型共同指向**"文档理解即对话"**的新范式。值得警惕的是，"Uncensored" 微调模型的高热度（HauhauCS 版本下载量超 220 万）揭示出**安全对齐与有用性之间的张力已成为社区级研究议题**，亟需系统性的红队评估基准。长上下文方面，视频理解（Marlin-2B）与任意模态生成（Lance）的涌现，将幻觉缓解的研究场景从文本-图像二元扩展至多模态时序一致性这一更复杂的维度。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[PaddlePaddle/PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)** | OCR 领域向视觉语言范式转型的标志性模型。基于 ERNIE4.5 的架构使其具备文档级语义理解能力，可直接用于 HMER 任务的端到端重定义实验，或与 Qwen-VL 系列对比分析通用 VLM 与专用 OCR-VL 的幻觉差异。PaddlePaddle 生态的完整性便于复现与扩展。 |
| ⭐⭐⭐ | **[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** + **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** | 构建**架构对比×量化策略×多模态幻觉**的三维研究矩阵。MoE vs 密集、MTP vs 自回归、FP16 vs GGUF 量化的交叉组合，为分析模型结构对视觉幻觉敏感度的影响提供天然实验条件。建议优先验证 MTP 在长视觉序列中的一致性优势假设。 |
| ⭐⭐☆ | **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | 被低估的对齐基础设施研究对象。对话模板作为 RLHF/DPO 的"隐式先验"，其修复实践可系统化为**模板工程方法论**，进而研究不同模板设计对多模态指令跟随中幻觉率的因果效应。零下载量反而说明其作为"纯工具"的定位清晰，适合作为控制变量引入对比实验。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*