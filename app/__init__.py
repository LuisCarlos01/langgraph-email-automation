"""Alias the ``app`` package to ``backend.app`` for backwards compatibility."""

from importlib import import_module
import sys

_backend_app = import_module("backend.app")

# Replace this module entry with the backend implementation so that nested
# imports like ``app.db.models`` resolve to the same objects without creating
# duplicate modules. This avoids SQLAlchemy table redefinition errors during
# testing.
sys.modules[__name__] = _backend_app

# Expose already imported ``backend.app`` submodules under the ``app`` prefix so
# that any future ``import app.x`` statements reuse the existing modules.
prefix = "backend.app."
for name, module in list(sys.modules.items()):
    if name.startswith(prefix):
        sys.modules[name.replace(prefix, "app.", 1)] = module
