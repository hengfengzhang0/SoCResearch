# UALink 数据封装与编码流程 (Data Packing Flow)

## 1. 物理层与链路层封装流程图

```mermaid
graph TD
    %% 事务层层级
    subgraph TL_Layer ["1. 事务层 (TL)"]
        A1["原始事务数据 (Payload)"] --> A2["注入: TL Header & FC Credit (流控)"]
        A2 --> A["生成: 64B TL Flit"]
    end

    %% 数据链路层层级
    subgraph DL_Layer ["2. 数据链路层 (DL)"]
        A --> B{"DL Muxer (多路复用)"}
        B1["Message 注入: Basic / Control / UART"] -.-> B
        B --> C["构造: 640B DL Flit (10x TL Flits)"]
        C --> C_Fields["注入: Segment Header / Flit Header / CRC32 Footer"]
    end

    %% 协调子层层级
    subgraph RS_Layer ["3. 协调子层 (RS)"]
        C_Fields --> D["切分为 80 个 64b 原始负载块"]
        D --> D_Block["注入控制块 (66b Control Block)"]
        note_rs["Sync Header: 01(数据)/10(控制)<br/>插入 S(Start)/T(Terminate) 标记边界"] --- D_Block
    end

    %% PCS层级
    subgraph PCS_Layer ["4. 物理编码子层 (PCS)"]
        D_Block --> E["64B/66B -> 256B/257B 编码转换"]
        E --> F["汇聚 20 个 257b Block (5140 bits)"]
    end

    %% FEC与物理媒介层
    subgraph FEC_PMA_Layer ["5. 纠错与物理媒介 (FEC/PMA)"]
        F --> G["RS-FEC (544, 514) 10-bit 符号化"]
        G --> H["生成 30 个校验符号 (300 bits)"]
        H --> I{"Lane 分发 (Distributor)"}
        I --> J["注入 AM (Alignment Markers)"]
        J --> K["Gray Coding & PAM4 调制输出"]
    end
