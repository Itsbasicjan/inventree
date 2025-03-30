# Plugin-Installationsanleitung

## 1. setup.py anpassen

Fügen Sie folgende Einträge in Ihre `setup.py` ein:

```python
from setuptools import setup

setup(
    name="meinplugin",
    version="0.1.0",
    entry_points={
        "inventree_plugins": [
            "meinplugin = meinplugin.core:meinplugin"
        ]
    },
    include_package_data=True,
    package_data={
        'meinplugin': [
            'templates/**/*.html',
            'static/**/*',
            'locale/**/*',
        ]
    }
)
```

## 2. Ordnerstruktur erstellen

```bash
mkdir -p meinplugin/static/meinplugin/css
mkdir -p meinplugin/static/meinplugin/js
mkdir -p meinplugin/templates/meinplugin
mkdir -p meinplugin/locale/de/LC_MESSAGES
```

## 3. Plugin aktivieren

In der InvenTree-Konfiguration:
```python
PLUGINS = [
    'meinplugin',
]