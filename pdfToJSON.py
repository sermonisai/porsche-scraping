from cgitb import text
import fitz, sys, json, jsonlines

def web_scraper(filename):
    doc = fitz.open(filename)
    text_blocks = []

    for page in doc:
        text = page.get_text("blocks")

        for block in text:
            if(block[4][0:7] == "<image:"):
                continue
            else:
                if block[4].count(" ") > 5:
                    dict = {
                        "url" : "",
                        "heading" : "",
                        "prompt" : "",
                        "paragraph" : block[4]
                    }

                    text_blocks.append(dict)  

    filename = text_blocks[0]["paragraph"] + ".jsonl"
    
    with open(filename, "w") as outfile:
        for i in range(1,len(text_blocks)):
            outfile.write(json.dumps(text_blocks[i]) + "\n")

web_scraper(sys.arv[1])
