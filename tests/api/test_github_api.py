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
def test_emojis_count_more_than_one_thousand(github_api):
    emojis_length = len(github_api.get_emojis())
    assert emojis_length > 1000


@pytest.mark.api
def test_first_commit_exists(github_api):
    owner = 'Memessidy'
    repo = 'qa-auto'
    r = github_api.get_commits(owner, repo)
    assert r[-1]['commit']['author']['name'] == 'YehorMukomel'
    assert r[-1]['commit']['author']['email'] == 'mukomelegor@gmail.com'
    assert r[-1]['commit']['message'] == 'initial'
