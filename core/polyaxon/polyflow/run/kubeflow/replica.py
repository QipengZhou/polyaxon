#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import polyaxon_sdk

from marshmallow import fields

from polyaxon.containers.names import MAIN_JOB_CONTAINER
from polyaxon.k8s import k8s_schemas
from polyaxon.polyflow.environment import EnvironmentSchema
from polyaxon.polyflow.init import InitSchema
from polyaxon.schemas.base import BaseCamelSchema, BaseConfig
from polyaxon.schemas.fields.swagger import SwaggerField


class KFReplicaSchema(BaseCamelSchema):
    replicas = fields.Int(allow_none=True)
    environment = fields.Nested(EnvironmentSchema, allow_none=True)
    connections = fields.List(fields.Str(), allow_none=True)
    volumes = fields.List(SwaggerField(cls=k8s_schemas.V1Volume), allow_none=True)
    init = fields.List(fields.Nested(InitSchema), allow_none=True)
    sidecars = fields.List(SwaggerField(cls=k8s_schemas.V1Container), allow_none=True)
    container = SwaggerField(
        cls=k8s_schemas.V1Container,
        defaults={"name": MAIN_JOB_CONTAINER},
        allow_none=True,
    )

    @staticmethod
    def schema_config():
        return V1KFReplica


class V1KFReplica(BaseConfig, polyaxon_sdk.V1KFReplica):
    SCHEMA = KFReplicaSchema
    IDENTIFIER = "replica"
    REDUCED_ATTRIBUTES = [
        "replicas",
        "environment",
        "connections",
        "volumes",
        "init",
        "sidecars",
        "container",
    ]
