"""!@namespace httpproxy Transport Layer fuer XMLRPClib"""
import xmlrpclib
import urllib2

class Urllib2Transport(xmlrpclib.Transport):
    """!Transport-Layer fuer das XMLRPC-Modul unter Verwendung von urllib2"""
    def __init__(self, opener=None, https=False, use_datetime=0):
        xmlrpclib.Transport.__init__(self, use_datetime)
        self.opener = opener or urllib2.build_opener()
        self.https = https
        self.verbose = 0

    def request(self, host, handler, request_body, verbose=0):
        """!HTTP-Request"""
        proto = ('http', 'https')[bool(self.https)]
        req = urllib2.Request('%s://%s%s' % (proto, host, handler), request_body)
        req.add_header('User-agent', self.user_agent)
        self.verbose = verbose
        return self.parse_response(self.opener.open(req))

class HTTPProxyTransport(Urllib2Transport):
    """!HTTP-Proxy fuer das XMLRPC-Modul"""
    def __init__(self, proxies, use_datetime=0):
        self._proxies = proxies
        opener = urllib2.build_opener(urllib2.ProxyHandler(proxies))
        Urllib2Transport.__init__(self, opener, use_datetime)

    def get_proxy_name(self):
        """!Liefert die Connect-Parameter des Proxies zurueck
        @return Dictionary mit den Proxy-Parametern
        """
        return self._proxies
