from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import translators as ts
import whois
import time
import os

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
        else:
            new_text += orig_text[i].upper()
        if (orig_text[i] != ' '):
            kek += 1
    msg.edit(new_text)

tr_lang = 'ru'

@app.on_message(filters.command("whois", prefixes=".") & filters.me)
def who_is(_, msg):
    domain = msg.text.split(".whois", maxsplit=1)[1]
    er = False
    try:
        dom = whois.query(domain).__dict__
    except Exception as e:
        er = True
        #print(e)
    if (er == False):
        msg.edit('``' + str(dom) + '``')
    if (er == True):
        msg.edit('**Не ворк**')
        
@app.on_message(filters.command("eval_l", prefixes=".") & filters.me)
def eval_os(_, msg):
        error = 0
        toeval = msg.text.split(".eval_l ", maxsplit=1)[1]
        toeval_edit = toeval
        toeval_edit = toeval.replace('**', '^^')
        ret_str = "**Expression:**\n"
        ret_str += toeval_edit
        ret_str += '\n'
        ret_str += "**Result**:\n"
        help_plz = '```' +  os.popen(toeval).read() + '```'
        ret_str += str(help_plz)
       # try:
      #  ret_str += str(os.system(toeval))
     #   except Exception as e:
         #   error = 1
            #ret_str = ('**Invalid** **expression** **format**')
       # if error == 0:
        msg.edit(ret_str)
       # else:
       #     msg.edit('**Invalid** **expression** **format**')
        #print(str(os.system(toeval)))
        
@app.on_message(filters.command("chlang", prefixes=".") & filters.me)
def chlang(_, msg):
    global tr_lang
    tr_lang = msg.text.split(".chlang ", maxsplit=1)[1]
    msg.edit('**Done!**')

@app.on_message(filters.command("translate", prefixes=".") & filters.me)
def trans_late(_, msg):
    #new_text = ''
    orig_text = msg.text.split(".translate ", maxsplit=1)[1]
    #new_text = translator.translate(orig_text, dest='ru')
    new_text = ts.google(orig_text, to_language=tr_lang)
    #print(tr_lang)
    ret_str = "**Original:**\n"
    ret_str += orig_text
    ret_str += '\n'
    ret_str += "**Translation:**\n"
    ret_str += str(new_text)
    #print(ret_str)
    msg.edit(ret_str)
# eval

newlang = 'en'

@app.on_message(filters.command("lang", prefixes=".") & filters.me)
def chlang(_, msg):
    global newlang
    newlang = msg.text.split(".lang ", maxsplit=1)[1]
    msg.edit('**Done!**')

@app.on_message(filters.command("t", prefixes=".") & filters.me)
def translate_mini(_, msg):
    orig_text = msg.text.split(".t", maxsplit=1)[1]
    new_text = ts.google(orig_text, to_language=newlang)
    msg.edit(new_text)

# 🪜
@app.on_message(filters.command("trap", prefixes=".") & filters.me)
def trap(_, msg):
    msg.edit("**It's a trap!**")
    
#eval

@app.on_message(filters.command("eval", prefixes=".") & filters.me)
def eva_l(_, msg):
        error = 0
        toeval = msg.text.split(".eval ", maxsplit=1)[1]
        toeval_edit = toeval
        toeval_edit = toeval.replace('**', '^^')
        ret_str = "**Expression:**\n"
        ret_str += toeval_edit
        ret_str += '\n'
        ret_str += "**Result**:\n"
        try:
            ret_str += str(eval(toeval))
        except Exception as e:
            error = 1
            #ret_str = ('**Invalid** **expression** **format**')
        if error == 0:
            msg.edit(ret_str)
        else:
            msg.edit('**Invalid** **expression** **format**')
            
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


# http://github.com/KonstDev/


@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def ping(_, msg):
    msg.edit('Pong!')


@app.on_message(filters.command("gh", prefixes=".") & filters.me)
def gh(_, msg):
    msg.edit('My github: http://github.com/KonstDev/')


@app.on_message(filters.command("tb", prefixes=".") & filters.me)
def type(_, msg):
    # orig_text = msg.text.split(".tb ", maxsplit=1)[1]
    # text = orig_text
    # tbp = "" # to be printed
    # typing_symbol = "▒"
    msg.edit('**тЯнОчКу** **Бы**')


@app.on_message(filters.command("tbspam", prefixes=".") & filters.me)
def tbspam(_, msg):
    n = int(msg.text.split(".tbspam", maxsplit=1)[1])
    for i in range(0, n):
        sleep(0.03)
        app.send_message(msg.chat.id, "Тяночку бы!")
    msg.edit("YES, CAPTAIN! SPAMMING " + str(n) + " TIMES")

@app.on_message(filters.command("piar", prefixes=".") & filters.me)
def mybots(_, msg):
    msg.edit('My bots: \n 1)@howpythonbot \n 2)@whatsciencebot \n 3)@wplangbot')


app.run()
