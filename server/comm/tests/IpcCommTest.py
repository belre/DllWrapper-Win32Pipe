import unittest

from comm import IpcComm
from comm import IpcTransmitter

import json

class IpcCommTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_IpcCommTest_0011(self):
        """
        テストケースNo.11
        """

        ### No.11-1 コンストラクタ生成 ###
        try:
            com_obj = IpcComm.IpcComm(None)
            assert(True)
        except:
            self.fail()

        ### No.11-2 正常メッセージ伝送 ###
        state = IpcComm.IpcState()
        try:
            assert( com_obj.Execute("hoge", 5, json.dumps({"test1": 3, "test2":"str"}), state) == 0)
        except:
            self.fail()

        ### No.11-3 コマンドがnull ###
        try:
            assert( com_obj.Execute(None, 5, json.dumps({"test1": 3, "test2":"str"}), state) != 0)
        except:
            self.fail()
        
        ### No.11-4 パラメータがJSON形式になっていない ###
        try:
            assert( com_obj.Execute("hoge", 5, "ABCDEFGHI", state) != 0)
        except:
            self.fail()

        ### No.11-5 パラメータがnullになっている ###
        try:
            assert( com_obj.Execute("hoge", 5, None, state) != 0)
        except:
            self.fail()

        ### No.11-6 seqNo<0 ###
        try:
            assert( com_obj.Execute("hoge", -5, json.dumps({"test1": 3, "test2":"str"}), state) != 0)
        except:
            self.fail()

        ### No.11-7 stateがnull ###
        try:
            assert( com_obj.Execute("hoge", -5, json.dumps({"test1": 3, "test2":"str"}), None) != 0)
        except:
            self.fail()


        ### No.11-8 parameter=""(空白) ###
        state = IpcComm.IpcState()
        try:
            assert( com_obj.Execute("hoge", 5, "", state) == 0)
        except:
            self.fail()



    def tearDown(self):
        pass
