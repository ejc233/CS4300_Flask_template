import scipy.stats

def parse(inp):
    if "-" in inp:
        inps = inp.split("-")
        if len(inps) == 2 and inps[0].strip().isdigit() and inps[1].strip().isdigit():
            return [int(entry.strip()) for entry in inps[:2]]
        else:
            return []
    if inp.strip().isdigit():
        return [int(inp.strip())]
    else:
        return []

def filter_hard(movie_dict,low_bound, high_bound, high_val):
    rtn_movie = {}
    for movie in movie_dict:
        if movie_dict[movie]['runtime'] >= low_bound and movie_dict[movie]['runtime'] <= high_bound:
            rtn_movie[movie] = movie_dict[movie]
    return rtn_movie

# gaussian weighted appropriately: update the score_dict
def gaussian_score(movie_dict,mean,high_val,low_val):
    score_dict = {}

    if mean > 224:
        mean = 224

    dist = scipy.stats.norm(mean,10)
    movie_to_weight = {k:dist.pdf(v['runtime']) for k,v in movie_dict.iteritems()}
    max_val,min_val = max(movie_to_weight.values()), min(movie_to_weight.values())

    # movie -> weight value between 0 and 1
    if min_val < max_val:
        movie_to_weight = {k:((v - min_val)/(max_val - min_val)) for k,v in movie_to_weight.iteritems()}

    # movie -> weight value between high and low
    for movie in movie_dict:
        score_dict[movie] = movie_to_weight[movie]*(high_val + low_val) - low_val
    return score_dict


def main(movie_dict, inp, high_val):
    vals = parse(inp)
    if vals == []:
        return {}
    if len(vals) == 2:
        return filter_hard(movie_dict,vals[0],vals[1], high_val)
    return movie_dict
