
import comm
from time import sleep

outhandle = comm.IpcTransmitter.IpcOutHandler()
inhandle = comm.IpcReceiver.IpcInCallbackHandler(None)

# ハンドラ初期化
outhandle.Initialize()

if outhandle.IsInitialized():
    print("outhandle Initialized")
    inhandle.Initialize();
    if inhandle.IsInitialized():
        print("Very good")
    else:
        print("Finalization failed.")


else:
    print("Initialization failed.")


# ハンドラ破棄
inhandle.Finalize()
outhandle.Finalize()




