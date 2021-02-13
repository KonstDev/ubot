from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client("my_account")
 
@app.on_message(filters.command("funny", prefixes=".") & filters.me)
def funny(_, msg):
    new_text = ''
    orig_text = msg.text.split(".funny ", maxsplit=1)[1]
    kek = 0
    for i in range(0, len(orig_text)):
        if (kek % 2 == 0):
            new_text += orig_text[i].lower()
        else: new_text += orig_text[i].upper()
        if (orig_text[i] != ' '):
            kek += 1
    msg.edit(new_text)
 
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
#http://github.com/KonstDev/


@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(_, msg):
    msg.edit('Pong!')

@app.on_message(filters.command("gh", prefixes=".") & filters.me)
def gh(_, msg):
    msg.edit('My github: http://github.com/KonstDev/') 
    

@app.on_message(filters.command("tb", prefixes=".") & filters.me)
def type(_, msg):
    #orig_text = msg.text.split(".tb ", maxsplit=1)[1]
    #text = orig_text
    #tbp = "" # to be printed
    #typing_symbol = "▒"
    msg.edit('**тЯнОчКу** **Бы**')
@app.on_message(filters.command("piar", prefixes=".") & filters.me)
def mybots(_, msg):
    msg.edit('My bots: \n 1) @howpythonbot \n 2)@whatsciencebot \n 3)@wplangbot')
 
app.run() 
