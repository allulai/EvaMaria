class script(object):
    START_TXT = """𝗛𝗲𝗹𝗹𝗼 {},
𝗠𝘆 𝗡𝗮𝗺𝗲 𝗶𝘀 <a href=https://t.me/{}>{}</a>, 

𝗜𝗮𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗔𝘂𝘁𝗼 𝗙𝗶𝗹𝘁𝗲𝗿 + 𝗠𝗼𝘃𝗶𝗲 𝗦𝗲𝗮𝗿𝗰𝗵 + 𝗠𝗮𝗻𝘂𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿 𝗕𝗼𝘁. 𝗜 𝗖𝗮𝗻 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀. 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲𝘀 𝗩𝗶𝗮 𝗜𝗻𝗹𝗶𝗻𝗲. 𝗜 𝗖𝗮𝗻 𝗔𝗹𝘀𝗼 𝗔𝗱𝗱 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗚𝗿𝗼𝘂𝗽𝘀.  𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗘𝗻𝗷𝗼𝘆"""
    HELP_TXT = """𝗛𝗲𝘆 {}
𝗛𝗘𝗥𝗘 𝗜𝗦 𝗧𝗛𝗘 𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗠𝗬 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦."""
    ABOUT_TXT = """🤖 ʙᴏᴛ ɴᴀᴍᴇ: {}
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/SaeByeokTG>ꜱᴀᴇ ʙʏᴇᴏᴋ</a>
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ: ᴘʏʀᴏɢʀᴀᴍ
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ
📡 ʜᴏsᴛᴇᴅ ᴏɴ: ʜᴇʀᴏᴋᴜ
💡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/nokiyirunnoippokitum>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"""
    SOURCE_TXT = """💡sᴏᴜʀᴄᴇ - <a href=https://t.me/nokiyirunnoippokitum>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>

<b>ᴅᴇᴠᴇʟᴏᴘᴇʀ:</b>
- <a href=https://t.me/SaeByeokTG>ꜱᴀᴇ ʙʏᴇᴏᴋ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Zendaya will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Zendaya should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/TheZendayaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Zendaya

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴍʏ ᴀᴅᴍɪɴꜱ

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: <code>{}</code>
    
👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>

👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>

⚙️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> MB

🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> MB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
