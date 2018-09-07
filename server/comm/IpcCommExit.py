from . import IpcTransmitter
from . import IpcComm
import json


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

    def __ReplyToRequest__(self, reqparam):
        """
        レスポンスとして返却します。
            :param self: 
            :param jsonparam: 
        """   
        
        # レスポンス用の文字列を発行
        retval = 0
        jsonresparam = json.dumps({ "ret" : retval, 
                                    "message" : super().__list_errormsg__[retval]
                                    })
        print(jsonresparam)
        
        if( self.__transmit_handler__.IsInitialized() == True):
            self.__SendReply__(jsonresparam)

        return 100




