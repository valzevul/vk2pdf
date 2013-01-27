TEMPLATE = 'https://oauth.vk.com/authorize?client_id=%s\
&scope=%s&redirect_uri=%s&display=%s&response_type=token'


def get_token(APP_ID, SETTINGS, REDIRECT_URI, DISPLAY):
    print(TEMPLATE % (APP_ID, SETTINGS, REDIRECT_URI, DISPLAY))
    token = input()
    return token
