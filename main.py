def read_file():
    try:
        with open("a_an_example.in.txt", 'r') as f:
            lines = f.readlines()
            print(lines)

            for line in range(1, len(lines), 2):
                likes = lines[line].strip().split()

                likes.pop(0)
                for x in range(len(likes)):
                    all_likes.append(likes[x])

                # print(likes)
                # print("Line {}: {}".format(line, likes))
                # print(all_likes)
            f.close()

    except FileNotFoundError:
        return "File not found"


def get_dislikes():
    try:
        with open("a_an_example.in.txt", 'r') as f:
            lines = f.readlines()
            print(lines)

            for line in range(2, len(lines), 2):
                dislikes = lines[line].strip().split()

                dislikes.pop(0)
                for x in range(len(dislikes)):
                    all_dislikes.append(dislikes[x])

    except FileNotFoundError:
        return "File not found"


all_likes = []
all_dislikes = []
read_file()
get_dislikes()

all_likes = list(dict.fromkeys(all_likes))
print(all_likes)
print(all_dislikes)
