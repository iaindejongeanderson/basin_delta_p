from delta_p_master import delta_p,estimate_frac_pres,injectivity_index
from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Input data
# =============================================================================

# Constants

D = 1500 # depth, m
sf_t = 10 # seafloor temp, 10 degC

# Pressure gradients (per km)
grad_p = 10 # pressure gradient, hydrostatic, MPa/km
grad_t = 30 # temp gradient, 30 degC/km
grad_o = 23 # overburden gradient, MPa/km

# Aquifer conditions

T_f = (grad_t * D/1000) + sf_t # formation temperature, degC
p_init = grad_p * D/1000 # initial reservoir pressure, MPa
sv = grad_o * D/1000 # vertical stress, MPa
rho_co2 = PropsSI('D', 'T', T_f+273.15, 'P', p_init*1E6, 'CO2') # CO2 density, kg/m3

## Estimating fracture pressure

v = 0.1+(0.06*(D/1000)) # poisson's ratio
FP = estimate_frac_pres(sv,p_init,v)

## Conversion to bars

p_init = p_init * 10 # Mpa to bars
p_final = FP * 10 # Mpa to bars

## %% Estimate of injectivity index
k = 271 #mD
h = 275 #m
ic = injectivity_index(k,h,rho_co2)

## Well pressure, unclear what a reasonabe value is
## Should be lower than fracture pressure
## Currently defined as 2/3 between initial and frac pressure

p_well = p_init+(2/3*(p_final-p_init)); 

## A is the key parameter in defining how closed or open the site is
## Higher A = bigger pressure buildup.

v_p = 6.5 # pore volume in km2
A = -6.785 * v_p + 44.617   # Tian Guo's function for A versus v_p Large-scale CO2 Injection Analysis:
                            # understanding pressure variation in
                            # multiple compartments using
                            # analytical and computational
                            # analysis approaches


v_o,t_D,t_D_out,p_out = delta_p(p_init,p_well,p_final,A,ic,rho_co2)
