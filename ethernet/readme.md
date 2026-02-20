## This directory is used for summary ethernet tech, including 802.3 and serdes.
| 特性维度 | **USXGMII (类 MII 接口)** | **100GAUI-1 (PMA 接口)** | **100GBASE-KR1 (PMD 接口)** |
| :--- | :--- | :--- | :--- |
| **逻辑层级位置** | **MAC/RS 层 ↔ PCS 层** | **PMA 层 ↔ PMA 层** | **PMD 层 ↔ 物理介质 (MDI)** |
| **协议栈切分本质** | 逻辑链路层与物理层的交界点 | 物理层内部的可选扩展/中继点 | 物理层与物理世界的最终接触点 |
| **传输承载内容** | 原始数据符号 + 控制字符 (Control Characters) | 已完成编码/FEC加码的串行比特流 | 经过 PAM4 调制的物理电平信号 |
| **信道协商能力** | 无 (通常为静态配置) | 无 (仅执行基本的电气补偿) | **有 (强制执行链路训练 Link Training)** |
| **信道损耗预算** | 极低 (Ultra-short reach, < 5dB) | 中等 (VSR: ~16dB / MR: ~20dB) | 高 (Long reach, ~28.5dB+) |
| **时钟同步方式** | 显式或嵌入式时钟同步 | 嵌入式时钟 (CDR 恢复) | 嵌入式时钟 + 严格的抖动/频率容限 |
| **核心参考标准** | 借鉴 Cl 46 / Cisco 规范 | **Annex 120F / 120G** | **Clause 163** |
| **典型物理形态** | 芯片内走线 / 同板极短连接 | SoC 到 Retimer / SoC 到光模块 | 跨背板走线 / SoC 直连背板插槽 |
| **SoC 研发重点** | 数据接口的对齐与控制流握手 | 信号眼图质量 (VEC/VEO) 与插损匹配 | 复杂的均衡算法 (FFE/DFE/DSP) 与 LT 状态机 |
