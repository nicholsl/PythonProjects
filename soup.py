from bs4 import BeautifulSoup

soup = BeautifulSoup(open("wordfreq_ck"))
soup.contents[0]
soup.originalEncoding

str(soup)
