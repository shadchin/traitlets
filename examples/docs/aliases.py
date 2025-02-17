#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""A simple example of using Application aliases, for docs"""

from traitlets import Bool
from traitlets.config import Application, Configurable


class Foo(Configurable):
    enabled = Bool(False, help="whether enabled").tag(config=True)


class App(Application):
    classes = [Foo]
    dry_run = Bool(False, help="dry run test").tag(config=True)
    aliases = {
        "dry-run": "App.dry_run",
        ("f", "foo-enabled"): ("Foo.enabled", "whether foo is enabled"),
    }


if __name__ == "__main__":
    App.launch_instance()
