import json
import scipy.stats
import user_release
import numpy as np 
import math

# remove entries from dictionary that do not have specific ratings
def filter_ratings(movie_dict, inp):
    rtn_movie = {}
    inp_set = set(inp)
    for movie in movie_dict:
        if movie_dict[movie]['rating'].lower() in inp_set:
            rtn_movie[movie] = movie_dict[movie]
    return rtn_movie

# remove entries from dictionary that do not have specific languages
def filter_languages(movie_dict, inp):
    rtn_movie = {}
    inp_set = set(inp)
    for movie in movie_dict:
        if movie_dict[movie]['original_language'].lower() in inp_set:
            rtn_movie[movie] = movie_dict[movie]
    return rtn_movie

def filter_similar(movie_dict, similar_movies):
    rtn_movie = {}
    similar_movies = set(similar_movies)
    for movie in movie_dict:
        if movie_dict[movie]['title'].lower() not in similar_movies:
            rtn_movie[movie] = movie_dict[movie]
    return rtn_movie

# normalize the logarithmic scores...
def normalize_score(overall_score,denom):
    best_score = abs(math.log(1.0/denom))
    for movie in overall_score:
    #     print("here is your best_score " + str(best_score))
    #     print("overall score " + str(overall_score[movie]))
        overall_score[movie] = (overall_score[movie])/(best_score+1)
        # print("final score " + str(overall_score[movie]))
    return overall_score

def calc_popularity(movie_dict,movie,max_tmdb_count,max_imdb_count,max_meta_count):
    tmdb_count = movie_dict[movie]['tmdb_score_count']
    if tmdb_count == 0:
        tmdb_average = 0
    else:
        tmdb_average = math.log(tmdb_count) / math.log(max_tmdb_count)
    imdb_count = movie_dict[movie]['imdb_score_count']
    if imdb_count == 0:
        imdb_average = 0
    else:
        imdb_average = math.log(imdb_count) / math.log(max_imdb_count)
    meta_count = movie_dict[movie]['meta_score_count']
    if meta_count == 0:
        meta_average = 0
    else:
        meta_average = math.log(meta_count) / math.log(max_meta_count)
    average_score = (tmdb_average + imdb_average + meta_average) / 3.0
    return average_score

# fit to a distribution which weights high values much more heavily than lowerer ones
# penalize lower acclaim values more than a simple linear function
def half_gaussian_acclaim(movie_dict, high_val, low_val):
    rtn_dict = {}
    
    # gaussian with mean 10, stdev 6 => half gaussian w/ mean 10, stdev 3
    dist = scipy.stats.norm(10,2.5)
    movie_to_weight = {k:dist.pdf(v['tmdb_score_value']) for k,v in movie_dict.iteritems()}
    # max_val,min_val = max(movie_to_weight.values()), min(movie_to_weight.values())
    # make acclaim less impactful: map all values between 0 and 1 rather than having 
    # the highest acclaim have a value of 1
    max_val,min_val = 1,0

    # movie -> weight value between 0 and 1
    movie_to_weight = {k:((v - min_val)/(max_val - min_val)) for k,v in movie_to_weight.iteritems()}

    # movie -> weight value between high and low
    for movie in movie_dict:
        rtn_dict[movie] = (movie_to_weight[movie]*(high_val + low_val) - low_val)
    return rtn_dict

