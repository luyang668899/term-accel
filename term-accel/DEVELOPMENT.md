# term-accel 开发文档

## 1. 项目概述

**term-accel** 是一个 Mac 终端代理一键管理工具，用于简化各种开发工具（如 git/pip/npm/brew）的代理配置管理。

### 1.1 核心功能
- 一键开启/关闭终端代理
- 支持配置自定义代理地址
- 自动为常用开发工具配置代理
- 查看各工具代理状态
- 测试 GitHub 连通性验证代理效果

### 1.2 技术栈
- Python 3.6+
- Click（命令行框架）
- Requests（HTTP 请求库）

## 2. 项目结构

```
term-accel/
├── install.sh              # 安装脚本
├── requirements.txt        # 依赖声明
├── setup.py               # 项目配置与安装入口
├── term_accel/            # 主源码目录
│   ├── __init__.py        # 包初始化文件
│   ├── cli.py             # 命令行接口
│   ├── config.py          # 配置管理
│   └── proxy.py           # 代理管理核心功能
└── term_accel.egg-info/   # 包信息目录（安装后生成）
```

## 3. 核心模块详解

### 3.1 cli.py - 命令行接口

该模块使用 Click 框架实现命令行接口，提供以下命令：

- `set-proxy`: 设置代理地址
- `on`: 开启代理
- `off`: 关闭代理
- `status`: 查看代理状态
- `test`: 测试 GitHub 连通性

**关键函数**：
- `cli()`: 命令组入口
- `set_proxy_command()`: 设置代理地址命令
- `on()`: 开启代理命令
- `off()`: 关闭代理命令
- `status()`: 查看状态命令
- `test()`: 测试连通性命令

### 3.2 proxy.py - 代理管理核心

该模块实现了代理的核心管理功能，包括设置代理、清除代理和检查状态。

**关键函数**：
- `run_cmd(cmd)`: 执行终端命令并返回结果
- `set_proxy()`: 为各工具设置代理
- `unset_proxy()`: 清除各工具代理
- `check_status()`: 查看各工具代理状态

### 3.3 config.py - 配置管理

该模块负责代理配置的持久化存储和读取。

**关键函数**：
- `init_config()`: 初始化配置目录和文件
- `save_proxy_url(proxy_url)`: 保存代理地址
- `get_proxy_url()`: 读取代理地址（提供默认值）

**配置文件**：`~/.term-accel/config.json`

## 4. 开发环境搭建

### 4.1 依赖安装

```bash
# 安装依赖
pip install -r requirements.txt

# 开发模式安装（便于修改和测试）
pip install -e .
```

### 4.2 测试运行

```bash
# 查看帮助信息
term-accel --help

# 测试命令
term-accel status
```

## 5. 开发流程

### 5.1 代码修改

1. 确保在开发模式下安装项目
2. 修改相应模块的代码
3. 直接测试修改后的命令

### 5.2 添加新功能

1. 在 `cli.py` 中添加新的命令函数
2. 如果需要，在 `proxy.py` 中实现核心功能
3. 如果需要持久化配置，在 `config.py` 中添加相关函数
4. 更新 `setup.py` 中的依赖（如果有新依赖）
5. 编写测试并验证功能

### 5.3 代码风格

- 遵循 PEP 8 编码规范
- 使用清晰的函数和变量命名
- 添加必要的注释说明

## 6. 测试指南

### 6.1 功能测试

```bash
# 测试设置代理
term-accel set-proxy socks5://127.0.0.1:1080

# 测试开启代理
term-accel on

# 测试查看状态
term-accel status

# 测试连通性
term-accel test

# 测试关闭代理
term-accel off
```

### 6.2 边界测试

- 测试无效代理地址
- 测试网络不可用时的情况
- 测试配置文件损坏时的恢复机制

## 7. 发布流程

1. 更新 `setup.py` 中的版本号
2. 创建发布包：
   ```bash
   python setup.py sdist bdist_wheel
   ```
3. 安装到本地验证：
   ```bash
   pip install dist/term_accel-<version>.tar.gz
   ```
4. 发布到 PyPI（需要账号）：
   ```bash
   twine upload dist/*
   ```

## 8. 扩展建议

### 8.1 功能扩展
- 支持更多开发工具的代理配置
- 添加代理自动切换功能
- 支持多个代理配置的管理和切换

### 8.2 性能优化
- 减少命令执行时间
- 优化配置文件读写操作

### 8.3 兼容性改进
- 增加对 Linux 系统的支持
- 支持更多终端环境（bash、fish 等）

## 9. 常见问题

### 9.1 权限问题
如果遇到权限错误，尝试使用 `sudo` 命令或检查文件权限。

### 9.2 配置文件问题
如果配置文件损坏，可以删除 `~/.term-accel/config.json` 后重新创建。

### 9.3 工具支持问题
确保目标工具（如 git、npm）已正确安装在系统中。