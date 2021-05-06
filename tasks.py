# -*- coding: utf-8 -*-
"""
Invoke - Tasks
==============
"""

from invoke import task
from invoke.exceptions import Failure

from colour.utilities import message_box

import app

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2020-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'APPLICATION_NAME', 'ORG', 'CONTAINER', 'clean', 'quality', 'formatting'
]

APPLICATION_NAME = app.__application_name__


@task
def clean(ctx, bytecode=False):
    """
    Cleans the project.

    Parameters
    ----------
    bytecode : bool, optional
        Whether to clean the bytecode files, e.g. *.pyc* files.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Cleaning project...')

    patterns = []

    if bytecode:
        patterns.append('**/__pycache__')
        patterns.append('**/*.pyc')

    for pattern in patterns:
        ctx.run("rm -rf {}".format(pattern))


@task
def quality(ctx, flake8=True):
    """
    Checks the codebase with *Flake8*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    flake8 : bool, optional
        Whether to check the codebase with *Flake8*.

    Returns
    -------
    bool
        Task success.
    """

    if flake8:
        message_box('Checking codebase with "Flake8"...')
        ctx.run('flake8')


@task
def formatting(ctx, yapf=True):
    """
    Formats the codebase with *Yapf*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    yapf : bool, optional
        Whether to format the codebase with *Yapf*.

    Returns
    -------
    bool
        Task success.
    """

    if yapf:
        message_box('Formatting codebase with "Yapf"...')
        ctx.run('yapf -p -i -r .')
