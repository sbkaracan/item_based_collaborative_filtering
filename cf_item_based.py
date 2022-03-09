######################################
# Preparation of the Dataset
######################################

import pandas as pd
pd.set_option('display.max_columns', 20)

movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
df = movie.merge(rating, how="left", on="movieId")

df.head()
"""
   movieId             title                                       genres  \
0        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy   
1        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy   
2        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy   
3        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy   
4        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy   
   userId  rating            timestamp  
0     3.0     4.0  1999-12-11 13:36:47  
1     6.0     5.0  1997-03-13 17:50:52  
2     8.0     4.0  1996-06-05 13:37:51  
3    10.0     4.0  1999-11-25 02:44:47  
4    11.0     4.5  2009-01-02 01:13:41  
"""

######################################
# Creation of user movie df
######################################

rating_counts = pd.DataFrame(df["title"].value_counts())

rating_counts
"""
                                           title
Pulp Fiction (1994)                        67310
Forrest Gump (1994)                        66172
Shawshank Redemption, The (1994)           63366
Silence of the Lambs, The (1991)           63299
Jurassic Park (1993)                       59715
                                          ...
Rapture (Arrebato) (1980)                      1
Education of Mohammad Hussein, The (2013)      1
Satanas (2007)                                 1
Psychosis (2010)                               1
Innocence (2014)                               1
[27262 rows x 1 columns]
"""

rare_movies = rating_counts[rating_counts["title"] <= 1000].index

common_movies = df[~df["title"].isin(rare_movies)]

common_movies.shape
# (17766015, 6)

common_movies["title"].nunique()
# 3159

user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

user_movie_df.shape
# (138493, 3159)

user_movie_df.head(10)
"""
title   'burbs, The (1989)  (500) Days of Summer (2009)  \
userId                                                    
1.0                    NaN                          NaN   
2.0                    NaN                          NaN   
3.0                    NaN                          NaN   
4.0                    NaN                          NaN   
5.0                    NaN                          NaN   
6.0                    NaN                          NaN   
7.0                    NaN                          NaN   
8.0                    NaN                          NaN   
9.0                    NaN                          NaN   
10.0                   NaN                          NaN   
title   *batteries not included (1987)  ...And Justice for All (1979)  \
userId                                                                  
1.0                                NaN                            NaN   
2.0                                NaN                            NaN   
3.0                                NaN                            NaN   
4.0                                NaN                            NaN   
5.0                                NaN                            NaN   
6.0                                NaN                            NaN   
7.0                                NaN                            NaN   
8.0                                NaN                            NaN   
9.0                                NaN                            NaN   
10.0                               NaN                            NaN   
title   10 Things I Hate About You (1999)  10,000 BC (2008)  \
userId                                                        
1.0                                   NaN               NaN   
2.0                                   NaN               NaN   
3.0                                   NaN               NaN   
4.0                                   NaN               NaN   
5.0                                   NaN               NaN   
6.0                                   NaN               NaN   
7.0                                   NaN               NaN   
8.0                                   NaN               NaN   
9.0                                   NaN               NaN   
10.0                                  NaN               NaN   
title   101 Dalmatians (1996)  \
userId                          
1.0                       NaN   
2.0                       NaN   
3.0                       NaN   
4.0                       NaN   
5.0                       NaN   
6.0                       NaN   
7.0                       NaN   
8.0                       NaN   
9.0                       NaN   
10.0                      NaN   
title   101 Dalmatians (One Hundred and One Dalmatians) (1961)  \
userId                                                           
1.0                                                   NaN        
2.0                                                   NaN        
3.0                                                   NaN        
4.0                                                   NaN        
5.0                                                   NaN        
6.0                                                   NaN        
7.0                                                   NaN        
8.0                                                   NaN        
9.0                                                   NaN        
10.0                                                  NaN        
title   102 Dalmatians (2000)  12 Angry Men (1957)  ...  \
userId                                              ...   
1.0                       NaN                  NaN  ...   
2.0                       NaN                  NaN  ...   
3.0                       NaN                  NaN  ...   
4.0                       NaN                  NaN  ...   
5.0                       NaN                  NaN  ...   
6.0                       NaN                  NaN  ...   
7.0                       NaN                  NaN  ...   
8.0                       NaN                  NaN  ...   
9.0                       NaN                  NaN  ...   
10.0                      NaN                  NaN  ...   
title   Zero Dark Thirty (2012)  Zero Effect (1998)  Zodiac (2007)  \
userId                                                               
1.0                         NaN                 NaN            NaN   
2.0                         NaN                 NaN            NaN   
3.0                         NaN                 NaN            NaN   
4.0                         NaN                 NaN            NaN   
5.0                         NaN                 NaN            NaN   
6.0                         NaN                 NaN            NaN   
7.0                         NaN                 NaN            NaN   
8.0                         NaN                 NaN            NaN   
9.0                         NaN                 NaN            NaN   
10.0                        NaN                 NaN            NaN   
title   Zombieland (2009)  Zoolander (2001)  Zulu (1964)  [REC] (2007)  \
userId                                                                   
1.0                   NaN               NaN          NaN           NaN   
2.0                   NaN               NaN          NaN           NaN   
3.0                   NaN               NaN          NaN           NaN   
4.0                   NaN               NaN          NaN           NaN   
5.0                   NaN               NaN          NaN           NaN   
6.0                   NaN               NaN          NaN           NaN   
7.0                   NaN               NaN          NaN           NaN   
8.0                   NaN               NaN          NaN           NaN   
9.0                   NaN               NaN          NaN           NaN   
10.0                  NaN               NaN          NaN           NaN   
title   eXistenZ (1999)  xXx (2002)  ¡Three Amigos! (1986)  
userId                                                      
1.0                 NaN         NaN                    NaN  
2.0                 NaN         NaN                    NaN  
3.0                 NaN         NaN                    NaN  
4.0                 NaN         NaN                    NaN  
5.0                 NaN         NaN                    NaN  
6.0                 NaN         NaN                    NaN  
7.0                 NaN         NaN                    2.0  
8.0                 NaN         NaN                    NaN  
9.0                 NaN         NaN                    NaN  
10.0                NaN         NaN                    NaN  
[10 rows x 3159 columns]
"""

