"""Fourier representation"""

from Representation import Representation, QFunRepresentation
from Tools import indices, pi, cos, dot

__copyright__ = "Copyright 2013, RLPy http://www.acl.mit.edu/RLPy"
__credits__ = ["Alborz Geramifard", "Robert H. Klein", "Christoph Dann",
               "William Dabney", "Jonathan P. How"]
__license__ = "BSD 3-Clause"

class Fourier(Representation):

    def __init__(self,domain,logger,order=3):
        dims = domain.state_space_dims
        self.coeffs = indices((order,)*dims).reshape((dims,-1)).T
        self.features_num = self.coeffs.shape[0]
        super(Fourier,self).__init__(domain,logger)

    def phi_nonTerminal(self,s):
        # normalize the state
        s_min,s_max = self.domain.statespace_limits.T
        norm_state = (s - s_min) / (s_max - s_min)
        return cos(pi * dot(self.coeffs, norm_state))

    def featureType(self):
        return float

class QFourier(Fourier, QFunRepresentation):
    pass
