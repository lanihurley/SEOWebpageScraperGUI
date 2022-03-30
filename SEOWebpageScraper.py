"""
Program: SEOWebpageScraper.py
Date: 3/22/2022
Author: Lani Hurley
Program is an SEO tool that scrapes links: "a" and "href", images: "alt" text and "src"  from webpage,
and metatitle keywords.
* Must have breezypythongui.py file in same directory.
*Must Import Python requests and BeautifulSoup modules.
"""

import requests
from breezypythongui import EasyFrame
from bs4 import BeautifulSoup


class SEOWebpageScraper(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="SEO Websraper Tool", background="#4a5772", width=1900, height=700)
        # Label and field for the input and output
        self.addLabel(text="Please enter URL\nto be scraped:", background="#4a5772", row=1, column=1,
                      font="Rajdhani", foreground="white")
        self.addLabel(text="Links & Keywords listed below:", background="#4a5772", row=1, column=0,
                      font="Rajdhani", foreground="white", sticky="W")
        self.addLabel(text="Images source and alternate text below:", background="#4a5772", row=6, column=0,
                      font="Rajdhani", foreground="white", sticky="W")
        self.inputField = self.addTextField(text="https://www.", row=1, column=1, width=70)
        self.outputArea = self.addTextArea(text="", row=2, column=0, columnspan=3, height=15, wrap="word")
        self.outputArea2 = self.addTextArea(text="", row=7, column=0, columnspan=3, height=15, wrap="word")
        # The command button
        self.button = self.addButton(text="Click to Get Links,\n Keywords and Images", row=1, column=2,
                                     command=self.is_valid)

    def is_valid(self):

        url = self.inputField.get()
        # concatenate requests module to get() method and put it in a variable
        response = requests.get(url).text
        # pass it to Beautiful soup to be parsed into individual tags within the html
        soup = BeautifulSoup(response, "html5lib")
        # create a variable to hold all "a" tags in html webpage
        all_anchor_tags = soup.find_all("a")
        images = [[a["src"], a["alt"]] if "alt" in str(a) else [a["src"], ""] for a in soup.find_all("img")]
        keywords = (soup.find('title')).get_text()
        # create variable to hold string data
        links_str = ""
        # create for() loop to search through the parsed text data and retrieve all "a" and "href"
        for anchor_tag in all_anchor_tags:
            link = anchor_tag.get("href") + "\n"
            # create a new variable to hold on to and combine the links into a string to print out
            links_str += link
            # display the links in outputArea
        self.outputArea.setText(
            "\nTHE <META> DATA KEYWORDS ARE:\n" + keywords + "\n\n" + "THE LINKS START HERE:" + "\n\n" +
            links_str)
        self.outputArea2.setText(f"{images}")


# definition of the main() function for program entry
def main():
    SEOWebpageScraper().mainloop()


# global call to trigger the main() function
if __name__ == "__main__":
    main()
