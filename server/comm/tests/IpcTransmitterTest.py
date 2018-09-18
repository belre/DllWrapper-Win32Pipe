
import unittest
import IpcTransmitter
from time import sleep



class IpcOutHandlerTest(unittest.TestCase):
    __pipe_in__ = None
    debug_type = 1            # 1, 2

    def setUp(self):
        pass

    def test_IpcTransmitter_0001(self):
        """
        テストケース No.1
        """
        try:
            trans_obj = IpcTransmitter.IpcOutHandler()
            assert(True==True)
        except:
            self.fail()

    @unittest.skipIf(debug_type != 1, 'test sim 01')
    def test_IpcTransmitter_0002(self):
        """
        テストケース No.2
        """        
        ### No.2-1 ###
        print("2-1")
        trans_obj = IpcTransmitter.IpcOutHandler()
        assert(trans_obj.IsInitialized()==False)
        assert(trans_obj.IsFinalized()==False)

        ### No.2-2 初期化 ###
        ## パイプ生成
        print("2-2")
        print("Test0002 - 入力パイプの生成をしてください。")
        assert(trans_obj.Initialize()==True)
        assert(trans_obj.IsInitialized()==True)
        assert(trans_obj.IsFinalized()==False)
        

        ### No.2-3 二重初期化 ###
        print("2-3")        
        assert(trans_obj.Initialize()==False)
        assert(trans_obj.IsInitialized()==True)
        assert(trans_obj.IsFinalized()==False)
        
        ### No.2-4 データ送信 ###
        print("2-4 - try1")        
        assert(trans_obj.SendByBlocking("hoge", -1,"piyo","foobar")==0)

        ### No.2-5 コマンド名がnull ###
        print("2-5")
        ret = 1
        try:
            ret = trans_obj.SendByBlocking(None, -1, "piyo", "foobar")
            assert(ret==-1)
        except:
            self.fail()

        ### No.2-6 タイプ名がnull ###
        print("2-6")
        ret = 1
        try:
            ret = trans_obj.SendByBlocking("hoge", -1, None, "foobar")
            assert(ret==-1)
        except:
            self.fail()


        ### No.2-7 パラメータがnull ###
        print("2-7")
        ret = 1
        try:
            ret = trans_obj.SendByBlocking("hoge", -1, "piyo", None)
            assert(ret==-1)
        except:
            self.fail()


        ### No.2-8 データ送信 ###
        print("2-8 - try2")        
        assert(trans_obj.SendByBlocking("hoge",-1, "piyo","foobar")==0)

        ### No.2-9 データ送信 ###
        print("2-9 - try3")        
        assert(trans_obj.SendByBlocking("ほげ",-1, "ぴよ","あいうえお")==0)

        ### No.2-10 データ送信 ###
        print("2-10 - try4")        
        assert(trans_obj.SendByBlocking("\\",-1, "\'","\\r\\n")==0)

        ### No.2-11 データ送信 ###
        print("2-11 - try5")        
        assert(trans_obj.SendByBlocking("hoge", 100, "piyo","foobar")==0)

        print("10秒待機した後にパイプを終了します。")
        sleep(10)

        ### No.2-12 破棄 ###
        print("2-12")        
        assert(trans_obj.Finalize()==True)
        assert(trans_obj.IsInitialized()==True)
        assert(trans_obj.IsFinalized()==True)

        ### No.2-13 パイプ再生成禁止 ###
        print("2-13")        
        assert(trans_obj.Initialize()==False)
        assert(trans_obj.Finalize()==False)
        assert(trans_obj.IsInitialized()==True)
        assert(trans_obj.IsFinalized()==True)

    @unittest.skipIf(debug_type != 2, 'test sim 02')
    def test_IpcTransmitter_0004(self):
        """
        テストケース No.4
        """


        ### No.4 パイプ占有されている状態で初期化
        trans_obj = IpcTransmitter.IpcOutHandler()
        trans_obj2 = IpcTransmitter.IpcOutHandler()

        print("Test0004 - 入力パイプを生成してください")
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

    def test_IpcTransmitter_0005(self):
        """
        テストケース No.5
        何もしていない状態でFinalize
        """

        ### No.5　何もしていない状態でパイプ破棄
        trans_obj = IpcTransmitter.IpcOutHandler()

        try:
            assert(trans_obj.Finalize() == False)
            assert(trans_obj.IsInitialized() == False)
            assert(trans_obj.IsFinalized() == False)
        except:
            self.fail()



    def tearDown(self):
        pass








