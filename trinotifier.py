from discord_webhook import DiscordWebhook
import requests
import time

# Made by Danyal I. on 12 March 2021
# Just change the variable 'url' to your webhook
# And replace the variable 'category' to the item type you want to monitor

# Set up variables
start       = time.time()
url         = 'https://discord.com/api/webhooks/819923763801751593/38DNvKFMggCAu8_9jN1QoqZazEBpQ507F7Xzp0C0lXZZQ7PaDgwj8gpXEqk9vNz47gBb'
category    = 'hat' # hat, face, gear, shirt, pants
api         = 'https://vistora.xyz/api/store/fetch?type=' + category + '&sort=newest&limit=1&page=1'

# Set the most recent item
json        = requests.get(api).json()[0]
currentItem = json['name']

# Function to check if a new item has replaced the initially set one
def check():
    global currentItem

    json = requests.get(api).json()[0]

    if currentItem != json['name']:c
        currentItem = json['name']
        webhook = DiscordWebhook(url = url, content = 'New item ' + json['name'])
        response = webhook.execute()

# Run the script every 5 seconds
# Do not decrease the time as it may cause performance issues
while True:
    check()
    print "Checked items"
    time.sleep(5.0 - ((time.time() - start) % 5.0))