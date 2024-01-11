from buttons import *
from pyrogram import Client as cli,filters,enums
from database import *
import os 
@cli.on_callback_query() 
async def callback_func(_,u):
    user_id = u.message.from_user.id
    if u.data == "help":
        print('do nothing')
        #await u.message.edit(HELP_TXT,reply_markup=CLOSEH)
    elif u.data.startswith('approach'):
        appr = u.data.split('-')[1]
        update_approach (user_id , appr)
        await u.message.reply("**fApproach/Tone updated to {appr}**")
    else :
        update_language(user_id , u.data)
        await u.message.edit("language setup Done ")
        