#!/usr/bin/env python
import sord,numpy

rundir = 'flat-g'

L = 3400, 3400, 2000
dx = 100, 100, 100
dt = dx[0] / 12500.0                           # time step size
T=20.0
nt=int(T/dt+1.5)
#nt=1
nn = (
    int( L[0] / dx[0] + 1.5 ),
    int( L[1] / dx[1] + 1.5 ),
    int( L[2] / dx[2] + 2.5 ),
)

np3 = 2, 2, 1
#careful about nodes/processor

# Near side boundary conditions:
bc1 = 10, 10, 10

# Far side boundary conditions:
# PML absorbing boundaries for the x, y and z boundaries
bc2 = 10, 10, 10

# Material properties
fieldio = [
   ( '=', 'rho', [],     2670.0  ),        # density
   ( '=', 'vp',  [],     6000.0  ),        # P-wave speed
   ( '=', 'vs',  [],     3464.0  ),        # S-wave speed
]
hourglass = 1.0, 2.0

# Fault parameters
faultnormal = 3                             # fault plane of constant z
ihypo = (nn[0] + 1) / 2, (nn[1] + 1) / 2, nn[2]/2 + 0.5     
print ihypo              # hypocenter indices
npml = 2
#ivols = 'yes'
fieldio += [
#    ('=R', 'x1',[],  'x'),
#    ('=R', 'x2',[],  'y'),
#    ('=R', 'x3',[],  'z'),
    ( '=', 'dc',  [],           0.4   ),    # slip weakening distance
    ( '=', 'mud', [],           0.5 ),    # dynamic friction
    ( '=', 'mus', [],           0.7),
#    ( '=R', 'mus', [],           'mus'),    # static friction - slipping section
    ( '=', 's11',  [],          -120e6 ),    # normal traction
    ( '=', 's22',  [],          -120e6 ),
    ( '=', 's33',  [],          -120e6 ),
    ( '=', 's31',  [],  70e6 ),    # shear traction
]

#nucleation patch
#delts = 1.0
#rnucl = 1500
#tmnucl = -1
vrup=0.1*3464
rcrit=1000
 # Write fault plane output
fieldio += [
    ( '=w', 'su1',  [(),(),(),-1], 'slip_x'  ),
    ( '=w', 'su2',  [(),(),(),-1], 'slip_y'  ),
    ( '=w', 'su3',  [(),(),(),-1], 'slip_z'  ),
    ( '=w', 'sv1',  [], 'slipr_x'  ),
    ( '=w', 'sv2',  [], 'slipr_y'  ),
    ( '=w', 'sv3',  [], 'slipr_z'  ), 
    ( '=w', 'x1',  [], 'xx'  ),
    ( '=w', 'x2',  [], 'yy'  ),
    ( '=w', 'x3',  [], 'zz'  ), # final horizontal slip
#    ( '=w', 'mus', [], 'mustatic'),
    ( '=w', 'nhat1',[], 'n_x'),
    ( '=w', 'nhat2',[], 'n_y'),
    ( '=w', 'nhat3',[], 'n_z'),
    ( '=w', 'trup', [(),(),1,-1], 'trup'),
    ( '=w', 'ts1',  [(),(),1,1], 'tsoriginal'),
    ( '=w', 'ts1',  [(),(),1,-1], 'tsfinal'),
]
    
# Launch SORD code
sord.run( locals() )


