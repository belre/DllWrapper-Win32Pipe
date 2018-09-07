"""
Ipc Transmitter Module
"""

import win32api, win32pipe, win32file
import json


class IpcOutHandler:
    __pipe_out__ = None                     # パイプ(内部保持)
    __is_initialize__ = False               # 初期化されたかどうか
    __is_finalize__ = False                 # 破棄されたかどうか

    __seqno_counter__ = 0                   # seqNo用のカウンタ

    def __init__(self):
        """ コンストラクタです。
        """
        __is_initialize__ = False
        __is_finalize__ = False


    def Initialize(self):
        """
        出力パイプを初期化します。
            :param self: 
        """
        if(not(self.__is_initialize__) and not(self.__is_finalize__)):
            # パイプ作成
            self.__pipe_out__ = win32pipe.CreateNamedPipe(r'\\.\pipe\biassys_pipein', win32pipe.PIPE_ACCESS_OUTBOUND, win32pipe.PIPE_WAIT | win32pipe.PIPE_TYPE_BYTE, 1, 4096, 0, 10000, None)
            
            
            if self.__pipe_out__ != None:
                if win32pipe.ConnectNamedPipe(self.__pipe_out__) == 0:            # パイプ接続確認
                    self.__is_initialize__ = True

    def Finalize(self):
        """
        出力パイプを破棄します。
            :param self: 
        """
        if self.__is_initialize__ and not(self.__is_finalize__):
            if self.__pipe_out__ != None:
                # パイプ閉じる
                win32pipe.DisconnectNamedPipe(self.__pipe_out__)
                self.__pipe_out__.close()             
                
                self.__is_finalize__ = True

    def IsInitialized(self):
        """
        出力パイプが初期化されているかを表します。
            :param self: 
        """
        return self.__is_initialize__

    def IsFinalized(self):
        """
        出力パイプが破棄されているかを表します。
            :param self: 
        """   
        return self.__is_finalize__

    def SendByBlocking(self, commname, commtype, commparam):
        # メッセージ生成
        jsonmsg = json.dumps({'command':commname, 'seqNo': self.__seqno_counter__, 'type': commtype, 'param' : commparam}, ensure_ascii=False)
        self.__seqno_counter__ = self.__seqno_counter__ + 1

        # データ書込み処理
        recvjsonmsg = win32file.WriteFile(self.__pipe_out__, jsonmsg.encode('utf-8'))
        return 0



if __name__ == '__main__':
    print("Hello")

