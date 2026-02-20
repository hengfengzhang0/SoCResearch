| 分层 (Layer) | 核心功能 | 100G 参考条款 | 200G/400G 参考条款 | UEC/UALink 的变更逻辑 |
| :--- | :--- | :--- | :--- | :--- |
| **LLC / 网络层** | 逻辑链路控制 / IP 路由 | Clause 2 | Clause 2 | **UEC 核心区**：引入 UET 传输协议，重写拥塞控制逻辑 |
| **MAC (Media Access)** | 帧起始/结束、校验 (CRC) | Clause 4 | Clause 4 | **UALink 核心区**：跳过传统 MAC，改用内存映射 (Load/Store) 语义 |
| **RS (Reconciliation)** | 接口映射 (MII 适配) | Clause 81 | Clause 117 | **关键借用点**：借用电平特性，但修改控制字符定义 |