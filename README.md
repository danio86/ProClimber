# ProClimber

ProClimber is the backend project for ProClimbersFE. The project is written in Python Django and utilizes the Python Rest framework. Here, all models can be viewed and manipulated.
Admins have full CRUD functionality but can also simulate not having admin rights. There are three types of users: Admins, who have full CRUD functionality, logged in customers who can create orders and reviews, and visitors, who can just read what is there.
All objects can manipulates manually in the restframework admin panel:

![Admin Panel Screenshot](./backend/assets/images/screenshot-adminpanel.png)


The Project can be seen here: [ProClimbers](https://proclimbers-backend-d69c858b50d1.herokuapp.com/)

The frontend project can be seen here: [ProClimbers-FE](https://proclibers-frontend-5a09a51b15d8.herokuapp.com/)


## Features

### User

- The User Model is an imported Django default model. In the frontend, the username gets replaced with a mandatory user email. The model is connected to other child models through a foreign key.

![Admin Panel Screenshot](./backend/assets/images/screenshot-user-if-not-authenticated.png)

![Admin Panel Screenshot](./backend/assets/images/screenshot-got-testtoken.png)


### Product

- The Product Model is the main model in this project. All attributes are optional since only shop owners or employees, who want to sell the products, have access to the CRUD functionality. It is not necessary to make attributes mandatory. Various attributes, like title, price, etc., can be assigned to them. The model is connected to other child models through a foreign key.

![Admin Panel Screenshot](./backend/assets/images/screenshot-products.png)
![Admin Panel Screenshot](./backend/assets/images/screenshot-products-details.png)


### Review

- The Review model is a direct child of the Product model. No attributes are mandatory. A logged in user can write a comment and give stars to vote for the product, motivating other customers to buy the product.
![Admin Panel Screenshot](./backend/assets/images/screenshot-rating-adminpanel.png)



### Order

- A logged-in customer can create an order and go through the payment process. Here the user does not fill the mandatory attributes (except for the Payment method). The other attributes are set automatically. Only the delivery status can be set, but not by the creator, only by an admin. The model is a child model of the user model and direct parent model of the shipping model.
![Admin Panel Screenshot](./backend/assets/images/screenshot-order.png)


### Order Item

- This model is connected to an Order and to products. An Order can have several Items. During the ordering and payment process, the attributes get filled.
![Admin Panel Screenshot](./backend/assets/images/screenshot-oderItem-admin.png)


### Shipping

- During the order payment process, the user gets led through several pages. There the user has to fill all mandatory attributes (Address, Name, Amount, etc.) of the model.
![Admin Panel Screenshot](./backend/assets/images/screenshot-shipping.png)



### 404
- If the user clicks a page which does not exist, the user comes to an options overview:
![Admin Panel Screenshot](./backend/assets/images/screenshot-404-loggedin.png)


### Thought before creating the models:
- Before I started creating the models, I made a wireframe manually:
![Admin Panel Screenshot](./backend/assets/images/model-wireframe.jpg)





## Testing 

- I have manually tested the program in my local terminal by doing the following:
    - I have tested that the website works in different browsers (Chrome and Firefox).
    - I confirm that the website works and looks good on all standard screen sizes. This was tested with the devtools device toolbar.
    - I confirm that all forms are working.
    - I confirm that the user can create, edit, and delete properties and inquiries.
    - Passed the code through the Code Institute - PEP8 linter and confirmed that there are no problems.
    - Passt my API Urls in Postman to check tokens


    - I have also tested automatically in a tests,py file:
      - This code is testing different parts of a Django application using Django's built-in testing tools and the Django REST Framework's testing tools.

      - ProductViewTestCase: This class tests the functionality related to products. It sets up a test environment with a user and a product. It then tests getting a product, deleting a product, and updating a product.

      - UserViewTests: This class tests the functionality related to users and orders. It sets up a test environment with a user, an admin, a product, an order, an order item, and a shipping address. It then tests adding order items, deleting a user, and getting a user by their ID.

      - OrderViewTests: This class tests the functionality related to users and their profiles. It sets up a test environment with a user and an admin. It then tests registering a user, updating a user profile, getting a user profile, getting all users, getting a user by their ID, updating a user, and deleting a user.

      - In all these tests, the setUp method is used to create a test environment, and the other methods are used to test different functionalities. The self.client is used to make requests to the server, and the assertEqual method is used to check if the response from the server is as expected.



### Validator Testing

  - CI Python PEP8 Linter 
     - No errors were detected when passing through the CI Python PEP8 Linter.
     ![Admin Panel Screenshot](./backend/assets/images/screenshot-pep8.png)


### API and token Testing
- [Postman](https://www.postman.com/)
![Admin Panel Screenshot](./backend/assets/images/screenshot-postman-api-token-check.png)


### Unfixed Bugs

 - All Bugs are fixed.

## Deployment

The project was deployed using Code Institute's mock for Heroku.

    Steps for deployment:
        This repository was cloned from a local VS-Code project.
        A Heroku app was created.
        Added config vars for the secret key, for Cloudinary, and for the PostgreSQL database.
        The Heroku app was linked to the repository.
        Deploy was clicked.


## Credits 

### Content

- Instructions on how to structure backend projects, how to work with databases, how to use Django, PostgreSQL, and Cloudinary, are from [Code Institute - I think therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) and
[Code Institute - Django Rest Framework](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/a706dbb65b2d467a84e1bf67266851b1/)
- Instructions on how to use postman were taken from [Youtube](https://www.youtube.com/watch?v=cGn_LTFCif0)

### Libraries

- asgiref: ASGI server and utilities. Used for handling asynchronous requests in Django.
- cloudinary and django-cloudinary-storage: Used for cloud-based image and video management.
- dj-database-url: Utility to help you load your database into your dictionary from the DATABASE_URL environment variable.
- Django: The main framework for building your web application.
- django-cors-headers: Handles Cross-Origin Resource Sharing (CORS) headers in responses.
- djangorestframework and djangorestframework-simplejwt: Toolkit for building Web APIs. SimpleJWT provides a JSON Web Token - - authentication plugin.
- gunicorn: A WSGI HTTP server for UNIX, used to serve your Django application.
- Pillow: Image processing library to handle tasks such as reading, manipulating, and saving images.
- psycopg2: PostgreSQL adapter for Python, used to connect your Django application to a PostgreSQL database.
- PyJWT: A Python library to encode and decode JSON Web Tokens (JWT).
- pytz: Library for timezone calculations.
- sqlparse: Non-validating SQL parser module for Python.
- whitenoise: Allows your web app to serve its own static files, simplifying deployment.

### Personal Advice

  - Thank You!
    -  Jubril Akolade
    - All people from my Slack Group!