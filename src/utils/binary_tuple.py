from typing import Tuple

Binary_Tuple = Tuple[float, float]


def multiply_binary_tuple(binary_tuple: Binary_Tuple, multiply: float):
    return tuple([binary_tuple[0] * multiply, binary_tuple[1] * multiply])
