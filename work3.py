import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名前作成")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

names = []  # 名前を保存するリストを初期化


def button_action():
    names.append(entry1.get())  # 入力フィールドから名前をnamesリストに追加

    # name_out = ""  # 追加した名前を表示する用の文字列を初期化
    # forを使用してリストの各名前の後ろに改行コードを入れてname_outに結合
    # for name in names:
    #     name_out += f"{name}\n"

    name_out = "\n".join(names)

    label2.config(text=f"{name_out}\n")  # 　結果をラベルに設定して表示


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)
# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
