# Tasks for developers

When submitting a pull request, ensure that unit tests are included in your submission.

## Task 1: Validate new entries

At the moment, a user can create a new company with very little information.

For example, a new company can be created without a company reference number. In this case, the Django model sets the company reference field to the empty string as a default.

Modify the application so that two conditions are met when submitting a new company:

1. The company reference cannot be an empty string
2. The company reference cannot be a reference that already exists in the database.

The API should respond with descriptive error messages if either of these conditions are not met.

## Task 2: User authentication

Currently, the API is open to anyone to use, i.e. anyone can create, read, update, or delete data without being authenticated.

Modify the application to have the following features:

1. Companies are always associated with a creator
2. Only authenticated users may create companies
3. Only the creator of a company may update or delete it
4. Unauthenticated requests should have full read-only access

