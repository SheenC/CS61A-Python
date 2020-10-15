"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    "*** YOUR CODE HERE ***"
    return min(centroids, key = lambda x: distance(location, x))
    # END Question 3


def group_by_first(pairs):
    """Return a list of lists that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)  # Values from pairs that start with 1, 3, and 2 respectively
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    "*** YOUR CODE HERE ***"
    return group_by_first([[find_closest(restaurant_location(x),centroids),x]for x in restaurants])
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    "*** YOUR CODE HERE ***"
    def lat(cluster):
        return [restaurant_location(x)[0] for x in cluster]
    def lon(cluster):
        return [restaurant_location(x)[1] for x in cluster]
    return [mean(lat(cluster)), mean(lon(cluster))]
    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0

    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        "*** YOUR CODE HERE ***"
        cluster = group_by_centroid(restaurants, centroids)
        centroids = [find_centroid(x) for x in cluster]
        # END Question 6
        n += 1
    return centroids

'''
    Grouping the restaurants into k clusters by location.
    
    Randomly initialize k centroids.
    
    Create a cluster for each centroid consisting of all elements closest to
    that centroid.
    Find the centroid (average position) of each cluster.
'''


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.
    ‘’‘
    find_predictor(user, restaurants, feature_fn)
    takes in a restaurant and returns the predicted rating for that restaurant
    ’‘’
    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    '''
    feature_fn —— the extracted feature value for each restaurant in restaurants
    '''
    """
    xs = [feature_fn(r) for r in restaurants]
    ys = [user_rating(user, restaurant_name(r)) for r in restaurants]
    '''
        user's ratings for the restaurants in restaurants
    '''

    # BEGIN Question 7
    "*** YOUR CODE HERE ***"
    meanx=mean(xs)
    meany=mean(ys)
    sxx=sum([pow(x-meanx,2) for x in xs])
    syy=sum([pow(y-meany,2) for y in ys])
    sxy=sum([(x-meanx)*(y-meany) for x,y in zip(xs,ys)])
    b=sxy/sxx
    a=meany-b*meanx
    r_squared=pow(sxy,2)/(sxx*syy)
    # END Question 7

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.
    
    '''
     Given a user, a list of restaurants, and a feature function, what
     does find_predictor from Problem 7 return?
     a predictor function and its r_squared value
    
     After computing a list of [predictor, r_squared] pairs,
     which predictor should we select?
     the predictor with the highest r_squared value
    '''

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    '''
        reviewed —— a list of restaurants reviewed by the user
    '''
    # BEGIN Question 8
    "*** YOUR CODE HERE ***"
    return max([find_predictor(user,reviewed,f) for f in feature_fns], key=lambda x: x[1])[0]
    # END Question 8


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.
    
    '''
    rate_all returns a dictionary. What are the keys of this dictionary?
    restaurant names
    
    What are the values of the returned dictionary?
    numbers - a mix of user ratings and predicted ratings
    '''

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    '''
        predictor: a list of restaurants reviewed by the user
    '''
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 9
    "*** YOUR CODE HERE ***"
 
    dic_restaurants = {}
    for restaurant in restaurants:
        name = restaurant_name(restaurant)
        if restaurant in reviewed:
           dic_restaurants[name] = user_rating(user, name)
        else:
           dic_restaurants[name] = predictor(restaurant)
    return dic_restaurants


    # END Question 9


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    '''
    Given a restaurant, what does restaurant_categories in abstractions.py return?
    a list of strings (categories)
    
    When does a restaurant match a search query?
    if the query string is one of the restaurant's categories
    
    What type of object does search return?
    a list of restaurants
    '''
    
    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    "*** YOUR CODE HERE ***"
    return [x for x in restaurants if query in restaurant_categories(x)]
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)
