# mongodb-useful
Some useful mongodb commands to remember

## Start mongod process by issuing the following command
```
sudo systemctl start mongod
```

## verify if mongodb has started successfully
```
sudo systemctl status mongod
```

## start a mongosh shell
```
mongosh
```

## display the database you are using
```
db
```

## Create a new database
To create a new database, issue "use <db>" command with the database to be created

You can also create a new collection using "insertOne()". If the collection doesn't exist mongo DB creates it when you first store data on it
```
use myNewDatabase
db.myCollection.insertOne({x:1})
```
