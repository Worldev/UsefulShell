#!/usr/bin/env python3
import os
import sys
import platform
import webbrowser
import time
import random
import subprocess
import logging, logging.handlers
import logging.config
import http.server
import socketserver
import queue
import urllib, urllib.parse, urllib.request
import json
import re
import base64
import inspect
import builtins
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Lib import *
