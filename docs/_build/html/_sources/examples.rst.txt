Examples
===========

Monod Model
^^^^^^^^^^^


A monod model can be run using the following code::

    import planktonpy as pp
    from planktonpy import parameters
    from planktonpy import groups
    from planktonpy import environments
    
    plankton_groups = groups("ward2016")

    plankton_param =  parameters("ward2016")

    environment = environments("oligotrophic_surface")

    model = pp.monod(plankton_groups, plankton_param, environment) 

Custom Parameters
^^^^^^^^^^^^^^^^^

Custom parameters can be defined if desired::

    import planktonpy as pp

    plankton_groups = pp.def_plankton(pico = 5, euk=5, diat = 5, 
    					cocco=5, diat=5, zoo=5)
    					
    plankton_param = pp.def_param(cocco_kN = 0,
    				   cocco_kI = 0,
    				   cocco_kSi = 0,
    				   cocco_min = 5,
    				   cocco_max = 30,
    				   cocco_defense = 0.2 
				   diat_kN = 0,
    				   diat_kI = 0,
    				   diat_kSi = 0,
    				   diat_min = 5,
    				   diat_max = 30,
    				   diat_defense = 0.2,
    				   zoo_min = 20,
    				   zoo_max = 200,   
    				   
    environment = pp.def_env(N=0.5, Si=0.5, PAR=500, K=0.02)  
    
    model = pp.monod(plankton_groups, plankton_param, environment)
    
    
Plotting
^^^^^^^^

Parallel
^^^^^^^^

Projection
^^^^^^^^^^


 				   
