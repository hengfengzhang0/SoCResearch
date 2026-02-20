# UALink 数据封装与编码全流程 (Data Packing Flow)

本文档描述了 UALink 协议从事务层 (TL) 到物理层 (PMA) 的数据封装、分层开销注入及编码转换过程。

## 1. UALink 数据流逻辑架构图

```mermaid
graph TD
    subgraph TL_Layer ["1. 事务层 (Transaction Layer)"]
        A1["原始事务数据 (Payload)"] --> A2["注入: TL Header & FC Credit (流控)"]
        A2 --> A["生成: 64B TL Flit"]
    end

    subgraph DL_Layer ["2. 数据链路层 (Data Link Layer)"]
        A --> B{"DL Muxer (多路复用)"}
        B1["Message 注入: Basic / Control / UART"] -.-> B
        B --> C["构造: 640B DL Flit (包含 10个 TL Flit)"]
        C --> C_Fields["注入开销: Segment Header / Flit Header / CRC32 Footer"]
    end

    subgraph RS_Layer ["3. 协调子层 (Reconciliation Sublayer)"]
        C_Fields --> D["切分为 80 个 64b 原始载荷"]
        D --> D_Block["注入控制块 (Control Block)"]
        note_rs["同步头 (Sync Header): 01 (数据) / 10 (控制)<br/>插入 S (Start) / T (Terminate) 标记 Flit 边界"] --- D_Block
    end

    subgraph PCS_Layer ["4. 物理编码子层 (PCS)"]
        D_Block --> E["64B/66B -> 256B/257B 编码转换"]
        E --> F["汇聚 20 个 257b Block (总计 5140 bits)"]
    end

    subgraph FEC_PMA_Layer ["5. 纠错与物理媒介层 (FEC/PMA)"]
        F --> G["RS-FEC (544, 514) 符号化 (10-bit Symbol)"]
        G --> H["生成 30 个校验符号 (Parity Symbols)"]
        H --> I{"Lane Distributor (物理通道分发)"}
        I --> J["注入 AM (Alignment Markers, 对齐标记)"]
        J --> K["Gray Coding & PAM4 调制输出"]
    end
