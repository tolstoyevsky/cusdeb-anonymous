# CusDeb Anonymous

CusDeb Anonymous is a microservice intended for issuing JWT tokens for anonymous access to [CusDeb](https://cusdeb.com).

## Installation

```
$ git clone https://github.com/tolstoyevsky/cusdeb-anonymous.git
$ virtualenv -ppython3 cusdeb-anonymous-env
$ source cusdeb-anonymous-env/bin/activate
(cusdeb-helpik-env) $ cd cusdeb-anonymous
(cusdeb-helpik-env) $ python3 setup.py install
(cusdeb-helpik-env) $ python3 bin/server.py
```

## Configuration

The microservice can be configured via the following environment variables (called params).

| Param         | Description                                                                                                                                           | Default        |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| `ALGO`        | The algorithm used for encoding the JWT tokens.                                                                                                       | `HS256`        |
| `ISSUE_DELAY` | The delay (in seconds) in issuing the JWT tokens.                                                                                                     | `5`            |
| `PORT`        | The port the CusDeb Anonymous server listens on.                                                                                                      | `8007`         |
| `SECRET_KEY`  | The secret key used for encoding the JWT tokens. It's **HIGHLY RECOMMENDED** to change the default value.                                             | `secret`       |
| `TIME_ZONE`   | A string representing the time zone for this installation. See the [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).| `Europe/Moscow`|
| `TOKEN_TTL`   | How long (in seconds) the JWT tokens are alive.                                                                                                       | `20`           |

## API

* **URI:** `/anonymous/`
* **Method:** `GET`
* **Params:** None
* **Success Response**
  * **Code:** 200
  * **Content:** *an encoded JWT token*<br/>
    Each JWT token issued by the microservice has the following payload: `{'token_type': 'access', 'exp': <exp>, 'jti': '<jti>', 'user_id': -1}`, where
    * `token_type` is obviously a token type. The field always contains `access`.
      A refresh token is not provided, therefore to obtain a new access token, invoke the endpoint once again.
    * `exp` is an expiration date (see the `TOKEN_TTL` param above). It accepts integer numbers known as Unix timestamps.
    * `jti` is a JWT ID (see [Section 4.1.7](https://tools.ietf.org/html/rfc7519#page-10) of RFC 7519).
    * `user_id` is the pseudo id of an anonymous user. The field always contains `-1` to let clients easily distinguish the pseudo id from a real one.

## Authors

See [AUTHORS](AUTHORS.md).

## Licensing

CusDeb Anonymous is available under the [Apache License, Version 2.0](LICENSE).
