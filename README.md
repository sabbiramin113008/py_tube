## Sixads Video Fetcher 1.0
A Server application  with 'Fetch the Video with analytics' utility

## Environment Preparation

0. Make sure `venv` or any virtual environment is installed. If not, try,
`sudo apt-get install python3-venv` and also, please make sure the pip is upgraded to
the latest version.
If Not, then try `pip install ---upgrade pip`

1. If you are using `venv` make sure to activate it via `source venv/bin/activate`.
2. Make sure to install the exact same version of the modules docked in `requirements.txt`. Type
 `pip install -r requirements.txt` on terminal and you are ready to go.


## Creating Database
0. All the DB Credentials are kept in `.env` file and is `.gitignored`. `.ENV` file contains fields
```code
API_KEY=<youtube_api_key>
APP_SECRET=<app_secret_key>
DATABASE_NAME=<db_nam>
TEST_DATABASE_NAME=<test_db_name>
DATABASE_USER=<db_user_name>
DATABASE_PASSWORD=<db_password>
DATABASE_HOST=localhost
DATABASE_PORT=3306
DEFAULT_CHANNEL_ID=<default_channel_id>
```

1. To create tables please run `python ./init_db.py` file. Depending on the `APP_ENV`, you need to run this only once.
2. For the initial fetch, please run `python init_fetcher.py` to load all the videos of a particular channel ID.

### Setting Up the Cron JOB
 The Cron job (periodic vidoe analytics fetcher) is run as a background periodic task with the start of the
 application. Further configuration can be done in `./cron_handler.py`



### Running the Application.

0. Most of the Application level `configurations` can be found in `./app_config.py` File. Application can be run
in two `DEV` or `TEST` mode, make sure to set it before running, in `./app_config.py` file as `APP_ENV` value.

3. The main application can be run via Default Python Interpreter, so to follow,
 ` python wsgi.py` would launch the application.

### Running with Gunicorn
1. To run with Gunicorn, please type,

`gunicorn --bind localhost:5600 -w 2 wsgi:app`,

Here,
- `localhost` - the hostname (I kept it localhost, change it, if is required)
- `5600` - The Port No.
- `-w 2` - The Number of Workers, as it is 2 in this setup. ( Pleas change accordingly).

### Major Components
1. `API Server` that enlists videos with different filter option.
2. `Admin Dashboard`, a Minimal Flask Admin for Quick views, search, filter and edits.
3. `Cron JOB`, that periodically updates the latest analytics of the videos of a particular Youtube Channel.
4. `Fetcher Script`, that can be used to load, fetch and save Video with analytics.
5. `Unit Test`, of some of the base testing utility.


### API Doc
-------------------------------------
Insomnia API Collections are added in the `./insomnia_docs` dir. Just load them to play with.
### GET List Videos
#### HTTP Method:
GET
#### Request Header:
```code
Content-Type:application/json
```
#### API Path:
/api/v1/videos

#### Query Params:
1. `page`: (int) Page Number
2.  `size`: (int) Limit of the Returned results.
3.  `tags`: (str) String of tags, separated by comma.
4.  `view_count_lt`: (int) Total view count less than operative.
5.  `view_count_gt`: (int) Total view count greater than operative
6.  `view_count_eq`: (int) Total view count equal operative
7.  `like_count_lt`: (int) Total Like Count less than operative.
8.  `like_count_gt`: (int) Total Like Count greater than operative
9.  `like_count_eq`: (int) Total Like Count equal operative
10. `comment_count_lt`: (int) Total Comment count less than operative.
11. `comment_count_gt`: (int) Total Comment count greater than operative
12. `comment_count_eq`: (int) Total Comment count equal operative
13. `dislike_count_lt`: (int) Total Dislike Count less than operative.
14. `dislike_count_gt`: (int) Total Dislike Count greater than operative
15. `dislike_count_eq`: (int) Total Dislike Count equal operative

#### Sample API Query:
http://localhost:5003/api/v1/videos?view_count_gt=500&tags=MMA&like_count_gt=100&dislike_count_lt=500
#### Sample Response Body:
```json
{
"count": 1,
"models": [
{
  "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
  "comment_count": 124,
  "created": "Tue, 22 Jun 2021 21:28:01 GMT",
  "dislike_count": 9,
  "duration": 290,
  "fetch_count": 2,
  "id": 99,
  "last_edited": "Tue, 22 Jun 2021 23:22:34 GMT",
  "like_count": 1141,
  "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'abdulmanap']",
  "title": "'That was my first fight without Abdulmanap in my corner' - Tagir Ulanbekov",
  "video_id": "UDtmAKq_PZg",
  "view_count": 46394
}
]
}
```

### Optimizing API Call to Update Video Analytics.
--------------------------------------------------
Quota limit of Youtube V3 API is 10K Per Day for free tier. So it is important to keep the track of the quota count so as to
call the API efficiently.

First, after each `CRON_INTERVAL`, the remaining API quota limit is calculated.
Also the `total_video_count` is also fetched.
Now, the `remaining_call_count` is calculated as
remaining_call_count = API_CALL_MAX_LIMIT - total_quota_spent ( the current day)
If `total_video_count` > `remaining_call_count`:
    possible_call_count = total_video_count -remaining_call_count
    videos = Video.select().paginate(1, possible_call_count) sorted by `last_edit` and `view_count`
    then, only `videos` are updated.
else, all the videos are updates as the remaining_call_count is greater than the total_video_count.

