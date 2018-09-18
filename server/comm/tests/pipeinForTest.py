import win32api, win32pipe, win32file


__pipe_in__ = win32pipe.CreateNamedPipe(r'\\.\pipe\biassys_pipein', win32pipe.PIPE_ACCESS_INBOUND, win32pipe.PIPE_WAIT | win32pipe.PIPE_TYPE_BYTE, 1, 65536, 0, 10000, None)
win32pipe.ConnectNamedPipe(__pipe_in__)


win32pipe.DisconnectNamedPipe(__pipe_in__)
__pipe_in__.close()



