from setuptools import setup, find_packages

setup(
    name="tiktok-downloader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "asyncio",
        # 添加其他项目依赖
    ],
    author="tiktok-downloader ",
    description="A TikTok video downloader",
    python_requires=">=3.7",
) 