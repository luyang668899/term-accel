import subprocess
from .config import get_proxy_url

def run_cmd(cmd):
    """执行终端命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def set_proxy():
    """为各工具设置代理"""
    proxy_url = get_proxy_url()
    # 不再检查proxy_url是否为空，因为get_proxy_url会返回默认地址
    
    # Git代理
    run_cmd(f"git config --global http.proxy {proxy_url}")
    run_cmd(f"git config --global https.proxy {proxy_url}")
    # Pip代理 - 使用pip3确保兼容
    run_cmd(f"pip3 config set global.proxy {proxy_url}")
    # Npm代理
    run_cmd(f"npm config set proxy {proxy_url}")
    run_cmd(f"npm config set https-proxy {proxy_url}")
    # Brew代理（MacOS）
    run_cmd(f'echo "export http_proxy={proxy_url}" >> ~/.zshrc')
    run_cmd(f'echo "export https_proxy={proxy_url}" >> ~/.zshrc')
    # 同时在当前会话中设置环境变量
    run_cmd(f'export http_proxy={proxy_url}')
    run_cmd(f'export https_proxy={proxy_url}')
    return True, f"代理已开启，适配git/pip/npm/brew\n使用的代理地址：{proxy_url}"

def unset_proxy():
    """清除各工具代理"""
    # Git代理
    run_cmd("git config --global --unset http.proxy")
    run_cmd("git config --global --unset https.proxy")
    # Pip代理 - 使用pip3确保兼容
    run_cmd("pip3 config unset global.proxy")
    # Npm代理
    run_cmd("npm config delete proxy")
    run_cmd("npm config delete https-proxy")
    # Brew代理
    run_cmd("sed -i '' '/export http_proxy/d' ~/.zshrc")
    run_cmd("sed -i '' '/export https_proxy/d' ~/.zshrc")
    # 同时在当前会话中清除环境变量
    run_cmd("unset http_proxy")
    run_cmd("unset https_proxy")
    return True, "代理已关闭，恢复默认网络状态"

def check_status():
    """查看代理状态"""
    status = {}
    # 检查Git代理
    git_proxy, out, _ = run_cmd("git config --global http.proxy")
    status["git"] = out.strip() if git_proxy else "未配置"
    # 检查Pip代理 - 使用pip3确保兼容
    pip_proxy, out, _ = run_cmd("pip3 config get global.proxy")
    status["pip"] = out.strip() if pip_proxy and out.strip() else "未配置"
    # 检查Npm代理
    npm_proxy, out, _ = run_cmd("npm config get proxy")
    status["npm"] = out.strip() if npm_proxy and out.strip() and out.strip() != "null" else "未配置"
    # 检查系统代理环境变量
    env_proxy, out, _ = run_cmd("echo $http_proxy")
    status["system"] = out.strip() if env_proxy and out.strip() else "未配置"
    return status