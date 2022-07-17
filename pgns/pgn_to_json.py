import argparse
parser = argparse.ArgumentParser(description='Read PGN file to JSON and print to standard out')
parser.add_argument('pgn_file_path',metavar='PGN_FILE', type=str, help='PGN file to parse')
parser.add_argument('-f', '--file',dest='json_file_path',metavar='OUTPUT_FILE', type=str, default=None, help='write JSON into OUTPUT_FILE')

args = parser.parse_args()

import json
import re
tag_re = r'\[([^\[\]]*)\]'
tag_pair_re = r'(\w*)\s+"(.*)"'

move_item_re = r'(\d+)\.\s?([^\s]+)\s?([^\s]+)?'
result_re = r'[^O\s]+-[^O\s]+'

def parse_move_str(string):
    moves = {}
    moves['list'] = []
    moves['result'] = re.search(result_re, string).group(0)
    string = re.sub(result_re, '', string)
    moves_iter = re.finditer(move_item_re, string)
    for move in moves_iter:
        move_dict = { 'light_move': move.group(2) }
        if move.group(3) != None:
            move_dict['dark_move'] = move.group(3);
        moves['list'].append( move_dict )
    return moves;

def write(entry, is_first_write):
    json_dump = json.dumps(entry, indent=4)
    if args.json_file_path != None:
        with open(args.json_file_path, 'a') as file:
            if is_first_write != True:
                file.write(',')
            file.write(json_dump)
            return

    print(json_dump)

if __name__ == "__main__":
    if args.json_file_path != None:
        with open(args.json_file_path, 'w') as file:
            file.write('[')

    with open(args.pgn_file_path, 'r') as file:
        is_first_write = True
        reading_tags = True #pgn entry begin with meta data
        tags = {}
        move_str = ''
        for line in file.readlines():
            tags_match = re.findall(tag_re, line)
            if tags_match and reading_tags == False:
                #if we found tags and we were expecting more move data
                #start new entry and save current one
                entry = {
                        'tags': tags,
                        'moves': parse_move_str(move_str)
                        }
                write(entry, is_first_write)
                is_first_write = False

                tags = {}
                move_str = ''
                reading_tags = True
            elif not tags_match:
                reading_tags = False

            if reading_tags:
                for match in tags_match:
                    tag_pair = re.match(tag_pair_re, match)
                    if tag_pair == None:
                        raise ValueError('Tag WRONG!')
                    tags[tag_pair.group(1)] = tag_pair.group(2)
            else:
                move_str += line.strip('\n') + ' '

    if args.json_file_path != None:
        with open(args.json_file_path, 'a') as file:
            file.write(']')
