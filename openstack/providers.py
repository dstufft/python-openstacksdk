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

import inspect

import six

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

from openstack.auth.base import BaseAuthPlugin
from openstack.auth.service_filter import ServiceFilter


class MultiProvider(object):

    def __init__(self, *providers):
        self.providers = providers

    def __getattr__(self, name):
        for provider in self.providers:
            item = getattr(provider, name, None)
            if item is not None:
                return item

        raise AttributeError(
            "'{0}' object has no attribute '{1}'".format(
                self.__class__.__name__,
                name,
            ),
        )

    @property
    def plugin_names(self):
        all_names = set()
        for provider in self.providers:
            all_names |= provider.plugin_names
        return all_names


class ProviderMeta(type):

    def __new__(cls, name, bases, attrs):
        plugin_names = set()

        # Load all of the plugin names from our bases
        for base in bases:
            plugin_names |= getattr(base, "plugin_names", set())

        # Load all of the plugin names from this class
        for name, value in attrs.items():
            if (inspect.isclass(value)
                    and issubclass(value, (BaseAuthPlugin, ServiceFilter))):
                plugin_names.add(name)

        attrs["plugin_names"] = plugin_names

        return super(ProviderMeta, cls).__new__(cls, name, bases, attrs)


@six.add_metaclass(ProviderMeta)
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
