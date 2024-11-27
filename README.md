This code implements the basin delta P approach for dynamic CO2 storage capacity, following Ringrose & Meckel (2019)

**Files**
- delta_p_master.py contains the relevant functions
- example.py is a working example

**Inputs**
- reservoir depth
- reservoir permeability
- reservoir thickness
- connected pore volume (v_p)
- pressure and temperature gradients

**Calculated intermediate parameters**
- Poisson's ratio (from depth)
- Fracture pressure (from Poisson's ratio, overburden and pore pressure gradient)
- Injectivity (from permeability and thickness)
- Rate of pressure buildup (A), from connected pore volume

