# Здесь писать код решения задачи. В качестве примера решение "Ближайший ноль"

def get_distances(houses, empty="0"):
    zeros = [index for index, number in enumerate(houses) if number == empty]
    distances = [0] * len(houses)
    first, last = zeros[0], zeros[-1]
    for left, right in zip(zeros, zeros[1:]):
        distances[left + 1:right] = [
            min(position - left, right - position)
            for position in range(left + 1, right)
        ]
    distances[:first] = [first - position for position in range(first)]
    distances[last + 1:] = [
        position - last for position in range(last + 1, len(distances))
    ]
    return distances


def call_main(file_path):

    file_path.readline().rstrip()
    print(*get_distances(houses=file_path.readline().rstrip().split()))
