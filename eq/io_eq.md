# 高速链路均衡技术 (EQ) 在 IO Bus 与 Memory Bus 中的应用全景图


---

## 一、 IO Bus (PCIe, Ethernet) —— “重型装甲”，对抗极限损耗

IO 接口的特点是**走线长、环境恶劣**（跨越主板、连接器、线缆甚至背板），插入损耗动辄 25dB~35dB。因此，IO PHY 通常是 EQ 技术的“集大成者”。

### 1. PCIe (Peripheral Component Interconnect Express)
PCIe PHY 通常采用**混合信号（Mixed-Signal）架构**，追求在可控功耗下实现极低延迟。

*   **PCIe Gen3 (8 GT/s, NRZ):**
    *   **EQ 方案:** Tx FFE (3-tap) + Rx CTLE。
    *   **选型备注:** 此时损耗尚可，基本不需要 DFE。
*   **PCIe Gen4 (16 GT/s, NRZ):**
    *   **EQ 方案:** Tx FFE (3-tap) + Rx CTLE + **Rx DFE (通常 1~2 taps)**。
    *   **选型备注:** 16G 速率下，FR4 板材的损耗急剧增加，DFE 成为标配。
*   **PCIe Gen5 (32 GT/s, NRZ):**
    *   **EQ 方案:** Tx FFE (3-tap) + 强力 Rx CTLE + **Rx DFE (通常 3~4+ taps)**。
    *   **选型备注:** 损耗预算高达 36dB。IP 选型时要重点看 PHY 是否支持自适应均衡（Adaptive EQ），即芯片上电后自己跑算法寻找最佳的 FFE/DFE 系数。
*   **PCIe Gen6 (64 GT/s, PAM4):**
    *   **EQ 方案:** Tx FFE + Rx CTLE + **高阶 DFE (可能高达 16 taps)** + **FEC (前向纠错)**。
    *   **选型备注:** 引入 PAM4（4电平）后，眼图高度变成原来的 1/3，对噪声极度敏感。纯靠物理层 EQ 已经撑不住了，必须引入数字层的 FEC 来纠错。**选型时要看 PHY 和 Controller 之间的 FEC 延迟是否满足系统要求。**

### 2. Ethernet (以太网 10G ~ 112G/224G)
以太网的特点是**距离跨度极大**（从几厘米的芯片到芯片 VSR，到几米的背板 LR）。高速以太网 PHY（50G 以上）已经发生了架构突变。

*   **10G / 25G (NRZ):**
    *   **EQ 方案:** 类似 PCIe Gen3/4，采用模拟架构的 FFE + CTLE + DFE。
*   **50G / 112G / 224G (PAM4):**
    *   **EQ 方案:** **DSP-based PHY (数字信号处理架构)**。
    *   **选型备注 (极其重要):** 在 112G 速率下，传统的模拟 DFE 根本来不及在 8 皮秒内完成反馈。因此，高端 Ethernet PHY 内部包含高速 ADC（模数转换器），将信号全部数字化，然后在 **DSP 里面用纯数字逻辑做 FFE 和 DFE（甚至 MLSE 最大似然序列估计）**。
    *   **代价:** DSP 架构功耗巨大（每通道可能 >1W），且延迟较高（几十纳秒级别）。

---

## 二、 Memory Bus (DDR, LPDDR, HBM) —— “轻装上阵”，死磕功耗与延迟

Memory 接口的特点是**走线相对较短，但总线极宽（几十到上百根线），且对延迟（Latency）和功耗（Power）极度敏感。** CPU 等数据是不能忍受内存有几十纳秒的 EQ 延迟的。

### 1. DDR (Standard DDR for DIMM / PC / Server)
DDR 的走线要经过 CPU 封装 -> 主板 -> DIMM 插槽 -> 内存条 PCB -> DRAM 颗粒，存在大量的阻抗不匹配（反射严重）。

*   **DDR4 (最高 3200 MT/s):**
    *   **EQ 方案:** Tx 简单的去加重 (De-emphasis) + Rx 简单的 CTLE。
    *   **选型备注:** 速率较低，主要靠控制走线长度和阻抗匹配来解决问题。
*   **DDR5 (最高 6400~8400 MT/s):**
    *   **EQ 方案:** Tx FFE + Rx CTLE + **Rx DFE (标准规定 4-tap)**。
    *   **选型备注 (历史性转折):** DDR5 是内存史上**首次引入 DFE** 的标准。因为 6.4G 速率下，DIMM 插槽的反射造成的 ISI 太严重了。选型 DDR5 PHY 时，**必须严格评估 DFE 带来的 Read Latency 增加**，这直接影响 CPU 的 IPC（每时钟周期指令数）性能。

### 2. LPDDR (Low Power DDR for Mobile / Auto / Edge)
LPDDR 通常是直接焊在主板上（甚至和 SoC 封装在一起，如 PoP），走线很短，但对功耗要求变态级苛刻。

*   **LPDDR4/4X (最高 4266 MT/s):**
    *   **EQ 方案:** Tx FFE + Rx 极低功耗 CTLE。
*   **LPDDR5/5X (最高 8533~10667 MT/s):**
    *   **EQ 方案:** Tx FFE (多 tap) + Rx CTLE + **Rx DFE (通常 1~2 taps)**。
    *   **选型备注:** 相比 DDR5 的 4-tap，LPDDR5X 通常只用 1 到 2 个 tap 的 DFE，且设计得极其精简，一切为了省电。很多时候，如果走线足够好，系统会选择**关闭 DFE** 以节省功耗。

### 3. HBM (High Bandwidth Memory)
*   **HBM2E / HBM3 (每 pin 3.2G ~ 6.4G, 但有 1024 根数据线):**
    *   **EQ 方案:** **几乎没有复杂的 EQ (No DFE, 极弱的 CTLE/FFE)**。
    *   **选型备注:** HBM 是通过 2.5D 硅中介层（Silicon Interposer）连接的，走线只有几毫米，信道极其完美。因此 HBM PHY 的设计重点是高密度、低功耗和解决串扰（Crosstalk），而不是对抗插入损耗。

---

## 三、 SoC 工程师选型 Cheat Sheet (速查表)

| 接口类型 | 典型速率 | 调制方式 | Tx FFE | Rx CTLE | Rx DFE | 核心架构 | 选型最关注的 Trade-off |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PCIe Gen4** | 16 GT/s | NRZ | 3-tap | 标配 | 1~2 tap | 模拟/混合 | 面积 vs. 损耗预算 |
| **PCIe Gen5** | 32 GT/s | NRZ | 3-tap | 强力 | 3~4+ tap | 模拟/混合 | 自适应 EQ 算法收敛时间 |
| **PCIe Gen6** | 64 GT/s | PAM4 | 多 tap | 标配 | 高阶 | 模拟/DSP | FEC 延迟 vs. 误码率 |
| **Eth 112G** | 112 Gbps | PAM4 | 数字 | 模拟 | 数字(高阶) | **DSP (ADC+DSP)** | 功耗极大，需评估散热 |
| **DDR4** | 3.2 GT/s | NRZ | 简单 | 简单 | **无** | 模拟 | 面积，引脚排列 |
| **DDR5** | 6.4+ GT/s | NRZ | 标配 | 标配 | **4-tap** | 模拟 | **DFE 带来的读取延迟** |
| **LPDDR5X** | 8.5+ GT/s | NRZ | 标配 | 标配 | 1~2 tap | 模拟 | 极低功耗，待机漏电 |
| **HBM3** | 6.4 GT/s | NRZ | 极弱 | 极弱 | **无** | 纯数字/简单模拟 | 面积密度，串扰控制 |

---
