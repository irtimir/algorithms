"""
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
"""

def moving_avg_simple(timeseries, K):
    result = []

    for begin_index in range(0, len(timeseries) - K + 1):
        end_index = begin_index + K
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / K
        result.append(current_avg)

    return result


def moving_avg(timeseries, K):
    result = []

    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)

    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


def main():
    length = int(input())
    timeseries = list(map(int, input().split(' ')))
    K = int(input())
    # length = int('7')
    # timeseries = list(map(int, '1 2 3 4 5 6 7'.split(' ')))
    # K = int('4')


    # result = moving_avg_simple(timeseries, K)
    result = moving_avg(timeseries, K)

    print(' '.join(map(lambda d: '{:.9f}'.format(d).rstrip('0').rstrip('.'), result)))


if __name__ == '__main__':
    main()
