# Synopsys DesignWare 高速 SerDes PHY IP 核心规格汇总表

本文档汇总了 Synopsys 在先进制程（7nm/5nm/3nm）下的主流 SerDes PHY IP 核心参数，用于芯片架构选型及 PPA 审阅。


| PHY 系列名称 | 核心架构 | 最高速率 / 协议支持 | 插损支持 (IL) | 能效比 (pJ/bit) | 面积密度 (Gbps/mm²) | 配套 PCS 层 | LPO 支持情况 | 官方产品链接 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **224G PHY** | **纯 DSP (ADC)** | 1.6T Eth / PCIe 7.0 | **45 dB+** | 4.0 - 5.5 | **> 400** | 802.3dj / 1.6T | **深度支持 (2.0)** | [224G SerDes](https://www.synopsys.com) |
| **112G PHY** | **DSP (ADC)** | 800G Eth / PCIe 6.0 / CXL 3.0 | **38-40 dB** | 3.5 - 4.5 | 250 - 300 | 112G / RS-FEC | **主流支持 (1.0)** | [112G SerDes](https://www.synopsys.com) |
| **56G/64G PHY** | **混合 / DSP** | 400G Eth / PCIe 5.0 / CXL 2.0 | **32-35 dB** | 4.5 - 6.0 | 100 - 150 | Multi-rate PCS | 支持较弱 | [56G SerDes](https://www.synopsys.com) |
| **32G Multi-Prot** | **纯 AMS (模拟)** | 25G Eth / PCIe 4.0 / USB 3.2 | **24-28 dB** | 3.0 - 5.0 | 60 - 90 | PCIe & Eth PCS | 不支持 | [32G SerDes](https://www.synopsys.com) |
| **16G Multi-Prot** | **纯 AMS (模拟)** | 10G Eth / PCIe 3.1 / SATA 3 | **15-22 dB** | 2.5 - 4.0 | 40 - 60 | 8b/10b 混合层 | 不支持 | [16G SerDes](https://www.synopsys.com) |

---

### 🛠️ 核心架构审阅要点 (Key Review Points)

#### 1. 架构选型 (Architecture: DSP vs. AMS)
*   **DSP-based (ADC) [112G/224G]:** 
    *   **原理：** 采用高速 ADC 将模拟信号数字化，通过数字均衡器（FFE/DFE）处理。
    *   **优势：** 极强的插损补偿能力（IL > 40dB），支持 **LPO（线性直驱）**，在 5nm/3nm 下具有更好的 PPA 缩放性。
*   **AMS-based (Analog) [32G及以下]:** 
    *   **原理：** 基于传统模拟 CTLE 和时钟恢复逻辑。
    *   **优势：** **超低延迟 (Latency)**、极小面积。适用于链路短、对成本极其敏感的消费级或车载局部互联。

#### 2. LPO (Linear Drive Pluggable Optics) 兼容性
*   **实现原理：** LPO 模组省去了内部 DSP 以降低功耗（~2W/端口）。
*   **硬件要求：** 主机侧（Host）PHY 必须具备极强的接收端均衡余量。
*   **Synopsys 表现：** 其 [112G/224G SerDes PHY](https://www.synopsys.com) 的数字前端（AFE）和 DSP 算法专为应对 LPO 导致的信号衰减和抖动而设计。

#### 3. 核心物理指标 (PPA Metrics)
*   **pJ/bit (能效比):** 衡量单比特传输功耗。112G/224G 虽采用 DSP，但单比特功耗通过先进制程红利维持在较低水平。
*   **Gbps/mm² (面积密度):** 关键指标。在 AI 交换芯片设计中，高密度 PHY（如 224G）能显著缩小芯片尺寸并增加有效 IO 数量。

#### 4. 物理编码子层 (PCS) 适配
*   **协议转换：** Synopsys 的 [Ethernet PCS](https://www.synopsys.com) 或 [PCIe Controller](https://www.synopsys.com) 与物理层 PMA 深度绑定。
*   **FEC 支持：** 针对 100G+ 速率，PCS 强制集成 **RS-FEC (544, 514)** 或更复杂的级联纠错逻辑，以确保在 PAM-4 信号下的低误码率。

---

### 🔗 官方资源速览
*   **SerDes PHY 家族总览:** [Synopsys SerDes IP Portfolio](https://www.synopsys.com)
*   **以太网全栈方案 (MAC/PCS/PHY):** [DesignWare Ethernet IP](https://www.synopsys.com)
*   **PCIe 与 CXL 解决方案:** [DesignWare PCIe IP](https://www.synopsys.com)
