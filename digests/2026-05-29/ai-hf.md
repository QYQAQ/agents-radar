# Hugging Face 热门模型日报 2026-05-29

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-05-29 00:34 UTC

---

# Hugging Face 研究模型日报 | 2026-05-29

---

## 今日速览

本周 Hugging Face 生态呈现多模态推理与长上下文模型的密集迭代趋势。**Qwen3.6 系列**（27B/35B-A3B）以极高下载量主导视觉语言模型赛道，MTP（Multi-Token Prediction）变体成为推理加速研究的热点配置。字节跳动的 **Lance** 以 any-to-any 架构探索统一多模态生成，而 MiniCPM 系列持续推动端侧 VLM 的 OCR 与文档理解能力边界。DeepSeek-V4 系列则延续其在长上下文推理与后训练对齐方面的技术领导力。值得注意的是，"Uncensored/OBLITERATED" 类模型的流行反映了社区对后训练对齐机制（尤其是安全对齐与有用性权衡）的逆向工程兴趣，这对幻觉缓解研究具有警示意义。

---

## 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**openbmb/MiniCPM5-1B**](https://huggingface.co/openbmb/MiniCPM5-1B) | openbmb | 493 | 15,629 | MiniCPM 系列以端侧高效 OCR 与文档理解著称，1B 规模适合研究轻量级版面分析与公式识别（HMER）的蒸馏策略。 |
| [**numind/NuExtract3**](https://huggingface.co/numind/NuExtract3) | numind | 184 | 44,827 | 基于 Qwen3.5 的视觉信息抽取模型，直接关联文档 OCR 后结构化提取任务，适合研究 VLM 在表单/票据理解中的幻觉问题。 |

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**bytedance-research/Lance**](https://huggingface.co/bytedance-research/Lance) | bytedance-research | 954 | 2,506 | **Any-to-any 统一多模态模型**，支持图像/视频/音频的跨模态生成与理解，为研究多模态推理的统一表征空间提供新基线。 |
| [**openbmb/MiniCPM-V-4.6**](https://huggingface.co/openbmb/MiniCPM-V-4.6) | openbmb | 1,046 | 388,525 | MiniCPM-V 最新迭代，强化高分辨率图像理解与 OCR 能力，是研究端侧 VLM 效率-精度权衡的关键参照。 |
| [**Qwen/Qwen3.6-27B**](https://huggingface.co/Qwen/Qwen3.6-27B) | Qwen | 1,509 | 4,790,806 | Qwen3.6 主版本，视觉语言对齐架构的代表作，其 MoE 稀疏激活机制对研究多模态推理的计算效率具有重要价值。 |
| [**unsloth/Qwen3.6-27B-MTP-GGUF**](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF) | unsloth | 533 | 806,874 | **MTP（Multi-Token Prediction）量化版**，研究推理加速与投机解码（speculative decoding）在多模态场景中的适用性。 |
| [**unsloth/Qwen3.6-35B-A3B-MTP-GGUF**](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF) | unsloth | 404 | 686,839 | 35B-A3B MoE 结构的 MTP 量化变体，适合研究稀疏专家模型在长上下文多模态推理中的动态路由行为。 |
| [**HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive**](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 998 | 1,956,558 | **极高下载量的"去对齐"变体**，揭示原始安全对齐对多模态幻觉的抑制机制，是研究对齐-幻觉权衡的负面样本库。 |
| [**Jackrong/Qwopus3.6-27B-v2-GGUF**](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-GGUF) / [**v2-MTP-GGUF**](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF) | Jackrong | 172/151 | 24,336/65,968 | Qwen3.6 的社区优化分发版本，MTP 变体下载量显著更高，反映社区对推理效率优化的强烈需求。 |
| [**nvidia/LocateAnything-3B**](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 188 | 1,755 | 视觉定位模型，支持开放词汇的图像区域定位，为研究 VLM 的细粒度空间推理与指代表达理解提供工具。 |
| [**NemoStation/Marlin-2B**](https://huggingface.co/NemoStation/Marlin-2B) | NemoStation | 430 | 13,855 | 视频-文本理解模型，专注于视频描述生成，适合研究时序多模态推理中的长上下文信息聚合。 |

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**deepseek-ai/DeepSeek-V4-Pro**](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,403 | 5,281,601 | **本周最高点赞与下载的基座模型**，V4 系列在长上下文推理（128K+）与数学代码能力上持续领先，是研究长文本 RAG 与复杂推理的必备基线。 |
| [**deepseek-ai/DeepSeek-V4-Flash**](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | deepseek-ai | 1,277 | 3,327,898 | V4 的轻量推理优化版，MIT 许可证与公开 eval-results 使其成为研究长上下文模型效率-性能帕累托前沿的理想对象。 |
| [**LiquidAI/LFM2.5-8B-A1B**](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) | LiquidAI | 110 | 0 | 液态神经网络（Liquid Neural Network）架构的 MoE 变体，探索连续时间动态系统在序列推理中的优势，长上下文研究的前沿探索。 |
| [**tencent/Hy-MT2-1.8B**](https://huggingface.co/tencent/Hy-MT2-1.8B) / [**Hy-MT2-30B-A3B**](https://huggingface.co/tencent/Hy-MT2-30B-A3B) | tencent | 1,078/416 | 14,600/2,894 | 混元翻译模型，1.8B 密集与 30B-A3B MoE 双版本，适合研究长上下文机器翻译中的上下文感知与指代消解。 |

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**froggeric/Qwen-Fixed-Chat-Templates**](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates) | froggeric | 444 | 0 | **纯聊天模板修正资源**，无模型权重，反映社区对官方模板漏洞的修复需求，是研究对话格式对齐（format alignment）对下游性能影响的典型案例。 |
| [**OBLITERATUS/Qwen3.6-27B-OBLITERATED**](https://huggingface.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED) | OBLITERATUS | 111 | 13,911 | 系统性的"去对齐"微调模型，用于研究 RLHF/DPO 安全训练的鲁棒性与逆向攻击面。 |

### 👁️ 幻觉缓解

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**sapientinc/HRM-Text-1B**](https://huggingface.co/sapientinc/HRM-Text-1B) | sapientinc | 400 | 121,862 | **HRM（Hallucination-Resistant Model）** 系列，明确以幻觉缓解为训练目标，1B 规模适合研究轻量级事实 grounding 机制与置信度校准方法。 |

### 🏗️ 研究基础设施

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [**zhen-nan/L2P**](https://huggingface.co/zhen-nan/L2P) | zhen-nan | 78 | 0 | 论文 arxiv:2605.12013 的配套资源，Apache-2.0 许可证，推测为长上下文或提示学习相关的方法论基础设施，待进一步调研。 |

---

## 研究生态信号

**Qwen 家族**以 3.6 版本的密集迭代（27B/35B-A3B、MTP、GGUF、Uncensored 变体）形成绝对主导的模型生态，其视觉语言对齐架构已成为多模态研究的"默认选择"。**MiniCPM** 在端侧 OCR/文档理解赛道保持技术领导力，与 Qwen 形成"云端-边缘"分层格局。后训练对齐领域出现显著分化：官方版本强化安全对齐，而社区通过 Uncensored/OBLITERATED 变体进行逆向工程，这种"对齐军备竞赛"对幻觉缓解研究提出新挑战——安全对齐是否以牺牲事实准确性为代价？开源权重在视觉语言模型中已占据主流，但 any-to-any 统一架构（如 Lance）仍属前沿探索。值得注意的是，**MTP（Multi-Token Prediction）** 从训练目标演变为推理优化配置，可能成为长上下文模型效率突破的关键范式。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | [**bytedance-research/Lance**](https://huggingface.co/bytedance-research/Lance) | Any-to-any 架构是下一代多模态系统的核心方向。研究其跨模态生成与理解的统一机制，可探索 OCR→图像→视频→音频的链式推理中幻觉的跨模态传播与抑制策略，对构建可信多模态 Agent 具有奠基意义。 |
| ⭐⭐⭐ | [**sapientinc/HRM-Text-1B**](https://huggingface.co/sapientinc/HRM-Text-1B) | 罕见的明确以幻觉缓解为优化目标的开放权重模型。建议深入分析其训练目标（可能涉及事实一致性损失、检索增强或置信度正则化），并与 Qwen/DeepSeek 系列进行受控对比，提取可迁移的幻觉缓解技术。 |
| ⭐⭐☆ | [**deepseek-ai/DeepSeek-V4-Flash**](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | MIT 许可证与完整 eval-results 提供前所未有的研究透明度。建议利用其长上下文能力，构建需要跨文档推理的 OCR+RAG 基准测试，验证其在复杂文档理解中的事实保持能力，并对比 MTP 变体的效率-精度 trade-off。 |

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*