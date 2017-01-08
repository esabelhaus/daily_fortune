from subprocess import Popen
from subprocess import PIPE


def get_fortune():
    fortune = ''
    author = ''

    getting_fortune = True

    while (getting_fortune):
        with Popen(['fortune'], stdout=PIPE) as proc:
            fortune = str(proc.stdout.read(), 'utf-8')

        cleaned_fortune = fortune.strip('\\n\\t').rsplit('--')
        fortune = cleaned_fortune[0]

        try:
            author = cleaned_fortune[1]
        except:
            pass

        if ('' == author):
            author = " unknown"

        author = '--' + author

        if (140 >= len(fortune) + len('\n' + author)):
            getting_fortune = False
        else:
            fortune = ''
            author = ''

    return fortune + '\n' + author

print(get_fortune())
