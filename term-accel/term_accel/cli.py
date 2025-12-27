import click
import requests
from .config import save_proxy_url, get_proxy_url
from .proxy import set_proxy, unset_proxy, check_status, run_cmd

@click.group()
def cli():
    """Mac终端代理一键管理工具"""
    pass

@cli.command(name="set-proxy")
@click.argument("proxy_url")
def set_proxy_command(proxy_url):
    """配置代理地址，如：term-accel set-proxy socks5://127.0.0.1:1080"""
    save_proxy_url(proxy_url)
    click.echo(f"代理地址已保存：{proxy_url}")

@cli.command()
def on():
    """开启终端代理"""
    success, msg = set_proxy()
    if success:
        click.echo(msg)
    else:
        click.echo(f"开启失败：{msg}", err=True)

@cli.command()
def off():
    """关闭终端代理"""
    success, msg = unset_proxy()
    click.echo(msg)

@cli.command()
def status():
    """查看代理状态"""
    status = check_status()
    click.echo("当前代理状态：")
    for tool, proxy in status.items():
        click.echo(f"  {tool}: {proxy}")

@cli.command()
def test():
    """测试GitHub连通性"""
    try:
        # 使用当前代理配置测试GitHub连接
        proxy_url = get_proxy_url()
        proxies = {}
        if proxy_url:
            proxies = {"http": proxy_url, "https": proxy_url}
        
        response = requests.head("https://github.com", proxies=proxies, timeout=5)
        if response.status_code == 200:
            click.echo("GitHub连通性测试成功（代理生效）")
        else:
            click.echo(f"GitHub连通性测试失败：状态码 {response.status_code}", err=True)
    except requests.RequestException as e:
        click.echo(f"GitHub连通性测试失败：{e}", err=True)

if __name__ == "__main__":
    cli()