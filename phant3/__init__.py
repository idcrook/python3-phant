# -*- coding: utf-8 -*-
"""Client for Sparkfun Phant."""

__author__ = 'David Crook'
__copyright__ = 'Copyright 2020'
__credits__ = ['phant', 'python-phant']
__license__ = 'MIT'
__version__ = "0.1.2"
__maintainer__ = 'David Crook'
__email__ = 'idcrook@users.noreply.github.com'
__status__ = "Development"

import logging

logger = logging.getLogger(__name__)
logger.info('version={}'.format(__version__))

# clean up namespace
del (logger)
