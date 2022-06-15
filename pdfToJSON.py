from cgitb import text
import fitz
import sys

def web_scraper(filename):
    doc = fitz.open(filename)
    text_blocks = []
    for page in doc:
    #    text_page = page.get_textpage()


    #    text_blocks.append(text_page.extractText())

    #for blocks in text_blocks:
    #    print(blocks)


    #for blocks in text_blocks:
    #    print(blocks[4])
    

        text = page.get_text("blocks")
        for block in text:
            if(block[4][0:7] == "<image:"):
                continue
            else:
                print(block[4])
                



    #text_blocks.append(block.extractRAWDICT())



    


web_scraper(sys.argv[1])
