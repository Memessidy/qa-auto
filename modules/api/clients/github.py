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

    def get_commit_by_sha(self, owner, repo, sha):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}")
        return r.json()


if __name__ == '__main__':
    g = Github()
    owner = 'Memessidy'
    repo = 'qa-auto'
    hash = '4071929a6f78368887fc30eda716c3d7f60d68a5'
    print(g.get_commit_by_sha(owner, repo, hash))
