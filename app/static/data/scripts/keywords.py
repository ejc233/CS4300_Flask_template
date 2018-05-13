import json
from collections import Counter


def main():
    keywords = Counter()
    languages = Counter()
    for movie in json.load(open("movies.json", "r")):
        data = json.load(open("movies/" + movie['id'] + ".json", "r"))
        for keyword in data['keywords']:
            keywords[keyword] += 1
        languages[data['original_language']] += 1

    print(len(keywords))
    ok = set([kw for kw in keywords if keywords[kw] > 5])
    print(len(ok))

    for movie in json.load(open("movies.json", "r")):
        data = None
        with open("movies/" + movie['id'] + ".json", "r") as infile:
            data = json.load(infile)

        data['keywords'] = [w for w in data['keywords'] if w in ok]

        with open("movies/" + movie['id'] + ".json", "w") as outfile:
            json.dump(data, outfile)


if __name__ == "__main__":
    main()
