def main():
    sum = 0
    
    with open("03/input") as f:
        for line in f:


            line = ' ' + line.strip()
            i = 0
            while line != "":
                line = line[1:]
            
                if not line.startswith("mul("):
                    continue

                num1 = 0
                line = line[4:]
                while line.lstrip('1234567890') != line:
                    num1 = int(line[0]) + (num1 * 10)
                    #print(">", num1)
                    line = line[1:]
                
                if (len(line) == 0) or line[0] != ',':
                    continue

                line = line[1:]

                num2 = 0
                while line.lstrip('1234567890') != line:
                    num2 = int(line[0]) + (num2 * 10)
                    line = line[1:]
                
                if (len(line) == 0) or line[0] != ')':
                    continue

                sum += num1 * num2

    print(sum)



if __name__ == "__main__":
    main()