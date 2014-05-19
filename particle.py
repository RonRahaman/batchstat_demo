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

class SourceBank(np.ndarray):
    """ An array of sites from a point, isotropic, monoenergetic source.

    Args:
        n_sites (int): number of source sites
        pos ([float, float]): position in 2D cartesian space
        energy (float): energy of source

    """
    def __new__(cls, n_sites, pos, energy):
        array = np.ndarray.__new__(cls, n_sites, dtype=phase_space_dtype)
        array['wgt'] = 1.
        array['pos'] = pos
        array['dir'] = [[np.cos(phi), np.sin(phi)] 
                for phi in 2.*np.pi*np.random.random(n_sites) ]
        array['e']   = energy
        return array


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



