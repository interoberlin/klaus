#!/usr/bin/python2.6

TITLE = u"git.interoberlin.de"
PATH_TO_REPOS = u"/home/git/" # end with "/"

# search for git repos in path_to_repos
def isGit(path):
	ends_with_git = len(path) > 4 and path[-4:] == '.git'
	blacklisted = False
	return ends_with_git and not blacklisted

from os import listdir
REPOSITORIES = [PATH_TO_REPOS+repo for repo in filter(isGit, listdir(PATH_TO_REPOS))]

# don't include blacklisted repos
REPOSITORIES.remove('/home/git/tools.git')
REPOSITORIES.remove('/home/git/cardsuilib.git')

# klaus provides a make_app function that creates a WSGI application
# Don't forget to add the path to klaus to WSGIPythonPath in your Apache config
import sys
sys.path.append('/usr/local/lib/python2.6/dist-packages')
sys.path.append('/opt/klaus')
sys.path.append('/opt/klaus/klaus')
from klaus import make_app

# Export WSGI application
application = make_app(REPOSITORIES, TITLE)

