from setuptools import setup

setup(
    name="meinplugin",
    version="0.1.0",
    packages=["meinplugin"],
    include_package_data=True,
    entry_points={
        "inventree_plugins": [
            "Mein Allocation Plugin = meinplugin.core:meinplugin"
        ]
    },
    package_data={
        "meinplugin": [
            "templates/**/*",
            "static/**/*",
        ]
    },
)
