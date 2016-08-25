# microbe_toolbox

git garbage:
I needed to do the following to connect to git from the RCF:
$ git remote set-url origin https://username:userpwd@github.com/user/repo.git


# To run the tests:
(do this once!)
$ pip install nose
Then run the tests with:
$ nosetests
This will run all the functional tests for the project.  Make sure they all pass before you install!

# To install:
$ pip install .
OR (Dev install use a symlink so you can modify stuff)
$ pip install -e .
