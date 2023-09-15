import json
import pyperclip
from bardapi import Bard
from bardapi import BardCookies
import PySimpleGUI as sg

#Jsonファイルの読み込み（Macの場合こちらが上手くいった）
with open("bardcookie.json",'r') as f:
    cookie_dict = json.load(f)

try:
    #Macの場合クッキーをセットすると上手くいった
    BardCookies(cookie_dict = cookie_dict)
except Exception as e:
    print(e.args)
    #Windowsの場合、こちらが上手くいった
    bard = Bard(token_from_browser=True)

#Bardに質問を投げる関数
def BardRes(prompt):
    res = bard.get_answer(prompt)["content"]
    return res


#GUIのレイアウト部分
layout = [
    [sg.Text('BardAPIで答えを返すアプリです')],
    [sg.Text('質問を入力し送信ボタンを押してください')],
    [sg.InputText(key='prompt'),sg.Button('送信')],
    [sg.Output(size=(80,20), key='res')],
    [sg.Button("コピー",key="-cpy-"),sg.Button("終了",key="-exit-")],
    #[sg.Column([sg.Button("コピー",key="-cpy-"),sg.Button("終了",key="-exit-")],justification='c')],
]

#ウインドウを生成
win = sg.Window('Bardデスクトップ',layout,size=(600, 500),resizable=True)

#イベント処理のループ
while True:
    event, val = win.read()
    
    if event in ('Exit','Quit',None): break
    
    if event == '送信':
        res = BardRes(val['prompt'])
        win['res'].update(res)
        
    if event == '-cpy-':
        #クリップボードにコピー
        pyperclip.copy(win['res'].get())
        
    if event == '-exit-':
        break
    
#Windowを閉じる
win.close()