## Our workflow
- branch named "development" is our main branch, 
- whatever feature we do we need to make new branch from development (i suggest look on "git flow" to understand this process)
- master branch is only for relased version
- document everything <3

## our goals
>## Main modules
>
>Server template (tornado): 
>[https://github.com/pathscale/mach4-backend](https://github.com/pathscale/mach4-backend) 


>## Server
>
> wrapper for [uWs](https://github.com/uNetworking/uWebSockets)<br>
> hint: [https://github.com/MadrinX/uWebSockets.py ](https://github.com/MadrinX/uWebSockets.py )

>### objectives:
> - GIL-free connection handler
> - reasonable caching structure
> 	- candidate: [robin-map](https://github.com/Tessil/robin-map) 
> - Request and response objects
> - Method forwarding
> - Optional tcp socket connection with other servers
> - High level wrapper to make it at least partly available from py interface


>## Parser
>[rapidjson](https://rapidjson.org/) -based<br>
>hint: [https://github.com/python-rapidjson/python-rapidjson ](https://github.com/python-rapidjson/python-rapidjson ) 

>### objectives:
> - DOM model instead of direct json -> object mapping
> - DOM model will be transferred into client request object
> - request pbject parameters should be limited to basic types, no high-level objects

>## Database connector
>GIL-free postgresql connector

>### Candidate C/C++ libraries:
>- [pgfe](https://github.com/dmitigr/pgfe/tree/master/lib/dmitigr) -> preferred (?)
>- [libpq](https://www.postgresql.org/docs/12/libpq.html)  -> will end up as >[psycopg2](https://github.com/psycopg/psycopg2) alternative
>- ?

>### Objectives
>Focus on stored procedures (no ORM)
>- expected input: stored procedure names and methods
>- expected output: probably a similar DOM model as constructed for parser -> will be used internally os passed to response object

## other help resources:
https://github.com/markojaadam/cython-lwan-fibo
https://github.com/pathscale/GameServers2

## template to follow as our goal lib how to use:
- ```b'{"method": 1, "params"{"test": "param"}}' -> request.get_parameter("test") -> "param"```
- >```{"method": 10000, "params":{"username": "krumplee", "password": "mypass"}}``` -> SignUp = 10000, username = "krumplee", password = "mypass", 
which schematically end up as ```signup(username="krumplee", password="mypass")``` in py
- schematically do the following: ```data, err = db.invoke("api.fun_autencicate", {"a_username": request.get_parameter("username", "a_password": request.get_parameter("password"))})``` -> if err: bye-bye, game over; else: ...get token from db for the selected service...

## TODOS:
- [ ] wrap [rapidjson](https://rapidjson.org/), https://rapidjson.org/md_doc_schema.html