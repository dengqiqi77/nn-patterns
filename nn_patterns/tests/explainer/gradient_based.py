# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


from ...utils.tests import dryrun

from ...explainer import GradientExplainer
from ...explainer import DeConvNetExplainer
from ...explainer import GuidedBackpropExplainer
from ...explainer import AlternativeGradientExplainer


class TestGradientExplainer(dryrun.ExplainerTestCase):

    def _method(self, output_layer):
        return GradientExplainer(output_layer)


class TestDeConvNetExplainer(dryrun.ExplainerTestCase):

    def _method(self, output_layer):
        return DeConvNetExplainer(output_layer)


class TestGuidedBackpropExplainer(dryrun.ExplainerTestCase):

    def _method(self, output_layer):
        return GuidedBackpropExplainer(output_layer)


class TestAlternativeGradientExplainer(dryrun.ExplainerTestCase):

    def _method(self, output_layer):
        return AlternativeGradientExplainer(output_layer)
