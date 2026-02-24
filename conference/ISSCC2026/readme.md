# ISSCC 2026 通信与连接专题：Wireline 与 Chiplet 主要进展

根据 **ISSCC 2026 预告议程（Advance Program）**，通信与连接（Connectivity）领域的 **Wireline（有线传输）** 和 **Chiplet（芯粒）** 技术取得了显著进展。

**核心趋势**：为了满足 AI 和 HPC（高性能计算）对算力的渴求，互连技术正朝着“超高带宽密度（Tb/s/mm²）”、“极低功耗（pJ/b）”以及“标准化（UCIe）”的方向飞速发展。

---

### 1. Die-to-Die (D2D) 与 Chiplet 接口：UCIe 走向成熟与高性能
**Session 8** 是这一领域的重头戏，展示了 Chiplet 互连技术的最新突破。

*   **极高带宽密度 (Bandwidth Density)**
    *   **TSMC (8.2)**：展示了一个 **3nm** 工艺的 UCIe-Like D2D 接口，实现了惊人的 **12.35Tb/s/mm²** 带宽密度（利用 Active LSI 封装），单通道速率 32Gb/s，能效为 0.36pJ/b。这是目前业界极高的密度指标。
    *   **Intel (8.1)**：展示了符合 **UCIe 标准** 的 D2D 链路，单通道 **48Gb/s**，带宽密度达到 **1.24Tb/s/mm²**，支持 30mm 的标准封装传输距离。

*   **极低功耗与能效 (Energy Efficiency)**
    *   **Microsoft (8.3)**：发布了 **3nm** 工艺的模块化 D2D 接口，单通道 24Gb/s，能效仅为 **0.23pJ/b**，并具有“零唤醒惩罚”（Zero Wake Penalty）的时钟门控技术，非常适合大规模 AI 集群的节能需求。
    *   **Seoul National Univ (8.8)**：展示了 **0.292pJ/b** 的 56Gb/s/wire 电容驱动双向收发器。

*   **单端信号 (Single-Ended) 的复兴**
    *   为了节省面积和引脚，**Peking Univ (8.4)** 和 **Southern Univ of Sci & Tech (8.9)** 分别展示了 **112Gb/s/wire** 和 **72Gb/s/pin** 的单端同时双向（SBD）收发器，证明了单端信号在短距 D2D 中的巨大潜力。

### 2. 超高速电收发器：迈向 224Gb/s 及以上
传统的 SerDes 技术继续挖掘铜缆传输的极限，PAM-4 仍是主流，但更高阶调制（PAM-8）和更高即速率开始出现。

*   **112Gb/s 成为标配，迈向低功耗**
    *   **Broadcom (8.6)**：展示了 **5nm** 工艺的 **112Gb/s PAM-4/NRZ** 收发器，功耗仅 **280mW**，专为低功耗 IO 设计。
    *   **CAS (8.5)**：展示了无参考时钟的 112Gb/s PAM-4 CDR，能效 0.76pJ/b。

*   **探索 200G+ 速率**
    *   **Tsinghua Univ (8.10)**：展示了一个 **180-to-240Gb/s** 的 PAM-4 发射机（TX），虽然使用的是 65nm 工艺（主要验证架构），但证明了模拟密集型架构在超高速率下的可行性。
    *   **National Taiwan Univ (8.11)**：展示了 **168Gb/s PAM-8** 发射机，探索更高阶调制以提升频谱效率。

### 3. 存储器接口 (Memory Interface)：LPDDR6 与 HBM
**Session 37** 聚焦于解决“内存墙”问题的接口技术。

*   **LPDDR6 首秀**
    *   **Samsung (37.3)**：发布了 **2nm** 全数字 **LPDDR6 PHY**，速率达到 **14.4Gb/s/pin**，采用了四分之一速率时钟架构。
    *   **SK hynix (15.7, 15.8)**：在 Session 15 中也展示了 14.4Gb/s/pin 的 LPDDR6 SDRAM。

*   **高密度单端互连**
    *   **Nanjing Univ (37.2)**：展示了用于短距内存接口的 **112Gb/s/pin PAM4 单端收发器**，实现了 **47.0Tb/s/mm** 的线性带宽密度（Linear Density），这对于下一代高带宽内存互连至关重要。

### 4. 光互连 (Optical Interconnects)：CPO 与 Coherent
虽然属于光通信，但在 ISSCC 中常被视为 Wireline 的延伸（Session 23），用于解决电互连的距离和损耗瓶颈。

*   **Broadcom (23.4)**：展示了 **6.4Tb/s** 的共封装光学（CPO）ASIC，采用 7nm 工艺，能效 4.2pJ/b，集成了直接驱动 TIA 和驱动器。
*   **Marvell (23.2)**：展示了 **5nm** 的 **800Gb/s** 收发器，针对 Coherent-Lite 应用，延迟小于 300ns。
*   **Nvidia (23.1)**：展示了 3D 堆叠的 DWDM 光链路，单波长 32Gb/s，单光纤容量 256Gb/s。

---

### 总结表：ISSCC 2026 Wireline & Chiplet 关键指标

| 类别 | 关键论文/机构 | 核心指标/技术 | 意义 |
| :--- | :--- | :--- | :--- |
| **Chiplet (D2D)** | **TSMC (8.2)** | **12.35 Tb/s/mm²**, 3nm | 刷新了 Chiplet 互连的带宽密度记录，支持大规模 AI 芯片拼接。 |
| **Chiplet (D2D)** | **Intel (8.1)** | **UCIe Compliant**, 48Gb/s/lane | 推动 UCIe 标准落地，实现不同厂商 Chiplet 的互联互通。 |
| **Chiplet (D2D)** | **Microsoft (8.3)** | **0.23 pJ/b**, 3nm | 极致能效，降低大规模集群的互连功耗。 |
| **High-Speed IO** | **Tsinghua (8.10)** | **240 Gb/s** PAM-4 TX | 探索下一代电接口速率极限（224G+）。 |
| **Memory IO** | **Samsung (37.3)** | **LPDDR6**, 14.4 Gb/s/pin, 2nm | 下一代移动端和边缘 AI 内存标准的首个物理层实现。 |
| **Optical IO** | **Broadcom (23.4)** | **6.4 Tb/s** CPO ASIC | 共封装光学（CPO）走向实用化，解决数据中心带宽瓶颈。 |
