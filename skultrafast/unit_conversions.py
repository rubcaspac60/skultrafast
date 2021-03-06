"""
This module contains functions to covert between units.
"""
import numpy as np
from scipy.constants import physical_constants, c


c_cm = c*100
names = dict(
    cm = "wavenumbers in 1/cm",
    fs = "period in femotoseconds",
    nm = "wavelengths in nanometer",
    eV = "energy in electron Volt",
    THz = "frequency in THz",
    )


def make_doc(func):
    a, b = str.split(func.__name__, '2')

    func.__doc__ = ('%s to %s'%(names[a], names[b])).capitalize()
    return func




@make_doc
def fs2cm(t):
    return 1/(t*1e-15 * c_cm)

@make_doc
def cm2fs(cm):
    return  1e15/(cm * c_cm)

@make_doc
def nm2cm(nm):
    return 1e7/nm

@make_doc
def cm2nm(cm):
    return 1e7/cm

@make_doc
def cm2eV(cm):
    eV_m = physical_constants['electron volt-inverse meter relationship'][0]
    eV_cm = eV_m/100
    return cm/eV_cm

@make_doc
def eV2cm(eV):
    eV_m = physical_constants['electron volt-inverse meter relationship'][0]
    eV_cm = eV_m/100
    return eV*eV_cm

@make_doc
def cm2THz(cm):
    return 1/fs2cm(cm)/1e-3

@make_doc
def THz2cm(THz):
    return cm2fs(1e3/THz)

print(fs2cm.__doc__)


def dichro_to_angle(d):
    return np.arccos(np.sqrt((2*d-1)/(d+2)))/np.pi*180


def angle_to_dichro(x):
    return (1+2*np.cos(x)**2)/(2-np.cos(x)**2)


def angle_to_aniso(ang):
    return  2/5*(3*np.cos(ang)**2-1)/2


def aniso_to_angle(r):
    return np.arccos(np.sqrt((r*10/2+1)/3))
