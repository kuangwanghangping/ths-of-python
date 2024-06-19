from ctypes import *

import psutil
import win32api

import exehandle

FAGE_READWRITE = 0x04  # 偏移地址：0x04的意思就是：在空间上偏移4个内存单元
PROCESS_ALL_ACCESS = 0x001F0FFF
VIRTUAL_MEN = (0x1000 | 0x2000)

kernel32 = windll.kernel32
user32 = windll.user32


def ths_prc_hwnd():
    pl = psutil.pids()
    for pid in pl:
        # 进程id 获取进程名 转化为小写
        if psutil.Process(pid).name().lower() == 'hexin.exe':
            # isinstance() 函数来判断一个对象是否是一个已知的类型 pid 是 int类型
            if isinstance(pid, int):
                # 打开一个已存在的进程对象hexin.exe，并返回进程的句柄
                ths_process_hwnd = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))  # 申请内存所在的进程句柄
                return ths_process_hwnd


def bytes_16(dec_num, code):
    ascii_char = chr(dec_num)  # 将整数转换为对应的ASCII字符
    codex = ascii_char + str(code)
    # 将Python字符串转换为bytes类型
    bytes_codex = codex.encode('ascii', 'ignore')
    return bytes_codex


def ths_convert_code(code):
    '''
    代码转换
    :param code:
    :return:
    '''
    # 上海，深圳股票判断;
    if str(code)[0] == '6':
        # 将16进制数转换为整数
        dec_num = int('11', 16)
        bytes_codex = bytes_16(dec_num, code)
    # 11开头的可转债
    elif str(code).startswith('11'):
        # 将16进制数转换为整数
        dec_num = int('13', 16)
        bytes_codex = bytes_16(dec_num, code)
    # 12开头的可转债
    elif str(code).startswith('12'):
        # 将16进制数转换为整数
        dec_num = int('23', 16)
        bytes_codex = bytes_16(dec_num, code)
    else:
        # 将16进制数转换为整数
        dec_num = int('21', 16)
        bytes_codex = bytes_16(dec_num, code)
    return bytes_codex


def send_code_message(code, exe):
    # 同花顺进程句柄
    ths_process_hwnd = ths_prc_hwnd()
    # 用kerne132.VirtualAllocEx在目标进程开辟内存空间(用于存放数据)
    # 在指定进程的虚拟地址空间中保留、提交或更改内存区域的状态。 函数将它分配的内存初始化为零。
    argv_address = kernel32.VirtualAllocEx(ths_process_hwnd, 0, 8, VIRTUAL_MEN, FAGE_READWRITE)
    bytes_str = ths_convert_code(code)
    # 用kerne132.WriteProcessMemory在目标进程内存空间写入数据
    kernel32.WriteProcessMemory(ths_process_hwnd, argv_address, bytes_str, 7, None)
    # 同花顺窗口句柄
    ths_handle = exehandle.get_handle(exe)
    win32api.SendMessage(ths_handle, int(1168), 0, argv_address)
if __name__ == '__main__':
    # 让同花顺切换到股票代码
    send_code_message('000006', 'hexin.exe')
