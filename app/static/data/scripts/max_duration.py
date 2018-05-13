import json


def main():
    duration = 0
    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))
        duration = max(duration, movie['runtime'])

    print(duration)


if __name__ == "__main__":
    main()
