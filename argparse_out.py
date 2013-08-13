# -*- coding: utf-8 -*-

import argparse
import sys


# We override the standard ArgumentParser to allows optional configuration of
# The output/error streams (makes testing easier)
# We basically rewrote each method that write to stdout or stderr to make it "redirectable"
class ArgumentParserOut(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        self.out_stream = kwargs.pop('out', sys.stdout)
        self.err_stream = kwargs.pop('err', sys.stderr)
        
        argparse.ArgumentParser.__init__(self, *args, **kwargs)
    
    # We ignore the file argument and send output to self.out_stream
    def print_help(self, file=None):
        self._print_message(self.format_help(), self.out_stream)
    
    # We ignore the file argument and send output to self.out_stream
    def print_usage(self, file=None):
        self._print_message(self.format_usage(), self.out_stream)
        
    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, self.err_stream)
        sys.exit(status)
