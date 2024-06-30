# -*- coding: utf-8 -*-
OUTPUT_FILE_NAME = "image.bmp"
OUTPUT_FILE_PATH = "./src/output/" + OUTPUT_FILE_NAME

LITTLE_ENDIAN = 0
BIG_ENDIAN = 1

FILE_WIDTH = 640
FILIE_HEIGHT = 480
PX_SIZE = 3
IMAGE_SIZE = FILE_WIDTH * FILIE_HEIGHT * PX_SIZE

FILE_HEADER_SIZE = 14
INFO_HEADER_SIZE = 40
FILE_SIZE = FILE_HEADER_SIZE + INFO_HEADER_SIZE + IMAGE_SIZE
OFFSET = FILE_HEADER_SIZE + INFO_HEADER_SIZE

# def int2bytes(int_val_r: int, length_r: int, endian: int) -> bytes:
def int2bytes(int_val_r, length_r, endian):
    """int型をバイト列に変換する

    Args:
        int_val_r (int): 変換したいint型の値
        length_r (int): 変換したいバイト列の長さ
        endian (int): 変換したいエンディアン

    Returns:
        bytes: 変換したバイト列
    """
    bytes_data = b""
    hex_str = hex(int_val_r)[2:]
    hex_str = hex_str.zfill(length_r * 2)
    bytes_data = hex_str.decode("hex")

    if endian == LITTLE_ENDIAN:
        bytes_data = bytes_data[::-1]

    return bytes_data


# def make_file_header() -> bytes:
def make_file_header():
    """ファイルヘッダの作成

    Returns:
        bytes: 作成したファイルヘッダ
    """
    bytes_data = b""
    bytes_data = bytes_data + int2bytes(0x424d, 2, BIG_ENDIAN)  # ファイルタイプ
    bytes_data = bytes_data + int2bytes(FILE_SIZE, 4, LITTLE_ENDIAN)  # ファイルサイズ
    bytes_data = bytes_data + int2bytes(0, 2, LITTLE_ENDIAN)  # 予約領域
    bytes_data = bytes_data + int2bytes(0, 2, LITTLE_ENDIAN)  # 予約領域
    bytes_data = bytes_data + int2bytes(OFFSET, 4, LITTLE_ENDIAN)  # "ファイル先頭から"画像データまでのオフセット  ☆
    return bytes_data


def main():
    bytes_data = b""
    bytes_data = bytes_data + make_file_header()


    with open(OUTPUT_FILE_PATH, "wb") as f:
        f.write(bytes_data)


if __name__ == "__main__":
    main()
