
import unittest


from time import sleep

from comm import IpcTransmitter
from comm import IpcComm
from comm import IpcCommSysCtrl
#from .. import IpcComm
#from .. import IpcCommSysCtrl

import json

class CommCheckifTest(unittest.TestCase):
    trans_obj = None

    def setUp(self):
 
        print("入力パイプを生成してください。")
        self.trans_obj = IpcTransmitter.IpcOutHandler()
        self.trans_obj.Initialize()

    def test_CommCheckif_0101(self):
        """
        テストケース No.101　checkifコマンド
        """

        # コンストラクタ生成
        print("101-1")
        checkif_obj = None
        try:
            checkif_obj = IpcCommSysCtrl.IpcCommCheckif(self.trans_obj)
            assert(True)
        except:
            self.fail()

        print("101-2")
        state = IpcComm.IpcState()
        assert(checkif_obj.Execute("checkif", 100, json.dumps({"text":"Hello World"}), state)==0)

        print("101-3")
        assert(checkif_obj.Execute("checkif", 1000, json.dumps({"text":""}), state)==0)

        print("101-4")
        assert(checkif_obj.Execute("checkif", 4000, json.dumps({"text":"ゴッドファザー"}), state)==0)

        print("101-5")
        assert(checkif_obj.Execute("checkif", 8000, json.dumps({"text":"\"abcdefg\""}), state)==0)

        print("101-6")
        assert(checkif_obj.Execute("checkif", -1, json.dumps({"text":"\"abcdefg\""}), state)!=0)

        print("101-7")
        assert(checkif_obj.Execute("checkif", 1500, "text abcdefg", state)!=0)

        print("101-8")
        assert(checkif_obj.Execute("checkif", 2500, None, state)!=0)

        sleep(10)



    def tearDown(self):
        self.trans_obj.Finalize()


class CommExitTest(unittest.TestCase):
    trans_obj = None

    def setUp(self):
        print("入力パイプを生成してください。")
        self.trans_obj = IpcTransmitter.IpcOutHandler()
        self.trans_obj.Initialize()

    def test_CommExit_0111(self):
        print("111-1")
        checkif_obj = None
        try:
            checkif_obj = IpcCommSysCtrl.IpcCommExit(self.trans_obj)
            assert(True)
        except:
            self.fail()

        print("111-2")
        state = IpcComm.IpcState()
        assert(checkif_obj.Execute("exit", 101, "", state)>0)

        print("111-3")
        state = IpcComm.IpcState()
        assert(checkif_obj.Execute("exit", 102, "owarutte", state)<0)

        
        print("111-4")
        state = IpcComm.IpcState()
        assert(checkif_obj.Execute("exit", 103, json.dumps({"text":"hanamogera"}), state)>0)

        print("111-5")
        state = IpcComm.IpcState()
        assert(checkif_obj.Execute("exit", 104, None, state)<0)

        sleep(10)

    def tearDown(self):
        self.trans_obj.Finalize()




#python -m unittest tests.IpcTransmitterTest
#python -m unittest tests.IpcCommTest
#python -m unittest tests.IpcReceiverTest
#python -m unittest tests.IpcCommSysCtrlTest