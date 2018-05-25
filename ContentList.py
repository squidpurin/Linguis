import os
import page as p
class ContentCollection:
    def __init__(self):
        self.content_collection = []

    def init_pages(self):
        directory = os.fsencode('htmls')

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith('html'):
                tmp = p.Page(filename[:5], filename[6:-5], filename)
                self.content_collection.append(tmp)

        for f in self.content_collection:
            print("-"*10)
            print(type(f))
            print(f.getPageID())
            print(f.getPageTitle())
            print(f.getHTMLFilename())
            print("-" * 10)
        self.content_collection.sort()






