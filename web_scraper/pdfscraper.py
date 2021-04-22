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


    def save_pdf(self, output_path):
        """
        Given the URL containing the PDF file, the name of the folder to save the file is asked,
        it is extracted and saved locally.

        """

        # create folder if it does not exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        try:
            # get, to retrieve data
            r = requests.get(self.pdf_URL, stream=True)  # if True will keep our session with server open
            r.raise_for_status()  # implement a different actions for the different error types

            try:
                # The URL containing the PDF could be for example:
                # https://www.kaleyra.com/wp-content/uploads/SMS-surcharge-USA-1.pdf
                # I extract the filename after the last "/"
                filename = self.pdf_URL.split("/")[-1]

                file_path = os.path.join(output_path, filename)

                if str(file_path).endswith(".pdf"):  # check if the file is a PDF
                    with open(file_path, "wb") as file:  # iterates over the response data

                        for chunk in r.iter_content(chunk_size=1024):  # number of bytes it should read into memory
                            if chunk:  # writing one chunk at a time to pdf file
                                file.write(chunk)
                                file.flush()
                                os.fsync(file.fileno())  # forces write of file to disk.
                        print("\n-The file '{}' is available in the folder '{}'".format(filename, output_path))
                        return file_path

                else:
                    raise Exception("File format not supported")

            # when we attempt to open a file and if it does not exist, the IOError will be encountered
            except (IOError, OSError) as ioe:
                print(ioe.errno)
                print(ioe)

        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)
