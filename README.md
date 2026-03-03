# CMPS-394-Day 6


## Lab 1: Python FastAPI
- Follow this video: https://www.youtube.com/watch?v=iWS9ogMPOI0
- This is a good introduction to web APIs and python is simple enough to operate without getting overwhelmed by syntax
- Exit criteria:
	- Start up a localhost server
	- Define a GET, POST, and DELETE endpoint (you may need to branch out from the linked tutorial)
	- Dr. Russell, through the Swagger UI (if you choose to include it) or via `curl`, should be able to trigger these 3 endpoints. What they do is up to you. I would keep things simple and return a 200 status code until lab 2.

## Lab 2: Set up a SQL Server with FastAPI
- Optionally, watch this video: https://youtu.be/zzOwU41UjTM?si=TN8g5rKK7ab19mey
- This goes into FastAPI with MySQL. If you prefer another flavor of SQL or don't like this tutorial, that is fine. Google around for your own preference.
- Exit Criteria:
	- Start up a localhost server
	- Start up a database instance
	- A FastAPI instance with a GET, POST, and DELETE endpoint
	- Each endpoint MUST perform an associated operation in the database (GET an item, POST a new entry, DELETE an entry). Don't overcomplicate it.
	- If you locally installed the database instance, Dr. Russell may not be able to run it, so keep the code simple so he can verify it.

## Assignment: Tie it all together and containerize it
- Take what you did in labs 1 and 2 and containerize the web API and database using a docker compose file
- The database should store its data in a volume
- The exit criteria is no different from Lab 2, except now Dr. Russell should be able to run it via docker compose with no issues. A failing `docker compose up -d` command is an invalid submission.

 
 
