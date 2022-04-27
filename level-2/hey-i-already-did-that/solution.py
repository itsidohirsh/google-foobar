# Subtract 2 string numbers with the same base, and return string result.
# Constraints:
#       1. len(str1) = len(str2)
#       2. str1.value > str2.value
def sub_with_base(str1, str2, base):
    result = ""
    num1 = list(map(int, list(str1)))
    num2 = list(map(int, list(str2)))

    while len(num1):
        # Carry if needed
        if num1[-1] < num2[-1]:
            num1[-1] += base
            num1[-2] -= 1

        cur_dig = num1[-1] - num2[-1]
        result += str(cur_dig)
        num1.pop(-1)
        num2.pop(-1)

    return result[::-1]


def solution(n, b):
    k = len(n)
    seen_values = {}

    while True:
        if n in seen_values.keys():
            return len(seen_values.keys()) - seen_values.get(n)

        seen_values[n] = len(seen_values.keys())

        n = "".join(sorted(n))
        x = n[::-1]
        y = n
        z = sub_with_base(x, y, b)
        n = str(z).zfill(k)


def main():
    print(solution("1211", 10))
    print(solution("210022", 3))


if __name__ == "__main__":
    main()
