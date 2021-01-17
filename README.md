# biasbot
A web scraper that searches for bias on Wikipedia. 

This is accomplished by searching for keywords that often indicate bias. To read or change these, go to the list called "words" on Line 28. 

The biasbot can also detect whether a keyword is within a quote. Quotes are allowed and often expected to be biased, so this prevents a lot of false positives. 
Quote-checking is accomplished with BeautifulSoup. 
