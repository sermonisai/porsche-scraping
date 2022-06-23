# Scraping of Porsche Newsroom

## Description
This script is designed to read the PDF format of Porsche Newsroom articles and processing these articles as JSON Lines documents.

### requestArticles.py
This script retrieves all Newsroom articles in PDF format from June 1st to June 15. This results in 25 PDFs.
<!---First is a basic scrape of all the PDFs within the month of July from the first to the 15th, resulting in 25 PDFs.--->

### pdfToJSON.py
We then use the PyMuPDF library to extract information from each PDF and convert it into a JSON Lines document.

### Name of Script
Finally we process each PDF to remove extraneous data in order to allow for neural embedding of each document.
<!---Finally we process the PDFs to remove extraneous data to allow for proper usage during the NN training stages, which are next.--->

Each JSON Line consist of the following elements.

```json
"url": str (required)
"heading": str (optional - not all paragraphs are under a heading)
"prompt": str (optional - the question before an answer during an interview)
"paragraph": str (required)
```

## How to run
TBD.

### Contact
Justin Lai, justinlai@ucsb.edu

George Bennett, bennettgc@outlook.com

Ronaldo Santiago Vazquez, rsant057@ucr.edu

### Authors
George Bennett, Justin Lai, and Ronaldo Santiago Vazquez.

