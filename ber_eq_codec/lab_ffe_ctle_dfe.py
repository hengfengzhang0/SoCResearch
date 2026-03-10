#this is for study only.
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ==========================================
# 0. 基础参数设置 (SoC 工程师的 "Knobs")
# ==========================================
NUM_BITS = 2000       # 仿真的总比特数
SPS = 16              # Samples Per Symbol (每个UI采多少个点，用于画平滑的模拟波形)
UI = 1.0              # Unit Interval (一个比特的时间长度)

# ==========================================
# 辅助函数：画眼图 (Eye Diagram)
# ==========================================
def plot_eye(ax, sig, sps, title, color='blue'):
    # 丢弃开头和结尾的不稳定数据，每次截取 2 个 UI 的长度叠加
    eye_width = 2 * sps
    start_idx = sps * 10
    end_idx = len(sig) - sps * 10
    
    for i in range(start_idx, end_idx, sps):
        segment = sig[i : i + eye_width]
        if len(segment) == eye_width:
            # 时间轴归一化为 UI
            time_axis = np.linspace(-0.5, 1.5, eye_width)
            ax.plot(time_axis, segment, color=color, alpha=0.05) # alpha调低产生余辉效果
            
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Time (UI)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, linestyle='--')
    ax.set_ylim(-1.5, 1.5)

# ==========================================
# 1. 生成原始数据 (Tx 端的 0101 序列)
# ==========================================
np.random.seed(42) # 固定随机种子，方便对比
bits = np.random.randint(0, 2, NUM_BITS)
symbols = 2 * bits - 1 # 将 0/1 映射为 -1V / +1V (NRZ 信号)

# ==========================================
# 2. 模块二实验：FFE (Tx 预加重)
# ==========================================
# FFE Taps: [Pre-cursor, Main-cursor, Post-cursor]
# 尝试修改这里！比如改成 [0, 1.0, 0] 就是关闭 FFE
ffe_taps = [-0.15, 0.7, -0.15] 

# 在符号率上做卷积 (FIR 滤波)
tx_symbols_ffe = np.convolve(symbols, ffe_taps, mode='same')

# 将离散的符号过采样成连续的模拟波形 (Zero-Order Hold)
tx_waveform_ideal = np.repeat(symbols, SPS)
tx_waveform_ffe = np.repeat(tx_symbols_ffe, SPS)

# ==========================================
# 3. 模块一实验：信道 (Channel ISI)
# ==========================================
# 使用一个低通滤波器模拟 PCB 走线的插入损耗
# 尝试修改 cutoff！值越小，损耗越大，眼图闭合越严重
cutoff_freq = 0.12  # 归一化截止频率 (模拟高损耗信道)
b_chan, a_chan = signal.butter(1, cutoff_freq, btype='low')

# 信号经过信道 (泥潭)
rx_waveform_no_eq = signal.lfilter(b_chan, a_chan, tx_waveform_ideal) # 没开FFE的信号过信道
rx_waveform_with_ffe = signal.lfilter(b_chan, a_chan, tx_waveform_ffe) # 开了FFE的信号过信道

# ==========================================
# 4. 模块三实验：CTLE (Rx 连续时间线性均衡)
# ==========================================
# 使用一个简单的高通滤波器来模拟 CTLE 的高频提升 (Peaking)
# 尝试修改 peaking_gain！
peaking_gain = 0.6
b_ctle = [1.0, -peaking_gain] # 简单的一阶高通 FIR 近似
a_ctle = [1.0]

# FFE 后的信号再经过 CTLE
rx_waveform_ffe_ctle = signal.lfilter(b_ctle, a_ctle, rx_waveform_with_ffe)

# ==========================================
# 5. 模块四实验：DFE (Rx 判决反馈均衡)
# ==========================================
# DFE 是非线性的，必须逐个 bit 判决并反馈
dfe_tap_1 = 0.3 # 1-tap DFE 的权重 (消除后一个 bit 的拖尾)
rx_waveform_dfe = np.copy(rx_waveform_ffe_ctle)

# 模拟时钟恢复 (CDR) 找到最佳采样点 (这里简化为 UI 的正中间)
sample_offset = SPS // 2 

for i in range(1, NUM_BITS - 1):
    # 1. 在当前 UI 的中心进行采样
    sample_idx = i * SPS + sample_offset
    sampled_voltage = rx_waveform_dfe[sample_idx]
    
    # 2. 判决 (Slicer): 大于0判为1，小于0判为-1
    decision = 1.0 if sampled_voltage > 0 else -1.0
    
    # 3. DFE 反馈：从下一个 UI 的波形中减去当前判决造成的拖尾 (ISI)
    # 在实际电路中，这个减法是在下一个 bit 的采样瞬间完成的
    next_start = (i + 1) * SPS
    next_end = (i + 2) * SPS
    rx_waveform_dfe[next_start:next_end] -= decision * dfe_tap_1

# ==========================================
# 6. 绘图展示 (见证奇迹的时刻)
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
plt.subplots_adjust(hspace=0.3)

# 图1：完全没有均衡的接收信号 (眼图完全闭合)
plot_eye(axes[0, 0], rx_waveform_no_eq, SPS, "1. Rx Signal (No EQ) - Severe ISI", 'red')

# 图2：只开启 Tx FFE (眼图微微张开)
plot_eye(axes[0, 1], rx_waveform_with_ffe, SPS, f"2. Rx Signal (Tx FFE Only)\nTaps: {ffe_taps}", 'orange')

# 图3：Tx FFE + Rx CTLE (眼图进一步张开，但线条变粗/抖动增加)
plot_eye(axes[1, 0], rx_waveform_ffe_ctle, SPS, "3. Rx Signal (FFE + CTLE)", 'green')

# 图4：Tx FFE + Rx CTLE + Rx DFE (终极杀器，眼图清晰)
plot_eye(axes[1, 1], rx_waveform_dfe, SPS, f"4. Rx Signal (FFE + CTLE + 1-Tap DFE)\nDFE Tap: {dfe_tap_1}", 'blue')

plt.show()
