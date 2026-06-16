import os

SKIP_DIRS = {
    ".git", "node_modules", "target", "dist", "build",
    ".svelte-kit", "__pycache__", ".omx",
}


def repo_root():
    here = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(os.path.dirname(here)))


def iter_repo_files(root=None):
    root = root or repo_root()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            yield os.path.join(dirpath, name)


def read_lines(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def rel(path, root=None):
    return os.path.relpath(path, root or repo_root())
