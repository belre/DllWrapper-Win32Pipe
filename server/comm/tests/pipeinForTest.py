import win32api, win32pipe, win32file
import win32con

import binascii

from time import sleep

#try:

__pipe_in__ = win32file.CreateFile(r'\\.\pipe\biassys_pipein', win32con.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, win32con.FILE_FLAG_OVERLAPPED, None)
#win32pipe.SetNamedPipeHandleState(__pipe_in__, win32pipe.PIPE_READMODE_MESSAGE, 65536, None)

#tmp = []
tmp = win32file.ReadFile(__pipe_in__, 4096  )[1].decode('utf-8')
#buffer = win32file.AllocateReadBuffer(4096)

sleep(5)

__pipe_in__.close()

print(tmp)
