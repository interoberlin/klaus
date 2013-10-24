#!/usr/bin/python2.6

TITLE = u"interoberlin.de / git"

# A list of paths pointing to your git repositories
#REPOSITORIES = [
#    "/home/git/modelboat.git",
#]

def isGit(path):
	return len(path) > 4 and path[-4:] == '.git'

from os import listdir
REPOSITORIES = ['/home/git/'+r for r in filter(isGit, listdir('/home/git'))]

# klaus provides a make_app function that creates a WSGI application
import site
site.addsitedir('/usr/local/lib/python2.6/dist-packages')
from klaus import make_app

# Create the application
application = make_app(REPOSITORIES, TITLE)
