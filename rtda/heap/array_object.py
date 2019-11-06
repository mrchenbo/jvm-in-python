import copy


def ArrayCopy(src, dst, srcPos, dstPos, length):
    _src = src.data
    _dst = dst.data
    for i in range(length):
        _dst[dstPos + i] = _src[srcPos + i]
