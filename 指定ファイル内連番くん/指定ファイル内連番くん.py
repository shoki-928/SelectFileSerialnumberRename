import os
import glob
import datetime
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText
import time

count_num = 1

layout = [
    [sg.Text("ファイル名")],
    [sg.InputText(key="-FNAME-",size=(20,1))],
    [sg.Text("出力例：(ファイル名)_(番号).(拡張子)")],
    [sg.Combo(["名前順", "作成順"], key="-IF-", default_value="並び替え方法", size=(12,1))],
    [sg.FolderBrowse("フォルダ選択"), sg.InputText(key="-FOLDER-")],
    [sg.Button("実行", key="-START-")],
    [sg.Output(size=(100, 5), key='-MULTILINE-')],
]

window = sg.Window("指定ファイル内連番くん", layout, size=(500, 250))


while True:
    event, values = window.read()
    if event == "-START-":
        files = glob.glob(values["-FOLDER-"] + '/*')
        if values["-IF-"] == "名前順":
            if values["-FNAME-"] == "":
                file_name = values["-FOLDER-"]
                folder_name = file_name.split("/")
                for file in files:
                    time.sleep(0.1)
                    zero_i = "{0:03d}".format(count_num)
                    name, ext = os.path.splitext(file)
                    new_file = values["-FOLDER-"] + '/' + folder_name[-1] + '_' + zero_i + ext
                    os.rename(file, new_file)
                    print(new_file)
                    count_num += 1
                count_num = 1
            else:
                for file in files:
                    time.sleep(0.1)
                    zero_i = "{0:03d}".format(count_num)
                    name, ext = os.path.splitext(file)
                    new_file = values["-FOLDER-"] + '/' + values["-FNAME-"] + '_' + zero_i + ext
                    os.rename(file, new_file)
                    print(new_file)
                    count_num += 1
                count_num = 1
                print("処理が終了しました。")


        if values["-IF-"] == "作成順":
            files = glob.glob(values["-FOLDER-"] + '/*')
            if values["-FNAME-"] == "":
                file_name = values["-FOLDER-"]
                folder_name = file_name.split("/")
                for file in files:
                    time.sleep(0.1)
                    name, ext = os.path.splitext(file)
                    ctime = os.path.getctime(file)
                    ftime = datetime.datetime.fromtimestamp(ctime)
                    fname = ftime.strftime('%Y.%m.%d-%H.%M.%S.%f')
                    new_file = values["-FOLDER-"] + '/' + fname + ext
                    os.rename(file, new_file)
                    print(new_file)
                    files = glob.glob(values["-FOLDER-"] + '/*')
                for file in files:
                    time.sleep(0.1)
                    zero_i = "{0:03d}".format(count_num)
                    name, ext = os.path.splitext(file)
                    new_file = values["-FOLDER-"] + '/' + folder_name[-1] + '_' + zero_i + ext
                    os.rename(file, new_file)
                    print(new_file)
                    count_num += 1
                count_num = 1
                print("処理が終了しました。")
            else:
                for file in files:
                    time.sleep(0.1)
                    name, ext = os.path.splitext(file)
                    ctime = os.path.getctime(file)
                    ftime = datetime.datetime.fromtimestamp(ctime)
                    fname = ftime.strftime('%Y.%m.%d-%H.%M.%S.%f')
                    new_file = values["-FOLDER-"] + '/' + fname + ext
                    os.rename(file, new_file)
                    print(new_file)
                files = glob.glob(values["-FOLDER-"] + '/*')
                for file in files:
                    time.sleep(0.1)
                    zero_i = "{0:03d}".format(count_num)
                    name, ext = os.path.splitext(file)
                    new_file = values["-FOLDER-"] + '/' + values["-FNAME-"] + '_' + zero_i + ext
                    os.rename(file, new_file)
                    print(new_file)
                    count_num += 1
                count_num = 1
                print("処理が終了しました。")

    if event == sg.WIN_CLOSED:
        break