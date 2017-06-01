from transitions.extensions import GraphMachine
from random import *
choose_hand =''
choose_where=''
choose_order=''
draw=0
win=0
table=['   ','   ','   ','   ','   ','   ','   ','   ','   ']

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def askIntro(self,update):
        text=update.message.text
        return text=='你是誰?'

    def playCircleFork(self,update):
        text=update.message.text
        return text=='圈圈叉叉'

    def startCircleFork(self,update):
        text=update.message.text
        global choose_order
        global choose_where
        global table
        choose_order=text
        choose_where=''
        table=['   ','   ','   ','   ','   ','   ','   ','   ','   ']
        if text=='先攻':
            update.message.reply_text("棋盤:\n   |   |   \n   |   |   \n   |   |    ")
            return text=='先攻'
        elif text=='後攻':
            num=randint(0,8)
            table[num]='O'
            text1='棋盤:\n'+table[0]+'|'+table[1]+'|'+table[2]+'\n'+table[3]+'|'+table[4]+'|'+table[5]+'\n'+table[6]+'|'+table[7]+'|'+table[8]
            update.message.reply_text(text1)
            return text=='後攻'

    def chooseCircleFork(self,update):
        text=update.message.text
        global choose_where
        choose_where=text
        return choose_where==text

    def endCircleFork(self,update):
        global win
        global draw
        if win==1:
            update.message.reply_text("You Win!!")
            win=-1
            return True
        elif win==2:
            update.message.reply_text("You Lose!!")
            win=-1
            return True
        elif draw==9:
            update.message.reply_text("Draw!!")
            draw=-1
            return True

    def againCircleFork(self,update):
        text=update.message.text	
        if text=='no':
            self.go_back(update)
        elif text=='yes':
            return text=='yes'

    def play_mora(self,update):
        text=update.message.text
        return text=='猜拳'

    def chooseHand(self,update):
        text=update.message.text
        global choose_hand
        choose_hand=text
        return text == choose_hand

    def moraPlayAgain(self,update):
        text=update.message.text
        if text=='no':
            self.go_back(update)
        elif text=='yes':
            return text=='yes'

    def on_enter_intro(self,update):
        update.message.reply_text("我是GameBot,你可以選擇跟我玩猜拳或圈圈叉叉")
        self.go_back(update)

    def on_enter_circle_fork(self,update):
        update.message.reply_text("先攻或後攻?")

    def on_enter_circle_fork_start(self,update):
        global choose_where
        global choose_order
        global win
        global draw
        global table
        win=0
        if choose_where != '' and choose_order=='先攻':
            if choose_where=='左上':
                table[0]='O'
            elif choose_where=='上':
                table[1]='O'
            elif choose_where=='右上':
                table[2]='O'
            elif choose_where=='左':
                table[3]='O'
            elif choose_where=='中':
                table[4]='O'
            elif choose_where=='右':
                table[5]='O'
            elif choose_where=='左下':
                table[6]='O'
            elif choose_where=='下':
                table[7]='O'
            elif choose_where=='右下':
                table[8]='O'
            text1='棋盤:\n'+table[0]+'|'+table[1]+'|'+table[2]+'\n'+table[3]+'|'+table[4]+'|'+table[5]+'\n'+table[6]+'|'+table[7]+'|'+table[8]
            update.message.reply_text(text1)
            if table[0]!='   ' and table[0]==table[1] and table[1]==table[2]:
                win=1
            elif table[3]!='   ' and table[3]==table[4] and table[4]==table[5]:
                win=1
            elif table[6]!='   ' and table[6]==table[7] and table[7]==table[8]:
                win=1
            elif table[0]!='   ' and table[0]==table[3] and table[3]==table[6]:
                win=1
            elif table[1]!='   ' and table[1]==table[4] and table[4]==table[7]:
                win=1
            elif table[2]!='   ' and table[2]==table[5] and table[5]==table[8]:
                win=1
            elif table[0]!='   ' and table[0]==table[4] and table[4]==table[8]:
                win=1
            elif table[2]!='   ' and table[2]==table[4] and table[4]==table[6]:
                win=1
            draw=0
            for i in range(9):
                if table[i]!='   ':
                    draw=draw+1
            if win==1 or draw==9:
                self.end(update)
            if win==0 and draw!=9:
                num=randint(0,8)
                while table[num]!='   ':
                    num=randint(0,8)
                table[num]='X'
                text1='棋盤:\n'+table[0]+'|'+table[1]+'|'+table[2]+'\n'+table[3]+'|'+table[4]+'|'+table[5]+'\n'+table[6]+'|'+table[7]+'|'+table[8]
                update.message.reply_text(text1)
                if table[0]!='   ' and table[0]==table[1] and table[1]==table[2]:
                    win=2
                elif table[3]!='   ' and table[3]==table[4] and table[4]==table[5]:
                    win=2
                elif table[6]!='   ' and table[6]==table[7] and table[7]==table[8]:
                    win=2
                elif table[0]!='   ' and table[0]==table[3] and table[3]==table[6]:
                    win=2
                elif table[1]!='   ' and table[1]==table[4] and table[4]==table[7]:
                    win=2
                elif table[2]!='   ' and table[2]==table[5] and table[5]==table[8]:
                    win=2
                elif table[0]!='   ' and table[0]==table[4] and table[4]==table[8]:
                    win=2
                elif table[2]!='   ' and table[2]==table[4] and table[4]==table[6]:
                    win=2
                if win==2:
                    self.end(update)
        elif choose_where != '' and choose_order=='後攻':
            if choose_where=='左上':
                table[0]='X'
            elif choose_where=='上':
                table[1]='X'
            elif choose_where=='右上':
                table[2]='X'
            elif choose_where=='左':
                table[3]='X'
            elif choose_where=='中':
                table[4]='X'
            elif choose_where=='右':
                table[5]='X'
            elif choose_where=='左下':
                table[6]='X'
            elif choose_where=='下':
                table[7]='X'
            elif choose_where=='右下':
                table[8]='X'
            text1='棋盤:\n'+table[0]+'|'+table[1]+'|'+table[2]+'\n'+table[3]+'|'+table[4]+'|'+table[5]+'\n'+table[6]+'|'+table[7]+'|'+table[8]
            update.message.reply_text(text1)
            if table[0]!='   ' and table[0]==table[1] and table[1]==table[2]:
                win=1
            elif table[3]!='   ' and table[3]==table[4] and table[4]==table[5]:
                win=1
            elif table[6]!='   ' and table[6]==table[7] and table[7]==table[8]:
                win=1
            elif table[0]!='   ' and table[0]==table[3] and table[3]==table[6]:
                win=1
            elif table[1]!='   ' and table[1]==table[4] and table[4]==table[7]:
                win=1
            elif table[2]!='   ' and table[2]==table[5] and table[5]==table[8]:
                win=1
            elif table[0]!='   ' and table[0]==table[4] and table[4]==table[8]:
                win=1
            elif table[2]!='   ' and table[2]==table[4] and table[4]==table[6]:
                win=1
            if win==1:
                self.end(update)
            if win==0:
                num=randint(0,8)
                while table[num]!='   ':
                    num=randint(0,8)
                table[num]='O'
                text1='棋盤:\n'+table[0]+'|'+table[1]+'|'+table[2]+'\n'+table[3]+'|'+table[4]+'|'+table[5]+'\n'+table[6]+'|'+table[7]+'|'+table[8]
                update.message.reply_text(text1)
                if table[0]!='   ' and table[0]==table[1] and table[1]==table[2]:
                    win=2
                elif table[3]!='   ' and table[3]==table[4] and table[4]==table[5]:
                    win=2
                elif table[6]!='   ' and table[6]==table[7] and table[7]==table[8]:
                    win=2
                elif table[0]!='   ' and table[0]==table[3] and table[3]==table[6]:
                    win=2
                elif table[1]!='   ' and table[1]==table[4] and table[4]==table[7]:
                    win=2
                elif table[2]!='   ' and table[2]==table[5] and table[5]==table[8]:
                    win=2
                elif table[0]!='   ' and table[0]==table[4] and table[4]==table[8]:
                    win=2
                elif table[2]!='   ' and table[2]==table[4] and table[4]==table[6]:
                    win=2
                draw=0
                for i in range(9):
                    if table[i]!='   ':
                        draw=draw+1
                if win==2 or draw==9:
                    self.end(update)
	
    def on_enter_circle_fork_end(self,update):
        update.message.reply_text("Wanna play again?")

    def on_enter_mora(self,update):
        update.message.reply_text("請出拳")

    def on_enter_mora_end(self,update):
        choose=('剪刀','石頭','布')
        num=randint(0,2)
        update.message.reply_text(choose[num])
        global choose_hand
        if choose[num]==choose_hand:
            update.message.reply_text("Draw！！")
        elif num==0:
            if choose_hand=='石頭':
                update.message.reply_text("You are Winner!!")
            else:
                update.message.reply_text("You are Loser!!")
        elif num==1:
            if choose_hand=='布':
                update.message.reply_text("You are Winner!!")
            else:
                update.message.reply_text("You are Loser!!")
        elif num==2:
            if choose_hand=='剪刀':
                update.message.reply_text("You are Winner!!")
            else:
                update.message.reply_text("You are Loser!!")
        update.message.reply_text("Wanna play again?")

