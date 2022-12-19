"""Main file."""
import os

from websites import Website

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

website = Website("websites.txt")
