
# 从铜到光：高速 SerDes 演进 
From Copper to Optics: The Evolution of Serdes

> **注：** 以下数据以主流 **112G PAM4** 工艺节点为基准参考，部分前瞻性指标涉及 224G。

## 1. DAC Copper：铜缆的黄金时代 (LR Serdes)
*   **信道特征 (Channel Specs)：**
    *   **规格：** **LR (Long Reach)**
    *   **插损 (Insertion Loss)：** **> 30 dB @ Nyquist** (甚至达到 35dB+)。
    *   **挑战：** 极高的衰减和反射，信噪比 (SNR) 极低。
*   **关键指标 (Metrics)：**
    *   **功耗：** **~10 - 12 pJ/bit** (Host 端全开)。
    *   **带宽密度：** **低** (受限于庞大的 QSFP/OSFP 连接器和粗硬的铜缆体积)。
*   **架构与分工 (Architecture & Split)：**
    *   **分工：** **Host 独挑大梁**。Host 芯片直接驱动无源铜缆，远端芯片接收。
    *   **Host SerDes 架构：** **ADC + DSP 架构**。
        *   必须配备高抽头数的 FFE (Feed Forward Equalizer) 和 DFE (Decision Feedback Equalizer)。
        *   DSP 需要强大的 MLSE (Maximum Likelihood Sequence Estimation) 或复杂的纠错算法。
    *   **Transceiver/Cable：** 无源 (Passive)，仅作为物理传输介质。

## 2. AEC Copper：电缆的智能化救赎 (Retimer)
*   **信道特征 (Channel Specs)：**
    *   **规格：** **MR (Medium Reach) / LR**
    *   **插损：** Host 到 AEC 芯片通常 **15 - 20 dB**；AEC 芯片驱动剩余线缆。
*   **关键指标 (Metrics)：**
    *   **功耗：** Host 端 **~6 - 8 pJ/bit**；但线缆端增加了 **~4 - 6 pJ/bit**。系统总功耗并未降低，甚至略高。
    *   **带宽密度：** 中等 (线缆比 DAC 细，改善了布线密度)。
*   **架构与分工 (Architecture & Split)：**
    *   **分工：** **接力传输**。Host 负责驱动到线缆接口，AEC 芯片负责信号再生。
    *   **Host SerDes 架构：** **ADC + DSP** (配置可适当降低) 或 **高性能 Analog**。
    *   **Cable 架构：** **DSP Retimer**。
        *   线缆内部集成 CDR (Clock Data Recovery)，将信号解调、重整时钟后再发送。
        *   **代价：** 增加了延时 (Latency)。

## 3. Pluggable Optical Module：光模块的标准时代 (C2M)
*   **信道特征 (Channel Specs)：**
    *   **规格：** **VSR (Very Short Reach) / MR**，遵循 OIF-CEI-112G-VSR/MR 标准。
    *   **插损：** **10 - 16 dB @ Nyquist** (PCB 走线 + 连接器)。
*   **关键指标 (Metrics)：**
    *   **功耗：** Host 端 **~4 - 6 pJ/bit**；光模块端 DSP 功耗巨大 (单模块 20W+)。
    *   **带宽密度：** 受限于面板尺寸 (Faceplate limited)，约 **100 - 200 Gbps/mm** (沿板边)。
*   **架构与分工 (Architecture & Split)：**
    *   **分工：** **数字解耦**。Host 和 Module 之间是标准的数字信号再生关系。
    *   **Host SerDes 架构：** **ADC + DSP** (VSR 模式) 或 **Analog SerDes**。
    *   **Module 架构：** **DSP Based**。
        *   模块内含独立的 DSP 芯片，负责电信号的 CDR、均衡以及光器件的非线性补偿。
        *   **双重 DSP：** 链路中存在两颗 DSP (Host + Module)，导致功耗和延时叠加。

## 4. LPO (Linear Pluggable Optics)：去 DSP 化的低功耗尝试
*   **信道特征 (Channel Specs)：**
    *   **规格：** **Linear Drive (线性直驱)**。
    *   **插损：** **10 - 12 dB** (Host 到光模块 Driver)。
    *   **特殊要求：** 极高的**线性度 (Linearity)**，要求低 THD (总谐波失真)。
*   **关键指标 (Metrics)：**
    *   **功耗：** Host 端略增至 **~6 - 7 pJ/bit** (需更强均衡)；但模块端功耗降低 **50%** (去掉了 DSP)。
    *   **带宽密度：** 与传统光模块持平。
