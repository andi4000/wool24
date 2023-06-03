# pylint: disable=missing-docstring
import os
import traceback
from importlib import util


def _load_module(module_path: str):  # type: ignore
    name = os.path.split(module_path)[-1]
    spec = util.spec_from_file_location(name, module_path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_modules() -> None:
    path = os.path.abspath(__file__)
    dirpath = os.path.dirname(path)

    for fname in os.listdir(dirpath):
        # load python files in this directory as module
        if (
            not fname.startswith(".")
            and not fname.startswith("__")
            and fname.endswith(".py")
        ):
            try:
                _load_module(os.path.join(dirpath, fname))
            except Exception:
                traceback.print_exc()
