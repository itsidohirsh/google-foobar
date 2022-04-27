def str_mul(str1, str2):
    result = [0] * (len(str1) + len(str2))

    for i in range(-1, -len(str1) - 1, -1):
        for j in range(-1, -len(str2) - 1, -1):
            result[i + j + 1] += int(str1[i]) * int(str2[j])
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = "".join(map(str, result)).lstrip("0")

    return "0" if result == "" else result


def solution(xs):
    num_zeros = xs.count(0)
    negatives = [n for n in xs if n < 0]

    if num_zeros == len(xs):
        return str(0)

    if len(negatives) == 1 and len(xs) == 1:
        return str(xs[0])

    if len(negatives) == 1 and num_zeros == len(xs) - 1:
        return str(0)

    if len(negatives) % 2 == 1:
        xs.pop(xs.index(max(negatives)))

    result = "1"
    for panel in xs:
        if panel != 0:
            result = str_mul(result, str(abs(panel)))

    return result


print(solution([0, 0, 0, 0, 0]))
print(solution([0, -1, 0, 0, 0]))
print(solution([0, -1, 0, 0, -30]))
print(solution([2, 0, 0, 2, 2]))
print(solution([-2, -3, 4, -5]))
print(solution([2, -3, 1, 0, -5]))