*   **架构与分工 (Architecture & Split)：**
    *   **分工：** **模拟透传**。Host 直接控制光信号的波形，模块仅做光电转换放大。
    *   **Host SerDes 架构：** **强化的 ADC + DSP**。
        *   必须具备补偿光器件非线性和色散的能力 (Pre-distortion)。
    *   **Module 架构：** **Analog Only (Linear TIA/Driver)**。
        *   移除了 DSP/CDR，信号在模块内不进行数字重整。

## 5. Co-package Optical Module (CPO)：终极形态——光电合封
*   **信道特征 (Channel Specs)：**
    *   **规格：** **XSR (Extra Short Reach)** 或 **UCIe/D2D**。
    *   **插损：** **< 5 - 10 dB @ Nyquist** (毫米级走线)。
*   **关键指标 (Metrics)：**
    *   **功耗：** **< 1 - 2 pJ/bit** (XSR) 甚至 **< 0.5 pJ/bit** (D2D)。
    *   **带宽密度：** **极高**。可达 **500 - 1000+ Gbps/mm** (Shoreline density)。
*   **架构与分工 (Architecture & Split)：**
    *   **分工：** **极致融合**。Host 与光引擎 (EIC/PIC) 封装在同一基板上。
    *   **Host SerDes 架构：** **Simplified Analog / Parallel D2D**。
        *   去掉了复杂的长距均衡电路，甚至不再使用传统的 SerDes 架构，转而使用宽并行、低电压的接口 (如 UCIe)。
    *   **Module (Optical Engine) 架构：** **Analog / Silicon Photonics**。
        *   光电转换紧贴计算核心，消除了寄生参数影响。

## 6. Technical Drivers：高速互连演进的三大博弈逻辑

### 1. 距离的博弈：电信号“跑不动”了
*   **逻辑验证：** 随着频率升高（从 10G 到 112G/224G），电信号在 PCB 和铜缆上的趋肤效应和介质损耗呈指数级上升。
*   **演进对应：**
    *   **DAC (LR)：** 硬抗损耗，但传输距离越来越短。
    *   **AEC：** 跑不动了，加个中继站（Retimer）接着跑。
    *   **CPO (XSR)：** 既然电跑不动，那就别跑了，直接在芯片旁边转成光。
*   **结论：** SerDes 的演进史，就是**电通道 (Electrical Channel) 不断变短**的历史。

### 2. 功耗的博弈：DSP 是把双刃剑
*   **逻辑验证：** 为了解决信号完整性问题，引入了强大的 DSP（数字信号处理）。DSP 虽然能修复劣质信号，但它像个“电老虎”，功耗巨大且增加延时。
*   **演进对应：**
    *   **Pluggable Module：** 为了标准化，在模块里放了 DSP，结果模块功耗爆炸（20W+）。
    *   **LPO：** 为了省电，尝试把模块里的 DSP 去掉，让 Host SerDes 多干点活（线性直驱）。
    *   **CPO：** 为了极致省电，彻底去掉长距离传输所需的复杂 DSP，改用超短距、低功耗的驱动电路。
*   **结论：** 演进的动力之一是**“去 DSP 化”或“DSP 轻量化”**，以降低 pJ/bit。

### 3. 密度的博弈：面板塞不下了
*   **逻辑验证：** 交换机容量从 12.8T 到 25.6T 再到 51.2T，前面板的空间是有限的 (Faceplate density limit)。QSFP/OSFP 模块体积太大，限制了带宽密度。
*   **演进对应：**
    *   **DAC/AEC/Pluggable：** 都受限于物理连接器 (Connector) 的体积。
    *   **CPO：** 抛弃了面板上的粗大接口，光纤直接从芯片引出，密度提升一个数量级。

### 4. 结论
*   **结论：** 演进的终局是 **IO 密度 (Gbps/mm) 的爆发式增长**。


## 巨头博弈：AI 计算领域的光铜技术选择对比

不同公司由于其在产业链中的位置（芯片设计 vs. 终端用户 vs. 设备商）以及自身的架构积累，对“光进铜退”的节奏和技术路线选择存在显著差异。

---

### 1. 芯片设计巨头 (Chip Designers)
**核心逻辑：** 追求极致的算力密度和互连带宽，定义物理层标准。

