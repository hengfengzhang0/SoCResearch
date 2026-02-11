# 高速互联与存储系统 (High-Speed Interconnect & Memory Systems)

> **维护周期**: 2026 年度
> **最后更新**: 2026-02-11

## 📅 Q1 & Q2 (Spring/Summer) - 核心技术与标准定义

| 时间 (2026) | 会议名称 | 主办方/类型 | 涉及厂商 (Key Players) | SoC 核心关注点 (Actionable Insights) | 地点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Feb 15-19** | **ISSCC** | IEEE (学术顶会) | Samsung, SK Hynix, Intel | **[PHY/Circuit]** LPDDR6/HBM4 首个硅验证数据；224G SerDes 架构；DRAM Cell 物理极限。 | San Francisco, CA |
| **Mar 11-12** | **SNUG Silicon Valley** | Synopsys (EDA/IP) | Synopsys | **[IP/Implementation]** DDR PHY PPA 优化数据；UCIe IP 集成避坑；3D-IC 物理设计流程。 | Santa Clara, CA |
| **Mar 16-19** | **NVIDIA GTC** | NVIDIA (AI/Chip) | NVIDIA, Micron, SK Hynix | **[Architecture]** HBM4 在 Blackwell/Rubin 架构中的系统集成；NVLink Switch 互联架构；RAS 可靠性设计。 | San Jose, CA |
| **Apr 15-16** | **CadenceLIVE** | Cadence (EDA/IP) | Cadence | **[Simulation/SI/PI]** LPDDR6/GDDR7 信号完整性仿真；DRAM Memory Controller 验证方法学。 | Santa Clara, CA |
| **May (TBD)** | **JEDEC Workshop** | JEDEC (标准组织) | Google, Meta, Memory Vendors | **[Standard]** **LPDDR6 Spec 最终草案**；DDR6 时序定义；CAMM2 模组标准更新。 | Santa Clara / Hybrid |
| **Jun (TBD)** | **ISCA / MICRO** | IEEE/ACM (体系结构) | Google, NVIDIA, Universities | **[Research]** 存内计算 (PIM) 架构；Memory Pooling 策略；解决 Memory Wall 的新型架构探索。 | TBD |
| **Jul/Aug** | **OCP China Day** | OCP Foundation | Alibaba, Tencent, Inspur | **[Ecosystem]** 国内大厂对 AI 芯片互联 (CXL/UCIe) 的定制化需求；国产 Chiplet 接口标准落地。 | Beijing, CN |

## 📅 Q3 & Q4 (Autumn/Winter) - 生态落地与未来路线图

| 时间 (2026) | 会议名称 | 主办方/类型 | 涉及厂商 (Key Players) | SoC 核心关注点 (Actionable Insights) | 地点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Aug 4-6** | **FMS** (Future of Memory) | 行业联盟 | **Micron**, Samsung, SK Hynix | **[Ecosystem]** **HBM4E 封装展示**；CXL 3.0 Switch 芯片量产进度；车规级 LPDDR5X/GDDR7。 | Santa Clara, CA |
| **Aug (TBD)** | **Hot Chips 2026** | IEEE (工业界) | Tesla, AMD, Intel | **[Competitor Analysis]** 竞品 SoC (如 Thor, FSD) 的 Memory Subsystem 架构拆解；Chiplet 互联实战。 | Stanford Univ |
| **Sep 15-17** | **AI Infra Summit** | Kisaco (垂直行业) | Hyperscalers (Meta/Msft) | **[System]** **(原 MemCon)** 聚焦解决 Memory Wall 的系统级方案；AI 训练集群中的 HBM/CXL 部署痛点。 | Santa Clara, CA |
| **Sep/Oct** | **TSMC OIP Forum** | TSMC (Foundry) | TSMC, Synopsys | **[Packaging]** CoWoS 产能与设计规则；3D Fabric 对 HBM Base Die 的工艺要求；HBM4 热管理。 | Santa Clara, CA |
| **Oct 13-15** | **OCP Global Summit** | OCP Foundation | Meta, Microsoft, Intel, AMD | **[System Architecture]** **ODSA/Chiplet**: UCIe 物理层与互操作性演示；<br>**CXL**: 内存池化 (Memory Pooling) 真实硬件；<br>**OAM**: 大算力 HBM 芯片模组标准。 | San Jose, CA |
| **Oct (TBD)** | **Samsung Tech Day** | Samsung (原厂) | Samsung | **[Roadmap]** 必须关注的 **DRAM Roadmap (1c, 0a nm)**；LPCAMM2 在移动端的应用；下一代 GDDR。 | San Jose, CA |
| **Oct/Nov** | **Micron Insight** | Micron (原厂) | Micron | **[Roadmap]** 美光在 HBM 能效比上的优化方案；GDDR7 车规认证进度。 | TBD |

---

### 📝 参会策略建议 (For SoC Team)

1.  **物理层与 IP (PHY/IP)**: 必须关注 **ISSCC** (电路创新) 和 **SNUG** (工程落地)。重点看 224G SerDes 和 LPDDR6 PHY 的 PPA 数据。
2.  **系统架构 (System Arch)**: 必须关注 **OCP Global Summit** 和 **Hot Chips**。OCP 决定了 Chiplet (UCIe) 和 CXL 怎么连，Hot Chips 展示了别人怎么连。
3.  **存储颗粒 (Memory Device)**: **Samsung Tech Day** 和 **FMS** 是获取下一代颗粒 Spec (HBM4, LPDDR6) 最直接的渠道。
4.  **国内生态**: **OCP China Day** 是了解国内互联网大厂（潜在客户）对互联标准需求的最佳窗口。
