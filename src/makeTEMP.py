# -*- coding: utf-8 -*-
import main


def make_temp_data():
    bytes_data = b''
    for h in range(main.FILE_HEIGHT):
        for _ in range(main.FILE_WIDTH):
            if h < int(main.FILE_HEIGHT / 2):
                # 半分以下は緑
                r = main.int2bytes(0, 1, main.LITTLE_ENDIAN)
                g = main.int2bytes(255, 1, main.LITTLE_ENDIAN)
                b = main.int2bytes(0, 1, main.LITTLE_ENDIAN)
            else:
                # 半分以降は赤
                r = main.int2bytes(255, 1, main.LITTLE_ENDIAN)
                g = main.int2bytes(0, 1, main.LITTLE_ENDIAN)
                b = main.int2bytes(0, 1, main.LITTLE_ENDIAN)

            # 以下順での書き込みはBGRと解釈される
            # bytes_data = bytes_data + r + g + b

            bytes_data = bytes_data + b + g + r

    return bytes_data


if __name__ == '__main__':
    with open(main.TEMP_FILE_PATH, 'wb') as f:
        f.write(make_temp_data())
