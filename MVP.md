<!-- (5 points): As a developer, I want to make good, consistent commits (at least 25 for the entire team for both the backend and frontend). You will create two repositories on GitHub – one for the frontend, and one for the backend -->

<!-- (5 points) As a developer, I want to setup the DRF JWT starter code and connect it to my MySQL database. -->

<!-- (5 points) As a developer, I want to create a Comment model: -->

<!-- Property names must be in snake_case and match the following exactly! -->

<!-- user – ForeignKey -->

<!-- video_id – CharField -->

<!-- text – CharField - went with body -->

<!-- likes – IntegerField - went with likes/disklikes tables instead

dislikes – IntegerField -->

<!-- (5 points) As a developer, I want to create a Reply model: -->

<!-- Property names must be in snake_case and match the following exactly! -->

<!-- user – ForeignKey -->

<!-- comment – ForeignKey -->

<!-- text – CharField - went with body -->

<!-- (7.5 points) As a developer, I want to create a GET endpoint that does the following things: -->

<!-- · Accepts a value from the request’s URL (The YouTube video id I am trying to get comments for). -->

<!-- · Returns a 200 status code. -->

<!-- · Responds with all comments from the database that are related to the video id sent in the URL. -->

<!-- (5 points) As a developer, I want to create a POST endpoint that does the following things: -->

<!-- · Requires JWT authorization (Protected route). -->

<!-- · Accepts a body object from the request in the form of a Comment model. -->

<!-- · Adds the new comment to the database associated with the user who sent the JWT in the request. -->

<!-- · Returns a 201 status code. -->

<!-- · Responds with the newly created comment object. -->

<!-- (5 points) As a developer, I want to create a PUT endpoint that does the following things: -->

<!-- · Requires JWT authorization (Protected route). -->

<!-- · Accepts a value from the request’s URL (The id of the comment to be updated). -->

<!-- · Accepts a body object from the request in the form of a Comment model. -->

<!-- · Finds the comment in the Comments table and updates that comment with the properties that were sent in the request’s body. -->

<!-- · Returns a 200 status code. -->

<!-- · Responds with the newly updated comment object. -->

<!-- (5 points) As a developer, I want to create a GET endpoint that does the following things: -->

<!-- · Requires JWT authorization (Protected route). -->

<!-- · Accepts a value from the request’s URL (The id of the comment I am trying to get replies for). -->

<!-- · Returns a 200 status code. -->

<!-- · Responds with all replies from the database that are related to the comment id sent in the URL. -->

<!-- (5 points) As a developer, I want to create a POST endpoint that does the following things: -->

<!-- · Requires JWT authorization (Protected route). -->

<!-- · Accepts a value from the request’s URL (The id of the comment the reply will be connected to). -->

<!-- · Accepts a body object from the request in the form of a Reply model. -->

<!-- · Adds the new reply to the database associated with the comment id sent in the URL and the user who sent the JWT in the request. -->

<!-- · Returns a 201 status code. -->

<!-- · Responds with the newly created reply object. -->

<!-- (5 points) As a developer, I want to use Postman to make a POST, PUT, and both GET requests (get by id and get all) request to my REST web API, save it to a collection, and then export it as a JSON from Postman. -->
