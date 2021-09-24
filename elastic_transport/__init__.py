#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

"""Transport classes and utilities shared among Python Elastic client libraries"""

from ._exceptions import (
    ApiError,
    BadGatewayError,
    BadRequestError,
    ConflictError,
    ConnectionError,
    ConnectionTimeout,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotImplementedError,
    NotFoundError,
    PayloadTooLargeError,
    PaymentRequiredError,
    SecurityWarning,
    SerializationError,
    ServiceUnavailableError,
    TlsError,
    TooManyRequestsError,
    TransportError,
    TransportWarning,
    UnauthorizedError,
    UnprocessableEntityError,
)
from ._models import HttpHeaders, HttpResponse, NodeConfig, QueryParams, RequestOptions
from ._node import AiohttpHttpNode, BaseNode, RequestsHttpNode, Urllib3HttpNode
from ._node_pool import (
    EmptyNodePool,
    NodePool,
    NodeSelector,
    RandomSelector,
    RoundRobinSelector,
    SingleNodePool,
)
from ._serializer import Deserializer, JsonSerializer, Serializer, TextSerializer
from ._transport import Transport
from ._version import __version__ as __version__  # noqa

__all__ = [
    "AiohttpHttpNode",
    "ApiError",
    "BadGatewayError",
    "BadRequestError",
    "BaseNode",
    "ConflictError",
    "ConnectionError",
    "ConnectionTimeout",
    "Deserializer",
    "EmptyNodePool",
    "ForbiddenError",
    "GatewayTimeoutError",
    "HttpHeaders",
    "HttpResponse",
    "InternalServerError",
    "JsonSerializer",
    "MethodNotImplementedError",
    "NodeConfig",
    "NodePool",
    "NodeSelector",
    "NotFoundError",
    "PayloadTooLargeError",
    "PaymentRequiredError",
    "QueryParams",
    "RandomSelector",
    "RequestOptions",
    "RequestsHttpNode",
    "RoundRobinSelector",
    "SecurityWarning",
    "SerializationError",
    "Serializer",
    "ServiceUnavailableError",
    "SingleNodePool",
    "TextSerializer",
    "TlsError",
    "TooManyRequestsError",
    "Transport",
    "TransportError",
    "TransportWarning",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "Urllib3HttpNode",
]
