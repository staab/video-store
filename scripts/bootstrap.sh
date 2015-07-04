#!/bin/bash

sudo apt-get update && apt-get install -y ruby
gem install sass

mkvirtualenv video-store
pip install -r requirements.txt
./src/manage.py migrate
./src/manage.py createsuperuser