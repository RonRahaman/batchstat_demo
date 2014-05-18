import numpy as np

phase_space_dtype = np.dtype([
    ('wgt', 'float32'),
    ('pos', 'float32', 3),
    ('dir', 'float32', 3),
    ('e',   'float32')
    ])

tally_dtype = np.dtype([
    ('fission', 'float64', 1),
    ])

class SourceBank(object):

    def __init__(self, n_sites, pos, energy):
        self.sample_external_source(n_sites, pos, energy)
        return

    def sample_external_source(self, n_sites, pos, energy):
        self.array = np.empty(n_sites, dtype=phase_space_dtype)
        self.array['wgt'] = 1.
        self.array['pos'] = pos
        self.array['dir'] = self._sample_isotropic_angles(n_sites)
        self.array['e']   = energy
        return

    def _sample_isotropic_angles(self, n):
        phi = 2.*np.pi*np.random.random()
        mu  = 2.*np.random.random() - 1.
        return [[ mu, 
                np.sqrt(1.-mu**2) * np.cos(phi),
                np.sqrt(1.-mu**2) * np.sin(phi) ] for i in range(n) ]

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



