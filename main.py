from auth import get_token
from secret import TOKEN
import vkontakte

APP_ID = '3385824'
SETTINGS = 'friends,messages,offline'
REDIRECT_URI = 'http://oauth.vk.com/blank.html'
DISPLAY = 'page'


def exist(TOKEN):
    return TOKEN != ''


def main():
    global TOKEN
    if not exist(TOKEN):
        TOKEN = get_token(APP_ID, SETTINGS, REDIRECT_URI, DISPLAY)
    else:
        vk = vkontakte.API(token=TOKEN)
        uid = input()
        messages = vk.messages.getHistory(uid=uid, count='200')
        for elem in range(messages[0], 1, -1):
            msg = messages[elem]['body'].replace('<br>', '\n')
            print(msg)

main()