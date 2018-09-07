import ctypes           # C++のデータ型ライブラリ
from ctypes import *    

import struct           # C++の構造体ライブラリ
import binascii         # bin <--> ASCII変換


# DLL読込
___lib_ijl20___ = CDLL("dll/ijl20.dll")
___lib_casmodule___ = CDLL("dll/CASRecogModule.dll")
___lib_casmodule___.ReadTemplateInteg2_wp.argtypes = [ ctypes.c_char_p, POINTER(ctypes.c_void_p)]
___lib_casmodule___.HaltTemplateInteg2_wp.argtypes = [ ctypes.c_void_p, ctypes.c_int]

# テンプレートをバイナリ形式で読み込み
__fd_templatebin__ = open("ES2_050_A.tp", "rb")
bindata = __fd_templatebin__.read()
buff=binascii.b2a_hex(bindata)
__fd_templatebin__.read()
__fd_templatebin__.close()


# 暗号化動作テスト
integ_ptr = c_void_p()
print(___lib_casmodule___.ReadTemplateInteg2_wp(buff, byref(integ_ptr)))
print(___lib_casmodule___.HaltTemplateInteg2_wp(integ_ptr, 1))







