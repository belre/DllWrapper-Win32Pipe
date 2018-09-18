import unittest
import IpcCommSysCtrl

from time import sleep

import IpcComm
import IpcTransmitter

import json

class CommCheckifTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_IpcReceiver_0101(self):
        """
        テストケース No.101　checkifコマンド
        """

        # transmitter生成
        print("出力パイプを生成してください。")
        trans_obj = IpcTransmitter.IpcOutHandler()
        trans_obj.Initialize()

        checkif_obj = IpcCommSysCtrl.IpcCommCheckif(trans_obj)
        
        print("101-2")
        state = IpcComm.IpcState()
        checkif_obj.Execute("checkif", 100, json.dumps({"text":"Hello World"}), state)


        print("101-3")
        state = IpcComm.IpcState()
        checkif_obj.Execute("checkif", 1000, json.dumps({"text":""}), state)

        print("101-4")
        state = IpcComm.IpcState()
        checkif_obj.Execute("checkif", 4000, json.dumps({"text":"ゴッドファザー"}), state)




        sleep(10)

        trans_obj.Finalize()





    def tearDown(self):
        pass








#cd D:\SVN\SampleProject\TestOkui\trunk\Project\BOE\Python\src\public\DllWrapper-Win32Pipe\server\comm
#python -m unittest tests.IpcTransmitterTest
#python -m unittest tests.IpcCommTest
#python -m unittest tests.IpcInCallbackHandlerTest
#python -m unittest tests.IpcCommSysCtrlTest