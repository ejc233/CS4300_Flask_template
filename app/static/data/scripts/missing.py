import re


def main():

    regex = re.compile('\d\d:\d\d:\d\d \[ERROR\] (\d+):')

    with open('movies.log', 'r') as log:
        for line in log:
            match = regex.match(line)
            if match:
                print(match.group(1))


if __name__ == "__main__":
    main()
