def get_likes(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

            for line in range(1, len(lines), 2):
                likes = lines[line].strip().split()

                likes.pop(0)
                for x in range(len(likes)):
                    all_likes.append(likes[x])

            f.close()

    except FileNotFoundError:
        return "File not found"


def get_dislikes(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

            for line in range(2, len(lines), 2):
                dislikes = lines[line].strip().split()

                dislikes.pop(0)
                for x in range(len(dislikes)):
                    all_dislikes.append(dislikes[x])

            f.close()

    except FileNotFoundError:
        return "File not found"


def output():
    textfile = open("output.txt", "w")

    likesCount = len(all_likes)

    textfile.write("{} ".format(likesCount))
    for element in all_likes:
        textfile.write(element + " ")
    textfile.close()


file = "e_elaborate.in.txt"
all_likes = []
all_dislikes = []

get_likes(file)
all_likes = list(dict.fromkeys(all_likes))

get_dislikes(file)
all_dislikes = list(dict.fromkeys(all_dislikes))

for element in all_dislikes:
    if element in all_likes:
        all_likes.remove(element)

output()

print("Your output is ready!!!")
