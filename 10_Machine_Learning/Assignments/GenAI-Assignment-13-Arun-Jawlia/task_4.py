
'''
Task 4: API Mini Project ( TMDB API )

'''

import requests
import pandas as pd


Final_Data = pd.DataFrame()

for i in range(1, 100):
  url = f'https://api.themoviedb.org/3/trending/movie/day?api_key=your_tmdb_api_key&language=en-US&page={i}'.format(i)

  headers = {
      "accept": 'application/json',
      "Authorization": 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDdiYTNkODM0NmM3NTM1Y2QzMzcwNDdiNGQ3MzAxYSIsIm5iZiI6MTcwMDcxNjg2NS4yMTcsInN1YiI6IjY1NWVlMTQxMjQ0MTgyMDBjYTc1OGNlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._5am4jD-PMi-i63jiF5rtndOGfKgPRNjogC0CEL802c'
    }

  response = requests.get(url = url, headers=headers)

  df =pd.DataFrame(response.json()['results'])

  df = df[[ 'id', 'title', 'original_title', 'overview','adult',
         'original_language',
       'popularity', 'release_date', 'vote_average',
       'vote_count']]

  Final_Data = pd.concat([Final_Data, df], ignore_index= False)

print(Final_Data.shape)

#Save The File
Final_Data.to_csv('tmdb_movies.csv', index =  False)