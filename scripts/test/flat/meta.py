affine = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
bc1 = (10, 10, 10)
bc2 = (10, 10, 10)
debug = 0
delts = 0.0
dt = 0.008
dtype = '<f4'
dx = (100, 100, 100)
eplasticity = 'elastic'
faultnormal = 3
faultopening = 0
friction = 'slipweakening'
gam1 = -1.0
gam2 = 0.8
gridnoise = 0.0
hourglass = (1.0, 2.0)
i1pml = (10, 10, 10)
i2pml = (26, 26, 13)
ihypo = (18.0, 18.0, 11.5)
itcheck = 0
itio = 50
itstats = 10
itstop = 0
ivols = 'yes'
mpin = 1
mpout = 1
n1expand = (0, 0, 0)
n2expand = (0, 0, 0)
name = 'flat'
nn = (35, 35, 22)
np3 = (1, 1, 1)
npml = 10
nsource = 0
nt = 3126
oplevel = 0
pcdep = 'no'
period = 0.075
ppml = 2
rcrit = 4000
rexpand = 1.06
rho1 = -1.0
rho2 = -1.0
rnucl = 0.0
rundate = 'Tue Feb 17 13:38:53 2015'
rundir = '/Users/yow004/software/SORD/sord/scripts/test/flat'
slipvector = (1.0, 0.0, 0.0)
source = 'potency'
source1 = (0.0, 0.0, 0.0)
source2 = (0.0, 0.0, 0.0)
svtol = 0.001
timefunction = 'none'
tm0 = 0.0
tmnucl = 1.0
trelax = 0.07
user = 'yow004'
vdamp = -1.0
vp1 = -1.0
vp2 = -1.0
vpml = -1.0
vrup = 1732.0
vs1 = -1.0
vs2 = -1.0
shape = {
'n_x': [35, 35],
'n_y': [35, 35],
'n_z': [35, 35],
'slipr_x': [35, 35, 3126],
'slipr_y': [35, 35, 3126],
'slipr_z': [35, 35, 3126],
'trup': [35, 35],
'tsfinal': [35, 35],
'tsoriginal': [35, 35],
'xx': [35, 35, 22],
'yy': [35, 35, 22],
'zz': [35, 35, 22],
}
xi = {
}
indices = {
'n_x': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)],
'n_y': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)],
'n_z': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)],
'slipr_x': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)],
'slipr_y': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)],
'slipr_z': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)],
'trup': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (3126, 3126, 1)],
'tsfinal': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (3126, 3126, 1)],
'tsoriginal': [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 1, 1)],
'xx': [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)],
'yy': [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)],
'zz': [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)],
}
fieldio = [
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 34, 1), (1, 34, 1), (1, 21, 1), (0, 0, 1)], '-', 2670.0, ['rho']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 34, 1), (1, 34, 1), (1, 21, 1), (0, 0, 1)], '-', 6000.0, ['vp']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 34, 1), (1, 34, 1), (1, 21, 1), (0, 0, 1)], '-', 3464.0, ['vs']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], '-', 0.4, ['dc']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], '-', 0.525, ['mud']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], '-', 0.677, ['mus']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 34, 1), (1, 34, 1), (1, 21, 1), (0, 0, 1)], '-', -120000000.0, ['a33']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 34, 1), (1, 34, 1), (1, 21, 1), (0, 0, 1)], '-', 70000000.0, ['a31']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 10, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)], 'slipr_x', 1.0, ['sv1']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 10, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)], 'slipr_y', 1.0, ['sv2']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 10, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 3126, 1)], 'slipr_z', 1.0, ['sv3']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)], 'xx', 1.0, ['x1']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)], 'yy', 1.0, ['x2']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (1, 22, 1), (0, 0, 1)], 'zz', 1.0, ['x3']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], 'n_x', 1.0, ['nhat1']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], 'n_y', 1.0, ['nhat2']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (0, 0, 1)], 'n_z', 1.0, ['nhat3']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (3126, 3126, 1)], 'trup', 1.0, ['trup']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (1, 1, 1)], 'tsoriginal', 1.0, ['ts1']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 35, 1), (1, 35, 1), (11, 11, 1), (3126, 3126, 1)], 'tsfinal', 1.0, ['ts1']),
]
