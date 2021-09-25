import argparse
import os
import sys
from spider import spider

parser = argparse.ArgumentParser(description='Guzzer')
parser.add_argument('-u','--url', help='base url of the page', required=True)
parser.add_argument('-n','--notfound', help='a pice of not found page.for example:this page not found', required=True)
args = vars(parser.parse_args())

spider(args['url'],args['notfound'])


