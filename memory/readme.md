| 特性指标 | HBM4 | HBM3E | GDDR7 | LPDDR6 | DDR6 | LPW / LLW | ZAM-DRAM | HMC (Legacy) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **核心应用** | AI训练/推理 (Nvidia Rubin), HPC, 超算 | AI训练 (H100/H200/Blackwell), 数据中心 | 游戏显卡 (RTX 5090), 边缘AI推理, 汽车 | 旗舰手机, AI PC, 端侧大模型 | 服务器主存, 工作站, 高端PC | 端侧AI (On-Device AI), 高端移动设备 | 未来AI训练, 解决HBM散热瓶颈 | (已停产) 早期3D堆叠探索 |
| **接口/通道架构** | 2048-bit 宽接口 (单堆叠) | 1024-bit 接口 (单堆叠) | 4 x 8-bit 通道 (单芯片) | 4 x 24-bit 子通道 (96-bit 总线) | 4 x 24-bit 子通道 (96-bit) | Wide I/O (具体位宽未公开，强调多通道低频) | Z-Angle 对角互连 (专有接口) | 串行器/解串器 (SerDes) 链路 |
| **峰值带宽** | 1.6 TB/s - 2.0+ TB/s (每堆叠) | 1.18 - 1.2 TB/s (每堆叠) | 128 - 192 GB/s (每芯片 @ 32-48Gbps) | 28.5 - 38.4 GB/s (每通道 @ 10.7-14.4Gbps) | 140 GB/s (每模组 @ 17.6Gbps) | 128 GB/s (目标 &gt;200GB/s) | 目标高于HBM (具体未定) | 160 GB/s - 320 GB/s (当时数据) |
| **堆叠/容量** | 12-Hi / 16-Hi (48GB - 64GB) | 8-Hi / 12-Hi (24GB - 36GB) | 单芯片 (16Gb - 24Gb) | 封装级堆叠 (PoP) / LPCAMM2 (最高16GB+) / Discrete | 模组 (CAMM2/DIMM) (32GB - 256GB+) | 3D封装 (容量未定) | 超高密度堆叠 (目标单芯片512GB) | 4-Hi / 8-Hi (2GB - 8GB) |
| **关键创新** | 逻辑基础裸片 (Logic Base Die), 2048-bit 降频宽总线 | 速度提升至 9.6 Gbps+ | PAM3 信号调制 | 24-bit 子通道, 12-burst length, 带内ECC | 4x24架构, 彻底抛弃2x32, 针对高频优化 | 垂直引线键合 (VWB), 替代TSV | 对角线互连 (Diagonal), Via-in-One 结构 | 早期逻辑底座概念, 串行接口 |
| **工艺/封装** | 混合键合 (Hybrid Bonding) / 改进型MR-MUF | MR-MUF / TC-NCF (微凸块) | 标准BGA (无须CoWoS) | LPCAMM2 模组 / PoP / Discrete | CAMM2 连接器 (LGA触点) | VWB (Vertical Wire Bonding) | Z-Angle 3D 异构键合 (NGDB) | 3D TSV |
| **厂商** | SK Hynix, Samsung, Micron | SK Hynix, Samsung, Micron | Samsung, Micron, SK Hynix | Samsung, SK Hynix, Micron | Samsung, SK Hynix, Micron | Samsung (主导), SK Hynix (类似技术) | Intel, SoftBank (Saimemory) | (Micron, Samsung曾主导) |
| **上市时间** | 2026年 (量产/出样) | 2024-2025年 (主流) | 2025-2026年 (量产) | 2026年 (商用) | 2027年 (预计) | 2028年 (预计) | 2027原型 / 2030商用 | 2011-2018 (已淘汰) |
| **技术难点 (劣势)** | 混合键合良率低; 16层堆叠散热极难; 成本极高 | 功耗随频率线性增加; 带宽扩展遇瓶颈 | PCB信号完整性要求极高; 延迟略高于GDDR6 | 控制器逻辑复杂(非2次幂位宽); 成本高于LPDDR5X | 必须更换主板接口(CAMM2); 高频信号衰减严重 | 定制化程度高; 制造工艺(VWB)成熟度挑战 | 斜向光刻与对准极难; 产业链空白; 早期阶段 | 专有接口封闭; 功耗过高(SerDes); 成本昂贵 |
| **能效比 (pJ/bit)** | 极优 (宽总线+低频)<br>&lt; 3.5 (目标) | 优<br>~3.5 - 4.0 | 良 (PAM3比PAM4更节能, 但不如HBM)<br>4.5 | 优 (DVFS+低电压)<br>&lt; 3.0 | 良 (1.0V 电压)<br>&gt; 10 (系统级) | 极优 (~1.2 pJ/bit) | 理论极优 (目标比HBM低40-50%) | 差 (接口功耗高) |
| **工作电压** | ~1.1V | ~1.1V | 1.2V | 多轨 DVFSL | &lt; 1.0V | 未公开 | - | - |
| **相对成本** | 最高 | - | - | - | - | - | 初期极高 | - |
