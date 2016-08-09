#!/bin/bash
sudo apt-get update
sudo apt-get -y install git-core python-dev libjpeg-dev zlib1g-dev libpng12-dev build-essential libpcre3 libpcre3-dev postgresql postgresql-contrib python-psycopg2 python libpq-dev



# sudo easy_install -U pip
# sudo pip install -r /vagrant/requirements.txt
# TODO
# Creating user and database in psql
# sudo -i -u postgres createdb light_it_db
# sudo -i -u postgres createuser -h localhost -S -D -R -e light_it_usr
# exit
# sudo -u postgres psql -U postgres -d postgres -c "alter user light_it_usr with password '1111';"
