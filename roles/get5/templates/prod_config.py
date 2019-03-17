SQLALCHEMY_DATABASE_URI = 'mysql://get5:{{ mysql_password }}@database/get5'  # Sqlalchemy database connection info
STEAM_API_KEY = '{{ steam_api_key }}'  # See https://steamcommunity.com/dev/apikey

##### Everything below this line is optional to change

import os

SECRET_KEY = os.environ['FLASK_SECRET']  # Secret key used for flask cookies

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..', 'logs'))
LOG_PATH = os.path.join(location, 'get5.log')

DEBUG = False
TESTING = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
USER_MAX_SERVERS = 10  # Max servers a user can create
USER_MAX_TEAMS = 100  # Max teams a user can create
USER_MAX_MATCHES = 1000  # Max matches a user can create
DEFAULT_PAGE = '/matches'
ADMINS_ACCESS_ALL_MATCHES = False  # Whether admins can always access any match admin panel
CREATE_MATCH_TITLE_TEXT = False # Whether settings for "match title text" and "team text" appear on "create a match page"

# All maps that are selectable in the "create a match" page
MAPLIST = [
    'de_cache',
    'de_cbble',
    'de_inferno',
    'de_mirage',
    'de_nuke',
    'de_overpass',
    'de_train',
    'de_dust2',
    'de_season',
]

# Maps whose checkbox is selected (in the mappool) by default in the "create a match" page
DEFAULT_MAPLIST = [
    'de_cache',
    'de_dust2',
    'de_inferno',
    'de_mirage',
    'de_nuke',
    'de_overpass',
    'de_train',
]

# You may set the server to allow allow whitelisted steamids to login.
# By default any user can login and create teams/servers/matches.
WHITELISTED_IDS = []

# Admins will have extra access to create "public" teams, and if ADMINS_ACCESS_ALL_MATCHES
# is set, they can access admin info for all matches (can pause, cancel, etc.) ANY match.
ADMIN_IDS = []
