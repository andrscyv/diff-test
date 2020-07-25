import git

repo = git.Repo(".", search_parent_directories=True)
hcommit = repo.head.commit
diff = hcommit.diff('HEAD~1')
print(diff)
