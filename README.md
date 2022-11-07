# company-relationship-manager

**This is an example application to assess developer skills with python and Django REST framework.**

The 'CRM' manages relationships between companies and a UK government department.

Currently a user can: 
- create a company by sending a POST request to the `/companies/` endpoint
- view one company or a view a list of all companies
- update a company
- delete a company

It is built using the Django REST framework and a Postgres database running in a Docker container environment.

## Usage

### Using Docker

You can run the api and all associated services using `docker-compose`, or use the script `up.sh` like so

```
./up.sh
```

To tell `docker-compose` to stop all services, there is a script `down.sh` you can use like so

```
./down.sh
```

### Tests

You can run tests using pytest from a running Docker container using the `test.sh` script like so

```
./test.sh
```

## Tasks

To see suggested development tasks, go to [TASKS.md](TASKS.md)
