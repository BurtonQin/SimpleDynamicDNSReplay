# Simple Dynamic DNS Relay

The IP of the servers in campus network keeps changing due to DHCP, thus I build a local DNS relay server without bothering with the DynDNS.

* Protocol Format
For simplicity, I use UDP as the transport layer protocol. The message format is as follows:
```
HOSTNAME\nIPv4\nIPv6
```

* Client

Report local IP every hour(It depends on dhcp lease time) to the server.
Note that the hostnames of all the clients in one server domain shall not be the same.

* Server

Receive the report and change the /etc/hosts, then restart the dnsmasq service.

* Deployment
	1. client: Store the get_ip.sh
	2. client: Modify `path` in `collectclient.py` to the path of `get_ip.sh`
	3. client: `mv collectclient.py /etc/cron.hourly/collectclient`
    4. server: Run the collectserver.py in the background or using [supervisor](https://supervisord.org/)

* Future works

Find a better solution without restarting the dnsmasq service

