
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterMusic

from astro.plugins import OWNER_ID, ASTRO
from . import CMD_HELP

PROF = f"[{ASTRO}](tg://user?id={OWNER_ID})"


@borg.on(admin_cmd("spotify ?(.*)"))
async def _(event):
    try:
        await astro(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))
    except UserAlreadyParticipantError:
        pass
    except Exception as e:
        await event.edit(
            f"`Hmm.. Some unknown error occured!\nAborting...\nError - {str(e)}`"
        )
        return
    name = event.pattern_match.group(1)
    if not name:
        await event.edit(
            "Song donwloader.\nSyntax - `.spotify name`\nFor better results, use Artist Name -Song Name."
        )
        return
    chat = -1001569474379
    current_chat = event.chat_id
    current_msg = event.id
    cap = """
༆ **Song name** - `{}`
༆ **Uploaded by** {}
"""
    try:
        async for event in astro.iter_messages(
            chat, search=name, limit=1, filter=InputMessagesFilterMusic
        ):
            ok = cap.format(event.message, PROF)
            await astro.delete_messages(current_chat, current_msg)
            await astro.send_file(current_chat, event, caption=ok)
    except BaseException:
        await event.reply(
            f"`Song, {name}, not found. For better results, use Artist Name -Song Name.`"
        )
        return


CMD_HELP.update({"spotify": ".spotify <song name>\nUse - Download song from spotify"})
