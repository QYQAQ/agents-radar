# Hugging Face 热门模型日报 2026-07-12

> 数据来源: [Hugging Face Hub](https://huggingface.co/) | 共 30 个模型 | 生成时间: 2026-07-12 00:24 UTC

---

# Hugging Face 研究模型日报｜2026-07-12

## 1. 今日速览

本日 Hugging Face 热门模型中，**OCR 与文档理解**和**多模态推理**持续升温：baidu/Unlimited-OCR 以近 200 万下载量领跑文档理解类模型；Qwen3.5/3.6 生态在 image-text-to-text 与长上下文推理赛道占据主导，empero-ai/Qwythos 1M 上下文模型兼具多模态与推理标签。后训练社区活跃度显著，大量基于 Qwen、Gemma、MiniCPM 的融合/微调/量化模型上榜，涉及 chat-template、thinking trace、agentic 等方向。视觉 grounding 与长上下文推理的结合，为幻觉缓解研究提供了新的开源基线。

---

## 2. 热门模型

### 📄 OCR 与文档模型

**[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**
- 作者：baidu｜点赞：1,929｜下载：1,380,690
- 百度发布的文档/图像文本理解模型，上榜原因是下载量极高，适合作为 OCR、版面分析与文档理解研究的强 baseline 与工业落地参考。

**[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**
- 作者：empero-ai｜点赞：2,010｜下载：1,944,961
- 1M 上下文 Qwen3.5 多模态量化模型，兼具 image-text-to-text 与 reasoning 标签，可用于长文档 OCR+推理的端侧部署研究。

**[empero-ai/Qwythos-9B-Claude-Mythos-5-1M](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M)**
- 作者：empero-ai｜点赞：768｜下载：186,852
- 同名非量化版，适合研究多模态长上下文中的文档理解与数学/公式识别能力。

**[migtissera/Tess-4-27B](https://huggingface.co/migtissera/Tess-4-27B)**
- 作者：migtissera｜点赞：84｜下载：806
- 基于 Qwen3.5 的 27B image-text-to-text 模型，社区后训练产物，适合探索多模态文档任务中的微调效果。

---

### 🎭 多模态与视觉语言

**[bottlecapai/ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**
- 作者：bottlecapai｜点赞：235｜下载：4,128
- Qwen3.6 视觉语言模型，强调 thinking 能力，可用于研究多模态链式推理与视觉问答中的可解释性。

**[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**
- 作者：HauhauCS｜点赞：2,650｜下载：2,641,936
- 35B MoE 视觉语言模型，热度极高，可用于研究后训练对多模态模型对齐与指令遵循的影响。

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**
- 作者：nvidia｜点赞：2,707｜下载：1,472,194
- NVIDIA 视觉 grounding/特征提取模型，与幻觉缓解和视觉定位研究高度相关，适合作为跨模态对齐的轻量基线。

**[unsloth/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**
- 作者：unsloth｜点赞：1,047｜下载：2,904,169
- Unsloth 发布的 Qwen3.6 27B 量化版，下载量极大，适合多模态推理的低成本推理与后训练实验。

**[InternScience/Agents-A1](https://huggingface.co/InternScience/Agents-A1)**
- 作者：InternScience｜点赞：492｜下载：28,141
- 基于 Qwen3.5 MoE 的 image-text-to-text 模型，面向 agent 场景，适合研究多模态工具调用与长程推理。

---

### 🧠 长上下文与推理模型

**[empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**
- 作者：empero-ai｜点赞：2,010｜下载：1,944,961
- 1M 上下文、多模态、reasoning 三标签合一，是研究长上下文推理与长文档多模态理解的理想实验对象。

**[zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**
- 作者：zai-org｜点赞：3,830｜下载：421,270
- 智谱 GLM 5.2 对话模型，点赞数最高，可作为长上下文与对话推理研究的中文基线。

**[deepreinforce-ai/Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**
- 作者：deepreinforce-ai｜点赞：850｜下载：1,216,495
- 35B 量化推理模型，MIT 许可且兼容推理端点，适合长上下文推理与端侧部署研究。

**[nvidia/NVIDIA-Nemotron-Labs-3-Puzzle-75B-A9B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Puzzle-75B-A9B-NVFP4)**
- 作者：nvidia｜点赞：105｜下载：30,418
- NVIDIA Nemotron Labs 75B 级 Puzzle 模型，面向复杂推理任务，适合研究长程规划与推理评估。

**[GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**
- 作者：GnLOLot｜点赞：191｜下载：29,887
- 1B 级 MiniCPM5 thinking 量化模型，适合研究小模型上的推理能力与思维链蒸馏。

---

### 🔧 Post-Training 与对齐

**[froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**
- 作者：froggeric｜点赞：852｜下载：0
- Qwen chat-template 修正资源，直接服务于后训练阶段模板工程与指令对齐研究。

**[HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**
- 作者：HauhauCS｜点赞：2,650｜下载：2,641,936
- “Uncensored/Aggressive” 微调变体，可用于研究安全对齐、偏好微调与模型行为边界。

**[yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**
- 作者：yuxinlu1｜点赞：1,148｜下载：436,530
- Gemma4 多来源融合 agentic/coding 模型，体现社区在后训练模型融合与能力组合上的活跃探索。

**[AliesTaha/fable-traces](https://huggingface.co/AliesTaha/fable-traces)**
- 作者：AliesTaha｜点赞：199｜下载：5,053
- 基于 Qwen3 的 instruct 模型，名称提示可能包含 reasoning traces，适合研究推理轨迹监督与 SFT。

---

### 👁️ 幻觉缓解

**[nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**
- 作者：nvidia｜点赞：2,707｜下载：1,472,194
- 视觉定位模型，通过像素级 grounding 为 VLM 生成提供事实锚点，是缓解视觉幻觉的重要工具。

**[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**
- 作者：baidu｜点赞：1,929｜下载：1,380,690
- 高精度文档 OCR 可为大模型提供“文本

---
*本日报由 [agents-radar](https://github.com/QYQAQ/agents-radar) 自动生成。*