# Copyright (C) 2020 Evgeny Golyshev. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Server-side of the CusDeb Anonymous microservice. """

import asyncio
import datetime
import uuid

import jwt
from aiohttp import web

from cusdeb_anonymous import config


ANONYMOUS_USER_ID = -1


async def issue_token(_request):
    """Handles requests to the /anonymous/ endpoint. """

    await asyncio.sleep(config.ISSUE_DELAY)

    payload = {
        'token_type': 'access',
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=config.TOKEN_TTL),
        # The way of creating a JWT ID was borrowed from django-rest-framework-simplejwt.
        # See the set_jti method of the Token class.
        'jti': uuid.uuid4().hex,
        'user_id': ANONYMOUS_USER_ID,
    }

    encoded_token = jwt.encode(payload, config.SECRET_KEY, algorithm=config.ALGO)

    return web.Response(text=encoded_token.decode('utf-8'))


async def main():
    """The main entry point. """

    app = web.Application(middlewares=[web.normalize_path_middleware()])
    app.add_routes([web.get('/anonymous/', issue_token)])
    return app


if __name__ == '__main__':
    web.run_app(main(), port=config.PORT)
