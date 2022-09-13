import os
from typing import Optional, Union

import github
from github.Repository import Repository


def get_repo(repo: str) -> Repository:
    assert repo, 'repository name is missing'
    g = github.Github(os.environ['GITHUB_TOKEN'])
    return g.get_repo(repo)


def upsert_file(
    name: str,
    body: str,
    message: Optional[str] = None,
    *,
    repo: Optional[Union[Repository, str]] = None,
    branch: Optional[str] = "main",
    verbose: Optional[bool] = False,
):
    r = repo if isinstance(repo, Repository) else get_repo(repo)
    try:
        description_ = message or f'Update {name}'
        current = r.get_contents(name, ref=branch)
        current = r.update_file(
            current.path,
            description_,
            body,
            current.sha,
            branch=branch,
        )
        if verbose:
            print(current)
    except github.GithubException:
        message = message or f'Create {name}'
        created = r.create_file(name, message, body, branch=branch)
        if verbose:
            print(created)


def delete_file(
    name: str,
    message: str = None,
    *,
    repo: Optional[Union[Repository, str]] = None,
    branch: str = "main",
    verbose: Optional[bool] = False,
):
    r = repo if isinstance(repo, Repository) else get_repo(repo)
    message = message or f'Delete {name}'
    current = r.get_contents(name, ref=branch)
    deleted = r.delete_file(
        current.path,
        message,
        current.sha,
        branch=branch,
    )
    if verbose:
        print(deleted)


assert os.getenv('GITHUB_TOKEN'), 'Set GITHUB_TOKEN'

repo = "<YOUR_GITHUB_NAME>/<REPO_NAME>"

upsert_file("README.md", "NEW BODY", repo=repo, verbose=True)
upsert_file("README.md", "UPDATED BODY", repo=repo, verbose=True)

delete_file("README.md", repo=repo, verbose=True)
