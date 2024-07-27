# Importing Package
import pandas as pd

# Importing Youtube Data:
# Canada
canada_vids = pd.read_csv(
    'Raw Data/canada_videos.csv'
)
canada_vids['country'] = 'Canada'

# France
france_vids = pd.read_csv(
    'Raw Data/france_videos.csv'
)
france_vids['country'] = 'France'

# Germany
germany_vids = pd.read_csv(
    'Raw Data/germany_videos.csv'
)
germany_vids['country'] = 'Germany'

# India
india_vids = pd.read_csv(
    'Raw Data/india_videos.csv'
)
india_vids['country'] = 'India'

# Japan
japan_vids = pd.read_csv(
    'Raw Data/japan_videos.csv',
    encoding='ISO-8859-1'
)
japan_vids['country'] = 'Japan'

# Korea
korea_vids = pd.read_csv(
    'Raw Data/korea_videos.csv',
    encoding='ISO-8859-1'
)
korea_vids['country'] = 'Korea'

# Mexico
mexico_vids = pd.read_csv(
    'Raw Data/mexico_videos.csv',
    encoding='ISO-8859-1'
)
mexico_vids['country'] = 'Mexico'

# Russia
russia_vids = pd.read_csv(
    'Raw Data/russia_videos.csv',
    encoding='ISO-8859-1'
)
russia_vids['country'] = 'Russia'

# UK
uk_vids = pd.read_csv(
    'Raw Data/uk_videos.csv'
)
uk_vids['country'] = 'United Kingdom'

# US
us_vids = pd.read_csv(
    'Raw Data/us_videos.csv'
)
us_vids['country'] = 'United States'

# Combining the data into one Dataframe
df_list = [
    canada_vids,
    france_vids,
    germany_vids,
    india_vids,
    japan_vids,
    korea_vids,
    mexico_vids,
    russia_vids,
    uk_vids,
    us_vids
]
yt_videos = pd.concat(df_list, ignore_index=True, axis=0)

# Adding a category column for convenience during analysis
category_map = {
    1: 'Film and Animation',
    2: 'Autos and Vehicles',
    10: 'Music',
    15: 'Pets and Animals',
    17: 'Sports',
    19: 'Travels and Events',
    20: 'Gaming',
    22: 'People and Blogs',
    23: 'Comedy',
    24: 'Entertainment',
    25: 'News and Politics',
    26: 'Howto and Style',
    27: 'Education',
    28: 'Science and Technology',
    29: 'Nonprofits and Activism',
    30: 'Movies',
    43: 'Shows',
    44: 'Trailers'
}

yt_videos['category'] = yt_videos['category_id'].map(category_map)


# Cleaning the "trending_date" column
yt_videos['trending_date'] = yt_videos['trending_date']\
    .str.replace('.', '-')
yt_videos['trending_date'] = '20' + yt_videos['trending_date']

yt_videos['trending_date'] = yt_videos['trending_date'].str[0:5]\
                             + yt_videos['trending_date'].str[8:10]\
                             + yt_videos['trending_date'].str[4:7]

# Converting "trending_date" and "publish_time" column to datetime
yt_videos['trending_date'] = pd.to_datetime(yt_videos['trending_date'], yearfirst=True, ).dt.date
yt_videos['publish_time'] = pd.to_datetime(yt_videos['publish_time'])

# Creating a publish_date column
yt_videos['publish_date'] = yt_videos['publish_time'].dt.date

# Saving cleaned data for analysis
yt_videos.to_csv('youtube_videos.csv')