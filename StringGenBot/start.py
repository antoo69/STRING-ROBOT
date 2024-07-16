from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

this is the string session {me2},
please use it as best as possible.
New accounts are prohibited from being used (unless they have already been used for interaction)
ID 5/6 is prohibited from use.

𝐌𝐚𝐝𝐞 𝐁𝐲  : [𝐓𝐇𝐄 𝐕𝐈𝐏 𝐁𝐎𝐘 !](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" Group ", url="https://t.me/BestieVirtual"),
                    InlineKeyboardButton(" channel ", url="https://t.me/Nenen_degrees")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
