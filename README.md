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
- `-w 2` - The Number of Workers, as it is 2 in this setup. ( Please change accordingly).

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
  "count": 30,
  "models": [
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 1912,
      "created": "Tue, 22 Jun 2021 20:20:32 GMT",
      "dislike_count": 124,
      "duration": 100,
      "fetch_count": 2,
      "id": 2,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 11647,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'justin gaethje', 'ufc 254', 'khabib nurmagomedov', 'eagle fc', 'eagle fc mma', 'eagle fighting championship', 'eagle fc 37', 'хабиб eagle', 'ufc 205', 'хабиб', 'хабиб нурмагомедов', 'хабиб алматы']",
      "title": "Khabib Nurmagomedov explains why he felt bad hurting Justin Gaethje and Michael Johnson",
      "video_id": "YrKIgalEgdo",
      "view_count": 334305
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 1298,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 112,
      "duration": 113,
      "fetch_count": 2,
      "id": 6,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 8333,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Khabib - 'Steer fattening, cows and greenhouses... that's what I am going to do now'",
      "video_id": "XzzF5GAcyt4",
      "view_count": 405097
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 947,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 183,
      "duration": 106,
      "fetch_count": 2,
      "id": 7,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 14180,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'ufc 254', 'khabib nurmagomedov', 'abdulmanap', 'nurmagomedov']",
      "title": "Abdulmanap Nurmagomedov’s words on Khabib’s retirement",
      "video_id": "17bh1pskCVg",
      "view_count": 486560
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 888,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 132,
      "duration": 254,
      "fetch_count": 2,
      "id": 8,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 6930,
      "tags": "['Khabib', 'UFC 249', 'Khabib Nurmagomedov', 'UFC', 'MMA', 'Xабиб', 'Нурмагомедов', 'Хабиб Нурмагомедов', 'Абдулманап', 'Абдулманап Нурмагомедов', 'Abdulmanap', 'Abdulmanap Nurmagomedov']",
      "title": "Abdulmanap Nurmagomedov speaks on Khabib's childhood [Part 1]",
      "video_id": "_v-vIsleRVM",
      "view_count": 405930
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 462,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 31,
      "duration": 114,
      "fetch_count": 2,
      "id": 9,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2061,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'khabib nurmagomedov', 'floyd mayweather', 'khabib vs floyd mayweather', 'eagle fc 36', 'eagle fc mma', 'eagle fc']",
      "title": "'Saudi Arabia offered to host Floyd Mayweather fight' - Khabib Nurmagomedov",
      "video_id": "g9WlFmM8p4Y",
      "view_count": 134148
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 465,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 35,
      "duration": 431,
      "fetch_count": 2,
      "id": 12,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 3088,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Daniel Cormier talks Khabib return, Conor McGregor and Umar Nurmagomedov's potential",
      "video_id": "h2kTXBF1vf4",
      "view_count": 154299
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 696,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 187,
      "duration": 132,
      "fetch_count": 2,
      "id": 13,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 4953,
      "tags": "['khabib nurmagomedov', 'mma news', 'Khabib', 'Conor McGregor', 'McGregor', 'abdulmanap nurmagomedov', 'abdulmanap nurmagomedov training', 'abdulmanap nurmagomedov interview', 'Dagestan', 'абдулманап нурмагомедов', 'Хабиб', 'Хабиб Нурмагомедов', 'дагестан', 'UFC', 'MMA', 'ММА']",
      "title": "'McGregor's a showman, I never considered him a top opponent': Abdulmanap Nurmagomedov",
      "video_id": "6w2vlwSXcSY",
      "view_count": 298023
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 1454,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 310,
      "duration": 140,
      "fetch_count": 2,
      "id": 14,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 10486,
      "tags": "['khabib nurmagomedov', 'mma', 'мма', 'mixed martial arts', 'ultimate fighting championships', 'Conor McGregor', 'McGregor', 'khabib mcgregor', 'khabib conor', 'mcgregor vs khabib', 'Khabib', 'Nurmagomedov', 'Хабиб', 'Хабиб Конор', 'Хабиб Нурмагомедов', 'Хабиб МакГрегор', 'ufc 229', 'ultimate fighting championship']",
      "title": "'I don't like hurting people, but I enjoyed smashing McGregor' - Khabib Nurmagomedov",
      "video_id": "WEnHz5twmo8",
      "view_count": 528529
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 311,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 31,
      "duration": 102,
      "fetch_count": 2,
      "id": 15,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1937,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'mma news', 'dana white', 'khabib nurmagomedov', 'EFC', 'eagle fighting championship', 'eagle fight', \"khabib's promotion\", 'khabib business', 'RT Khabib']",
      "title": "Khabib gives details about his conversation with Dana White following EFC event",
      "video_id": "x0qv4J3U5Sk",
      "view_count": 72826
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 135,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 17,
      "duration": 146,
      "fetch_count": 2,
      "id": 19,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1568,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'Khamzat', 'Chimaev', 'Daniel Cormier', 'dc and helwani', 'espn mma', 'mma news']",
      "title": "'Good luck with Khamzat to anyone fighting him' - Daniel Cormier",
      "video_id": "pN-aB2z2Ym0",
      "view_count": 87837
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 164,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 11,
      "duration": 142,
      "fetch_count": 2,
      "id": 20,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1676,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Khabib hails 'important family victory' following Umar Nurmagomedov debut UFC win",
      "video_id": "ormFogckcq4",
      "view_count": 62083
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 1088,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 157,
      "duration": 215,
      "fetch_count": 2,
      "id": 23,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 12721,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Khabib Nurmagomedov's final octagon entrance at UFC 254",
      "video_id": "q9RcAzy-BvM",
      "view_count": 572535
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 190,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 9,
      "duration": 145,
      "fetch_count": 2,
      "id": 24,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 961,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Khabib talks difference between US and Dagestan wrestling, Gaethje and Conor",
      "video_id": "MOESiWElTrY",
      "view_count": 43391
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 962,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 74,
      "duration": 167,
      "fetch_count": 2,
      "id": 25,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 3355,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'khabib nurmagomedov', 'conor mcgregor', 'dustin poirier']",
      "title": "Khabib: 'I choked McGregor & Poirier out... why would I fight them again?'",
      "video_id": "ZRIC-aQDUtI",
      "view_count": 157580
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 426,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 30,
      "duration": 158,
      "fetch_count": 2,
      "id": 27,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1989,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'khabib nurmagomedov', 'mixed martial arts', 'dana white', 'mma news', 'ufc 254', 'khabib nurmagomedov highlights']",
      "title": "Khabib details his plan to about Eagle Fighting Championship!",
      "video_id": "Y7y8cOoUrj4",
      "view_count": 102048
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 318,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 70,
      "duration": 246,
      "fetch_count": 2,
      "id": 28,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2739,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'McGregor', 'Daniel Cormier', 'khabib nurmagomedov', 'conor mcgregor', 'ufc 229']",
      "title": "'I want to see Khabib fighting McGregor again' - Daniel Cormier",
      "video_id": "Qm-wuQQrUYk",
      "view_count": 111924
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 393,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 51,
      "duration": 243,
      "fetch_count": 2,
      "id": 29,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 3381,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'khamzat', 'chimaev']",
      "title": "Daniel Cormier talks wrestling Khamzat Chimaev at UFC Fight Island",
      "video_id": "sMa7m7g_lBs",
      "view_count": 219605
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 369,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 60,
      "duration": 159,
      "fetch_count": 2,
      "id": 30,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 3677,
      "tags": "['Islam Makhachev', 'Khabibs gym', 'khabib gym workout', 'khabib gym training', 'khabib gym dagestan', 'Дагестан', 'Dagestan', 'dagestan basketball', 'dagestan chronicles', 'Dagestan land of warriors', 'land of warriors', 'islam makhachev mma', 'islam makhachev mma fight', 'islam makhachev mma record', 'javier mendez', 'mixed martial arts', 'khabib nurmagomedov']",
      "title": "Islam Makhachev: 'We can't have only fighters, we need doctors too'",
      "video_id": "npNisA9vFBQ",
      "view_count": 177719
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 477,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 36,
      "duration": 266,
      "fetch_count": 2,
      "id": 33,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2863,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "'I am still here, unfortunately for my opponents!' - Khamzat Chimaev talks Covid-19 recovery",
      "video_id": "PGE8yKkjW-w",
      "view_count": 126270
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 1707,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 313,
      "duration": 153,
      "fetch_count": 2,
      "id": 34,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 10460,
      "tags": "['Conor McGregor', 'Tony Ferguson', 'UFC LIghtweight', 'Хабиб', 'Дагестан', 'Хабиб Нармегомедов', 'dana white', 'mma news', 'mixed martial arts', 'synergy forum khabib', 'synergy forum spb', 'synergy forum 2019', 'khabib nurmagomedov', 'ultimate fighting championship']",
      "title": "Khabib Nurmagomedov: 'Ferguson fight will happen next, McGregor should deserve it'",
      "video_id": "pdY-wMQRMPI",
      "view_count": 626860
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 227,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 20,
      "duration": 222,
      "fetch_count": 2,
      "id": 35,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1648,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'islam makhachev', 'khabib nurmagomedov', 'eagle fc', 'ислам махачев', 'ислам махачев дрю добер полный бой', 'ислам махачев последний бой', 'Дагестан', 'Land of Warriors', 'Dagestan land', 'dagestan land of warriors', 'dagestan land of warriors episode 4', 'dagestan land of warriors episode 3']",
      "title": "'None of us want Khabib to come back' - Islam Makhachev",
      "video_id": "nvmLjStXnso",
      "view_count": 87537
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 233,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 19,
      "duration": 367,
      "fetch_count": 2,
      "id": 36,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1853,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "'Dana told us to fight again in March' - Umar Nurmagomedov post-UFC victory",
      "video_id": "Ux37NjXbzZ4",
      "view_count": 89009
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 380,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 26,
      "duration": 475,
      "fetch_count": 2,
      "id": 40,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2103,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'Javier Mendez', 'Nurmagomedov', 'Conor McGregor', 'McGregor', 'Umar Nurmagomedov', 'american kickboxing academy', 'ufc news', 'khabib nurmagomedov']",
      "title": "Javier Mendez talks Umar Nurmagomedov UFC debut, Khabib's comeback & McGregor",
      "video_id": "bnfQMF1bZYE",
      "view_count": 66124
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 248,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 67,
      "duration": 906,
      "fetch_count": 2,
      "id": 42,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2879,
      "tags": "['Dagestan', 'MMA', 'UFC', 'Khabib', 'Khabib Nurmagomedov', 'Umar', 'Umar Nurmagomedov', 'Timur Valiev', 'Dagestan Land of Warriors', 'Land of Warriors', 'Dagestan Chronicals', 'Дагестан', 'Хабиб', 'Хабиб Нурмагомедов', 'Умар Нурмагомедов', 'ММА', 'Тимур Валиев', 'GFC', 'MMA documentary', 'anatomy of a fighter']",
      "title": "Dagestan: Land of Warriors – Fight Night (Episode 3)",
      "video_id": "gUsF35fZuN8",
      "view_count": 145244
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 619,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 88,
      "duration": 187,
      "fetch_count": 2,
      "id": 45,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2937,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "'Mateusz, brother, it wasn't my fight': Guram Kutateladze reacts to his victory over Gamrot",
      "video_id": "dUbmUWaA1bo",
      "view_count": 321434
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 959,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 372,
      "duration": 698,
      "fetch_count": 2,
      "id": 46,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 10524,
      "tags": "['Dagestan', 'UFC Khabib', 'Хабиб', 'Нурмагомедов', 'Хабиб Нурмагомедов', 'Умар Нурмагомедов', 'Umar Nurmagomedov', 'Дагестан', 'Dagestan Land of Warriors', 'ufc embedded', 'zubaira tukhugov', 'зубайра тухугов', 'зубайра', 'dagestan chronicles', 'anatomy of a fighter', 'Dagestan MMA', 'abdulmanap nurmagomedov', 'will harris productions', 'land of warriors', 'timur valiev', 'khabib nurmagomedov']",
      "title": "Dagestan: Land of Warriors – Nurmagomedov Jr. (Episode 2)",
      "video_id": "-Z9heFkh80k",
      "view_count": 894642
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 263,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 22,
      "duration": 202,
      "fetch_count": 2,
      "id": 48,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 1098,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "'Sean O'Malley went silent, I should call out someone else' - Said Nurmagomedov",
      "video_id": "lg4pRARbgfs",
      "view_count": 95124
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 484,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 48,
      "duration": 123,
      "fetch_count": 2,
      "id": 49,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2440,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'UFC 254', 'Daniel Cormier']",
      "title": "Daniel Cormier breaks down Khabib vs. Gaethje fight",
      "video_id": "V5JjMaibH4U",
      "view_count": 119852
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 462,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 31,
      "duration": 285,
      "fetch_count": 2,
      "id": 50,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 4064,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport']",
      "title": "Khabib's advice to youth: 'Be grateful for what you have now!'",
      "video_id": "kvBSjKjykP4",
      "view_count": 87459
    },
    {
      "channel_id": "UC1ZRNf5khuJFrtacQsFqV6w",
      "comment_count": 390,
      "created": "Tue, 22 Jun 2021 21:28:01 GMT",
      "dislike_count": 15,
      "duration": 72,
      "fetch_count": 2,
      "id": 51,
      "last_edited": "Wed, 23 Jun 2021 02:44:43 GMT",
      "like_count": 2222,
      "tags": "['UFC', 'Khabib', 'MMA', 'RT Sport', 'khabib nurmagomedov', 'khabib nurmagomedov vs dustin poirier', 'Eagle FC', 'eagle fc mma', 'Eagle FC 37', 'khabib eagle fighting championship', 'khabib eagle highlights', 'Хабиб eagle', 'logan paul']",
      "title": "'Floyd Mayweather vs Logan Paul was purely business' - Khabib Nurmagomedov",
      "video_id": "SRL8zcr4Y6I",
      "view_count": 91475
    }
  ]
}
```

### Optimizing API Call to Update Video Analytics (Pseudo Algo ( Implemented)
--------------------------------------------------
Quota limit of Youtube V3 API is 10K Per Day for free tier. So it is important to keep the track of the quota count so as to
call the API efficiently.

1. First, after each `CRON_INTERVAL`, the remaining API quota limit is calculated.
2. Also the `total_video_count` is also fetched.
3. Now, the `remaining_call_count` is calculated as
`remaining_call_count` = `API_CALL_MAX_LIMIT` - `total_quota_spent` ( the current day)
4. If
```json
total_video_count > remaining_call_count:
possible_call_count = total_video_count - remaining_call_count
videos = Video.select().paginate(1, possible_call_count) sorted by `last_edit` and `view_count`
```
then, only `videos` are updated.
5. Else, all the videos are updates as the `remaining_call_count` is greater than the `total_video_count`.




