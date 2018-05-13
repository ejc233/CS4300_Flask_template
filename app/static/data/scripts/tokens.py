import json
import matplotlib.pyplot as plt


def main():
    votes = []
    tokens = []
    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))
        votes.append(movie['imdb_score_count'])
        tokens.append(len(movie['tokens']))

    plt.scatter(votes, tokens)
    plt.title("Vote and Token Distribution")
    plt.savefig('tokens.png', figsize=(24, 13.5), dpi=80)
    plt.show()


if __name__ == "__main__":
    main()
