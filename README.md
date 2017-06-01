# TOC Project 2017 - GameBot

## How to run this code
use 'ngrok' as a proxy

```sh
./ngrok http 5000
```

After that,'ngrok' would generate a https URL.

set `WEBHOOK_URL`(in app.py) to `your-https-URL/hook`

And then, run the server

```sh
python3 app.py
```

ChatBot URL:https://telegram.me/TOC_ChatBot

## How to interact with chatbot
一開始的state 都是 `user`
有三種指令:
#### 你是誰?
輸入"你是誰?"之後，Bot會回應，介紹自己在幹嘛，狀態會回到`user`

#### 圈圈叉叉
輸入"圈圈叉叉"後，就可以與Bot玩圈圈叉叉，Bot會先問你要先攻還後攻，選擇之後就可以開始遊戲，選擇先攻的代表圈圈，後攻是叉叉。輸入"左上""上""右上""左""中""右""左下""下""右下"九個位子來選擇，你與Bot會輪流下，一直到比賽分出勝負。而比賽分出勝負後會問你是否要再玩一次，輸入yes的話就可以再玩一次，輸入no的話就會回到`user`的狀態
#### 猜拳
輸入"猜拳"之後，就可以與Bot玩猜拳，Bot會先問出什麼拳，你可以選擇出"剪刀","石頭","布"三種，輸入其中一種後，Bot也會隨機出一種拳，並且公布勝負，結束之後會問你是否要再玩一次，輸入yes的話就可以再玩一次，輸入no的話就會回到`user`的狀態
