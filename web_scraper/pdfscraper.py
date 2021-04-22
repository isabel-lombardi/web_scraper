import sys
import re
import os

from bs4 import BeautifulSoup
import requests


class PDFScraper:

    def __init__(self, URL):
        self.URL = URL
        self.pdf_URL = ""