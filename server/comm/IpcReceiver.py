"""
Ipc Receiver Module
"""



class IpcInCallbackHandler:
    __is_initialize__ = False           # 初期化されたかどうか
    __is_finalize__ = False             # 破棄されたかどうか
    __comm_list__ = None

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
            self.__is_initialize__ = True

    def Finalize(self):
        """
        入力パイプを破棄します。
            :param self: 
        """
        if self.__is_initialize__ and not(self.__is_finalize__):
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

    def RecvByBlocking(self, jsonmsg):
        """
        データを受信します。
            :param self: 
            :param jsonmsg: 
        """   
        execstate = 0
        return execstate

    


if __name__ == '__main__':
    rec1 = IpcInCallbackHandler()
    rec1.Initialize()

    rec2 = rec1
    print(rec1.IsInitialized())
    print(rec2.IsInitialized())
    print(rec1.IsFinalized())
    print(rec2.IsFinalized())







