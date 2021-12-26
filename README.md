# ACME Platform

This project was generated with Django that default come with sqlite3

## Install dependencies

In order to locally run this backend server, open the terminal under this project folder, run 
```
pip3 install -r requirements.txt
```

## Build
Run the following command in terminal to build and init the associated database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

And finally, to fire up this server with sqlite3 database, run 
```
python3 manage.py runserver
```

