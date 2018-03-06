#!/usr/bin/env/ python3
""" App's entry point. Run first to start the Flask server and launch app """

from app import app


if __name__ == '__main__':
    app.run(debug=True)