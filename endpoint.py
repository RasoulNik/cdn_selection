from prometheus_client import start_http_server
from prometheus_client import Gauge
import time

# declare prometheus metrics-variable
cdn= Gauge('cdn_UC42', 'Selected CDN {0,1,2}')
cache = Gauge('cache_UC42', 'upgrade the cache {0,1,2}')

# Initiate HTTP server for Prometheus metrics
server_port= 8080
start_http_server(int(server_port))


#### The CDN selection algorithm goes here
while True:
    cdn.set(1)
    cache.set(1)
    time.sleep(.5)
    print("running")
