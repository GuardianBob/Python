import tmdbsimple as tmdb
import random
import requests


tmdb.API_KEY = '1185412e00a20896217f777462cbdaff'
tmdb.REQUESTS_SESSION = requests.Session()

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


def search_btwn_years(start, end):
    discover = tmdb.Discover()
    # kwargs = {'release_date.gte': end, 'primary_release_date.lte': end}
    response = discover.movie(release_date_lte=end, primary_release_date_gte=start)
    return discover

def srch_genres(**kwargs):
    lst=[]
    for k, v in kwargs.items():
        lst.append(mGenres[v])
    gen = lst
    return gen


search = tmdb.Search()
discover = tmdb.Discover()
movies = tmdb.Movies(120)
# response = search.person()
# response = discover.movie(with_genres=mGenres['action'])

prnt1 = srch_genres(gen1='action', gen2='adventure')
print(prnt1)
response = discover.movie(with_genres=prnt1)
# response = discover.movie(release_date_lte=2011, primary_release_date_gte=2010)
# res = search_btwn_years(2010, 2011)
# # print(res)

# i=0
# while i < 10:
#     for j in discover.results:
#         print(j['title'])
#         i +=1
num = []
# for i in range(0, 10):    
#     rnd = random.randint(0,len(discover.results) - 1)
#     if rnd not in num:
#         num.append(rnd)
#         print(discover.results[rnd]['title'])
#     # print(num)
for i in range(0, 10):    
    rnd = random.randint(0,len(discover.results) - 1)
    if rnd not in num:
        num.append(rnd)
        print(discover.results[rnd]['title'])