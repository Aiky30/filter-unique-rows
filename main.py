from config import *

import sys
import csv

def write_to_output_file(data):

    # Open file for writing
    try:
        # Open the file with option 'rU' Enable Universal newline support
        with open(OUTPUT_FILENAME, 'w') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=OUTPUT_HEADINGS)
            writer.writeheader()

            for row in data:

                writer.writerow(row)

    except IOError as err:
        sys.exit(err)

def filter_unique_objects(mapped_data):

    unique_list = []

    for x in mapped_data:

        if x not in unique_list:
            unique_list.append(x)

    return unique_list


def process_input_file(reader):

    # Load the file into memory (FIXME: this won't work for big data sets)
    mapped_data = []

    for row in reader:

        row_data = {}

        for heading in INPUT_HEADINGS:

            row_data.update({
                heading: row[heading]
            })

        mapped_data.append(row_data)

    return mapped_data

def load_input_file():

    # Open file for reading
    try:
        # Open the file with option 'rU' Enable Universal newline support
        with open(INPUT_FILENAME, 'rU') as csvfile:

            reader = csv.DictReader(csvfile)

            return process_input_file(reader)

    except IOError as err:
        sys.exit(err)


def main():

    input_data = load_input_file()

    unique_list = filter_unique_objects(input_data)

    write_to_output_file(unique_list)

    sys.exit(0)


main()
