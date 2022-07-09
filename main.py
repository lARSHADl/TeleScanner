import configparser
from telethon import TelegramClient, events
from call import notify


dealsFilter = ['grab', 'loot', 'looot', 'mrp Error', 'mrp error', 'MRP Error', 'Loot', 'big loot', 'fast', 'grab fast',
               'looot', 'Grab']
channel = 'target-chanel-link'

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient(phone, api_id, api_hash)

tim = datetime.datetime.now()


@client.on(events.NewMessage(chats=channel))
async def newMessageListen(event):
    newMessage = event.message.message

    if "over" not in newMessage.lower():
        for x in dealsFilter:
            if re.search(x, newMessage):
                await client.forward_messages(entity='me', messages=event.message)
                notify()
                print("The user is notified at : , tim)
                break


with client:
    client.run_until_disconnected()
