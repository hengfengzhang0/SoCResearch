| 领域分类 | 协议名称 | 属性 (开源/私有) | 最新版本 (2025/2026) | 核心速率 / 聚合带宽 | 物理距离 / Reach | 核心机制与优势 | 典型应用场景 | 主导者及生态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **算力一致性<br>(Scale-Up)** | **NVLink** | 私有 | v5.0 | 224G PAM4 / 聚合单向 900 GB/s | VSR / MR / 铜缆 | 内存语义硬连线，极低延迟 | N卡多 GPU 显存共享与互联 | NVIDIA |
| | **Infinity Fabric**| 私有 | 4.0 | 随 PCIe PHY / 宽链路聚合 | XSR / MR | 剥离 PCIe 冗余的定制化路由 | AMD 内 CPU/GPU 及 Die 间互联 | AMD |
| | **HCCS** | 私有 | (匹配 910C) | 56G/112G / 聚合 392+ GB/s | VSR / MR | P2P 拓扑无阻塞数据交换 | 昇腾多卡 P2P 互联 | 华为 (Huawei) |
| | **UPI** | 私有 | 3.0 | 24 GT/s+ / x20 聚合链路 | MR (插槽间) | 优化的目录与路由机制 | 多路 CPU 缓存一致 | Intel |
| | **UALink** | 联盟公开 | 1.0 | 224 Gbps+ / 交换机拓扑 | VSR / MR | 对抗 NVLink 的开源扩展网络 | 跨厂商 AI 加速器 Scale-up | UALink Consortium |
| | **SUE**<br>*(Scale-Up Ethernet)*| OCP 公开 | 1.0 | 单实例 800G (多网平面) | VSR / MR | 在以太网上实现 Load/Store | Pod 内 XPU 高速直连 | Broadcom / OCP |
| | **Google ICI** | 私有 | Ironwood (v7) | 单片 9.6 Tb/s | 光电混合 / 3D Torus | 光路交换 (OCS) 动态重构 | TPU 阵列核心底层互联网络 | Google |
| **集群与网联<br>(Scale-Out)**| **UEC**<br>*(Ultra Ethernet)*| 联盟公开 | 1.0 | 兼容 800G/1.6T 物理层 | LR / ZR | 多路径 Packet Spraying，乱序传输 | AI/HPC 高性能集群 | UEC |
| | **InfiniBand** | 公开(事实垄断) | GDR (1.6T) | 200G/400G 端口 | LR / ZR | 极高确定性，纯硬件 RDMA | 顶级 AI 训练集群后端 | IBTA / NVIDIA |
| | **Ethernet** | 公开 | 1.6T / 800G | 112G/224G (PAM4) | LR / ZR | 绝对通用，生态成本最低 | 数据中心前端、传统云基建 | IEEE 802.3 |
| **异构封装<br>(Chiplet)**| **UCIe** | 公开 | 2.0 | 32 ~ 64 GT/s | USR / XSR (< 2mm) | 极高带宽密度 (<0.3 pJ/bit) | 标准化 D2D 异构集成 | UCIe Consortium |
| | **BoW** | 公开 | BoW 2.0 | 16 Gbps+ (NRZ) | USR / XSR (< 2mm) | 容忍普通有机基板，极简 PHY | 低成本 Chiplet 互联 | OCP (ODSA) |
| **主存与显存<br>(Memory)** | **HBM** | 公开 | HBM4 | 10 Gbps (1024/2048-bit) | USR (< 5mm) | 3D TSV 解决内存墙 | 顶级 GPU / NPU 显存 | JEDEC |
| | **GDDR** | 公开 | GDDR7 | 36 Gbps (PAM3) | VSR (5~10cm) | 单端信号的极致压榨 | 独立显卡、端侧 AI | JEDEC |
| | **DDR / LPDDR**| 公开 | DDR6 / LPDDR6 | 17.6 Gbps / 14.4 Gbps | VSR / XSR | 容量、成本、功耗的黄金三角 | PC、座舱、边缘系统主存 | JEDEC |
| **系统与板级<br>(System)** | **PCIe / CXL** | 公开 | 7.0 / 3.1 | 128 GT/s (PAM4) | MR (10~25cm) | 即插即用，CXL 支持内存池化 | 算力卡、SSD、扩展缓存 | PCI-SIG / CXL |
| **存储外设<br>(Storage/IO)**| **UFS** | 公开 | 5.0 | 10.8 GB/s (M-PHY 6.0) | XSR (< 5cm) | 原生隔离电源轨，内联哈希 | 车载存储 (IVI)、旗舰 ROM | JEDEC |
| | **USB / DP** | 公开 | USB4 Gen4 / DP 2.1a| 80 Gbps / 80 Gbps (PAM3) | VSR (< 0.8m) | 统一 Type-C 物理层，隧道协议 | 消费电子、智能座舱外接屏 | USB-IF / VESA |
| **长距视觉与传感** | **MIPI A-PHY** | 公开 | 2.0 | 下行 32 Gbps / 上行 1.6G | LR (高达 15m) | 极低误码率 (1E-19)，无需桥接 | 车载传感直连、高分屏输出 | MIPI Alliance |
| | **MIPI D/C-PHY**| 公开 | D3.6 / C3.1 | 11Gbps / 6.4Gsps | XSR / VSR (<15cm) | 极低功耗，面积友好 | 手机摄像头、近距屏幕 | MIPI Alliance |
| | **GMSL / FPD-Link**| 私有 | GMSL 3 / FPD-Link IV| 12 Gbps / 13.5 Gbps | LR (15m) | 生态极其成熟，即插即用 | 车规级长距视频解串器 (主流)| ADI / TI |
