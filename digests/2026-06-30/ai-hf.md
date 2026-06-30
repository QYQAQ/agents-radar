# Hugging Face 热门模型日报 2026-06-30

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-30 00:33 UTC

---

# Hugging Face 研究模型日报（2026-06-30）

## 1. 今日速览

今日 Hugging Face 热门模型中，**OCR 与文档理解**领域迎来百度 **Unlimited-OCR**，以高下载量显示文档识别需求持续旺盛；**多模态视觉语言**方面，Qwen3.5/3.6 与 Gemma 4 系列衍生模型占据主流，覆盖图文理解、视觉编码与量化部署。**长上下文与推理**模型亮点包括 Qwythos-9B-Claude-Mythos-5-1M 等扩展上下文衍生版本，以及 WeiboAI 的 VibeThinker-3B 数学推理小模型。Post-training 对齐与幻觉缓解虽未出现专门标签模型，但大量 GGUF 量化微调与 uncensored 变体反映社区后训练活动高度活跃。整体趋势显示：Qwen/Gemma/GLM 三大开源家族主导多模态与长上下文生态，而 OCR 与视觉 grounding 正成为新的研究热点。

---

## 2. 热门模型

### 📄 OCR 与文档模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) | baidu | 1,368 | 362,945 | 百度发布的通用 OCR/文档理解模型，主打无长度或版面限制的文本识别，是 HMER、文档分析与版面分析研究的直接相关基准。 |

---

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF) | empero-ai | 943 | 907,682 | 基于 Qwen3.5 的 1M 上下文视觉语言模型量化版，高下载量说明长上下文多模态部署需求强劲，适合跨模态长文档推理研究。 |
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | empero-ai | 558 | 79,540 | 上述模型的完整权重版，便于研究 1M 上下文 VLM 的微调、对齐与幻觉行为。 |
| [Qwen/Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B) | Qwen | 435 | 26,223 | Qwen3.5 MoE 架构的多模态 Agent 世界模型，体现视觉语言模型向 Agentic 交互与工具使用的演进。 |
| [deepreinforce-ai/Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B) | deepreinforce-ai | 274 | 19,170 | Qwen3.5 基础的多模态模型，MIT 许可证，适合作为 VLM 后训练与对齐研究的基础模型。 |
| [deepreinforce-ai/Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B) | deepreinforce-ai | 239 | 38,857 | 更大规模的 Ornith 多模态模型，可用于研究模型规模对视觉推理与幻觉的影响。 |
| [deepreinforce-ai/Ornith-1.0-397B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B) | deepreinforce-ai | 166 | 1,622 | 397B MoE 多模态模型，为超大规模 VLM 的效率、推理与对齐研究提供实验对象。 |
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 2,332 | 3,089,944 | Qwen3.6 MoE 的激进去审查视觉模型，极高下载量反映社区对多模态对齐边界的强烈兴趣，也是幻觉与安全对齐研究的反面案例。 |
| [HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Aggressive) | HauhauCS | 107 | 46,053 | Gemma 4 视觉模型的 QAT 量化去审查版本，适合研究量化对多模态模型对齐与幻觉的影响。 |
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,481 | 728,320 | NVIDIA 3B 视觉定位模型，高热度显示 visual grounding 与空间推理成为多模态研究新前沿，与 OCR/文档理解高度互补。 |

