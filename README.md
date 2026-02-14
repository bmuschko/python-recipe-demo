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

These OpenRewrite Python recipes are run against this project in GitHub Actions:

| Recipe | Parameters | Target |
|--------|------------|--------|
| `PythonSpaces` | - | `.py` files |
| `DependencyInsight` | `packageNamePattern="requests*"` | `pyproject.toml` |
| `UpgradeDependencyVersion` | `packageName=requests`, `newVersion=">=2.31.0"` | `pyproject.toml` |
| `AddDependency` | `packageName=httpx`, `version=">=0.25.0"` | `pyproject.toml` |
| `ChangeDependency` | `oldPackageName=click`, `newPackageName=typer`, `newVersion=">=0.9.0"` | `pyproject.toml` |
| `RemoveDependency` | `packageName=ruff`, `scope=project.optional-dependencies`, `groupName=dev` | `pyproject.toml` |

## Python Code Features

The demo code includes `__future__` imports which can be detected by migration recipes:
- `from __future__ import annotations`
- `from __future__ import division`
- `from __future__ import print_function`
- `from __future__ import absolute_import`
- `from __future__ import unicode_literals`
