#!/usr/bin/env python2.7
# Copyright (C) 2018 Daniel Asarnow
# University of California, San Francisco
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import numpy as np


def bincorr(p1, p2, bins):
    bflat = bins.reshape(-1)
    p1flat = p1.reshape(-1)
    p2flat = p2.reshape(-1)
    fc = p1flat * np.conj(p2flat)
    fcr = np.bincount(bflat, fc.real)
    fcc = np.bincount(bflat, fc.imag)
    mag = np.sqrt(np.bincount(bflat, np.abs(p1flat)**2) *
                  np.bincount(bflat, np.abs(p2flat)**2))
    mag[-1] += 1e-17
    frc = (fcr + fcc*1j) / mag
    return frc