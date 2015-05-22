#!/bin/bash

mkvirtualenv video-store
pip install -r requirements.txt
./src/manage.py migrate
./src/manage.py createsuperuser