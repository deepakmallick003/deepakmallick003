#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import json
import configparser as cfg


# In[11]:


token="1743726854:AAH2GztAPqLNnxFQBNmMeIG0bcTuvJ6Ep_g"
base="https://api.telegram.org/bot{}/".format(token)

class bot():
    def _init_(config):
        token=read_token_from_config_file(config)
        base="https://api.telegram.org/bot{}/".format(token)
    
    def get_updates(offset=None):
        url=base + "getUpdates?timeout=100"
        if offset:
            url = url+"&offset={}".format(offset + 1)
        
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(msg,chat_id):
        url=base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
        if msg is not None:
            requests.get(url)
            
    def make_reply(msg):
        reply=None
        if msg is not None:
            reply="Okay"
        return reply
    
    def read_token_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')


# In[ ]:


update_id=None

while True:
    print("...")
    updates=bot.get_updates(offset=update_id)
    updates=updates["result"]
    if updates:
        for item in updates:
            update_id=item["update_id"]
            try:
                message=item["message"]["text"]
            except:
                message=None
            from_=item["message"]["from"]["id"]
            reply=bot.make_reply(message)
            bot.send_message(reply,from_)    


# In[ ]:




