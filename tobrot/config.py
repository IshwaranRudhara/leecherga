import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1494936760:AAEBU-KROFifr5TrjqdPimR7-12RoaVeXvE"
    # The Telegram API things
    APP_ID = 1640301
    API_HASH = "a4041a10f706bc95285393d871357007"
    OWNER_ID = 1382991744
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001273851623, -1001398883981]
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = 6800
    EDIT_SLEEP_TIME_OUT = 15
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 600
    MAX_TG_SPLIT_FILE_SIZE = 2097152000
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "█"
    UN_FINISHED_PROGRESS_STR = "░"
    # add offensive API
    TG_OFFENSIVE_API = None
    CUSTOM_FILE_NAME = ""
    LEECH_COMMAND = "leech@Leeching_Robot"
    YTDL_COMMAND = "ytdl@Leeching_Robot"
    RCLONE_CONFIG = ""
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    GLEECH_COMMAND = "gleech"
    INDEX_LINK = ""
    TELEGRAM_LEECH_COMMAND_G = "tleech"
    CANCEL_COMMAND_G = "cancel@Leeching_Robot"
    GET_SIZE_G = "getsize"
    STATUS_COMMAND = "status@Leeching_Robot"
    SAVE_THUMBNAIL = "savethumbnail@Leeching_Robot"
    CLEAR_THUMBNAIL = "clearthumbnail@Leeching_Robot"
    UPLOAD_AS_DOC = "True"
    PYTDL_COMMAND_G = "pytdl@Leeching_Robot"
    LOG_COMMAND = "log"
    CLONE_COMMAND_G = "gclone"
    UPLOAD_COMMAND = "upload"
    RENEWME_COMMAND = "renewme"
