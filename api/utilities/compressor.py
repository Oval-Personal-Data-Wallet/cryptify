import base64
import zlib


def compress_text(text):
    if isinstance(text, str):
        text = text.encode('utf-8')
    compressed_text = zlib.compress(text)
    compressed_base64 = base64.b64encode(compressed_text).decode('utf-8')
    return compressed_base64


def decompress_text(compressed_base64):
    compressed_text = base64.b64decode(compressed_base64.encode('utf-8'))
    data = zlib.decompress(compressed_text).decode('utf-8')
    return data
