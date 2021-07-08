#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @lnc3f3r Jins Mathew Re-Create

import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import OWNER_ID

from bot import VERIFY # pylint: disable=import-error

@Client.on_message(filters.command(["settings"]) & filters.group, group=1)
async def settings(bot, update):
    
    if not update.from_user.id in OWNER_ID:
        buttons = [[
            InlineKeyboardButton('Developers', url='https://t.me/joinchat/TRlZZilyh-MVa66t'),
            InlineKeyboardButton('Source Code 🧾', url='https://t.me/joinchat/YS-WlsUC9nFiOWM0')
        ], [
            InlineKeyboardButton('Support 🛠', url='https://t.me/joinchat/YS-WlsUC9nFiOWM0')
        ]]

        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=update.chat.id,
            text="""<b>Hey {}!!</b>
            <i>Am Just A Advance Auto Filter Bot....😉

            Only For <b><u><a href="https://t.me/joinchat/TRlZZilyh-MVa66t">Universal Film Studio Group</a></u></b>""".format(update.from_user.first_name),
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
        return
    
    chat_id = update.chat.id
    user_id = update.from_user.id if update.from_user else None
    global VERIFY

    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = [631110062]
        #Jins Has Changed This Code For Privacy 06th May 2021
        #async for x in bot.iter_chat_members(chat_id=chat_id, filter="administrators"):
            #admin_id = x.user.id 
            #admin_list.append(admin_id)
        #admin_list.append(None)
        #######################################################
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return
    
    bot_info = await bot.get_me()
    bot_first_name= bot_info.first_name
    
    text =f"<i>{bot_first_name}'s</i> Settings Pannel.....\n"
    text+=f"\n<i>You Can Use This Menu To Change Connectivity And Know Status Of Your Every Connected Channel, Change Filter Types, Configure Filter Results And To Know Status Of Your Group...</i>"
    
    buttons = [
        [
            InlineKeyboardButton
                (
                    "Channels", callback_data=f"channel_list({chat_id})"
                ), 
            
            InlineKeyboardButton
                (
                    "Filter Types", callback_data=f"types({chat_id})"
                )
        ],
        [
            InlineKeyboardButton
                (
                    "Configure 🛠", callback_data=f"config({chat_id})"
                )
        ], 
        [
            InlineKeyboardButton
                (
                    "Status", callback_data=f"status({chat_id})"
                ),
            
            InlineKeyboardButton
                (
                    "About", callback_data=f"about({chat_id})"
                )
        ],
        [
            InlineKeyboardButton
                (
                    "Close 🔐", callback_data="close"
                )
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message (
        
        chat_id=chat_id, 
        text=text, 
        reply_markup=reply_markup, 
        parse_mode="html",
        reply_to_message_id=update.message_id
        
        )


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F" 
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF" 
                               u"\U0001F1E0-\U0001F1FF" 
                               u"\U00002500-\U00002BEF" 
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
    "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r' ', str(string))
