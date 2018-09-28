"""
This script reflects all content passing through the proxy.
"""
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host not in ['www.instagram.com', 'www.corriere.it']:
        if not flow.request.pretty_host.endswith('nasa.gov'):
            reflector = b"<style>img, background-url {transform: rotate(180deg);}</style></head>"
        else:
            reflector = b'<style>body {transform: scaleX(-1);}</style></head>'
        flow.response.content = flow.response.content.replace(b"</head>", reflector)
