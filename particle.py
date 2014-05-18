import numpy as np

phase_space_dtype = np.dtype([
    ('wgt', 'float32'),
    ('pos', 'float32', 2),
    ('dir', 'float32', 2),
    ('e',   'float32')
    ])

tally_dtype = np.dtype([
    ('fission', 'float64', 1),
    ])

class SourceBank(object):
    """ A bank of sites from a point, isotropic, monoenergetic source.

    Args:
        n_sites (int): number of source sites
        pos ([float, float]): position in 2D cartesian space
        energy (float): energy of source

    Attributes:
        array (np.array(dtype=phase_space_dtype)): array of banked sites

    """
    def __init__(self, n_sites, pos, energy):
        self.array = np.empty(n_sites, dtype=phase_space_dtype)
        self.array['wgt'] = 1.
        self.array['pos'] = pos
        self.array['dir'] = [[np.cos(phi), np.sin(phi)] 
                for phi in 2.*np.pi*np.random.random(n_sites) ]
        self.array['e']   = energy
        return

class TallyBins(object):

    def __init__(self):
        return


class Model(object):

    def __init__(self):
        return

    def get_macro_xs(self, pos, e):
        return 0.

class Particle(object):

    def __init__(self, init_coord, model):
        self.pos = init_coord['pos']
        self.dir = init_coord['dir']
        self.e   = init_coord['e']
        self.model = model
        self.alive = True
        return

    def transport(self):
        macro_xs = self.model.get_macro_xs(pos=self.pos, e=self.e)
        return



