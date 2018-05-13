import json
import matplotlib.pyplot as plt
from collections import defaultdict


def main():
    # genres = defaultdict(int)
    # language = defaultdict(int)
    # rating = defaultdict(int)
    # runtime = []
    # imdb = []
    # tmdb = []
    # meta = []

    n = 0
    for movie in json.load(open("movies.json", "r")):
        movie = json.load(open("movies/" + movie['id'] + ".json", "r"))
        if filter(movie):
            if movie["release_date"] == "":
                print(movie['id'], movie['title'])
                n += 1
    print(n)
            # for genre in movie['genres']:
            #     genres[genre] += 1
            # language[movie['original_language']] += 1
            # rating[movie['rating']] += 1
            # runtime.append(movie['runtime'])
            # tokens.append(len(movie['tokens']))
            # imdb.append(movie['imdb_score_value'])
            # tmdb.append(movie['tmdb_score_value'])
            # meta.append(movie['meta_score_value'])

            # if movie['tmdb_score_value'] < 1 and movie['tmdb_score_count'] > 0:
            #     print(
            #         "%s (%s), TMDB: %f, %d, IMDB: %f, %d, META: %f, %d" %
            #         (
            #             movie['title'],
            #             movie['id'],
            #             movie['tmdb_score_value'],
            #             movie['tmdb_score_count'],
            #             movie['imdb_score_value'],
            #             movie['imdb_score_count'],
            #             movie['meta_score_value'],
            #             movie['meta_score_count']
            #         )
            #     )

    # genres = {k: v for k, v in genres.items() if v > 20}
    # rating = {k: v for k, v, in rating.items() if v > 10}
    # runtime = [t for t in runtime if t < 200]
    # tokens = [t for t in tokens if t < 1000]
    # language = {k: v for k, v in language.items() if v > 50}

    # f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(24, 13.5), dpi=80)
    # plt.figure(figsize=(24, 13.5), dpi=80)

    # plt.subplot(331)
    # plt.hist(runtime)
    # plt.title("Runtime Distribution")

    # plt.subplot(332)
    # plt.hist(tokens)
    # plt.title("Tokens")

    # plt.subplot(333)
    # plt.bar(range(len(rating)), list(rating.values()), tick_label=list(rating.keys()))
    # plt.title("Rating Distribution")

    # plt.subplot(311)
    # plt.hist(imdb)
    # plt.title("IMDB Scores")
    # ax1.tick_params(
    #     axis='x',
    #     which='both',
    #     bottom='off',
    #     top='off',
    #     labelbottom='off'
    # )
    # ax1.spines['bottom'].set_visible(False)

    # ax2.spines['top'].set_visible(False)
    # plt.subplot(312)
    # plt.hist(tmdb)
    # plt.title("TMDB Scores")
    # ax2.tick_params(
    #     axis='x',
    #     which='both',
    #     bottom='off',
    #     top='off',
    #     labelbottom='off'
    # )
    # ax2.spines['bottom'].set_visible(False)

    # ax3.spines['top'].set_visible(False)
    # plt.subplot(313)
    # plt.hist(meta)
    # plt.title("Metacritic Scores")

    # plt.subplot(337)
    # f, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 13.5), dpi=80)
    # ax.set_title("Language Distribution")
    # ax.bar(range(len(language)), list(language.values()), tick_label=list(language.keys()))
    # ax2.bar(range(len(language)), list(language.values()), tick_label=list(language.keys()))
    # ax.set_ylim(9900, 10000)  # outliers only
    # ax2.set_ylim(0, 700)  # most of the data
    # ax.spines['bottom'].set_visible(False)
    # ax2.spines['top'].set_visible(False)
    # ax.tick_params(
    #     axis='x',          # changes apply to the x-axis
    #     which='both',      # both major and minor ticks are affected
    #     bottom='off',      # ticks along the bottom edge are off
    #     top='off',         # ticks along the top edge are off
    #     labelbottom='off'
    # )
    # ax2.xaxis.tick_bottom()
    # d = .005  # how big to make the diagonal lines in axes coordinates
    # # arguments to pass to plot, just so we don't keep repeating them
    # kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    # ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
    # ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

    # kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    # ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    # ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)


    # plt.subplot(338)
    # plt.bar(range(len(genres)), list(genres.values()), tick_label=list(genres.keys()))
    # plt.title("Genre Distribution")

    # plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    # plt.savefig('med_tokens.png')
    # plt.show()

# All movies with meta_score_count > 0 also have imdb_score_count > 0
def filter(movie):
    return movie['meta_score_count'] > 0


if __name__ == "__main__":
    main()
