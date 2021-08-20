"""
Available commands:
.google
"""

from re import findall

import requests
from search_engine_parser import GoogleSearch

from astro import CMD_HELP
from astro.utils import admin_cmd


@astro.on(admin_cmd(outgoing=True, pattern=r"google (.*)"))
@astro.on(sudo_cmd(allow_sudo=True, pattern=r"google (.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search from @Astro_HelpChat . """
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await eor(
        q_event,
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg,
        link_preview=False,
    )


CMD_HELP.update(
    {
        "search": ".google <query>\nUse - Google the query."
    }
)
