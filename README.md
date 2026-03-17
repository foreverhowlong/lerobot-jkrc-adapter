# 🤖 LeRobot JAKA Bridge

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LeRobot](https://img.shields.io/badge/LeRobot-HuggingFace-yellow.svg)](https://github.com/huggingface/lerobot)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)]()

本项目提供了一个轻量级的 Python 适配器，用于将 [Hugging Face LeRobot](https://github.com/huggingface/lerobot) 框架与 **JAKA (节卡)** 协作机械臂无缝对接。

通过封装JAKA官方的 `jkrc` SDK，本项目能将机械臂的底层数据转化为 LeRobot 支持的 PyTorch Tensor 格式，让开发者可以快速在 Windows 环境下开展基于 JAKA 机械臂的模仿学习 与强化学习研究。


##  声明 

本项目**不包含** JAKA 官方的闭源 SDK 文件。为了正常运行本项目，您必须：
1. 拥有 JAKA 机械臂或运行 CoboΠ 仿真软件。
2. 自行获取 JAKA 提供的 `jkrc.pyd`（Python 动态库）及相关的 `.dll` 驱动文件。

##  安装指南

### 1. 环境准备
推荐使用 [uv](https://astral.sh/uv) 来管理虚拟环境，以获得最快的安装体验。

```bash
# 创建虚拟环境 (请确保 Python 版本与您的 jkrc.pyd 要求的版本一致)
uv venv --python 3.10
# 激活环境
.venv\Scripts\activate
# 安装依赖
uv pip install torch numpy