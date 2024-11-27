This code implements the basin delta P approach for dynamic CO2 storage capacity, after Ringrose & Meckel (2019)
Requires installation of coolprops for CO2 density calculations

**Files**
- delta_p_master.py contains the relevant functions
- example.py is a working example

**Inputs**
- reservoir depth
- reservoir permeability
- reservoir thickness
- connected pore volume
- pressure and temperature gradients

**Calculated intermediate parameters**
- Poisson's ratio (from depth)
- Fracture pressure (from Poisson's ratio, overburden and pore pressure gradient)
- Injectivity (from permeability and thickness)
- Rate of pressure buildup (A), from connected pore volume

**Output**
- v_out: array of volume of CO2 stored (one value per year)
- p_out: array of reservoir pressure (one value per year)
- end_year: year simulation stops (maximum of 30 years)

