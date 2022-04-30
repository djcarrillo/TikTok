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
        #    tag = api.hashtag(name="petro")
        #    print(tag.info())

        while offset < number_video:
            for video in api.search.videos(search_term='petro', count=number_video, offset=offset):
                # for video in api.hashtag(name='funny').videos():
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
                # video.stats
                scraper.append(metadata)

            for video in api.search.videos(search_term='fico', count=number_video, offset=offset):
                # for video in api.hashtag(name='funny').videos():
                metadata = {'tema': 'fico',
                            'create_video': video.create_time,
                            'video_id': video.id,
                            'author': video.as_dict['author'],
                            'hashtags': video.hashtags,
                            'desc': video.as_dict['desc'],
                            '_browser': getattr(video.parent, '_browser'),
                            'lenguage': getattr(video.parent, '_language'),
                            'time_zone': getattr(video.parent, '_timezone_name'),
                            'source': getattr(video.parent, '_user_agent'), 'stats': video.stats}

                for key, value in metadata.items():
                    if '|' in str(value):
                        metadata[key] = str(value).replace('|', '-')
                # video.stats
                scraper.append(metadata)
            offset = offset + 400
            time.sleep(5)

    df = pd.DataFrame(scraper)
    df.to_csv('data_big_data.csv', sep='|', encoding='utf-8')
    # video_bytes = api.video(id=video.id).bytes()
    # Saving The Video
    # with open('saved_video.mp4', 'wb') as output:
    #    output.write(video_bytes)
# for video in tag.videos():
#    print(video.id)
