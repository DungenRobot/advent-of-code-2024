def main():
    sum = 0

    mul_enabled = True
    
    with open("03/input") as f:
        for line in f:


            line = ' ' + line.strip()
            i = 0
            while line != "":
                line = line[1:]

                if line.startswith("do()"):
                    mul_enabled = True
                
                if line.startswith("don't"):
                    mul_enabled = False
            
                if not line.startswith("mul("):
                    continue

                if not mul_enabled:
                    continue

                num1 = 0
                line = line[4:]
                while line.lstrip('1234567890') != line:
                    num1 = int(line[0]) + (num1 * 10)
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