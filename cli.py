import sys
import argparse

from argparse_out import ArgumentParserOut
from meuh.engine import MeuhEngine


class BadConfigFileException(Exception):
    pass


def _load_configuration(config_file_path):
    loc = {}
    exec(config_file_path.read(), globals(), loc)
    
    try:
        return loc['MeuhConfig']
    except KeyError:
        raise BadConfigFileException("MeuhConfig variable not found in configuration file.")


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

    config_obj = _load_configuration(arguments.config_file)

    with MeuhEngine(config=config_obj, dwca=arguments.data_file) as engine:
        engine.run(err)

    return 0
