"""
Author: Nino Ross
Class: SDEV 300

This is lab assignment 8 for SDEV 300. This code creates
and launches the Flask webpage.
"""

from . import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()
