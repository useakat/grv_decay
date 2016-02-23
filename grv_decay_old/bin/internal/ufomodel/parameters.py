# This file was automatically created by FeynRules 1.7.160
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Apr 2013 13:43:12



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
RRd1x1 = Parameter(name = 'RRd1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd1x1}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 1, 1 ])

RRd2x2 = Parameter(name = 'RRd2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd2x2}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 2, 2 ])

RRd3x3 = Parameter(name = 'RRd3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.486508213,
                   texname = '\\text{RRd3x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 3, 3 ])

RRd3x6 = Parameter(name = 'RRd3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.873676003,
                   texname = '\\text{RRd3x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 3, 6 ])

RRd4x4 = Parameter(name = 'RRd4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd4x4}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 4, 4 ])

RRd5x5 = Parameter(name = 'RRd5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd5x5}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 5, 5 ])

RRd6x3 = Parameter(name = 'RRd6x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.873676003,
                   texname = '\\text{RRd6x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 6, 3 ])

RRd6x6 = Parameter(name = 'RRd6x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.486508213,
                   texname = '\\text{RRd6x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 6, 6 ])

alp = Parameter(name = 'alp',
                nature = 'external',
                type = 'real',
                value = -0.0741746992,
                texname = '\\alpha',
                lhablock = 'FRALPHA',
                lhacode = [ 1 ])

RMUH = Parameter(name = 'RMUH',
                 nature = 'external',
                 type = 'real',
                 value = 421.979267,
                 texname = '\\text{RMUH}',
                 lhablock = 'HMIX',
                 lhacode = [ 1 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 14.4876879,
               texname = 't_b',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MA2 = Parameter(name = 'MA2',
                nature = 'external',
                type = 'real',
                value = 312178.137,
                texname = 'm_A^2',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

RmD21x1 = Parameter(name = 'RmD21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.08445579e6,
                    texname = '\\text{RmD21x1}',
                    lhablock = 'MSD2',
                    lhacode = [ 1, 1 ])

RmD22x2 = Parameter(name = 'RmD22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.08445062e6,
                    texname = '\\text{RmD22x2}',
                    lhablock = 'MSD2',
                    lhacode = [ 2, 2 ])

RmD23x3 = Parameter(name = 'RmD23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.07444332e6,
                    texname = '\\text{RmD23x3}',
                    lhablock = 'MSD2',
                    lhacode = [ 3, 3 ])

RmE21x1 = Parameter(name = 'RmE21x1',
                    nature = 'external',
                    type = 'real',
                    value = 29006.552,
                    texname = '\\text{RmE21x1}',
                    lhablock = 'MSE2',
                    lhacode = [ 1, 1 ])

RmE22x2 = Parameter(name = 'RmE22x2',
                    nature = 'external',
                    type = 'real',
                    value = 29004.0134,
                    texname = '\\text{RmE22x2}',
                    lhablock = 'MSE2',
                    lhacode = [ 2, 2 ])

RmE23x3 = Parameter(name = 'RmE23x3',
                    nature = 'external',
                    type = 'real',
                    value = 28231.2776,
                    texname = '\\text{RmE23x3}',
                    lhablock = 'MSE2',
                    lhacode = [ 3, 3 ])

RmL21x1 = Parameter(name = 'RmL21x1',
                    nature = 'external',
                    type = 'real',
                    value = 124601.846,
                    texname = '\\text{RmL21x1}',
                    lhablock = 'MSL2',
                    lhacode = [ 1, 1 ])

RmL22x2 = Parameter(name = 'RmL22x2',
                    nature = 'external',
                    type = 'real',
                    value = 124600.587,
                    texname = '\\text{RmL22x2}',
                    lhablock = 'MSL2',
                    lhacode = [ 2, 2 ])

RmL23x3 = Parameter(name = 'RmL23x3',
                    nature = 'external',
                    type = 'real',
                    value = 124217.434,
                    texname = '\\text{RmL23x3}',
                    lhablock = 'MSL2',
                    lhacode = [ 3, 3 ])

RMx1 = Parameter(name = 'RMx1',
                 nature = 'external',
                 type = 'real',
                 value = 144.408964,
                 texname = '\\text{RMx1}',
                 lhablock = 'MSOFT',
                 lhacode = [ 1 ])

RMx2 = Parameter(name = 'RMx2',
                 nature = 'external',
                 type = 'real',
                 value = 272.090564,
                 texname = '\\text{RMx2}',
                 lhablock = 'MSOFT',
                 lhacode = [ 2 ])

RMx3 = Parameter(name = 'RMx3',
                 nature = 'external',
                 type = 'real',
                 value = 744.35661,
                 texname = '\\text{RMx3}',
                 lhablock = 'MSOFT',
                 lhacode = [ 3 ])

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = 108528.532,
                 texname = 'm_{H_d}^2',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = -158605.691,
                 texname = 'm_{H_u}^2',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ21x1 = Parameter(name = 'RmQ21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.19708078e6,
                    texname = '\\text{RmQ21x1}',
                    lhablock = 'MSQ2',
                    lhacode = [ 1, 1 ])

RmQ22x2 = Parameter(name = 'RmQ22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.19707689e6,
                    texname = '\\text{RmQ22x2}',
                    lhablock = 'MSQ2',
                    lhacode = [ 2, 2 ])

RmQ23x3 = Parameter(name = 'RmQ23x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.10424867e6,
                    texname = '\\text{RmQ23x3}',
                    lhablock = 'MSQ2',
                    lhacode = [ 3, 3 ])

RmU21x1 = Parameter(name = 'RmU21x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.0943808e6,
                    texname = '\\text{RmU21x1}',
                    lhablock = 'MSU2',
                    lhacode = [ 1, 1 ])

RmU22x2 = Parameter(name = 'RmU22x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.09437814e6,
                    texname = '\\text{RmU22x2}',
                    lhablock = 'MSU2',
                    lhacode = [ 2, 2 ])

RmU23x3 = Parameter(name = 'RmU23x3',
                    nature = 'external',
                    type = 'real',
                    value = 915823.36,
                    texname = '\\text{RmU23x3}',
                    lhablock = 'MSU2',
                    lhacode = [ 3, 3 ])

RNN1x1 = Parameter(name = 'RNN1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.990612708,
                   texname = '\\text{RNN1x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 1 ])

RNN1x2 = Parameter(name = 'RNN1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.0311086091,
                   texname = '\\text{RNN1x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 2 ])

RNN1x3 = Parameter(name = 'RNN1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.124078997,
                   texname = '\\text{RNN1x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 3 ])

RNN1x4 = Parameter(name = 'RNN1x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.0481987613,
                   texname = '\\text{RNN1x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 4 ])

RNN2x1 = Parameter(name = 'RNN2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.0736604963,
                   texname = '\\text{RNN2x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 1 ])

RNN2x2 = Parameter(name = 'RNN2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.938902386,
                   texname = '\\text{RNN2x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 2 ])

RNN2x3 = Parameter(name = 'RNN2x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.280952912,
                   texname = '\\text{RNN2x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 3 ])

RNN2x4 = Parameter(name = 'RNN2x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.184667003,
                   texname = '\\text{RNN2x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 4 ])

RNN3x1 = Parameter(name = 'RNN3x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.0507574728,
                   texname = '\\text{RNN3x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 1 ])

RNN3x2 = Parameter(name = 'RNN3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.0737154491,
                   texname = '\\text{RNN3x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 2 ])

RNN3x3 = Parameter(name = 'RNN3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.699232734,
                   texname = '\\text{RNN3x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 3 ])

RNN3x4 = Parameter(name = 'RNN3x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.709269551,
                   texname = '\\text{RNN3x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 4 ])

RNN4x1 = Parameter(name = 'RNN4x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.103364762,
                   texname = '\\text{RNN4x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 1 ])

RNN4x2 = Parameter(name = 'RNN4x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.334754532,
                   texname = '\\text{RNN4x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 2 ])

RNN4x3 = Parameter(name = 'RNN4x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.645556696,
                   texname = '\\text{RNN4x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 3 ])

RNN4x4 = Parameter(name = 'RNN4x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.67861011,
                   texname = '\\text{RNN4x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 4 ])

RRl1x1 = Parameter(name = 'RRl1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl1x1}',
                   lhablock = 'SELMIX',
                   lhacode = [ 1, 1 ])

RRl2x2 = Parameter(name = 'RRl2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl2x2}',
                   lhablock = 'SELMIX',
                   lhacode = [ 2, 2 ])

RRl3x3 = Parameter(name = 'RRl3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1137153,
                   texname = '\\text{RRl3x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 3, 3 ])

RRl3x6 = Parameter(name = 'RRl3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.993513377,
                   texname = '\\text{RRl3x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 3, 6 ])

RRl4x4 = Parameter(name = 'RRl4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl4x4}',
                   lhablock = 'SELMIX',
                   lhacode = [ 4, 4 ])

RRl5x5 = Parameter(name = 'RRl5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl5x5}',
                   lhablock = 'SELMIX',
                   lhacode = [ 5, 5 ])

RRl6x3 = Parameter(name = 'RRl6x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.993513377,
                   texname = '\\text{RRl6x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 3 ])

RRl6x6 = Parameter(name = 'RRl6x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.1137153,
                   texname = '\\text{RRl6x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.934,
                  texname = '\\alpha _w^{-1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1172,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

MP = Parameter(name = 'MP',
               nature = 'external',
               type = 'real',
               value = 2.435323203596526e18,
               texname = 'M_P',
               lhablock = 'SMINPUTS',
               lhacode = [ 10 ])

M32 = Parameter(name = 'M32',
                nature = 'external',
                type = 'real',
                value = 1.e-13,
                texname = 'M_{\\frac{3}{2}}',
                lhablock = 'SMINPUTS',
                lhacode = [ 11 ])

RRn1x1 = Parameter(name = 'RRn1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn1x1}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 1, 1 ])

RRn2x2 = Parameter(name = 'RRn2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn2x2}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 2, 2 ])

RRn3x3 = Parameter(name = 'RRn3x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn3x3}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 3, 3 ])

Rtd3x3 = Parameter(name = 'Rtd3x3',
                   nature = 'external',
                   type = 'real',
                   value = -53.6703421,
                   texname = '\\text{Rtd3x3}',
                   lhablock = 'TD',
                   lhacode = [ 3, 3 ])

Rte3x3 = Parameter(name = 'Rte3x3',
                   nature = 'external',
                   type = 'real',
                   value = -3.97043409,
                   texname = '\\text{Rte3x3}',
                   lhablock = 'TE',
                   lhacode = [ 3, 3 ])

Rtu3x3 = Parameter(name = 'Rtu3x3',
                   nature = 'external',
                   type = 'real',
                   value = -204.889532,
                   texname = '\\text{Rtu3x3}',
                   lhablock = 'TU',
                   lhacode = [ 3, 3 ])

RUU1x1 = Parameter(name = 'RUU1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.916581757,
                   texname = '\\text{RUU1x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 1 ])

RUU1x2 = Parameter(name = 'RUU1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.399847324,
                   texname = '\\text{RUU1x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 2 ])

RUU2x1 = Parameter(name = 'RUU2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.399847324,
                   texname = '\\text{RUU2x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 1 ])

RUU2x2 = Parameter(name = 'RUU2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.916581757,
                   texname = '\\text{RUU2x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 2 ])

RMNS1x1 = Parameter(name = 'RMNS1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS1x1}',
                    lhablock = 'UPMNS',
                    lhacode = [ 1, 1 ])

RMNS2x2 = Parameter(name = 'RMNS2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS2x2}',
                    lhablock = 'UPMNS',
                    lhacode = [ 2, 2 ])

RMNS3x3 = Parameter(name = 'RMNS3x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS3x3}',
                    lhablock = 'UPMNS',
                    lhacode = [ 3, 3 ])

RRu1x1 = Parameter(name = 'RRu1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu1x1}',
                   lhablock = 'USQMIX',
                   lhacode = [ 1, 1 ])

RRu2x2 = Parameter(name = 'RRu2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu2x2}',
                   lhablock = 'USQMIX',
                   lhacode = [ 2, 2 ])

RRu3x3 = Parameter(name = 'RRu3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.240566882,
                   texname = '\\text{RRu3x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 3, 3 ])

RRu3x6 = Parameter(name = 'RRu3x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.970632564,
                   texname = '\\text{RRu3x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 3, 6 ])

RRu4x4 = Parameter(name = 'RRu4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu4x4}',
                   lhablock = 'USQMIX',
                   lhacode = [ 4, 4 ])

RRu5x5 = Parameter(name = 'RRu5x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu5x5}',
                   lhablock = 'USQMIX',
                   lhacode = [ 5, 5 ])

RRu6x3 = Parameter(name = 'RRu6x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.970632564,
                   texname = '\\text{RRu6x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 6, 3 ])

RRu6x6 = Parameter(name = 'RRu6x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.240566882,
                   texname = '\\text{RRu6x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 6, 6 ])

RCKM1x1 = Parameter(name = 'RCKM1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM1x1}',
                    lhablock = 'VCKM',
                    lhacode = [ 1, 1 ])

RCKM2x2 = Parameter(name = 'RCKM2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM2x2}',
                    lhablock = 'VCKM',
                    lhacode = [ 2, 2 ])

RCKM3x3 = Parameter(name = 'RCKM3x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RCKM3x3}',
                    lhablock = 'VCKM',
                    lhacode = [ 3, 3 ])

RVV1x1 = Parameter(name = 'RVV1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.963915835,
                   texname = '\\text{RVV1x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 1 ])

RVV1x2 = Parameter(name = 'RVV1x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.266207182,
                   texname = '\\text{RVV1x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 2 ])

RVV2x1 = Parameter(name = 'RVV2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.266207182,
                   texname = '\\text{RVV2x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 1 ])

RVV2x2 = Parameter(name = 'RVV2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.963915835,
                   texname = '\\text{RVV2x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 2 ])

Ryd3x3 = Parameter(name = 'Ryd3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.203348501,
                   texname = '\\text{Ryd3x3}',
                   lhablock = 'YD',
                   lhacode = [ 3, 3 ])

Rye3x3 = Parameter(name = 'Rye3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.151067903,
                   texname = '\\text{Rye3x3}',
                   lhablock = 'YE',
                   lhacode = [ 3, 3 ])

Ryu3x3 = Parameter(name = 'Ryu3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.87019871,
                   texname = '\\text{Ryu3x3}',
                   lhablock = 'YU',
                   lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.4079107,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 139.236428,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 264.618388,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = -430.561525,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 450.179622,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 264.718379,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 449.560218,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 834.577372,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MH01 = Parameter(name = 'MH01',
                 nature = 'external',
                 type = 'real',
                 value = 113.50612,
                 texname = '\\text{MH01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

MH02 = Parameter(name = 'MH02',
                 nature = 'external',
                 type = 'real',
                 value = 535.787591,
                 texname = '\\text{MH02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 535.504243,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 541.914915,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 37 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 174.3,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 5.61337101,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Msn1 = Parameter(name = 'Msn1',
                 nature = 'external',
                 type = 'real',
                 value = 349.048271,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 349.048271,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 348.284449,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 358.229154,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 358.229154,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 173.805339,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 180.171945,
                 texname = '\\text{Msl4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

Msl5 = Parameter(name = 'Msl5',
                 nature = 'external',
                 type = 'real',
                 value = 180.171945,
                 texname = '\\text{Msl5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000013 ])

Msl6 = Parameter(name = 'Msl6',
                 nature = 'external',
                 type = 'real',
                 value = 359.295621,
                 texname = '\\text{Msl6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000015 ])

Msu1 = Parameter(name = 'Msu1',
                 nature = 'external',
                 type = 'real',
                 value = 1117.57569,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 1117.57569,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 975.622369,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 1069.75128,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 1069.75128,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 1084.45435,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 1120.2291,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 1120.2291,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 1056.74315,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 1066.30946,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 1066.30946,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 1074.57127,
                 texname = '\\text{Msd6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

Mgld = Parameter(name = 'Mgld',
                 nature = 'external',
                 type = 'real',
                 value = 1.e-13,
                 texname = '\\text{Mgld}',
                 lhablock = 'MASS',
                 lhacode = [ 1000039 ])

Mgrv = Parameter(name = 'Mgrv',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{Mgrv}',
                 lhablock = 'MASS',
                 lhacode = [ 1000049 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.41143316,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.00282196,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wneu1 = Parameter(name = 'Wneu1',
                  nature = 'external',
                  type = 'real',
                  value = 2.00347693e-12,
                  texname = '\\text{Wneu1}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000022 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 0.0328974531,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 1.81691697,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 2.31444629,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 0.0268917113,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 2.10289779,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 0.0166384299,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WH01 = Parameter(name = 'WH01',
                 nature = 'external',
                 type = 'real',
                 value = 0.00359453009,
                 texname = '\\text{WH01}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

WH02 = Parameter(name = 'WH02',
                 nature = 'external',
                 type = 'real',
                 value = 2.02404488,
                 texname = '\\text{WH02}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 2.27784733,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 1.89694764,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 37 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.49575771,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsn1 = Parameter(name = 'Wsn1',
                 nature = 'external',
                 type = 'real',
                 value = 1.04817117,
                 texname = '\\text{Wsn1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsn2 = Parameter(name = 'Wsn2',
                 nature = 'external',
                 type = 'real',
                 value = 1.04817117,
                 texname = '\\text{Wsn2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsn3 = Parameter(name = 'Wsn3',
                 nature = 'external',
                 type = 'real',
                 value = 1.13951321,
                 texname = '\\text{Wsn3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

Wsl1 = Parameter(name = 'Wsl1',
                 nature = 'external',
                 type = 'real',
                 value = 1.10284098,
                 texname = '\\text{Wsl1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

Wsl2 = Parameter(name = 'Wsl2',
                 nature = 'external',
                 type = 'real',
                 value = 1.10284098,
                 texname = '\\text{Wsl2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000013 ])

Wsl3 = Parameter(name = 'Wsl3',
                 nature = 'external',
                 type = 'real',
                 value = 0.114292019,
                 texname = '\\text{Wsl3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000015 ])

Wsl4 = Parameter(name = 'Wsl4',
                 nature = 'external',
                 type = 'real',
                 value = 0.150438638,
                 texname = '\\text{Wsl4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

Wsl5 = Parameter(name = 'Wsl5',
                 nature = 'external',
                 type = 'real',
                 value = 0.150438638,
                 texname = '\\text{Wsl5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000013 ])

Wsl6 = Parameter(name = 'Wsl6',
                 nature = 'external',
                 type = 'real',
                 value = 1.21851696,
                 texname = '\\text{Wsl6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000015 ])

Wsu1 = Parameter(name = 'Wsu1',
                 nature = 'external',
                 type = 'real',
                 value = 19.6057435,
                 texname = '\\text{Wsu1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

Wsu2 = Parameter(name = 'Wsu2',
                 nature = 'external',
                 type = 'real',
                 value = 19.6057435,
                 texname = '\\text{Wsu2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

Wsu3 = Parameter(name = 'Wsu3',
                 nature = 'external',
                 type = 'real',
                 value = 9.66336473,
                 texname = '\\text{Wsu3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

Wsu4 = Parameter(name = 'Wsu4',
                 nature = 'external',
                 type = 'real',
                 value = 8.06323304,
                 texname = '\\text{Wsu4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

Wsu5 = Parameter(name = 'Wsu5',
                 nature = 'external',
                 type = 'real',
                 value = 8.06323304,
                 texname = '\\text{Wsu5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

Wsu6 = Parameter(name = 'Wsu6',
                 nature = 'external',
                 type = 'real',
                 value = 22.4653276,
                 texname = '\\text{Wsu6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

Wsd1 = Parameter(name = 'Wsd1',
                 nature = 'external',
                 type = 'real',
                 value = 19.6001241,
                 texname = '\\text{Wsd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

Wsd2 = Parameter(name = 'Wsd2',
                 nature = 'external',
                 type = 'real',
                 value = 19.6001241,
                 texname = '\\text{Wsd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

Wsd3 = Parameter(name = 'Wsd3',
                 nature = 'external',
                 type = 'real',
                 value = 8.61637979,
                 texname = '\\text{Wsd3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

Wsd4 = Parameter(name = 'Wsd4',
                 nature = 'external',
                 type = 'real',
                 value = 6.20756473,
                 texname = '\\text{Wsd4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

Wsd5 = Parameter(name = 'Wsd5',
                 nature = 'external',
                 type = 'real',
                 value = 6.20756473,
                 texname = '\\text{Wsd5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

Wsd6 = Parameter(name = 'Wsd6',
                 nature = 'external',
                 type = 'real',
                 value = 19.9595789,
                 texname = '\\text{Wsd6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

Wgrv = Parameter(name = 'Wgrv',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{Wgrv}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000049 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM1x1',
                   texname = '\\text{CKM1x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM2x2',
                   texname = '\\text{CKM2x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RCKM3x3',
                   texname = '\\text{CKM3x3}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

mD21x1 = Parameter(name = 'mD21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD21x1',
                   texname = '\\text{mD21x1}')

mD22x2 = Parameter(name = 'mD22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD22x2',
                   texname = '\\text{mD22x2}')

mD23x3 = Parameter(name = 'mD23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD23x3',
                   texname = '\\text{mD23x3}')

mE21x1 = Parameter(name = 'mE21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE21x1',
                   texname = '\\text{mE21x1}')

mE22x2 = Parameter(name = 'mE22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE22x2',
                   texname = '\\text{mE22x2}')

mE23x3 = Parameter(name = 'mE23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE23x3',
                   texname = '\\text{mE23x3}')

mL21x1 = Parameter(name = 'mL21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL21x1',
                   texname = '\\text{mL21x1}')

mL22x2 = Parameter(name = 'mL22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL22x2',
                   texname = '\\text{mL22x2}')

mL23x3 = Parameter(name = 'mL23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL23x3',
                   texname = '\\text{mL23x3}')

mQ21x1 = Parameter(name = 'mQ21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ21x1',
                   texname = '\\text{mQ21x1}')

mQ22x2 = Parameter(name = 'mQ22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ22x2',
                   texname = '\\text{mQ22x2}')

mQ23x3 = Parameter(name = 'mQ23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ23x3',
                   texname = '\\text{mQ23x3}')

mU21x1 = Parameter(name = 'mU21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU21x1',
                   texname = '\\text{mU21x1}')

mU22x2 = Parameter(name = 'mU22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU22x2',
                   texname = '\\text{mU22x2}')

mU23x3 = Parameter(name = 'mU23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU23x3',
                   texname = '\\text{mU23x3}')

MUH = Parameter(name = 'MUH',
                nature = 'internal',
                type = 'complex',
                value = 'RMUH',
                texname = '\\mu')

Mx1 = Parameter(name = 'Mx1',
                nature = 'internal',
                type = 'complex',
                value = 'RMx1',
                texname = 'M_1')

Mx2 = Parameter(name = 'Mx2',
                nature = 'internal',
                type = 'complex',
                value = 'RMx2',
                texname = 'M_2')

Mx3 = Parameter(name = 'Mx3',
                nature = 'internal',
                type = 'complex',
                value = 'RMx3',
                texname = 'M_3')

NN1x1 = Parameter(name = 'NN1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x1',
                  texname = '\\text{NN1x1}')

NN1x2 = Parameter(name = 'NN1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x2',
                  texname = '\\text{NN1x2}')

NN1x3 = Parameter(name = 'NN1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x3',
                  texname = '\\text{NN1x3}')

NN1x4 = Parameter(name = 'NN1x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x4',
                  texname = '\\text{NN1x4}')

NN2x1 = Parameter(name = 'NN2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x1',
                  texname = '\\text{NN2x1}')

NN2x2 = Parameter(name = 'NN2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x2',
                  texname = '\\text{NN2x2}')

NN2x3 = Parameter(name = 'NN2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x3',
                  texname = '\\text{NN2x3}')

NN2x4 = Parameter(name = 'NN2x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x4',
                  texname = '\\text{NN2x4}')

NN3x1 = Parameter(name = 'NN3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x1',
                  texname = '\\text{NN3x1}')

NN3x2 = Parameter(name = 'NN3x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x2',
                  texname = '\\text{NN3x2}')

NN3x3 = Parameter(name = 'NN3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x3',
                  texname = '\\text{NN3x3}')

NN3x4 = Parameter(name = 'NN3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x4',
                  texname = '\\text{NN3x4}')

NN4x1 = Parameter(name = 'NN4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x1',
                  texname = '\\text{NN4x1}')

NN4x2 = Parameter(name = 'NN4x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x2',
                  texname = '\\text{NN4x2}')

NN4x3 = Parameter(name = 'NN4x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x3',
                  texname = '\\text{NN4x3}')

NN4x4 = Parameter(name = 'NN4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x4',
                  texname = '\\text{NN4x4}')

Rd1x1 = Parameter(name = 'Rd1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd1x1',
                  texname = '\\text{Rd1x1}')

Rd2x2 = Parameter(name = 'Rd2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd2x2',
                  texname = '\\text{Rd2x2}')

Rd3x3 = Parameter(name = 'Rd3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd3x3',
                  texname = '\\text{Rd3x3}')

Rd3x6 = Parameter(name = 'Rd3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd3x6',
                  texname = '\\text{Rd3x6}')

Rd4x4 = Parameter(name = 'Rd4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd4x4',
                  texname = '\\text{Rd4x4}')

Rd5x5 = Parameter(name = 'Rd5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd5x5',
                  texname = '\\text{Rd5x5}')

Rd6x3 = Parameter(name = 'Rd6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd6x3',
                  texname = '\\text{Rd6x3}')

Rd6x6 = Parameter(name = 'Rd6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd6x6',
                  texname = '\\text{Rd6x6}')

Rl1x1 = Parameter(name = 'Rl1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl1x1',
                  texname = '\\text{Rl1x1}')

Rl2x2 = Parameter(name = 'Rl2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl2x2',
                  texname = '\\text{Rl2x2}')

Rl3x3 = Parameter(name = 'Rl3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl3x3',
                  texname = '\\text{Rl3x3}')

Rl3x6 = Parameter(name = 'Rl3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl3x6',
                  texname = '\\text{Rl3x6}')

Rl4x4 = Parameter(name = 'Rl4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl4x4',
                  texname = '\\text{Rl4x4}')

Rl5x5 = Parameter(name = 'Rl5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl5x5',
                  texname = '\\text{Rl5x5}')

Rl6x3 = Parameter(name = 'Rl6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x3',
                  texname = '\\text{Rl6x3}')

Rl6x6 = Parameter(name = 'Rl6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x6',
                  texname = '\\text{Rl6x6}')

Rn1x1 = Parameter(name = 'Rn1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn1x1',
                  texname = '\\text{Rn1x1}')

Rn2x2 = Parameter(name = 'Rn2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn2x2',
                  texname = '\\text{Rn2x2}')

Rn3x3 = Parameter(name = 'Rn3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn3x3',
                  texname = '\\text{Rn3x3}')

Ru1x1 = Parameter(name = 'Ru1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu1x1',
                  texname = '\\text{Ru1x1}')

Ru2x2 = Parameter(name = 'Ru2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu2x2',
                  texname = '\\text{Ru2x2}')

Ru3x3 = Parameter(name = 'Ru3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu3x3',
                  texname = '\\text{Ru3x3}')

Ru3x6 = Parameter(name = 'Ru3x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu3x6',
                  texname = '\\text{Ru3x6}')

Ru4x4 = Parameter(name = 'Ru4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu4x4',
                  texname = '\\text{Ru4x4}')

Ru5x5 = Parameter(name = 'Ru5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu5x5',
                  texname = '\\text{Ru5x5}')

Ru6x3 = Parameter(name = 'Ru6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu6x3',
                  texname = '\\text{Ru6x3}')

Ru6x6 = Parameter(name = 'Ru6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu6x6',
                  texname = '\\text{Ru6x6}')

UU1x1 = Parameter(name = 'UU1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x1',
                  texname = '\\text{UU1x1}')

UU1x2 = Parameter(name = 'UU1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x2',
                  texname = '\\text{UU1x2}')

UU2x1 = Parameter(name = 'UU2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x1',
                  texname = '\\text{UU2x1}')

UU2x2 = Parameter(name = 'UU2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x2',
                  texname = '\\text{UU2x2}')

VV1x1 = Parameter(name = 'VV1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x1',
                  texname = '\\text{VV1x1}')

VV1x2 = Parameter(name = 'VV1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x2',
                  texname = '\\text{VV1x2}')

VV2x1 = Parameter(name = 'VV2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x1',
                  texname = '\\text{VV2x1}')

VV2x2 = Parameter(name = 'VV2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x2',
                  texname = '\\text{VV2x2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

td3x3 = Parameter(name = 'td3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtd3x3',
                  texname = '\\text{td3x3}')

te3x3 = Parameter(name = 'te3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rte3x3',
                  texname = '\\text{te3x3}')

tu3x3 = Parameter(name = 'tu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtu3x3',
                  texname = '\\text{tu3x3}')

yd3x3 = Parameter(name = 'yd3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryd3x3',
                  texname = '\\text{yd3x3}')

ye3x3 = Parameter(name = 'ye3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rye3x3',
                  texname = '\\text{ye3x3}')

yu3x3 = Parameter(name = 'yu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryu3x3',
                  texname = '\\text{yu3x3}')

bb = Parameter(name = 'bb',
               nature = 'internal',
               type = 'complex',
               value = '((-mHd2 + mHu2)*cmath.tan(2*alp))/2. - MZ**2*(cmath.sin(2*beta)/2. + cmath.cos(2*beta)*cmath.tan(2*alp))',
               texname = 'b')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

I1x11 = Parameter(name = 'I1x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru1x1*complexconjugate(Ru1x1)',
                  texname = '\\text{I1x11}')

I1x22 = Parameter(name = 'I1x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru2x2*complexconjugate(Ru2x2)',
                  texname = '\\text{I1x22}')

I1x33 = Parameter(name = 'I1x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru3x3*complexconjugate(Ru3x3)',
                  texname = '\\text{I1x33}')

I1x36 = Parameter(name = 'I1x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru6x3*complexconjugate(Ru3x3)',
                  texname = '\\text{I1x36}')

I1x63 = Parameter(name = 'I1x63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru3x3*complexconjugate(Ru6x3)',
                  texname = '\\text{I1x63}')

I1x66 = Parameter(name = 'I1x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ru6x3*complexconjugate(Ru6x3)',
                  texname = '\\text{I1x66}')

I10x33 = Parameter(name = 'I10x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(ye3x3)',
                   texname = '\\text{I10x33}')

I100x33 = Parameter(name = 'I100x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(ye3x3)',
                    texname = '\\text{I100x33}')

I101x11 = Parameter(name = 'I101x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x1*complexconjugate(Rl1x1)',
                    texname = '\\text{I101x11}')

I101x22 = Parameter(name = 'I101x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(Rl2x2)',
                    texname = '\\text{I101x22}')

I101x33 = Parameter(name = 'I101x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I101x33}')

I101x36 = Parameter(name = 'I101x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I101x36}')

I102x33 = Parameter(name = 'I102x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I102x33}')

I102x36 = Parameter(name = 'I102x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I102x36}')

I103x33 = Parameter(name = 'I103x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                    texname = '\\text{I103x33}')

I103x36 = Parameter(name = 'I103x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                    texname = '\\text{I103x36}')

I104x33 = Parameter(name = 'I104x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I104x33}')

I104x36 = Parameter(name = 'I104x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I104x36}')

I105x11 = Parameter(name = 'I105x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I105x11}')

I105x22 = Parameter(name = 'I105x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I105x22}')

I105x33 = Parameter(name = 'I105x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I105x33}')

I105x36 = Parameter(name = 'I105x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I105x36}')

I105x63 = Parameter(name = 'I105x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I105x63}')

I105x66 = Parameter(name = 'I105x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I105x66}')

I106x33 = Parameter(name = 'I106x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I106x33}')

I106x36 = Parameter(name = 'I106x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I106x36}')

I106x63 = Parameter(name = 'I106x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I106x63}')

I106x66 = Parameter(name = 'I106x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I106x66}')

I107x33 = Parameter(name = 'I107x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I107x33}')

I107x36 = Parameter(name = 'I107x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I107x36}')

I107x63 = Parameter(name = 'I107x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I107x63}')

I107x66 = Parameter(name = 'I107x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I107x66}')

I108x11 = Parameter(name = 'I108x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x1*complexconjugate(Ru1x1)',
                    texname = '\\text{I108x11}')

I108x22 = Parameter(name = 'I108x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x2*complexconjugate(Ru2x2)',
                    texname = '\\text{I108x22}')

I108x33 = Parameter(name = 'I108x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I108x33}')

I108x36 = Parameter(name = 'I108x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I108x36}')

I108x63 = Parameter(name = 'I108x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I108x63}')

I108x66 = Parameter(name = 'I108x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I108x66}')

I109x33 = Parameter(name = 'I109x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I109x33}')

I109x36 = Parameter(name = 'I109x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I109x36}')

I109x44 = Parameter(name = 'I109x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*complexconjugate(Ru4x4)',
                    texname = '\\text{I109x44}')

I109x55 = Parameter(name = 'I109x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x5*complexconjugate(Ru5x5)',
                    texname = '\\text{I109x55}')

I109x63 = Parameter(name = 'I109x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I109x63}')

I109x66 = Parameter(name = 'I109x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I109x66}')

I11x33 = Parameter(name = 'I11x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I11x33}')

I11x36 = Parameter(name = 'I11x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I11x36}')

I110x11 = Parameter(name = 'I110x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I110x11}')

I110x22 = Parameter(name = 'I110x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I110x22}')

I110x33 = Parameter(name = 'I110x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I110x33}')

I110x36 = Parameter(name = 'I110x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I110x36}')

I110x63 = Parameter(name = 'I110x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I110x63}')

I110x66 = Parameter(name = 'I110x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I110x66}')

I111x33 = Parameter(name = 'I111x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I111x33}')

I111x36 = Parameter(name = 'I111x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I111x36}')

I111x63 = Parameter(name = 'I111x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I111x63}')

I111x66 = Parameter(name = 'I111x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I111x66}')

I112x33 = Parameter(name = 'I112x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I112x33}')

I112x36 = Parameter(name = 'I112x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I112x36}')

I112x63 = Parameter(name = 'I112x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I112x63}')

I112x66 = Parameter(name = 'I112x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I112x66}')

I113x33 = Parameter(name = 'I113x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I113x33}')

I113x36 = Parameter(name = 'I113x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I113x36}')

I113x63 = Parameter(name = 'I113x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I113x63}')

I113x66 = Parameter(name = 'I113x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*td3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I113x66}')

I114x33 = Parameter(name = 'I114x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I114x33}')

I114x36 = Parameter(name = 'I114x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I114x36}')

I114x63 = Parameter(name = 'I114x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I114x63}')

I114x66 = Parameter(name = 'I114x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I114x66}')

I115x33 = Parameter(name = 'I115x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I115x33}')

I115x36 = Parameter(name = 'I115x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I115x36}')

I115x63 = Parameter(name = 'I115x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I115x63}')

I115x66 = Parameter(name = 'I115x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I115x66}')

I116x33 = Parameter(name = 'I116x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I116x33}')

I116x36 = Parameter(name = 'I116x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I116x36}')

I116x63 = Parameter(name = 'I116x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I116x63}')

I116x66 = Parameter(name = 'I116x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I116x66}')

I117x33 = Parameter(name = 'I117x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I117x33}')

I117x36 = Parameter(name = 'I117x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I117x36}')

I117x63 = Parameter(name = 'I117x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I117x63}')

I117x66 = Parameter(name = 'I117x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*yu3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I117x66}')

I118x11 = Parameter(name = 'I118x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM1x1*Ru1x1',
                    texname = '\\text{I118x11}')

I118x22 = Parameter(name = 'I118x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM2x2*Ru2x2',
                    texname = '\\text{I118x22}')

I118x33 = Parameter(name = 'I118x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3',
                    texname = '\\text{I118x33}')

I118x36 = Parameter(name = 'I118x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3',
                    texname = '\\text{I118x36}')

I119x33 = Parameter(name = 'I119x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(yd3x3)',
                    texname = '\\text{I119x33}')

I119x36 = Parameter(name = 'I119x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(yd3x3)',
                    texname = '\\text{I119x36}')

I12x33 = Parameter(name = 'I12x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3',
                   texname = '\\text{I12x33}')

I12x36 = Parameter(name = 'I12x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3',
                   texname = '\\text{I12x36}')

I120x33 = Parameter(name = 'I120x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3',
                    texname = '\\text{I120x33}')

I120x36 = Parameter(name = 'I120x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3',
                    texname = '\\text{I120x36}')

I121x11 = Parameter(name = 'I121x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                    texname = '\\text{I121x11}')

I121x22 = Parameter(name = 'I121x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                    texname = '\\text{I121x22}')

I121x33 = Parameter(name = 'I121x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I121x33}')

I121x36 = Parameter(name = 'I121x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I121x36}')

I121x63 = Parameter(name = 'I121x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I121x63}')

I121x66 = Parameter(name = 'I121x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I121x66}')

I122x33 = Parameter(name = 'I122x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122x33}')

I122x36 = Parameter(name = 'I122x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122x36}')

I122x63 = Parameter(name = 'I122x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122x63}')

I122x66 = Parameter(name = 'I122x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I122x66}')

I123x33 = Parameter(name = 'I123x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                    texname = '\\text{I123x33}')

I123x36 = Parameter(name = 'I123x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                    texname = '\\text{I123x36}')

I123x63 = Parameter(name = 'I123x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                    texname = '\\text{I123x63}')

I123x66 = Parameter(name = 'I123x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                    texname = '\\text{I123x66}')

I124x33 = Parameter(name = 'I124x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*tu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I124x33}')

I124x36 = Parameter(name = 'I124x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*tu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I124x36}')

I124x63 = Parameter(name = 'I124x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*tu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I124x63}')

I124x66 = Parameter(name = 'I124x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*tu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I124x66}')

I125x33 = Parameter(name = 'I125x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I125x33}')

I125x36 = Parameter(name = 'I125x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I125x36}')

I125x63 = Parameter(name = 'I125x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I125x63}')

I125x66 = Parameter(name = 'I125x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I125x66}')

I126x33 = Parameter(name = 'I126x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*yu3x3*complexconjugate(Rd3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I126x33}')

I126x36 = Parameter(name = 'I126x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*yu3x3*complexconjugate(Rd3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I126x36}')

I126x63 = Parameter(name = 'I126x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*yu3x3*complexconjugate(Rd6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I126x63}')

I126x66 = Parameter(name = 'I126x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*yu3x3*complexconjugate(Rd6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I126x66}')

I127x33 = Parameter(name = 'I127x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I127x33}')

I127x36 = Parameter(name = 'I127x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I127x36}')

I127x63 = Parameter(name = 'I127x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I127x63}')

I127x66 = Parameter(name = 'I127x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I127x66}')

I128x33 = Parameter(name = 'I128x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I128x33}')

I128x36 = Parameter(name = 'I128x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I128x36}')

I128x63 = Parameter(name = 'I128x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I128x63}')

I128x66 = Parameter(name = 'I128x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I128x66}')

I129x11 = Parameter(name = 'I129x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x1*complexconjugate(Ru1x1)',
                    texname = '\\text{I129x11}')

I129x22 = Parameter(name = 'I129x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x2*complexconjugate(Ru2x2)',
                    texname = '\\text{I129x22}')

I129x33 = Parameter(name = 'I129x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I129x33}')

I129x36 = Parameter(name = 'I129x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I129x36}')

I129x63 = Parameter(name = 'I129x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I129x63}')

I129x66 = Parameter(name = 'I129x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I129x66}')

I13x33 = Parameter(name = 'I13x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I13x33}')

I13x36 = Parameter(name = 'I13x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I13x36}')

I130x33 = Parameter(name = 'I130x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I130x33}')

I130x36 = Parameter(name = 'I130x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru3x6)',
                    texname = '\\text{I130x36}')

I130x44 = Parameter(name = 'I130x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*complexconjugate(Ru4x4)',
                    texname = '\\text{I130x44}')

I130x55 = Parameter(name = 'I130x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x5*complexconjugate(Ru5x5)',
                    texname = '\\text{I130x55}')

I130x63 = Parameter(name = 'I130x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I130x63}')

I130x66 = Parameter(name = 'I130x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*complexconjugate(Ru6x6)',
                    texname = '\\text{I130x66}')

I131x33 = Parameter(name = 'I131x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131x33}')

I131x36 = Parameter(name = 'I131x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131x36}')

I131x63 = Parameter(name = 'I131x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131x63}')

I131x66 = Parameter(name = 'I131x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131x66}')

I132x33 = Parameter(name = 'I132x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I132x33}')

I132x36 = Parameter(name = 'I132x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I132x36}')

I132x63 = Parameter(name = 'I132x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I132x63}')

I132x66 = Parameter(name = 'I132x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I132x66}')

I133x33 = Parameter(name = 'I133x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*tu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I133x33}')

I133x36 = Parameter(name = 'I133x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*tu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I133x36}')

I133x63 = Parameter(name = 'I133x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*tu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I133x63}')

I133x66 = Parameter(name = 'I133x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*tu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I133x66}')

I134x33 = Parameter(name = 'I134x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I134x33}')

I134x36 = Parameter(name = 'I134x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I134x36}')

I134x63 = Parameter(name = 'I134x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I134x63}')

I134x66 = Parameter(name = 'I134x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I134x66}')

I135x33 = Parameter(name = 'I135x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*yu3x3*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I135x33}')

I135x36 = Parameter(name = 'I135x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*yu3x3*complexconjugate(Ru3x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I135x36}')

I135x63 = Parameter(name = 'I135x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*yu3x3*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I135x63}')

I135x66 = Parameter(name = 'I135x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*yu3x3*complexconjugate(Ru6x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I135x66}')

I136x33 = Parameter(name = 'I136x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136x33}')

I136x36 = Parameter(name = 'I136x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136x36}')

I136x63 = Parameter(name = 'I136x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136x63}')

I136x66 = Parameter(name = 'I136x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I136x66}')

I137x33 = Parameter(name = 'I137x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I137x33}')

I137x36 = Parameter(name = 'I137x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I137x36}')

I137x63 = Parameter(name = 'I137x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x6*yd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I137x63}')

I137x66 = Parameter(name = 'I137x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x6*yd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I137x66}')

I138x33 = Parameter(name = 'I138x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I138x33}')

I138x36 = Parameter(name = 'I138x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I138x36}')

I138x63 = Parameter(name = 'I138x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I138x63}')

I138x66 = Parameter(name = 'I138x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I138x66}')

I139x11 = Parameter(name = 'I139x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x1*complexconjugate(Rl1x1)',
                    texname = '\\text{I139x11}')

I139x22 = Parameter(name = 'I139x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x2*complexconjugate(Rl2x2)',
                    texname = '\\text{I139x22}')

I139x33 = Parameter(name = 'I139x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I139x33}')

I139x36 = Parameter(name = 'I139x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I139x36}')

I139x63 = Parameter(name = 'I139x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I139x63}')

I139x66 = Parameter(name = 'I139x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I139x66}')

I14x33 = Parameter(name = 'I14x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I14x33}')

I14x36 = Parameter(name = 'I14x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(yd3x3)',
                   texname = '\\text{I14x36}')

I140x33 = Parameter(name = 'I140x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*complexconjugate(Rl3x6)',
                    texname = '\\text{I140x33}')

I140x36 = Parameter(name = 'I140x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl3x6)',
                    texname = '\\text{I140x36}')

I140x44 = Parameter(name = 'I140x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x4*complexconjugate(Rl4x4)',
                    texname = '\\text{I140x44}')

I140x55 = Parameter(name = 'I140x55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x5*complexconjugate(Rl5x5)',
                    texname = '\\text{I140x55}')

I140x63 = Parameter(name = 'I140x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I140x63}')

I140x66 = Parameter(name = 'I140x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I140x66}')

I141x33 = Parameter(name = 'I141x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I141x33}')

I141x36 = Parameter(name = 'I141x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I141x36}')

I141x63 = Parameter(name = 'I141x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x6*ye3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I141x63}')

I141x66 = Parameter(name = 'I141x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*ye3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I141x66}')

I142x33 = Parameter(name = 'I142x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I142x33}')

I142x36 = Parameter(name = 'I142x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I142x36}')

I142x63 = Parameter(name = 'I142x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I142x63}')

I142x66 = Parameter(name = 'I142x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I142x66}')

I143x33 = Parameter(name = 'I143x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I143x33}')

I143x36 = Parameter(name = 'I143x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru3x3)',
                    texname = '\\text{I143x36}')

I143x63 = Parameter(name = 'I143x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I143x63}')

I143x66 = Parameter(name = 'I143x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x6*yu3x3*complexconjugate(Ru6x3)',
                    texname = '\\text{I143x66}')

I144x33 = Parameter(name = 'I144x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I144x33}')

I144x36 = Parameter(name = 'I144x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I144x36}')

I144x63 = Parameter(name = 'I144x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I144x63}')

I144x66 = Parameter(name = 'I144x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x3*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I144x66}')

I145x11 = Parameter(name = 'I145x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM1x1*complexconjugate(Rd1x1)',
                    texname = '\\text{I145x11}')

I145x22 = Parameter(name = 'I145x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM2x2*complexconjugate(Rd2x2)',
                    texname = '\\text{I145x22}')

I145x33 = Parameter(name = 'I145x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I145x33}')

I145x36 = Parameter(name = 'I145x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I145x36}')

I146x33 = Parameter(name = 'I146x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I146x33}')

I146x36 = Parameter(name = 'I146x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I146x36}')

I147x33 = Parameter(name = 'I147x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*yu3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I147x33}')

I147x36 = Parameter(name = 'I147x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*yu3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I147x36}')

I148x11 = Parameter(name = 'I148x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl1x1)',
                    texname = '\\text{I148x11}')

I148x22 = Parameter(name = 'I148x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl2x2)',
                    texname = '\\text{I148x22}')

I148x33 = Parameter(name = 'I148x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl3x3)',
                    texname = '\\text{I148x33}')

I148x36 = Parameter(name = 'I148x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x3)',
                    texname = '\\text{I148x36}')

I149x33 = Parameter(name = 'I149x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I149x33}')

I149x36 = Parameter(name = 'I149x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I149x36}')

I15x33 = Parameter(name = 'I15x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I15x33}')

I15x36 = Parameter(name = 'I15x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I15x36}')

I150x11 = Parameter(name = 'I150x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn1x1)',
                    texname = '\\text{I150x11}')

I150x22 = Parameter(name = 'I150x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn2x2)',
                    texname = '\\text{I150x22}')

I150x33 = Parameter(name = 'I150x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn3x3)',
                    texname = '\\text{I150x33}')

I151x33 = Parameter(name = 'I151x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I151x33}')

I152x11 = Parameter(name = 'I152x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I152x11}')

I152x22 = Parameter(name = 'I152x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I152x22}')

I152x33 = Parameter(name = 'I152x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I152x33}')

I152x36 = Parameter(name = 'I152x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I152x36}')

I153x33 = Parameter(name = 'I153x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I153x33}')

I153x36 = Parameter(name = 'I153x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I153x36}')

I154x33 = Parameter(name = 'I154x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I154x33}')

I154x36 = Parameter(name = 'I154x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I154x36}')

I155x11 = Parameter(name = 'I155x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                    texname = '\\text{I155x11}')

I155x22 = Parameter(name = 'I155x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                    texname = '\\text{I155x22}')

I155x33 = Parameter(name = 'I155x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I155x33}')

I155x36 = Parameter(name = 'I155x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I155x36}')

I155x63 = Parameter(name = 'I155x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I155x63}')

I155x66 = Parameter(name = 'I155x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I155x66}')

I156x11 = Parameter(name = 'I156x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x1*complexconjugate(Rl1x1)',
                    texname = '\\text{I156x11}')

I156x22 = Parameter(name = 'I156x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(Rl2x2)',
                    texname = '\\text{I156x22}')

I156x33 = Parameter(name = 'I156x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I156x33}')

I156x36 = Parameter(name = 'I156x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I156x36}')

I157x11 = Parameter(name = 'I157x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I157x11}')

I157x22 = Parameter(name = 'I157x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I157x22}')

I157x33 = Parameter(name = 'I157x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I157x33}')

I157x36 = Parameter(name = 'I157x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I157x36}')

I157x63 = Parameter(name = 'I157x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I157x63}')

I157x66 = Parameter(name = 'I157x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I157x66}')

I158x11 = Parameter(name = 'I158x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x1*complexconjugate(Rn1x1)',
                    texname = '\\text{I158x11}')

I158x22 = Parameter(name = 'I158x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I158x22}')

I158x33 = Parameter(name = 'I158x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I158x33}')

I158x36 = Parameter(name = 'I158x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rn3x3)',
                    texname = '\\text{I158x36}')

I159x11 = Parameter(name = 'I159x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn1x1)',
                    texname = '\\text{I159x11}')

I159x22 = Parameter(name = 'I159x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn2x2)',
                    texname = '\\text{I159x22}')

I159x33 = Parameter(name = 'I159x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn3x3)',
                    texname = '\\text{I159x33}')

I16x33 = Parameter(name = 'I16x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I16x33}')

I16x36 = Parameter(name = 'I16x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I16x36}')

I160x11 = Parameter(name = 'I160x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                    texname = '\\text{I160x11}')

I160x22 = Parameter(name = 'I160x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                    texname = '\\text{I160x22}')

I160x33 = Parameter(name = 'I160x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                    texname = '\\text{I160x33}')

I160x36 = Parameter(name = 'I160x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                    texname = '\\text{I160x36}')

I161x11 = Parameter(name = 'I161x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x1*complexconjugate(Rd1x1)',
                    texname = '\\text{I161x11}')

I161x22 = Parameter(name = 'I161x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x2*complexconjugate(Rd2x2)',
                    texname = '\\text{I161x22}')

I161x33 = Parameter(name = 'I161x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I161x33}')

I161x36 = Parameter(name = 'I161x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd3x3)',
                    texname = '\\text{I161x36}')

I161x63 = Parameter(name = 'I161x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I161x63}')

I161x66 = Parameter(name = 'I161x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x3*complexconjugate(Rd6x3)',
                    texname = '\\text{I161x66}')

I162x11 = Parameter(name = 'I162x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x1*complexconjugate(Rl1x1)',
                    texname = '\\text{I162x11}')

I162x22 = Parameter(name = 'I162x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x2*complexconjugate(Rl2x2)',
                    texname = '\\text{I162x22}')

I162x33 = Parameter(name = 'I162x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I162x33}')

I162x36 = Parameter(name = 'I162x36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl3x3)',
                    texname = '\\text{I162x36}')

I162x63 = Parameter(name = 'I162x63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I162x63}')

I162x66 = Parameter(name = 'I162x66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I162x66}')

I17x33 = Parameter(name = 'I17x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3',
                   texname = '\\text{I17x33}')

I17x36 = Parameter(name = 'I17x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I17x36}')

I18x33 = Parameter(name = 'I18x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(ye3x3)',
                   texname = '\\text{I18x33}')

I18x36 = Parameter(name = 'I18x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(ye3x3)',
                   texname = '\\text{I18x36}')

I19x33 = Parameter(name = 'I19x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3',
                   texname = '\\text{I19x33}')

I19x36 = Parameter(name = 'I19x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3',
                   texname = '\\text{I19x36}')

I2x33 = Parameter(name = 'I2x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye3x3',
                  texname = '\\text{I2x33}')

I20x33 = Parameter(name = 'I20x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I20x33}')

I20x36 = Parameter(name = 'I20x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(yd3x3)',
                   texname = '\\text{I20x36}')

I21x33 = Parameter(name = 'I21x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3',
                   texname = '\\text{I21x33}')

I21x36 = Parameter(name = 'I21x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3',
                   texname = '\\text{I21x36}')

I22x33 = Parameter(name = 'I22x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(yu3x3)',
                   texname = '\\text{I22x33}')

I22x36 = Parameter(name = 'I22x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(yu3x3)',
                   texname = '\\text{I22x36}')

I23x33 = Parameter(name = 'I23x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I23x33}')

I23x36 = Parameter(name = 'I23x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I23x36}')

I24x33 = Parameter(name = 'I24x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I24x33}')

I24x36 = Parameter(name = 'I24x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I24x36}')

I25x33 = Parameter(name = 'I25x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I25x33}')

I25x36 = Parameter(name = 'I25x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I25x36}')

I26x33 = Parameter(name = 'I26x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I26x33}')

I26x36 = Parameter(name = 'I26x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I26x36}')

I27x33 = Parameter(name = 'I27x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I27x33}')

I27x36 = Parameter(name = 'I27x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I27x36}')

I28x33 = Parameter(name = 'I28x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I28x33}')

I28x36 = Parameter(name = 'I28x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I28x36}')

I29x33 = Parameter(name = 'I29x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I29x33}')

I3x11 = Parameter(name = 'I3x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn1x1*complexconjugate(Rl1x1)',
                  texname = '\\text{I3x11}')

I3x22 = Parameter(name = 'I3x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn2x2*complexconjugate(Rl2x2)',
                  texname = '\\text{I3x22}')

I3x33 = Parameter(name = 'I3x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn3x3*complexconjugate(Rl3x3)',
                  texname = '\\text{I3x33}')

I3x36 = Parameter(name = 'I3x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rn3x3*complexconjugate(Rl6x3)',
                  texname = '\\text{I3x36}')

I30x33 = Parameter(name = 'I30x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I30x33}')

I31x33 = Parameter(name = 'I31x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3',
                   texname = '\\text{I31x33}')

I31x36 = Parameter(name = 'I31x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3',
                   texname = '\\text{I31x36}')

I32x33 = Parameter(name = 'I32x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I32x33}')

I32x36 = Parameter(name = 'I32x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(yd3x3)',
                   texname = '\\text{I32x36}')

I33x33 = Parameter(name = 'I33x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I33x33}')

I33x36 = Parameter(name = 'I33x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I33x36}')

I34x33 = Parameter(name = 'I34x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I34x33}')

I34x36 = Parameter(name = 'I34x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I34x36}')

I35x33 = Parameter(name = 'I35x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3',
                   texname = '\\text{I35x33}')

I35x36 = Parameter(name = 'I35x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I35x36}')

I36x33 = Parameter(name = 'I36x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(ye3x3)',
                   texname = '\\text{I36x33}')

I36x36 = Parameter(name = 'I36x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(ye3x3)',
                   texname = '\\text{I36x36}')

I37x33 = Parameter(name = 'I37x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I37x33}')

I37x36 = Parameter(name = 'I37x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I37x36}')

I38x33 = Parameter(name = 'I38x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I38x33}')

I38x36 = Parameter(name = 'I38x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I38x36}')

I39x33 = Parameter(name = 'I39x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*yu3x3',
                   texname = '\\text{I39x33}')

I39x36 = Parameter(name = 'I39x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*yu3x3',
                   texname = '\\text{I39x36}')

I4x11 = Parameter(name = 'I4x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                  texname = '\\text{I4x11}')

I4x22 = Parameter(name = 'I4x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                  texname = '\\text{I4x22}')

I4x33 = Parameter(name = 'I4x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                  texname = '\\text{I4x33}')

I4x36 = Parameter(name = 'I4x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                  texname = '\\text{I4x36}')

I4x63 = Parameter(name = 'I4x63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                  texname = '\\text{I4x63}')

I4x66 = Parameter(name = 'I4x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                  texname = '\\text{I4x66}')

I40x33 = Parameter(name = 'I40x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(yu3x3)',
                   texname = '\\text{I40x33}')

I40x36 = Parameter(name = 'I40x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(yu3x3)',
                   texname = '\\text{I40x36}')

I41x33 = Parameter(name = 'I41x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I41x33}')

I41x36 = Parameter(name = 'I41x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(CKM3x3)*complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I41x36}')

I42x33 = Parameter(name = 'I42x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                   texname = '\\text{I42x33}')

I42x36 = Parameter(name = 'I42x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                   texname = '\\text{I42x36}')

I43x33 = Parameter(name = 'I43x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru3x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I43x33}')

I43x36 = Parameter(name = 'I43x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru6x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I43x36}')

I44x33 = Parameter(name = 'I44x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I44x33}')

I44x36 = Parameter(name = 'I44x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I44x36}')

I45x11 = Parameter(name = 'I45x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I45x11}')

I45x22 = Parameter(name = 'I45x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I45x22}')

I45x33 = Parameter(name = 'I45x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I45x33}')

I45x36 = Parameter(name = 'I45x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I45x36}')

I45x63 = Parameter(name = 'I45x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I45x63}')

I45x66 = Parameter(name = 'I45x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I45x66}')

I46x33 = Parameter(name = 'I46x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I46x33}')

I46x36 = Parameter(name = 'I46x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I46x36}')

I46x44 = Parameter(name = 'I46x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I46x44}')

I46x55 = Parameter(name = 'I46x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I46x55}')

I46x63 = Parameter(name = 'I46x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I46x63}')

I46x66 = Parameter(name = 'I46x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I46x66}')

I47x11 = Parameter(name = 'I47x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I47x11}')

I47x22 = Parameter(name = 'I47x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I47x22}')

I47x33 = Parameter(name = 'I47x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I47x33}')

I47x36 = Parameter(name = 'I47x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I47x36}')

I48x33 = Parameter(name = 'I48x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I48x33}')

I48x36 = Parameter(name = 'I48x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I48x36}')

I49x33 = Parameter(name = 'I49x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I49x33}')

I49x36 = Parameter(name = 'I49x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I49x36}')

I5x11 = Parameter(name = 'I5x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl1x1*complexconjugate(Rn1x1)',
                  texname = '\\text{I5x11}')

I5x22 = Parameter(name = 'I5x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl2x2*complexconjugate(Rn2x2)',
                  texname = '\\text{I5x22}')

I5x33 = Parameter(name = 'I5x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl3x3*complexconjugate(Rn3x3)',
                  texname = '\\text{I5x33}')

I5x36 = Parameter(name = 'I5x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl6x3*complexconjugate(Rn3x3)',
                  texname = '\\text{I5x36}')

I50x11 = Parameter(name = 'I50x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I50x11}')

I50x22 = Parameter(name = 'I50x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I50x22}')

I50x33 = Parameter(name = 'I50x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I50x33}')

I50x36 = Parameter(name = 'I50x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I50x36}')

I50x63 = Parameter(name = 'I50x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I50x63}')

I50x66 = Parameter(name = 'I50x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I50x66}')

I51x33 = Parameter(name = 'I51x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I51x33}')

I51x36 = Parameter(name = 'I51x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I51x36}')

I51x44 = Parameter(name = 'I51x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I51x44}')

I51x55 = Parameter(name = 'I51x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I51x55}')

I51x63 = Parameter(name = 'I51x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I51x63}')

I51x66 = Parameter(name = 'I51x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I51x66}')

I52x11 = Parameter(name = 'I52x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I52x11}')

I52x22 = Parameter(name = 'I52x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I52x22}')

I52x33 = Parameter(name = 'I52x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I52x33}')

I52x36 = Parameter(name = 'I52x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I52x36}')

I52x63 = Parameter(name = 'I52x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I52x63}')

I52x66 = Parameter(name = 'I52x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I52x66}')

I53x33 = Parameter(name = 'I53x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I53x33}')

I53x36 = Parameter(name = 'I53x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I53x36}')

I53x44 = Parameter(name = 'I53x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I53x44}')

I53x55 = Parameter(name = 'I53x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I53x55}')

I53x63 = Parameter(name = 'I53x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I53x63}')

I53x66 = Parameter(name = 'I53x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I53x66}')

I54x11 = Parameter(name = 'I54x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I54x11}')

I54x22 = Parameter(name = 'I54x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I54x22}')

I54x33 = Parameter(name = 'I54x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I54x33}')

I54x36 = Parameter(name = 'I54x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I54x36}')

I54x63 = Parameter(name = 'I54x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I54x63}')

I54x66 = Parameter(name = 'I54x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I54x66}')

I55x33 = Parameter(name = 'I55x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I55x33}')

I55x36 = Parameter(name = 'I55x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I55x36}')

I55x44 = Parameter(name = 'I55x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I55x44}')

I55x55 = Parameter(name = 'I55x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I55x55}')

I55x63 = Parameter(name = 'I55x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I55x63}')

I55x66 = Parameter(name = 'I55x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I55x66}')

I56x33 = Parameter(name = 'I56x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I56x33}')

I56x36 = Parameter(name = 'I56x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(td3x3)',
                   texname = '\\text{I56x36}')

I56x63 = Parameter(name = 'I56x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I56x63}')

I56x66 = Parameter(name = 'I56x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(td3x3)',
                   texname = '\\text{I56x66}')

I57x11 = Parameter(name = 'I57x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x1*complexconjugate(Ru1x1)',
                   texname = '\\text{I57x11}')

I57x22 = Parameter(name = 'I57x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x2*complexconjugate(Ru2x2)',
                   texname = '\\text{I57x22}')

I57x33 = Parameter(name = 'I57x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I57x33}')

I57x36 = Parameter(name = 'I57x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I57x36}')

I57x63 = Parameter(name = 'I57x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I57x63}')

I57x66 = Parameter(name = 'I57x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I57x66}')

I58x33 = Parameter(name = 'I58x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I58x33}')

I58x36 = Parameter(name = 'I58x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I58x36}')

I58x44 = Parameter(name = 'I58x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I58x44}')

I58x55 = Parameter(name = 'I58x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x5*complexconjugate(Ru5x5)',
                   texname = '\\text{I58x55}')

I58x63 = Parameter(name = 'I58x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I58x63}')

I58x66 = Parameter(name = 'I58x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I58x66}')

I59x33 = Parameter(name = 'I59x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I59x33}')

I59x36 = Parameter(name = 'I59x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I59x36}')

I59x63 = Parameter(name = 'I59x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I59x63}')

I59x66 = Parameter(name = 'I59x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I59x66}')

I6x11 = Parameter(name = 'I6x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x1*complexconjugate(CKM1x1)*complexconjugate(Ru1x1)',
                  texname = '\\text{I6x11}')

I6x22 = Parameter(name = 'I6x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x2*complexconjugate(CKM2x2)*complexconjugate(Ru2x2)',
                  texname = '\\text{I6x22}')

I6x33 = Parameter(name = 'I6x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                  texname = '\\text{I6x33}')

I6x36 = Parameter(name = 'I6x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                  texname = '\\text{I6x36}')

I6x63 = Parameter(name = 'I6x63',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru3x3)',
                  texname = '\\text{I6x63}')

I6x66 = Parameter(name = 'I6x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x3*complexconjugate(CKM3x3)*complexconjugate(Ru6x3)',
                  texname = '\\text{I6x66}')

I60x33 = Parameter(name = 'I60x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I60x33}')

I60x36 = Parameter(name = 'I60x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I60x36}')

I60x63 = Parameter(name = 'I60x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*td3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I60x63}')

I60x66 = Parameter(name = 'I60x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*td3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I60x66}')

I61x33 = Parameter(name = 'I61x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I61x33}')

I61x36 = Parameter(name = 'I61x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(Rd3x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I61x36}')

I61x63 = Parameter(name = 'I61x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I61x63}')

I61x66 = Parameter(name = 'I61x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*yd3x3*complexconjugate(Rd6x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I61x66}')

I62x33 = Parameter(name = 'I62x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I62x33}')

I62x36 = Parameter(name = 'I62x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I62x36}')

I62x63 = Parameter(name = 'I62x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I62x63}')

I62x66 = Parameter(name = 'I62x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I62x66}')

I63x33 = Parameter(name = 'I63x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I63x33}')

I63x36 = Parameter(name = 'I63x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I63x36}')

I63x63 = Parameter(name = 'I63x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*yd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I63x63}')

I63x66 = Parameter(name = 'I63x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*yd3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I63x66}')

I64x11 = Parameter(name = 'I64x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I64x11}')

I64x22 = Parameter(name = 'I64x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I64x22}')

I64x33 = Parameter(name = 'I64x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I64x33}')

I64x36 = Parameter(name = 'I64x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I64x36}')

I65x33 = Parameter(name = 'I65x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I65x33}')

I65x36 = Parameter(name = 'I65x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I65x36}')

I66x11 = Parameter(name = 'I66x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rn1x1)',
                   texname = '\\text{I66x11}')

I66x22 = Parameter(name = 'I66x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I66x22}')

I66x33 = Parameter(name = 'I66x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I66x33}')

I66x36 = Parameter(name = 'I66x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I66x36}')

I67x33 = Parameter(name = 'I67x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I67x33}')

I67x36 = Parameter(name = 'I67x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I67x36}')

I68x11 = Parameter(name = 'I68x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I68x11}')

I68x22 = Parameter(name = 'I68x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I68x22}')

I68x33 = Parameter(name = 'I68x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I68x33}')

I68x36 = Parameter(name = 'I68x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I68x36}')

I68x63 = Parameter(name = 'I68x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I68x63}')

I68x66 = Parameter(name = 'I68x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I68x66}')

I69x33 = Parameter(name = 'I69x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I69x33}')

I69x36 = Parameter(name = 'I69x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I69x36}')

I69x44 = Parameter(name = 'I69x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I69x44}')

I69x55 = Parameter(name = 'I69x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I69x55}')

I69x63 = Parameter(name = 'I69x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I69x63}')

I69x66 = Parameter(name = 'I69x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I69x66}')

I7x33 = Parameter(name = 'I7x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl3x6*ye3x3',
                  texname = '\\text{I7x33}')

I7x36 = Parameter(name = 'I7x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rl6x6*ye3x3',
                  texname = '\\text{I7x36}')

I70x11 = Parameter(name = 'I70x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I70x11}')

I70x22 = Parameter(name = 'I70x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I70x22}')

I70x33 = Parameter(name = 'I70x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I70x33}')

I70x36 = Parameter(name = 'I70x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I70x36}')

I70x63 = Parameter(name = 'I70x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I70x63}')

I70x66 = Parameter(name = 'I70x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I70x66}')

I71x33 = Parameter(name = 'I71x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I71x33}')

I71x36 = Parameter(name = 'I71x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I71x36}')

I71x44 = Parameter(name = 'I71x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I71x44}')

I71x55 = Parameter(name = 'I71x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I71x55}')

I71x63 = Parameter(name = 'I71x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I71x63}')

I71x66 = Parameter(name = 'I71x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I71x66}')

I72x33 = Parameter(name = 'I72x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I72x33}')

I72x36 = Parameter(name = 'I72x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I72x36}')

I72x44 = Parameter(name = 'I72x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I72x44}')

I72x55 = Parameter(name = 'I72x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x5*complexconjugate(Ru5x5)',
                   texname = '\\text{I72x55}')

I72x63 = Parameter(name = 'I72x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I72x63}')

I72x66 = Parameter(name = 'I72x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I72x66}')

I73x33 = Parameter(name = 'I73x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*complexconjugate(yd3x3)',
                   texname = '\\text{I73x33}')

I74x33 = Parameter(name = 'I74x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*yu3x3',
                   texname = '\\text{I74x33}')

I75x33 = Parameter(name = 'I75x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye3x3)',
                   texname = '\\text{I75x33}')

I76x11 = Parameter(name = 'I76x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*Ru1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I76x11}')

I76x22 = Parameter(name = 'I76x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM2x2*Ru2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I76x22}')

I76x33 = Parameter(name = 'I76x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I76x33}')

I76x36 = Parameter(name = 'I76x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I76x36}')

I76x63 = Parameter(name = 'I76x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I76x63}')

I76x66 = Parameter(name = 'I76x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I76x66}')

I77x33 = Parameter(name = 'I77x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I77x33}')

I77x36 = Parameter(name = 'I77x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I77x36}')

I77x63 = Parameter(name = 'I77x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x6*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I77x63}')

I77x66 = Parameter(name = 'I77x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x6*yu3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I77x66}')

I78x33 = Parameter(name = 'I78x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I78x33}')

I78x36 = Parameter(name = 'I78x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd3x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I78x36}')

I78x63 = Parameter(name = 'I78x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru3x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I78x63}')

I78x66 = Parameter(name = 'I78x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM3x3*Ru6x3*complexconjugate(Rd6x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I78x66}')

I79x11 = Parameter(name = 'I79x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I79x11}')

I79x22 = Parameter(name = 'I79x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I79x22}')

I79x33 = Parameter(name = 'I79x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I79x33}')

I79x36 = Parameter(name = 'I79x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I79x36}')

I79x63 = Parameter(name = 'I79x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I79x63}')

I79x66 = Parameter(name = 'I79x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I79x66}')

I8x33 = Parameter(name = 'I8x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                  texname = '\\text{I8x33}')

I8x36 = Parameter(name = 'I8x36',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                  texname = '\\text{I8x36}')

I80x33 = Parameter(name = 'I80x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I80x33}')

I80x36 = Parameter(name = 'I80x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I80x36}')

I80x44 = Parameter(name = 'I80x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I80x44}')

I80x55 = Parameter(name = 'I80x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I80x55}')

I80x63 = Parameter(name = 'I80x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I80x63}')

I80x66 = Parameter(name = 'I80x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I80x66}')

I81x11 = Parameter(name = 'I81x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1',
                   texname = '\\text{I81x11}')

I81x22 = Parameter(name = 'I81x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2',
                   texname = '\\text{I81x22}')

I81x33 = Parameter(name = 'I81x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3',
                   texname = '\\text{I81x33}')

I81x36 = Parameter(name = 'I81x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3',
                   texname = '\\text{I81x36}')

I82x33 = Parameter(name = 'I82x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3',
                   texname = '\\text{I82x33}')

I82x36 = Parameter(name = 'I82x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I82x36}')

I83x11 = Parameter(name = 'I83x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rl1x1)',
                   texname = '\\text{I83x11}')

I83x22 = Parameter(name = 'I83x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rl2x2)',
                   texname = '\\text{I83x22}')

I83x33 = Parameter(name = 'I83x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I83x33}')

I83x36 = Parameter(name = 'I83x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I83x36}')

I83x63 = Parameter(name = 'I83x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I83x63}')

I83x66 = Parameter(name = 'I83x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I83x66}')

I84x33 = Parameter(name = 'I84x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I84x33}')

I84x36 = Parameter(name = 'I84x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl3x6)',
                   texname = '\\text{I84x36}')

I84x44 = Parameter(name = 'I84x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x4*complexconjugate(Rl4x4)',
                   texname = '\\text{I84x44}')

I84x55 = Parameter(name = 'I84x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x5*complexconjugate(Rl5x5)',
                   texname = '\\text{I84x55}')

I84x63 = Parameter(name = 'I84x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I84x63}')

I84x66 = Parameter(name = 'I84x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I84x66}')

I85x33 = Parameter(name = 'I85x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                   texname = '\\text{I85x33}')

I85x36 = Parameter(name = 'I85x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(te3x3)',
                   texname = '\\text{I85x36}')

I85x63 = Parameter(name = 'I85x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I85x63}')

I85x66 = Parameter(name = 'I85x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I85x66}')

I86x33 = Parameter(name = 'I86x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86x33}')

I86x36 = Parameter(name = 'I86x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86x36}')

I86x63 = Parameter(name = 'I86x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86x63}')

I86x66 = Parameter(name = 'I86x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I86x66}')

I87x33 = Parameter(name = 'I87x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I87x33}')

I87x36 = Parameter(name = 'I87x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I87x36}')

I87x63 = Parameter(name = 'I87x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I87x63}')

I87x66 = Parameter(name = 'I87x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I87x66}')

I88x33 = Parameter(name = 'I88x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I88x33}')

I88x36 = Parameter(name = 'I88x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I88x36}')

I88x63 = Parameter(name = 'I88x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I88x63}')

I88x66 = Parameter(name = 'I88x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I88x66}')

I89x11 = Parameter(name = 'I89x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x1*complexconjugate(Rd1x1)',
                   texname = '\\text{I89x11}')

I89x22 = Parameter(name = 'I89x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x2*complexconjugate(Rd2x2)',
                   texname = '\\text{I89x22}')

I89x33 = Parameter(name = 'I89x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I89x33}')

I89x36 = Parameter(name = 'I89x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd3x3)',
                   texname = '\\text{I89x36}')

I89x63 = Parameter(name = 'I89x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I89x63}')

I89x66 = Parameter(name = 'I89x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x3*complexconjugate(Rd6x3)',
                   texname = '\\text{I89x66}')

I9x33 = Parameter(name = 'I9x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye3x3*complexconjugate(Rn3x3)',
                  texname = '\\text{I9x33}')

I90x33 = Parameter(name = 'I90x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I90x33}')

I90x36 = Parameter(name = 'I90x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl3x3)',
                   texname = '\\text{I90x36}')

I90x63 = Parameter(name = 'I90x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I90x63}')

I90x66 = Parameter(name = 'I90x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I90x66}')

I91x33 = Parameter(name = 'I91x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I91x33}')

I91x36 = Parameter(name = 'I91x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd3x6)',
                   texname = '\\text{I91x36}')

I91x44 = Parameter(name = 'I91x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I91x44}')

I91x55 = Parameter(name = 'I91x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x5*complexconjugate(Rd5x5)',
                   texname = '\\text{I91x55}')

I91x63 = Parameter(name = 'I91x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I91x63}')

I91x66 = Parameter(name = 'I91x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x6*complexconjugate(Rd6x6)',
                   texname = '\\text{I91x66}')

I92x33 = Parameter(name = 'I92x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I92x33}')

I92x36 = Parameter(name = 'I92x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl3x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I92x36}')

I92x63 = Parameter(name = 'I92x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I92x63}')

I92x66 = Parameter(name = 'I92x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I92x66}')

I93x11 = Parameter(name = 'I93x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x1*complexconjugate(Ru1x1)',
                   texname = '\\text{I93x11}')

I93x22 = Parameter(name = 'I93x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x2*complexconjugate(Ru2x2)',
                   texname = '\\text{I93x22}')

I93x33 = Parameter(name = 'I93x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I93x33}')

I93x36 = Parameter(name = 'I93x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru3x3)',
                   texname = '\\text{I93x36}')

I93x63 = Parameter(name = 'I93x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I93x63}')

I93x66 = Parameter(name = 'I93x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x3*complexconjugate(Ru6x3)',
                   texname = '\\text{I93x66}')

I94x33 = Parameter(name = 'I94x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I94x33}')

I94x36 = Parameter(name = 'I94x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru3x6)',
                   texname = '\\text{I94x36}')

I94x44 = Parameter(name = 'I94x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I94x44}')

I94x55 = Parameter(name = 'I94x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x5*complexconjugate(Ru5x5)',
                   texname = '\\text{I94x55}')

I94x63 = Parameter(name = 'I94x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I94x63}')

I94x66 = Parameter(name = 'I94x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x6*complexconjugate(Ru6x6)',
                   texname = '\\text{I94x66}')

I95x11 = Parameter(name = 'I95x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x1*complexconjugate(Rn1x1)',
                   texname = '\\text{I95x11}')

I95x22 = Parameter(name = 'I95x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I95x22}')

I95x33 = Parameter(name = 'I95x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I95x33}')

I95x36 = Parameter(name = 'I95x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I95x36}')

I96x33 = Parameter(name = 'I96x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*te3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I96x33}')

I96x36 = Parameter(name = 'I96x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I96x36}')

I97x33 = Parameter(name = 'I97x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x3*ye3x3*complexconjugate(Rn3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I97x33}')

I97x36 = Parameter(name = 'I97x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rn3x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I97x36}')

I98x33 = Parameter(name = 'I98x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I98x33}')

I98x36 = Parameter(name = 'I98x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rn3x3)',
                   texname = '\\text{I98x36}')

I99x11 = Parameter(name = 'I99x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x1',
                   texname = '\\text{I99x11}')

I99x22 = Parameter(name = 'I99x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2',
                   texname = '\\text{I99x22}')

I99x33 = Parameter(name = 'I99x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x3',
                   texname = '\\text{I99x33}')

