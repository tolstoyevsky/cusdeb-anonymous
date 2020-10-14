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

"""Module allowing configuration of the microservice via the environment variables. """

import os

ALGO = os.getenv('ALGO', 'HS256')

ISSUE_DELAY = int(os.getenv('ISSUE_DELAY', '5'))

SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

PORT = os.getenv('PORT', '8007')

TIME_ZONE = os.getenv('TIME_ZONE', 'Europe/Moscow')

TOKEN_TTL = int(os.getenv('TOKEN_TTL', '20'))
