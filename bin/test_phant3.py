#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python3 ./test_phant3.py

import argparse
import logging
import os
import shutil
import sys
import tempfile

from phant3 import VERSION

# Configure tempfile dir
name = os.path.basename(__file__)
tempdirname = tempfile.mkdtemp(prefix='python3-phant-', dir=tempfile.tempdir)

# Determine a location for logfile
logging_filename = '{}.log'.format(
    os.path.join(tempdirname, os.path.basename(__file__)))
print('-I- Using log file {}'.format(logging_filename), file=sys.stderr)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename=logging_filename,
    filemode='w')
# Define a Handler which writes INFO messages or higher to the sys.stderr ('console')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)
logger.info('Version: {}'.format(VERSION))

# Parse CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--verbose', help="increase output verbosity", action='count')
    args = parser.parse_args()

    if args.verbose:
        console.setLevel(logging.DEBUG)

# Start it up
if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        sys.stdout.flush()
        sys.stderr.flush()
        logger.warn('Deleting tempdir {}'.format(tempdirname))
        shutil.rmtree(tempdirname)