def get_similar_ranking(sim_movie_tup, movie_dict):
    sim_movie, genres, castCrew,release_year,sim_rating,sim_lang = sim_movie_tup
    movie_feature_lst,movie_id_lookup = [],{}

    release_score_dict = user_release.gaussian_release_score(movie_dict,release_year,0,1)
    acclaim_score_dict = half_gaussian_acclaim(movie_dict, 1, 0)

    for index,movie in enumerate(movie_dict):
        features_lst = []

        # genre matters for a similar movie
        features_lst.append(get_set_overlap(genres,movie_dict[movie]['genres']))

        # release year matters for a similar movie 
        features_lst.append(0.5 * release_score_dict[movie])

        # rating matters for a similar movie: improvement upon final submission
        if sim_rating.lower() == movie_dict[movie]['rating'].lower():
            features_lst.append(0.5)
        elif sim_rating.lower() == 'pg' and movie_dict[movie]['rating'].lower() == 'g':
            features_lst.append(0.3)
        elif sim_rating.lower() == 'pg' and movie_dict[movie]['rating'].lower() == 'pg-13':
            features_lst.append(0.3)
        elif sim_rating.lower() == 'g' and movie_dict[movie]['rating'].lower() == 'pg':
            features_lst.append(0.3)
        else:
            features_lst.append(0)

        # language matters for a similar movie: improvement upon final submission
        if sim_lang.lower() == movie_dict[movie]['original_language'].lower():
            features_lst.append(0.5)
        else:
            features_lst.append(0)

        cast = [member['name'] for member in movie_dict[movie]['cast']]
        crew = [member['name'] for member in movie_dict[movie]['crew']]
        features_lst.append(get_set_overlap(castCrew,cast + crew))

        features_lst.append(acclaim_score_dict[movie])

        if sim_movie in movie_dict[movie]['cosine']:
            if movie_dict[movie]['cosine'][sim_movie] > 1.0:
                features_lst.append(1.0)
            else:
                features_lst.append(movie_dict[movie]['cosine'][sim_movie])
        else:
            features_lst.append(0.0)

        movie_feature_lst.append(features_lst)
        movie_id_lookup[index] = movie

    movie_matrix = np.zeros((len(movie_feature_lst),len(movie_feature_lst[0])))
    for i in range(len(movie_feature_lst)):
        for k in range(len(movie_feature_lst[i])):
            movie_matrix[i][k] = movie_feature_lst[i][k]

    ########### RUN KNN ON VECTORS, RETURN TOP MATCHES ###########
    n,d = movie_matrix.shape
    query = np.ones(d)
    dists = np.linalg.norm(movie_matrix - query,axis=1,ord=2)
    ranked_lst = np.argsort(dists)
    rtn = [movie_id_lookup[movie_id] for movie_id in ranked_lst]
    return rtn

# get the fraction of items in list1 available in list2
def get_set_overlap(list1, list2):
    set1 = set([x.lower() for x in list1])
    set2 = set([x.lower() for x in list2])
    num = float(len(set1.intersection(set2)))
    den = len(set1)
    return num / den

def get_jsons():
    movies_json = json.load(open('app/static/data/movies.json'))
    movie_dict = dict()
    for movie in movies_json:
        movie_dict[movie['id']] = json.load(open('app/static/data/movies/' + movie['id'] + '.json'))
    castCrew_list = []
    keywords_list = []
    ratings_list = []
    languages_list = []
    for movie in movie_dict:
        castCrew_list += ([member['name'] for member in movie_dict[movie]['cast']] + [member['name'] for member in movie_dict[movie]['crew']])
        keywords_list += movie_dict[movie]['keywords']
        ratings_list.append(movie_dict[movie]['rating'])
        languages_list.append(movie_dict[movie]['original_language'])
    castCrew_list = list(set(castCrew_list))
    castCrew_list.sort()
    castCrew_dict = [{'name' : i} for i in castCrew_list]
    keywords_list = list(set(keywords_list))
    keywords_list.sort()
    keywords_dict = [{'name' : i} for i in keywords_list]
    ratings_list = list(set(ratings_list))
    ratings_list.sort()
    ratings_dict = [{'name' : i} for i in ratings_list]
    languages_list = list(set(languages_list))
    languages_list.sort()
    languages_dict = [{'name' : i} for i in languages_list]

    with open('app/static/data/cast.json', 'w') as outfile:
        json.dump(castCrew_dict, outfile)

    with open('app/static/data/keywords.json', 'w') as outfile:
        json.dump(keywords_dict, outfile)

    with open('app/static/data/ratings.json', 'w') as outfile:
        json.dump(ratings_dict, outfile)

    with open('app/static/data/languages.json', 'w') as outfile:
        json.dump(languages_dict, outfile)
    

if __name__ == "__main__":
    get_jsons()