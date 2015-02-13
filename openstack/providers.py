# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import openstack.auth.identity.discoverable
import openstack.auth.identity.v2
import openstack.auth.identity.v3
import openstack.compute.compute_service
import openstack.database.database_service
import openstack.identity.identity_service
import openstack.image.image_service
import openstack.keystore.keystore_service
import openstack.network.network_service
import openstack.object_store.object_store_service
import openstack.orchestration.orchestration_service
import openstack.telemetry.telemetry_service


class BaseProvider(object):
    auth = openstack.auth.identity.discoverable.Auth
    compute = openstack.compute.compute_service.ComputeService
    database = openstack.database.database_service.DatabaseService
    identity = openstack.identity.identity_service.IdentityService
    image = openstack.image.image_service.ImageService
    keystore = openstack.keystore.keystore_service.KeystoreService
    network = openstack.network.network_service.NetworkService
    object_store = \
        openstack.object_store.object_store_service.ObjectStoreService
    orchestration = \
        openstack.orchestration.orchestration_service.OrchestrationService
    telemetry = openstack.telemetry.telemetry_service.TelemetryService


class Identity(BaseProvider):
    pass


class IdentityV2(BaseProvider):
    auth = openstack.auth.identity.v2.Auth


class IdentityV3(BaseProvider):
    auth = openstack.auth.identity.v3.Auth