---

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) | zai-org | 2,934 | 133,350 | GLM 新一代 MoE+DSA 架构文本生成模型，高点赞反映开源社区对新型长上下文基础架构的关注。 |
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF) | empero-ai | 943 | 907,682 | 1M 上下文 Qwen3.5 量化模型，是长上下文检索、推理与幻觉评测的理想实验平台。 |
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | empero-ai | 558 | 79,540 | 完整版 1M 上下文模型，便于进行长上下文微调、对齐与 needle-in-haystack 评测。 |
| [yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 2,501 | 561,577 | Gemma 4 代码推理模型的高下载量版本，适合代码生成、长程序推理与工具使用研究。 |
| [yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF) | yuxinlu1 | 843 | 241,409 | Agentic 版本的 Gemma 4 代码模型，体现推理模型向自主 Agent 系统的迁移趋势。 |
| [deepseek-ai/DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark) | deepseek-ai | 211 | 5,460 | DeepSeek V4 Pro 衍生版本，附 arxiv 论文标签，适合作为长上下文与推理增强的基础研究模型。 |
| [deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) | deepseek-ai | 95 | 2,239 | DeepSeek V4 Flash 版本，关注推理效率与长上下文成本优化。 |
| [unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF) | unsloth | 464 | 164,180 | GLM-5.2 的 Unsloth 量化版，便于长上下文模型的低成本推理与微调实验。 |
| [WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B) | WeiboAI | 749 | 63,449 | 3B 数学推理专用小模型，适合研究小模型推理能力、蒸馏与长思维链生成。 |
| [Chunjiang-Intelligence/DeepSeek-v4-Fable](https://huggingface.co/Chunjiang-Intelligence/DeepSeek-v4-Fable) | Chunjiang-Intelligence | 130 | 1,463 | DeepSeek V4 网络安全领域微调版，可作为领域特定长上下文对齐与幻觉研究的案例。 |
| [unsloth/Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF) | unsloth | 113 | 116,693 | Qwen AgentWorld 的量化版，支持长上下文 Agent 推理的低成本研究。 |

---

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 2,332 | 3,089,944 | 激进对齐移除的 Qwen3.6 MoE 模型，是研究 RLHF/DPO 边界、安全对齐与偏好微调效果的极端案例。 |
| [HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced](https://huggingface.co/HauhauCS/Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced) | HauhauCS | 107 | 46,053 | 平衡版去审查 Gemma 4，结合 QAT 量化，适合研究量化与对齐干预的交互作用。 |
| [yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF) | yuxinlu1 | 2,501 | 561,577 | 基于 Fable/Composer 后训练配方的代码模型，反映社区后训练合成数据与 SFT/RL 方法的活跃。 |
| [yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF) | yuxinlu1 | 843 | 241,409 | Agentic 后训练变体，体现从 SFT 到工具调用与自主决策的对齐扩展。 |

---

### 👁️ 幻觉缓解

> 今日榜单中无直接标注"幻觉缓解"或"事实 grounded"的专门模型，但以下模型可作为幻觉研究的载体或对比对象：

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) | baidu | 1,368 | 362,945 | 文档 OCR 模型为幻觉研究提供可验证的文本 grounding 来源，适合探索 RAG+多模态的事实性增强。 |
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 2,481 | 728,320 | 视觉定位模型可作为 VLM 幻觉缓解的 grounding 模块，通过空间-文本对齐减少对象幻觉。 |
| [empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M) | empero-ai | 558 | 79,540 | 1M 上下文 VLM 是研究长上下文检索幻觉、位置偏差与事实一致性的重要平台。 |
| [WeiboAI/VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B) | WeiboAI | 749 | 63,449 | 数学推理小模型可用于研究推理链中的过度自信幻觉与校准方法。 |

---

### 🏗️ 研究基础设施

| 模型/工具 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [unsloth/GLM-5.2-GGUF](https://huggingface.co/unsloth/GLM-5.2-GGUF) | unsloth | 464 | 164,180 | Unsloth 量化版降低长上下文/对齐实验的计算门槛，是后训练研究的实用基础设施。 |
| [unsloth/Qwen-AgentWorld-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen-AgentWorld-35B-A3B-GGUF) | unsloth | 113 | 116,693 | Unsloth 对 Agent 世界模型的量化支持，便于 Agent 对齐与长上下文推理的低成本复现。 |
| [nvidia/GLM-5.2-NVFP4](https://huggingface.co/nvidia/GLM-5.2-NVFP4) | nvidia | 169 | 81,944 | NVIDIA NVFP4 精度优化版，为长上下文模型的高效推理与评测提供硬件协同基础设施。 |
| [nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | nvidia | 378 | 5,392,518 | 极高下载量的 NVFP4 优化版，是研究量化对多模态/长上下文模型对齐影响的重要基准。 |
| [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | nvidia | 742 | 76,154 | NVIDIA 流式 ASR 模型，可作为多模态语音-文本幻觉与对齐研究的补充基础设施。 |

---

## 3. 研究生态信号

今日榜单清晰显示 **Qwen（3.5/3.6）、Gemma 4 与 GLM 5.2** 三大开源家族主导多模态与长上下文生态，衍生出大量量化、Agentic、代码与去审查微调版本。视觉语言模型正从静态图文理解向 **Agent 工具使用、视觉定位与长文档推理** 扩展，[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) 的高热度标志着 visual grounding 成为新的研究前沿。OCR 领域 [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) 的高下载量反映文档理解需求强劲，但专门模型仍相对稀缺。后训练对齐方面，社区活动高度活跃但呈现"去审查化"倾向，[HauhauCS](https://huggingface.co/HauhauCS) 等账号的 uncensored 模型下载量惊人，这为安全对齐与幻觉缓解研究提供了反面数据集与对比实验对象。开源权重在 VLM 与长上下文领域已具备与闭源模型抗衡的规模与多样性，但专门面向幻觉缓解、事实 grounded 与可校准置信度的模型仍显不足，是值得投入的研究空白。

---

## 4. 值得探索

1. **[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**  
   作为榜单中唯一专注 OCR/文档理解的模型，它为 HMER、版面分析与长文档 OCR 提供了直接的研究对象，尤其适合探索 OCR 错误如何传播至多模态幻觉。

2. **[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**  
   高点赞高下载的视觉定位模型，可作为 VLM 幻觉缓解的 grounding 模块，研究空间-文本对齐如何减少对象幻觉与引用错误。

3. **[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**  
   1M 上下文的多模态模型，完整权重便于微调与对齐实验，是长上下文检索、needle-in-haystack 评测与多模态幻觉研究的理想平台。

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*