#### **NVIDIA (英伟达)**
*   **核心策略：** **铜的极限挖掘者 + 光的坚定拥护者**
*   **铜 (Copper) 选择：**
    *   **NVL72 架构 (Blackwell)：** 在单机柜内部（72卡互连），放弃光互连，使用 **5000+ 根铜缆** 构建巨大的铜背板 (Copper Backplane)。
    *   **理由：** 机柜内短距 (<1m) 场景下，铜的功耗、成本和可靠性优于光。通过私有协议 (NVLink) 和定制 SerDes 榨干铜的物理极限。
*   **光 (Optics) 选择：**
    *   **Scale-out (机柜间)：** 全面拥抱光 (InfiniBand / Spectrum-X Ethernet)。
    *   **路线：** 主流为可插拔模块 (OSFP)，积极布局 **LPO** 和 **CPO** 以应对未来 X1600 互连。

#### **Intel (英特尔)**
*   **核心策略：** **硅光技术的领跑者 (Silicon Photonics Leader)**
*   **铜 (Copper) 选择：**
    *   传统服务器依然大量使用 DAC/AEC，但在 AI 高性能集群试图通过光技术弯道超车。
*   **光 (Optics) 选择：**
    *   **CPO (光电合封)：** 利用 IDM 优势，致力于将硅光引擎直接集成到 CPU/XPU 封装中。
    *   **路线：** 演示 TCP (Tightly Coupled Photonics) 技术，主导 UEC 标准，推动全光互连。

#### **AMD**
*   **核心策略：** **务实的 Chiplet 拥护者**
*   **铜 (Copper) 选择：**
    *   Infinity Fabric 在节点内互连依然依赖高性能 PCB 和铜。
*   **光 (Optics) 选择：**
    *   **合作生态：** 倾向于与光模块厂商合作而非全自研。
    *   **路线：** 重点关注 **LPO** (低功耗/高性价比)，利用 UCIe 接口标准为集成光 Chiplet 铺路。

---

### 2. 互联网/云服务巨头 (Hyperscalers)
**核心逻辑：** 追求大规模集群的 TCO (总拥有成本) 和能效比，愿意尝试定制化方案。

#### **Google**
*   **核心策略：** **光交换的先驱 (Optical First)**
*   **铜 (Copper) 选择：**
    *   仅在 TPU Pod 内部极短距离使用 DAC。
*   **光 (Optics) 选择：**
    *   **OCS (Optical Circuit Switch)：** 全球唯一大规模商用 OCS (Apollo 网络)，用 MEMS 镜面反射光信号替代传统电交换。
    *   **路线：** 极其激进，大量定制光模块，推动 800G/1.6T 快速落地，看重光的灵活性和低延时。

#### **Microsoft (Azure)**
*   **核心策略：** **AEC 的最大推手 + 标准化以太网**
*   **铜 (Copper) 选择：**
    *   **AEC (有源电缆)：** 微软是 AEC 技术的最大买家。解决 112G 时代 DAC 线缆太粗太硬、无法在拥挤机架中布线的痛点。
*   **光 (Optics) 选择：**
    *   **InfiniBand & Ethernet：** AI 集群 (ChatGPT 训练) 大量使用 IB 光互连。
    *   **路线：** 正在从可插拔向 **CPO/NPO** (Near Package Optics) 演进，旨在降低数据中心 PUE。

---


### 4. 网络交换核心：芯片与系统厂商的架构抉择

处于产业链核心位置的交换芯片与设备厂商，直接决定了 SerDes 速率的演进节奏。它们需要在**单芯片容量 (Switch Capacity)**、**功耗 (Power)** 和 **I/O 密度** 之间寻找平衡。

---

#### Broadcom (博通)：商用芯片的 CPO 激进派
**角色定位：** 全球最大的商用交换芯片供应商 (Merchant Silicon)，其 Tomahawk 和 Jericho 系列芯片定义了数据中心网络的代际演进。

##### 1. SerDes 演进策略：定义行业标杆
*   **技术现状：** Broadcom 的 **Peregrine SerDes IP** 是行业的标杆。在 **Tomahawk 5 (51.2T)** 这一代，其 100G PAM4 SerDes 展现了极强的驱动能力，依然能够支持 3-4 米的 DAC 铜缆，强行延续了铜缆的生命周期。
*   **未来规划：** 在 **Tomahawk 6 (102.4T)** 及 224G 时代，Broadcom 明确指出 PCB 和铜缆的物理极限已到，电信号传输距离将大幅缩短。

