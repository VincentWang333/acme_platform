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

## API Documentation
```
# GET /devices/ ->  get all device common data which only include track_id, device_type, loc_lat, loc_lng
# DELETE /devices/<track_id> ->  delete all the data of a speific device of given track_id
# PATCH /devices/cars/<track_id> -> update a specific device's state of given track_id
#GET /devices/cars/ -> get all specific type devices' (cars) detailed info list 
                       (except common data, there are more car related data such as fluid level, engine temp etc)
#POST /devices/cars/ -> add a new specific type (car) of device 
#GET /devices/fridges/ -> get all specific type devices' (fridges) detailed info list
                          (except common data, there are more fridge related data such as ice level, water leak etc.)
#POST /devices/fridges/ -> add new specific type (fridges) device 
```
Since this api havs only two device type implemented, only car list, fridge list and all device list can be retrived. 

