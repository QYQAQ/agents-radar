# Hugging Face 热门模型日报 2026-05-28

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-28 00:30 UTC

---

# Hugging Face 研究模型日报 | 2026-05-28

## 今日速览

本周 Hugging Face 热点显著向**多模态统一架构**倾斜：字节跳动的 Lance 以 any-to-any 范式实现图像-视频-文本的任意模态互转，标志生成式多模态进入新阶段；Qwen3.6 系列（27B/35B-A3B）持续主导视觉语言模型生态，多个社区微调版本涌现；DeepSeek-V4-Pro/Flash 以极高下载量巩固长上下文推理基座地位。值得注意的是，**OCR/HMER 专用模型仍显稀缺**，NuExtract3 虽具视觉能力但偏向信息抽取，文档理解领域存在明显空白。后训练对齐方面，社区主要通过 GGUF 量化与去审查化微调间接探索，缺乏系统性的幻觉缓解专用发布。

---

## 热门模型（按研究相关性分类）

### 🎭 多模态与视觉语言

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research \| 👍 920 \| ⬇️ 1,908 | **Any-to-any 原生多模态生成模型**，支持图像/视频/文本任意输入输出，是研究统一多模态表征与跨模态生成的关键基线，其架构设计对 VLM 的逆向 OCR（视觉→符号）能力有直接影响。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen \| 👍 1,495 \| ⬇️ 4,577,271 | **主流视觉语言基座**，image-text-to-text 任务的高下载量验证其作为研究平台的统治力，是评估 OCR 鲁棒性、多模态幻觉与长上下文视觉推理的首选实验载体。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb \| 👍 1,011 \| ⬇️ 355,020 | **端侧高效 VLM**，以较小参数量实现 competitive 的多模态理解，适合研究资源受限场景下的 OCR 精度-效率权衡及边缘部署幻觉问题。 |
| **[CohereLabs/command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs \| 👍 212 \| ⬇️ 7,769 | **W4A4 量化视觉语言模型**，4-bit 权重激活量化下的多模态推理，为研究量化对视觉特征提取精度（尤其是细粒度文本识别）的影响提供独特样本。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** / **[unsloth/Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth \| 👍 518/396 \| ⬇️ 735,349/627,535 | **Multi-Token Prediction 优化的量化 VLM**，MTP 训练目标与视觉模态的结合值得研究：预测多个视觉 token 是否提升结构化输出（如表格、公式）的连贯性。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS \| 👍 946 \| ⬇️ 1,598,473 | **高下载量去审查 MoE VLM**，"Uncensored" 标签暗示安全对齐的移除，为研究**对齐与幻觉的 trade-off** 提供反面教材——过度 RLHF 是否抑制真实知识表达？ |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind \| 👍 174 \| ⬇️ 20,350 | **视觉信息抽取模型**，基于 Qwen3.5 架构，虽非纯 OCR 但涉及文档视觉理解，可作为研究结构化文档解析与实体级幻觉的切入点。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation \| 👍 415 \| ⬇️ 9,144 | **Video-text-to-text 模型**，视频时序理解与文本生成的结合，扩展了多模态推理的时序维度，对长视频文档（如讲座、演示）的自动摘要与事实一致性研究有意义。 |

### 🧠 长上下文与推理模型

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai \| 👍 4,359 \| ⬇️ 5,019,884 | **本周最高点赞与下载的推理基座**，其长上下文能力与数学推理性能是研究扩展上下文窗口下注意力机制效率、推理链忠实度（faithfulness）的核心基准。 |
| **[deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)** | deepseek-ai \| 👍 1,256 \| ⬇️ 3,088,308 | **轻量版长上下文模型**，MIT 许可证与 eval-results 标签暗示可复现的评测，适合研究推理加速技术（推测解码、缓存策略）对长文档理解的影响。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb \| 👍 408 \| ⬇️ 2,409 | **1B 级长上下文 LLM**，极小参数下的文本生成能力，为研究长上下文机制的可压缩性及涌现能力的尺度律提供极端案例。 |
| **[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)** / **[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)** | tencent \| 👍 1,071/405 \| ⬇️ 7,471/2,091 | **翻译专用模型（Hunyuan 系列）**，长上下文对文档级翻译的连贯性至关重要，其 1.8B→30B 的尺度对比可辅助研究推理能力随模型规模的变化。 |

### 🔧 Post-Training 与对齐

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** / **[Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** | Jackrong \| 👍 159/131 \| ⬇️ 16,379/31,597 | **社区微调 Qwen 的 GGUF 变体**，"Qwopus" 命名暗示章鱼式多能力融合，反映社区后训练实验的活跃，适合分析非官方微调的对齐漂移（alignment drift）现象。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric \| 👍 433 \| ⬇️ 0 | **聊天模板修正项目**，纯 Jinja 模板工程，高点赞零下载表明社区对**对话格式标准化**的重视，是对齐基础设施的关键但易被忽视的环节。 |
| **[OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)** | OBLITERATUS \| 👍 105 \| ⬇️ 10,015 | **激进去对齐化实验**，"OBLITERATED" 标签明示安全训练的移除，为研究 RLHF 的副作用（如过度拒绝、模式崩溃）及对齐的可逆性提供极端对照。 |

### 👁️ 幻觉缓解（间接相关）

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc \| 👍 393 \| ⬇️ 103,033 | **HRM（Human Resource Management?）文本模型**，标签含 "hrm_text" 但任务为通用 text-generation，高下载量与模糊定位提示需警惕**任务描述与实际能力的错位**——一种元层面的幻觉现象。 |

### 🏗️ 研究基础设施

| 模型 | 作者/数据 | 一句话说明 |
|:---|:---|:---|
| **[circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)** | circlestone-labs \| 👍 1,572 \| ⬇️ 690,196 | **ComfyUI 生态的扩散模型基础设施**，高下载量反映视觉生成工作流的工具化趋势，其单文件格式（diffusion-single-file）对可复现的多模态实验环境建设有参考价值。 |
| **[nvidia/PiD](https://huggingface.co/nvidia/PiD)** | nvidia \| 👍 141 \| ⬇️ 117 | **图像超分辨率扩散模型**，低下载量但 nvidia 背书，其超分能力可作为 OCR 前置增强模块，研究分辨率恢复对低质量文档识别的影响。 |
| **[zhen-nan/L2P](https://huggingface.co/zhen-nan/L2P)** | zhen-nan \| 👍 74 \| ⬇️ 0 | **arXiv:2605.12013 关联研究**，Apache-2.0 许可证与论文引用表明学术向发布，零下载暗示预印本阶段，需追踪其是否涉及长上下文或对齐新方法。 |

---

## 研究生态信号

**Qwen 家族形成事实上的多模态研究垄断**：Qwen3.6 系列占据视觉语言模型的官方基座、社区微调、量化优化三个层级，其架构选择（MTP、MoE）成为后续研究的默认前提。这种集中化降低了实验迁移成本，但也可能抑制架构多样性。**开源权重在 VLM 领域已完全主导**，闭源模型（如 GPT-4V）不再作为可比较的研究对象出现。令人忧虑的是，**专用 OCR/HMER 模型几乎缺席**——NuExtract3 偏向抽取而非识别，Lance 的 any-to-any 能力尚未验证对 LaTeX 公式等结构化符号的精度；文档理解的进步似乎被 VLM 的"通用能力"叙事所遮蔽。后训练对齐呈现**两极化**：unsloth 等提供高效微调基础设施，而 "Uncensored"/"OBLITERATED" 标签的流行反映社区对安全对齐的反弹，这种张力为"对齐即幻觉来源"的批判性研究提供了社会实验场。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | Any-to-any 架构是评估**逆向 OCR 能力**的理想平台：测试其从图像生成精确符号序列（如数学公式、程序代码）的保真度，可直接揭示统一多模态表征的瓶颈。若 Lance 在文本→图像→文本循环中引入符号错误，则指向视觉-语言对齐的根本缺陷。 |
| ⭐⭐⭐ | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | 极高下载量的"去对齐" MoE VLM，可系统对比其与官方 Qwen3.6 在**事实准确性 vs 安全拒绝率**上的 trade-off。若移除 RLHF 后幻觉率下降，将挑战"对齐必然提升可信度"的默认假设，为"对齐幻觉"（alignment hallucination）研究提供实证。 |
| ⭐⭐☆ | **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | 虽非纯粹 OCR，但其文档视觉理解能力可作为**结构化幻觉**的探针：在发票、表格等半结构化文档上，检验模型对空白字段、模糊区域的置信度校准，填补文档级幻觉缓解研究的工具空白。建议扩展其至手写数学公式识别场景。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*