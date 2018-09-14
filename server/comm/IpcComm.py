"""
IPCComm Module
"""
from . import IpcTransmitter
import json

class IpcComm:
    """
    プロセス間通信用の一般化コマンドクラスを表す。
    """

    # 現在取得したコマンドの情報。
    __command_name__ = None

    # 送信用のパイプハンドラ
    __transmit__handler = None

    # エラーコード
    __list_errormsg__ = {   
        0:"", 
        100: "Parameter is null.",
        101: "Request parameter is invalid."
    }


    def __init__(self, transmit_handler):
        """
        コマンド命令を初期化します。
        コマンド命令ごとに出力用のハンドラを持たせる必要があります。

        Arguments:
            transmit_handler {IpcTransmitter} -- 出力用ハンドラ
        """
        self.__transmit_handler__ = transmit_handler


    def Execute(self, commname, jsonreqparam, state):
        """
        jsonmsgに従ってコマンドを実行します。
            :param self: 
            :param jsonmsg: クライアントから到達したJSONメッセージ
        """ 

        # JSONを読み込む。
        try:
            reqparam = json.loads(jsonreqparam)
        except json.decoder.JSONDecodeError:
            reqparam = None

        # 現在のコマンド名を確保する。
        # 非通知命令等で受信に対して送信するパケットが1対1ではないので、
        # 常に上位クラスがコマンド名を送れるようにする。
        self.__command_name__ = commname

        execret = self.__ExecuteProcedures__(reqparam, state)
        execrep = self.__ReplyToRequest__(reqparam, execret, state)
        
        return execrep
    
    def __ExecuteProcedures__(self, jsonreqparam, state):
        return 0

    def __ReplyToRequest__(self, jsonreqparam, execret, state):
        return 0

    def __SendReply__(self, commparam):
        return self.__transmit_handler__.SendByBlocking(self.__command_name__, "reply", commparam)


    def __SendNotify__(self, commparam):
        return self.__transmit_handler__.SendByBlocking(self.__command_name__, "notify", commparam)



class IpcState:
    """
    プロセス間通信における次状態を表します。
    """
    ipc_nextstateparam = {}
    
    def __init__ (self):
        self.ipc_nextstateparam = {}

