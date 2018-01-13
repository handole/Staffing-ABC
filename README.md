## Staffing-ABC
is web app creating from django for seeking job seeker, the employee or client create a job and the applicant create resume.
Then, client lookings many resume for a match on to the job.

# How to use

# install python and virtual environment for ubuntu and mac, via terminal typing
- sudo apt-get update
- sudo apt-get install python3.6
- wget https://bootstrap.pypa.io/get-pip.py
- sudo python3.6 get-pip.py
- sudo pip3.6 install virtualenv

# create the root folder, eg / myapp then enter, inside the myapp folder, via terminal type command
- virtualenv venv -p python3.6

# then activate the virtual environment
- source venv/bin/activate
- deactivate (to exit the virtual environment)

# then, install the required python package in requirements.txt type command in the terminal (install all packages listed in requirements.txt)
- pip install -r requirements.txt

# create a migration
- python manage.py makemigrations
- python manage.py migrate

# create superuser, then terminal will redirect to fill
- python manage.py createsuperuser

# run app, to local with port 8000 (default)
- python manage.py runserver

# open the browser, and type the address
- localhost:8000
