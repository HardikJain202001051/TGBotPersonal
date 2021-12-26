from selenium.webdriver.common.by import By
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

TOKEN = '5027998873:AAHaa9EOETEwvUAVFsX0almIMw-wr9jJVm4'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
      
def welcome(update, context):
    update.message.reply_text("Hey!Send the link of tweet to get the video")

allowed_users = [1518770169,1243219058]
def message_action(update, context):
    if update.message.chat_id in allowed_users:
        link = update.message.text        
        site = "https://twittervideodownloader.com"
        #s = Service("D:\SeleniumDriverChrome\chromedriver.exe")
        #driver = webdriver.Chrome(service=s)
        driver.get(site)
        field = driver.find_element(By.NAME, 'tweet')
        field.send_keys(link)
        submit = driver.find_element(By.CLASS_NAME, 'input-group-button')
        submit.click()
        d = driver.find_element(By.LINK_TEXT,"Download Video")
        link = d.get_attribute('href')
        update.message.reply_video(video=link)
            
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
start = CommandHandler('start', welcome)
dispatcher.add_handler(start)
user_message = MessageHandler(Filters.text, message_action)
dispatcher.add_handler(user_message)
updater.start_polling()
updater.idle()
