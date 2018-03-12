# game_of_drones
## Build Setup

``` bash

#Make sure you have installed python3 and virtualenv in your machine
https://www.python.org/downloads/
https://virtualenv.pypa.io/en/stable/installation/

#Create virtualenv for the project
virtualenv -p python3 <virtualenvName>

#Activate your virtualenv
source <virtualenvName>/bin/activate

#Enter into the project folder
cd game_of_drones

#Install dependencies
pip install -r requirements.txt 

#Run de project
python manage.py runserver

#To run unittests
python manage.py test

