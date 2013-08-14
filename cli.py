import sys
import argparse

from argparse_out import ArgumentParserOut


def parse_arguments(cli_args, err):
    parser = ArgumentParserOut(description="Meuh, a Dwc-A data quality analyzer.",
                               out=err, err=err)
    
    parser.add_argument("config_file",
                        help="Meuh config file.",
                        type=argparse.FileType('r'))
            
    parser.add_argument("data_file", help="The Dwc-A file you want to analyze.",
                        type=argparse.FileType('r'))
    
    return parser.parse_args(cli_args)


def main(argv, out=sys.stderr, err=sys.stderr):
    arguments = parse_arguments(argv[1:], err)

    return 0
