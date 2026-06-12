# Hugging Face 热门模型日报 2026-06-12

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-06-12 00:38 UTC

---

# Hugging Face 研究模型日报 | 2026-06-12

---

## 今日速览

本周 Hugging Face 热点呈现**多模态统一架构**与**高效推理**两大主线。Google Gemma-4 系列以 "any-to-any" 范式强势霸榜，其原生多模态设计与量化友好特性引发研究社区高度关注，直接关联视觉语言推理与长上下文研究。NVIDIA LocateAnything-3B 在开放集视觉定位领域取得突破，为文档版面分析与细粒度 OCR 提供新工具。DeepSeek-V4-Pro 以压倒性下载量（400万+）验证 MoE 架构在推理任务中的规模化优势。值得注意的是，对齐与后训练领域出现活跃社区微调活动，围绕 Gemma-4 的 abliteration 与 uncensored 变体反映研究者对模型可控性与价值对齐的持续探索。

---

## 热门模型

### 🎭 多模态与视觉语言

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | nvidia | 1,869 | 131,794 | **开放集视觉定位模型**，支持任意文本描述定位图像区域；与 OCR/HMER 研究高度相关——可赋能文档版面分析、公式区域检测及手写数学表达式的空间定位，弥补传统 OCR 缺乏语义理解的短板。 |
| [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | google | 939 | 675,936 | **原生多模态统一架构**（any-to-any），单模型处理图文交错输入输出；视觉语言推理的核心基座，其统一表征为跨模态长上下文推理与幻觉缓解研究提供理想实验平台。 |
| [google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B) | google | 516 | 140,221 | Gemma-4 基础版本，保留预训练灵活性；适合研究者针对 OCR、文档理解等垂直领域进行领域自适应后训练。 |
| [unsloth/gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF) | unsloth | 561 | 711,706 | Gemma-4 的高效量化版，下载量超官方原版；降低多模态推理研究门槛，便于长上下文实验的本地部署与迭代。 |
| [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) | HauhauCS | 1,675 | 3,057,541 | **社区激进对齐解除版** MoE VLM，下载量本周最高；其"uncensored"标签反映后训练对齐的脆弱性，为幻觉缓解与价值对齐研究提供反面案例与对抗测试基准。 |
| [stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) | stepfun-ai | 368 | 50,187 | 阶跃星辰视觉语言模型，强调推理效率；其 vision-language 架构在中文场景文档理解中的潜力值得 OCR 研究者验证。 |
| [nex-agi/Nex-N2-Pro](https://huggingface.co/nex-agi/Nex-N2-Pro) / [Nex-N2-mini](https://huggingface.co/nex-agi/Nex-N2-mini) | nex-agi | 206/163 | 1,185/1,222 | 基于 Qwen3.5-MoE 的多模态模型；社区对 MoE+多模态组合的持续探索，为推理效率与模型容量权衡研究提供新数据点。 |
| [unsloth/gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF) | unsloth | 142 | 129,110 | Gemma-4 26B MoE 量化版；大容量多模态模型的端侧部署方案，支撑长上下文多模态推理的硬件可行性研究。 |

### 🧠 长上下文与推理模型

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | deepseek-ai | 4,781 | 4,061,006 | **本周绝对霸主**，MoE 架构推理旗舰；其长上下文处理能力（推测 256K+）与数学/代码推理优势，为长程依赖建模与复杂推理链研究提供最强开源基线。 |
| [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | google | 486 | 0 | **扩散语言模型**，将离散文本生成转化为连续扩散过程；革新性架构为长文本连贯性生成与迭代式推理修正开辟新路径，可能缓解自回归模型的累积幻觉问题。 |
| [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | CohereLabs | 307 | 1,859 | Cohere MoE 代码模型；结构化推理与长程代码依赖理解能力，可迁移至数学公式结构预测与 LaTeX 生成任务。 |
| [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) | LiquidAI | 594 | 142,134 | 液态神经网络架构 MoE 模型；非传统循环结构在长序列建模中的记忆优势，为超越 Transformer 的长上下文机制探索提供对比基准。 |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) / [NVFP4 版](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4) | nvidia | 198/168 | 59,066/91,117 | 550B 总参数/55B 激活的超大 MoE，NVFP4 量化版下载更高；超大规模模型的推理效率与长上下文扩展极限的工业级参考。 |

### 🔧 Post-Training 与对齐

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated) | huihui-ai | 143 | 6,400 | **Gemma-4 对齐擦除版**（abliterated），移除原始安全微调；直接暴露后训练对齐的"手术"可行性，为对齐鲁棒性、越狱机制与防御性微调研究提供可控实验对象。 |
| [OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED) | OBLITERATUS | 234 | 14,838 | 另一 Gemma-4 对齐解除变体，命名更激进；社区对齐解除活动的重复出现，暗示当前 RLHF/DPO 方法可能存在系统性脆弱模式。 |
| [unsloth/gemma-4-12B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-12B-it-qat-GGUF) / [gemma-4-26B-A4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-qat-GGUF) | unsloth | 200/142 | 148,252/129,110 | QAT（量化感知训练）版 Gemma-4；后训练阶段的量化友好优化，为对齐阶段的效率-性能帕累托前沿研究提供新工具。 |
| [google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) | google | 129 | 96,749 | 官方 QAT GGUF，验证社区量化路线的正确性；官方与社区后训练技术的收敛，标志多模态模型部署标准的形成。 |

### 👁️ 幻觉缓解（间接相关）

| 模型 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [sapientinc/HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B) | sapientinc | 749 | 134,752 | **HRM（Human Resource Management?）文本模型**，标签含 "hrm_text"；若涉及结构化事实生成，其高下载量暗示行业对可靠文本生成的需求，需进一步验证其事实 grounding 机制。 |
| [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | nvidia | 372 | 4,965 | **流式 ASR 模型**，cache-aware 设计；实时语音转录的延迟-准确性权衡，其流式解码机制可启发视觉语言模型的渐进式/流式文档理解，减少长序列生成的幻觉累积。 |

### 🏗️ 研究基础设施

| 模型/工具 | 作者 | 点赞 | 下载 | 一句话说明 |
|:---|:---|---:|---:|:---|
| [unsloth/diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF) | unsloth | 179 | 0 | 扩散语言模型的首个 GGUF 实现；新型生成架构的社区基础设施支持，降低扩散模型在 NLP 研究中的准入门槛。 |

---

## 研究生态信号

**Gemma-4 家族形成多模态研究新基座**：Google 以 12B/26B 双规模、官方/社区量化多形态覆盖，确立 "any-to-any" 为视觉语言模型新标准。其原生多模态设计区别于拼接式 VLM，为 OCR 研究者的端到端文档理解实验提供统一框架。开源权重策略持续强化——Gemma-4 下载量分布显示社区量化版（unsloth GGUF）反超官方原版，反映研究者对高效部署的刚性需求，也暗示未来基座模型的竞争力将包含"后训练生态友好度"。对齐领域呈现**对抗性张力**：Huihui-ai、OBLITERATUS 等社区的 abliteration 活动与官方版本并行传播，表明当前 RLHF 的安全边界可被低成本逆向工程，这对幻觉缓解研究既是挑战（对齐失效即幻觉风险）也是机遇（生成对抗性测试数据）。值得注意的是，**扩散语言模型**（DiffusionGemma）的出现可能重塑长文本生成与推理范式——其迭代去噪机制天然支持"反思式"生成，或为缓解自回归幻觉提供根本性新路径。

---

## 值得探索

| 优先级 | 模型 | 研究理由 |
|:---|:---|:---|
| ⭐⭐⭐ | [nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B) | **OCR/HMER 研究的直接工具升级**。开放集定位能力可突破传统文档 OCR 的预定义版面假设，手写数学公式的任意描述定位（如"找到二次求根公式"→空间坐标）将重新定义公式识别流程。建议探索：与 SATRN/TrOCR 等编码器级联，构建"定位-识别-解析"全链路。 |
| ⭐⭐⭐ | [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | **幻觉缓解的范式级机会**。扩散模型在图像生成中已验证的"迭代修正"特性，迁移至文本域可能实现：长文档生成中的事实一致性自检、数学推理中的多步验证回溯。关键假设：扩散时间步可作为"推理深度"的显式控制变量，值得与链式思维（CoT）机制对比研究。 |
| ⭐⭐☆ | [huihui-ai/Huihui-gemma-4-12B-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-12B-it-abliterated) + [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | **对齐鲁棒性的控制实验对**。同一基座的对齐/未对齐版本同时可用，为量化分析 RLHF 对幻觉率、事实性、拒绝行为的影响提供罕见天然实验组。建议构建：多模态幻觉评测基准（如文档中的图文矛盾检测），对比两版本的错误模式差异。 |

---

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*