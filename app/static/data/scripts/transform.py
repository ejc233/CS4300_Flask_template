import json
from shutil import copyfile, rmtree
from os import mkdir
from iso639 import languages
from collections import Counter


def main():

    index = json.load(open("movies.json", "r"))
    count = Counter([movie['title'] for movie in index])
    duplicate = set([movie for movie in count if count[movie] > 1])
    print(duplicate)

    # for movie in json.load(open("movies.json", "r")):
    for i in range(len(index)):
        movie = index[i]
        data = None
        with open("movies/" + movie['id'] + ".json", "r") as infile:
            data = json.load(infile)

        try:
            name = languages.get(part1=data["original_language"]).name
            data['original_language'] = name
            print(movie['title'] + ": " + name)
        except KeyError as e:
            if data['original_language'] == 'cn':
                print(movie['title'] + ": Cantonese")
                data['original_language'] = 'Cantonese'

        if data['title'] in duplicate:
            index[i]['title'] += ' (' + data['release_date'][:4] + ')'
            data['title'] += ' (' + data['release_date'][:4] + ')'

        with open("movies/" + movie['id'] + ".json", "w") as outfile:
            # del data['tokens']
            json.dump(data, outfile)

    # for i in range(len(index)):
    #     movie = index[i]
    #     data = None
    #     with open("movies/" + movie['id'] + ".json", "r") as infile:
    #         data = json.load(infile)

    #     if movie['title'] in duplicate:
    #         index[i]['title'] += ' (' + data['release_date'][:4] + ')'

    with open("movies.json", "w") as outfile:
        json.dump(index, outfile, indent=4)


if __name__ == "__main__":
    main()
