Examples
========

Steady state monod
^^^^^^^^^^^^^^^^^^

A steady state monod model can be created like this::

    import planktonpy as pp      
    
    #Define environmental parameters:
    environment = pp.def_steady_env(N=0.5, Si=0.5, PAR=500, K=0.02)  
    
    #Load plankton groups:
    groups = pp.load_groups("dutkiewicz2020")
    
    #Load plankton parameters:
    parameters = pp.load_param("dutkiewicz2020")
    
    #Run model:
    model_output = pp.monod_steady(environment, groups, parameters) 
    
    
    
Variable state monod
^^^^^^^^^^^^^^^^^^^^

A variable monod model can be run like so::

    import planktonpy as pp      
    
    #Define enviromental parameters:
    environment = pp.def_variable_env(N_min = 0, N_max = 5,
    				       Si_min=0, Si_max=3,
    				       PAR_min=1000, PAR_max=7500,
    				       frequency=365, K=0.02)  
    #Load groups
    groups = pp.load_groups("dutkiewicz2020")
    
    #Load parameters:
    parameters = pp.load_param("dutkiewicz2020")
    
    #Run model:
    model_output = pp.monod_variable(environment, groups, parameters) 
    


Custom parameters
^^^^^^^^^^^^^^^^^

Custom parameters can be defined if desired::

    import planktonpy as pp      

    #Define environmental parameters:
    environment = pp.def_steady_env(N=0.5, Si=0.5, PAR=500, K=0.02)  
            
    #Define plankton groups:    
    groups = pp.def_groups(pico = 5, euk=5, diat = 5, 
    					cocco=5, diat=5, zoo=5)
    
    #Load default plankton parameters
    default_param = pp.load_param("dutkiewicz2020")
    
    #Define parameter(s):
    custom_param = pp.def_param(default = default_param,
    				   cocco_defense = 0.2)      				
    #Run model:				   
    model_output = pp.monod_steady(environment, groups, custom_param)   

    
        
Plotting
^^^^^^^^

Parallel
^^^^^^^^

Projection
^^^^^^^^^^


 				   
