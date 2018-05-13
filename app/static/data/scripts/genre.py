import json
import matplotlib.pyplot as plt
from collections import defaultdict


def main():
    genres = defaultdict(int)
    n = 0
    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))
        n += 1
        for genre in movie['genres']:
            genres[genre] += 1
        print(n)

    genres = {k: v for k, v in genres.items() if v > 20}
    plt.figure(figsize=(24, 13.5), dpi=80)
    plt.bar(range(len(genres)), list(genres.values()), tick_label=list(genres.keys()))
    plt.title("Genre Distribution")
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.savefig('genres.png')
    plt.show()


if __name__ == "__main__":
    main()
