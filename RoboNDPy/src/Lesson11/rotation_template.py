from sympy import symbols, cos, sin, pi, sqrt
from sympy.matrices import Matrix

### Create symbols for joint variables
q1, q2 = symbols('q1:3')

# Create a symbolic matrix representing an intrinsic sequence of rotations 
  # about the Y and then Z axes. Let the rotation about the Y axis be described
  # by q1 and the rotation about Z by q2. 
####### TO DO ########
# Replace R_y and R_z with the appropriate (symbolic) elementary rotation matrices 
  # and then compute YZ_intrinsic. 
#R_x = Matrix([[ 1,              0,        0],
#              [ 0,        cos(q1), -sin(q1)],
#              [ 0,        sin(q1),  cos(q1)]])

R_y = Matrix([[ cos(q1),        0,  sin(q1)],
              [       0,        1,        0],
              [-sin(q1),        0,  cos(q1)]])

R_z = Matrix([[ cos(q2), -sin(q2),        0],
              [ sin(q2),  cos(q2),        0],
              [ 0,              0,        1]])
YZ_intrinsic_sym = R_y*R_z

rtd = 180./pi # radians to degrees
dtr = pi/180. # degrees to radians

####### TO DO ########
# Numerically evaluate YZ_intrinsic assuming:
   # q1 = 45 degrees and q2 = 60 degrees. 
   # NOTE: Trigonometric functions in Python assume the input is in radians!  
print("Rotation about the X-axis by 45-degrees")
print(R_y.evalf(subs={q1: 45*dtr}))
print("Rotation about the y-axis by 45-degrees")
print(R_z.evalf(subs={q2: 60*dtr}))
print("Rotation at last")
print(YZ_intrinsic_sym.evalf(subs={q1: 45*dtr, q2: 60*dtr}))
YZ_intrinsic_num = YZ_intrinsic_sym.evalf(subs={q1: 45*dtr, q2: 60*dtr})

####### TO DO ########
# Numerically evaluate ZY_extrinsic assuming:
   # q1 = 45 degrees and q2 = 60 degrees. 
   # NOTE: Trigonometric functions in Python assume the input is in radians! 
ZY_extrinsic_sym = R_y*R_z

print("Rotation about the X-axis by 45-degrees")
print(R_y.evalf(subs={q1: 45*dtr}))
print("Rotation about the y-axis by 60-degrees")
print(R_z.evalf(subs={q2: 60*dtr}))
print("Rotation at last")
print(ZY_extrinsic_sym.evalf(subs={q1: 45*dtr, q2: 60*dtr}))
ZY_extrinsic_num = ZY_extrinsic_sym.evalf(subs={q1: 45*dtr, q2: 60*dtr})
