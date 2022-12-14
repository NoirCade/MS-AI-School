# 단층 퍼셉트론 이용하여 AND, NAND, OR 게이트 구현

# AND 게이트 구현
# 입력값 두개 모두 1이면 output = 1, 그 외 0

# AND 게이트를 만족하는 두개의 가중치와 편향 값에는 무엇이 있는가?
# w1, w2, b 라고 하면 (w 가중치 b 편향)
# 0.5, 0.2, 0.1 -> 결과 구해진 수치 [0.5, 0.5, -0.7]

def and_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.7

    # x1*w1 + x2*w2 + b
    result = x1*w1 + x2*w2 + b

    if result <= 0:
        return 0
    else:
        return 1


# print(and_gate(0, 0))

# 단층 퍼셉트론 NAND 게이트 구현
# 입력값 두개 다 1인 경우에만 output = 0, 나머지 1

def nand_gate(x1, x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7

    result = x1*w1 + x2*w2 + b

    if result >= 0:
        return 0
    else:
        return 1


# print(nand_gate(0, 0))

def or_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.2

    result = x1*w1 + x2*w2 + b

    if result >= 0:
        return 0
    else:
        return 1