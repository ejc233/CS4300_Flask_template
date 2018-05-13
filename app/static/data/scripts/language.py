import json
import matplotlib.pyplot as plt
from collections import defaultdict


def main():
    languages = defaultdict(int)
    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))
        languages[movie['original_language']] += 1

    languages = {k: v for k, v in languages.items() if v > 20}
    plt.figure(figsize=(24, 13.5), dpi=80)
    plt.bar(range(len(languages)), list(languages.values()), tick_label=list(languages.keys()))
    plt.title("Language Distribution")
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.savefig('languages.png')
    plt.show()


if __name__ == "__main__":
    main()
