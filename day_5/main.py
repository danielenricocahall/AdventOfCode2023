

def compute_winning_strategies(times, distances) -> int:
    prod = 1
    for time, distance in zip(times, distances):
        prod *= sum((time - t) * t > distance for t in range(1, time))
    return prod


if __name__ == "__main__":
    with open('./input.txt') as fp:
        data = fp.readlines()
        print(data)
        times, distances = data
        times = times.replace("Time:", "").strip().split()
        distances = distances.replace("Distance:", "").strip().split()

        # Part 1
        print(compute_winning_strategies(map(int, times), map(int, distances)))

        # Part 2
        time = int("".join(times))
        distance = int("".join(distances))
        print(compute_winning_strategies([time], [distance]))
