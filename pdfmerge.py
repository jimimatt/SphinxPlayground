#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Simple tool for merging pdf files from command-line.

Usage
...on Windows:
python pdfmerge.py out.pdf A.pdf B.pdf

...on Linux:
./pdfmerge.py out.pdf A.pdf B.pdf

The first argument 'out.pdf' is the name for the output-file. The file extension '.pdf' is
not added automatically. The output-file will be overwritten if it already exists.
The following parameters can be of any number and are the filenames of the pdf files to
be merged.
"""
from PyPDF2 import PdfFileReader, PdfFileMerger


def pdf_merge(output_filename, input_files):
    """
    This does the magic and merges the pdf files in 'input_files' in the same order to a
    new created file 'output_filename'. An existing output_filename will be overwritten.

    :param output_filename: name for the output pdf
    :param input_files: list of filenames
    """
    input_streams = []
    try:
        merger = PdfFileMerger(strict=False)
        for filename in input_files:
            print("opening '{}'".format(filename))
            input_streams.append(open(filename, 'rb'))

        for input_stream, input_filename in zip(input_streams, input_files):
            print("merging '{}'".format(input_filename))
            merger.append(PdfFileReader(input_stream))

        print("write to file '{}'".format(output_filename))
        merger.write(output_filename)
    finally:
        for file in input_streams:
            file.close()
    print("done.")


if __name__ == '__main__':
    import sys
    pdf_merge(sys.argv[1], sys.argv[2:])
