# GitHub as a database

Related blog posts:

<https://dev.to/begoon/github-as-a-database-2g0m>

<https://medium.com/@ademin/github-as-a-database-73fa81e3cdcc>

I needed a way to keep information about certain important events in my code nicely saved for later analysis. What can be better than committing them to a VCS?

The little code below demonstrates how this approach works.

It needs two things to be set: GITHUB_TOKEN, which can be generated in your [GitHub account](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and the `repo` variable with the repository name.

It upserts a new file to create a file. Then it upserts it again to modify it. Then it deletes the file.

The repository log nicely keeps all these actions in the commit history.

Note: The PyGithub package needs to be installed first:

    pip instal pygithub

Execute it by:

    python main.py

It prints something like:

```
{'content': ContentFile(path="README.md"), 'commit': Commit(sha="a6c540fec9b1b02e21acbb0ddd790efb6b7cb33f")}
{'commit': Commit(sha="2436e7ff2692a9af398dabd9eb9d1eee0f821954"), 'content': ContentFile(path="README.md")}
{'commit': Commit(sha="31fefb51e3510071777e4f4c8a0971de0a184f78"), 'content': NotSet}
```

Go to your GitHub repository and check the commits.
