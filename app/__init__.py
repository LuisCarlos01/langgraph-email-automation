from importlib import import_module
import sys

_backend_app = import_module('backend.app')

# Expose attributes from backend.app at this level
globals().update(_backend_app.__dict__)

# Map important submodules so imports using 'app.' work
for submodule in ['api', 'db', 'schemas', 'core']:
    try:
        sys.modules[f'app.{submodule}'] = import_module(f'backend.app.{submodule}')
    except ModuleNotFoundError:
        pass
