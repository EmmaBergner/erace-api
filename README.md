# erace-api

Project description 

....


## User stories 

- As a user I should be logged in to access the site.
- As a user I want a friendly interface.
- As a user I want to be able to edit the race I have added.
- As a user I want to be able to see all information about a race and add to it.
- As a user I want to be able to see the races I am interested in.
- As a user I want to be able to search on a country to see upcoming races in that specific country.
- As a user I want to be able to see my past and upcoming races.
- As a user I want to be able to sign up and to sign in with username and password so that I can access my account.
- As a user I want to be able to add a race I’m interested in, I will attend or I want to recommend.
- As a user I want to be able to mark races so that I can easily see the ones I’m interested in or will attend.
- As a user I want to be able to see details about my next upcoming race so that I get an extra push.
- Add a README file.

## Entity Relationship Diagram

![Entity Relationship Diagram](documentation/entity.png)

## Model and CRUD breakdown 

| Model | Endpoints | Create | Retrieve | Update | Delete | Filter | Text search |
|-----|-----|-----|-----|-----|-----|-----|-----| 
| User | users/ users/:id/ | Yes | Yes | Yes | No | No | No |
| Profile | profiles/ profiles/:id/ | Yes (auto) | Yes | Yes | No | No | No |
| Race | races/ races/:id/ | Yes | Yes | Yes | No | Star Run | Country |
| Comment | comments/ comment/:id/ | Yes | Yes | No | Yes | Run | No |
| Run | runs/ runs/:id/ | Yes | Yes | No | Yes | No | No |
| Star | stars/ stars/:id/ | Yes | Yes | No | Yes | No | No |

## Tests

Logged in users can: 
- create a race/comment/run/star
- update a race they own

Logged in users can't:  
- update a race they don't own
- update a comment/run/star

Logged out users can:  
- list races/comments/runs/stars
- retrieve a race/comment/run/star with a valid id

Logged out users can't:  
- create a race/comment/run/star
- retrieve a race/comment/run/star with an invalid id

Tests were preformed using Postman and the Erace application frontend.

## Pre-deployment checklist

Set default renderer to JSON 
- Verify that Procfile contains correct release and web commands
- Verify that DEBUG is set to False
- Verify that requirements.txt is up to date.

## Deployment steps

The application is deployed on Heroku.

The following environment variables are defined:

| Variable | Value |
|-----|-----| 
| ALLOWED_HOST | erace-api.herokuapp.com |
| CLIENT_ORIGIN | https://erace-client.herokuapp.com |
| CLOUDINARY_URL | cloudinary://... |
| SECRET_KEY | ... |



