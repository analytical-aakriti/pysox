import unittest
import os

from sox import transform
from sox.core import SoxError


def relpath(f):
    return os.path.join(os.path.dirname(__file__), f)


SPACEY_FILE = relpath("data/annoying filename (derp).wav")
INPUT_FILE = relpath('data/input.wav')
OUTPUT_FILE = relpath('data/output.wav')

def new_transformer():
    return transform.Transformer()

class TestTransformerChorus(unittest.TestCase):

    

    def test_invalid_gain_in(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(gain_in=0)

    def test_invalid_gain_out(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(gain_out=1.1)

    def test_invalid_n_voices(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(n_voices=0)

    def test_invalid_delays(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(delays=40)

    def test_invalid_delays_wronglen(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(delays=[40, 60])

    def test_invalid_delays_vals(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(delays=[40, 10, 60])

    def test_invalid_decays(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(decays=0.4)

    def test_invalid_decays_wronglen(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(decays=[0.2, 0.6])

    def test_invalid_decays_vals(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(decays=['a', 'b', 'c'])

    def test_invalid_speeds(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(speeds=0.4)

    def test_invalid_speeds_wronglen(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(speeds=[0.2, 0.6])

    def test_invalid_speeds_vals(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(speeds=[0.2, 0.2, 0])

    def test_invalid_depths(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(depths=12)

    def test_invalid_depths_wronglen(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(depths=[])

    def test_invalid_depths_vals(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(depths=[0.0, 0.0, 0.0])

    def test_invalid_shapes(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(shapes='s')

    def test_invalid_shapes_wronglen(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(shapes=['s', 's'])

    def test_invalid_shapes_vals(self):
        tfm = new_transformer()
        with self.assertRaises(ValueError):
            tfm.chorus(shapes=['s', 's', 'c'])

