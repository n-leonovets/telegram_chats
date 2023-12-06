import asyncio
import platform

from src.enums.utils import PlatformName


def asyncio_speedup() -> None:
    platform_name = platform.system().lower()
    if platform_name == PlatformName.WINDOWS:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    elif platform_name == PlatformName.DARWIN or platform_name == PlatformName.LINUX:
        from uvloop import install
        install()