##### 2. 光/铜路线选择：CPO 的最大推手
*   **CPO (光电合封) 战略：**
    *   Broadcom 是 CPO 技术最激进的推动者。他们推出了 **"Bailly"** CPO 交换机系统，将硅光引擎 (Silicon Photonics Engine) 直接与 Tomahawk 芯片封装在一起。
    *   **商业逻辑：** 通过 CPO，Broadcom 不仅卖交换芯片，还能把高价值的光互连组件（光引擎）一并卖给客户，从而在后摩尔定律时代通过“系统级销售”维持高利润。
*   **铜的定位：** 在 51.2T 节点，依然提供支持 DAC/AEC 的标准版本，以满足成本敏感型客户（如二线云厂商）的需求。

---

#### Huawei (华为)：端到端系统的 LPO 务实派
**角色定位：** 拥有自研芯片 (Hisilicon)、光模块 (Hisilicon Optoelectronics) 和交换机 (CloudEngine) 的全栈系统厂商。

##### 1. SerDes 演进策略：系统级协同优化
*   **技术现状：** 依托海思芯片，华为在 SerDes 与系统背板的协同设计上具有独特优势。
*   **核心理念：** **“无损网络” (Lossless Ethernet)**。华为非常看重低延时和零丢包，因此对 SerDes 的误码率 (BER) 和链路稳定性要求极高。

##### 2. 光/铜路线选择：LPO 的坚定捍卫者
*   **LPO (线性直驱) 战略：**
    *   华为是 LPO 技术的主要贡献者和早期采用者。
    *   **技术逻辑：** LPO 移除了光模块中的 DSP，虽然对 Host SerDes 的线性度要求极高，但华为作为**系统厂商**，可以同时控制交换机芯片 (Host) 和光模块 (Module) 的设计。这种**端到端的控制力**使得华为能够完美调校链路，解决 LPO 的互操作性难题，从而获得更低的功耗和延时。
*   **全光底座：** 华为倾向于将光技术下沉。在 AI 集群 (Atlas 900) 中，华为利用其在光传输领域的积累，推动全光互连，减少电层的转换跳数。

---

### 全局总结对比表 (更新版)

| 公司类型 | 代表公司 | 铜 (Copper) 策略 | 光 (Optics) 策略 | 关键技术关键词 |
| :--- | :--- | :--- | :--- | :--- |
| **芯片设计** | **NVIDIA** | **极致挖掘** (NVL72 铜背板) | **Scale-out 标配** (OSFP) | NVLink, Copper Backplane |
| | **Intel** | 传统应用 | **激进集成** (CPO/SiPh) | Silicon Photonics, CPO |
| | **AMD** | 节点内互连 | **务实演进** (LPO/UCIe) | Infinity Fabric, Chiplet |
| **互联网** | **Google** | 极短距应用 | **架构革新** (OCS 光交换) | OCS, TPU Pods |
| | **Microsoft** | **AEC 主力军** (解决布线痛点) | 标准化 IB/Ethernet | AEC, InfiniBand |
| **交换机/系统** | **Broadcom** | **延续生命** (强力 SerDes 支持 DAC) | **商业整合** (CPO 吞噬光引擎) | Tomahawk, CPO (Bailly) |
| | **Huawei** | 逐步替代 | **系统优化** (LPO 端到端调校) | LPO, Lossless Ethernet |

---

### 行业趋势总结

1.  **铜的韧性 (Copper Resilience)：**
    *   NVIDIA 和 Broadcom 证明了，只要系统设计得当（如 NVL72 背板）或 SerDes 足够强（Tomahawk 5），铜在机柜内部（Scale-up）依然是**成本和功耗的王者**。

2.  **光的两条路 (The Fork in the Road for Optics)：**
    *   **LPO (演进派)：** 以华为、AMD 为代表。在不改变现有封装形态的前提下，通过去 DSP 化降低功耗。这需要强大的**系统级调校能力**。
    *   **CPO (革命派)：** 以 Intel、Broadcom 为代表。试图将光引擎封装进芯片，彻底解决 I/O 瓶颈。这更多是**商业模式和封装技术**的竞争。

3.  **终局思维 (End Game)：**
    *   无论是互联网巨头（Google OCS）还是设备商（Huawei 全光网），大家的终极目标都是**“光进铜退”**，将光传输尽可能地靠近计算核心 (ASIC)，以打破物理损耗的墙。
```
