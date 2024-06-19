import win32api
import win32gui
import win32process
import psutil
import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


def get_pids(pname):
    # print(pname)
    pids = []
    for proc in psutil.process_iter():
        if pname in proc.name():
            pids.append(proc.pid)
    # print(pids)
    return pids


def get_handles(pid):
    def callback(hwnd, handles):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

            if found_pid == pid:
                handles.append(hwnd)
            return True

    handles = []
    win32gui.EnumWindows(callback, handles)
    return handles


def get_handle(pname):
    pids = get_pids(pname)
    for pid in pids:
        handles = get_handles(pid)
        # print(handles)
        for hwnd in handles:
            if IsWindowVisible(hwnd):
                return hwnd


if __name__ == '__main__':
    # handle = get_handle('tdxw.exe')
    handle = get_handle('hexin.exe')
    print(handle)
