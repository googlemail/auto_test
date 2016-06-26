import win32api,win32con,win32gui
import time
import sys
import psutil
import requests
VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0,
    ':':'zuhe'}

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename


def key_input(str=''):

    for c in str:
        print(c)
        if c == ':':
            win32api.keybd_event(VK_CODE['left_shift'],0,0,0)
            win32api.keybd_event(VK_CODE[';'],0,0,0)
            win32api.keybd_event(VK_CODE[';'],0,win32con.KEYEVENTF_KEYUP,0)
            win32api.keybd_event(VK_CODE['left_shift'],0,win32con.KEYEVENTF_KEYUP,0)
        else:
            time.sleep(0.01)
            win32api.keybd_event(VK_CODE[c],0,0,0)
            win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
            time.sleep(0.01)

def check(jubing):
    (left,top,right,bottom) = win32gui.GetWindowRect(jubing)

    win32api.SetCursorPos((left+(right-left)//2,top+(bottom-top)//2)) #光标定位
    time.sleep(0.5)


    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.05)
    time.sleep(1.5)

def find_idxSubHandle(pHandle, winClass, index=0):
    assert type(index) == int and index >= 0
    handle = win32gui.FindWindowEx(pHandle, 0, winClass[0], winClass[1])
    while index > 0:
        handle = win32gui.FindWindowEx(pHandle, handle, winClass[0], winClass[1])
        index -= 1
    return handle


def find_subHandle(pHandle, winClassList):
    assert type(winClassList) == list
    if len(winClassList) == 1:
        return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
    else:
        pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        return find_subHandle(pHandle, winClassList[1:])
class GenWindow():
    def __init__(self, leiming,biaoti = None):
        self.Mhandle = win32gui.FindWindow(leiming, biaoti)
    def jubing(self,findlist):
        handle = find_subHandle(self.Mhandle, findlist)
        print("%x" % (handle))
        return handle


#---------------------------------
win32api.WinExec('C:\\Users\\Administrator\\Downloads\\1.exe')
#------------------------------------------
qq = FaceGenWindow("TSelectLanguageForm")
jubin = qq.jubing([(["TNewButton",'确定'], 0),])
check(jubin)
qq = FaceGenWindow("TWizardForm")
jubin = qq.jubing([(["TNewButton",'下一步(&N) >'], 0),])
check(jubin)
#---------------------
qq = FaceGenWindow("#32770 (对话框)")
jubin = qq.jubing([(["Button",'确定'], 0),])
check(jubin)
time.sleep(1.5)
check(jubin)
#-------------------
qq = FaceGenWindow("TWizardForm")
jubin = qq.jubing([(["TNewNotebookPage",''], 0),(["TEdit",''], 0),])
check(jubin)
key_input(str='e:\\edo6')
time.sleep(1.5)
jubin = qq.jubing([(["TNewButton",'下一步(&N) >'], 0),])
check(jubin)
jubin = qq.jubing([(["TNewButton",'下一步(&N) >'], 0),])
check(jubin)
jubin = qq.jubing([(["TNewButton",'下一步(&N) >'], 0),])
check(jubin)

#-------------------
qq = FaceGenWindow("#32770 (对话框)")
jubin = qq.jubing([(["Button",'确定'], 0),])
check(jubin)
#-----------------------
qq = FaceGenWindow("TWizardForm")
jubin = qq.jubing([(["TNewButton",'安装(&I)'], 0),])
check(jubin)
#-----------------------

##filename = sys.argv(1)
##url = "hettp://wwww.hao123.com/" + filename
##download_file(url)
##win32api.WinExec(filename)
##qq =GenWindow('MsiDialogCloseClass','ActiveState ActivePython 3.4.3.2 (64-bit) Setup')
##jubin = qq.jubing([(["RichEdit20W",''], 0),])
##check(jubin)
##key_input(str='d:\\python34\\www')
##jubin = qq.jubing([(["Button",'OK'], 0),])
##check(jubin)
##
##r = requests.get('http://github.com', timeout=0.001)
##print(r.text)
##
##allfuwu = ['wo','oc']
##live = []
##for fuwu in allfuwu:
##    r = requests.get('http://127.0.0.1/{}'.format(fuwu), timeout=5)
##    if r.status == '200':
##        live.append(fuwu)
##
##all_jincheng = {}
##for proc in psutil.process_iter():
##    alljincheng[proc.name()] = proc.cmdline()
##
##for one_jincheng in alljincheng.keys():
##    if one_jincheng in alljincheng:
##        live.append(one_jincheng)
