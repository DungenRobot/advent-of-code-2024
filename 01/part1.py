def main():

    list1 = []
    list2 = []

    with open("01/input") as f:
        for line in f:
            num1, num2 = line.split("   ")
            list1.append(int(num1))
            list2.append(int(num2))

    list1.sort()
    list2.sort()

    sum = 0

    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])

    print(sum)




if __name__ == "__main__":
    main()