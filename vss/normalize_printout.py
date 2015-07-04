import argparse
import json
import os
import re

parser = argparse.ArgumentParser(
    description='Process VSS export data into json.'
)

parser.add_argument('--file', required=True, help='File with raw VSS data.')

args = parser.parse_args()

underline_regexp = r"(\s+-+)+"


def find_column_defninition(contents):
    last_line = ''
    for line in contents.split('\n'):
        column_underline_match = re.search(underline_regexp, line)

        if column_underline_match:
            return last_line, line

        last_line = line


def get_column_widths(line):
    return [len(underline) for underline in line.strip().split(' ')]


def get_columns(line):
    return re.split(r'\s\s+', line.strip())


def process_field(column_name, value):
    if column_name == 'Movie Title':
        # Formats
        value = value.replace("-DVD", '')
        value = value.replace("-BLURAY", '')
        value = value.replace("3D BLURAY-", '')

        # Dates
        value = re.sub(r'\(\d+\)', '', value)
        value = re.sub(r'-\d+$', '', value)

    return value

data = []
with open(args.file, 'r') as f:
    contents = f.read()
    definition, underline = find_column_defninition(contents)
    columns = get_columns(definition)
    column_widths = get_column_widths(underline)

    data_regexp = r''
    for width in column_widths[0:-1]:
        data_regexp += r".{%d}\s" % width
    data_regexp = re.compile(data_regexp)

    for line in contents.split('\n'):
        # Match data - ignore headings, blank lines, and heading underlines
        is_data = (
            re.match(data_regexp, line.strip())
            and columns[0] not in line
            and not re.match(underline_regexp, line)
            and line.strip()
            and "Listing of All Movies" not in line
            and not re.match(r"^\s{6}", line)
        )
        if not is_data:
            continue

        line = line.strip()

        datum = {}
        for index, width in enumerate(column_widths):
            datum[columns[index]] = process_field(
                columns[index],
                line[:width].strip()
            )
            line = line[width:]
        data.append(datum)

print json.dumps(data, indent=4)
