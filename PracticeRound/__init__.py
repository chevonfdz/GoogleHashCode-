def read_file():
    try:
        count = 0
        with open("a_an_example.in.txt", 'r') as f:
            lines = f.readlines()
            print(lines)

            for line in range(1, len(lines), 2):
                # count += 1
                likes = lines[line].strip().split()

                # for x in (1, len(likes)):
                # # if x < 0:
                # # like_f = likes[x]
                #     all_likes = []
                #     all_likes.append(likes[x])

                print(likes)

                print("Line {}: {}".format(line, likes[1]))
                # print(all_likes)

                # if (count / 2) == int(count / 2):
                #     for x in range(1, len(line)):
                #         print("Line {}: {}".format(count, line.strip()))

    except FileNotFoundError:
        return "File not found"


read_file()
