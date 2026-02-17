def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if len(numbers) == 0:
        return 0

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())

    for num in numbers:
        if counts[num] == max_count:
            return num

def main():
    test_list = [1, 2, 2, 3, 4, 5, 2]

    print("List:", test_list)
    print("Mean:", mean(test_list))
    print("Median:", median(test_list))
    print("Mode:", mode(test_list))

if __name__ == "__main__":
    main()
