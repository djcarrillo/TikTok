import os
import time
import pandas as pd
from TikTokApi import TikTokApi

path_base = os.path.dirname(os.path.realpath(__file__))

# use_selenium=True, executablePath=f'{path_base}/controller/chromedriver'

if __name__ == "__main__":
    number_video = 1
    scraper = []
    offset = 0
    with TikTokApi() as api:
        temas = ['petro','fico']
        for tema in temas:
            while offset < number_video:
                for video in api.search.videos(search_term=tema, count=number_video, offset=offset):
                    metadata = {'tema': 'petro',
                                'create_video': video.create_time,
                                'video_id': video.id,
                                'author': video.as_dict['author'],
                                'hashtags': video.hashtags,
                                'desc': video.as_dict['desc'],
                                '_browser': getattr(video.parent, '_browser'),
                                'lenguage': getattr(video.parent, '_language'),
                                'time_zone': getattr(video.parent, '_timezone_name'),
                                'source': getattr(video.parent, '_user_agent'),
                                'stats': video.stats}

                    for key, value in metadata.items():
                        if '|' in str(value):
                            metadata[key] = str(value).replace('|', '-')
                    scraper.append(metadata)
                offset = offset + 400
                time.sleep(5)

    df = pd.DataFrame(scraper)
    df.to_csv('data_big_data_result.csv', sep='|', encoding='utf-8')
