#!/bin/bash

echo "=== Mac终端代理一键管理工具安装脚本 ==="

# 检查Python3是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误：未检测到Python3，请先安装Python3"
    exit 1
fi

# 检查pip3是否安装
if ! command -v pip3 &> /dev/null; then
    echo "错误：未检测到pip3，请先安装pip3"
    exit 1
fi

echo "正在安装依赖..."
pip3 install -r requirements.txt --break-system-packages

if [ $? -ne 0 ]; then
    echo "依赖安装失败，请检查网络连接或权限"
    exit 1
fi

echo "正在安装工具..."
pip3 install -e . --break-system-packages

if [ $? -ne 0 ]; then
    echo "工具安装失败，请检查权限"
    exit 1
fi

echo "正在配置默认代理..."
# 设置默认代理地址（常见的本地代理端口）
term-accel set-proxy socks5://127.0.0.1:1080

echo ""
echo "=== 安装完成！==="
echo "现在可以使用以下命令："
echo "  term-accel on    # 开启代理"
echo "  term-accel off   # 关闭代理"
echo "  term-accel status # 查看状态"
echo "  term-accel test  # 测试连通性"
echo ""
echo "默认代理已配置为：socks5://127.0.0.1:1080"
echo "如果需要修改代理，请使用：term-accel set-proxy [url]"
