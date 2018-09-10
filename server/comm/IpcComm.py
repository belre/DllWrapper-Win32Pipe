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


    def Execute(self, commname, jsonreqparam):
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

        execret = self.__ExecuteProcedures__(reqparam)
        nextstate = self.__ReplyToRequest__(reqparam, execret)
        
        """
        # JSON文字列の状態を決定する。
        nextstate = 0
        if reqmsg == None:
            nextstate = 1
        elif self.__json_req_key_seqNo__ not in reqmsg or self.__json_req_key_command__ not in reqmsg or self.__json_req_key_param__ not in reqmsg:
            nextstate = 1
        elif reqmsg[self.__json_req_key_seqNo__] == None or reqmsg[self.__json_req_key_command__] == None:
            nextstate = 1
        else:
            nextstate = self.__ReplyToRequest__(reqmsg[self.__json_req_key_param__])
        """
        return nextstate
    
    def __ExecuteProcedures__(self, jsonreqparam):
        return 0

    def __ReplyToRequest__(self, jsonreqparam, execret):
        return 0

    def __SendReply__(self, commparam):
        return self.__transmit_handler__.SendByBlocking(self.__command_name__, "reply", commparam)


    def __SendNotify__(self, commparam):
        return self.__transmit_handler__.SendByBlocking(self.__command_name__, "notify", commparam)




