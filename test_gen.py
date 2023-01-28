import random

if __name__ == '__main__':
    output_file = open("new_test.txt", "w")
    output_list = []
    for i in range(10000):
        x = random.choice([1, 2, 3])
        y = random.randint(1, 10000)
        z = random.randint(y, 100000)
        output_list.append(str(x)+" ")
        output_list.append(str(y)+" ")
        output_list.append(str(z)+"\n")

    output_file.writelines(output_list)