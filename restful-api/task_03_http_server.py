#!/usr/bin/python3
"""
task_03_http_server.py
A simple API server using Python's built-in http.server module.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API."""

    def _send_json(self, payload, status_code=200):
        """Send JSON response with proper headers."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, text, status_code=200):
        """Send plain text response with proper headers."""
        body = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """
        Handle GET requests:
        - /        -> plain text greeting
        - /data    -> JSON dataset
        - /status  -> plain text OK
        - /info    -> JSON info (mentioned in expected output)
        - else     -> 404
        """
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_text("OK")
        elif self.path == "/info":
            self._send_json(
                {"version": "1.0", "description": "A simple API built with http.server"}
            )
        else:
            # 404 for undefined endpoints
            self._send_text("Endpoint not found", status_code=404)

    def log_message(self, format, *args):
        """
        Optional: keep output clean (removes default access logs).
        If your checker expects logs, you can delete this method.
        """
        return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)  # "" means all interfaces (localhost)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
