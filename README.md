# Welcome to Netflix Catalogue

Hi! This demo Django project provides you a public REST API where you can get all the Netflix titles currently available and it also fetches details on a title from IMDB.com.

This demo project is mainly intended to demonstrate functionalities in Django such as but not limited to, class-based and function-based REST APIs, Models migration, saving & queries, Serialization, Caching, Throttling, Parsers, Testing, Remote calls.

# 1. How it works?

This project is divided into 2 apps, namely:

 1. middleware 
 2. api
 
It also has a main app which has all the configs in `settings.py`.

## 1.1 middleware

This app acts as a middleware between the public APIs and the remote APIs. 

Since the remote APIs have limits on the number of calls we can make, I decided to create this layer to fetch all the titles in the remote API and store them in the local DB. This layer also stores title details from IMDB if it has already been fetched before. The middleware contains all logic for doing the remote calls, parsing and storing the results.

Additionally, this layer has result caching enabled on both APIs to speed up the response time. 

The remote APIs used are:

 1. watchmode (https://api.watchmode.com/) 
The watchmode APIs provides all the titles (Movies, TV Shows) currently available on Netflix.

 3. IMDB (https://imdb-api.com/)
The IMDB API fetches the details of a title such as rating, plot, runtime, etc.

## **1.2 api**
This app exposes 3 endpoints which the user/frontend application can call. I have enabled throttling to limit the call rate.

Its main purpose is to query the database to fetch all the titles and titles' details and return the results via a REST response in the form of json.

Note that I call the middleware in case the *title details* is missing to fetch them from imdb.

I have *intentionally* not called the middleware to get all titles from watchmode  (if it the db is empty) because it takes time to fetch all of them from the remote APIs. It is better to manually call the API - GET `/middleware/titles` first.
However, in this GitHub repo, I have already included a populated db.sqlite3 file, so no need to call it.

In production most likely the APIs will be called periodically to refresh the Titles in the db (it can be controlled by caching remote api calls and response every 5 mins for eg)

# 2. Database storage details

There are two models as follows:

 1. Title (**id**, tmdb_type, year, type, title_name, imdb_id)
 2. Imdb (**id**,  *title_id*, runtimeStr, plot, release_date, directors, imdb_rating, trailer, image)

# 3. Endpoints
Each of the two apps(api, middleware) exposes a REST API listed below. 

## 3.1 API Endpoints
These endpoints are intended to be used by the public or frontend user.

 1. Get all titles 
GET `/api/titles`   

 2. Get all titles by year and/or type
GET `/api/titles/?year=2022&type=tv`
GET `/api/titles/?year=2021&type=movie`

 3. Get title details (imdb) by id
  GET `/middleware/titles/6708`

## **3.2 Middleware Endpoints**

These endpoints are *not* intended to be used by the public user, but *for the admin* to prefetch all the titles from the watchmode APIs.

 1. Get all titles 
GET `/middleware/titles`   

 2. Get all titles by page number 
GET `/middleware/titles/2`

 3. Get imdb title details by imdb id
  GET `/middleware/title/tt11278476`


## 4. How to run the project?
This project can be run locally on a local development server as follows:

    $ python manage.py runserver
