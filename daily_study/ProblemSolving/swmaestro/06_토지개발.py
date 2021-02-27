def divide(array, x):
    n1 = max(array[:x])
    n2 = max(array[x:])

    if n1 > n2:
        return n1, array[x:]
    else:
        return n2, array[:x]

def main():
    n = int(input())
    array = list(map(int, input().split()))
    answer = 0
    index = n
    while True:
        num, new_array = divide(array, index//2)
        if len(new_array) == 1:
            answer += num
            break
        answer += num
        index //= 2
        array = new_array
    print(answer)

if __name__ == "__main__":
    main()