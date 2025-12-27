我已经帮你把这份使用说明优化为规范的Markdown格式，替换了所有占位符，调整了排版和可读性，你可以直接复制粘贴到GitHub的README.md中：
# term-accel 使用说明

## 1. 项目简介
**term-accel** 是一个 Mac 终端代理一键管理工具，专为开发者设计，用于简化各种开发工具（如 git/pip/npm/brew）的代理配置管理。

### 1.1 主要特性
- 一键开启/关闭终端代理
- 自动为多种开发工具配置代理
- 支持自定义代理地址
- 实时查看各工具代理状态
- 测试 GitHub 连通性验证代理效果

## 2. 安装方法
### 2.1 方法一：使用安装脚本（推荐）
```bash
# 下载并运行安装脚本
bash <(curl -s https://raw.githubusercontent.com/luyang668899/term-accel/master/install.sh)
2.2 方法二：手动安装

1. 克隆项目：
git clone https://github.com/luyang668899/term-accel.git
cd term-accel
2. 安装依赖：
pip install -r requirements.txt
3. 安装项目：
pip install .
3. 快速开始

3.1 设置代理地址

首次使用需要设置代理地址：
# 示例：设置 SOCKS5 代理
term-accel set-proxy socks5://127.0.0.1:1080

# 示例：设置 HTTP 代理
term-accel set-proxy http://127.0.0.1:8080
3.2 开启代理
term-accel on
开启后，会自动为以下工具配置代理：

• Git

• Pip

• Npm

• Brew

• 系统环境变量（当前会话和 .zshrc）

3.3 关闭代理
term-accel off
关闭后，会清除所有工具的代理配置。

3.4 查看代理状态
term-accel status
输出示例：
当前代理状态：
  git: socks5://127.0.0.1:1080
  pip: socks5://127.0.0.1:1080
  npm: socks5://127.0.0.1:1080
  system: socks5://127.0.0.1:1080
3.5 测试 GitHub 连通性
term-accel test
如果代理生效，会显示：
GitHub连通性测试成功（代理生效）
4. 命令详解

4.1 set-proxy
term-accel set-proxy <proxy_url>
功能：设置代理地址。
参数：

• <proxy_url>: 代理地址，支持 http/https/socks5 等协议。
示例：
term-accel set-proxy socks5://127.0.0.1:1080
4.2 on
term-accel on
功能：开启代理，为所有支持的工具自动配置代理。

4.3 off
term-accel off
功能：关闭代理，清除所有工具的代理配置。

4.4 status
term-accel status
功能：查看各工具的代理状态。

4.5 test
term-accel test
功能：测试 GitHub 连通性，验证代理是否生效。

4.6 --help
term-accel --help
功能：查看帮助信息。

5. 支持的工具

5.1 Git

为 Git 全局配置 HTTP 和 HTTPS 代理：
git config --global http.proxy <proxy_url>
git config --global https.proxy <proxy_url>
5.2 Pip

为 Pip 配置代理：
pip3 config set global.proxy <proxy_url>
5.3 Npm

为 Npm 配置 HTTP 和 HTTPS 代理：
npm config set proxy <proxy_url>
npm config set https-proxy <proxy_url>
5.4 Brew

为 Brew 配置代理（通过环境变量）：
export http_proxy=<proxy_url>
export https_proxy=<proxy_url>
6. 配置文件

代理配置存储在 ~/.term-accel/config.json 文件中：
{
  "proxy_url": "socks5://127.0.0.1:1080"
}
你可以手动编辑此文件修改代理地址。

7. 常见问题

7.1 代理设置不生效

解决方法：

1. 检查代理地址是否正确

2. 确认代理服务器正在运行

3. 尝试重新开启代理：term-accel off && term-accel on

4. 重启终端后再次尝试

7.2 权限错误

解决方法：
使用 sudo 命令运行：
sudo term-accel <command>
7.3 某些工具代理未配置

解决方法：

1. 确保工具已正确安装

2. 检查工具的配置文件是否存在

3. 尝试手动配置该工具的代理

7.4 测试命令失败

解决方法：

1. 检查网络连接

2. 确认代理服务器正在运行

3. 检查代理地址是否正确

8. 卸载方法
pip uninstall term-accel
同时，你可以删除配置文件：
rm -rf ~/.term-accel
9. 更新方法

9.1 使用安装脚本更新
bash <(curl -s https://raw.githubusercontent.com/luyang668899/term-accel/master/install.sh)
9.2 手动更新
# 进入项目目录
cd term-accel

# 拉取最新代码
git pull

# 重新安装
pip install .
10. 联系与反馈

如有问题或建议，欢迎通过以下方式反馈：

• GitHub Issues: https://github.com/luyang668899/term-accel/issues

• 邮箱: 
11. 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。


