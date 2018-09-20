"""
This script reflects all content passing through the proxy.
"""
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    reflector = b"<style>img, background-url {transform: rotate(180deg);}</style></head>"
    flow.response.content = flow.response.content.replace(b"</head>", reflector)