user_movie_df.columns
"""
Index([''burbs, The (1989)', '(500) Days of Summer (2009)',
       '*batteries not included (1987)', '...And Justice for All (1979)',
       '10 Things I Hate About You (1999)', '10,000 BC (2008)',
       '101 Dalmatians (1996)',
       '101 Dalmatians (One Hundred and One Dalmatians) (1961)',
       '102 Dalmatians (2000)', '12 Angry Men (1957)',
       ...
       'Zero Dark Thirty (2012)', 'Zero Effect (1998)', 'Zodiac (2007)',
       'Zombieland (2009)', 'Zoolander (2001)', 'Zulu (1964)', '[REC] (2007)',
       'eXistenZ (1999)', 'xXx (2002)', '¡Three Amigos! (1986)'],
      dtype='object', name='title', length=3159)
"""

len(user_movie_df.columns)
# 3159

######################################
# Item based recommendation
######################################

movie_name = "Matrix, The (1999)"

movie_name = user_movie_df[movie_name]

user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)
"""
title
Matrix, The (1999)                                           1.000000
Matrix Reloaded, The (2003)                                  0.516906
Matrix Revolutions, The (2003)                               0.449588
Animatrix, The (2003)                                        0.367151
Blade (1998)                                                 0.334493
Terminator 2: Judgment Day (1991)                            0.333882
Minority Report (2002)                                       0.332434
Edge of Tomorrow (2014)                                      0.326762
Mission: Impossible (1996)                                   0.320815
Lord of the Rings: The Fellowship of the Ring, The (2001)    0.318726
"""

movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)
"""
title
Ocean's Twelve (2004)                                 1.000000
Ocean's Thirteen (2007)                               0.681654
Ocean's Eleven (2001)                                 0.551280
Eddie (1996)                                          0.474808
National Treasure: Book of Secrets (2007)             0.474230
Eagle Eye (2008)                                      0.473061
Pirates of the Caribbean: On Stranger Tides (2011)    0.472446
Ocean's Eleven (a.k.a. Ocean's 11) (1960)             0.470412
Analyze That (2002)                                   0.459010
Bad Boys II (2003)                                    0.458827
dtype: float64
"""

# random movie choice
movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name
# 'Lara Croft: Tomb Raider (2001)'
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)
"""
title
Lara Croft: Tomb Raider (2001)                       1.000000
Lara Croft Tomb Raider: The Cradle of Life (2003)    0.798952
National Treasure: Book of Secrets (2007)            0.566507
xXx (2002)                                           0.555180
Man of the House (1995)                              0.553329
Resident Evil: Apocalypse (2004)                     0.551067
Resident Evil: Extinction (2007)                     0.547451
Catwoman (2004)                                      0.546193
Mummy Returns, The (2001)                            0.539675
Blade: Trinity (2004)                                0.533800
dtype: float64
"""


######################################
# Script of the project
######################################

def create_user_movie_df():
    movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
    rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["title"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df

user_movie_df = create_user_movie_df()

def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


item_based_recommender("Wall Street (1987)", user_movie_df)
"""
title
Wall Street (1987)                                    1.000000
Presumed Innocent (1990)                              0.468602
Pirates of the Caribbean: On Stranger Tides (2011)    0.408174
Fatal Attraction (1987)                               0.402455
Dirty Harry (1971)                                    0.400804
Thing from Another World, The (1951)                  0.400716
Love Affair (1994)                                    0.396500
American Gangster (2007)                              0.396235
Color of Money, The (1986)                            0.395827
Lincoln Lawyer, The (2011)                            0.393988
dtype: float64
"""


def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]


check_film("Sher", user_movie_df)
# ['Sherlock Holmes (2009)', 'Sherlock Holmes: A Game of Shadows (2011)', 'Young Sherlock Holmes (1985)']




