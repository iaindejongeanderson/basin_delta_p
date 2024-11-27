import numpy as np

def dimensionless_pressure(t_D):
    if t_D == 0:
        t_D = 0.25 * 1.781
    return 1/2 * np.log((4*t_D)/1.781)

def delta_p(p_init,p_well,p_final,A,inj,rho_co2):
    
    # preallocate outputs
    t_D_out = np.zeros(31)
    p_out = np.zeros(31)
    v_well = np.zeros(31)
    
    # initial conditions
    t_D = 0
    p_res = p_init
    
    # main function
    while (p_res < min(p_final,p_well)) and (t_D <= 30):
        p_D = dimensionless_pressure(t_D)
        p_res = p_init + (A * p_D)
        rate = inj * (p_well - p_res)
        
        v_well[t_D]=(365 * rho_co2 * rate) * 1e-9
        t_D_out[t_D]=t_D
        p_out[t_D]=p_res
        
        t_D = t_D + 1
        
    if t_D == 31:
        print("no pressure constraint, sim runs for full 30 years")
    else:
        print("sim stops after ",t_D-1,' years')

    v_out = np.array(v_well)    
    cumulative_storage = np.round(sum(v_well[v_well>0]),2)
    print('CO2 stored = ',cumulative_storage,' Mt')
        
    return v_out,t_D-1,p_out

def estimate_frac_pres(sv,pp,v):
    # Equation 7 from Zhang (2011) 
    # https://doi.org/10.1016/j.earscirev.2011.06.001
    # Estimate of most-likely fracture pressure
    return (3*v)/(2*(1-v))*(sv-pp)+pp 

def injectivity_index(k,h,co2_den):
    
    # estimate of injectivity index based on the correlations presented
    # in https://doi.org/10.1002/ghg.2046
    # Those authors express injectivity in tonnes/year/psi so unit
    # conversions required to get m3/day/bar
    
    ## unit conversions
    m_to_ft = 3.28084
    ton_to_kg = 1e3
    yr_to_day = 365.25
    psi_to_bar = 0.0689476
    
    h_ft = m_to_ft * h
    
    # 0.08 is their median coefficient, 0.03 is low, 0.23 is high 
    j_mt_yr_psi = 0.23*k*h_ft
    
    return j_mt_yr_psi*ton_to_kg/co2_den/yr_to_day*psi_to_bar
