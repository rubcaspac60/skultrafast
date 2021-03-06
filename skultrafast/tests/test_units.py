from skultrafast.unit_conversions import *
import numpy as np

def test_roundtrip():
    x = 100
    assert eV2cm(cm2eV(x)) == x
    assert cm2fs(fs2cm(x)) == x
    assert cm2THz(THz2cm(x)) == x
    assert cm2nm(nm2cm(x)) == x

def test_handle_np():
    x = np.arange(2, 30, dtype='float')
    np.testing.assert_allclose(eV2cm(cm2eV(x)), x)
    np.testing.assert_allclose(cm2fs(fs2cm(x)), x)
    np.testing.assert_allclose(cm2THz(THz2cm(x)),x)
    np.testing.assert_allclose(cm2nm(nm2cm(x)), x)
