"""
IPCComm Module
"""
import IpcTransmitter
import json

class IpcComm:
    """
    プロセス間通信用の一般化コマンドクラスを表す。
    """
    __list_errormsg__ = {   
        0:"", 
        100: "Parameter is null.",
        101: "Request parameter is invalid."
    }

    __json_req_key_seqNo__           = "seqNo"
    __json_req_key_command__         = "command"
    __json_req_key_param__           = "param"

    def __init__(self, transmit_handler):
        """
        コマンド命令を初期化します。
        コマンド命令ごとに出力用のハンドラを持たせる必要があります。

        Arguments:
            transmit_handler {IpcTransmitter} -- 出力用ハンドラ
        """
        self.__transmit_handler__ = transmit_handler


    def Execute(self, jsonreqmsg):
        """
        jsonmsgに従ってコマンドを実行します。
            :param self: 
            :param jsonmsg: クライアントから到達したJSONメッセージ
        """ 

        # JSONを読み込む。
        try:
            reqmsg = json.loads(jsonreqmsg)
        except json.decoder.JSONDecodeError:
            reqmsg = None

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

        return nextstate
    
    def __ExecuteProcedures__(self, jsonreqparam):
        return 0

    def __ReplyToRequest__(self, jsonreqparam):
        return 0


