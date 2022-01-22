#https://gitpython.readthedocs.io/en/stable/tutorial.html
# > python3.6.2

import git

PATH = "E:\\divyaprojects\\visualpathdevops\\class17\\sample_repo"
GIT_CLONE_URL = "https://gitlab.com/pavan-projects/april_come.git"
BRANCH_NAME = "automation_branch"

#clone step

try:
    repo = git.Repo.clone_from(GIT_CLONE_URL, PATH)
except git.exc.GitCommandError:
    repo = git.Repo(PATH)


try:
    repo.git.checkout("-b", "devops_branch")
except git.exc.GitCommandError:
    repo.git.checkout("devops_branch")


try:
    repo.git.add("--all")
    repo.git.commit('-m', "sample commit", author="parameswara.kuna@gmail.com")
except git.exc.GitCommandError:
    print("noting to add")



origin = repo.remote(name="origin")
origin.push()







