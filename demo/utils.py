"""Utility functions for common operations."""

from __future__ import unicode_literals

import os
import re
from datetime import datetime


def get_env_var(name, default=None):
    """Get environment variable with optional default."""
    return os.environ.get(name, default)


def format_date(dt, fmt="%Y-%m-%d"):
    """Format a datetime object as string."""
    return dt.strftime(fmt)


def parse_date(date_str, fmt="%Y-%m-%d"):
    """Parse a date string into datetime object."""
    return datetime.strptime(date_str, fmt)


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text.strip("-")


def truncate(text, max_length, suffix="..."):
    """Truncate text to max length with suffix."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def chunk_list(lst, chunk_size):
    """Split a list into chunks of specified size."""
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


def flatten_list(nested_list):
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def deep_merge(base, override):
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
