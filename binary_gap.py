"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps:
one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5,
because N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0,
because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
"""

import re


def solution(num: int) -> int:
    print(bin(num))
    binary_repr = str(bin(num)).split("b")[1]
    gaps_found_with_re = re.findall(r"(?<=1)0+(?=1)", binary_repr)
    if len(gaps_found_with_re) == 0:
        return 0
    sorted_list = sorted(gaps_found_with_re, key=len, reverse=True)
    return len(sorted_list[0])


if __name__ == "__main__":
    print(solution(32))
