import io,win32file,win32pipe, win32api
import binascii
import time
import json



# Pipe in
_pipe_in_ = win32pipe.CreateNamedPipe(r'\\.\pipe\biassys_pipein', win32pipe.PIPE_ACCESS_OUTBOUND, win32pipe.PIPE_WAIT | win32pipe.PIPE_TYPE_BYTE, 1, 4096, 0, 10000, None)
ret1 = win32pipe.ConnectNamedPipe(_pipe_in_)

# Pipe out
_pipe_out_ = win32pipe.CreateNamedPipe(r'\\.\pipe\biassys_pipeout', win32pipe.PIPE_ACCESS_INBOUND, win32pipe.PIPE_WAIT | win32pipe.PIPE_TYPE_BYTE, 1, 4096, 0, 10000, None)
ret2 = win32pipe.ConnectNamedPipe(_pipe_out_)

cnt = 0
while 1:


    print("Already written")
    revdata = win32file.ReadFile(_pipe_out_, 4096)
    req_jsonobj = json.loads(revdata[1].decode('utf-8'))

    print("Command>" + format(req_jsonobj['command']))
    print("Parameter>" + format(req_jsonobj['param']))

    jsonmsg = json.dumps({'command':req_jsonobj['command'], 'seqNo': cnt, 'type': 'reply', 'param' : json.dumps({'text' : 'Hello World'}, ensure_ascii=False) }, ensure_ascii=False)
    data = jsonmsg.encode('utf-8')
    win32file.WriteFile(_pipe_in_, data)

    if(format(req_jsonobj['command']) == 'exit' ):
        break
    
    cnt = cnt + 1








win32pipe.DisconnectNamedPipe(_pipe_out_)
_pipe_out_.close()

win32pipe.DisconnectNamedPipe(_pipe_in_)
_pipe_in_.close()





