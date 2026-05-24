"""aidlc-workflows: AI-driven development lifecycle workflows.

This package provides workflow automation tools for AI-assisted
software development lifecycle management, including code review,
testing, documentation generation, and deployment pipelines.

Note: This is a personal fork for learning and experimentation.
Upstream: https://github.com/awslabs/aidlc-workflows

Fork notes:
- Experimenting with custom workflow configurations
- See docs/fork-notes.md for personal modifications
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("aidlc-workflows")
except PackageNotFoundError:
    __version__ = "0.0.0"

__author__ = "aidlc-workflows contributors"
__license__ = "Apache-2.0"

__all__ = [
    "__version__",
    "__author__",
    "__license__",
]
