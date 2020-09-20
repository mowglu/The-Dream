# The-Dream
A project for a Business Aviation company, that automates tasks like collecting information from acukwik.com, and parsing through data obtained from an aircraft performance tool published by APG (Aircraft Performance Group).

The project used BeautifulSoup and string manipulation for acquiring data from acukwik.com. 

Selenium's web automation was used to navigate through APG's webite, and then the downloaded PDF reports with the relevant data were parsed. This parsing involved Tabula and Tesseract.
All data collected was written into Pandas dataframe objects, and then written to "Source" Excel files. The TemplateV1 Excel file has macros to acquire information from these Source files.

