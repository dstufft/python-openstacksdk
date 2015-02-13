import openstack.auth.identity.discoverable
import openstack.auth.identity.v2
import openstack.auth.identity.v3


class BaseProvider(object):
    auth = openstack.auth.identity.discoverable.Auth


class Default(BaseProvider):
    pass


class IdentityV2(BaseProvider):
    auth = openstack.auth.identity.v2.Auth


class IdentityV3(BaseProvider):
    auth = openstack.auth.identity.v3.Auth
