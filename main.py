# -*- coding:utf8 -*-

# discord.pyを読み込む
import discord

import os
import requests

import config

# ログを取得
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ファイルをダウンロードする関数
def download(title, url):
    try:
        # urlを取得
        r = requests.get(url)
        # openの中で保存先のパス（ファイル名の指定）
        with open("dis_file/" + title, mode='wb') as f:
            f.write(r.content)
    except requests.exceptions.RequestException as err:
        print(err)

# 自分のBOTのアクセストークン
TOKEN = config.TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作するイベント
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージが表示された時
@client.event
async def on_message(message):
    # メッセージ送信者がBOTだった場合は無視する
    if message.author.bot:
        return
        
    # ifで分岐 パスコード入力があるかどうか
    try:
        # 投稿されたファイルの詳細を取得
        file = message.attachments[0]

        # ファイル保存
        download(file.filename, file.url)

        # ダウンロード完了
        await message.channel.send('ダウンロード完了')

            # パスワード入力がなかった場合エラー
    except FileNotFoundError:
        await message.channel.send('フォルダがありません')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)