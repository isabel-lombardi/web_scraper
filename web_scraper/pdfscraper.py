import sys
import re
import os

from bs4 import BeautifulSoup
import requests


class PDFScraper:

    def __init__(self, URL):
        self.URL = URL
        self.pdf_URL = ""

    def get_pdf(self):
        """
        Given the requested URL, the file is searched in the HTML structure,
        cleaned by HTML tags and returned the URL containing the PDF
        """

        try:
            # connect to website to get pdf file, get to retrieve data
            r = requests.get(self.URL)
            r.raise_for_status()      # implement a different actions for the different error types


            soup = BeautifulSoup(r.text, "html.parser")

            try:
                # extracting the URL found within a page’s <a> tags and href
                link = soup.find("a", attrs={"href": re.compile(r'(.pdf)')})  # to find link ends with ".pdf"

                # clear link from html structure
                # [^"\s]] search for any character except those in brackets after "^"
                # ?P<url>, captures the group "url" found by the regex
                pdf_url = re.search('(?P<url>https?://[^"\s]+)', str(link)).group("url")
                self.pdf_URL = pdf_url

            except AttributeError:
                print("The requested file was not found in the URL")
                sys.exit(1)

        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)