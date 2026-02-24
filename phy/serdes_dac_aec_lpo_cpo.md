
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
