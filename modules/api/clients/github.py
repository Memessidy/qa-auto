import requests


class Github:

    def get_user(self, username):
        url = "https://api.github.com/users/" + username
        r = requests.get(url)
        body = r.json()
        return body

    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories',
                         params={'q': name})
        body = r.json()
        return body
