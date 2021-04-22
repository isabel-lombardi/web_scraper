from web_scraper.pdfscraper import PDFScraper


def generate_url(URL):
    """
    Generate and return a URL based on the choice of the State (USA/Canada)
    to access the page containing the prices of the same
    The dictionary contains the States with the attached Path, for which the PDF file is available,
    with the possibility of being updated in the future
    The page for the selected State will return, for example: https://www.kaleyra.com/pricing/us-usd/
    """

    allowed_state = {"usa": "us-usd/",
                     "canada": "ca-cad/"}

    # user choice, USA - Canada (pdf available)
    print("You can choose to extract prices for USA or Canada")
    while True:
        state = input("Enter the name of the State: ").lower()

        if state in allowed_state.keys():
            URL += allowed_state.get(state)
            return URL

        else:
            print("Price list is not available for this State or does not exist. Choose between USA and Canada")