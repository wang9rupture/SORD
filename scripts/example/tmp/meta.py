affine = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
bc1 = (10, 10, 0)
bc2 = (10, 10, 10)
debug = 0
delts = 0.0
dt = 0.0075
dtype = '<f4'
dx = (100.0, 100.0, 100.0)
eplasticity = 'elastic'
faultnormal = 0
faultopening = 0
friction = 'slipweakening'
gam1 = -1.0
gam2 = 0.8
gridnoise = 0.0
hourglass = (1.0, 1.0)
i1pml = (20, 20, 0)
i2pml = (42, 42, 42)
ihypo = (31.0, 31.0, 31.0)
itcheck = 0
itio = 10
itstats = 10
itstop = 0
ivols = 'no'
mpin = 1
mpout = 1
n1expand = (0, 0, 0)
n2expand = (0, 0, 0)
name = 'tmp'
nn = (61, 61, 61)
np3 = (2, 1, 1)
npml = 20
nsource = 0
nt = 10
oplevel = 0
pcdep = 'no'
period = 0.045
ppml = 2
rcrit = 0.0
rexpand = 1.06
rho1 = -1.0
rho2 = -1.0
rnucl = 0.0
rundate = 'Sun Mar  1 16:53:55 2015'
rundir = '/Users/yow004/software/SORD/sord/scripts/example/tmp'
slipvector = (1.0, 0.0, 0.0)
source = 'potency'
source1 = (1000000.0, 1000000.0, 1000000.0)
source2 = (0.0, 0.0, 0.0)
svtol = 0.001
timefunction = 'brune'
tm0 = 0.0
tmnucl = 1.0
trelax = 0.07
user = 'yow004'
vdamp = -1.0
vp1 = -1.0
vp2 = -1.0
vpml = -1.0
vrup = -1.0
vs1 = -1.0
vs2 = -1.0
shape = {
'vx': [61, 61],
'vy': [61, 61],
}
xi = {
}
indices = {
'vx': [(1, 61, 1), (31, 31, 1), (1, 61, 1), (10, 10, 1)],
'vy': [(1, 61, 1), (31, 31, 1), (1, 61, 1), (10, 10, 1)],
}
fieldio = [
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 60, 1), (1, 60, 1), (1, 60, 1), (0, 0, 1)], '-', 2670.0, ['rho']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 60, 1), (1, 60, 1), (1, 60, 1), (0, 0, 1)], '-', 6000.0, ['vp']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 60, 1), (1, 60, 1), (1, 60, 1), (0, 0, 1)], '-', 3464.0, ['vs']),
('=', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 60, 1), (1, 60, 1), (1, 60, 1), (0, 0, 1)], '-', 0.3, ['gam']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 61, 1), (31, 31, 1), (1, 61, 1), (10, 10, 1)], 'vx', 1.0, ['v1']),
('=w', 1, 'const', 1.0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1, [(1, 61, 1), (31, 31, 1), (1, 61, 1), (10, 10, 1)], 'vy', 1.0, ['v2']),
]