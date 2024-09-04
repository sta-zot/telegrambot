
import logging
import asyncio

from app.bot import start_bot
from db.queryes import engine, create_db

async def main():
    logging.basicConfig(level=logging.INFO)
    #await start_bot()
    #print("Bot started")
    await create_db(engine)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as err:
        print(err)
        exit(0)