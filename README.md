# Flask-Guardian

---

## About

Chainable request-validation rules for Flask, inspired by [Joi](https://joi.dev/).

This is an earlier library. Validate behavior against your Flask version before production use. The repository’s LICENSE file is currently empty; licensing needs clarification before redistribution.


## Installation

**Use pip for installation**

```sh
pip install flask-guardian
```

## How to use

### Create your rule

```py

from flask_guardian.rules import Rules
from flask_guardian.validator import Validator

my_rules = {
  "login": Rules().Required().String().Max(20),
  "password": Rules().Required().String().Min(8).Max(120)
}
```

### Add the middleware inside your route

```py
@app.route("/login", methods=["POST"])
@Validator(my_rules)
def login_():
  '''your code here'''
```

## Rules

#### .String()
Verify if the parameter is a string.

#### .Integer()
Verify if the parameter is an integer.

#### .Email()
Using a regex, verify if the parameter is conform with email format.

#### .Min(x)
Verify if the parameter len is more than x.

#### .Max(x)
Verify if the parameter len is less or equal than x.

#### .Contains([x, y, z])
Verify if the parameter contains at least one argument of the array.

#### .notContains([x, y, z])
Verify if the parameter not contains any argument of the array.

#### .Equal(x)
Verify if the parameter equal x.

#### .notEqual(x)
Verify if the parameter not equal x.


