import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File for which you want to create a hash")
parser.add_argument("hashvalue", help="hash value that is determined to match the calculated hash of the file")
args = parser.parse_args()

file = args.file
hashval = args.hashvalue

algo = hashlib.md5()

with open(file, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        algo.update(byte_block)
    digest = algo.hexdigest()

exit(0) if digest == hashval else exit("Hash values do not match. Data may be corrupted!")