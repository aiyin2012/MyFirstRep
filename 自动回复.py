import itchat
@itchat.msg_register(itchat.content.TEXT)  
def text_reply(msg):  
    message = msg['Text']  
    replay = u'Sir, 对方暂时无法进行交流'  
    if u'干什么' in message:  
        replay = u'对不起，你所联系的对方正在干大事ing'  
    elif u'生气' in message:  
        replay = u'忙完给你买好吃的呐(づ￣3￣)づ╭❤～'  
    elif u'好吧' in message:  
        replay = u'要乖乖的哦'  
    return replay
itchat.auto_login()
itchat.run()
