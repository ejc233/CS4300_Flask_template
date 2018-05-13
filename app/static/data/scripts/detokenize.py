import json


def main():

    for movie in json.load(open("movies.json", "r")):
        data = None
        with open("movies/" + movie['id'] + ".json", "r") as infile:
            data = json.load(infile)

        with open("movies/" + movie['id'] + ".json", "w") as outfile:
            del data['tokens']
            json.dump(data, outfile)


if __name__ == "__main__":
    main()
