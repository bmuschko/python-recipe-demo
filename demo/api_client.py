"""HTTP API client module."""

from __future__ import absolute_import

import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


class ApiClient:
    """Simple HTTP API client."""

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def set_header(self, key, value):
        """Set a custom header."""
        self.headers[key] = value

    def get(self, endpoint):
        """Make a GET request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        request = Request(url, headers=self.headers)
        try:
            with urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            raise Exception(f"HTTP Error {e.code}: {e.reason}")
        except URLError as e:
            raise Exception(f"URL Error: {e.reason}")

    def post(self, endpoint, data):
        """Make a POST request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        body = json.dumps(data).encode("utf-8")
        request = Request(url, data=body, headers=self.headers, method="POST")
        try:
            with urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            raise Exception(f"HTTP Error {e.code}: {e.reason}")
        except URLError as e:
            raise Exception(f"URL Error: {e.reason}")


def fetch_json(url):
    """Fetch JSON data from a URL."""
    request = Request(url)
    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))
