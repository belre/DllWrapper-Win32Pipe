"""
Ipc Transmitter Module
"""

class IpcOutHandler:

    __is_initialize__ = False               # 初期化されたかどうか
    __is_finalize__ = False                 # 破棄されたかどうか

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
            self.__is_initialize__ = True

    def Finalize(self):
        """
        出力パイプを破棄します。
            :param self: 
        """
        if self.__is_initialize__ and not(self.__is_finalize__):
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

    def SendByBlocking(self, jsonmsg):
        sendres = 0
        return 0


