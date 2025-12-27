import json
import os

CONFIG_DIR = os.path.expanduser("~/.term-accel")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def init_config():
    """初始化配置目录和文件"""
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({"proxy_url": ""}, f)

def save_proxy_url(proxy_url):
    """保存代理地址"""
    init_config()
    # 先读取现有配置，然后更新
    config = {}
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except json.JSONDecodeError:
        # 如果JSON文件格式错误，创建新的配置
        config = {}
    
    config["proxy_url"] = proxy_url
    
    # 写入更新后的配置
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def get_proxy_url():
    """读取代理地址，如果没有配置则返回默认地址"""
    init_config()
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        # 如果没有配置代理，返回默认地址
        return config.get("proxy_url", "socks5://127.0.0.1:1080")