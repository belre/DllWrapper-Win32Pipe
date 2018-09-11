"""
Ipc Receiver Module
"""
import win32api, win32pipe, win32file
import json
import binascii

class IpcInCallbackHandler:
    __pipe_in__ = None                  # パイプ(内部保持)

    __is_initialize__ = False           # 初期化されたかどうか
    __is_finalize__ = False             # 破棄されたかどうか
    __comm_list__ = None                # コマンド一覧表

    def __init__(self, comm_list):
        """ コンストラクタです。
        """
        self.__is_initialize__ = False
        self.__is_finalize__ = False
        self.__comm_list__ = comm_list


    def Initialize(self):
        """
        入力パイプを初期化します。
            :param self: 
        """
        if(not(self.__is_initialize__) and not(self.__is_finalize__)):
            # パイプ作成
            self.__pipe_in__ = win32pipe.CreateNamedPipe(r'\\.\pipe\biassys_pipeout', win32pipe.PIPE_ACCESS_INBOUND, win32pipe.PIPE_WAIT | win32pipe.PIPE_TYPE_BYTE, 1, 65536, 0, 10000, None)
            
            if self.__pipe_in__ != None:
                if win32pipe.ConnectNamedPipe(self.__pipe_in__) == 0:            # パイプ接続確認
                    self.__is_initialize__ = True

    def Finalize(self):
        """
        入力パイプを破棄します。
            :param self: 
        """
        if self.__is_initialize__ and not(self.__is_finalize__):
            if self.__pipe_in__ != None:
                # パイプ閉じる
                win32pipe.DisconnectNamedPipe(self.__pipe_in__)
                self.__pipe_in__.close()         

                self.__is_finalize__ = True

    def IsInitialized(self):
        """
        入力パイプが初期化されているかを表します。
            :param self: 
        """
        return self.__is_initialize__

    def IsFinalized(self):
        """
        入力パイプが破棄されているかを表します。
            :param self: 
        """   
        return self.__is_finalize__

    def RecvByBlocking(self, beforestate):
        """
        データを受信します。
            :param self: 
            :param jsonmsg:

            :return: 次の動作状態。>0ならばパイプ処理は終了します。 
        """   
        
        # データ受取処理
        recvjsonmsg = win32file.ReadFile(self.__pipe_in__, 4096)[1].decode('utf-8')

        # jsonへの変換
        recvmsg = json.loads(recvjsonmsg)

        # 命令が存在するかどうかを確認
        nextstate = 0
        if recvmsg['command'] in self.__comm_list__:
            # 命令実行
            nextstate = self.__comm_list__[recvmsg['command']].Execute(recvmsg['command'], recvmsg['param'], beforestate)

        return nextstate

    


if __name__ == '__main__':
    rec1 = IpcInCallbackHandler(None)
    rec1.Initialize()

    rec2 = rec1
    print(rec1.IsInitialized())
    print(rec2.IsInitialized())
    print(rec1.IsFinalized())
    print(rec2.IsFinalized())







