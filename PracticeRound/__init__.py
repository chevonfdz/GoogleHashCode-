def read_file():
    try:
        count = 0
        with open("a_an_example.in.txt", 'r') as f:
            lines = f.readlines()
            print(lines)

            for line in lines:
                count += 1

                if (count / 2) == int(count / 2):
                    for x in range(1, len(line)):
                        print("Line {}: {}".format(count, line.strip()))

    except FileNotFoundError:
        return "File not found"


read_file()

