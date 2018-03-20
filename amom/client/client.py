"""
    # TODO jstejska: Package description
"""

from inspect import stack

from ..node import Node
from odict import odict


class Client:
    """
    Abstract class for every messaging client
    """

    # Required variables
    supported_protocols = []
    name = ''
    version = ''

    def __init__(self):
        self.logs = None  # @TODO

    @property
    def get_supported_protocols(self):
        return self.supported_protocols

    @property
    def get_name(self):
        return self.name

    @property
    def get_version(self):
        return self.version

    @staticmethod
    def _not_supported():
        print("Function %s is not supported for this client." % stack()[1][3])
        raise NotImplementedError
