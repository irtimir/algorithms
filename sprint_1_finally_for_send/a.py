"""
Run ID: 52332298
"""
import sys


def get_min_distances_to_zero(numbers):
    last_zero_idx = None
    result = []

    for idx, number in enumerate(numbers):
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
