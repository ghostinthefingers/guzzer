import argparse
import os
import sys
from spider import spider

parser = argparse.ArgumentParser(description='Guzzer')
parser.add_argument('-u','--url', help='base url of the page', required=True)
args = vars(parser.parse_args())

spider(args['url'])


