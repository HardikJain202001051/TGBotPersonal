from selenium.webdriver.common.by import By
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import requests
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tweepy
from selenium import webdriver

#following secrets have been removed
TOKEN = ''
API_Key = ''
API_Key_Secret = ''
allowed_users = [] #list of allowed users
auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
api = tweepy.API(auth)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
      
def welcome(update, context):
    update.message.reply_text("Hey!Send the link of tweet to get the video")
    #r = 'https://api.telegram.org/bot'+TOKEN+'/sendMessage?chat_id='+'@DevelopmentNewsIndia'+'&text=Hello World!'

def message_action(update, context):
    if update.message.chat_id in allowed_users:
        link = update.message.text
        ids = link.split('/')[-1].split('?')[0]
        
        status = api.get_status(id=ids, tweet_mode="extended")
        cap = status.full_text
        site = "https://twittervideodownloader.com"
        #s = Service("D:\SeleniumDriverChrome\chromedriver.exe")
        #driver = webdriver.Chrome(service=s)
        driver.get(site)
        field = driver.find_element(By.NAME, 'tweet')
        field.send_keys(link)
        submit = driver.find_element(By.CLASS_NAME, 'input-group-button')
        submit.click()
        d = driver.find_element(By.LINK_TEXT,"Download Video")
        link2 = d.get_attribute('href')
        r = 'https://api.telegram.org/bot' + TOKEN + '/sendVideo?chat_id=@DevelopmentNewsIndia&caption='+cap+'&video='+link2
        requests.post(r)
        #update.message.reply_video(video=link2,caption=cap)
    else:
        update.message.reply_text("Sorry, you are not an authorized user")
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
start = CommandHandler('start', welcome)
dispatcher.add_handler(start)
user_message = MessageHandler(Filters.text, message_action)
dispatcher.add_handler(user_message)
updater.start_polling()
updater.idle()
