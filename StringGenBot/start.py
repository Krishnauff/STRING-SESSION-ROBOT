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
        text=f"""Hᴇʏ {msg.from_user.mention}🍷,

Tʜɪs ɪs {me2},Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝐊𝐑𝐈𝐒𝐇𝐍𝐀](https://t.me/ab_krishna_uff) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ❣️", url="https://t.me/ab_krishna_uff"),
                    InlineKeyboardButton("🥀 𝐎𝐟𝐟𝐢𝐜𝐞 🥀", url="https://t.me/Ajanabee_Duniya")   
            ]
         ]
      ),
        disable_web_page_preview=True,
    )
