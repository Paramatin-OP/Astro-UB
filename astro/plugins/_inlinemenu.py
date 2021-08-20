# Astro
# INLINE_HELP
import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from astro import CMD_HELP, CMD_LIST, CUSTOM_PMPERMIT, bot

from astro.plugins import astrostats
from astro.config import Config
NAME = Config.NAME
PM_PIC = os.environ.get("PM_PIC", None)
ASTRO_PIC = (
    PM_PIC
    if PM_PIC
    else "https://telegra.ph/file/1dc4cf071ecd2be57e30a.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "This is Pro Security By ƛsτʀ๏ υsєяъ๏т To my Master...!"
)
DEFAULTUSER = str(NAME) if NAME else "ASTRO user✨"
USER_BOT_WARN_ZERO = "𝘼𝙃𝙃𝙃𝙃𝙃!!!!!\n𝙄 𝙩𝙤𝙡𝙙 𝙮𝙤𝙪 𝙉𝙤𝙩 𝙏𝙤 𝙨𝙥𝙖𝙢 𝙗𝙚 𝙞𝙣 𝙇𝙞𝙢𝙞𝙩𝙨 𝙗𝙪𝙩 𝙔𝙤𝙪 𝙏𝙤𝙤𝙠 𝙈𝙚 𝙇𝙞𝙜𝙝𝙩𝙡𝙮....😒\n𝗡𝗢𝗪 𝗟𝗘𝗧 𝗠𝗘 𝗕𝗟𝗢𝗖𝗞 𝗬𝗢𝗨😂✌️\n𝘿𝙊𝙉'𝙏 𝙈𝙀𝙎𝙎-𝙐𝙋 𝙒𝙄𝙏𝙃 𝙈𝙀 𝘼𝙂𝘼𝙄𝙉 \n𝙁𝙐𝘾𝙆 𝙊𝙁𝙁🙂"

if Config.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "__knock Knock__👀\nWho is There✨**This is PM SECURITY OF [{}](tg://user?id={})**\nBY ƛsτʀ๏ υsєяъ๏т\n\n"
        "{}\n\n"
        "Something Important you Have?🤔\nSorry But I can't Approve You 🙂Until My master Says\n"
        "\n TRY TO **PM** via {} if Something Important"
        "\nPlease choose why you are here, from the available options:\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif Config.LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "✨")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 4))

if Config.BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Hellow"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© ƛsτʀ๏ Help",
                text="{}\ncυяяєηт ρłυgıηs of ƛsτʀ๏ υsєяъ๏т: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**astro Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n© @Astro_HelpChat ™",
                buttons=[
                    [custom.Button.inline("Stats📊", data="statcheck")],
                    [Button.url("Repository ✨", "https://github.com/PsychoBots/Astro-UB")],
                    [
                        Button.url(
                            "Deploy Astro🌌",
                            "https://heroku.com/deploy?template=https://github.com/PsychoBots/Astro-UB",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("__knock"):
            ASTROBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=ASTRO_PIC,
                text=ASTROBT,
                buttons=[
                    [
                        custom.Button.inline("To Request 😓", data="req"),
                        custom.Button.inline("To Ask❔", data="ask")
                    ],
                    [
                        custom.Button.inline("For Chatting💬", data="chat"),
                        custom.Button.inline("Something else😶", data="elsi")],
                    [custom.Button.inline("What is this❓", data="wht")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"astro - Telegram Userbot.",
                buttons=[
                    [
                        Button.url("Repository ✨", "https://github.com/PsychoBots/Astro-UB"),
                        Button.url(
                            "Deploy Astro🌌",
                            "https://heroku.com/deploy?template=https://github.com/PsychoBots/Astro-UB",
                        ),
                    ],
                    [Button.url("Support✌️", "https://t.me/Astro_HelpChat")],
                ],
            )
        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to ƛsτʀ๏ υsєяъ๏т**\n\nClick below buttons for more",
                buttons=[
                    [custom.Button.url("Creator👀", "https://t.me/Alone_loverboy")],
                    [
                        custom.Button.url(
                            "💾Source Code", "https://github.com/PsychoBots"
                        ),
                        custom.Button.url(
                            "Deploy🌌",
                            "https://heroku.com/deploy?template=https://github.com/PsychoBots/Astro-UB",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Updates and Support Group↗️", "https://t.me/Astro_HelpChat"
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Create Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine😒"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wht")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Don't you know what is this🙄?"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"This is the PM Security for {DEFAULTUSER} ✨ To Protect My Master From Scammers And those Who want  to disturb my Master.. PROTECTION IS ON BY [ASTRO_USERBOT](https://t.me/Astro_UserBot).\n If You also wanted to have That Deoloy Astro-Userbot Get Help from [Astro_HelpChat](https://t.me/Astro_HelpChat)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu main Opened-Again🍁", buttons=buttons)
        else:
            reply_pop_up_alert = "Hey you.🙄 Get Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine🙂!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Is it joke🙄You wanna to request your self\nthis is not for you"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oki👀You have something to request to {DEFAULTUSER}\nIf {DEFAULTUSER} knows He will glad to help you😊\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!\nSee what he wants to request 👀!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "You wanna to chat your self😆\nThis is not for you Master"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"You wanna to chat👀💬\nOki My master is offline now. if {DEFAULTUSER} will be in mood of chatting he will talk to you😊\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!\nIf you are in mood of chatting You can talk to him👀!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ask")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "😆 What are you going to ask yourself\n This is not for you Master"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"👀What you want to ask to {DEFAULTUSER} ? Leave Your queies in Single Line\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {MYUSER}, [{first_name}](tg://user?id={ok}) wants to **ASK Something** in PM🤔check his DM👀I told him to leave your message!\ngo and Check🙃!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"elsi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "what are u doing 🥴This is not for u"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"😶ok..!You have something else For my {MYUSER} \nNow wait...! My master is offline NoW🥴When he will come he will Reply\nDon't Spam till wait he comes 🙂."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_GP,
                f"Hey {MYUSER}, [{first_name}](tg://user?id={ok}) wants to PM you\nHE HAVE **Something Else** For u😲\nGo and check..",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "Menu Closed!!🍂", buttons=[Button.inline("Re-open Menu", data="reopen")]
            )
        else:
            reply_pop_up_alert = "Hey you.🙄 Get Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine🙂 "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = astrostats
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Hey you.🙄 Get Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine🙂!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"Commands Available in {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Astro UserBot".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "Commands List is Big😓Check Your Saved Message Commands list is Forwarded There🙃!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nThis will be auto-deleted in 2 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(120)
                    await ok.delete()
            else:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    tele = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {}".format(tele, x), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⊰≾•ρяєѵıσυs", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⎝⎝cłσsє⎠⎠", data="close"),
                custom.Button.inline(
                    "ηєxт•≳⊱", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
