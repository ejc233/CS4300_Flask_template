import json
from shutil import copyfile, rmtree
from os import mkdir


def filter(movie):
    imdb = movie['imdb_score_count'] > 0
    date = movie['release_date'] != ""
    genre = len(movie['genres']) > 0
    cast = len(movie['cast']) > 0
    crew = len(movie['crew']) > 0
    runtime = movie['runtime'] >= 60
    return imdb and date and genre and cast and crew and runtime


def main():

    n = 0
    rmtree("filtered")
    mkdir("filtered")
    mkdir("filtered/movies")
    mkdir("filtered/posters")
    top = []

    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))

        if filter(movie):
            top.append((movie['imdb_score_count'], movie['title'], movie['id']))

    with open("filtered/movies.json", "w") as f:
        f.write('[\n')

        for (count, title, id) in sorted(top, reverse=True)[:5000]:
            print(count, title, n)
            copyfile("movies/" + id + ".json", "filtered/movies/" + id + ".json")
            copyfile("posters/" + id + ".jpg", "filtered/posters/" + id + ".jpg")
            n += 1
            f.write(
                '    {"id":"%s","title":"%s"},\n' % (
                    id,
                    title
                )
            )

        f.write(']\n')


if __name__ == "__main__":
    main()
