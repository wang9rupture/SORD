#!/usr/bin/env python
import sord                               # import the sord module
rundir = 'tmp'                            # directory location for output
np3 = 2,1,1
dx = 100.0, 100.0, 100.0                  # spatial step length in x, y, and z
dt = 0.0075                               # time step length
nn = 61, 61, 61                           # number of mesh nodes in x, y, and z
nt = 10
#thickn=nn[2]-5                                   # number of time steps
fieldio = [                               # field variable input and output
    ( '=',  'rho', [], 2670.0 ),          # material density
    ( '=',  'vp',  [], 6000.0 ),          # material P-wave velocity
    ( '=',  'vs',  [], 3464.0 ),          # material S-wave velocity
    ( '=',  'gam', [], 0.3    ),          # material viscosity
    ( '=w', 'v1',  [0,31,0,-1], 'vx' ),   # write X velocity slice output
    ( '=w', 'v2',  [0,31,0,-1], 'vy' ),   # write Y velocity slice output
]                                 
ihypo = 31.0, 31.0, 31.0                  # source location
bc1 = 10,10,0
bc2 = 10,10,10
source = 'potency'                        # source type
source1 = 1e6, 1e6, 1e6                   # source normal components
source2 = 0.0, 0.0, 0.0                   # source shear components
timefunction = 'brune'                    # source time function
period = 6 * dt                           # source dominant period
npml = 20
sord.run( locals() )                      # launch SORD job
