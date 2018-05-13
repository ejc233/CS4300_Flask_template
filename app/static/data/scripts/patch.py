import json
from shutil import copyfile


def main():

    index = json.load(open("movies.json", "r"))
    patch = json.load(open("popular/movies.json", "r"))

    id_set = set([movie['id'] for movie in index])

    for movie in patch:
        if movie['id'] not in id_set:
            print(movie['title'])
            index.append(movie)
            m = movie['id']
            copyfile("popular/movies/" + m + ".json", "movies/" + m + ".json")
            copyfile("popular/posters/" + m + ".jpg", "posters/" + m + ".jpg")

    with open("movies.json", "w") as f:
        json.dump(index, f)


if __name__ == "__main__":
    main()
