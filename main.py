def read_file():
    try:
        with open("a_an_example.in.txt", 'r') as f:
            lines = f.readlines()
            print(lines)

            for line in range(1, len(lines), 2):
                likes = lines[line].strip().split()

                likes.pop(0)
                for x in  range(len(likes)):
                    all_likes.append(likes[x])

                print(likes)
                print("Line {}: {}".format(line, likes))
                print(all_likes)

    except FileNotFoundError:
        return "File not found"

all_likes = []
read_file()

