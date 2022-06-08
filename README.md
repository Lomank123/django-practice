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


### Sessions

For sessions I used `django.contrib.sessions.backends.cached_db` session engine (with the help of Redis).

In `/blog/views.py`, in `BlogPostDetailView` you can find simple sessions implementation which counts how many times have user visited this page.
Using debug toolbar you can see that after the first time it makes 1 less query every time because session is stored in cache as well as in the database.


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


## Fixtures

Describe fixtures content and installation process here.


## Author

[Lomank123](https://github.com/Lomank123)
