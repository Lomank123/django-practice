# django-practice

The goal is to practice remained django features which never been used before.


## Table of contents
- [django-practice](#django-practice)
  - [Table of contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Features](#features)
    - [Middleware](#middleware)
    - [Logging](#logging)
    - [Context processors](#context-processors)
    - [Signals](#signals)
    - [Sessions](#sessions)
    - [Multiple apps](#multiple-apps)
    - [Cache](#cache)
    - [Complex database queries](#complex-database-queries)
    - [Localization](#localization)
    - [Timezone](#timezone)
    - [CI](#ci)
  - [Fixtures](#fixtures)
  - [Author](#author)

In the future here may be also DRF stuff.


## Requirements
- Python (3.9.2 or newer) [link](https://www.python.org/downloads/)
- Redis


## Installation

- Clone repo:
```
git clone https://github.com/Lomank123/django-practice.git
```

- Copy the content of `.env.sample` to `.env` file inside project dir:
```
cd /path/to/project/django-practice
cp .env.sample .env
```

- `venv` setup:
```
mkdir venv
cd venv
py -m venv ./venv
```

- Install requirements:
```
pip install -r requirements.txt
```

- Create Postgres db and user (credentials should be the same as in `.env` file)

- Go to `/main` dir:
```
cd main
```

- Run migrations:
```
py manage.py makemigrations
py manage.py migrate
```

- Create superuser:
```
py manage.py createsuperuser
```

- Run server:
```
py manage.py runserver
```


## Features


### Middleware

There are 4 custom middlewares:
- `LogTimeTakenMiddleware` - Calculates and logs total time taken for the response to get.
- `CountRequestsMiddleware` - Counts number of requests and exceptions.
- `SetUserAgentMiddleware` - Adds attr to the request with meaningful info about user agent.
- `BlockMobileMiddleware` - Blocks all incoming requests if they are from mobile browsers. Depends on `SetUserAgentMiddleware`.


### Logging

There are 3 custom loggers:
- `django` - Overriden default logger
- `main.middleware` - For custom middleware's file output
- `main.middleware.custom` - For custom middleware's console output with `propagate = True`

In result all output is written to log file. Middleware's logs can be also seen in the console.


### Context processors

Here you can find 1 custom context processor:
- `item_count` - Simply returns count of `Item` objects.

As a result you can access `all_items_count` in templates.


### Signals

In `accounts/signals.py` you can find 1 custom signal and 3 receivers.

Signals:
- `new_sign_up` - signal which is being sent when new user signs up.

Receivers:
- `create_profile` - Creates `UserProfile` and attaches it to newly created `CustomUser`.
- `update_profile` - Updates `UserProfile` after related `CustomUser` has been saved.
- `notify_new_sign_up` - Logs the fact that new user has signed up.

Everything is covered with mock tests here in `accounts/tests/test_signals.py`.


### Sessions

For sessions I used `django.contrib.sessions.backends.cached_db` session engine (with the help of Redis).

In `/blog/views.py`, in `BlogPostDetailView` you can find simple sessions implementation which counts how many times have user visited this page.
Using debug toolbar you can see that after the first time it makes 1 less query every time because session is stored in cache as well as in the database.

In the tests session engine has been changed to `django.contrib.sessions.backends.db`.


### Multiple apps

There are 3 different apps other than `main`:
- `testapp` - For learning purposes. Filled with different connected things like item, category and tag.
- `blog` - Represents blog posts with comments.
- `accounts` - For authentication. Describes auth process with it's custom user model.


### Cache

I decided to use Redis for caching.

Caches settings:
```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}
```

In `testapp/urls.py` I cached `HomeView` with delayed request. For the first time it may take ~2 seconds but after that it'll load the page in several milliseconds.


### Complex database queries


### Localization


### Timezone


### CI

- Go to `.github/workflows/CI.yml`

On each commit or pull request there is 1 test job which uses postgres image to create db, and python env to install requirements and run all tests.

To create proper conditions:
- Some tests connected with cache use dummy cache
- Before running the job we create `/main/logs/debug.log` file to test custom logger


## Fixtures

Describe fixtures content and installation process here.


## Author

[Lomank123](https://github.com/Lomank123)
