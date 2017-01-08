from TwitterAPI import TwitterAPI
from subprocess import Popen
from subprocess import PIPE
import configparser
import os

# create a config object
config = configparser.ConfigParser()
# get the current directory of THIS file at runtime
dir_path = os.path.dirname(os.path.realpath(__file__))

# read in configuration file
config.read(dir_path + '/config/auth')

# populate auth block from config
consumer_key =         config['twitter']['c_key']
consumer_secret =      config['twitter']['c_secret']
access_token_key=api = config['twitter']['a_key']
access_token_secret =  config['twitter']['a_secret']

# method will return a string containing a fortune quote and author no longer than 140 characters in length
def get_fortune():
    # instance methods for population
    fortune = ''
    author = ''

    # operation boolean
    getting_fortune = True

    # iterate until you find a valid fortune within parameters
    while (getting_fortune):
        with Popen(['fortune'], stdout=PIPE) as proc:
            fortune = str(proc.stdout.read(), 'utf-8')

        # strip newline and tab characters, split at author block
        cleaned_fortune = fortune.strip('\\n\\t').rsplit('--')
        fortune = cleaned_fortune[0]

        # see whether there is an author
        try:
            author = cleaned_fortune[1]
        except:
            pass

        # if no author exists, list as unknown
        if ('' == author):
            author = " unknown"

        # differentiate author string
        author = '--' + author

        # find length of string
        if (140 >= len(fortune) + len('\\n' + author)):
            getting_fortune = False
        else:
            fortune = ''
            author = ''

    # return the fortune string
    return fortune + '\n' + author

# instantiate twitter api using auth block above
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# post the fortune
todays_fortune = api.request('statuses/update', {'status':get_fortune()})

# print success statement for logging as part of crontab
print(todays_fortune.status_code)
