import telebot
from telebot import types
from pytubefix import YouTube
import os
from dotenv import load_dotenv

load_dotenv()

TELEBOT_TOKEN = os.environ.get("TELEBOT_TOKEN")
bot = telebot.TeleBot(TELEBOT_TOKEN)

def fetch_video(link):
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    yt_url = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().url
    return yt_url

def create_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton("Start", callback_data="start")
    help_button = types.InlineKeyboardButton("Help", callback_data="help")
    keyboard.add(start_button, help_button)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = create_menu_keyboard()
    bot.send_message(
        message.chat.id,
        f'Hello , I am built to provide download link for YouTube videos which can be directly saved to your local device.\nKindly paste the URL of the video here👇',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    keyboard = create_menu_keyboard()
    bot.send_message(
        message.chat.id,
        "If you are facing problems finding the URL, go to the YouTube video and copy the link in the Address Bar of the Browser or try to share the video and then copy the link.",
        reply_markup=keyboard
    )

@bot.message_handler()
def handle_video(message):
    try:
        bot.reply_to(message, "Fetching your video, please wait...")
        download_link = fetch_video(message.text)
        bot.reply_to(message, f"Download Link: {download_link}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        send_welcome(call.message)
    elif call.data == "help":
        send_help(call.message)
    bot.answer_callback_query(call.id)

print("Server running")
bot.infinity_polling()
