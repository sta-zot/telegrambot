from app.bot import start_bot
import logging
import asyncio


async def main():
    logging.basicConfig(level=logging.INFO)
    await start_bot()
    print("Bot started")
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
        exit(0)