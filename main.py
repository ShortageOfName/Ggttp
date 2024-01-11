from config import *
from callback import *
from pyrogram import Client ,filters , enums
from pyroaddon import listen
from pyrogram.errors import *
import requests,json
from pyrogram.types import *
from time import sleep
from buttons import *
import random,  string
cli = Client (  "evil gpt mr rk",
                api_id = API_ID,
                api_hash = API_HASH ,
                bot_token = BOT_TOKEN 
                )
                
headers = {
                'authority': 'awesomeflare',
                'Authorization':APIKEY,
                'content-type': 'application/json'
            }
            
            
            
@cli.on_message(filters.private & filters.command(['start']))
async def start(_, m):
    usr_name = m.from_user.first_name  
    usr_id = m.from_user.id
    usr_set(usr_id)
    usr_username= m.from_user.username
    await m.reply('**Dark Gpt Api Demo Bot  \ntype /HELP for help**', reply_markup = ALLBOTS )
    
    
@cli.on_message(filters.private & filters.command(['language']))
async def language_(_, m):
    await m.reply("select language",reply_markup = InlineKeyboardMarkup(Languages()[0]))
 
    
@cli.on_message(filters.private & filters.command(['tone']))
async def tone_(_, m):
    await m.reply("**select your prefered Tone **",reply_markup=APPROACH_BUTTON)
                
@cli.on_message(filters.private & filters.command(['mysetting']))
async def settings_(_, m):
    usr_id = m.from_user.id
    _, s, j = ret_setting(usr_id)
    await m.reply(f"**Approach : {s}\nLanguage : {j}**")

@cli.on_message(filters.private & filters.command(['help']))
async def help_message(_, m):
    await m.reply(f"""**.   type /help for this menu
    type /mysetting to see your current setting 
    type /language to set language
    type /tone to set approach/tone 
    
    or directly ask a question
    
    to upgrade your Api for commercial use, contact us @neuralg or DM @nextdevil**""")

        
    


 
@cli.on_message(filters.private & filters.text)
async def handlsev(c,m):
        resp = apiprocess(m.from_user.id , "generator","all",m.text , "i want exact answer")
        e = resp[slice(0,4096)]
        await m.reply(e.replace('#','•'),quote = True, parse_mode=enums.ParseMode.MARKDOWN, protect_content=False)
        f = resp.replace(e,"")
        try :
            await m.reply(f.replace('#','•'),quote = True, parse_mode=enums.ParseMode.MARKDOWN, protect_content=False)
        except:
            pass
        fl = resp.split('```')[1]
        ext = fl.split('\n') 
        fl = fl.replace(ext[0],"",1)
        with open(f'code.{ext[0]}','w') as f: 
            f.write(fl)
        await m.reply_document(f'code.{ext[0]}',caption='**Excercise Left for you😈**\n1 save the code \n2 run it in your best IDE ')
        os.remove(f'code.{ext[0]}')
            
 
    
@cli.on_callback_query() 
async def callback_func(_,u):
    user_id = u.from_user.id
    if u.data.startswith('approach'):
        appr = u.data.split(',')[1]
        update_approach (user_id , appr)
        await u.message.edit(f"**Approach/Tone updated to {appr}**")
    else :
        update_language(user_id , u.data)
        await u.message.edit(f"**language updated to {u.data} **")
            


@cli.on_inline_query() 
async def inline_func (c,m):
  if m.query == "" or None :
        await m.answer( results = [ ( InlineQueryResultArticle(
                                                                title = ("👇 please type something "),
                                                                description = ("it should not be blank query"),
                                                                  thumb_url = "",
                                                                input_message_content = InputTextMessageContent(("**still you are perfect idiot after all, men😤 did you just clicked empty inline result or don't you kñow how to type **"))
                                                                ))],cache_time = 3000 )
        return
  else :
       resp = apiprocess(m.from_user.id , "generator","all",m.query , "i want exact answer")
       e = resp[slice(0,4096)]
       await m.answer( results = [ ( InlineQueryResultArticle(
                                                                title = ("Answer"),
                                                                description = m.query,
                                                                thumb_url = "",
                                                                input_message_content = InputTextMessageContent((e.replace('#','•')))
                                                                ))],cache_time = 3000 )
            
            
            
def apiprocess(user_id , task , lang , prompt , code='none' ):
    _, language , tone = ret_setting(user_id)
    json_data = {
        'task':task,
        'program':lang,
        "prompt":prompt,
        "code":code ,
        'further_description1' :'none',
        'further_description2' : 'none',
        'language' :language, 
        'approach' : tone 
        }
    e = requests.post('https://darkgpt.hop.sh/neural/api' ,headers=headers,json=json_data)
    rs = json.loads(e.text)
    return rs["message"]


    
print('running')
cli.run()
