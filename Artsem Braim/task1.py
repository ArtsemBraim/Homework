def main():

    with open("../data/unsorted_names.txt") as file:
        names = file.readlines()
        names.sort()

    with open("data/sorted_names.txt", "w") as file:
        file.writelines(names)


if __name__ == "__main__":
    main()
