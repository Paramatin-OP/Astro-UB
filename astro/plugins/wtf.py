"""Emoji
Available Commands:
.wtf"""

import asyncio

from astro import CMD_HELP


@astro.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah",
            "What the Fuck You are saying",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5])


CMD_HELP.update({"wtf": ".wtf\nUse - Animation Plugin to spam the chat recents lel"})
