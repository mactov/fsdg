# fsdg

Fake Solar Data Generator

This project is a **REST API** to get some **fake (but possible) solar data**.

There are 2 endpoints at the moment:
* **/oneday** that returns a jsonified list of 144 measures for a full day looking 
like this:
[{"prod":0.0,"ts":"00:00"},
 {"prod":0.0,"ts":"00:15"},
 {"prod":0.0,"ts":"00:30"},
 ...
 {"prod":3208.5324,"ts":"07:30"},
 ...
 {"prod":0.0,"ts":"23:45"}]
* **/prod/hh:mm** that returns a dictionary like this:
 {'ts':'hh:mm', 'prod':val}
 
 There is a 5% probability of not getting any value (Well you get None then) and
 a 3% probability of getting a weird value.

## How to run the project:
It is a docker container, so you need docker installed on your machine.
Then, with admin rights, enter the following commands:
```
    docker build -t fsdg:latest .
    docker run -d -p 5000:5000 fsdg:latest
```
and go to `localhost:5000/oneday` to get a full one day dataset
 
 
 