import os


def read_file():

    with open("../package.json") as f:
        f.read()



def main():
    read_file()

if __name__ == '__main__':
    main()