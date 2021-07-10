# Logging
## Why use it?
- Get to know what is happening in your script
- prints() are can be usefull while short development but in prod they are a pain!
- changing the logging level is fast and changes the amount and importants of outputs
- Is not slower than prints but more flexible and Prod-prove ;) 

## Logging levels and when to use which?
Taken from [Fanpelin]( https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/)

|Name| Numerical Value | what to be used for     |
| ---  | ---- | --- |
| DEBUG | 10 | details, internal ste of loop, ... |
| INFO | 20 | handling requests or server state changed |
| WARNING | 30 | needs your attention, nut not an errer, user attempts to log in with a wrong password
| ERROR | 40 | exception is thrown, IO operation failure or connectivity issue
| CRITICAL | 50 | something horrible happels, out of memory, disk is full or nuclear meltdown

## Useful Links
- [Fanpelin]( https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/)
- [Python Docs](https://docs.python.org/2/library/logging.html)
- [Real Python](https://realpython.com/python-logging/)