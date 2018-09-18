import unittest
import IpcReceiver
import IpcException
import IpcComm
import IpcCommTest

from time import sleep

class IpcInCallbackHandlerTest(unittest.TestCase):


    
    def setUp(self):
        pass


    def test_IpcReceiver_0021(self):
        """
        テストケース No.21　コンストラクタ生成
        """

        ### No.21-1　コンストラクタ（コマンド定義）
        list00 = { "TestCom1" : IpcCommTest.IpcTest(1), "TestCom2" : IpcCommTest.IpcTest(2)}
        recv_obj = IpcReceiver.IpcInCallbackHandler(list00)


        ### No.21-2　コンストラクタ（コマンド未定義）
        self.assertRaises(IpcException.IpcCommInvalidException, lambda: IpcReceiver.IpcInCallbackHandler(None))

    @unittest.skipIf(True, 'debug')
    def test_IpcReceiver_0022(self):
        """
        テストケース No.22　パケット受信処理
        """
        list00 = { "TestCom1" : IpcCommTest.IpcTest(1), "TestCom2" : IpcCommTest.IpcTest(2)}
        recv_obj = IpcReceiver.IpcInCallbackHandler(list00)
        
        ### No.22-1 初期化前
        assert(recv_obj.IsInitialized() == False)
        assert(recv_obj.IsFinalized() == False)

        ### No.22-2 Initialize処理
        print("Test0002 - 出力パイプの生成をしてください。")
        assert(recv_obj.Initialize() == True)
        assert(recv_obj.IsInitialized() == True)
        assert(recv_obj.IsFinalized() == False)

        ### No.22-3 Initialize処理(二重起動)
        assert(recv_obj.Initialize() == False)
        assert(recv_obj.IsInitialized() == True)
        assert(recv_obj.IsFinalized() == False)

        state = IpcComm.IpcState()

        ### No.22-4 通常実行
        print("22-4")
        assert(recv_obj.RecvByBlocking(state) == 0)
        sleep(1)

        ### No.22-5 コマンド名無記名
        print("22-5")
        assert(recv_obj.RecvByBlocking(state) != 0)
        sleep(1)

        ### No.22-6 JSONフォーマット崩れ
        print("22-6")
        assert(recv_obj.RecvByBlocking(state) != 0)
        sleep(1)


        ### No.22-7 コマンド未定義
        print("22-7")
        assert(recv_obj.RecvByBlocking(state) != 0)
        sleep(1)

        ### No.22-8 通常実行
        print("22-8")
        assert(recv_obj.RecvByBlocking(state) == 0)
        sleep(1)

        ### No.22-9 通常実行
        print("22-9")
        assert(recv_obj.RecvByBlocking(state) == 0)
        sleep(1)

        ### No.22-10 通常実行
        print("22-10")
        assert(recv_obj.RecvByBlocking(state) == 0)
        sleep(1)


        ### No.22-11 破棄
        print("22-11")
        assert(recv_obj.Finalize() == True )
        assert(recv_obj.IsInitialized() == True)
        assert(recv_obj.IsFinalized() == True)

        ### No.22-12 再生成禁止
        print("22-12")
        assert(recv_obj.Initialize() == False) 
        assert(recv_obj.Finalize() == False )
        assert(recv_obj.IsInitialized() == True)
        assert(recv_obj.IsFinalized() == True)

    def test_IpcReceiver_0023(self):
        """
        テストケース No.23　パケット受信処理(コマンド未定義時)
        基本的には全てエラー
        """

        ### No.21-2　コンストラクタ（コマンド未定義）
        recvn_obj = None
        try:
            recvn_obj = IpcReceiver.IpcInCallbackHandler(None)
        except:
            pass

    def test_IpcReceiver_0024(self):
        """
        テストケース No.24　パイプ占有状態
        """
        list00 = { "TestCom1" : IpcCommTest.IpcTest(1), "TestCom2" : IpcCommTest.IpcTest(2)}
        trans_obj = IpcReceiver.IpcInCallbackHandler(list00)
        trans_obj2 = IpcReceiver.IpcInCallbackHandler(list00)

        print("Test0004 - 出力パイプを生成してください")
        assert(trans_obj.Initialize() == True)

        print("4")
        print("二重生成禁止確認")
        try:
            assert(trans_obj2.Initialize() == False)
            assert(trans_obj2.IsInitialized() == False)
            assert(trans_obj2.IsFinalized() == False)
        except:
            self.fail()


        trans_obj.Finalize()


    def test_IpcReceiver_0025(self):
        """
        テストケース No.25 何もせずにFinalize処理実行
        """
        list00 = { "TestCom1" : IpcCommTest.IpcTest(1), "TestCom2" : IpcCommTest.IpcTest(2)}
        trans_obj = IpcReceiver.IpcInCallbackHandler(list00)

        assert(trans_obj.Finalize() == False)
        assert(trans_obj.IsInitialized() == False)
        assert(trans_obj.IsFinalized() == False)


    def tearDown(self):
        pass




