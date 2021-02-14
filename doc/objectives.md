# Main modules

Server template (tornado): 
[https://github.com/pathscale/mach4-backend](https://github.com/pathscale/mach4-backend) 


## Server

 wrapper for [uWs](https://github.com/uNetworking/uWebSockets)<br>
 hint: [https://github.com/MadrinX/uWebSockets.py ](https://github.com/MadrinX/uWebSockets.py )

### objectives:
 - GIL-free connection handler
 - reasonable caching structure
 	- candidate: [robin-map](https://github.com/Tessil/robin-map) 
 - Request and response objects
 - Method forwarding
 - Optional tcp socket connection with other servers
 - High level wrapper to make it at least partly available from py interface


## Parser
[rapidjson](https://rapidjson.org/) -based<br>
hint: [https://github.com/python-rapidjson/python-rapidjson ](https://github.com/python-rapidjson/python-rapidjson ) 

### objectives:
 - DOM model instead of direct json -> object mapping
 - DOM model will be transferred into client request object
 - request pbject parameters should be limited to basic types, no high-level objects

## Database connector
GIL-free postgresql connector
### Candidate C/C++ libraries:
- [pgfe](https://github.com/dmitigr/pgfe/tree/master/lib/dmitigr) -> preferred (?)
- [libpq](https://www.postgresql.org/docs/12/libpq.html)  -> will end up as [psycopg2](https://github.com/psycopg/psycopg2) alternative
- ?

### Objectives
Focus on stored procedures (no ORM)
- expected input: stored procedure names and methods
- expected output: probably a similar DOM model as constructed for parser -> will be used internally os passed to response object