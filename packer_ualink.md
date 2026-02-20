graph TD
    subgraph TL_Layer [事务层 - TL]
        A1[原始事务数据] --> A2[+ TL Header & FC Credit]
        A2 --> A[64B TL Flit]
    end

    subgraph DL_Layer [数据链路层 - DL]
        A --> B{DL Muxer}
        B1[Message: Basic/Control/UART] -.-> B
        B --> C[640B DL Flit 构造]
        C --> C_Fields[注入: Segment Header / Flit Header / CRC32 Footer]
        note_dl[CRC32 负责 640B 整体校验] --- C_Fields
    end

    subgraph RS_Layer [协调子层 - RS]
        C_Fields --> D[切分为 80x64b 载荷]
        D --> D_Block[注入: Control Block / Sync Header 10/01]
        note_rs[插入 S/T 标记 Flit 边界] -.-> D_Block
    end

    subgraph PCS_Layer [物理编码子层 - PCS]
        D_Block --> E[64B/66B to 256B/257B 转换]
        E --> F[257b * 20 Block 汇聚]
    end

    subgraph FEC_PMA_Layer [纠错与物理层]
        F --> G[RS-FEC 544, 514 计算]
        G --> H[+ 30 Parity Symbols]
        H --> I{Lane 分发}
        I --> J[注入: AM Alignment Markers]
        J --> K[Gray Code / PAM4]
    end
