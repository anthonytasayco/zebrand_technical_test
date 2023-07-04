# Zebrand Techincal test Description

We need to build a basic catalog system to manage products. A product should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) admins to create / update / delete products and to create / update / delete other admins; and (ii) anonymous users who can only retrieve products information but can't make changes.

As a special requirement, whenever an admin user makes a change in a product (for example, if a price is adjusted), we need to notify all other admins about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an anonymous user, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference.


## Requirements
- docker y docker-compose

## Solution
- The framework used in this project is django.
- For api services this project uses django rest framework.
- This project uses the default User model from django.
- This project defines an admin user whether a user if "is_staff" or "is_superuser".
- For mailing notifications the project uses celery workers to send emails asynchronously.
- The number of visitis a product has is denifed as a field  and it increases using django signals.

## Build the project for local environment

Create an .env file with the values inside the env_template.txt
```
$ docker-compose -f ./compose/docker-compose.yml build
```
```
$ docker-compose -f ./compose/docker-compose.yml up
```
Create superuser inside zebrand_webapp

## Tools for developing in local environment

The project uses the following libries and tools:
- django, django rest framework, postgres, smtp, redis, docker.
- django debug toolbar library
- mailhog, to view testing mailing notifications visit  http://localhost:8025/
- swagger, you can visit http://localhost:8000/swagger for check the api documentation


## Tasks to develop
- Testing to run all test cases.
- create the config for a production environment(new docker configuration)
- Generate fixture to load initial data on db.
