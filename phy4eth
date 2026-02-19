# 以太网协议全维度技术参数枚举表 (IEEE 802.3)


| 速率层级 | 信号调制 | 通道数 (Lanes) | 物理连接器 (Connector) | 外部PHY/模组需求 | 车载/前沿技术 (Auto/LPO) | Synopsys IP 支持 [官网链接] |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **10/100M** | Manchester | 1 | RJ45 | **必选**外部PHY | 10Base-T1S / 100Base-T1 | [Ethernet 10/100 IP](https://www.synopsys.com) |
| **1G** | PAM-5 / NRZ | 1 / 4 | RJ45, SFP | **必选**外部PHY(铜线) | 1000Base-T1 | [Gigabit Ethernet IP](https://www.synopsys.com) |
| **10G** | NRZ/PAM-16 | 1 / 4 | RJ45, SFP+ | RJ45需PHY; SFP+直连 | 10GBase-T1 | [10G PHY & PCS](https://www.synopsys.com) |
| **25/40G** | NRZ | 1 / 4 | SFP28, QSFP+ | 通常直连 SerDes | N/A | [25G/40G Enterprise](https://www.synopsys.com) |
| **100G** | NRZ/PAM-4 | 4 / 10 / 1 | QSFP28, QSFP-DD | **支持 LPO** (线性直驱) | 适配数据中心高速链路 | [100G MAC/PCS](https://www.synopsys.com) |
| **400G** | PAM-4 | 4 / 8 / 16 | QSFP-DD, OSFP | **依赖 LPO 1.0** (省DSP) | 超大规模数据中心 | [400G/800G MAC](https://www.synopsys.com) |
| **800G** | PAM-4 | 8 | QSFP-DD800, OSFP | **依赖 LPO 2.0** | 112G SerDes 关键应用 | [800G Ethernet IP](https://www.synopsys.com) |
| **1.6T** | PAM-4 | 8 / 16 | OSFP-XD | **224G SerDes 直连** | IEEE 802.3dj 标准中 | [1.6T IP 全栈方案](https://www.synopsys.com) |

---

### 📋 核心技术维度解析

#### 1. 外部 PHY 与模组需求 (External PHY vs Module)
*   **铜线 (BASE-T):** 由于 RJ45 传输需要复杂的模拟驱动和磁隔离，SoC 通常只集成 MAC，必须搭配外部独立 PHY 芯片（如 Marvell 或 Realtek）。
*   **光纤/DAC (BASE-R):** 高速 SerDes 信号通常直接从芯片引出至连接器。在 100G+ 速率下，可选择带 DSP 的标准模组，或选择 **LPO（线性可插拔光学）** 方案以大幅降低功耗和延迟。

#### 2. 车载以太网 (Automotive Ethernet)
*   **物理层:** 采用 **Single Pair Ethernet (SPE)** 技术，仅需一对双绞线以减轻车重。
*   **协议栈:** 深度依赖 [Synopsys TSN IP](https://www.synopsys.com) 实现时间敏感联网，确保自动驾驶数据的实时性。
*   **连接器:** 使用专用抗震接口（如 HSD, Mini-FAKRA）。

#### 3. LPO (Linear Drive Pluggable Optics) 适配要求
*   LPO 移除光模块内部 DSP，将信号均衡压力转移至 ASIC 侧。
*   **硬件要求:** 需要芯片侧具备极高性能的 **112G/224G SerDes**（如 Synopsys DesignWare PHY），支持强大的 CTLE 和 DFE 功能以补偿信道损耗。
