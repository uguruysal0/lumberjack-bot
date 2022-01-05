from io_provider import fast_provider
from bot import LumberjackBot


def prepare_telegram():
    import psutil
    import sys
    if sys.platform.startswith('darwin'):
        import Foundation
        import Cocoa
        pid = -1
        for proc in psutil.process_iter():
            try:
                if proc.name() == "Telegram":
                    pid = proc.pid
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if pid == -1:
            exit(1)
        telegram_app = Foundation.NSRunningApplication.runningApplicationWithProcessIdentifier_(
            pid)
        telegram_app.activateWithOptions_(
            Cocoa.NSApplicationActivateIgnoringOtherApps)
    else:
        raise ValueError(sys.platform + "is not supported")


def main(*args, **kwargs):
    """
    Driver code for Lumberjack telegram game bot. Just open telegram, start the game then run the code.
    But be careful, you might get banned and your further scores for *any game* will not be recored.
    """
    prepare_telegram()
    fast_prvider = fast_provider.FastProvider()
    bot = LumberjackBot(fast_prvider, key_delay=0.01, screenshot_delay=0.02)
    bot.play()


if __name__ == "__main__":
    main()
