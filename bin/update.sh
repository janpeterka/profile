#!/bin/bash

cd /home/profile/profile

# ensure to get origin's data and discard any local change
git fetch
git reset origin/production --hard
git pull

# update pipenv
pipenv sync

# upgrade database
# pipenv run flask db upgrade

