# This is for final simulation where Class are declared here itself
# There no Glory in Modularity ........

from simul_1 import ParticleSimulator
import dis

dis.dis(ParticleSimulator.evolve)
### --------------------Result Printed Below ----------------------------------------### 

# 20           0 RESUME                   0

#  21           2 LOAD_CONST               1 (0.0001)
#               4 STORE_FAST               2 (timestep)

#  22           6 LOAD_GLOBAL              1 (NULL + int)
#              18 LOAD_FAST                1 (dt)
#              20 LOAD_FAST                2 (timestep)
#              22 BINARY_OP               11 (/)
#              26 PRECALL                  1
#              30 CALL                     1
#              40 STORE_FAST               3 (nsteps)

#  24          42 LOAD_GLOBAL              3 (NULL + range)
#              54 LOAD_FAST                3 (nsteps)
#              56 PRECALL                  1
#              60 CALL                     1
#              70 GET_ITER
#         >>   72 FOR_ITER               115 (to 304)
#              74 STORE_FAST               4 (i)

#  25          76 LOAD_FAST                0 (self)
#              78 LOAD_ATTR                2 (particles)
#              88 GET_ITER
#         >>   90 FOR_ITER               105 (to 302)
#              92 STORE_FAST               5 (p)

#  27          94 LOAD_FAST                5 (p)
#              96 LOAD_ATTR                3 (x)
#             106 LOAD_CONST               2 (2)
#             108 BINARY_OP                8 (**)
#             112 LOAD_FAST                5 (p)
#             114 LOAD_ATTR                4 (y)
#             124 LOAD_CONST               2 (2)
#             126 BINARY_OP                8 (**)
#             130 BINARY_OP                0 (+)
#             134 LOAD_CONST               3 (0.5)
#             136 BINARY_OP                8 (**)
#             140 STORE_FAST               6 (norm)

#  28         142 LOAD_FAST                5 (p)
#             144 LOAD_ATTR                4 (y)
#             154 UNARY_NEGATIVE
#             156 LOAD_FAST                6 (norm)
#             158 BINARY_OP               11 (/)
#             162 STORE_FAST               7 (v_x)

#  29         164 LOAD_FAST                5 (p)
#             166 LOAD_ATTR                3 (x)
#             176 LOAD_FAST                6 (norm)
#             178 BINARY_OP               11 (/)
#             182 STORE_FAST               8 (v_y)

#  31         184 LOAD_FAST                2 (timestep)
#             186 LOAD_FAST                5 (p)
#             188 LOAD_ATTR                5 (ang_vel)
#             198 BINARY_OP                5 (*)
#             202 LOAD_FAST                7 (v_x)
#             204 BINARY_OP                5 (*)
#             208 STORE_FAST               9 (d_x)

#  32         210 LOAD_FAST                2 (timestep)
#             212 LOAD_FAST                5 (p)
#             214 LOAD_ATTR                5 (ang_vel)
#             224 BINARY_OP                5 (*)
#             228 LOAD_FAST                8 (v_y)
#             230 BINARY_OP                5 (*)
#             234 STORE_FAST              10 (d_y)

#  34         236 LOAD_FAST                5 (p)
#             238 COPY                     1
#             240 LOAD_ATTR                3 (x)
#             250 LOAD_FAST                9 (d_x)
#             252 BINARY_OP               13 (+=)
#             256 SWAP                     2
#             258 STORE_ATTR               3 (x)

#  35         268 LOAD_FAST                5 (p)
#             270 COPY                     1
#             272 LOAD_ATTR                4 (y)
#             282 LOAD_FAST               10 (d_y)
#             284 BINARY_OP               13 (+=)
#             288 SWAP                     2
#             290 STORE_ATTR               4 (y)
#             300 JUMP_BACKWARD          106 (to 90)

#  25     >>  302 JUMP_BACKWARD          116 (to 72)

#  24     >>  304 LOAD_CONST               0 (None)
#             306 RETURN_VALUE