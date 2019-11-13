#### Loftly Analytics Application 
Contains both frontend and backend code for the Loftly Analytics Application 
useful for collecting survey information from users about Loftly and improvements. 

### Setup the Development Enviroment 

Create a .env file in the project root.
```sh 
    # The .env file should contain 
    MONGO_URI = mongodb://localhost:27017
```

Start the Database
```sh 
    sudo mongod
    #MacOS Catalina:  sudo mongod -dbpath=/usr/local/var/mongodb
```
Start the actual application
```sh 
    # We recommend setting up a virtualenv before this
    pip install -r requirements.txt
    python app.py 
```