import comm
import comm.private

from time import sleep

### コマンド-レスポンス構造定義 ###
# 出力側パイプの作成
outhandle = comm.IpcTransmitter.IpcOutHandler()

# 命令割り当て
comm_list = comm.private.InternalFunc.Initialize(outhandle)
comm_list["checkif"] = comm.IpcCommSysCtrl.IpcCommCheckif(outhandle)
comm_list["exit"] = comm.IpcCommSysCtrl.IpcCommExit(outhandle)

# 入力側パイプの作成
inhandle = comm.IpcReceiver.IpcInCallbackHandler(comm_list)

### ハンドラ初期化 ###
outhandle.Initialize()

if outhandle.IsInitialized():
    #print("outhandle Initialized")
    pass
    inhandle.Initialize()
    if inhandle.IsInitialized():
        #print("Very good")
        pass
    else:
        #print("Finalization failed.")
        pass
else:
    pass
    #print("Initialization failed.")


state = comm.IpcComm.IpcState()
while inhandle.RecvByBlocking(state) <= 0:
    pass
    #print("Executed RecvBlocking")

#print("Exit")

sleep(3)

### ハンドラ破棄 ###
inhandle.Finalize()
outhandle.Finalize()


