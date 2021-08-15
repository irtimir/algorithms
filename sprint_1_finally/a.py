"""
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
На каждом участке либо уже построен дом, либо участок пустой. Тимофей ищет место для строительства своего дома.
Он очень общителен и не хочет жить далеко от других людей, живущих на этой улице.

Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого участка знать расстояние до
ближайшего пустого участка. (Для пустого участка эта величина будет равна нулю –— расстояние до самого себя).

Ваша задача –— помочь Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на
карте никак не упорядочены. Пустые участки обозначены нулями.

52343856
"""
import sys


def get_min_distances_to_zero(numbers):
    last_zero_idx = None
    result = []

    for idx, number in enumerate(numbers):
        # obvious comparison with zeros is based in this algorithm, bool typecast could make it more entangled
        if number == 0:
            if idx != 0:
                if last_zero_idx is None:
                    to_recalculate_count = idx
                else:
                    to_recalculate_count = ((idx - 1) - last_zero_idx) // 2
                for dst_to_idx in range(to_recalculate_count, 0, -1):
                    result[idx - dst_to_idx] = dst_to_idx
            result.append(0)
            last_zero_idx = idx
        else:
            if last_zero_idx is None:
                result.append(None)
            else:
                result.append(idx - last_zero_idx)
    return result


def main():
    sys.stdin.readline().rstrip()
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    print(' '.join(map(str, get_min_distances_to_zero(numbers))))


if __name__ == '__main__':
    main()
