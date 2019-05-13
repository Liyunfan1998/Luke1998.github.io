def CMYK2RGB(C, M, Y, K):
    R = 255 * (100 - C) * (100 - K) / 10000;
    G = 255 * (100 - M) * (100 - K) / 10000;
    B = 255 * (100 - Y) * (100 - K) / 10000;
    return R, G, B


def RGB2CMYK(R, G, B):
    K = int(min(min(255 - R, 255 - G), 255 - B) / 2.55)
    R = round(R / 2.55)
    Div = 100 - K
    if Div == 0:
        Div = 1
    G = round(G / 2.55)
    C = int(((100 - R - K) / Div) *100)
    M = int(((100 - G - K) / Div) * 100)
    B = round(B / 2.55)
    Y = int(((100 - B - K) / Div) * 100)
    return C, M, Y, K


R, G, B = 230, 99, 88
C, M, Y, K = RGB2CMYK(R, G, B)
print(C, M, Y, K)
