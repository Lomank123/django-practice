# django-practice

The goal is to practice remained django features which never been used before. Most of custom implementations are covered with tests.


## Table of contents
- [django-practice](#django-practice)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Features](#features)
    - [Middleware](#middleware)
    - [Logging](#logging)
    - [Context processors](#context-processors)
    - [Signals](#signals)
    - [Sessions](#sessions)
    - [Multiple apps](#multiple-apps)
    - [Complex database queries](#complex-database-queries)
    - [Localization](#localization)
    - [Timezone](#timezone)
  - [Tests](#tests)
  - [Fixtures](#fixtures)
  - [Author](#author)

In the future here may be also DRF stuff.


## Installation

Describe installation process here.


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

In result all output is written to log file. Middlewares logs can be also seen in the console.


### Context processors


### Signals


### Sessions


### Multiple apps


### Complex database queries


### Localization


### Timezone


## Tests
All custom classes and methods have been covered with tests.


## Fixtures

Describe fixtures content and installation process here.


## Author

[Lomank123](https://github.com/Lomank123)
