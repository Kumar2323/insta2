from pyrogram import Client, filters
from datetime import datetime
import os,subprocess
import time
import pytz

app = Client("EenaduPapers",
             api_id=23933217,
             api_hash="9295ff05232442f3dbb48beb8698b5ed",
             bot_token="6044902922:AAE9EaEHAt80YUWEvvy74rU0JzL8KdaUXRs",
             workers=50,
             max_concurrent_transmissions=20
             )
@app.on_message(filters.command('post'))
async def post(bot,message):
    chat_id=message.chat.id
    user_id=message.from_user.id
    msg_id = message.id
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    msg = await bot.send_message(message.from_user.id,'Getting All Papers',reply_to_message_id=message.id)
    date = now.strftime("%d-%m-%Y")
    subprocess.run(['python','eenadu.py'])
    await msg.edit("Uploading Papers to Telegram Channel")
    await bot.send_document("-1001532850156",f"Mains/Eenadu_TG {date}.pdf")
    await bot.send_document("-1001532850156",f"Mains/Eenadu_AP {date}.pdf")
    await bot.send_document("-1001532850156",f"Mains/Eenadu_GHYD {date}.pdf")
    await msg.edit("Done Uploading....")
    
@app.on_message(filters.command('ap'))
async def post(bot,message):
    chat_id=message.chat.id
    user_id=message.from_user.id
    msg_id = message.id
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    msg = await bot.send_message(message.from_user.id,'Getting All AP State Papers',reply_to_message_id=message.id)
    date = now.strftime("%Y-%m-%d")
    subprocess.run(['python','ap.py'])
    folder_path = "apdist"
    await bot.send_message("-1001532850156","AP District Papers")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        

        await bot.send_document("-1001532850156",file_path)
        time.sleep(0.75)
    os.rmdir("apdist")         
    await msg.edit("Done Uploading....")
              
              
@app.on_message(filters.command('ts'))
async def post(bot,message):
    chat_id=message.chat.id
    user_id=message.from_user.id
    msg_id = message.id
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    msg = await bot.send_message(message.from_user.id,'Getting All TS State Papers',reply_to_message_id=message.id)
    date = now.strftime("%Y-%m-%d")
    subprocess.run(['python','ts.py'])
    folder_path = "tsdist"
    await bot.send_message("-1001532850156","TSDistrict Papers")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        await bot.send_document("-1001532850156",file_path)
        time.sleep(0.75)      
    os.rmdir("tsdist")
    await msg.edit("Done Uploading....")
    
@app.on_message(filters.command('sun'))
async def post(bot,message):
    chat_id=message.chat.id
    user_id=message.from_user.id
    msg_id = message.id
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    msg = await bot.send_message(message.from_user.id,'Getting Sunday Papers',reply_to_message_id=message.id)
    date = now.strftime("%d-%m-%Y")
    subprocess.run(['python','sun.py'])
    folder_path = 'Sunday'
   # try:
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        await bot.send_document("-1001532850156",file_path)
        
    await msg.edit("Done Uploading....")
    os.rmdir("Sunday")
    #except:
      
     # await msg.edit("Papers Not Found")
    
    
    
app.run()
