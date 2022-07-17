import argparse
parser = argparse.ArgumentParser(description='Read PGN file to JSON and print to standard out')
parser.add_argument('pgn_file_path',metavar='PGN_FILE', type=str, help='PGN file to parse')
parser.add_argument('-f', '--file',dest='json_file_path',metavar='OUTPUT_FILE', type=str, default=None, help='write JSON into OUTPUT_FILE')

args = parser.parse_args()

import json
import re
tag_re = r'\[([^\[\]]*)\]'
tag_pair_re = r'(\w*)\s+"(.*)"'

def write(entry, is_first_write):
    json_dump = json.dumps(entry, indent=4)
    if args.json_file_path != None:
        with open(args.json_file_path, 'a') as file:
            if is_first_write != True:
                file.write(',')
            file.write(json_dump)
            return

    print(json_dump)

if args.json_file_path != None:
    with open(args.json_file_path, 'w') as file:
        file.write('[')

with open(args.pgn_file_path, 'r') as file:
    tags = {}
    pgn_str = ''
    is_first_write = True
    reading_tags = True #pgn entry begin with meta data
    for line in file.readlines():
        tags_match = re.findall(tag_re, line)
        if tags_match and reading_tags == False:
            #if we found tags and we were expecting more move data
            #start new entry and save current one
            entry = {
                        'tags': tags,
                        'pgn': pgn_str,
                    }
            write(entry, is_first_write)

            tags = {}
            pgn_str = ''
            reading_tags = True
            is_first_write = False
        elif not tags_match:
            reading_tags = False

        if reading_tags:
            for match in tags_match:
                tag_pair = re.match(tag_pair_re, match)
                if tag_pair == None:
                    raise ValueError('Tag WRONG!')
                tags[tag_pair.group(1)] = tag_pair.group(2)

        pgn_str += line

if args.json_file_path != None:
    with open(args.json_file_path, 'a') as file:
        file.write(']')
