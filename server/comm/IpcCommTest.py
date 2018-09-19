#from . import IpcTransmitter
from comm import IpcComm
import json



class IpcTest(IpcComm.IpcComm):
    TestComNo = 0


    def __init__(self, no):
        """
        コマンド命令を初期化します。
        コマンド命令ごとに出力用のハンドラを持たせる必要があります。

        Arguments:
            transmit_handler {IpcTransmitter} -- 出力用ハンドラ
        """
        self.TestComNo = no

    def __ReplyToRequest__(self, reqparam, execret, state):
        """
        レスポンスとして返却します。
            :param self: 
            :param jsonparam: 
        """   
        print("This is TestCom" + str(self.TestComNo))
        print("Reqparam:" + reqparam["text"])
        return 0

