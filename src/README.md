# BookStoreAPI
Book Store API using django rest framework 

##User Registration:

URL : http://127.0.0.1:8000/api/auth/register/

Response:
{
    "username": "username1",
    "email": "email@example@gmail.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRleHRlciIsImV4cCI6MTU1NjYwNjk1NSwiZW1haWwiOiJkZXguc2hyZXN0aGExMEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU1NjYwNjM1NX0.yAzQLO3XdkvhyzfLZgBEF23BQqizN8IZINX0RUE_taA",
    "expires": "2019-05-07T06:35:55.626773Z",
    "message": "Thank you for registering. Please verify"
}

## Get JWT token
URL :http://127.0.0.1:8000/api/auth/jwt/
Refresh URL : http://127.0.0.1:8000/api/auth/jwt/refresh/
Response:
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRleHRlciIsImV4cCI6MTU1NjYwNzAzOCwiZW1haWwiOiJkZXguc2hyZXN0aGExMEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU1NjYwNjQzOH0.C6KGg5a6dokk4a1ihAt_plTYPk3iWdAnP9DHqDQB_fE",
    "user": "username1",
    "expires": "2019-05-07T06:37:18.740557Z"
}

## Book List View
Method : GET
URL : http://127.0.0.1:8000/api/v1/book/

## Book Detail View
- Select book by id
Method: GET
URL :http://127.0.0.1:8000/api/v1/book/{book_id}/

## Book Create 
Method: POST
URL : http://127.0.0.1:8000/api/v1/book/

## Book Edit
Method: PUT
URL : http://127.0.0.1:8000/api/v1/book/{book_id}/

## Book Delete

Method: DELETE
URL : http://127.0.0.1:8000/api/v1/book/{book_id}/

## Review Create
Method: POST
http://127.0.0.1:8000/api/v1/review

## Review Search
Method: GET
-by username:http://127.0.0.1:8000/api/v1/review/?user__username=username1

## Review Detail View
Method: GET
http://127.0.0.1:8000/api/v1/review/{review_id}

## Review Edit
Method: PUT
http://127.0.0.1:8000/api/v1/review/{review_id}

## Review Delete
Method: DELETE
http://127.0.0.1:8000/api/v1/review/{review_id}

## Comment Create
Method: POST
http://127.0.0.1:8000/api/v1/comment

## Comment Search
Method: GET
-by username:http://127.0.0.1:8000/api/v1/comment/?user__username=username1

## Comment Detail View
Method: GET
http://127.0.0.1:8000/api/v1/comment/{comment_id}

## Comment Edit
Method: PUT
http://127.0.0.1:8000/api/v1/comment/{comment_id}

## Comment Delete
Method: DELETE
http://127.0.0.1:8000/api/v1/comment/{comment_id}