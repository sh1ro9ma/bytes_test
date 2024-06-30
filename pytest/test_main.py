#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..//src'))


import main


# テストケースを作成
def test_int2bytes_big_endian():
    assert main.int2bytes(1, 4, main.BIG_ENDIAN) == b'\x00\x00\x00\x01'
    assert main.int2bytes(255, 2, main.BIG_ENDIAN) == b'\x00\xff'
    assert main.int2bytes(305419896, 4, main.BIG_ENDIAN) == b'\x12\x34\x56\x78'

def test_int2bytes_little_endian():
    assert main.int2bytes(1, 4, main.LITTLE_ENDIAN) == b'\x01\x00\x00\x00'
    assert main.int2bytes(255, 2, main.LITTLE_ENDIAN) == b'\xff\x00'
    assert main.int2bytes(305419896, 4, main.LITTLE_ENDIAN) == b'\x78\x56\x34\x12'

def test_int2bytes_length():
    assert main.int2bytes(1, 1, main.LITTLE_ENDIAN) == b'\x01'
    assert main.int2bytes(1, 2, main.BIG_ENDIAN) == b'\x00\x01'
    assert main.int2bytes(65535, 2, main.BIG_ENDIAN) == b'\xff\xff'
    assert main.int2bytes(65535, 3, main.LITTLE_ENDIAN) == b'\xff\xff\x00'

# pytestを使ったテストの実行
if __name__ == "__main__":
    pytest.main()
