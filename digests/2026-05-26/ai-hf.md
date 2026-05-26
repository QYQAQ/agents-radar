# Hugging Face 热门模型日报 2026-05-26

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-26 00:31 UTC

---

# Hugging Face 研究模型日报 | 2026-05-26

---

## 今日速览

本周 Hugging Face 热点显著向**多模态推理**与**长上下文架构**倾斜：Qwen3.6 系列（27B/35B-A3B）以高下载量主导视觉语言模型生态，MiniCPM-V-4.6 延续端侧 VLM 的强劲势头；DeepSeek-V4-Pro 作为纯文本推理旗舰获得最高社区关注。值得注意的是，**OCR/文档理解专用模型出现明显空缺**——NuExtract3 虽具视觉能力但偏向信息抽取，HRM-Text-1B 的"hrm"标签暗示手写识别数学公式潜力却任务标注模糊。后训练对齐领域未见显式 RLHF/DPO 发布，但大量 GGUF 量化衍生模型（Uncensored/Obliterated 系列）反映出社区对**对齐干预与价值校准**的逆向工程兴趣，间接凸显幻觉缓解与可控生成的研究紧迫性。

---

## 热门模型（按研究相关性分类）

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)** | sapientinc | 314 | 90,026 | **高下载量但任务标注存疑**：标签含"hrm"（Handwritten Recognition & Math?），若属 HMER（手写数学表达式识别）或文档版面分析方向，则填补本周 OCR 空白；需验证其编码器架构与公式识别基准表现。 |
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 137 | 17,501 | 基于 Qwen3.5 的视觉信息抽取模型，**文档结构理解能力**可迁移至 OCR 后处理场景；研究价值在于其从视觉文档到结构化数据的端到端范式，而非传统 OCR 的字符级识别。 |

