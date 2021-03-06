#from . import IpcTransmitter
#from . import IpcComm

from comm import IpcTransmitter
from comm import IpcComm


import json


class IpcCommCheckif(IpcComm.IpcComm):
    """
    インタフェースチェックコマンドを表します。
    """

    __json_req_key_text__ = "text"

    def __init__(self, transmit_handler):
        """
        コマンド命令を初期化します。
        コマンド命令ごとに出力用のハンドラを持たせる必要があります。

        Arguments:
            transmit_handler {IpcTransmitter} -- 出力用ハンドラ
        """
        super().__init__(transmit_handler)

    def __ReplyToRequest__(self, reqparam, execret, state):
        """
        レスポンスとして返却します。
            :param self: 
            :param jsonparam: 
        """   
        # JSON文字列の状態を決定する。
        retval = 0
        textval = ""
        if reqparam == None:
            retval = 100
        elif self.__json_req_key_text__ not in reqparam:
            retval = 101
        else:
            retval = 0
            textval = reqparam[self.__json_req_key_text__]
        
        # レスポンス用の文字列を発行
        jsonresparam = json.dumps({ "ret" : retval, 
                                    "message" : super().__list_errormsg__[retval], 
                                    "text" : textval}, ensure_ascii=False)
        #print(jsonresparam)
        
        if( self.__transmit_handler__.IsInitialized() == True):
            self.__SendReply__(jsonresparam)

        return 0


class IpcCommExit(IpcComm.IpcComm):
    """
    終了コマンドを表します。
    """

    def __init__(self, transmit_handler):
        """
        コマンド命令を初期化します。
        コマンド命令ごとに出力用のハンドラを持たせる必要があります。

        Arguments:
            transmit_handler {IpcTransmitter} -- 出力用ハンドラ
        """
        super().__init__(transmit_handler)

    def __ReplyToRequest__(self, reqparam, execret, state):
        """
        レスポンスとして返却します。
            :param self: 
            :param jsonparam: 
        """   
        
        # レスポンス用の文字列を発行
        retval = 0
        jsonresparam = json.dumps({ "ret" : retval, 
                                    "message" : super().__list_errormsg__[retval]
                                    }, ensure_ascii=False)
        
        if( self.__transmit_handler__.IsInitialized() == True):
            self.__SendReply__(jsonresparam)

        return 100      





