# Sample Microservices

| Endpoint | Arguments | Method | Comments |
| -- | -- | -- | -- |
| / | None | GET | returns status |
| /sync | None | GET | returns status |  
| /greetings| name, greetword | GET | returns a greeting |
| /async | delta | GET | delta = seconds after which the request is returend by the server|
|/register|user_id, age, password | POST | user_id must be unique|
|/login| user_id, password| POST | returns of the user had already registered |

The app is hosted on [heroku](https://gor-test-micro.herokuapp.com/).
