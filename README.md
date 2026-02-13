# Python Recipe Demo

Demo Python project for OpenRewrite/Moderne Python support.

## Project Structure

```
python-recipe-demo/
├── pyproject.toml        # Python project configuration
└── demo/                 # Demo Python package
    ├── __init__.py
    ├── calculator.py     # Basic math operations
    ├── data_processor.py # JSON data processing
    ├── api_client.py     # HTTP API client
    └── utils.py          # Utility functions
```

## Dependencies

Project dependencies (in pyproject.toml):
- `requests>=2.28.0` - HTTP client library
- `pyyaml>=6.0` - YAML parser
- `click>=8.0.0` - CLI framework

Dev dependencies:
- `pytest>=7.0.0` - Testing framework
- `black>=23.0.0` - Code formatter
- `ruff>=0.1.0` - Linter

## Sample Recipes

These OpenRewrite Python recipes can be applied to this project:

| Recipe | Description |
|--------|-------------|
| `org.openrewrite.python.search.DependencyInsight` | Find dependencies matching a pattern |
| `org.openrewrite.python.UpgradeDependencyVersion` | Upgrade dependency version |
| `org.openrewrite.python.AddDependency` | Add a new dependency |
| `org.openrewrite.python.ChangeDependency` | Change one dependency to another |
| `org.openrewrite.python.RemoveDependency` | Remove a dependency |

## Python Code Features

The demo code includes `__future__` imports which can be detected by migration recipes:
- `from __future__ import annotations`
- `from __future__ import division`
- `from __future__ import print_function`
- `from __future__ import absolute_import`
- `from __future__ import unicode_literals`
