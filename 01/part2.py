









def main():

    list1 = []
    list2 = {}

    with open("01/input") as f:
        for line in f:
            num1, num2 = line.split("   ")
            list1.append(int(num1))

            list2[int(num2)] = list2.get(int(num2), 0) + 1

    sum = 0

    for num in list1:
        sum += num * list2.get(num, 0)

    print(sum)




if __name__ == "__main__":
    main()