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

    # Індивідуальна частина
    def get_emojis(self):
        return requests.get('https://api.github.com/emojis').json()

    def get_commits(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        return r.json()
