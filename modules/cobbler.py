import xmlrpclib
from httpproxy import HTTPProxyTransport


class Cobbler(object):

    def __init__(self):
        self.transport = HTTPProxyTransport({'http': '<proxy_address>'})
        self.cobbler_server = xmlrpclib.Server("http://<cobbler_url>/cobbler_api", transport=self.transport)
        self.token = self.cobbler_server.login("cobbler", "cobbler")

    def get_all_distros(self):
        all_distros = self.cobbler_server.get_distros()
        return all_distros

    def get_all_systems(self):
        all_systems = self.cobbler_server.get_systems()
        return all_systems

