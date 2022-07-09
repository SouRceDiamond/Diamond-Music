import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/c41c41a1b48e64fea51c9.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@CR_T2"
)

CAPTION = f"**سرعة البينج:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("SouRce Diamond", "https://t.me/CR_T2")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)