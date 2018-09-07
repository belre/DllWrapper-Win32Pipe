import comm
from time import sleep

### コマンド-レスポンス構造定義 ###
# 出力側パイプの作成
outhandle = comm.IpcTransmitter.IpcOutHandler()

# 命令割り当て
comm_list = {"checkif": comm.IpcCommCheckif.IpcCommCheckif(outhandle),
             "exit": comm.IpcCommExit.IpcCommExit(outhandle)}

# 入力側パイプの作成
inhandle = comm.IpcReceiver.IpcInCallbackHandler(comm_list)

### ハンドラ初期化 ###
outhandle.Initialize()

if outhandle.IsInitialized():
    print("outhandle Initialized")
    inhandle.Initialize()
    if inhandle.IsInitialized():
        print("Very good")
    else:
        print("Finalization failed.")
else:
    print("Initialization failed.")


while inhandle.RecvByBlocking() <= 0:
    print("Executed RecvBlocking")

print("Exit")

### ハンドラ破棄 ###
inhandle.Finalize()
outhandle.Finalize()