> ⚠️ **领域观察**：本周 Top 30 中**缺乏专用 OCR 编码器**（如 Donut、Nougat 后继者）或显式 HMER 模型，文档智能研究需关注 Qwen3.6 / MiniCPM-V 的零样本文档 OCR 能力是否已替代专用模型。

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** | Qwen | 1,451 | 4,423,521 | **社区核心基座**：image-text-to-text 任务标注确认原生视觉能力，MTP（Multi-Token Prediction）架构对**视觉特征序列的并行解码**具有研究价值，可探索其多模态推理的上下文效率。 |
| **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | openbmb | 943 | 285,414 | **端侧 VLM 技术前沿**：以较小参数实现 competitive 视觉理解，其**视觉编码器压缩与端侧部署策略**对边缘 OCR、实时文档扫描场景有直接研究意义。 |
| **[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)** / **[35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | unsloth | 479 / 371 | 695,277 / 578,580 | **量化与推理优化基础设施**：GGUF 格式 + MTP 的兼容性验证，为**多模态模型的高效推理**提供实验平台；可研究量化对视觉-语言对齐精度的影响。 |
| **[CohereLabs/command-a-plus-05-2026-bf16](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)** / **[w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)** | CohereLabs | 120 / 200 | 12,824 / 7,449 | **企业级多模态对话**：cohere2_vision 架构的 bf16/w4a4 对比发布，为**多模态模型的精度-效率权衡**提供控制实验；关注其视觉指令跟随的对齐方法。 |
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 852 | 1,392,596 | **对齐干预的逆向样本**："Uncensored + Aggressive" 标签暗示**安全对齐的移除实验**，高下载量反映社区需求；研究其幻觉率与事实性退化可为对齐鲁棒性提供负面案例。 |
| **[Jackrong/Qwopus3.6-27B-v2-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF)** / **[v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF)** / **[3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)** | Jackrong | 128 / 92 / 188 | 12,677 / 23,762 / 42,644 | 社区衍生优化版本，**多模态代码生成能力**（image-text-to-text + Coder）对视觉编程、UI 自动化等 OCR+推理 复合任务有探索价值。 |
| **[NemoStation/Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)** | NemoStation | 343 | 7,291 | **视频-文本理解**：video-text-to-text 任务标注，2B 参数的轻量视频 VLM；研究其**时序推理与长视频 OCR**（如字幕、场景文字跟踪）的权衡。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | **4,274** | **4,820,866** | **本周绝对核心**：纯 text-generation 任务下的最高社区认可，V4 架构的**长上下文推理效率**（推测延续 MLA + MTP）与数学/代码能力值得深度拆解；关注其上下文长度规格与推理基准。 |
| **[openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)** | openbmb | 144 | 2 | MiniCPM 系列的文本基座，1B 参数的**极长上下文可行性**（MiniCPM 历史优势）可探索小模型的记忆-推理权衡；极低下载量暗示尚未成熟或发布初期。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 406 | 0 | **模板工程基础设施**：针对 Qwen3.5/3.6 的 chat template 修正，直接关联**长对话上下文中的角色一致性**与**多轮推理的格式鲁棒性**研究。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | HauhauCS | 852 | 1,392,596 | **对齐移除的极端实验**：高下载量揭示社区对"去 RLHF"模型的需求；研究其**奖励黑客（reward hacking）后的行为分布**，可反推原模型对齐机制的有效性。 |
| **[OBLITERATUS/Qwen3.6-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED)** | OBLITERATUS | 95 | 7,701 | 类似方向的轻量尝试，"OBLITERATED" 命名暗示**系统级指令对齐的完全擦除**，适合作为对齐失效模式的对比样本。 |
| **[nvidia/Nemotron-Labs-Diffusion-14B](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-14B)** | nvidia | 100 | 5,195 | **扩散语言模型**：nemotron_labs_diffusion 架构将连续扩散应用于文本生成，其**非自回归解码的对齐特性**（如何执行 RLHF？）是后训练领域的开放问题。 |

---

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[numind/NuExtract3](https://huggingface.co/numind/NuExtract3)** | numind | 137 | 17,501 | 结构化信息抽取的**事实约束生成**：输出格式（键值对）天然限制幻觉空间，可研究其**模式遵循（schema following）** 作为幻觉缓解机制的迁移价值。 |
| **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | deepseek-ai | 4,274 | 4,820,866 | DeepSeek 系列的**链式思维可信度**：V4-Pro 的推理透明度（是否公开 thinking 过程？）直接影响幻觉检测与校准研究的可行性。 |
| **[Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)** / **[35B-A3B 衍生模型](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)** | Qwen / 社区 | — | — | 原生 Qwen3.6 与 Uncensored/Obliterated 版本的**对比幻觉审计**：相同基座、不同对齐干预，构成控制实验的理想材料。 |

---

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 研究相关性说明 |
|:---|:---|---:|---:|:---|
| **[bytedance-research/Lance](https://huggingface.co/bytedance-research/Lance)** | bytedance-research | 817 | 1,679 | **Any-to-any 统一架构**：支持 image/video generation 与理解的端到端模型，其**模态桥接机制**可为多模态 OCR（如视频中的公式动态生成）提供基础设施参考。 |
| **[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)** | froggeric | 406 | 0 | **对话格式标准化工具**：Jinja 模板修正直接影响**多模态对话数据的对齐质量**与长上下文中的指令跟随一致性。 |

---

## 研究生态信号

**Qwen 家族已实质垄断开源多模态生态**：Qwen3.5/3.6 架构衍生出 27B/35B-A3B 的密集与 MoE 变体，覆盖从端侧到服务器的全谱系，其视觉-语言对齐方法成为事实标准。MiniCPM-V 在 2B-4B 区间维持端侧竞争力，形成"大模型 Qwen、小模型 MiniCPM"的双层格局。**闭源权重+开源生态的混合模式**深化：DeepSeek-V4-Pro、Cohere command-a-plus 以完整权重开放，但核心训练数据与对齐细节仍闭源，研究者依赖逆向工程（如 Uncensored 衍生模型）推断对齐机制。OCR/文档理解领域出现**"通用 VLM 替代专用模型"**的收敛趋势——本周无 Nougat、Got-OCR2 等专用文档模型入榜，暗示社区可能将文档 OCR 视为 VLM 的基础能力而非独立研究方向；HMER 等精细任务仍需验证通用模型的零样本极限。幻觉缓解方面，**"去对齐化"运动的流行**（Uncensored/Obliterated 高下载）反而凸显原始对齐的脆弱性，催生对更鲁棒校准方法的迫切需求。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | **[deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | 4.8M 下载量的推理旗舰，其**长上下文效率架构**（推测 MLA + MTP）与**数学/代码推理的幻觉模式**值得系统性审计；若公开 thinking 过程，可作为"推理透明度 vs 幻觉率"相关性的关键样本。建议优先测试其在长文档 OCR 后的跨页推理一致性。 |
| ⭐⭐⭐ | **[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** | **对齐研究的"负面黄金标准"**：与原 Qwen3.6-35B-A3B（假设存在）构成完美控制对，可量化 RLHF/安全训练对**事实准确性、幻觉率、拒绝行为**的具体影响；高下载量确保社区复现基础。建议设计幻觉基准（如 MathVista、MMHallu）的前后对比实验。 |
| ⭐⭐☆ | **[openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)** | 端侧 VLM 的**OCR 能力边界探测**：在 2B-4B 参数约束下，其视觉编码器如何平衡分辨率、字符粒度与推理速度？适合作为**移动场景文档理解**的部署基线，研究其量化后（INT4/INT8）的 OCR 精度退化曲线具有工程价值。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*