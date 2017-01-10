"""
Fetches set IDs from data.pr.gov without their restrictions.
"""
import time, json, argparse, requests

parser = argparse.ArgumentParser(description='Download the dataset.')
parser.add_argument('set_id', metavar="set_id", type=str, help="The set_id to fetch")
parser.add_argument('filename_out', metavar="filename_out", type=str, help="The filename for the result.")
args = parser.parse_args()

count = 0
fetched = requests.get('https://data.pr.gov/resource/%s.json?$offset=%s&$limit=1000' % (args.set_id, count)).json()

while True:
    count = count + 1000
    print("Iterating cycle #%s" % count)
    sets = requests.get('https://data.pr.gov/resource/%s.json?$offset=%s&$limit=1000' % (args.set_id, count)).json()
    if sets == []:
        break
    else:
        fetched = fetched + sets
        print("So far dataset is %s records, taking a break." % len(fetched))

with open("out/%s" % args.filename_out, 'a') as f:
    print("Received %s records." % len(fetched))
    f.write(json.dumps(fetched, indent=2))


