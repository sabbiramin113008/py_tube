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