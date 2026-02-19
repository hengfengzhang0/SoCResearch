# IEEE 802.3 以太网协议全维度技术参数全景表 (含 FEC & 波特率)


| 速率层级 | IEEE 协议标准 | 信号调制 | 单通道波特率 | 通道数 | 物理连接器 | FEC 纠错类型 | 外部PHY需求 | Synopsys IP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **10/100M** | 802.3i/u/bw | Manchester | 10/31.25 MBd | 1 | RJ45/车载 | **无 (No FEC)** | 必选外部PHY | [支持](https://www.synopsys.com) |
| **1G** | 802.3ab/z/bp | PAM-5/NRZ | 125 MBd | 4/1 | RJ45/SFP | **无 (No FEC)** | 必选外部PHY | [支持](https://www.synopsys.com) |
| **10G** | 802.3ae/an/ch | NRZ/PAM-16 | 10.31/0.8 GBd | 1/4 | RJ45/SFP+ | **Base-R FEC** (可选) | RJ45需PHY | [支持](https://www.synopsys.com) |
| **25/40G** | 802.3by/ba | NRZ | 25.78/10.31 GBd | 1/4 | SFP28/QSFP+ | **Firecode / RS-FEC** | SerDes直连 | [支持](https://www.synopsys.com) |
| **100G** | 802.3ba/bm/ck | NRZ/PAM-4 | 25.7/53.1 GBd | 4/2/1 | QSFP28/DD | **RS-FEC (528/544)** | 支持 LPO | [支持](https://www.synopsys.com) |
| **400G** | 802.3bs/ck | PAM-4 | 26.5/53.1 GBd | 8/4 | QSFP-DD/OSFP | **KP4 RS-FEC (544)** | 依赖 LPO 1.0 | [支持](https://www.synopsys.com) |
| **800G** | 802.3df | PAM-4 | 53.1/106.2 GBd | 8/4 | QSFP-DD/OSFP | **Segmented FEC** | 依赖 LPO 2.0 | [支持](https://www.synopsys.com) |
| **1.6T** | 802.3dj (Draft) | PAM-4 | 106.2/212.4 GBd | 16/8 | OSFP-XD | **Concatenated FEC** | 224G SerDes | [支持](https://www.synopsys.com) |

---

### 📘 核心技术深度补充

#### 1. FEC (前向纠错) 的关键作用与延迟
*   **RS-FEC (Reed-Solomon):** 是 100G/400G 的标配。**RS(544, 514)**（也称 KP4 FEC）能够修复损坏的符号，但会引入约 **100ns - 200ns** 的处理延迟。
*   **Segmented/Concatenated FEC:** 在 800G 和 1.6T 中，为了应对更差的信号质量，采用了级联纠错，这要求 [Synopsys 控制器 IP](https://www.synopsys.com) 具备更强大的计算逻辑。

#### 2. LPO (线性直驱) 方案对硬件的影响
*   在 **LPO** 方案中，光模块内没有 DSP，无法进行重定时（Retiming）。
*   **挑战:** 所有的信号补偿全靠 ASIC 侧的 [Synopsys 112G/224G SerDes](https://www.synopsys.com)。如果 SerDes 性能不足，FEC 将无法纠正过高的原始误码率 (Pre-FEC BER)，导致链路失效。

#### 3. 车载以太网 (Automotive) 特点
*   **协议:** 802.3cg (10M), 802.3bw (100M), 802.3bp (1G), 802.3ch (2.5/5/10G)。
*   **硬件:** 必须使用专用的车载 PHY（外部）。Synopsys 提供针对车载环境优化的 [Automotive Ethernet MAC IP](https://www.synopsys.com)，重点支持 **TSN (时间敏感网络)** 协议族。

#### 4. 波特率 (Baud Rate) 计算逻辑
*   **PAM-4:** 112Gbps 信号的有效负载加上 FEC 开销后，实际线速率约为 106.25 GBd。
*   **NRZ:** 波特率与比特率基本一致。
