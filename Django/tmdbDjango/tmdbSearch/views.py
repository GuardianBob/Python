from django.shortcuts import render, redirect, HttpResponse
import tmdbsimple as tmdb
import random, datetime
# from .keywords import keywords as kWords

tmdb.API_KEY = '1185412e00a20896217f777462cbdaff'

mGenres = {    
    'action':28,
    'adventure':12,
    'animation':16,
    'comedy':35,
    'crime':80,
    'documentary':99,
    'drama':18,
    'family':10751,
    'fantasy':14,
    'history':36,
    'horror':27,
    'music':10402,
    'mystery':9648,
    'romance':10749,
    'sci_fi':878,
    'science_fiction':878,
    'tv_movie':10770,
    'thriller':53,
    'war':10752,
    'western':37
}

country = {
    'USA': 'en',
    "Japan": 'ja',
    'All':''
}

sortBy = {
    "Popularity Ascending" : "popularity.asc",
    "Popularity Descending" : "popularity.desc",
    "Release Date Ascending" : "release_date.asc",
    "Release Date Descending" : "release_date.desc",
    "Title Ascending" : "original_title.asc",
    "Title Descending" : "original_title.desc",
    "Rating Ascending" : "vote_average.asc",
    "Rating Descending" : "vote_average.desc",
    "Number of Votes Ascending" : "vote_count.asc",
    "Number of Votes Descending" : "vote_count.desc"    
}

search = tmdb.Search()
discover = tmdb.Discover()
movies = tmdb.Movies(120)

posterURL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2'

def get_movies(postData):
    # print(request.POST) 
    discover = tmdb.Discover()
    genres = []
    gens = postData.getlist('genres')
    for gen in gens:
        # print(gen)
        genres.append(mGenres.get(gen))
    # keyWds = []
    # key_Ws = postData.getlist('keywords')

    # key_List = list(filter(lambda d: d['name'] in key_Ws, kWords))
    # for k in key_List:
    #     keyWds.append(k['id'])
    kwargs = {
        'with_original_language': country.get(postData['country']),
        'sort_by': postData['sortBy'],
        'primary_release_date_gte': str(min(int(postData['startYear']), int(postData['endYear']))) + "-01-01",
        'release_date_lte': str(max(int(postData['startYear']), int(postData['endYear']))) + "-12-31",        
        'with_genres': genres,
        'vote_average.gte': postData['minRating'],
        'vote_count.gte': postData['minVotes'],        
        'page': 1,
    }
    if 'adult' in postData:
        kwargs['include_adult'] = True
    # if 'keywords' in postData:
    #     kwargs[postData['keywords']] = keyWds
    
    # print(postData['keywords'], " : ", keyWds)
    i = 1
    response = discover.movie(**kwargs) 
    results = []
    # print(len(discover.results))
    while len(discover.results) > 1:
        # print(len(discover.results))
        # print(i)
        kwargs['page'] = i
        response = discover.movie(**kwargs)            
        for res in discover.results:
            if all(x in res['genre_ids'] for x in genres):  # Checks to make sure all genres searched for are included in movie's genres
                # print(res['genre_ids'])                
                results.append({
                    'title': res['title'],
                    'date': res['release_date'][:4],
                    'descr': res['overview'],
                    'rating': res['vote_average'],
                    'posterImg': posterURL + str(res['poster_path']),
                    'movieID': res['id']
            })
        i += 1      
        res_list = [i for n, i in enumerate(results) if i not in results[n + 1:]]
    return res_list

def rand_movie(postData):
    num = []
    movies_all = get_movies(postData)
    movies = []
    # print (len(movies_all))
    if len(movies_all) <= 10:
        for movie in movies_all:
            movies.append(movie)
    else:
        while len(movies) < 10:
            # rnd = random.randint(0,len(movies_all) - 1)
            rnd = random.choice([i for i in range(0,(len(movies_all)-1)) if i not in num]) # generates a random number excluding ones already thrown            
            # if movies_all[rnd]['movieID'] not in movies:
            if not any(movie['movieID'] == movies_all[rnd]['movieID'] for movie in movies): # checks to make sure the movie ID isn't already in the list
                movies.append(movies_all[rnd])
            num.append(rnd)
            # print(num)
            # print(movies_all[rnd]['movieID'])
    context = {
        'movies': movies
    }
    return movies

def index(request):
    context = {
        'mGenres': mGenres,
        'sortBy': sortBy,
    }
    # if ['startYear'] in request.session:
    #     context[user_in] = request.session
    return render(request, 'index.html', context)

def search(request):
    if request.method == "GET":
        return redirect('/')
    # request.session = request.POST
    if 'random' in request.POST:
        movies = rand_movie(request.POST)
    else:
        movies = get_movies(request.POST)
    context = {
        'movies': movies
    }
    return render(request, 'results.html', context)



