def print_sum_of_current_and_previous(N, numbers):
    if N >= len(numbers):
        print("N must be less than the length of the list.")
        return

    prev = 0
    for i in range(N):
        current = numbers[i]
        print(f"Current Number {current} Previous Number {prev}, Sum: {current + prev}")
        prev = current

# Input
N = int(input())
numbers = list(map(int, input().strip()[1:-1].split(',')))
print_sum_of_current_and_previous(N, numbers)
