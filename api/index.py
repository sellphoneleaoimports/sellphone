# -*- coding: utf-8 -*-
"""
Vercel Serverless Function Entrypoint para o Sistema iLion CRM / Sellphone.
Redireciona todas as chamadas /api/* para o AppleStoreHandler do server.py.
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from server import AppleStoreHandler


class handler(AppleStoreHandler):
    """Handler compatível com o runtime @vercel/python (BaseHTTPRequestHandler)."""

    def _normalize_vercel_path(self):
        if not self.path.startswith('/api/') and self.path != '/api':
            if self.path.startswith('/'):
                self.path = '/api' + self.path
            else:
                self.path = '/api/' + self.path

    def do_GET(self):
        if self.path not in ('/', '', '/index.html', '/entrega.html', '/app.js', '/style.css', '/leao.jpg') and not self.path.startswith('/entrega.html'):
            self._normalize_vercel_path()
        return super().do_GET()

    def do_POST(self):
        self._normalize_vercel_path()
        return super().do_POST()

    def do_DELETE(self):
        self._normalize_vercel_path()
        return super().do_DELETE()
