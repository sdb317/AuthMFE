# AuthMFE
A micro-front-end for adding basic username/password authentication to any site


## Server

Django with an SQLite database is used to provide the back-end functionality. DRF is used for the REST api.

The following environment variables are required before running the server:

-  ```set DJANGO_SETTINGS_MODULE=server.settings.production```
- ``` set SECRET_KEY=```"Add Your Own Key Here"


Any 'superuser' can use the built-in Django admin functionality to create/delete users via the ```admin/``` URL.

The server also servers up a 'demo ' ```index.html``` from the root path.

The two REST endpoints are:

- ```api/v1/users/login/```, which takes ```application/x-www-form-urlencoded``` username & password
- ```api/v1/users/logout/```

They are called using the HTTP 'POST' method.


## UI

The demo page loads the custom element definition in ```auth.js``` and embeds it as ```<mfe-auth/>```.

A custom event, ```mfe-auth-changed```, is fired whenever the authenticated state changes. This can be used to retrieve the user data via ```event.target.getUser()``` and ```event.target.isAuthenticated()```.


