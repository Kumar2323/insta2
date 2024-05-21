import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7114731765:AAGmTqB72nH0LK16y3DML0ryWrVU0HyR5ac'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Instagram Downloader Bot! Send me an Instagram post URL and I'll download the media for you.")

def download_media(update, context):
    url = update.message.text
    response = requests.get(url)

    if response.status_code == 200:
        # Extract the media URL from the Instagram page
        media_url = extract_media_url(response.text)

        if media_url:
            # Download the media
            media_response = requests.get(media_url)
            if media_response.status_code == 200:
                # Save the media to a file
                file_name = f"instagram_media_{update.message.message_id}.jpg"
                with open(file_name, 'wb') as file:
                    file.write(media_response.content)

                # Send the downloaded media to the user
                context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_name, 'rb'))

                # Delete the temporary file
                os.remove(file_name)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Failed to download the media.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No media found in the provided URL.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Instagram URL.")

def extract_media_url(html):
    # Extract the media URL from the HTML using string manipulation or regular expressions
    # This is a simplified example and may not work for all Instagram pages
    start_index = html.find('meta property="og:image" content="') + len('meta property="og:image" content="')
    end_index = html.find('"', start_index)
    media_url = html[start_index:end_index]
    return media_url

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    media_handler = MessageHandler(Filters.text & ~Filters.command, download_media)
    dispatcher.add_handler(media_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
