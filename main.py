from web_scraper.pdfscraper import PDFScraper
from web_scraper.extract_data import ExtractData
from argparse import ArgumentParser

"""
Generate and return a URL based on the choice of the State (USA/Canada)
to access the page containing the prices of the same
The dictionary contains the States with the attached Path, for which the PDF file is available,
with the possibility of being updated in the future
The page for the selected State will return, for example: https://www.kaleyra.com/pricing/us-usd/
 """


if __name__ == "__main__":
    base_url = "https://www.kaleyra.com/pricing"
    allowed_states = {"usa": "us-usd/", "canada": "ca-cad/"}

    parser = ArgumentParser(description="Web Scraper Kaleyra Fares")
    parser.add_argument("-s", "-state", type=str, help="State", choices=allowed_states.keys())

    parser.add_argument("-o", "-output-path", type=str, help="Output Path")
    args = parser.parse_args()

    url = "{}/{}".format(base_url, allowed_states[args.s])

    s = PDFScraper(url)
    s.get_pdf()
    pdf_path = s.save_pdf(args.o)

    e = ExtractData(pdf_path)
    e.data_from_pdf()
