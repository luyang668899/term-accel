from setuptools import setup, find_packages

setup(
    name="term-accel",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "requests>=2.31.0"
    ],
    entry_points={
        "console_scripts": [
            "term-accel = term_accel.cli:cli"
        ]
    },
    author="",
    author_email="",
    description="Mac终端代理一键管理工具",
    long_description="用于Mac终端的代理一键管理工具，支持git/pip/npm/brew等工具的代理配置管理",
    long_description_content_type="text/plain",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)