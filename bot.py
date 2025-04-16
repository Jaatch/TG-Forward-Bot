from pyrogram import Client, __version__

from config import Config
from config import LOGGER

from user import User
import pyromod.listen


class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH, "3ff49e183e05744e7551cf14091cdced"
            api_id=Config.API_ID, "25728041"
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN, "7353037933:AAFt3HFYLvHd7r3sLO5xm-DBEM0J11Pyk7M"
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
