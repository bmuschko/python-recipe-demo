"""Data processing utilities using various dependencies."""

from __future__ import print_function

import json


def load_json_file(filepath):
    """Load data from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def save_json_file(data, filepath):
    """Save data to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def filter_data(data, key, value):
    """Filter a list of dictionaries by key-value pair."""
    return [item for item in data if item.get(key) == value]


def transform_data(data, transform_func):
    """Apply a transformation function to each item in the data."""
    return [transform_func(item) for item in data]


class DataProcessor:
    """Process and transform data collections."""

    def __init__(self, data=None):
        self.data = data or []

    def load_from_json(self, filepath):
        """Load data from JSON file."""
        self.data = load_json_file(filepath)
        return self

    def filter_by(self, key, value):
        """Filter data by key-value pair."""
        self.data = filter_data(self.data, key, value)
        return self

    def transform(self, func):
        """Transform data using provided function."""
        self.data = transform_data(self.data, func)
        return self

    def get_data(self):
        """Return current data."""
        return self.data.copy()

    def count(self):
        """Return count of items."""
        return len(self.data)
