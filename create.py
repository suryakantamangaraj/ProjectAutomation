import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('ap')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin git@github.com:{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

if __name__ == "__main__":
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    print("Succesfully created repository {}!".format(foldername))
    os.system('code .')
