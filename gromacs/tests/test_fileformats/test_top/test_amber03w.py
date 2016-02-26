from __future__ import division, absolute_import, print_function

import numpy as np
import numpy.matlib
from numpy.testing import assert_array_equal, assert_, run_module_suite

from gromacs.fileformats import TOP
from gromacs import testing as tm

from base import TopologyPrimitive

class TestCharmm(TopologyPrimitive):
	processed = 'amber03w/processed.top'
	molecules = ['Protein_chain_A', 'SOL', 'IB+', 'CA', 'CL', 'NA', 'MG', 'K', 'RB', 'CS', 'LI', 'ZN']

if __name__ == "__main__":
    run_module_suite()