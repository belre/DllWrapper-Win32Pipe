"""
Module no docstring
"""

class IpcComm():


    def Execute(self, jsonmsg):
        """
        docstring here
            :param self: 
            :param jsonmsg: クライアントから到達したJSONメッセージ
        """

        print(jsonmsg)





val = IpcComm()
val.Execute("Test")
