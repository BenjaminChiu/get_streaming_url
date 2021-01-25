import time

import win32api
import win32gui
import win32process
import win32clipboard as cp
import win32con
# 针对本机的potplayer位置，另外修改potPlay打开链接 这个选项的快捷键为F4；
# 设置默认使用剪切板中的地址
URL_POTPLAYER = 'C:\\Program Files\\PotPlayer\\PotPlayerMini64.exe'

class PotPlayer():

    def __init__(self, stream_url):
        self.pot_url = URL_POTPLAYER
        self.stream_url = stream_url


    def clipboard(self):
        # 复制到剪切板
        # SetClipboardData方法向剪贴板写入数据，后面两个参数，第一个表示数据类型，
        # 建议使用win32con.CF_UNICODETEXT，这样基本可以原样输出我们传入的数据
        # 如果使用win32con.CF_TEXT:输出的是字节码~很别扭
        # 注意！！！如果需要同时写入再获取内容，数据类型这个参数一定是使用一样的
        cp.OpenClipboard()
        cp.SetClipboardData(win32con.CF_UNICODETEXT, self.stream_url)  # 向剪贴板中写入数据
        cp.CloseClipboard()


    def start_pot(self):
        # win32api.ShellExecute(0, 'open', 'C:\Program Files\PotPlayer\PotPlayerMini64.exe', '', '', 1)  简单的打开，不返回任何东西
        handle = win32process.CreateProcess(self.pot_url,
                                            '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,
                                            win32process.STARTUPINFO())

        # win32api.SendMessage(handle[0], win32con.WM_KEYDOWN, win32con.VK_CONTROL, 0)
        # win32api.SendMessage(handle[0], win32con.KEYEVENTF_KEYUP, 85, 0)

        time.sleep(1.1)     # 第一次启动内存命中率为0，启动较慢 0.78秒等待启动potPlay

        win32api.keybd_event(win32con.VK_F4, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        time.sleep(0.1)
        # win32api.keybd_event(85, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(win32con.VK_F4, 0, win32con.KEYEVENTF_KEYUP, 0)

        time.sleep(0.18)    # 等待弹窗

        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        time.sleep(0.1)
        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)

    def run(self):
        self.clipboard()
        self.start_pot()