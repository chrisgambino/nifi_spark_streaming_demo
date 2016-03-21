import random
import sys
import json
Countries = ['USA','CANADA','MEXICO','ENGLAND','RUSSIA','CHINA','JAPAN']
Products = ['ELECTRONICS','FOOD','SOFTWARE','RAW_MATERIALS','WEAPONS']

transaction={'origin':random.choice(Countries),'merchant_location':random.choice(Countries),'amount':random.randint(0,100000),'type':random.choice(Products)}

sys.stdout.write(json.dumps(transaction))
