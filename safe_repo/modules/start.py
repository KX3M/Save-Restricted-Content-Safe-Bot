from pyrogram import filters
from safe_repo import app
from safe_repo.core import script
from safe_repo.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Update", url="https://t.me/pythonbotz"),
        InlineKeyboardButton("Support", url="https://t.me/offchats")],
        [ InlineKeyboardButton("Buy Premium", url= "t.me/metaui"),
         InlineKeyboardButton("Help", url="https://graph.org/How-To-Use-12-04")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
        await message.reply_photo(photo="https://graph.org/file/2f2033c98a4908125e03f-e74630cd759415b775.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
