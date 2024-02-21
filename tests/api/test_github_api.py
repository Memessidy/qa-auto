import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


# Індивідуальна частина
@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emojis()
    emoji_name = 'black_cat'
    assert r[emoji_name]


@pytest.mark.api
@pytest.mark.parametrize("owner,repo", [('Memessidy', 'qa-auto')])
def test_first_commit_exists(github_api, owner, repo):
    r = github_api.get_commits(owner, repo)
    assert r[-1]['commit']['author']['name'] == 'YehorMukomel'
    assert r[-1]['commit']['author']['email'] == 'mukomelegor@gmail.com'
    assert r[-1]['commit']['message'] == 'initial'


@pytest.mark.api
@pytest.mark.parametrize(
    "owner,repo,sha,expected_message", [('Memessidy', 'qa-auto', '27deed1a658b4a2d7e719745d83789c4e7251b7f',
                                         'rozetka tests has been added')])
def test_check_message_in_commit(github_api, owner, repo, sha, expected_message):
    msg = github_api.get_commit_by_sha(owner, repo, sha)['commit']['message']
    assert expected_message in msg


@pytest.mark.api
@pytest.mark.parametrize("owner,repo,sha", [('Memessidy', 'qa-auto', '43cac8bd7295612eab2c1fb534cf733d4327cf3e')])
def test_check_author_is_committer(github_api, owner, repo, sha):
    response = github_api.get_commit_by_sha(owner, repo, sha)
    committer = response['commit']['author']['name']
    author = response['commit']['committer']['name']
    assert committer == author
