# This file was automatically created by FeynRules 1.7.160
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Apr 2013 13:43:14


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'G/2.',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(-2*ee*complex(0,1)*I108x11)/3.',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G*I108x11)',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(-2*ee*complex(0,1)*I108x22)/3.',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*G*I108x22)',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-2*ee*complex(0,1)*I108x33)/3. - (2*ee*complex(0,1)*I109x33)/3.',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*G*I108x33) - complex(0,1)*G*I109x33',
                 order = {'QCD':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-2*ee*complex(0,1)*I108x36)/3. - (2*ee*complex(0,1)*I109x36)/3.',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*G*I108x36) - complex(0,1)*G*I109x36',
                 order = {'QCD':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-2*ee*complex(0,1)*I109x44)/3.',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(complex(0,1)*G*I109x44)',
                 order = {'QCD':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-2*ee*complex(0,1)*I109x55)/3.',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*G*I109x55)',
                 order = {'QCD':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(2*ee*complex(0,1)*I108x63)/3. + (2*ee*complex(0,1)*I109x63)/3.',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G*I108x63 + complex(0,1)*G*I109x63',
                 order = {'QCD':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-2*ee*complex(0,1)*I108x66)/3. - (2*ee*complex(0,1)*I109x66)/3.',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*G*I108x66) - complex(0,1)*G*I109x66',
                 order = {'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(8*ee**2*complex(0,1)*I129x11)/9.',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(4*ee*complex(0,1)*G*I129x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'complex(0,1)*G**2*I129x11',
                 order = {'QCD':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(8*ee**2*complex(0,1)*I129x22)/9.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(4*ee*complex(0,1)*G*I129x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'complex(0,1)*G**2*I129x22',
                 order = {'QCD':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(8*ee**2*complex(0,1)*I129x33)/9. + (8*ee**2*complex(0,1)*I130x33)/9.',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(4*ee*complex(0,1)*G*I129x33)/3. + (4*ee*complex(0,1)*G*I130x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'complex(0,1)*G**2*I129x33 + complex(0,1)*G**2*I130x33',
                 order = {'QCD':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(8*ee**2*complex(0,1)*I129x36)/9. + (8*ee**2*complex(0,1)*I130x36)/9.',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(4*ee*complex(0,1)*G*I129x36)/3. + (4*ee*complex(0,1)*G*I130x36)/3.',
                 order = {'QCD':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'complex(0,1)*G**2*I129x36 + complex(0,1)*G**2*I130x36',
                 order = {'QCD':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(8*ee**2*complex(0,1)*I130x44)/9.',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(4*ee*complex(0,1)*G*I130x44)/3.',
                 order = {'QCD':1,'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*G**2*I130x44',
                 order = {'QCD':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(8*ee**2*complex(0,1)*I130x55)/9.',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(4*ee*complex(0,1)*G*I130x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'complex(0,1)*G**2*I130x55',
                 order = {'QCD':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(8*ee**2*complex(0,1)*I129x63)/9. + (8*ee**2*complex(0,1)*I130x63)/9.',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(4*ee*complex(0,1)*G*I129x63)/3. + (4*ee*complex(0,1)*G*I130x63)/3.',
                 order = {'QCD':1,'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'complex(0,1)*G**2*I129x63 + complex(0,1)*G**2*I130x63',
                 order = {'QCD':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(8*ee**2*complex(0,1)*I129x66)/9. + (8*ee**2*complex(0,1)*I130x66)/9.',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(4*ee*complex(0,1)*G*I129x66)/3. + (4*ee*complex(0,1)*G*I130x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'complex(0,1)*G**2*I129x66 + complex(0,1)*G**2*I130x66',
                 order = {'QCD':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*complex(0,1)*I45x11)/3.',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(complex(0,1)*G*I45x11)',
                 order = {'QCD':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*I45x22)/3.',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(complex(0,1)*G*I45x22)',
                 order = {'QCD':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee*complex(0,1)*I45x33)/3. + (ee*complex(0,1)*I46x33)/3.',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(complex(0,1)*G*I45x33) - complex(0,1)*G*I46x33',
                 order = {'QCD':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1)*I45x36)/3. + (ee*complex(0,1)*I46x36)/3.',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(complex(0,1)*G*I45x36) - complex(0,1)*G*I46x36',
                 order = {'QCD':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ee*complex(0,1)*I46x44)/3.',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(complex(0,1)*G*I46x44)',
                 order = {'QCD':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(ee*complex(0,1)*I46x55)/3.',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(complex(0,1)*G*I46x55)',
                 order = {'QCD':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(ee*complex(0,1)*I45x63)/3. - (ee*complex(0,1)*I46x63)/3.',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'complex(0,1)*G*I45x63 + complex(0,1)*G*I46x63',
                 order = {'QCD':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*I45x66)/3. + (ee*complex(0,1)*I46x66)/3.',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(complex(0,1)*G*I45x66) - complex(0,1)*G*I46x66',
                 order = {'QCD':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(2*ee**2*complex(0,1)*I52x11)/9.',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '(-2*ee*complex(0,1)*G*I52x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'complex(0,1)*G**2*I52x11',
                 order = {'QCD':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(2*ee**2*complex(0,1)*I52x22)/9.',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(-2*ee*complex(0,1)*G*I52x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'complex(0,1)*G**2*I52x22',
                 order = {'QCD':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(2*ee**2*complex(0,1)*I52x33)/9. + (2*ee**2*complex(0,1)*I53x33)/9.',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(-2*ee*complex(0,1)*G*I52x33)/3. - (2*ee*complex(0,1)*G*I53x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'complex(0,1)*G**2*I52x33 + complex(0,1)*G**2*I53x33',
                 order = {'QCD':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(2*ee**2*complex(0,1)*I52x36)/9. + (2*ee**2*complex(0,1)*I53x36)/9.',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(-2*ee*complex(0,1)*G*I52x36)/3. - (2*ee*complex(0,1)*G*I53x36)/3.',
                 order = {'QCD':1,'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'complex(0,1)*G**2*I52x36 + complex(0,1)*G**2*I53x36',
                 order = {'QCD':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(2*ee**2*complex(0,1)*I53x44)/9.',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(-2*ee*complex(0,1)*G*I53x44)/3.',
                 order = {'QCD':1,'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'complex(0,1)*G**2*I53x44',
                 order = {'QCD':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(2*ee**2*complex(0,1)*I53x55)/9.',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(-2*ee*complex(0,1)*G*I53x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'complex(0,1)*G**2*I53x55',
                 order = {'QCD':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(2*ee**2*complex(0,1)*I52x63)/9. + (2*ee**2*complex(0,1)*I53x63)/9.',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(-2*ee*complex(0,1)*G*I52x63)/3. - (2*ee*complex(0,1)*G*I53x63)/3.',
                 order = {'QCD':1,'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'complex(0,1)*G**2*I52x63 + complex(0,1)*G**2*I53x63',
                 order = {'QCD':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(2*ee**2*complex(0,1)*I52x66)/9. + (2*ee**2*complex(0,1)*I53x66)/9.',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(-2*ee*complex(0,1)*G*I52x66)/3. - (2*ee*complex(0,1)*G*I53x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'complex(0,1)*G**2*I52x66 + complex(0,1)*G**2*I53x66',
                 order = {'QCD':2})

GC_90 = Coupling(name = 'GC_90',
                 value = 'ee*complex(0,1)*I79x11',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'ee*complex(0,1)*I79x22',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'ee*complex(0,1)*I79x33 + ee*complex(0,1)*I80x33',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'ee*complex(0,1)*I79x36 + ee*complex(0,1)*I80x36',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'ee*complex(0,1)*I80x44',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'ee*complex(0,1)*I80x55',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(ee*complex(0,1)*I79x63) - ee*complex(0,1)*I80x63',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = 'ee*complex(0,1)*I79x66 + ee*complex(0,1)*I80x66',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '2*ee**2*complex(0,1)*I83x11',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '2*ee**2*complex(0,1)*I83x22',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '2*ee**2*complex(0,1)*I83x33 + 2*ee**2*complex(0,1)*I84x33',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '2*ee**2*complex(0,1)*I83x36 + 2*ee**2*complex(0,1)*I84x36',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '2*ee**2*complex(0,1)*I84x44',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '2*ee**2*complex(0,1)*I84x55',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '2*ee**2*complex(0,1)*I83x63 + 2*ee**2*complex(0,1)*I84x63',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '2*ee**2*complex(0,1)*I83x66 + 2*ee**2*complex(0,1)*I84x66',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(complex(0,1)*G*I89x33)/(2.*MP) + (complex(0,1)*G*I91x33)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(complex(0,1)*G*I89x36)/(2.*MP) + (complex(0,1)*G*I91x36)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(complex(0,1)*G*I89x63)/(2.*MP) + (complex(0,1)*G*I91x63)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(complex(0,1)*G*I89x66)/(2.*MP) + (complex(0,1)*G*I91x66)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(complex(0,1)*G*I93x33)/(2.*MP) + (complex(0,1)*G*I94x33)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(complex(0,1)*G*I93x36)/(2.*MP) + (complex(0,1)*G*I94x36)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(complex(0,1)*G*I93x63)/(2.*MP) + (complex(0,1)*G*I94x63)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(complex(0,1)*G*I93x66)/(2.*MP) + (complex(0,1)*G*I94x66)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((G*I89x33)/(M32*MP*cmath.sqrt(6))) + (G*I91x33)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((G*I89x36)/(M32*MP*cmath.sqrt(6))) + (G*I91x36)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((G*I89x63)/(M32*MP*cmath.sqrt(6))) + (G*I91x63)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((G*I89x66)/(M32*MP*cmath.sqrt(6))) + (G*I91x66)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((G*I93x33)/(M32*MP*cmath.sqrt(6))) + (G*I94x33)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((G*I93x36)/(M32*MP*cmath.sqrt(6))) + (G*I94x36)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((G*I93x63)/(M32*MP*cmath.sqrt(6))) + (G*I94x63)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((G*I93x66)/(M32*MP*cmath.sqrt(6))) + (G*I94x66)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '1/(2.*MP)',
                  order = {'QGR':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(complex(0,1)*G)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(complex(0,1)*G*I89x11)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(complex(0,1)*G*I89x22)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(complex(0,1)*G*I91x44)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(complex(0,1)*G*I91x55)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(complex(0,1)*G*I93x11)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(complex(0,1)*G*I93x22)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(complex(0,1)*G*I94x44)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(complex(0,1)*G*I94x55)/(2.*MP)',
                  order = {'QCD':1,'QGR':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(complex(0,1)/(M32*MP*cmath.sqrt(6)))',
                  order = {'QGR':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(G/(M32*MP*cmath.sqrt(6)))',
                  order = {'QCD':1,'QGR':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((G*I89x11)/(M32*MP*cmath.sqrt(6)))',
                  order = {'QCD':1,'QGR':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((G*I89x22)/(M32*MP*cmath.sqrt(6)))',
                  order = {'QCD':1,'QGR':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(G*I91x44)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(G*I91x55)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((G*I93x11)/(M32*MP*cmath.sqrt(6)))',
                  order = {'QCD':1,'QGR':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((G*I93x22)/(M32*MP*cmath.sqrt(6)))',
                  order = {'QCD':1,'QGR':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(G*I94x44)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(G*I94x55)/(M32*MP*cmath.sqrt(6))',
                  order = {'QCD':1,'QGR':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-(complex(0,1)*G*Rd1x1*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((complex(0,1)*Rd1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(complex(0,1)*Rd1x1*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee*complex(0,1)*Rd1x1)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(ee*complex(0,1)*Rd1x1*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*G*Rd1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(complex(0,1)*G*Rd1x1*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_149 = Coupling(name = 'GC_149',
                  value = 'Rd1x1/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ee*Rd1x1)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(G*Rd1x1)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(complex(0,1)*G*Rd2x2*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*Rd2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(complex(0,1)*Rd2x2*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ee*complex(0,1)*Rd2x2)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(ee*complex(0,1)*Rd2x2*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((complex(0,1)*G*Rd2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(complex(0,1)*G*Rd2x2*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_159 = Coupling(name = 'GC_159',
                  value = 'Rd2x2/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(ee*Rd2x2)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(G*Rd2x2)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(complex(0,1)*G*Rd3x3*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*Rd3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(complex(0,1)*Rd3x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(ee*complex(0,1)*Rd3x3)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(ee*complex(0,1)*Rd3x3*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*G*Rd3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(complex(0,1)*G*Rd3x3*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_169 = Coupling(name = 'GC_169',
                  value = 'Rd3x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-(ee*Rd3x3)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '(G*Rd3x3)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_172 = Coupling(name = 'GC_172',
                  value = 'complex(0,1)*G*Rd3x6*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(complex(0,1)*Rd3x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((complex(0,1)*Rd3x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-(ee*complex(0,1)*Rd3x6)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(ee*complex(0,1)*Rd3x6*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(complex(0,1)*G*Rd3x6)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((complex(0,1)*G*Rd3x6*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-Rd3x6/(2.*M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee*Rd3x6)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((G*Rd3x6)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_182 = Coupling(name = 'GC_182',
                  value = 'complex(0,1)*G*Rd4x4*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(complex(0,1)*Rd4x4)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((complex(0,1)*Rd4x4*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-(ee*complex(0,1)*Rd4x4)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee*complex(0,1)*Rd4x4*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(complex(0,1)*G*Rd4x4)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((complex(0,1)*G*Rd4x4*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-Rd4x4/(2.*M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(ee*Rd4x4)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((G*Rd4x4)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_192 = Coupling(name = 'GC_192',
                  value = 'complex(0,1)*G*Rd5x5*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(complex(0,1)*Rd5x5)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((complex(0,1)*Rd5x5*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(ee*complex(0,1)*Rd5x5)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(ee*complex(0,1)*Rd5x5*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(complex(0,1)*G*Rd5x5)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((complex(0,1)*G*Rd5x5*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-Rd5x5/(2.*M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee*Rd5x5)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((G*Rd5x5)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(complex(0,1)*G*Rd6x3*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((complex(0,1)*Rd6x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(complex(0,1)*Rd6x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee*complex(0,1)*Rd6x3)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-(ee*complex(0,1)*Rd6x3*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((complex(0,1)*G*Rd6x3)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(complex(0,1)*G*Rd6x3*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_209 = Coupling(name = 'GC_209',
                  value = 'Rd6x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-(ee*Rd6x3)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(G*Rd6x3)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'complex(0,1)*G*Rd6x6*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(complex(0,1)*Rd6x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((complex(0,1)*Rd6x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(ee*complex(0,1)*Rd6x6)/(3.*MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*Rd6x6*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(complex(0,1)*G*Rd6x6)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-((complex(0,1)*G*Rd6x6*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-Rd6x6/(2.*M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(ee*Rd6x6)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((G*Rd6x6)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((complex(0,1)*Rl1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(complex(0,1)*Rl1x1*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(ee*complex(0,1)*Rl1x1)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((ee*complex(0,1)*Rl1x1*cmath.sqrt(2))/MP)',
                  order = {'QED':1,'QGR':1})

GC_226 = Coupling(name = 'GC_226',
                  value = 'Rl1x1/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((ee*Rl1x1)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QED':1,'QGR':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((complex(0,1)*Rl2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(complex(0,1)*Rl2x2*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(ee*complex(0,1)*Rl2x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((ee*complex(0,1)*Rl2x2*cmath.sqrt(2))/MP)',
                  order = {'QED':1,'QGR':1})

GC_232 = Coupling(name = 'GC_232',
                  value = 'Rl2x2/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((ee*Rl2x2)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QED':1,'QGR':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '-((complex(0,1)*Rl3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(complex(0,1)*Rl3x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(ee*complex(0,1)*Rl3x3)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((ee*complex(0,1)*Rl3x3*cmath.sqrt(2))/MP)',
                  order = {'QED':1,'QGR':1})

GC_238 = Coupling(name = 'GC_238',
                  value = 'Rl3x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-((ee*Rl3x3)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QED':1,'QGR':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(complex(0,1)*Rl3x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((complex(0,1)*Rl3x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((ee*complex(0,1)*Rl3x6)/(MP*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(ee*complex(0,1)*Rl3x6*cmath.sqrt(2))/MP',
                  order = {'QED':1,'QGR':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(Rl3x6/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(ee*Rl3x6)/(M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(complex(0,1)*Rl4x4)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((complex(0,1)*Rl4x4*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((ee*complex(0,1)*Rl4x4)/(MP*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(ee*complex(0,1)*Rl4x4*cmath.sqrt(2))/MP',
                  order = {'QED':1,'QGR':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(Rl4x4/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(ee*Rl4x4)/(M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '(complex(0,1)*Rl5x5)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((complex(0,1)*Rl5x5*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-((ee*complex(0,1)*Rl5x5)/(MP*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '(ee*complex(0,1)*Rl5x5*cmath.sqrt(2))/MP',
                  order = {'QED':1,'QGR':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-(Rl5x5/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '(ee*Rl5x5)/(M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '-((complex(0,1)*Rl6x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '(complex(0,1)*Rl6x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '(ee*complex(0,1)*Rl6x3)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '-((ee*complex(0,1)*Rl6x3*cmath.sqrt(2))/MP)',
                  order = {'QED':1,'QGR':1})

GC_262 = Coupling(name = 'GC_262',
                  value = 'Rl6x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '-((ee*Rl6x3)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QED':1,'QGR':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(complex(0,1)*Rl6x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-((complex(0,1)*Rl6x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-((ee*complex(0,1)*Rl6x6)/(MP*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(ee*complex(0,1)*Rl6x6*cmath.sqrt(2))/MP',
                  order = {'QED':1,'QGR':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-(Rl6x6/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '(ee*Rl6x6)/(M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((complex(0,1)*Rn1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '(complex(0,1)*Rn1x1*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-(Rn1x1/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '-((complex(0,1)*Rn2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(complex(0,1)*Rn2x2*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-(Rn2x2/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((complex(0,1)*Rn3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '(complex(0,1)*Rn3x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-(Rn3x3/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-(complex(0,1)*G*Ru1x1*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-((complex(0,1)*Ru1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '(complex(0,1)*Ru1x1*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '-(ee*complex(0,1)*Ru1x1*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '-((complex(0,1)*G*Ru1x1)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '(complex(0,1)*G*Ru1x1*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_285 = Coupling(name = 'GC_285',
                  value = 'Ru1x1/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '(2*ee*Ru1x1)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '(G*Ru1x1)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '-(complex(0,1)*G*Ru2x2*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((complex(0,1)*Ru2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '(complex(0,1)*Ru2x2*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '-(ee*complex(0,1)*Ru2x2*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '-((complex(0,1)*G*Ru2x2)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '(complex(0,1)*G*Ru2x2*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_294 = Coupling(name = 'GC_294',
                  value = 'Ru2x2/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '(2*ee*Ru2x2)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '(G*Ru2x2)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '-(complex(0,1)*G*Ru3x3*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '-((complex(0,1)*Ru3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '(complex(0,1)*Ru3x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '-(ee*complex(0,1)*Ru3x3*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '-((complex(0,1)*G*Ru3x3)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '(complex(0,1)*G*Ru3x3*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_303 = Coupling(name = 'GC_303',
                  value = 'Ru3x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '(2*ee*Ru3x3)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '(G*Ru3x3)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_306 = Coupling(name = 'GC_306',
                  value = 'complex(0,1)*G*Ru3x6*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '(complex(0,1)*Ru3x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '-((complex(0,1)*Ru3x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '(ee*complex(0,1)*Ru3x6*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '(complex(0,1)*G*Ru3x6)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '-((complex(0,1)*G*Ru3x6*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-(Ru3x6/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '(-2*ee*Ru3x6)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-((G*Ru3x6)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_315 = Coupling(name = 'GC_315',
                  value = 'complex(0,1)*G*Ru4x4*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '(complex(0,1)*Ru4x4)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-((complex(0,1)*Ru4x4*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ee*complex(0,1)*Ru4x4*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '(complex(0,1)*G*Ru4x4)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-((complex(0,1)*G*Ru4x4*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-(Ru4x4/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(-2*ee*Ru4x4)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-((G*Ru4x4)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_324 = Coupling(name = 'GC_324',
                  value = 'complex(0,1)*G*Ru5x5*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(complex(0,1)*Ru5x5)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-((complex(0,1)*Ru5x5*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(ee*complex(0,1)*Ru5x5*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '(complex(0,1)*G*Ru5x5)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '-((complex(0,1)*G*Ru5x5*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '-(Ru5x5/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(-2*ee*Ru5x5)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '-((G*Ru5x5)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-(complex(0,1)*G*Ru6x3*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((complex(0,1)*Ru6x3)/(MP*cmath.sqrt(2)))',
                  order = {'QGR':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '(complex(0,1)*Ru6x3*cmath.sqrt(2))/MP',
                  order = {'QGR':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '-(ee*complex(0,1)*Ru6x3*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-((complex(0,1)*G*Ru6x3)/(MP*cmath.sqrt(2)))',
                  order = {'QCD':1,'QGR':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(complex(0,1)*G*Ru6x3*cmath.sqrt(2))/MP',
                  order = {'QCD':1,'QGR':1})

GC_339 = Coupling(name = 'GC_339',
                  value = 'Ru6x3/(M32*MP*cmath.sqrt(3))',
                  order = {'QGR':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(2*ee*Ru6x3)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(G*Ru6x3)/(M32*MP*cmath.sqrt(3))',
                  order = {'QCD':1,'QGR':1})

GC_342 = Coupling(name = 'GC_342',
                  value = 'complex(0,1)*G*Ru6x6*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(complex(0,1)*Ru6x6)/(MP*cmath.sqrt(2))',
                  order = {'QGR':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '-((complex(0,1)*Ru6x6*cmath.sqrt(2))/MP)',
                  order = {'QGR':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '(ee*complex(0,1)*Ru6x6*cmath.sqrt(2))/(3.*MP)',
                  order = {'QED':1,'QGR':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '(complex(0,1)*G*Ru6x6)/(MP*cmath.sqrt(2))',
                  order = {'QCD':1,'QGR':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '-((complex(0,1)*G*Ru6x6*cmath.sqrt(2))/MP)',
                  order = {'QCD':1,'QGR':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '-(Ru6x6/(M32*MP*cmath.sqrt(3)))',
                  order = {'QGR':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '(-2*ee*Ru6x6)/(3.*M32*MP*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '-((G*Ru6x6)/(M32*MP*cmath.sqrt(3)))',
                  order = {'QCD':1,'QGR':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '(ee**2*complex(0,1)*I161x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(ee**2*complex(0,1)*I161x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(ee**2*complex(0,1)*I161x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(ee**2*complex(0,1)*I161x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '(ee**2*complex(0,1)*I161x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_359 = Coupling(name = 'GC_359',
                  value = '(ee**2*complex(0,1)*I161x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_360 = Coupling(name = 'GC_360',
                  value = '(ee**2*complex(0,1)*I162x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = '(ee**2*complex(0,1)*I162x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_362 = Coupling(name = 'GC_362',
                  value = '(ee**2*complex(0,1)*I162x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_363 = Coupling(name = 'GC_363',
                  value = '(ee**2*complex(0,1)*I162x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(ee**2*complex(0,1)*I162x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(ee**2*complex(0,1)*I162x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '(ee**2*complex(0,1)*I1x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(ee**2*complex(0,1)*I1x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(ee**2*complex(0,1)*I1x33)/(2.*sw**2)',
                  order = {'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(ee**2*complex(0,1)*I1x36)/(2.*sw**2)',
                  order = {'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(ee**2*complex(0,1)*I1x63)/(2.*sw**2)',
                  order = {'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(ee**2*complex(0,1)*I1x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '-((ee**2*complex(0,1)*I101x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '-((ee**2*complex(0,1)*I101x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '-((ee**2*complex(0,1)*I101x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '-((ee**2*complex(0,1)*I101x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(ee**2*complex(0,1)*I110x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(ee*complex(0,1)*G*I110x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ee**2*complex(0,1)*I110x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(ee*complex(0,1)*G*I110x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(ee**2*complex(0,1)*I110x33)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(ee*complex(0,1)*G*I110x33*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(ee**2*complex(0,1)*I110x36)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(ee*complex(0,1)*G*I110x36*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(ee**2*complex(0,1)*I110x63)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '(ee*complex(0,1)*G*I110x63*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(ee**2*complex(0,1)*I110x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '(ee*complex(0,1)*G*I110x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(ee**2*complex(0,1)*I121x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(ee*complex(0,1)*G*I121x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '(ee**2*complex(0,1)*I121x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_397 = Coupling(name = 'GC_397',
                  value = '(ee*complex(0,1)*G*I121x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(ee**2*complex(0,1)*I121x33)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '(ee*complex(0,1)*G*I121x33*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '(ee**2*complex(0,1)*I121x36)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '(ee*complex(0,1)*G*I121x36*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(ee**2*complex(0,1)*I121x63)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(ee*complex(0,1)*G*I121x63*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '(ee**2*complex(0,1)*I121x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_405 = Coupling(name = 'GC_405',
                  value = '(ee*complex(0,1)*G*I121x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '-((ee*complex(0,1)*I155x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '-((ee*complex(0,1)*I155x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-((ee*complex(0,1)*I155x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '-((ee*complex(0,1)*I155x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-((ee*complex(0,1)*I155x63)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '-((ee*complex(0,1)*I155x66)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '-((ee*complex(0,1)*I156x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '-((ee*complex(0,1)*I156x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((ee*complex(0,1)*I156x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_415 = Coupling(name = 'GC_415',
                  value = '-((ee*complex(0,1)*I156x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '(ee*complex(0,1)*I157x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '(ee*complex(0,1)*I157x22)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '(ee*complex(0,1)*I157x33)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '(ee*complex(0,1)*I157x36)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(ee*complex(0,1)*I157x63)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '(ee*complex(0,1)*I157x66)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '(ee*complex(0,1)*I158x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '(ee*complex(0,1)*I158x22)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '(ee*complex(0,1)*I158x33)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(ee*complex(0,1)*I158x36)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-((ee**2*complex(0,1)*I95x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '-((ee**2*complex(0,1)*I95x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '-((ee**2*complex(0,1)*I95x33)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '-((ee**2*complex(0,1)*I95x36)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '-(ee*complex(0,1)*I118x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '-(ee*complex(0,1)*I118x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '-(ee*complex(0,1)*I118x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '-(ee*complex(0,1)*I118x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(ee*complex(0,1)*I145x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(ee*complex(0,1)*I145x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(ee*complex(0,1)*I145x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(ee*complex(0,1)*I145x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '(ee*complex(0,1)*I148x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '(ee*complex(0,1)*I148x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '(ee*complex(0,1)*I148x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '(ee*complex(0,1)*I148x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '(ee*complex(0,1)*I159x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(ee*complex(0,1)*I159x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '(ee*complex(0,1)*I159x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(ee*complex(0,1)*I160x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '(ee*complex(0,1)*I160x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '(ee*complex(0,1)*I160x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '(ee*complex(0,1)*I160x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-(ee*complex(0,1)*I47x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '-(ee*complex(0,1)*I47x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-(ee*complex(0,1)*I47x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '-(ee*complex(0,1)*I47x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '-(ee*complex(0,1)*I81x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '-(ee*complex(0,1)*I81x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '-(ee*complex(0,1)*I81x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '-(ee*complex(0,1)*I81x36)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-(ee*complex(0,1)*I99x11)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '-(ee*complex(0,1)*I99x22)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-(ee*complex(0,1)*I99x33)/(2.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '(ee*I118x11)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '(ee*I118x22)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '(ee*I118x33)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '(ee*I118x36)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '(ee*I145x11*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((ee*I145x11)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(ee*I145x22*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((ee*I145x22)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '(ee*I145x33*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-((ee*I145x33)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '(ee*I145x36*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-((ee*I145x36)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '(ee*I148x11*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-((ee*I148x11)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '(ee*I148x22*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((ee*I148x22)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '(ee*I148x33*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '-((ee*I148x33)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '(ee*I148x36*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '-((ee*I148x36)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '(ee*I159x11*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((ee*I159x11)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '(ee*I159x22*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((ee*I159x22)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '(ee*I159x33*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((ee*I159x33)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(ee*I160x11*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-((ee*I160x11)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ee*I160x22*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((ee*I160x22)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(ee*I160x33*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-((ee*I160x33)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(ee*I160x36*cmath.sqrt(0.6666666666666666))/(M32*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-((ee*I160x36)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ee*I47x11)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '(ee*I47x22)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(ee*I47x33)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(ee*I47x36)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ee*I81x11)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(ee*I81x22)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ee*I81x33)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(ee*I81x36)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ee*I99x11)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(ee*I99x22)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(ee*I99x33)/(M32*MP*sw*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '-(ee*NN1x2)/(4.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '-((ee*complex(0,1)*NN1x2)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '-(ee*NN2x2)/(4.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '-((ee*complex(0,1)*NN2x2)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '-(ee*NN3x2)/(4.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '-((ee*complex(0,1)*NN3x2)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-(ee*NN4x2)/(4.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '-((ee*complex(0,1)*NN4x2)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '-((cw*ee**2*complex(0,1)*I3x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((cw*ee**2*complex(0,1)*I3x22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_515 = Coupling(name = 'GC_515',
                  value = '-((cw*ee**2*complex(0,1)*I3x33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '-((cw*ee**2*complex(0,1)*I3x36)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_517 = Coupling(name = 'GC_517',
                  value = '(cw*ee**2*complex(0,1)*I4x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '(cw*ee**2*complex(0,1)*I4x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(cw*ee**2*complex(0,1)*I4x33)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_520 = Coupling(name = 'GC_520',
                  value = '(cw*ee**2*complex(0,1)*I4x36)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_521 = Coupling(name = 'GC_521',
                  value = '(cw*ee**2*complex(0,1)*I4x63)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '(cw*ee**2*complex(0,1)*I4x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((cw*ee**2*complex(0,1)*I5x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '-((cw*ee**2*complex(0,1)*I5x22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((cw*ee**2*complex(0,1)*I5x33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '-((cw*ee**2*complex(0,1)*I5x36)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '(cw*ee**2*complex(0,1)*I6x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '(cw*ee**2*complex(0,1)*I6x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_529 = Coupling(name = 'GC_529',
                  value = '(cw*ee**2*complex(0,1)*I6x33)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_530 = Coupling(name = 'GC_530',
                  value = '(cw*ee**2*complex(0,1)*I6x36)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '(cw*ee**2*complex(0,1)*I6x63)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_532 = Coupling(name = 'GC_532',
                  value = '(cw*ee**2*complex(0,1)*I6x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_533 = Coupling(name = 'GC_533',
                  value = '-(cw*ee*complex(0,1)*I140x44*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '-(cw*ee*complex(0,1)*I140x55*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '-(cw*ee*complex(0,1)*I91x44*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '-(cw*ee*complex(0,1)*I91x55*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(cw*ee*complex(0,1)*I94x44*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(cw*ee*complex(0,1)*I94x55*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '-((cw*ee*I140x44*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '-((cw*ee*I140x55*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '-(cw*ee*I91x44*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '-(cw*ee*I91x55*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(cw*ee*I94x44*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(cw*ee*I94x55*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '-(cw*ee*complex(0,1)*I140x44*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '-(cw*ee*complex(0,1)*I140x55*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '-(cw*ee*complex(0,1)*I91x44*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '-(cw*ee*complex(0,1)*I91x55*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '(cw*ee*complex(0,1)*I94x44*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(cw*ee*complex(0,1)*I94x55*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((cw*ee*I140x44*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '-((cw*ee*I140x55*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '-(cw*ee*I91x44*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '-(cw*ee*I91x55*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(cw*ee*I94x44*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(cw*ee*I94x55*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '-(cw*ee*complex(0,1)*I140x44*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '-(cw*ee*complex(0,1)*I140x55*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-(cw*ee*complex(0,1)*I91x44*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '-(cw*ee*complex(0,1)*I91x55*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '(cw*ee*complex(0,1)*I94x44*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(cw*ee*complex(0,1)*I94x55*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '-((cw*ee*I140x44*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '-((cw*ee*I140x55*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '-(cw*ee*I91x44*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '-(cw*ee*I91x55*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '(cw*ee*I94x44*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(cw*ee*I94x55*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '-(cw*ee*complex(0,1)*I140x44*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '-(cw*ee*complex(0,1)*I140x55*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '-(cw*ee*complex(0,1)*I91x44*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '-(cw*ee*complex(0,1)*I91x55*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '(cw*ee*complex(0,1)*I94x44*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '(cw*ee*complex(0,1)*I94x55*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_575 = Coupling(name = 'GC_575',
                  value = '-((cw*ee*I140x44*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_576 = Coupling(name = 'GC_576',
                  value = '-((cw*ee*I140x55*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_577 = Coupling(name = 'GC_577',
                  value = '-(cw*ee*I91x44*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_578 = Coupling(name = 'GC_578',
                  value = '-(cw*ee*I91x55*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_579 = Coupling(name = 'GC_579',
                  value = '(cw*ee*I94x44*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '(cw*ee*I94x55*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_581 = Coupling(name = 'GC_581',
                  value = '(cw*ee*complex(0,1)*NN1x1*Rd4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '(cw*ee*complex(0,1)*NN2x1*Rd4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '(cw*ee*complex(0,1)*NN3x1*Rd4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '(cw*ee*complex(0,1)*NN4x1*Rd4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_585 = Coupling(name = 'GC_585',
                  value = '(cw*ee*complex(0,1)*NN1x1*Rd5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_586 = Coupling(name = 'GC_586',
                  value = '(cw*ee*complex(0,1)*NN2x1*Rd5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_587 = Coupling(name = 'GC_587',
                  value = '(cw*ee*complex(0,1)*NN3x1*Rd5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_588 = Coupling(name = 'GC_588',
                  value = '(cw*ee*complex(0,1)*NN4x1*Rd5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_589 = Coupling(name = 'GC_589',
                  value = '(cw*ee*complex(0,1)*NN1x1*Rl4x4*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_590 = Coupling(name = 'GC_590',
                  value = '(cw*ee*complex(0,1)*NN2x1*Rl4x4*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_591 = Coupling(name = 'GC_591',
                  value = '(cw*ee*complex(0,1)*NN3x1*Rl4x4*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_592 = Coupling(name = 'GC_592',
                  value = '(cw*ee*complex(0,1)*NN4x1*Rl4x4*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '(cw*ee*complex(0,1)*NN1x1*Rl5x5*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '(cw*ee*complex(0,1)*NN2x1*Rl5x5*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '(cw*ee*complex(0,1)*NN3x1*Rl5x5*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_596 = Coupling(name = 'GC_596',
                  value = '(cw*ee*complex(0,1)*NN4x1*Rl5x5*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_597 = Coupling(name = 'GC_597',
                  value = '(-2*cw*ee*complex(0,1)*NN1x1*Ru4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '(-2*cw*ee*complex(0,1)*NN2x1*Ru4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_599 = Coupling(name = 'GC_599',
                  value = '(-2*cw*ee*complex(0,1)*NN3x1*Ru4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '(-2*cw*ee*complex(0,1)*NN4x1*Ru4x4*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_601 = Coupling(name = 'GC_601',
                  value = '(-2*cw*ee*complex(0,1)*NN1x1*Ru5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '(-2*cw*ee*complex(0,1)*NN2x1*Ru5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '(-2*cw*ee*complex(0,1)*NN3x1*Ru5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '(-2*cw*ee*complex(0,1)*NN4x1*Ru5x5*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '-(cw*ee*complex(0,1)*Rd1x1)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '-(cw*ee*complex(0,1)*Rd2x2)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(cw*ee*complex(0,1)*Rd3x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(cw*ee*complex(0,1)*Rd6x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(cw*ee*complex(0,1)*Rl1x1)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '-(cw*ee*complex(0,1)*Rl2x2)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '-(cw*ee*complex(0,1)*Rl3x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '-(cw*ee*complex(0,1)*Rl6x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_616 = Coupling(name = 'GC_616',
                  value = '(cw*ee*complex(0,1)*Rn1x1)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_617 = Coupling(name = 'GC_617',
                  value = '-(cw*ee*Rn1x1)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_618 = Coupling(name = 'GC_618',
                  value = '(cw*ee*complex(0,1)*Rn2x2)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(cw*ee*Rn2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_620 = Coupling(name = 'GC_620',
                  value = '(cw*ee*complex(0,1)*Rn3x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(cw*ee*Rn3x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_622 = Coupling(name = 'GC_622',
                  value = '-(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_623 = Coupling(name = 'GC_623',
                  value = '(2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_624 = Coupling(name = 'GC_624',
                  value = '-((cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw)))',
                  order = {'QED':1})

GC_625 = Coupling(name = 'GC_625',
                  value = '(2*cw*ee**2*complex(0,1)*I51x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '(-2*cw*ee*complex(0,1)*G*I51x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_627 = Coupling(name = 'GC_627',
                  value = '(2*cw*ee**2*complex(0,1)*I51x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '(-2*cw*ee*complex(0,1)*G*I51x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_629 = Coupling(name = 'GC_629',
                  value = '(2*cw*ee**2*complex(0,1)*I55x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(2*cw*ee**2*complex(0,1)*I55x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(8*cw*ee**2*complex(0,1)*I58x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(4*cw*ee*complex(0,1)*G*I58x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '(8*cw*ee**2*complex(0,1)*I58x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(4*cw*ee*complex(0,1)*G*I58x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_635 = Coupling(name = 'GC_635',
                  value = '(cw*ee*complex(0,1)*I69x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_636 = Coupling(name = 'GC_636',
                  value = '(cw*ee*complex(0,1)*I69x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(cw*ee*complex(0,1)*I71x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '(cw*ee*complex(0,1)*I71x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '(-2*cw*ee*complex(0,1)*I72x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '(-2*cw*ee*complex(0,1)*I72x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_641 = Coupling(name = 'GC_641',
                  value = '(cw*ee*complex(0,1)*Rd1x1*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(cw*ee*complex(0,1)*Rd1x1*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cw*ee*complex(0,1)*Rd2x2*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(cw*ee*complex(0,1)*Rd2x2*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cw*ee*complex(0,1)*Rd3x3*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_646 = Coupling(name = 'GC_646',
                  value = '-(cw*ee*complex(0,1)*Rd3x3*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '-(cw*ee*complex(0,1)*Rd3x6*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_648 = Coupling(name = 'GC_648',
                  value = '(cw*ee*complex(0,1)*Rd3x6*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_649 = Coupling(name = 'GC_649',
                  value = '(cw*ee*Rd3x6*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_650 = Coupling(name = 'GC_650',
                  value = '-(cw*ee*complex(0,1)*Rd4x4*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '(cw*ee*complex(0,1)*Rd4x4*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_652 = Coupling(name = 'GC_652',
                  value = '(cw*ee*Rd4x4*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '-(cw*ee*complex(0,1)*Rd5x5*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_654 = Coupling(name = 'GC_654',
                  value = '(cw*ee*complex(0,1)*Rd5x5*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '(cw*ee*Rd5x5*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '(cw*ee*complex(0,1)*Rd6x3*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '-(cw*ee*complex(0,1)*Rd6x3*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '-(cw*ee*complex(0,1)*Rd6x6*sw)/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '(cw*ee*complex(0,1)*Rd6x6*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cw*ee*Rd6x6*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cw*ee*complex(0,1)*Rl1x1*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '-((cw*ee*complex(0,1)*Rl1x1*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw)))',
                  order = {'QED':1,'QGR':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cw*ee*complex(0,1)*Rl2x2*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '-((cw*ee*complex(0,1)*Rl2x2*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw)))',
                  order = {'QED':1,'QGR':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cw*ee*complex(0,1)*Rl3x3*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '-((cw*ee*complex(0,1)*Rl3x3*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw)))',
                  order = {'QED':1,'QGR':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '-((cw*ee*complex(0,1)*Rl3x6*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cw*ee*complex(0,1)*Rl3x6*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '(cw*ee*Rl3x6*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '-((cw*ee*complex(0,1)*Rl4x4*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cw*ee*complex(0,1)*Rl4x4*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cw*ee*Rl4x4*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '-((cw*ee*complex(0,1)*Rl5x5*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cw*ee*complex(0,1)*Rl5x5*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cw*ee*Rl5x5*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cw*ee*complex(0,1)*Rl6x3*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '-((cw*ee*complex(0,1)*Rl6x3*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw)))',
                  order = {'QED':1,'QGR':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '-((cw*ee*complex(0,1)*Rl6x6*sw)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':1,'QGR':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cw*ee*complex(0,1)*Rl6x6*sw*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '(cw*ee*Rl6x6*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(cw*ee*complex(0,1)*Ru3x6*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '(-2*cw*ee*Ru3x6*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cw*ee*complex(0,1)*Ru4x4*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '(-2*cw*ee*Ru4x4*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cw*ee*complex(0,1)*Ru5x5*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '(-2*cw*ee*Ru5x5*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '(cw*ee*complex(0,1)*Ru6x6*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '(-2*cw*ee*Ru6x6*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(-2*ee**2*complex(0,1)*I69x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_690 = Coupling(name = 'GC_690',
                  value = '(-2*ee**2*complex(0,1)*I69x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(-2*ee**2*complex(0,1)*I71x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(-2*ee**2*complex(0,1)*I71x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(-8*ee**2*complex(0,1)*I72x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '(-8*ee**2*complex(0,1)*I72x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '-(cw*NN1x1)/(2.*MP) - (NN1x2*sw)/(2.*MP)',
                  order = {'QGR':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '(cw*complex(0,1)*NN1x1)/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN1x2*sw)/(M32*MP*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '-(cw*NN2x1)/(2.*MP) - (NN2x2*sw)/(2.*MP)',
                  order = {'QGR':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '(cw*complex(0,1)*NN2x1)/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN2x2*sw)/(M32*MP*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(cw*NN3x1)/(2.*MP) - (NN3x2*sw)/(2.*MP)',
                  order = {'QGR':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '(cw*complex(0,1)*NN3x1)/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN3x2*sw)/(M32*MP*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '-(cw*NN4x1)/(2.*MP) - (NN4x2*sw)/(2.*MP)',
                  order = {'QGR':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '(cw*complex(0,1)*NN4x1)/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN4x2*sw)/(M32*MP*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '(cw*ee*complex(0,1)*I1x11)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I1x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '(cw*ee*complex(0,1)*I1x22)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I1x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(cw*ee**2*complex(0,1)*I50x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '(cw*ee*complex(0,1)*G*I50x11)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '-(cw*ee**2*complex(0,1)*I50x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cw*ee*complex(0,1)*G*I50x22)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '-(cw*ee**2*complex(0,1)*I50x33)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x33*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I51x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '(cw*ee*complex(0,1)*G*I50x33)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x33*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I51x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(cw*ee**2*complex(0,1)*I50x36)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x36*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I51x36*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '(cw*ee*complex(0,1)*G*I50x36)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x36*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I51x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '-(cw*ee**2*complex(0,1)*I50x63)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x63*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I51x63*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '(cw*ee*complex(0,1)*G*I50x63)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x63*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I51x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '-(cw*ee**2*complex(0,1)*I50x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I50x66*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I51x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '(cw*ee*complex(0,1)*G*I50x66)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I50x66*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I51x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '-((cw*ee**2*complex(0,1)*I54x11)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((cw*ee**2*complex(0,1)*I54x22)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '-((cw*ee**2*complex(0,1)*I54x33)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x33*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I55x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '-((cw*ee**2*complex(0,1)*I54x36)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x36*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I55x36*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '-((cw*ee**2*complex(0,1)*I54x63)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x63*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I55x63*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '-((cw*ee**2*complex(0,1)*I54x66)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I54x66*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I55x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '-((cw*ee*complex(0,1)*G*I57x11)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_725 = Coupling(name = 'GC_725',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '-((cw*ee*complex(0,1)*G*I57x22)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x33)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x33*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I58x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '-((cw*ee*complex(0,1)*G*I57x33)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x33*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I58x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x36)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x36*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I58x36*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '-((cw*ee*complex(0,1)*G*I57x36)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x36*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I58x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x63)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x63*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I58x63*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '-((cw*ee*complex(0,1)*G*I57x63)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x63*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I58x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '(-2*cw*ee**2*complex(0,1)*I57x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I57x66*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I58x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_734 = Coupling(name = 'GC_734',
                  value = '-((cw*ee*complex(0,1)*G*I57x66)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I57x66*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I58x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '-(cw*ee*complex(0,1)*I68x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I68x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '-(cw*ee*complex(0,1)*I68x22)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I68x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '-(cw*ee*complex(0,1)*I68x33)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I68x33*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I69x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '-(cw*ee*complex(0,1)*I68x36)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I68x36*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I69x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '(cw*ee*complex(0,1)*I68x63)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I68x63*sw)/(3.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I69x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '-(cw*ee*complex(0,1)*I68x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I68x66*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I69x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '-(cw*ee*complex(0,1)*I70x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I70x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '-(cw*ee*complex(0,1)*I70x22)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I70x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '-(cw*ee*complex(0,1)*I70x33)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I70x33*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I71x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '-(cw*ee*complex(0,1)*I70x36)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I70x36*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I71x36*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '(cw*ee*complex(0,1)*I70x63)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I70x63*sw)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I71x63*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '-(cw*ee*complex(0,1)*I70x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I70x66*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I71x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_747 = Coupling(name = 'GC_747',
                  value = '(cw*ee*complex(0,1)*I1x33)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I1x33*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I72x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_748 = Coupling(name = 'GC_748',
                  value = '(cw*ee*complex(0,1)*I1x36)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I1x36*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I72x36*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '-(cw*ee*complex(0,1)*I1x63)/(2.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee*complex(0,1)*I1x63*sw)/(3.*(-1 + sw)*(1 + sw)) + (2*cw*ee*complex(0,1)*I72x63*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '(cw*ee*complex(0,1)*I1x66)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I1x66*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I72x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cw*ee*complex(0,1)*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '(cw*ee*complex(0,1)*I139x11*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x11*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x11*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(cw*ee*complex(0,1)*I139x22*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x22*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x22*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '-(cw*ee*complex(0,1)*I89x11*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x11*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x11*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_755 = Coupling(name = 'GC_755',
                  value = '-(cw*ee*complex(0,1)*I89x22*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x22*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x22*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_756 = Coupling(name = 'GC_756',
                  value = '-(cw*ee*complex(0,1)*I93x11*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x11*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x11*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_757 = Coupling(name = 'GC_757',
                  value = '-(cw*ee*complex(0,1)*I93x22*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x22*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x22*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '(cw*ee*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '(cw*ee*I139x11*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '(cw*ee*I139x22*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_761 = Coupling(name = 'GC_761',
                  value = '-(cw*ee*I89x11*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '-(cw*ee*I89x22*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_763 = Coupling(name = 'GC_763',
                  value = '-(cw*ee*I93x11*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_764 = Coupling(name = 'GC_764',
                  value = '-(cw*ee*I93x22*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_765 = Coupling(name = 'GC_765',
                  value = '(cw*ee*complex(0,1)*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_766 = Coupling(name = 'GC_766',
                  value = '(cw*ee*complex(0,1)*I139x11*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x11*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x11*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_767 = Coupling(name = 'GC_767',
                  value = '(cw*ee*complex(0,1)*I139x22*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x22*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x22*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_768 = Coupling(name = 'GC_768',
                  value = '-(cw*ee*complex(0,1)*I89x11*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x11*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x11*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_769 = Coupling(name = 'GC_769',
                  value = '-(cw*ee*complex(0,1)*I89x22*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x22*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x22*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(cw*ee*complex(0,1)*I93x11*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x11*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x11*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_771 = Coupling(name = 'GC_771',
                  value = '-(cw*ee*complex(0,1)*I93x22*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x22*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x22*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '(cw*ee*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_773 = Coupling(name = 'GC_773',
                  value = '(cw*ee*I139x11*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_774 = Coupling(name = 'GC_774',
                  value = '(cw*ee*I139x22*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '-(cw*ee*I89x11*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '-(cw*ee*I89x22*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(cw*ee*I93x11*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '-(cw*ee*I93x22*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '(cw*ee*complex(0,1)*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '(cw*ee*complex(0,1)*I139x11*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x11*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x11*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '(cw*ee*complex(0,1)*I139x22*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x22*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x22*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '-(cw*ee*complex(0,1)*I89x11*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x11*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x11*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '-(cw*ee*complex(0,1)*I89x22*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x22*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x22*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '-(cw*ee*complex(0,1)*I93x11*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x11*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x11*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '-(cw*ee*complex(0,1)*I93x22*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x22*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x22*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '(cw*ee*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cw*ee*I139x11*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '(cw*ee*I139x22*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '-(cw*ee*I89x11*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '-(cw*ee*I89x22*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '-(cw*ee*I93x11*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '-(cw*ee*I93x22*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cw*ee*complex(0,1)*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cw*ee*complex(0,1)*I139x11*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x11*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x11*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '(cw*ee*complex(0,1)*I139x22*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x22*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x22*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '-(cw*ee*complex(0,1)*I89x11*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x11*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x11*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-(cw*ee*complex(0,1)*I89x22*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x22*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x22*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '-(cw*ee*complex(0,1)*I93x11*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x11*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x11*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '-(cw*ee*complex(0,1)*I93x22*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x22*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x22*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_800 = Coupling(name = 'GC_800',
                  value = '(cw*ee*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '(cw*ee*I139x11*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_802 = Coupling(name = 'GC_802',
                  value = '(cw*ee*I139x22*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_803 = Coupling(name = 'GC_803',
                  value = '-(cw*ee*I89x11*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_804 = Coupling(name = 'GC_804',
                  value = '-(cw*ee*I89x22*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '-(cw*ee*I93x11*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '-(cw*ee*I93x22*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_807 = Coupling(name = 'GC_807',
                  value = '(cw*ee*Rd1x1)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rd1x1*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_808 = Coupling(name = 'GC_808',
                  value = '(cw*ee*Rd2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rd2x2*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_809 = Coupling(name = 'GC_809',
                  value = '(cw*ee*Rd3x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rd3x3*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '(cw*ee*Rd6x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rd6x3*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '(cw*ee*Rl1x1)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rl1x1*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_812 = Coupling(name = 'GC_812',
                  value = '(cw*ee*Rl2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rl2x2*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cw*ee*Rl3x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rl3x3*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_814 = Coupling(name = 'GC_814',
                  value = '(cw*ee*Rl6x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*Rl6x3*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '(cw*ee*complex(0,1)*Ru1x1)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*Ru1x1*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '-(cw*ee*Ru1x1)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (2*cw*ee*Ru1x1*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_817 = Coupling(name = 'GC_817',
                  value = '(cw*ee*complex(0,1)*Ru2x2)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*Ru2x2*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_818 = Coupling(name = 'GC_818',
                  value = '-(cw*ee*Ru2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (2*cw*ee*Ru2x2*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_819 = Coupling(name = 'GC_819',
                  value = '(cw*ee*complex(0,1)*Ru3x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*Ru3x3*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '-(cw*ee*Ru3x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (2*cw*ee*Ru3x3*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_821 = Coupling(name = 'GC_821',
                  value = '(cw*ee*complex(0,1)*Ru6x3)/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*Ru6x3*sw*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QED':1,'QGR':1})

GC_822 = Coupling(name = 'GC_822',
                  value = '-(cw*ee*Ru6x3)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (2*cw*ee*Ru6x3*sw)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_823 = Coupling(name = 'GC_823',
                  value = '(4*ee**2*complex(0,1)*I1x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '(4*ee**2*complex(0,1)*I1x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '(2*ee**2*complex(0,1)*I68x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '(2*ee**2*complex(0,1)*I68x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '(2*ee**2*complex(0,1)*I68x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x33*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I69x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '(2*ee**2*complex(0,1)*I68x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x36*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I69x36*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(2*ee**2*complex(0,1)*I68x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x63*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I69x63*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '(2*ee**2*complex(0,1)*I68x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I68x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I68x66*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I69x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '(2*ee**2*complex(0,1)*I70x11)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(2*ee**2*complex(0,1)*I70x22)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '(2*ee**2*complex(0,1)*I70x33)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x33*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I71x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '(2*ee**2*complex(0,1)*I70x36)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x36*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I71x36*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '(2*ee**2*complex(0,1)*I70x63)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x63*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I71x63*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '(2*ee**2*complex(0,1)*I70x66)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I70x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I70x66*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I71x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '(4*ee**2*complex(0,1)*I1x33)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x33)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x33*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I72x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '(4*ee**2*complex(0,1)*I1x36)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x36)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x36*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I72x36*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '(4*ee**2*complex(0,1)*I1x63)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x63)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x63*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I72x63*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '(4*ee**2*complex(0,1)*I1x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I1x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I1x66*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I72x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(complex(0,1)*I32x33*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x33*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rd3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_842 = Coupling(name = 'GC_842',
                  value = '(complex(0,1)*I32x36*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x36*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rd6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_843 = Coupling(name = 'GC_843',
                  value = '(complex(0,1)*I36x33*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x33*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rl3x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_844 = Coupling(name = 'GC_844',
                  value = '(complex(0,1)*I36x36*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x36*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*Rl6x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_845 = Coupling(name = 'GC_845',
                  value = '-(cw*ee*complex(0,1)*I89x33*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x33*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x33*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x33*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x33*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x33*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_846 = Coupling(name = 'GC_846',
                  value = '-(cw*ee*complex(0,1)*I89x36*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x36*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x36*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x36*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x36*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x36*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_847 = Coupling(name = 'GC_847',
                  value = '-(cw*ee*complex(0,1)*I89x63*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x63*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x63*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x63*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x63*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x63*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_848 = Coupling(name = 'GC_848',
                  value = '-(cw*ee*complex(0,1)*I89x66*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x66*NN1x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x66*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x66*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x66*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x66*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_849 = Coupling(name = 'GC_849',
                  value = '(cw*ee*complex(0,1)*I139x33*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x33*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x33*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x33*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x33*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x33*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_850 = Coupling(name = 'GC_850',
                  value = '(cw*ee*complex(0,1)*I139x36*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x36*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x36*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x36*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x36*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x36*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_851 = Coupling(name = 'GC_851',
                  value = '(cw*ee*complex(0,1)*I139x63*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x63*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x63*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x63*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x63*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x63*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_852 = Coupling(name = 'GC_852',
                  value = '(cw*ee*complex(0,1)*I139x66*NN1x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x66*NN1x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x66*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x66*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x66*NN1x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x66*NN1x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_853 = Coupling(name = 'GC_853',
                  value = '-((I138x33*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x33*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x33*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x33*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_854 = Coupling(name = 'GC_854',
                  value = '-((I138x36*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x36*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x36*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x36*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((I138x63*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x63*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x63*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x63*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_856 = Coupling(name = 'GC_856',
                  value = '-((I138x66*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x66*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x66*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x66*NN1x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_857 = Coupling(name = 'GC_857',
                  value = '-((I142x33*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x33*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x33*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x33*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_858 = Coupling(name = 'GC_858',
                  value = '-((I142x36*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x36*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x36*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x36*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((I142x63*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x63*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x63*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x63*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_860 = Coupling(name = 'GC_860',
                  value = '-((I142x66*NN1x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x66*NN1x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x66*NN1x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x66*NN1x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_861 = Coupling(name = 'GC_861',
                  value = '(complex(0,1)*I40x33*NN1x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x33*NN1x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN1x1*Ru3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_862 = Coupling(name = 'GC_862',
                  value = '(complex(0,1)*I40x36*NN1x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x36*NN1x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN1x1*Ru6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_863 = Coupling(name = 'GC_863',
                  value = '-(cw*ee*complex(0,1)*I93x33*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x33*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x33*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x33*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x33*NN1x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x33*NN1x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_864 = Coupling(name = 'GC_864',
                  value = '-(cw*ee*complex(0,1)*I93x36*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x36*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x36*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x36*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x36*NN1x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x36*NN1x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_865 = Coupling(name = 'GC_865',
                  value = '-(cw*ee*complex(0,1)*I93x63*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x63*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x63*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x63*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x63*NN1x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x63*NN1x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_866 = Coupling(name = 'GC_866',
                  value = '-(cw*ee*complex(0,1)*I93x66*NN1x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x66*NN1x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x66*NN1x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x66*NN1x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x66*NN1x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x66*NN1x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cw*ee*I94x33*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x33*NN1x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x33*NN1x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x33*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_868 = Coupling(name = 'GC_868',
                  value = '(cw*ee*I94x36*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x36*NN1x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x36*NN1x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x36*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_869 = Coupling(name = 'GC_869',
                  value = '(cw*ee*I94x63*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x63*NN1x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x63*NN1x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x63*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_870 = Coupling(name = 'GC_870',
                  value = '(cw*ee*I94x66*NN1x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x66*NN1x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x66*NN1x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x66*NN1x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*NN1x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*NN1x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_871 = Coupling(name = 'GC_871',
                  value = '(complex(0,1)*I32x33*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x33*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rd3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_872 = Coupling(name = 'GC_872',
                  value = '(complex(0,1)*I32x36*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x36*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rd6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_873 = Coupling(name = 'GC_873',
                  value = '(complex(0,1)*I36x33*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x33*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rl3x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_874 = Coupling(name = 'GC_874',
                  value = '(complex(0,1)*I36x36*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x36*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*Rl6x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_875 = Coupling(name = 'GC_875',
                  value = '-(cw*ee*complex(0,1)*I89x33*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x33*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x33*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x33*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x33*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x33*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_876 = Coupling(name = 'GC_876',
                  value = '-(cw*ee*complex(0,1)*I89x36*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x36*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x36*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x36*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x36*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x36*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_877 = Coupling(name = 'GC_877',
                  value = '-(cw*ee*complex(0,1)*I89x63*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x63*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x63*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x63*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x63*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x63*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '-(cw*ee*complex(0,1)*I89x66*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x66*NN2x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x66*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x66*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x66*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x66*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cw*ee*complex(0,1)*I139x33*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x33*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x33*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x33*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x33*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x33*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cw*ee*complex(0,1)*I139x36*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x36*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x36*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x36*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x36*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x36*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_881 = Coupling(name = 'GC_881',
                  value = '(cw*ee*complex(0,1)*I139x63*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x63*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x63*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x63*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x63*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x63*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cw*ee*complex(0,1)*I139x66*NN2x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x66*NN2x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x66*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x66*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x66*NN2x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x66*NN2x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_883 = Coupling(name = 'GC_883',
                  value = '-((I138x33*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x33*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x33*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x33*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_884 = Coupling(name = 'GC_884',
                  value = '-((I138x36*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x36*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x36*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x36*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_885 = Coupling(name = 'GC_885',
                  value = '-((I138x63*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x63*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x63*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x63*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((I138x66*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x66*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x66*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x66*NN2x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((I142x33*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x33*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x33*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x33*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_888 = Coupling(name = 'GC_888',
                  value = '-((I142x36*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x36*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x36*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x36*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_889 = Coupling(name = 'GC_889',
                  value = '-((I142x63*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x63*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x63*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x63*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_890 = Coupling(name = 'GC_890',
                  value = '-((I142x66*NN2x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x66*NN2x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x66*NN2x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x66*NN2x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_891 = Coupling(name = 'GC_891',
                  value = '(complex(0,1)*I40x33*NN2x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x33*NN2x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN2x1*Ru3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_892 = Coupling(name = 'GC_892',
                  value = '(complex(0,1)*I40x36*NN2x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x36*NN2x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN2x1*Ru6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_893 = Coupling(name = 'GC_893',
                  value = '-(cw*ee*complex(0,1)*I93x33*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x33*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x33*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x33*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x33*NN2x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x33*NN2x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_894 = Coupling(name = 'GC_894',
                  value = '-(cw*ee*complex(0,1)*I93x36*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x36*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x36*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x36*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x36*NN2x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x36*NN2x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_895 = Coupling(name = 'GC_895',
                  value = '-(cw*ee*complex(0,1)*I93x63*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x63*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x63*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x63*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x63*NN2x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x63*NN2x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_896 = Coupling(name = 'GC_896',
                  value = '-(cw*ee*complex(0,1)*I93x66*NN2x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x66*NN2x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x66*NN2x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x66*NN2x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x66*NN2x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x66*NN2x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_897 = Coupling(name = 'GC_897',
                  value = '(cw*ee*I94x33*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x33*NN2x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x33*NN2x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x33*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_898 = Coupling(name = 'GC_898',
                  value = '(cw*ee*I94x36*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x36*NN2x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x36*NN2x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x36*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_899 = Coupling(name = 'GC_899',
                  value = '(cw*ee*I94x63*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x63*NN2x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x63*NN2x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x63*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_900 = Coupling(name = 'GC_900',
                  value = '(cw*ee*I94x66*NN2x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x66*NN2x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x66*NN2x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x66*NN2x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*NN2x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*NN2x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_901 = Coupling(name = 'GC_901',
                  value = '(complex(0,1)*I32x33*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x33*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rd3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_902 = Coupling(name = 'GC_902',
                  value = '(complex(0,1)*I32x36*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x36*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rd6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_903 = Coupling(name = 'GC_903',
                  value = '(complex(0,1)*I36x33*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x33*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rl3x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_904 = Coupling(name = 'GC_904',
                  value = '(complex(0,1)*I36x36*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x36*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*Rl6x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_905 = Coupling(name = 'GC_905',
                  value = '-(cw*ee*complex(0,1)*I89x33*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x33*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x33*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x33*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x33*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x33*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_906 = Coupling(name = 'GC_906',
                  value = '-(cw*ee*complex(0,1)*I89x36*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x36*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x36*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x36*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x36*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x36*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_907 = Coupling(name = 'GC_907',
                  value = '-(cw*ee*complex(0,1)*I89x63*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x63*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x63*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x63*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x63*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x63*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_908 = Coupling(name = 'GC_908',
                  value = '-(cw*ee*complex(0,1)*I89x66*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x66*NN3x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x66*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x66*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x66*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x66*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_909 = Coupling(name = 'GC_909',
                  value = '(cw*ee*complex(0,1)*I139x33*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x33*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x33*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x33*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x33*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x33*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_910 = Coupling(name = 'GC_910',
                  value = '(cw*ee*complex(0,1)*I139x36*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x36*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x36*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x36*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x36*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x36*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cw*ee*complex(0,1)*I139x63*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x63*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x63*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x63*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x63*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x63*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_912 = Coupling(name = 'GC_912',
                  value = '(cw*ee*complex(0,1)*I139x66*NN3x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x66*NN3x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x66*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x66*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x66*NN3x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x66*NN3x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_913 = Coupling(name = 'GC_913',
                  value = '-((I138x33*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x33*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x33*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x33*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((I138x36*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x36*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x36*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x36*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_915 = Coupling(name = 'GC_915',
                  value = '-((I138x63*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x63*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x63*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x63*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((I138x66*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x66*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x66*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x66*NN3x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((I142x33*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x33*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x33*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x33*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((I142x36*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x36*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x36*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x36*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_919 = Coupling(name = 'GC_919',
                  value = '-((I142x63*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x63*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x63*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x63*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_920 = Coupling(name = 'GC_920',
                  value = '-((I142x66*NN3x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x66*NN3x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x66*NN3x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x66*NN3x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_921 = Coupling(name = 'GC_921',
                  value = '(complex(0,1)*I40x33*NN3x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x33*NN3x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN3x1*Ru3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_922 = Coupling(name = 'GC_922',
                  value = '(complex(0,1)*I40x36*NN3x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x36*NN3x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN3x1*Ru6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_923 = Coupling(name = 'GC_923',
                  value = '-(cw*ee*complex(0,1)*I93x33*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x33*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x33*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x33*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x33*NN3x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x33*NN3x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_924 = Coupling(name = 'GC_924',
                  value = '-(cw*ee*complex(0,1)*I93x36*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x36*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x36*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x36*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x36*NN3x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x36*NN3x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_925 = Coupling(name = 'GC_925',
                  value = '-(cw*ee*complex(0,1)*I93x63*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x63*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x63*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x63*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x63*NN3x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x63*NN3x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_926 = Coupling(name = 'GC_926',
                  value = '-(cw*ee*complex(0,1)*I93x66*NN3x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x66*NN3x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x66*NN3x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x66*NN3x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x66*NN3x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x66*NN3x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_927 = Coupling(name = 'GC_927',
                  value = '(cw*ee*I94x33*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x33*NN3x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x33*NN3x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x33*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_928 = Coupling(name = 'GC_928',
                  value = '(cw*ee*I94x36*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x36*NN3x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x36*NN3x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x36*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_929 = Coupling(name = 'GC_929',
                  value = '(cw*ee*I94x63*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x63*NN3x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x63*NN3x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x63*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_930 = Coupling(name = 'GC_930',
                  value = '(cw*ee*I94x66*NN3x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x66*NN3x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x66*NN3x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x66*NN3x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*NN3x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*NN3x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_931 = Coupling(name = 'GC_931',
                  value = '(complex(0,1)*I32x33*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x33*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rd3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_932 = Coupling(name = 'GC_932',
                  value = '(complex(0,1)*I32x36*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I32x36*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rd6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_933 = Coupling(name = 'GC_933',
                  value = '(complex(0,1)*I36x33*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x33*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rl3x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '(complex(0,1)*I36x36*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I36x36*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*Rl6x6*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_935 = Coupling(name = 'GC_935',
                  value = '-(cw*ee*complex(0,1)*I89x33*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x33*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x33*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x33*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x33*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x33*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_936 = Coupling(name = 'GC_936',
                  value = '-(cw*ee*complex(0,1)*I89x36*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x36*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x36*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x36*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x36*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x36*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_937 = Coupling(name = 'GC_937',
                  value = '-(cw*ee*complex(0,1)*I89x63*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x63*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x63*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x63*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x63*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x63*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_938 = Coupling(name = 'GC_938',
                  value = '-(cw*ee*complex(0,1)*I89x66*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I91x66*NN4x1)/(6.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I89x66*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I89x66*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I138x66*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I138x66*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_939 = Coupling(name = 'GC_939',
                  value = '(cw*ee*complex(0,1)*I139x33*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x33*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x33*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x33*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x33*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x33*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_940 = Coupling(name = 'GC_940',
                  value = '(cw*ee*complex(0,1)*I139x36*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x36*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x36*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x36*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x36*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x36*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_941 = Coupling(name = 'GC_941',
                  value = '(cw*ee*complex(0,1)*I139x63*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x63*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x63*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x63*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x63*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x63*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_942 = Coupling(name = 'GC_942',
                  value = '(cw*ee*complex(0,1)*I139x66*NN4x1)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I140x66*NN4x1)/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I139x66*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I139x66*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I142x66*NN4x3)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I142x66*NN4x3*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_943 = Coupling(name = 'GC_943',
                  value = '-((I138x33*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x33*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x33*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x33*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((I138x36*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x36*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x36*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x36*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_945 = Coupling(name = 'GC_945',
                  value = '-((I138x63*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x63*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x63*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x63*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_946 = Coupling(name = 'GC_946',
                  value = '-((I138x66*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I138x66*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I89x66*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I91x66*NN4x1)/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((I142x33*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x33*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x33*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x33*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((I142x36*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x36*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x36*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x36*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '-((I142x63*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x63*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x63*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x63*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((I142x66*NN4x3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))) + (I142x66*NN4x3*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I139x66*NN4x1)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*I140x66*NN4x1)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '(complex(0,1)*I40x33*NN4x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x33*NN4x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN4x1*Ru3x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '(complex(0,1)*I40x36*NN4x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I40x36*NN4x4*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN4x1*Ru6x6*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '-(cw*ee*complex(0,1)*I93x33*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x33*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x33*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x33*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x33*NN4x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x33*NN4x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '-(cw*ee*complex(0,1)*I93x36*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x36*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x36*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x36*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x36*NN4x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x36*NN4x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '-(cw*ee*complex(0,1)*I93x63*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x63*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x63*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x63*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x63*NN4x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x63*NN4x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '-(cw*ee*complex(0,1)*I93x66*NN4x1)/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I94x66*NN4x1)/(3.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I93x66*NN4x2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I93x66*NN4x2*sw)/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*I144x66*NN4x4)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I144x66*NN4x4*sw**2)/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '(cw*ee*I94x33*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x33*NN4x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x33*NN4x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x33*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '(cw*ee*I94x36*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x36*NN4x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x36*NN4x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x36*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '(cw*ee*I94x63*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x63*NN4x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x63*NN4x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x63*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '(cw*ee*I94x66*NN4x1*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) - (I144x66*NN4x4)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (I144x66*NN4x4*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I93x66*NN4x1)/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*NN4x2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*NN4x2*sw)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(cw*NN1x2)/(2.*MP*(-1 + sw)*(1 + sw)) - (NN1x1*sw)/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*NN1x2*sw**2)/(2.*MP*(-1 + sw)*(1 + sw)) + (NN1x1*sw**3)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QGR':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((cw*complex(0,1)*NN1x2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*NN1x1*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*NN1x2*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (complex(0,1)*NN1x1*sw**3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '(cw*NN2x2)/(2.*MP*(-1 + sw)*(1 + sw)) - (NN2x1*sw)/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*NN2x2*sw**2)/(2.*MP*(-1 + sw)*(1 + sw)) + (NN2x1*sw**3)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QGR':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '-((cw*complex(0,1)*NN2x2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*NN2x1*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*NN2x2*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (complex(0,1)*NN2x1*sw**3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '(cw*NN3x2)/(2.*MP*(-1 + sw)*(1 + sw)) - (NN3x1*sw)/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*NN3x2*sw**2)/(2.*MP*(-1 + sw)*(1 + sw)) + (NN3x1*sw**3)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QGR':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((cw*complex(0,1)*NN3x2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*NN3x1*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*NN3x2*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (complex(0,1)*NN3x1*sw**3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '(cw*NN4x2)/(2.*MP*(-1 + sw)*(1 + sw)) - (NN4x1*sw)/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*NN4x2*sw**2)/(2.*MP*(-1 + sw)*(1 + sw)) + (NN4x1*sw**3)/(2.*MP*(-1 + sw)*(1 + sw))',
                  order = {'QGR':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((cw*complex(0,1)*NN4x2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*NN4x1*sw)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*NN4x2*sw**2)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (complex(0,1)*NN4x1*sw**3)/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '-UU1x1/(2.*MP)',
                  order = {'QGR':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '(ee*UU1x1)/(2.*MP)',
                  order = {'QED':1,'QGR':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '(complex(0,1)*UU1x1)/(M32*MP*cmath.sqrt(6))',
                  order = {'QGR':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '(ee*complex(0,1)*UU1x1)/(M32*MP*cmath.sqrt(6))',
                  order = {'QED':1,'QGR':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((ee*complex(0,1)*I145x11*UU1x1)/sw)',
                  order = {'QED':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((ee*complex(0,1)*I145x22*UU1x1)/sw)',
                  order = {'QED':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '-((ee*complex(0,1)*I148x11*UU1x1)/sw)',
                  order = {'QED':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((ee*complex(0,1)*I148x22*UU1x1)/sw)',
                  order = {'QED':1})

GC_977 = Coupling(name = 'GC_977',
                  value = '-(cw*ee*UU1x1)/(4.*MP*sw)',
                  order = {'QED':1,'QGR':1})

GC_978 = Coupling(name = 'GC_978',
                  value = '(ee*complex(0,1)*I64x11*UU1x1)/(2.*MP*sw*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '(ee*complex(0,1)*I64x22*UU1x1)/(2.*MP*sw*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '(ee*complex(0,1)*I76x11*UU1x1)/(2.*MP*sw*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '(ee*complex(0,1)*I76x22*UU1x1)/(2.*MP*sw*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((cw*ee*complex(0,1)*UU1x1)/(M32*MP*sw*cmath.sqrt(6)))',
                  order = {'QED':1,'QGR':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '(ee*I64x11*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '(ee*I64x22*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '(ee*I76x11*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '(ee*I76x22*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                  order = {'QED':1,'QGR':1})

GC_987 = Coupling(name = 'GC_987',
                  value = 'complex(0,1)*I100x33*UU1x2',
                  order = {'QED':1})

GC_988 = Coupling(name = 'GC_988',
                  value = 'complex(0,1)*I119x33*UU1x2',
                  order = {'QED':1})

GC_989 = Coupling(name = 'GC_989',
                  value = 'complex(0,1)*I119x36*UU1x2',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((ee*complex(0,1)*I145x33*UU1x1)/sw) + complex(0,1)*I146x33*UU1x2',
                  order = {'QED':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((ee*complex(0,1)*I145x36*UU1x1)/sw) + complex(0,1)*I146x36*UU1x2',
                  order = {'QED':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((ee*complex(0,1)*I148x33*UU1x1)/sw) + complex(0,1)*I149x33*UU1x2',
                  order = {'QED':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((ee*complex(0,1)*I148x36*UU1x1)/sw) + complex(0,1)*I149x36*UU1x2',
                  order = {'QED':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '(ee*complex(0,1)*I64x33*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I65x33*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '(ee*complex(0,1)*I64x36*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I65x36*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '(ee*complex(0,1)*I76x33*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x33*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '(ee*complex(0,1)*I76x36*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x36*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '(ee*complex(0,1)*I76x63*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x63*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '(ee*complex(0,1)*I76x66*UU1x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x66*UU1x2)/(MP*cmath.sqrt(2))',
                  order = {'QED':1,'QGR':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(ee*I64x33*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I65x33*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(ee*I64x36*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I65x36*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(ee*I76x33*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x33*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(ee*I76x36*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x36*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(ee*I76x63*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x63*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(ee*I76x66*UU1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x66*UU1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-UU2x1/(2.*MP)',
                   order = {'QGR':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(ee*UU2x1)/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(complex(0,1)*UU2x1)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(ee*complex(0,1)*UU2x1)/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '-((ee*complex(0,1)*I145x11*UU2x1)/sw)',
                   order = {'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((ee*complex(0,1)*I145x22*UU2x1)/sw)',
                   order = {'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((ee*complex(0,1)*I148x11*UU2x1)/sw)',
                   order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-((ee*complex(0,1)*I148x22*UU2x1)/sw)',
                   order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-(cw*ee*UU2x1)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(ee*complex(0,1)*I64x11*UU2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(ee*complex(0,1)*I64x22*UU2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(ee*complex(0,1)*I76x11*UU2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(ee*complex(0,1)*I76x22*UU2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-((cw*ee*complex(0,1)*UU2x1)/(M32*MP*sw*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(ee*I64x11*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(ee*I64x22*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(ee*I76x11*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(ee*I76x22*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = 'complex(0,1)*I100x33*UU2x2',
                   order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = 'complex(0,1)*I119x33*UU2x2',
                   order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = 'complex(0,1)*I119x36*UU2x2',
                   order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '-((ee*complex(0,1)*I145x33*UU2x1)/sw) + complex(0,1)*I146x33*UU2x2',
                   order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((ee*complex(0,1)*I145x36*UU2x1)/sw) + complex(0,1)*I146x36*UU2x2',
                   order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((ee*complex(0,1)*I148x33*UU2x1)/sw) + complex(0,1)*I149x33*UU2x2',
                   order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((ee*complex(0,1)*I148x36*UU2x1)/sw) + complex(0,1)*I149x36*UU2x2',
                   order = {'QED':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(ee*complex(0,1)*I64x33*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I65x33*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(ee*complex(0,1)*I64x36*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I65x36*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(ee*complex(0,1)*I76x33*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x33*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(ee*complex(0,1)*I76x36*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x36*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(ee*complex(0,1)*I76x63*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x63*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(ee*complex(0,1)*I76x66*UU2x1)/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I78x66*UU2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '(ee*I64x33*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I65x33*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(ee*I64x36*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I65x36*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(ee*I76x33*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x33*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(ee*I76x36*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x36*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '(ee*I76x63*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x63*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '(ee*I76x66*UU2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) - (I78x66*UU2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-(complex(0,1)*I11x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-(complex(0,1)*I11x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(complex(0,1)*I13x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(complex(0,1)*I13x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '-(complex(0,1)*I23x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-(complex(0,1)*I23x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(complex(0,1)*I24x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(complex(0,1)*I24x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-(complex(0,1)*I31x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-(complex(0,1)*I31x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(complex(0,1)*I32x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(complex(0,1)*I32x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-(complex(0,1)*I35x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '-(complex(0,1)*I35x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(complex(0,1)*I36x33*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(complex(0,1)*I36x36*vd)/(2.*MP)',
                   order = {'QGR':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-((I11x33*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((I11x36*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(I13x33*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(I13x36*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((I23x33*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-((I23x36*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(I24x33*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(I24x36*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((I31x33*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-((I31x36*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(I32x33*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(I32x36*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '-((I35x33*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-((I35x36*vd)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(I36x33*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(I36x36*vd)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-(ee*complex(0,1)*UU1x2*vd)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '(ee*UU1x2*vd)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(ee*complex(0,1)*UU2x2*vd)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(ee*UU2x2*vd)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-(complex(0,1)*I25x33*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-(complex(0,1)*I25x36*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(complex(0,1)*I26x33*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(complex(0,1)*I26x36*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-(complex(0,1)*I39x33*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-(complex(0,1)*I39x36*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(complex(0,1)*I40x33*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(complex(0,1)*I40x36*vu)/(2.*MP)',
                   order = {'QGR':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((I25x33*vu)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((I25x36*vu)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '(I26x33*vu)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '(I26x36*vu)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((I39x33*vu)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '-((I39x36*vu)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(I40x33*vu)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(I40x36*vu)/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(cw*ee*complex(0,1)*NN1x3*vd)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4*vu)/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-(cw*ee*NN1x3*vd)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x4*vu)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(cw*ee*complex(0,1)*NN2x3*vd)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4*vu)/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-(cw*ee*NN2x3*vd)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x4*vu)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(cw*ee*complex(0,1)*NN3x3*vd)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4*vu)/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-(cw*ee*NN3x3*vd)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x4*vu)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(cw*ee*complex(0,1)*NN4x3*vd)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4*vu)/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-(cw*ee*NN4x3*vd)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x4*vu)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = 'VV1x1/(2.*MP)',
                   order = {'QGR':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(ee*VV1x1)/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-((complex(0,1)*VV1x1)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '(ee*complex(0,1)*VV1x1)/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '-((ee*complex(0,1)*I150x11*VV1x1)/sw)',
                   order = {'QED':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '-((ee*complex(0,1)*I150x22*VV1x1)/sw)',
                   order = {'QED':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '-((ee*complex(0,1)*I150x33*VV1x1)/sw)',
                   order = {'QED':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '-((ee*complex(0,1)*I152x11*VV1x1)/sw)',
                   order = {'QED':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '-((ee*complex(0,1)*I152x22*VV1x1)/sw)',
                   order = {'QED':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-(cw*ee*VV1x1)/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-(ee*complex(0,1)*I105x11*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '-(ee*complex(0,1)*I105x22*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-(ee*complex(0,1)*I66x11*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-(ee*complex(0,1)*I66x22*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '-(ee*complex(0,1)*I66x33*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-(ee*complex(0,1)*I66x36*VV1x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '-((cw*ee*complex(0,1)*VV1x1)/(M32*MP*sw*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '-(ee*I105x11*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '-(ee*I105x22*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-(ee*I66x11*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '-(ee*I66x22*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-(ee*I66x33*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '-(ee*I66x36*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = 'complex(0,1)*I48x33*VV1x2',
                   order = {'QED':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = 'complex(0,1)*I48x36*VV1x2',
                   order = {'QED':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(ee*complex(0,1)*vu*VV1x2)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(ee*vu*VV1x2)/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-((ee*complex(0,1)*I152x33*VV1x1)/sw) + complex(0,1)*I153x33*VV1x2',
                   order = {'QED':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-((ee*complex(0,1)*I152x36*VV1x1)/sw) + complex(0,1)*I153x36*VV1x2',
                   order = {'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-(ee*complex(0,1)*I105x33*VV1x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x33*VV1x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-(ee*complex(0,1)*I105x36*VV1x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x36*VV1x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-(ee*complex(0,1)*I105x63*VV1x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x63*VV1x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-(ee*complex(0,1)*I105x66*VV1x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x66*VV1x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-(ee*I105x33*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x33*VV1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-(ee*I105x36*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x36*VV1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-(ee*I105x63*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x63*VV1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '-(ee*I105x66*VV1x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x66*VV1x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = 'VV2x1/(2.*MP)',
                   order = {'QGR':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(ee*VV2x1)/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-((complex(0,1)*VV2x1)/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(ee*complex(0,1)*VV2x1)/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-((ee*complex(0,1)*I150x11*VV2x1)/sw)',
                   order = {'QED':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '-((ee*complex(0,1)*I150x22*VV2x1)/sw)',
                   order = {'QED':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((ee*complex(0,1)*I150x33*VV2x1)/sw)',
                   order = {'QED':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((ee*complex(0,1)*I152x11*VV2x1)/sw)',
                   order = {'QED':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-((ee*complex(0,1)*I152x22*VV2x1)/sw)',
                   order = {'QED':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-(cw*ee*VV2x1)/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-(ee*complex(0,1)*I105x11*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-(ee*complex(0,1)*I105x22*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-(ee*complex(0,1)*I66x11*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-(ee*complex(0,1)*I66x22*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-(ee*complex(0,1)*I66x33*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-(ee*complex(0,1)*I66x36*VV2x1)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-((cw*ee*complex(0,1)*VV2x1)/(M32*MP*sw*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '-(ee*I105x11*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '-(ee*I105x22*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '-(ee*I66x11*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '-(ee*I66x22*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '-(ee*I66x33*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '-(ee*I66x36*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1163 = Coupling(name = 'GC_1163',
                   value = 'complex(0,1)*I48x33*VV2x2',
                   order = {'QED':1})

GC_1164 = Coupling(name = 'GC_1164',
                   value = 'complex(0,1)*I48x36*VV2x2',
                   order = {'QED':1})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(ee*complex(0,1)*vu*VV2x2)/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(ee*vu*VV2x2)/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '-((ee*complex(0,1)*I152x33*VV2x1)/sw) + complex(0,1)*I153x33*VV2x2',
                   order = {'QED':1})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '-((ee*complex(0,1)*I152x36*VV2x1)/sw) + complex(0,1)*I153x36*VV2x2',
                   order = {'QED':1})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '-(ee*complex(0,1)*I105x33*VV2x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x33*VV2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '-(ee*complex(0,1)*I105x36*VV2x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x36*VV2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '-(ee*complex(0,1)*I105x63*VV2x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x63*VV2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '-(ee*complex(0,1)*I105x66*VV2x1)/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I106x66*VV2x2)/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '-(ee*I105x33*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x33*VV2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '-(ee*I105x36*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x36*VV2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '-(ee*I105x63*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x63*VV2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '-(ee*I105x66*VV2x1)/(2.*M32*MP*sw*cmath.sqrt(3)) + (I106x66*VV2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '(cw*ee*complex(0,1)*I140x44*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(cw*ee*complex(0,1)*I140x55*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '(cw*ee*complex(0,1)*I91x44*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '(cw*ee*complex(0,1)*I91x55*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-(cw*ee*complex(0,1)*I94x44*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-(cw*ee*complex(0,1)*I94x55*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(cw*ee*I140x44*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '(cw*ee*I140x55*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '(cw*ee*I91x44*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '(cw*ee*I91x55*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-(cw*ee*I94x44*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-(cw*ee*I94x55*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(ee*complexconjugate(NN1x2))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(ee*complex(0,1)*complexconjugate(NN1x2))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cw*complexconjugate(NN1x1))/(2.*MP) + (sw*complexconjugate(NN1x2))/(2.*MP)',
                   order = {'QGR':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '-((cw*complex(0,1)*complexconjugate(NN1x1))/(M32*MP*cmath.sqrt(6))) - (complex(0,1)*sw*complexconjugate(NN1x2))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '-(cw*ee*complex(0,1)*I139x11*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x11*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x11*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '-(cw*ee*complex(0,1)*I139x22*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x22*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x22*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(cw*ee*complex(0,1)*I89x11*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x11*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x11*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cw*ee*complex(0,1)*I89x22*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x22*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x22*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(cw*ee*complex(0,1)*I93x11*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x11*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x11*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(cw*ee*complex(0,1)*I93x22*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x22*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x22*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '-(cw*ee*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '-(cw*ee*I139x11*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '-(cw*ee*I139x22*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cw*ee*I89x11*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(cw*ee*I89x22*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(cw*ee*I93x11*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(cw*ee*I93x22*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(cw*ee*complex(0,1)*Rd1x1*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd1x1*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd1x1*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(cw*ee*complex(0,1)*Rd2x2*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd2x2*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd2x2*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '-((cw*ee*complex(0,1)*Rl1x1*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl1x1*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl1x1*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '-((cw*ee*complex(0,1)*Rl2x2*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl2x2*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl2x2*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '-((cw*ee*complex(0,1)*Rn1x1*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn1x1*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn1x1*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '-((cw*ee*complex(0,1)*Rn2x2*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn2x2*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn2x2*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '-((cw*ee*complex(0,1)*Rn3x3*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn3x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn3x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(cw*ee*complex(0,1)*Ru1x1*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru1x1*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru1x1*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(cw*ee*complex(0,1)*Ru2x2*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru2x2*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru2x2*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(sw*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (sw**3*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*complexconjugate(NN1x2))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*sw**2*complexconjugate(NN1x2))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '-((complex(0,1)*sw*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*sw**3*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*complexconjugate(NN1x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*complex(0,1)*sw**2*complexconjugate(NN1x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(complex(0,1)*I31x33*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x33*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd3x3*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd3x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd3x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(complex(0,1)*I31x36*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x36*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd6x3*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd6x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd6x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(complex(0,1)*I35x33*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x33*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl3x3*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl3x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl3x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(complex(0,1)*I35x36*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x36*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl6x3*complexconjugate(NN1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl6x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl6x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(cw*ee*complex(0,1)*I89x33*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x33*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x33*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x33*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x33*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x33*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(cw*ee*complex(0,1)*I89x36*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x36*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x36*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x36*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x36*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x36*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(cw*ee*complex(0,1)*I89x63*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x63*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x63*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x63*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x63*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x63*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(cw*ee*complex(0,1)*I89x66*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x66*complexconjugate(NN1x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x66*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x66*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x66*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x66*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '-(cw*ee*complex(0,1)*I139x33*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x33*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x33*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x33*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x33*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x33*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '-(cw*ee*complex(0,1)*I139x36*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x36*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x36*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x36*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x36*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x36*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '-(cw*ee*complex(0,1)*I139x63*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x63*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x63*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x63*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x63*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x63*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-(cw*ee*complex(0,1)*I139x66*complexconjugate(NN1x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x66*complexconjugate(NN1x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x66*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x66*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x66*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x66*sw**2*complexconjugate(NN1x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '(I137x33*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x33*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x33*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x33*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '(I137x36*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x36*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x36*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x36*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '(I137x63*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x63*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x63*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x63*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '(I137x66*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x66*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x66*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x66*complexconjugate(NN1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '(I141x33*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x33*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x33*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x33*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '(I141x36*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x36*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x36*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x36*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '(I141x63*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x63*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x63*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x63*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '(I141x66*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x66*sw**2*complexconjugate(NN1x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x66*complexconjugate(NN1x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x66*complexconjugate(NN1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '-((ee*complex(0,1)*UU1x1*complexconjugate(NN1x2))/sw) - (ee*complex(0,1)*UU1x2*complexconjugate(NN1x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-((ee*complex(0,1)*UU2x1*complexconjugate(NN1x2))/sw) - (ee*complex(0,1)*UU2x2*complexconjugate(NN1x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '-(cw*ee*complex(0,1)*NN1x3*complexconjugate(NN1x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*complexconjugate(NN1x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '(cw*ee*complex(0,1)*NN2x3*complexconjugate(NN1x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4*complexconjugate(NN1x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(cw*ee*complex(0,1)*NN3x3*complexconjugate(NN1x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4*complexconjugate(NN1x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '(cw*ee*complex(0,1)*NN4x3*complexconjugate(NN1x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4*complexconjugate(NN1x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(complex(0,1)*I39x33*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*sw**2*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru3x3*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru3x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru3x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '(complex(0,1)*I39x36*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*sw**2*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru6x3*complexconjugate(NN1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru6x3*complexconjugate(NN1x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru6x3*sw*complexconjugate(NN1x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(cw*ee*complex(0,1)*I93x33*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x33*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x33*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x33*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x33*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x33*sw**2*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '(cw*ee*complex(0,1)*I93x36*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x36*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x36*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x36*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x36*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x36*sw**2*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(cw*ee*complex(0,1)*I93x63*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x63*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x63*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x63*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x63*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x63*sw**2*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '(cw*ee*complex(0,1)*I93x66*complexconjugate(NN1x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x66*complexconjugate(NN1x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x66*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x66*sw*complexconjugate(NN1x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x66*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x66*sw**2*complexconjugate(NN1x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-(cw*ee*I94x33*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x33*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x33*sw**2*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x33*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-(cw*ee*I94x36*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x36*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x36*sw**2*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x36*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '-(cw*ee*I94x63*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x63*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x63*sw**2*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x63*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-(cw*ee*I94x66*complexconjugate(NN1x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x66*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x66*sw**2*complexconjugate(NN1x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x66*complexconjugate(NN1x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*sw*complexconjugate(NN1x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(cw*ee*complex(0,1)*vd*complexconjugate(NN1x3))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*vu*complexconjugate(NN1x4))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-(cw*ee*vd*complexconjugate(NN1x3))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN1x4))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '-((ee*complex(0,1)*VV1x1*complexconjugate(NN1x2))/sw) + (ee*complex(0,1)*VV1x2*complexconjugate(NN1x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-((ee*complex(0,1)*VV2x1*complexconjugate(NN1x2))/sw) + (ee*complex(0,1)*VV2x2*complexconjugate(NN1x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(cw*ee*complex(0,1)*I140x44*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '(cw*ee*complex(0,1)*I140x55*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '(cw*ee*complex(0,1)*I91x44*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '(cw*ee*complex(0,1)*I91x55*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '-(cw*ee*complex(0,1)*I94x44*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-(cw*ee*complex(0,1)*I94x55*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(cw*ee*I140x44*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '(cw*ee*I140x55*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '(cw*ee*I91x44*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '(cw*ee*I91x55*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '-(cw*ee*I94x44*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-(cw*ee*I94x55*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(ee*complexconjugate(NN2x2))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(ee*complex(0,1)*complexconjugate(NN2x2))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '(cw*complexconjugate(NN2x1))/(2.*MP) + (sw*complexconjugate(NN2x2))/(2.*MP)',
                   order = {'QGR':1})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-((cw*complex(0,1)*complexconjugate(NN2x1))/(M32*MP*cmath.sqrt(6))) - (complex(0,1)*sw*complexconjugate(NN2x2))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-(cw*ee*complex(0,1)*I139x11*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x11*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x11*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-(cw*ee*complex(0,1)*I139x22*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x22*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x22*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '(cw*ee*complex(0,1)*I89x11*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x11*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x11*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '(cw*ee*complex(0,1)*I89x22*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x22*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x22*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '(cw*ee*complex(0,1)*I93x11*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x11*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x11*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(cw*ee*complex(0,1)*I93x22*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x22*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x22*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-(cw*ee*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '-(cw*ee*I139x11*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-(cw*ee*I139x22*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '(cw*ee*I89x11*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '(cw*ee*I89x22*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(cw*ee*I93x11*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '(cw*ee*I93x22*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '(cw*ee*complex(0,1)*Rd1x1*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd1x1*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd1x1*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '(cw*ee*complex(0,1)*Rd2x2*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd2x2*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd2x2*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-((cw*ee*complex(0,1)*Rl1x1*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl1x1*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl1x1*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-((cw*ee*complex(0,1)*Rl2x2*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl2x2*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl2x2*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '-((cw*ee*complex(0,1)*Rn1x1*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn1x1*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn1x1*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-((cw*ee*complex(0,1)*Rn2x2*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn2x2*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn2x2*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '-((cw*ee*complex(0,1)*Rn3x3*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn3x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn3x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '(cw*ee*complex(0,1)*Ru1x1*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru1x1*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru1x1*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '(cw*ee*complex(0,1)*Ru2x2*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru2x2*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru2x2*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '(sw*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (sw**3*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*complexconjugate(NN2x2))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*sw**2*complexconjugate(NN2x2))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '-((complex(0,1)*sw*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*sw**3*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*complexconjugate(NN2x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*complex(0,1)*sw**2*complexconjugate(NN2x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '(complex(0,1)*I31x33*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x33*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd3x3*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd3x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd3x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '(complex(0,1)*I31x36*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x36*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd6x3*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd6x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd6x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '(complex(0,1)*I35x33*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x33*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl3x3*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl3x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl3x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '(complex(0,1)*I35x36*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x36*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl6x3*complexconjugate(NN2x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl6x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl6x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '(cw*ee*complex(0,1)*I89x33*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x33*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x33*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x33*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x33*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x33*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '(cw*ee*complex(0,1)*I89x36*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x36*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x36*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x36*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x36*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x36*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '(cw*ee*complex(0,1)*I89x63*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x63*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x63*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x63*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x63*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x63*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '(cw*ee*complex(0,1)*I89x66*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x66*complexconjugate(NN2x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x66*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x66*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x66*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x66*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '-(cw*ee*complex(0,1)*I139x33*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x33*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x33*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x33*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x33*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x33*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '-(cw*ee*complex(0,1)*I139x36*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x36*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x36*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x36*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x36*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x36*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-(cw*ee*complex(0,1)*I139x63*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x63*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x63*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x63*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x63*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x63*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-(cw*ee*complex(0,1)*I139x66*complexconjugate(NN2x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x66*complexconjugate(NN2x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x66*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x66*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x66*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x66*sw**2*complexconjugate(NN2x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '(I137x33*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x33*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x33*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x33*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(I137x36*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x36*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x36*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x36*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '(I137x63*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x63*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x63*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x63*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(I137x66*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x66*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x66*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x66*complexconjugate(NN2x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(I141x33*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x33*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x33*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x33*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(I141x36*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x36*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x36*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x36*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '(I141x63*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x63*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x63*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x63*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(I141x66*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x66*sw**2*complexconjugate(NN2x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x66*complexconjugate(NN2x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x66*complexconjugate(NN2x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-((ee*complex(0,1)*UU1x1*complexconjugate(NN2x2))/sw) - (ee*complex(0,1)*UU1x2*complexconjugate(NN2x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '-((ee*complex(0,1)*UU2x1*complexconjugate(NN2x2))/sw) - (ee*complex(0,1)*UU2x2*complexconjugate(NN2x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-(cw*ee*complex(0,1)*NN1x3*complexconjugate(NN2x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*complexconjugate(NN2x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '-(cw*ee*complex(0,1)*NN2x3*complexconjugate(NN2x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN2x4*complexconjugate(NN2x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '(cw*ee*complex(0,1)*NN3x3*complexconjugate(NN2x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4*complexconjugate(NN2x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(cw*ee*complex(0,1)*NN4x3*complexconjugate(NN2x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4*complexconjugate(NN2x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '(complex(0,1)*I39x33*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*sw**2*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru3x3*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru3x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru3x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(complex(0,1)*I39x36*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*sw**2*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru6x3*complexconjugate(NN2x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru6x3*complexconjugate(NN2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru6x3*sw*complexconjugate(NN2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '(cw*ee*complex(0,1)*I93x33*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x33*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x33*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x33*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x33*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x33*sw**2*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(cw*ee*complex(0,1)*I93x36*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x36*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x36*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x36*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x36*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x36*sw**2*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '(cw*ee*complex(0,1)*I93x63*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x63*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x63*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x63*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x63*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x63*sw**2*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(cw*ee*complex(0,1)*I93x66*complexconjugate(NN2x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x66*complexconjugate(NN2x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x66*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x66*sw*complexconjugate(NN2x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x66*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x66*sw**2*complexconjugate(NN2x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '-(cw*ee*I94x33*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x33*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x33*sw**2*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x33*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '-(cw*ee*I94x36*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x36*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x36*sw**2*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x36*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '-(cw*ee*I94x63*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x63*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x63*sw**2*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x63*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '-(cw*ee*I94x66*complexconjugate(NN2x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x66*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x66*sw**2*complexconjugate(NN2x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x66*complexconjugate(NN2x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*sw*complexconjugate(NN2x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '(cw*ee*complex(0,1)*vd*complexconjugate(NN2x3))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*vu*complexconjugate(NN2x4))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '-(cw*ee*vd*complexconjugate(NN2x3))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN2x4))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '-((ee*complex(0,1)*VV1x1*complexconjugate(NN2x2))/sw) + (ee*complex(0,1)*VV1x2*complexconjugate(NN2x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-((ee*complex(0,1)*VV2x1*complexconjugate(NN2x2))/sw) + (ee*complex(0,1)*VV2x2*complexconjugate(NN2x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '(cw*ee*complex(0,1)*I140x44*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '(cw*ee*complex(0,1)*I140x55*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '(cw*ee*complex(0,1)*I91x44*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(cw*ee*complex(0,1)*I91x55*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '-(cw*ee*complex(0,1)*I94x44*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '-(cw*ee*complex(0,1)*I94x55*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(cw*ee*I140x44*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(cw*ee*I140x55*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(cw*ee*I91x44*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(cw*ee*I91x55*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-(cw*ee*I94x44*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '-(cw*ee*I94x55*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '(ee*complexconjugate(NN3x2))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(ee*complex(0,1)*complexconjugate(NN3x2))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(cw*complexconjugate(NN3x1))/(2.*MP) + (sw*complexconjugate(NN3x2))/(2.*MP)',
                   order = {'QGR':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '-((cw*complex(0,1)*complexconjugate(NN3x1))/(M32*MP*cmath.sqrt(6))) - (complex(0,1)*sw*complexconjugate(NN3x2))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '-(cw*ee*complex(0,1)*I139x11*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x11*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x11*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '-(cw*ee*complex(0,1)*I139x22*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x22*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x22*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '(cw*ee*complex(0,1)*I89x11*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x11*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x11*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '(cw*ee*complex(0,1)*I89x22*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x22*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x22*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(cw*ee*complex(0,1)*I93x11*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x11*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x11*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '(cw*ee*complex(0,1)*I93x22*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x22*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x22*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '-(cw*ee*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '-(cw*ee*I139x11*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '-(cw*ee*I139x22*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '(cw*ee*I89x11*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '(cw*ee*I89x22*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '(cw*ee*I93x11*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '(cw*ee*I93x22*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '(cw*ee*complex(0,1)*Rd1x1*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd1x1*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd1x1*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '(cw*ee*complex(0,1)*Rd2x2*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd2x2*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd2x2*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-((cw*ee*complex(0,1)*Rl1x1*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl1x1*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl1x1*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '-((cw*ee*complex(0,1)*Rl2x2*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl2x2*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl2x2*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-((cw*ee*complex(0,1)*Rn1x1*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn1x1*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn1x1*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '-((cw*ee*complex(0,1)*Rn2x2*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn2x2*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn2x2*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-((cw*ee*complex(0,1)*Rn3x3*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn3x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn3x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(cw*ee*complex(0,1)*Ru1x1*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru1x1*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru1x1*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '(cw*ee*complex(0,1)*Ru2x2*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru2x2*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru2x2*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(sw*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (sw**3*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*complexconjugate(NN3x2))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*sw**2*complexconjugate(NN3x2))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-((complex(0,1)*sw*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*sw**3*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*complexconjugate(NN3x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*complex(0,1)*sw**2*complexconjugate(NN3x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '(complex(0,1)*I31x33*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x33*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd3x3*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd3x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd3x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '(complex(0,1)*I31x36*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x36*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd6x3*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd6x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd6x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(complex(0,1)*I35x33*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x33*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl3x3*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl3x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl3x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '(complex(0,1)*I35x36*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x36*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl6x3*complexconjugate(NN3x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl6x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl6x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '(cw*ee*complex(0,1)*I89x33*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x33*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x33*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x33*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x33*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x33*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '(cw*ee*complex(0,1)*I89x36*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x36*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x36*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x36*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x36*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x36*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '(cw*ee*complex(0,1)*I89x63*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x63*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x63*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x63*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x63*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x63*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '(cw*ee*complex(0,1)*I89x66*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x66*complexconjugate(NN3x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x66*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x66*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x66*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x66*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '-(cw*ee*complex(0,1)*I139x33*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x33*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x33*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x33*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x33*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x33*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '-(cw*ee*complex(0,1)*I139x36*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x36*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x36*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x36*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x36*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x36*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '-(cw*ee*complex(0,1)*I139x63*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x63*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x63*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x63*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x63*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x63*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '-(cw*ee*complex(0,1)*I139x66*complexconjugate(NN3x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x66*complexconjugate(NN3x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x66*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x66*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x66*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x66*sw**2*complexconjugate(NN3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(I137x33*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x33*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x33*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x33*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '(I137x36*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x36*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x36*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x36*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '(I137x63*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x63*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x63*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x63*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '(I137x66*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x66*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x66*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x66*complexconjugate(NN3x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(I141x33*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x33*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x33*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x33*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '(I141x36*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x36*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x36*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x36*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '(I141x63*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x63*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x63*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x63*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '(I141x66*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x66*sw**2*complexconjugate(NN3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x66*complexconjugate(NN3x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x66*complexconjugate(NN3x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '-((ee*complex(0,1)*UU1x1*complexconjugate(NN3x2))/sw) - (ee*complex(0,1)*UU1x2*complexconjugate(NN3x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-((ee*complex(0,1)*UU2x1*complexconjugate(NN3x2))/sw) - (ee*complex(0,1)*UU2x2*complexconjugate(NN3x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '-(cw*ee*complex(0,1)*NN1x3*complexconjugate(NN3x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*complexconjugate(NN3x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '-(cw*ee*complex(0,1)*NN2x3*complexconjugate(NN3x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN2x4*complexconjugate(NN3x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '-(cw*ee*complex(0,1)*NN3x3*complexconjugate(NN3x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN3x4*complexconjugate(NN3x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '(cw*ee*complex(0,1)*NN4x3*complexconjugate(NN3x3))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4*complexconjugate(NN3x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '(complex(0,1)*I39x33*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*sw**2*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru3x3*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru3x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru3x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '(complex(0,1)*I39x36*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*sw**2*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru6x3*complexconjugate(NN3x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru6x3*complexconjugate(NN3x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru6x3*sw*complexconjugate(NN3x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '(cw*ee*complex(0,1)*I93x33*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x33*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x33*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x33*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x33*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x33*sw**2*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '(cw*ee*complex(0,1)*I93x36*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x36*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x36*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x36*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x36*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x36*sw**2*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(cw*ee*complex(0,1)*I93x63*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x63*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x63*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x63*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x63*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x63*sw**2*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '(cw*ee*complex(0,1)*I93x66*complexconjugate(NN3x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x66*complexconjugate(NN3x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x66*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x66*sw*complexconjugate(NN3x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x66*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x66*sw**2*complexconjugate(NN3x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '-(cw*ee*I94x33*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x33*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x33*sw**2*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x33*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '-(cw*ee*I94x36*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x36*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x36*sw**2*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x36*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '-(cw*ee*I94x63*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x63*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x63*sw**2*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x63*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-(cw*ee*I94x66*complexconjugate(NN3x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x66*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x66*sw**2*complexconjugate(NN3x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x66*complexconjugate(NN3x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*sw*complexconjugate(NN3x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(cw*ee*complex(0,1)*vd*complexconjugate(NN3x3))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*vu*complexconjugate(NN3x4))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-(cw*ee*vd*complexconjugate(NN3x3))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN3x4))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '-((ee*complex(0,1)*VV1x1*complexconjugate(NN3x2))/sw) + (ee*complex(0,1)*VV1x2*complexconjugate(NN3x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-((ee*complex(0,1)*VV2x1*complexconjugate(NN3x2))/sw) + (ee*complex(0,1)*VV2x2*complexconjugate(NN3x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(cw*ee*complex(0,1)*I140x44*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '(cw*ee*complex(0,1)*I140x55*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(cw*ee*complex(0,1)*I91x44*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(cw*ee*complex(0,1)*I91x55*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '-(cw*ee*complex(0,1)*I94x44*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-(cw*ee*complex(0,1)*I94x55*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '(cw*ee*I140x44*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '(cw*ee*I140x55*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '(cw*ee*I91x44*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '(cw*ee*I91x55*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-(cw*ee*I94x44*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-(cw*ee*I94x55*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '(ee*complexconjugate(NN4x2))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(ee*complex(0,1)*complexconjugate(NN4x2))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '(cw*complexconjugate(NN4x1))/(2.*MP) + (sw*complexconjugate(NN4x2))/(2.*MP)',
                   order = {'QGR':1})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '-((cw*complex(0,1)*complexconjugate(NN4x1))/(M32*MP*cmath.sqrt(6))) - (complex(0,1)*sw*complexconjugate(NN4x2))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-(cw*ee*complex(0,1)*I139x11*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x11*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x11*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '-(cw*ee*complex(0,1)*I139x22*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x22*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x22*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '(cw*ee*complex(0,1)*I89x11*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x11*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x11*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '(cw*ee*complex(0,1)*I89x22*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x22*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x22*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '(cw*ee*complex(0,1)*I93x11*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x11*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x11*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '(cw*ee*complex(0,1)*I93x22*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x22*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x22*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-(cw*ee*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '-(cw*ee*I139x11*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x11*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x11*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '-(cw*ee*I139x22*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x22*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x22*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '(cw*ee*I89x11*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x11*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x11*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '(cw*ee*I89x22*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x22*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x22*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '(cw*ee*I93x11*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x11*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x11*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '(cw*ee*I93x22*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x22*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x22*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(cw*ee*complex(0,1)*Rd1x1*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd1x1*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd1x1*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '(cw*ee*complex(0,1)*Rd2x2*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd2x2*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd2x2*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '-((cw*ee*complex(0,1)*Rl1x1*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl1x1*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl1x1*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '-((cw*ee*complex(0,1)*Rl2x2*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl2x2*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl2x2*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '-((cw*ee*complex(0,1)*Rn1x1*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn1x1*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn1x1*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '-((cw*ee*complex(0,1)*Rn2x2*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn2x2*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn2x2*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '-((cw*ee*complex(0,1)*Rn3x3*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn3x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn3x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '(cw*ee*complex(0,1)*Ru1x1*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru1x1*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru1x1*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '(cw*ee*complex(0,1)*Ru2x2*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru2x2*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru2x2*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '(sw*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (sw**3*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*complexconjugate(NN4x2))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*sw**2*complexconjugate(NN4x2))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '-((complex(0,1)*sw*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (complex(0,1)*sw**3*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*complex(0,1)*complexconjugate(NN4x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*complex(0,1)*sw**2*complexconjugate(NN4x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '(complex(0,1)*I31x33*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x33*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd3x3*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd3x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd3x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '(complex(0,1)*I31x36*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I31x36*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd6x3*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd6x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd6x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '(complex(0,1)*I35x33*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x33*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl3x3*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl3x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl3x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '(complex(0,1)*I35x36*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I35x36*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl6x3*complexconjugate(NN4x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl6x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl6x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '(cw*ee*complex(0,1)*I89x33*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x33*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x33*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x33*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x33*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x33*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '(cw*ee*complex(0,1)*I89x36*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x36*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x36*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x36*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x36*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x36*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '(cw*ee*complex(0,1)*I89x63*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x63*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x63*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x63*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x63*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x63*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(cw*ee*complex(0,1)*I89x66*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I91x66*complexconjugate(NN4x1))/(6.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I89x66*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I89x66*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I137x66*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I137x66*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '-(cw*ee*complex(0,1)*I139x33*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x33*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x33*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x33*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x33*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x33*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-(cw*ee*complex(0,1)*I139x36*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x36*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x36*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x36*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x36*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x36*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-(cw*ee*complex(0,1)*I139x63*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x63*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x63*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x63*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x63*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x63*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '-(cw*ee*complex(0,1)*I139x66*complexconjugate(NN4x1))/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I140x66*complexconjugate(NN4x1))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*I139x66*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*I139x66*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I141x66*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I141x66*sw**2*complexconjugate(NN4x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '(I137x33*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x33*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x33*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x33*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x33*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x33*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '(I137x36*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x36*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x36*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x36*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x36*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x36*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '(I137x63*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x63*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x63*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x63*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x63*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x63*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(I137x66*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I137x66*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I89x66*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I91x66*complexconjugate(NN4x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I89x66*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I89x66*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '(I141x33*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x33*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x33*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x33*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x33*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x33*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(I141x36*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x36*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x36*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x36*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x36*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x36*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '(I141x63*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x63*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x63*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x63*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x63*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x63*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(I141x66*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I141x66*sw**2*complexconjugate(NN4x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (cw*ee*I139x66*complexconjugate(NN4x1))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*I140x66*complexconjugate(NN4x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*I139x66*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*I139x66*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-((ee*complex(0,1)*UU1x1*complexconjugate(NN4x2))/sw) - (ee*complex(0,1)*UU1x2*complexconjugate(NN4x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-((ee*complex(0,1)*UU2x1*complexconjugate(NN4x2))/sw) - (ee*complex(0,1)*UU2x2*complexconjugate(NN4x3))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-(cw*ee*complex(0,1)*NN1x3*complexconjugate(NN4x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*complexconjugate(NN4x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '-(cw*ee*complex(0,1)*NN2x3*complexconjugate(NN4x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN2x4*complexconjugate(NN4x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-(cw*ee*complex(0,1)*NN3x3*complexconjugate(NN4x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN3x4*complexconjugate(NN4x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '-(cw*ee*complex(0,1)*NN4x3*complexconjugate(NN4x3))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN4x4*complexconjugate(NN4x4))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '(complex(0,1)*I39x33*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x33*sw**2*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru3x3*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru3x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru3x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(complex(0,1)*I39x36*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I39x36*sw**2*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru6x3*complexconjugate(NN4x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru6x3*complexconjugate(NN4x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru6x3*sw*complexconjugate(NN4x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '(cw*ee*complex(0,1)*I93x33*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x33*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x33*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x33*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x33*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x33*sw**2*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(cw*ee*complex(0,1)*I93x36*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x36*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x36*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x36*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x36*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x36*sw**2*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '(cw*ee*complex(0,1)*I93x63*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x63*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x63*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x63*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x63*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x63*sw**2*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(cw*ee*complex(0,1)*I93x66*complexconjugate(NN4x1))/(12.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I94x66*complexconjugate(NN4x1))/(3.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*I93x66*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*I93x66*sw*complexconjugate(NN4x2))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*I143x66*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I143x66*sw**2*complexconjugate(NN4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '-(cw*ee*I94x33*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x33*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x33*sw**2*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x33*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x33*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x33*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '-(cw*ee*I94x36*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x36*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x36*sw**2*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x36*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x36*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x36*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '-(cw*ee*I94x63*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x63*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x63*sw**2*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x63*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x63*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x63*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '-(cw*ee*I94x66*complexconjugate(NN4x1)*cmath.sqrt(0.6666666666666666))/(3.*M32*MP*(-1 + sw)*(1 + sw)) + (I143x66*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) - (I143x66*sw**2*complexconjugate(NN4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3)) + (cw*ee*I93x66*complexconjugate(NN4x1))/(6.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*I93x66*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*I93x66*sw*complexconjugate(NN4x2))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(cw*ee*complex(0,1)*vd*complexconjugate(NN4x3))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*vu*complexconjugate(NN4x4))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QGR':1})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '-(cw*ee*vd*complexconjugate(NN4x3))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN4x4))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '-((ee*complex(0,1)*VV1x1*complexconjugate(NN4x2))/sw) + (ee*complex(0,1)*VV1x2*complexconjugate(NN4x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '-((ee*complex(0,1)*VV2x1*complexconjugate(NN4x2))/sw) + (ee*complex(0,1)*VV2x2*complexconjugate(NN4x4))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '-(complex(0,1)*G*complexconjugate(Rd1x1)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '-((complex(0,1)*complexconjugate(Rd1x1))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '-(ee*complex(0,1)*complexconjugate(Rd1x1))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '(complex(0,1)*G*complexconjugate(Rd1x1))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '-(complexconjugate(Rd1x1)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '(-2*ee*complexconjugate(Rd1x1))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '(2*G*complexconjugate(Rd1x1))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rd1x1))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rd1x1))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '(cw*ee*complexconjugate(Rd1x1))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rd1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '(cw*ee*complex(0,1)*NN1x1*complexconjugate(Rd1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rd1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rd1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '(cw*ee*complex(0,1)*NN2x1*complexconjugate(Rd1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rd1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rd1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '(cw*ee*complex(0,1)*NN3x1*complexconjugate(Rd1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rd1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rd1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '(cw*ee*complex(0,1)*NN4x1*complexconjugate(Rd1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rd1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rd1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '-(complex(0,1)*G*complexconjugate(Rd2x2)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '-((complex(0,1)*complexconjugate(Rd2x2))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '-(ee*complex(0,1)*complexconjugate(Rd2x2))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(complex(0,1)*G*complexconjugate(Rd2x2))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '-(complexconjugate(Rd2x2)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(-2*ee*complexconjugate(Rd2x2))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(2*G*complexconjugate(Rd2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rd2x2))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rd2x2))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '(cw*ee*complexconjugate(Rd2x2))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rd2x2))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(cw*ee*complex(0,1)*NN1x1*complexconjugate(Rd2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rd2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rd2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(cw*ee*complex(0,1)*NN2x1*complexconjugate(Rd2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rd2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rd2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '(cw*ee*complex(0,1)*NN3x1*complexconjugate(Rd2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rd2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rd2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(cw*ee*complex(0,1)*NN4x1*complexconjugate(Rd2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rd2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rd2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '-(complex(0,1)*G*complexconjugate(Rd3x3)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '-((complex(0,1)*complexconjugate(Rd3x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '-(ee*complex(0,1)*complexconjugate(Rd3x3))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '(complex(0,1)*G*complexconjugate(Rd3x3))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '-(complexconjugate(Rd3x3)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(-2*ee*complexconjugate(Rd3x3))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(2*G*complexconjugate(Rd3x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rd3x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rd3x3))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(cw*ee*complexconjugate(Rd3x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rd3x3))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '(complex(0,1)*I11x33*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x33*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*complexconjugate(Rd3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rd3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rd3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '(complex(0,1)*I11x33*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x33*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*complexconjugate(Rd3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rd3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rd3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '(complex(0,1)*I11x33*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x33*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*complexconjugate(Rd3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rd3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rd3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '(complex(0,1)*I11x33*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x33*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*complexconjugate(Rd3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rd3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rd3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1543 = Coupling(name = 'GC_1543',
                   value = 'complex(0,1)*G*complexconjugate(Rd3x6)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '(complex(0,1)*complexconjugate(Rd3x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '(ee*complex(0,1)*complexconjugate(Rd3x6))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '-((complex(0,1)*G*complexconjugate(Rd3x6))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '-complexconjugate(Rd3x6)/(2.*M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '(2*ee*complexconjugate(Rd3x6))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '(-2*G*complexconjugate(Rd3x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rd3x6))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '(2*cw*ee*sw*complexconjugate(Rd3x6))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '(complex(0,1)*I13x33*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rd3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '(complex(0,1)*I13x33*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rd3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '(complex(0,1)*I13x33*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rd3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '(complex(0,1)*I13x33*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x33*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rd3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1556 = Coupling(name = 'GC_1556',
                   value = 'complex(0,1)*G*complexconjugate(Rd4x4)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(complex(0,1)*complexconjugate(Rd4x4))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '(ee*complex(0,1)*complexconjugate(Rd4x4))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '-((complex(0,1)*G*complexconjugate(Rd4x4))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '-complexconjugate(Rd4x4)/(2.*M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '(2*ee*complexconjugate(Rd4x4))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(-2*G*complexconjugate(Rd4x4))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rd4x4))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '(2*cw*ee*sw*complexconjugate(Rd4x4))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rd4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rd4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rd4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rd4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1569 = Coupling(name = 'GC_1569',
                   value = 'complex(0,1)*G*complexconjugate(Rd5x5)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '(complex(0,1)*complexconjugate(Rd5x5))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '(ee*complex(0,1)*complexconjugate(Rd5x5))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-((complex(0,1)*G*complexconjugate(Rd5x5))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '-complexconjugate(Rd5x5)/(2.*M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(2*ee*complexconjugate(Rd5x5))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '(-2*G*complexconjugate(Rd5x5))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rd5x5))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(2*cw*ee*sw*complexconjugate(Rd5x5))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rd5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rd5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rd5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rd5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '-(complex(0,1)*G*complexconjugate(Rd6x3)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '-((complex(0,1)*complexconjugate(Rd6x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '-(ee*complex(0,1)*complexconjugate(Rd6x3))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '(complex(0,1)*G*complexconjugate(Rd6x3))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '-(complexconjugate(Rd6x3)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '(-2*ee*complexconjugate(Rd6x3))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '(2*G*complexconjugate(Rd6x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rd6x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rd6x3))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(cw*ee*complexconjugate(Rd6x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rd6x3))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '(complex(0,1)*I11x36*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x36*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*complexconjugate(Rd6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rd6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rd6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '(complex(0,1)*I11x36*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x36*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*complexconjugate(Rd6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rd6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rd6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '(complex(0,1)*I11x36*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x36*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*complexconjugate(Rd6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rd6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rd6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '(complex(0,1)*I11x36*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x36*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*complexconjugate(Rd6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rd6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rd6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1595 = Coupling(name = 'GC_1595',
                   value = 'complex(0,1)*G*complexconjugate(Rd6x6)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(complex(0,1)*complexconjugate(Rd6x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '(ee*complex(0,1)*complexconjugate(Rd6x6))/(3.*MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '-((complex(0,1)*G*complexconjugate(Rd6x6))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '-complexconjugate(Rd6x6)/(2.*M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(2*ee*complexconjugate(Rd6x6))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '(-2*G*complexconjugate(Rd6x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rd6x6))/(3.*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '(2*cw*ee*sw*complexconjugate(Rd6x6))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '(complex(0,1)*I13x36*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rd6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '(complex(0,1)*I13x36*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rd6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(complex(0,1)*I13x36*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rd6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '(complex(0,1)*I13x36*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I13x36*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rd6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '-((complex(0,1)*complexconjugate(Rl1x1))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '-((ee*complex(0,1)*complexconjugate(Rl1x1))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_1610 = Coupling(name = 'GC_1610',
                   value = 'complexconjugate(Rl1x1)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '(-2*ee*complexconjugate(Rl1x1))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rl1x1))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rl1x1))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '(cw*ee*complexconjugate(Rl1x1))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rl1x1))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '-((cw*ee*complex(0,1)*NN1x1*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN1x2*complexconjugate(Rl1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '-((cw*ee*complex(0,1)*NN2x1*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN2x2*complexconjugate(Rl1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '-((cw*ee*complex(0,1)*NN3x1*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN3x2*complexconjugate(Rl1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '-((cw*ee*complex(0,1)*NN4x1*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN4x2*complexconjugate(Rl1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rl1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '-((complex(0,1)*complexconjugate(Rl2x2))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '-((ee*complex(0,1)*complexconjugate(Rl2x2))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_1620 = Coupling(name = 'GC_1620',
                   value = 'complexconjugate(Rl2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '(-2*ee*complexconjugate(Rl2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rl2x2))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rl2x2))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(cw*ee*complexconjugate(Rl2x2))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rl2x2))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '-((cw*ee*complex(0,1)*NN1x1*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN1x2*complexconjugate(Rl2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '-((cw*ee*complex(0,1)*NN2x1*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN2x2*complexconjugate(Rl2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '-((cw*ee*complex(0,1)*NN3x1*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN3x2*complexconjugate(Rl2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '-((cw*ee*complex(0,1)*NN4x1*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN4x2*complexconjugate(Rl2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rl2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '-((complex(0,1)*complexconjugate(Rl3x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '-((ee*complex(0,1)*complexconjugate(Rl3x3))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_1630 = Coupling(name = 'GC_1630',
                   value = 'complexconjugate(Rl3x3)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '(-2*ee*complexconjugate(Rl3x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rl3x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rl3x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(cw*ee*complexconjugate(Rl3x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rl3x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(complex(0,1)*I23x33*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rl3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(complex(0,1)*I23x33*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rl3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(complex(0,1)*I23x33*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rl3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '(complex(0,1)*I23x33*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x33*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rl3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rl3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(complex(0,1)*complexconjugate(Rl3x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '(ee*complex(0,1)*complexconjugate(Rl3x6))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '-(complexconjugate(Rl3x6)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '(2*ee*complexconjugate(Rl3x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rl3x6))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '(2*cw*ee*sw*complexconjugate(Rl3x6))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(complex(0,1)*I24x33*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rl3x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '(complex(0,1)*I24x33*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rl3x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(complex(0,1)*I24x33*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rl3x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '(complex(0,1)*I24x33*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x33*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rl3x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(complex(0,1)*complexconjugate(Rl4x4))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '(ee*complex(0,1)*complexconjugate(Rl4x4))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '-(complexconjugate(Rl4x4)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '(2*ee*complexconjugate(Rl4x4))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rl4x4))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '(2*cw*ee*sw*complexconjugate(Rl4x4))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rl4x4)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rl4x4)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rl4x4)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rl4x4)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '(complex(0,1)*complexconjugate(Rl5x5))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(ee*complex(0,1)*complexconjugate(Rl5x5))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '-(complexconjugate(Rl5x5)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '(2*ee*complexconjugate(Rl5x5))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rl5x5))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '(2*cw*ee*sw*complexconjugate(Rl5x5))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rl5x5)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rl5x5)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rl5x5)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rl5x5)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '-((complex(0,1)*complexconjugate(Rl6x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '-((ee*complex(0,1)*complexconjugate(Rl6x3))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_1670 = Coupling(name = 'GC_1670',
                   value = 'complexconjugate(Rl6x3)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '(-2*ee*complexconjugate(Rl6x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(cw*ee*complex(0,1)*complexconjugate(Rl6x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(Rl6x3))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '(cw*ee*complexconjugate(Rl6x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(Rl6x3))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '(complex(0,1)*I23x36*NN1x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*NN1x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*complexconjugate(Rl6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '(complex(0,1)*I23x36*NN2x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*NN2x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*complexconjugate(Rl6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(complex(0,1)*I23x36*NN3x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*NN3x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*complexconjugate(Rl6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '(complex(0,1)*I23x36*NN4x3)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I23x36*NN4x3*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*complexconjugate(Rl6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rl6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(complex(0,1)*complexconjugate(Rl6x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(ee*complex(0,1)*complexconjugate(Rl6x6))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '-(complexconjugate(Rl6x6)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '(2*ee*complexconjugate(Rl6x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(Rl6x6))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '(2*cw*ee*sw*complexconjugate(Rl6x6))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(complex(0,1)*I24x36*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*complexconjugate(NN1x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Rl6x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '(complex(0,1)*I24x36*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*complexconjugate(NN2x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Rl6x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(complex(0,1)*I24x36*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*complexconjugate(NN3x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Rl6x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '(complex(0,1)*I24x36*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I24x36*sw**2*complexconjugate(NN4x3))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Rl6x6)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '-((complex(0,1)*complexconjugate(Rn1x1))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '-(complexconjugate(Rn1x1)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Rn1x1))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '-((cw*ee*complexconjugate(Rn1x1))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '-((cw*ee*complex(0,1)*NN1x1*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN1x2*complexconjugate(Rn1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '-((cw*ee*complex(0,1)*NN2x1*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN2x2*complexconjugate(Rn1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '-((cw*ee*complex(0,1)*NN3x1*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN3x2*complexconjugate(Rn1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '-((cw*ee*complex(0,1)*NN4x1*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN4x2*complexconjugate(Rn1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rn1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '-((complex(0,1)*complexconjugate(Rn2x2))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '-(complexconjugate(Rn2x2)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Rn2x2))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '-((cw*ee*complexconjugate(Rn2x2))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '-((cw*ee*complex(0,1)*NN1x1*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN1x2*complexconjugate(Rn2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-((cw*ee*complex(0,1)*NN2x1*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN2x2*complexconjugate(Rn2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '-((cw*ee*complex(0,1)*NN3x1*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN3x2*complexconjugate(Rn2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '-((cw*ee*complex(0,1)*NN4x1*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN4x2*complexconjugate(Rn2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rn2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '-((complex(0,1)*complexconjugate(Rn3x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '-(complexconjugate(Rn3x3)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Rn3x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '-((cw*ee*complexconjugate(Rn3x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '-((cw*ee*complex(0,1)*NN1x1*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN1x2*complexconjugate(Rn3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '-((cw*ee*complex(0,1)*NN2x1*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN2x2*complexconjugate(Rn3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '-((cw*ee*complex(0,1)*NN3x1*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN3x2*complexconjugate(Rn3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '-((cw*ee*complex(0,1)*NN4x1*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN4x2*complexconjugate(Rn3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Rn3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '-(complex(0,1)*G*complexconjugate(Ru1x1)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '-((complex(0,1)*complexconjugate(Ru1x1))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '(ee*complex(0,1)*complexconjugate(Ru1x1)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '(complex(0,1)*G*complexconjugate(Ru1x1))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1716 = Coupling(name = 'GC_1716',
                   value = 'complexconjugate(Ru1x1)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '(4*ee*complexconjugate(Ru1x1))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(2*G*complexconjugate(Ru1x1))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Ru1x1))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*complexconjugate(Ru1x1)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '-((cw*ee*complexconjugate(Ru1x1))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (4*cw*ee*sw*complexconjugate(Ru1x1))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '(cw*ee*complex(0,1)*NN1x1*complexconjugate(Ru1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*complexconjugate(Ru1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Ru1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(cw*ee*complex(0,1)*NN2x1*complexconjugate(Ru1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*complexconjugate(Ru1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Ru1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '(cw*ee*complex(0,1)*NN3x1*complexconjugate(Ru1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*complexconjugate(Ru1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Ru1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '(cw*ee*complex(0,1)*NN4x1*complexconjugate(Ru1x1))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*complexconjugate(Ru1x1))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Ru1x1))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '-(complex(0,1)*G*complexconjugate(Ru2x2)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '-((complex(0,1)*complexconjugate(Ru2x2))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '(ee*complex(0,1)*complexconjugate(Ru2x2)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(complex(0,1)*G*complexconjugate(Ru2x2))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1729 = Coupling(name = 'GC_1729',
                   value = 'complexconjugate(Ru2x2)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '(4*ee*complexconjugate(Ru2x2))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '(2*G*complexconjugate(Ru2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Ru2x2))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*complexconjugate(Ru2x2)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '-((cw*ee*complexconjugate(Ru2x2))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (4*cw*ee*sw*complexconjugate(Ru2x2))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(cw*ee*complex(0,1)*NN1x1*complexconjugate(Ru2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*complexconjugate(Ru2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Ru2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(cw*ee*complex(0,1)*NN2x1*complexconjugate(Ru2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*complexconjugate(Ru2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Ru2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '(cw*ee*complex(0,1)*NN3x1*complexconjugate(Ru2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*complexconjugate(Ru2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Ru2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(cw*ee*complex(0,1)*NN4x1*complexconjugate(Ru2x2))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*complexconjugate(Ru2x2))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Ru2x2))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '-(complex(0,1)*G*complexconjugate(Ru3x3)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '-((complex(0,1)*complexconjugate(Ru3x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '(ee*complex(0,1)*complexconjugate(Ru3x3)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '(complex(0,1)*G*complexconjugate(Ru3x3))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1742 = Coupling(name = 'GC_1742',
                   value = 'complexconjugate(Ru3x3)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '(4*ee*complexconjugate(Ru3x3))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(2*G*complexconjugate(Ru3x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Ru3x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*complexconjugate(Ru3x3)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '-((cw*ee*complexconjugate(Ru3x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (4*cw*ee*sw*complexconjugate(Ru3x3))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '(complex(0,1)*I25x33*NN1x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x33*NN1x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*complexconjugate(Ru3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*complexconjugate(Ru3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Ru3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(complex(0,1)*I25x33*NN2x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x33*NN2x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*complexconjugate(Ru3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*complexconjugate(Ru3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Ru3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '(complex(0,1)*I25x33*NN3x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x33*NN3x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*complexconjugate(Ru3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*complexconjugate(Ru3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Ru3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(complex(0,1)*I25x33*NN4x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x33*NN4x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*complexconjugate(Ru3x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*complexconjugate(Ru3x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Ru3x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1751 = Coupling(name = 'GC_1751',
                   value = 'complex(0,1)*G*complexconjugate(Ru3x6)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(complex(0,1)*complexconjugate(Ru3x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '-(ee*complex(0,1)*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '-((complex(0,1)*G*complexconjugate(Ru3x6))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '-(complexconjugate(Ru3x6)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '(-4*ee*complexconjugate(Ru3x6))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '(-2*G*complexconjugate(Ru3x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '-(cw*ee*complex(0,1)*sw*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '(-4*cw*ee*sw*complexconjugate(Ru3x6))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1760 = Coupling(name = 'GC_1760',
                   value = '(complex(0,1)*I26x33*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x33*sw**2*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '(complex(0,1)*I26x33*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x33*sw**2*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '(complex(0,1)*I26x33*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x33*sw**2*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '(complex(0,1)*I26x33*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x33*sw**2*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Ru3x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1764 = Coupling(name = 'GC_1764',
                   value = 'complex(0,1)*G*complexconjugate(Ru4x4)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '(complex(0,1)*complexconjugate(Ru4x4))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '-(ee*complex(0,1)*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '-((complex(0,1)*G*complexconjugate(Ru4x4))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '-(complexconjugate(Ru4x4)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '(-4*ee*complexconjugate(Ru4x4))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(-2*G*complexconjugate(Ru4x4))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '-(cw*ee*complex(0,1)*sw*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(-4*cw*ee*sw*complexconjugate(Ru4x4))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Ru4x4)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1777 = Coupling(name = 'GC_1777',
                   value = 'complex(0,1)*G*complexconjugate(Ru5x5)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '(complex(0,1)*complexconjugate(Ru5x5))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '-(ee*complex(0,1)*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '-((complex(0,1)*G*complexconjugate(Ru5x5))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '-(complexconjugate(Ru5x5)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '(-4*ee*complexconjugate(Ru5x5))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '(-2*G*complexconjugate(Ru5x5))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '-(cw*ee*complex(0,1)*sw*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '(-4*cw*ee*sw*complexconjugate(Ru5x5))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Ru5x5)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '-(complex(0,1)*G*complexconjugate(Ru6x3)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '-((complex(0,1)*complexconjugate(Ru6x3))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '(ee*complex(0,1)*complexconjugate(Ru6x3)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '(complex(0,1)*G*complexconjugate(Ru6x3))/(MP*cmath.sqrt(2))',
                   order = {'QCD':1,'QGR':1})

GC_1794 = Coupling(name = 'GC_1794',
                   value = 'complexconjugate(Ru6x3)/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '(4*ee*complexconjugate(Ru6x3))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '(2*G*complexconjugate(Ru6x3))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(Ru6x3))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*complexconjugate(Ru6x3)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '-((cw*ee*complexconjugate(Ru6x3))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (4*cw*ee*sw*complexconjugate(Ru6x3))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '(complex(0,1)*I25x36*NN1x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x36*NN1x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*complexconjugate(Ru6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*complexconjugate(Ru6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*complexconjugate(Ru6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '(complex(0,1)*I25x36*NN2x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x36*NN2x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*complexconjugate(Ru6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*complexconjugate(Ru6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*complexconjugate(Ru6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '(complex(0,1)*I25x36*NN3x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x36*NN3x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*complexconjugate(Ru6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*complexconjugate(Ru6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*complexconjugate(Ru6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '(complex(0,1)*I25x36*NN4x4)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I25x36*NN4x4*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*complexconjugate(Ru6x3))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*complexconjugate(Ru6x3))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*complexconjugate(Ru6x3))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1803 = Coupling(name = 'GC_1803',
                   value = 'complex(0,1)*G*complexconjugate(Ru6x6)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '(complex(0,1)*complexconjugate(Ru6x6))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '-(ee*complex(0,1)*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '-((complex(0,1)*G*complexconjugate(Ru6x6))/(MP*cmath.sqrt(2)))',
                   order = {'QCD':1,'QGR':1})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '-(complexconjugate(Ru6x6)/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(-4*ee*complexconjugate(Ru6x6))/(3.*M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '(-2*G*complexconjugate(Ru6x6))/(M32*MP*cmath.sqrt(3))',
                   order = {'QCD':1,'QGR':1})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '-(cw*ee*complex(0,1)*sw*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '(-4*cw*ee*sw*complexconjugate(Ru6x6))/(3.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '(complex(0,1)*I26x36*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x36*sw**2*complexconjugate(NN1x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '(complex(0,1)*I26x36*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x36*sw**2*complexconjugate(NN2x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '(complex(0,1)*I26x36*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x36*sw**2*complexconjugate(NN3x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '(complex(0,1)*I26x36*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I26x36*sw**2*complexconjugate(NN4x4))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(Ru6x6)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '-complexconjugate(UU1x1)/(2.*MP)',
                   order = {'QGR':1})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '-(ee*complexconjugate(UU1x1))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '(complex(0,1)*complexconjugate(UU1x1))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '-((ee*complex(0,1)*I47x11*complexconjugate(UU1x1))/sw)',
                   order = {'QED':1})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '-((ee*complex(0,1)*I47x22*complexconjugate(UU1x1))/sw)',
                   order = {'QED':1})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '-((ee*complex(0,1)*I81x11*complexconjugate(UU1x1))/sw)',
                   order = {'QED':1})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '-((ee*complex(0,1)*I81x22*complexconjugate(UU1x1))/sw)',
                   order = {'QED':1})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '(cw*ee*complexconjugate(UU1x1))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '(ee*complex(0,1)*I105x11*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '(ee*complex(0,1)*I105x22*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '(ee*complex(0,1)*I66x11*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '(ee*complex(0,1)*I66x22*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '(cw*ee*complex(0,1)*complexconjugate(UU1x1))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '(ee*I105x11*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '(ee*I105x22*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '(ee*I66x11*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '(ee*I66x22*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1834 = Coupling(name = 'GC_1834',
                   value = 'complex(0,1)*I151x33*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1835 = Coupling(name = 'GC_1835',
                   value = 'complex(0,1)*I154x33*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1836 = Coupling(name = 'GC_1836',
                   value = 'complex(0,1)*I154x36*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '(ee*complex(0,1)*vd*complexconjugate(UU1x2))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '(ee*vd*complexconjugate(UU1x2))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '-((ee*complex(0,1)*I47x33*complexconjugate(UU1x1))/sw) + complex(0,1)*I49x33*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '-((ee*complex(0,1)*I47x36*complexconjugate(UU1x1))/sw) + complex(0,1)*I49x36*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '-((ee*complex(0,1)*I81x33*complexconjugate(UU1x1))/sw) + complex(0,1)*I82x33*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '-((ee*complex(0,1)*I81x36*complexconjugate(UU1x1))/sw) + complex(0,1)*I82x36*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '(ee*complex(0,1)*I105x33*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x33*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(ee*complex(0,1)*I105x36*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x36*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '(ee*complex(0,1)*I105x63*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x63*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(ee*complex(0,1)*I105x66*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x66*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '(ee*complex(0,1)*I66x33*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I67x33*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '(ee*complex(0,1)*I66x36*complexconjugate(UU1x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I67x36*complexconjugate(UU1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '(ee*I105x33*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x33*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '(ee*I105x36*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x36*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '(ee*I105x63*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x63*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '(ee*I105x66*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x66*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '(ee*I66x33*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I67x33*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '(ee*I66x36*complexconjugate(UU1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I67x36*complexconjugate(UU1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '-((ee*complex(0,1)*NN1x2*complexconjugate(UU1x1))/sw) - (ee*complex(0,1)*NN1x3*complexconjugate(UU1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '-((ee*complex(0,1)*NN2x2*complexconjugate(UU1x1))/sw) - (ee*complex(0,1)*NN2x3*complexconjugate(UU1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '-((ee*complex(0,1)*NN3x2*complexconjugate(UU1x1))/sw) - (ee*complex(0,1)*NN3x3*complexconjugate(UU1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '-((ee*complex(0,1)*NN4x2*complexconjugate(UU1x1))/sw) - (ee*complex(0,1)*NN4x3*complexconjugate(UU1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1859 = Coupling(name = 'GC_1859',
                   value = 'ee*complex(0,1)*UU1x1*complexconjugate(UU1x1) + ee*complex(0,1)*UU1x2*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '-((cw*ee*complex(0,1)*UU1x1*complexconjugate(UU1x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU1x1*complexconjugate(UU1x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU1x2*complexconjugate(UU1x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU1x2*complexconjugate(UU1x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1861 = Coupling(name = 'GC_1861',
                   value = 'ee*complex(0,1)*UU2x1*complexconjugate(UU1x1) + ee*complex(0,1)*UU2x2*complexconjugate(UU1x2)',
                   order = {'QED':1})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '-((cw*ee*complex(0,1)*UU2x1*complexconjugate(UU1x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU2x1*complexconjugate(UU1x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU2x2*complexconjugate(UU1x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU2x2*complexconjugate(UU1x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '-complexconjugate(UU2x1)/(2.*MP)',
                   order = {'QGR':1})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '-(ee*complexconjugate(UU2x1))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '(complex(0,1)*complexconjugate(UU2x1))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '-((ee*complex(0,1)*I47x11*complexconjugate(UU2x1))/sw)',
                   order = {'QED':1})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '-((ee*complex(0,1)*I47x22*complexconjugate(UU2x1))/sw)',
                   order = {'QED':1})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '-((ee*complex(0,1)*I81x11*complexconjugate(UU2x1))/sw)',
                   order = {'QED':1})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '-((ee*complex(0,1)*I81x22*complexconjugate(UU2x1))/sw)',
                   order = {'QED':1})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '(cw*ee*complexconjugate(UU2x1))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '(ee*complex(0,1)*I105x11*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '(ee*complex(0,1)*I105x22*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '(ee*complex(0,1)*I66x11*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '(ee*complex(0,1)*I66x22*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '(cw*ee*complex(0,1)*complexconjugate(UU2x1))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '(ee*I105x11*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(ee*I105x22*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '(ee*I66x11*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '(ee*I66x22*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1881 = Coupling(name = 'GC_1881',
                   value = 'complex(0,1)*I151x33*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1882 = Coupling(name = 'GC_1882',
                   value = 'complex(0,1)*I154x33*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1883 = Coupling(name = 'GC_1883',
                   value = 'complex(0,1)*I154x36*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '(ee*complex(0,1)*vd*complexconjugate(UU2x2))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '(ee*vd*complexconjugate(UU2x2))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '-((ee*complex(0,1)*I47x33*complexconjugate(UU2x1))/sw) + complex(0,1)*I49x33*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '-((ee*complex(0,1)*I47x36*complexconjugate(UU2x1))/sw) + complex(0,1)*I49x36*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '-((ee*complex(0,1)*I81x33*complexconjugate(UU2x1))/sw) + complex(0,1)*I82x33*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '-((ee*complex(0,1)*I81x36*complexconjugate(UU2x1))/sw) + complex(0,1)*I82x36*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(ee*complex(0,1)*I105x33*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x33*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '(ee*complex(0,1)*I105x36*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x36*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(ee*complex(0,1)*I105x63*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x63*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '(ee*complex(0,1)*I105x66*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I107x66*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '(ee*complex(0,1)*I66x33*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I67x33*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1895 = Coupling(name = 'GC_1895',
                   value = '(ee*complex(0,1)*I66x36*complexconjugate(UU2x1))/(2.*MP*sw*cmath.sqrt(2)) - (complex(0,1)*I67x36*complexconjugate(UU2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1896 = Coupling(name = 'GC_1896',
                   value = '(ee*I105x33*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x33*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1897 = Coupling(name = 'GC_1897',
                   value = '(ee*I105x36*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x36*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1898 = Coupling(name = 'GC_1898',
                   value = '(ee*I105x63*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x63*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1899 = Coupling(name = 'GC_1899',
                   value = '(ee*I105x66*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I107x66*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1900 = Coupling(name = 'GC_1900',
                   value = '(ee*I66x33*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I67x33*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1901 = Coupling(name = 'GC_1901',
                   value = '(ee*I66x36*complexconjugate(UU2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) - (I67x36*complexconjugate(UU2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1902 = Coupling(name = 'GC_1902',
                   value = '-((ee*complex(0,1)*NN1x2*complexconjugate(UU2x1))/sw) - (ee*complex(0,1)*NN1x3*complexconjugate(UU2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1903 = Coupling(name = 'GC_1903',
                   value = '-((ee*complex(0,1)*NN2x2*complexconjugate(UU2x1))/sw) - (ee*complex(0,1)*NN2x3*complexconjugate(UU2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1904 = Coupling(name = 'GC_1904',
                   value = '-((ee*complex(0,1)*NN3x2*complexconjugate(UU2x1))/sw) - (ee*complex(0,1)*NN3x3*complexconjugate(UU2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1905 = Coupling(name = 'GC_1905',
                   value = '-((ee*complex(0,1)*NN4x2*complexconjugate(UU2x1))/sw) - (ee*complex(0,1)*NN4x3*complexconjugate(UU2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1906 = Coupling(name = 'GC_1906',
                   value = 'ee*complex(0,1)*UU1x1*complexconjugate(UU2x1) + ee*complex(0,1)*UU1x2*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1907 = Coupling(name = 'GC_1907',
                   value = '-((cw*ee*complex(0,1)*UU1x1*complexconjugate(UU2x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU1x1*complexconjugate(UU2x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU1x2*complexconjugate(UU2x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU1x2*complexconjugate(UU2x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1908 = Coupling(name = 'GC_1908',
                   value = 'ee*complex(0,1)*UU2x1*complexconjugate(UU2x1) + ee*complex(0,1)*UU2x2*complexconjugate(UU2x2)',
                   order = {'QED':1})

GC_1909 = Coupling(name = 'GC_1909',
                   value = '-((cw*ee*complex(0,1)*UU2x1*complexconjugate(UU2x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU2x1*complexconjugate(UU2x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU2x2*complexconjugate(UU2x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU2x2*complexconjugate(UU2x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1910 = Coupling(name = 'GC_1910',
                   value = 'complexconjugate(VV1x1)/(2.*MP)',
                   order = {'QGR':1})

GC_1911 = Coupling(name = 'GC_1911',
                   value = '-(ee*complexconjugate(VV1x1))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1912 = Coupling(name = 'GC_1912',
                   value = '-((complex(0,1)*complexconjugate(VV1x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1913 = Coupling(name = 'GC_1913',
                   value = '-((ee*complex(0,1)*complexconjugate(VV1x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1914 = Coupling(name = 'GC_1914',
                   value = '-((ee*complex(0,1)*I118x11*complexconjugate(VV1x1))/sw)',
                   order = {'QED':1})

GC_1915 = Coupling(name = 'GC_1915',
                   value = '-((ee*complex(0,1)*I118x22*complexconjugate(VV1x1))/sw)',
                   order = {'QED':1})

GC_1916 = Coupling(name = 'GC_1916',
                   value = '-((ee*complex(0,1)*I99x11*complexconjugate(VV1x1))/sw)',
                   order = {'QED':1})

GC_1917 = Coupling(name = 'GC_1917',
                   value = '-((ee*complex(0,1)*I99x22*complexconjugate(VV1x1))/sw)',
                   order = {'QED':1})

GC_1918 = Coupling(name = 'GC_1918',
                   value = '-((ee*complex(0,1)*I99x33*complexconjugate(VV1x1))/sw)',
                   order = {'QED':1})

GC_1919 = Coupling(name = 'GC_1919',
                   value = '(cw*ee*complexconjugate(VV1x1))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1920 = Coupling(name = 'GC_1920',
                   value = '-(ee*complex(0,1)*I64x11*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1921 = Coupling(name = 'GC_1921',
                   value = '-(ee*complex(0,1)*I64x22*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1922 = Coupling(name = 'GC_1922',
                   value = '-(ee*complex(0,1)*I64x33*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1923 = Coupling(name = 'GC_1923',
                   value = '-(ee*complex(0,1)*I64x36*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1924 = Coupling(name = 'GC_1924',
                   value = '-(ee*complex(0,1)*I76x11*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1925 = Coupling(name = 'GC_1925',
                   value = '-(ee*complex(0,1)*I76x22*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1926 = Coupling(name = 'GC_1926',
                   value = '(cw*ee*complex(0,1)*complexconjugate(VV1x1))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1927 = Coupling(name = 'GC_1927',
                   value = '-(ee*I64x11*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1928 = Coupling(name = 'GC_1928',
                   value = '-(ee*I64x22*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1929 = Coupling(name = 'GC_1929',
                   value = '-(ee*I64x33*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1930 = Coupling(name = 'GC_1930',
                   value = '-(ee*I64x36*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1931 = Coupling(name = 'GC_1931',
                   value = '-(ee*I76x11*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1932 = Coupling(name = 'GC_1932',
                   value = '-(ee*I76x22*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1933 = Coupling(name = 'GC_1933',
                   value = 'complex(0,1)*I147x33*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1934 = Coupling(name = 'GC_1934',
                   value = 'complex(0,1)*I147x36*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1935 = Coupling(name = 'GC_1935',
                   value = '-(ee*complex(0,1)*vu*complexconjugate(VV1x2))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1936 = Coupling(name = 'GC_1936',
                   value = '(ee*vu*complexconjugate(VV1x2))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1937 = Coupling(name = 'GC_1937',
                   value = '-((ee*complex(0,1)*I118x33*complexconjugate(VV1x1))/sw) + complex(0,1)*I120x33*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1938 = Coupling(name = 'GC_1938',
                   value = '-((ee*complex(0,1)*I118x36*complexconjugate(VV1x1))/sw) + complex(0,1)*I120x36*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1939 = Coupling(name = 'GC_1939',
                   value = '-(ee*complex(0,1)*I76x33*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x33*complexconjugate(VV1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1940 = Coupling(name = 'GC_1940',
                   value = '-(ee*complex(0,1)*I76x36*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x36*complexconjugate(VV1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1941 = Coupling(name = 'GC_1941',
                   value = '-(ee*complex(0,1)*I76x63*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x63*complexconjugate(VV1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1942 = Coupling(name = 'GC_1942',
                   value = '-(ee*complex(0,1)*I76x66*complexconjugate(VV1x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x66*complexconjugate(VV1x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1943 = Coupling(name = 'GC_1943',
                   value = '-(ee*I76x33*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x33*complexconjugate(VV1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1944 = Coupling(name = 'GC_1944',
                   value = '-(ee*I76x36*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x36*complexconjugate(VV1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1945 = Coupling(name = 'GC_1945',
                   value = '-(ee*I76x63*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x63*complexconjugate(VV1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1946 = Coupling(name = 'GC_1946',
                   value = '-(ee*I76x66*complexconjugate(VV1x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x66*complexconjugate(VV1x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1947 = Coupling(name = 'GC_1947',
                   value = '-((ee*complex(0,1)*NN1x2*complexconjugate(VV1x1))/sw) + (ee*complex(0,1)*NN1x4*complexconjugate(VV1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1948 = Coupling(name = 'GC_1948',
                   value = '-((ee*complex(0,1)*NN2x2*complexconjugate(VV1x1))/sw) + (ee*complex(0,1)*NN2x4*complexconjugate(VV1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1949 = Coupling(name = 'GC_1949',
                   value = '-((ee*complex(0,1)*NN3x2*complexconjugate(VV1x1))/sw) + (ee*complex(0,1)*NN3x4*complexconjugate(VV1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1950 = Coupling(name = 'GC_1950',
                   value = '-((ee*complex(0,1)*NN4x2*complexconjugate(VV1x1))/sw) + (ee*complex(0,1)*NN4x4*complexconjugate(VV1x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1951 = Coupling(name = 'GC_1951',
                   value = 'ee*complex(0,1)*VV1x1*complexconjugate(VV1x1) + ee*complex(0,1)*VV1x2*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1952 = Coupling(name = 'GC_1952',
                   value = '-((cw*ee*complex(0,1)*VV1x1*complexconjugate(VV1x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV1x1*complexconjugate(VV1x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV1x2*complexconjugate(VV1x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV1x2*complexconjugate(VV1x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1953 = Coupling(name = 'GC_1953',
                   value = 'ee*complex(0,1)*VV2x1*complexconjugate(VV1x1) + ee*complex(0,1)*VV2x2*complexconjugate(VV1x2)',
                   order = {'QED':1})

GC_1954 = Coupling(name = 'GC_1954',
                   value = '-((cw*ee*complex(0,1)*VV2x1*complexconjugate(VV1x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV2x1*complexconjugate(VV1x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV2x2*complexconjugate(VV1x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV2x2*complexconjugate(VV1x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1955 = Coupling(name = 'GC_1955',
                   value = 'complexconjugate(VV2x1)/(2.*MP)',
                   order = {'QGR':1})

GC_1956 = Coupling(name = 'GC_1956',
                   value = '-(ee*complexconjugate(VV2x1))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_1957 = Coupling(name = 'GC_1957',
                   value = '-((complex(0,1)*complexconjugate(VV2x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QGR':1})

GC_1958 = Coupling(name = 'GC_1958',
                   value = '-((ee*complex(0,1)*complexconjugate(VV2x1))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_1959 = Coupling(name = 'GC_1959',
                   value = '-((ee*complex(0,1)*I118x11*complexconjugate(VV2x1))/sw)',
                   order = {'QED':1})

GC_1960 = Coupling(name = 'GC_1960',
                   value = '-((ee*complex(0,1)*I118x22*complexconjugate(VV2x1))/sw)',
                   order = {'QED':1})

GC_1961 = Coupling(name = 'GC_1961',
                   value = '-((ee*complex(0,1)*I99x11*complexconjugate(VV2x1))/sw)',
                   order = {'QED':1})

GC_1962 = Coupling(name = 'GC_1962',
                   value = '-((ee*complex(0,1)*I99x22*complexconjugate(VV2x1))/sw)',
                   order = {'QED':1})

GC_1963 = Coupling(name = 'GC_1963',
                   value = '-((ee*complex(0,1)*I99x33*complexconjugate(VV2x1))/sw)',
                   order = {'QED':1})

GC_1964 = Coupling(name = 'GC_1964',
                   value = '(cw*ee*complexconjugate(VV2x1))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_1965 = Coupling(name = 'GC_1965',
                   value = '-(ee*complex(0,1)*I64x11*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1966 = Coupling(name = 'GC_1966',
                   value = '-(ee*complex(0,1)*I64x22*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1967 = Coupling(name = 'GC_1967',
                   value = '-(ee*complex(0,1)*I64x33*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1968 = Coupling(name = 'GC_1968',
                   value = '-(ee*complex(0,1)*I64x36*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1969 = Coupling(name = 'GC_1969',
                   value = '-(ee*complex(0,1)*I76x11*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1970 = Coupling(name = 'GC_1970',
                   value = '-(ee*complex(0,1)*I76x22*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1971 = Coupling(name = 'GC_1971',
                   value = '(cw*ee*complex(0,1)*complexconjugate(VV2x1))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_1972 = Coupling(name = 'GC_1972',
                   value = '-(ee*I64x11*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1973 = Coupling(name = 'GC_1973',
                   value = '-(ee*I64x22*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1974 = Coupling(name = 'GC_1974',
                   value = '-(ee*I64x33*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1975 = Coupling(name = 'GC_1975',
                   value = '-(ee*I64x36*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1976 = Coupling(name = 'GC_1976',
                   value = '-(ee*I76x11*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1977 = Coupling(name = 'GC_1977',
                   value = '-(ee*I76x22*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1978 = Coupling(name = 'GC_1978',
                   value = 'complex(0,1)*I147x33*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1979 = Coupling(name = 'GC_1979',
                   value = 'complex(0,1)*I147x36*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1980 = Coupling(name = 'GC_1980',
                   value = '-(ee*complex(0,1)*vu*complexconjugate(VV2x2))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_1981 = Coupling(name = 'GC_1981',
                   value = '(ee*vu*complexconjugate(VV2x2))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_1982 = Coupling(name = 'GC_1982',
                   value = '-((ee*complex(0,1)*I118x33*complexconjugate(VV2x1))/sw) + complex(0,1)*I120x33*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1983 = Coupling(name = 'GC_1983',
                   value = '-((ee*complex(0,1)*I118x36*complexconjugate(VV2x1))/sw) + complex(0,1)*I120x36*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1984 = Coupling(name = 'GC_1984',
                   value = '-(ee*complex(0,1)*I76x33*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x33*complexconjugate(VV2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1985 = Coupling(name = 'GC_1985',
                   value = '-(ee*complex(0,1)*I76x36*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x36*complexconjugate(VV2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1986 = Coupling(name = 'GC_1986',
                   value = '-(ee*complex(0,1)*I76x63*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x63*complexconjugate(VV2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1987 = Coupling(name = 'GC_1987',
                   value = '-(ee*complex(0,1)*I76x66*complexconjugate(VV2x1))/(2.*MP*sw*cmath.sqrt(2)) + (complex(0,1)*I77x66*complexconjugate(VV2x2))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_1988 = Coupling(name = 'GC_1988',
                   value = '-(ee*I76x33*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x33*complexconjugate(VV2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1989 = Coupling(name = 'GC_1989',
                   value = '-(ee*I76x36*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x36*complexconjugate(VV2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1990 = Coupling(name = 'GC_1990',
                   value = '-(ee*I76x63*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x63*complexconjugate(VV2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1991 = Coupling(name = 'GC_1991',
                   value = '-(ee*I76x66*complexconjugate(VV2x1))/(2.*M32*MP*sw*cmath.sqrt(3)) + (I77x66*complexconjugate(VV2x2))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_1992 = Coupling(name = 'GC_1992',
                   value = '-((ee*complex(0,1)*NN1x2*complexconjugate(VV2x1))/sw) + (ee*complex(0,1)*NN1x4*complexconjugate(VV2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1993 = Coupling(name = 'GC_1993',
                   value = '-((ee*complex(0,1)*NN2x2*complexconjugate(VV2x1))/sw) + (ee*complex(0,1)*NN2x4*complexconjugate(VV2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1994 = Coupling(name = 'GC_1994',
                   value = '-((ee*complex(0,1)*NN3x2*complexconjugate(VV2x1))/sw) + (ee*complex(0,1)*NN3x4*complexconjugate(VV2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1995 = Coupling(name = 'GC_1995',
                   value = '-((ee*complex(0,1)*NN4x2*complexconjugate(VV2x1))/sw) + (ee*complex(0,1)*NN4x4*complexconjugate(VV2x2))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1996 = Coupling(name = 'GC_1996',
                   value = 'ee*complex(0,1)*VV1x1*complexconjugate(VV2x1) + ee*complex(0,1)*VV1x2*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1997 = Coupling(name = 'GC_1997',
                   value = '-((cw*ee*complex(0,1)*VV1x1*complexconjugate(VV2x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV1x1*complexconjugate(VV2x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV1x2*complexconjugate(VV2x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV1x2*complexconjugate(VV2x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1998 = Coupling(name = 'GC_1998',
                   value = 'ee*complex(0,1)*VV2x1*complexconjugate(VV2x1) + ee*complex(0,1)*VV2x2*complexconjugate(VV2x2)',
                   order = {'QED':1})

GC_1999 = Coupling(name = 'GC_1999',
                   value = '-((cw*ee*complex(0,1)*VV2x1*complexconjugate(VV2x1))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV2x1*complexconjugate(VV2x1))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV2x2*complexconjugate(VV2x2))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV2x2*complexconjugate(VV2x2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2000 = Coupling(name = 'GC_2000',
                   value = '-(complex(0,1)*I12x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2001 = Coupling(name = 'GC_2001',
                   value = '-(complex(0,1)*I12x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2002 = Coupling(name = 'GC_2002',
                   value = '(complex(0,1)*I14x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2003 = Coupling(name = 'GC_2003',
                   value = '(complex(0,1)*I14x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2004 = Coupling(name = 'GC_2004',
                   value = '-(complex(0,1)*I17x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2005 = Coupling(name = 'GC_2005',
                   value = '-(complex(0,1)*I17x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2006 = Coupling(name = 'GC_2006',
                   value = '(complex(0,1)*I18x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2007 = Coupling(name = 'GC_2007',
                   value = '(complex(0,1)*I18x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2008 = Coupling(name = 'GC_2008',
                   value = '-(complex(0,1)*I21x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2009 = Coupling(name = 'GC_2009',
                   value = '-(complex(0,1)*I21x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2010 = Coupling(name = 'GC_2010',
                   value = '(complex(0,1)*I22x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2011 = Coupling(name = 'GC_2011',
                   value = '(complex(0,1)*I22x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2012 = Coupling(name = 'GC_2012',
                   value = '-(complex(0,1)*I27x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2013 = Coupling(name = 'GC_2013',
                   value = '-(complex(0,1)*I27x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2014 = Coupling(name = 'GC_2014',
                   value = '(complex(0,1)*I28x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2015 = Coupling(name = 'GC_2015',
                   value = '(complex(0,1)*I28x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2016 = Coupling(name = 'GC_2016',
                   value = '-(complex(0,1)*I37x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2017 = Coupling(name = 'GC_2017',
                   value = '-(complex(0,1)*I37x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2018 = Coupling(name = 'GC_2018',
                   value = '(complex(0,1)*I38x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2019 = Coupling(name = 'GC_2019',
                   value = '(complex(0,1)*I38x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2020 = Coupling(name = 'GC_2020',
                   value = '-(complex(0,1)*I43x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2021 = Coupling(name = 'GC_2021',
                   value = '-(complex(0,1)*I43x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2022 = Coupling(name = 'GC_2022',
                   value = '(complex(0,1)*I44x33*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2023 = Coupling(name = 'GC_2023',
                   value = '(complex(0,1)*I44x36*cmath.cos(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2024 = Coupling(name = 'GC_2024',
                   value = '-((I12x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2025 = Coupling(name = 'GC_2025',
                   value = '-((I12x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2026 = Coupling(name = 'GC_2026',
                   value = '(I14x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2027 = Coupling(name = 'GC_2027',
                   value = '(I14x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2028 = Coupling(name = 'GC_2028',
                   value = '-((I17x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2029 = Coupling(name = 'GC_2029',
                   value = '-((I17x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2030 = Coupling(name = 'GC_2030',
                   value = '(I18x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2031 = Coupling(name = 'GC_2031',
                   value = '(I18x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2032 = Coupling(name = 'GC_2032',
                   value = '-((I21x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2033 = Coupling(name = 'GC_2033',
                   value = '-((I21x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2034 = Coupling(name = 'GC_2034',
                   value = '(I22x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2035 = Coupling(name = 'GC_2035',
                   value = '(I22x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2036 = Coupling(name = 'GC_2036',
                   value = '-((I27x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2037 = Coupling(name = 'GC_2037',
                   value = '-((I27x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2038 = Coupling(name = 'GC_2038',
                   value = '(I28x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2039 = Coupling(name = 'GC_2039',
                   value = '(I28x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2040 = Coupling(name = 'GC_2040',
                   value = '-((I37x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2041 = Coupling(name = 'GC_2041',
                   value = '-((I37x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2042 = Coupling(name = 'GC_2042',
                   value = '(I38x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2043 = Coupling(name = 'GC_2043',
                   value = '(I38x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2044 = Coupling(name = 'GC_2044',
                   value = '-((I43x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2045 = Coupling(name = 'GC_2045',
                   value = '-((I43x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2046 = Coupling(name = 'GC_2046',
                   value = '(I44x33*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2047 = Coupling(name = 'GC_2047',
                   value = '(I44x36*cmath.cos(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2048 = Coupling(name = 'GC_2048',
                   value = '-(ee*complex(0,1)*UU1x2*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2049 = Coupling(name = 'GC_2049',
                   value = '(ee*UU1x2*cmath.cos(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2050 = Coupling(name = 'GC_2050',
                   value = '-(ee*complex(0,1)*UU2x2*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2051 = Coupling(name = 'GC_2051',
                   value = '(ee*UU2x2*cmath.cos(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2052 = Coupling(name = 'GC_2052',
                   value = '(ee*complex(0,1)*VV1x2*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2053 = Coupling(name = 'GC_2053',
                   value = '(ee*VV1x2*cmath.cos(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2054 = Coupling(name = 'GC_2054',
                   value = '(ee*complex(0,1)*VV2x2*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2055 = Coupling(name = 'GC_2055',
                   value = '(ee*VV2x2*cmath.cos(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2056 = Coupling(name = 'GC_2056',
                   value = '-((complex(0,1)*yd3x3*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2057 = Coupling(name = 'GC_2057',
                   value = '-((complex(0,1)*ye3x3*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2058 = Coupling(name = 'GC_2058',
                   value = '-((complex(0,1)*yu3x3*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2059 = Coupling(name = 'GC_2059',
                   value = '(ee*complex(0,1)*complexconjugate(UU1x2)*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2060 = Coupling(name = 'GC_2060',
                   value = '(ee*complexconjugate(UU1x2)*cmath.cos(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2061 = Coupling(name = 'GC_2061',
                   value = '(ee*complex(0,1)*complexconjugate(UU2x2)*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2062 = Coupling(name = 'GC_2062',
                   value = '(ee*complexconjugate(UU2x2)*cmath.cos(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2063 = Coupling(name = 'GC_2063',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x2)*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2064 = Coupling(name = 'GC_2064',
                   value = '(ee*complexconjugate(VV1x2)*cmath.cos(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2065 = Coupling(name = 'GC_2065',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x2)*cmath.cos(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2066 = Coupling(name = 'GC_2066',
                   value = '(ee*complexconjugate(VV2x2)*cmath.cos(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2067 = Coupling(name = 'GC_2067',
                   value = '-((complex(0,1)*complexconjugate(yd3x3)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2068 = Coupling(name = 'GC_2068',
                   value = '-((complex(0,1)*complexconjugate(ye3x3)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2069 = Coupling(name = 'GC_2069',
                   value = '-((complex(0,1)*complexconjugate(yu3x3)*cmath.cos(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2070 = Coupling(name = 'GC_2070',
                   value = '-(complexconjugate(NN1x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN1x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2071 = Coupling(name = 'GC_2071',
                   value = '-(complexconjugate(NN2x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2072 = Coupling(name = 'GC_2072',
                   value = '-(complexconjugate(NN3x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2073 = Coupling(name = 'GC_2073',
                   value = '-(complexconjugate(NN4x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2074 = Coupling(name = 'GC_2074',
                   value = 'complex(0,1)*I29x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_2075 = Coupling(name = 'GC_2075',
                   value = 'complex(0,1)*I74x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_2076 = Coupling(name = 'GC_2076',
                   value = '-((complex(0,1)*I16x33*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2077 = Coupling(name = 'GC_2077',
                   value = '-((complex(0,1)*I16x36*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2078 = Coupling(name = 'GC_2078',
                   value = '(complex(0,1)*I19x33*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2079 = Coupling(name = 'GC_2079',
                   value = '(complex(0,1)*I19x36*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2080 = Coupling(name = 'GC_2080',
                   value = '(I21x33*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2081 = Coupling(name = 'GC_2081',
                   value = '(I21x36*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2082 = Coupling(name = 'GC_2082',
                   value = '(I22x33*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2083 = Coupling(name = 'GC_2083',
                   value = '(I22x36*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2084 = Coupling(name = 'GC_2084',
                   value = '-((complex(0,1)*I34x33*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2085 = Coupling(name = 'GC_2085',
                   value = '-((complex(0,1)*I34x36*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2086 = Coupling(name = 'GC_2086',
                   value = '(complex(0,1)*I41x33*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2087 = Coupling(name = 'GC_2087',
                   value = '(complex(0,1)*I41x36*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2088 = Coupling(name = 'GC_2088',
                   value = '-(I43x33*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2089 = Coupling(name = 'GC_2089',
                   value = '-(I43x36*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2090 = Coupling(name = 'GC_2090',
                   value = '-(I44x33*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2091 = Coupling(name = 'GC_2091',
                   value = '-(I44x36*cmath.cos(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2092 = Coupling(name = 'GC_2092',
                   value = '-((I16x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2093 = Coupling(name = 'GC_2093',
                   value = '-((I16x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2094 = Coupling(name = 'GC_2094',
                   value = '(I19x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2095 = Coupling(name = 'GC_2095',
                   value = '(I19x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2096 = Coupling(name = 'GC_2096',
                   value = '-((complex(0,1)*I21x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2097 = Coupling(name = 'GC_2097',
                   value = '-((complex(0,1)*I21x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2098 = Coupling(name = 'GC_2098',
                   value = '-((complex(0,1)*I22x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2099 = Coupling(name = 'GC_2099',
                   value = '-((complex(0,1)*I22x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2100 = Coupling(name = 'GC_2100',
                   value = '-((I34x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2101 = Coupling(name = 'GC_2101',
                   value = '-((I34x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2102 = Coupling(name = 'GC_2102',
                   value = '(I41x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2103 = Coupling(name = 'GC_2103',
                   value = '(I41x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2104 = Coupling(name = 'GC_2104',
                   value = '(complex(0,1)*I43x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2105 = Coupling(name = 'GC_2105',
                   value = '(complex(0,1)*I43x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2106 = Coupling(name = 'GC_2106',
                   value = '(complex(0,1)*I44x33*cmath.cos(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2107 = Coupling(name = 'GC_2107',
                   value = '(complex(0,1)*I44x36*cmath.cos(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2108 = Coupling(name = 'GC_2108',
                   value = '-(ee*complex(0,1)*NN1x4*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2109 = Coupling(name = 'GC_2109',
                   value = '(ee*NN1x4*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2110 = Coupling(name = 'GC_2110',
                   value = '-(ee*complex(0,1)*NN2x4*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2111 = Coupling(name = 'GC_2111',
                   value = '(ee*NN2x4*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2112 = Coupling(name = 'GC_2112',
                   value = '-(ee*complex(0,1)*NN3x4*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2113 = Coupling(name = 'GC_2113',
                   value = '(ee*NN3x4*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2114 = Coupling(name = 'GC_2114',
                   value = '-(ee*complex(0,1)*NN4x4*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2115 = Coupling(name = 'GC_2115',
                   value = '(ee*NN4x4*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2116 = Coupling(name = 'GC_2116',
                   value = '-((complex(0,1)*VV1x2*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_2117 = Coupling(name = 'GC_2117',
                   value = '(ee*complex(0,1)*VV1x2*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2118 = Coupling(name = 'GC_2118',
                   value = '(VV1x2*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_2119 = Coupling(name = 'GC_2119',
                   value = '(2*ee*VV1x2*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2120 = Coupling(name = 'GC_2120',
                   value = '-(ee*VV1x2*cmath.cos(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2121 = Coupling(name = 'GC_2121',
                   value = '(ee*complex(0,1)*VV1x2*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2122 = Coupling(name = 'GC_2122',
                   value = '-((complex(0,1)*VV2x2*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_2123 = Coupling(name = 'GC_2123',
                   value = '(ee*complex(0,1)*VV2x2*cmath.cos(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2124 = Coupling(name = 'GC_2124',
                   value = '(VV2x2*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_2125 = Coupling(name = 'GC_2125',
                   value = '(2*ee*VV2x2*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2126 = Coupling(name = 'GC_2126',
                   value = '-(ee*VV2x2*cmath.cos(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2127 = Coupling(name = 'GC_2127',
                   value = '(ee*complex(0,1)*VV2x2*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2128 = Coupling(name = 'GC_2128',
                   value = '(yu3x3*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2129 = Coupling(name = 'GC_2129',
                   value = '-(ee*complex(0,1)*complexconjugate(NN1x4)*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2130 = Coupling(name = 'GC_2130',
                   value = '(ee*complexconjugate(NN1x4)*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2131 = Coupling(name = 'GC_2131',
                   value = '-(ee*complex(0,1)*complexconjugate(NN2x4)*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2132 = Coupling(name = 'GC_2132',
                   value = '(ee*complexconjugate(NN2x4)*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2133 = Coupling(name = 'GC_2133',
                   value = '-(ee*complex(0,1)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2134 = Coupling(name = 'GC_2134',
                   value = '(ee*complexconjugate(NN3x4)*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2135 = Coupling(name = 'GC_2135',
                   value = '-(ee*complex(0,1)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2136 = Coupling(name = 'GC_2136',
                   value = '(ee*complexconjugate(NN4x4)*cmath.cos(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2137 = Coupling(name = 'GC_2137',
                   value = '-((complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_2138 = Coupling(name = 'GC_2138',
                   value = '(complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta)*cmath.sqrt(2))/MP',
                   order = {'QGR':1})

GC_2139 = Coupling(name = 'GC_2139',
                   value = '-((ee*complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2140 = Coupling(name = 'GC_2140',
                   value = '(ee*complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta)*cmath.sqrt(2))/MP',
                   order = {'QED':1,'QGR':1})

GC_2141 = Coupling(name = 'GC_2141',
                   value = '(complexconjugate(VV1x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_2142 = Coupling(name = 'GC_2142',
                   value = '(ee*complexconjugate(VV1x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2143 = Coupling(name = 'GC_2143',
                   value = '-(ee*complexconjugate(VV1x2)*cmath.cos(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2144 = Coupling(name = 'GC_2144',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2145 = Coupling(name = 'GC_2145',
                   value = '(cw*ee*complex(0,1)*complexconjugate(VV1x2)*cmath.cos(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2146 = Coupling(name = 'GC_2146',
                   value = '-((cw*ee*complex(0,1)*sw*complexconjugate(VV1x2)*cmath.cos(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2147 = Coupling(name = 'GC_2147',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(VV1x2)*cmath.cos(beta)*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2148 = Coupling(name = 'GC_2148',
                   value = '-((complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QGR':1})

GC_2149 = Coupling(name = 'GC_2149',
                   value = '(complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta)*cmath.sqrt(2))/MP',
                   order = {'QGR':1})

GC_2150 = Coupling(name = 'GC_2150',
                   value = '-((ee*complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2151 = Coupling(name = 'GC_2151',
                   value = '(ee*complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta)*cmath.sqrt(2))/MP',
                   order = {'QED':1,'QGR':1})

GC_2152 = Coupling(name = 'GC_2152',
                   value = '(complexconjugate(VV2x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QGR':1})

GC_2153 = Coupling(name = 'GC_2153',
                   value = '(ee*complexconjugate(VV2x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2154 = Coupling(name = 'GC_2154',
                   value = '-(ee*complexconjugate(VV2x2)*cmath.cos(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2155 = Coupling(name = 'GC_2155',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2156 = Coupling(name = 'GC_2156',
                   value = '(cw*ee*complex(0,1)*complexconjugate(VV2x2)*cmath.cos(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2157 = Coupling(name = 'GC_2157',
                   value = '-((cw*ee*complex(0,1)*sw*complexconjugate(VV2x2)*cmath.cos(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2158 = Coupling(name = 'GC_2158',
                   value = '(cw*ee*complex(0,1)*sw*complexconjugate(VV2x2)*cmath.cos(beta)*cmath.sqrt(2))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2159 = Coupling(name = 'GC_2159',
                   value = '-((complexconjugate(yu3x3)*cmath.cos(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2160 = Coupling(name = 'GC_2160',
                   value = '-(cw*ee*complex(0,1)*VV1x2*cmath.cos(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*VV1x2*cmath.cos(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2161 = Coupling(name = 'GC_2161',
                   value = '-((cw*ee*VV1x2*cmath.cos(beta))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (2*cw*ee*sw*VV1x2*cmath.cos(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2162 = Coupling(name = 'GC_2162',
                   value = '(ee*complex(0,1)*NN1x4*VV1x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x4*sw*VV1x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*VV1x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2163 = Coupling(name = 'GC_2163',
                   value = '(ee*complex(0,1)*NN2x4*VV1x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x4*sw*VV1x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*VV1x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2164 = Coupling(name = 'GC_2164',
                   value = '(ee*complex(0,1)*NN3x4*VV1x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x4*sw*VV1x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*VV1x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2165 = Coupling(name = 'GC_2165',
                   value = '(ee*complex(0,1)*NN4x4*VV1x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x4*sw*VV1x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*VV1x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*VV1x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2166 = Coupling(name = 'GC_2166',
                   value = '-(cw*ee*complex(0,1)*VV2x2*cmath.cos(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (cw*ee*complex(0,1)*sw*VV2x2*cmath.cos(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2167 = Coupling(name = 'GC_2167',
                   value = '-((cw*ee*VV2x2*cmath.cos(beta))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3))) + (2*cw*ee*sw*VV2x2*cmath.cos(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2168 = Coupling(name = 'GC_2168',
                   value = '(ee*complex(0,1)*NN1x4*VV2x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x4*sw*VV2x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*VV2x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*sw*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2169 = Coupling(name = 'GC_2169',
                   value = '(ee*complex(0,1)*NN2x4*VV2x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x4*sw*VV2x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*VV2x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*sw*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2170 = Coupling(name = 'GC_2170',
                   value = '(ee*complex(0,1)*NN3x4*VV2x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x4*sw*VV2x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*VV2x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*sw*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2171 = Coupling(name = 'GC_2171',
                   value = '(ee*complex(0,1)*NN4x4*VV2x1*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x4*sw*VV2x1*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*VV2x2*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*sw*VV2x2*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2172 = Coupling(name = 'GC_2172',
                   value = '-(cw*ee*complexconjugate(VV1x2)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (cw*ee*sw*complexconjugate(VV1x2)*cmath.cos(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2173 = Coupling(name = 'GC_2173',
                   value = '(ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2174 = Coupling(name = 'GC_2174',
                   value = '(ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2175 = Coupling(name = 'GC_2175',
                   value = '(ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2176 = Coupling(name = 'GC_2176',
                   value = '(ee*complex(0,1)*complexconjugate(NN4x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x4)*complexconjugate(VV1x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(VV1x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2177 = Coupling(name = 'GC_2177',
                   value = '-(cw*ee*complexconjugate(VV2x2)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) + (cw*ee*sw*complexconjugate(VV2x2)*cmath.cos(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2178 = Coupling(name = 'GC_2178',
                   value = '(ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2179 = Coupling(name = 'GC_2179',
                   value = '(ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2180 = Coupling(name = 'GC_2180',
                   value = '(ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2181 = Coupling(name = 'GC_2181',
                   value = '(ee*complex(0,1)*complexconjugate(NN4x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x4)*complexconjugate(VV2x1)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(VV2x2)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2182 = Coupling(name = 'GC_2182',
                   value = '(complex(0,1)*I12x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2183 = Coupling(name = 'GC_2183',
                   value = '(complex(0,1)*I12x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2184 = Coupling(name = 'GC_2184',
                   value = '-(complex(0,1)*I14x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2185 = Coupling(name = 'GC_2185',
                   value = '-(complex(0,1)*I14x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2186 = Coupling(name = 'GC_2186',
                   value = '(complex(0,1)*I17x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2187 = Coupling(name = 'GC_2187',
                   value = '(complex(0,1)*I17x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2188 = Coupling(name = 'GC_2188',
                   value = '-(complex(0,1)*I18x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2189 = Coupling(name = 'GC_2189',
                   value = '-(complex(0,1)*I18x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2190 = Coupling(name = 'GC_2190',
                   value = '-(complex(0,1)*I21x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2191 = Coupling(name = 'GC_2191',
                   value = '-(complex(0,1)*I21x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2192 = Coupling(name = 'GC_2192',
                   value = '(complex(0,1)*I22x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2193 = Coupling(name = 'GC_2193',
                   value = '(complex(0,1)*I22x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2194 = Coupling(name = 'GC_2194',
                   value = '(complex(0,1)*I27x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2195 = Coupling(name = 'GC_2195',
                   value = '(complex(0,1)*I27x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2196 = Coupling(name = 'GC_2196',
                   value = '-(complex(0,1)*I28x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2197 = Coupling(name = 'GC_2197',
                   value = '-(complex(0,1)*I28x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2198 = Coupling(name = 'GC_2198',
                   value = '(complex(0,1)*I37x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2199 = Coupling(name = 'GC_2199',
                   value = '(complex(0,1)*I37x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2200 = Coupling(name = 'GC_2200',
                   value = '-(complex(0,1)*I38x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2201 = Coupling(name = 'GC_2201',
                   value = '-(complex(0,1)*I38x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2202 = Coupling(name = 'GC_2202',
                   value = '-(complex(0,1)*I43x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2203 = Coupling(name = 'GC_2203',
                   value = '-(complex(0,1)*I43x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2204 = Coupling(name = 'GC_2204',
                   value = '(complex(0,1)*I44x33*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2205 = Coupling(name = 'GC_2205',
                   value = '(complex(0,1)*I44x36*cmath.sin(alp))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2206 = Coupling(name = 'GC_2206',
                   value = '(I12x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2207 = Coupling(name = 'GC_2207',
                   value = '(I12x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2208 = Coupling(name = 'GC_2208',
                   value = '-((I14x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2209 = Coupling(name = 'GC_2209',
                   value = '-((I14x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2210 = Coupling(name = 'GC_2210',
                   value = '(I17x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2211 = Coupling(name = 'GC_2211',
                   value = '(I17x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2212 = Coupling(name = 'GC_2212',
                   value = '-((I18x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2213 = Coupling(name = 'GC_2213',
                   value = '-((I18x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2214 = Coupling(name = 'GC_2214',
                   value = '-((I21x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2215 = Coupling(name = 'GC_2215',
                   value = '-((I21x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2216 = Coupling(name = 'GC_2216',
                   value = '(I22x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2217 = Coupling(name = 'GC_2217',
                   value = '(I22x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2218 = Coupling(name = 'GC_2218',
                   value = '(I27x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2219 = Coupling(name = 'GC_2219',
                   value = '(I27x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2220 = Coupling(name = 'GC_2220',
                   value = '-((I28x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2221 = Coupling(name = 'GC_2221',
                   value = '-((I28x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2222 = Coupling(name = 'GC_2222',
                   value = '(I37x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2223 = Coupling(name = 'GC_2223',
                   value = '(I37x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2224 = Coupling(name = 'GC_2224',
                   value = '-((I38x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2225 = Coupling(name = 'GC_2225',
                   value = '-((I38x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2226 = Coupling(name = 'GC_2226',
                   value = '-((I43x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2227 = Coupling(name = 'GC_2227',
                   value = '-((I43x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2228 = Coupling(name = 'GC_2228',
                   value = '(I44x33*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2229 = Coupling(name = 'GC_2229',
                   value = '(I44x36*cmath.sin(alp))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2230 = Coupling(name = 'GC_2230',
                   value = '(ee*complex(0,1)*UU1x2*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2231 = Coupling(name = 'GC_2231',
                   value = '-(ee*UU1x2*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2232 = Coupling(name = 'GC_2232',
                   value = '(ee*complex(0,1)*UU2x2*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2233 = Coupling(name = 'GC_2233',
                   value = '-(ee*UU2x2*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2234 = Coupling(name = 'GC_2234',
                   value = '(ee*complex(0,1)*VV1x2*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2235 = Coupling(name = 'GC_2235',
                   value = '(ee*VV1x2*cmath.sin(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2236 = Coupling(name = 'GC_2236',
                   value = '(ee*complex(0,1)*VV2x2*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2237 = Coupling(name = 'GC_2237',
                   value = '(ee*VV2x2*cmath.sin(alp))/(M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2238 = Coupling(name = 'GC_2238',
                   value = '(complex(0,1)*yd3x3*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2239 = Coupling(name = 'GC_2239',
                   value = '(complex(0,1)*ye3x3*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2240 = Coupling(name = 'GC_2240',
                   value = '-((complex(0,1)*yu3x3*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2241 = Coupling(name = 'GC_2241',
                   value = '-(ee*complex(0,1)*complexconjugate(UU1x2)*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2242 = Coupling(name = 'GC_2242',
                   value = '-((ee*complexconjugate(UU1x2)*cmath.sin(alp))/(M32*MP*sw*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2243 = Coupling(name = 'GC_2243',
                   value = '-(ee*complex(0,1)*complexconjugate(UU2x2)*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2244 = Coupling(name = 'GC_2244',
                   value = '-((ee*complexconjugate(UU2x2)*cmath.sin(alp))/(M32*MP*sw*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2245 = Coupling(name = 'GC_2245',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x2)*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2246 = Coupling(name = 'GC_2246',
                   value = '(ee*complexconjugate(VV1x2)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2247 = Coupling(name = 'GC_2247',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x2)*cmath.sin(alp))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2248 = Coupling(name = 'GC_2248',
                   value = '(ee*complexconjugate(VV2x2)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2249 = Coupling(name = 'GC_2249',
                   value = '(complex(0,1)*complexconjugate(yd3x3)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2250 = Coupling(name = 'GC_2250',
                   value = '(complex(0,1)*complexconjugate(ye3x3)*cmath.sin(alp))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2251 = Coupling(name = 'GC_2251',
                   value = '-((complex(0,1)*complexconjugate(yu3x3)*cmath.sin(alp))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2252 = Coupling(name = 'GC_2252',
                   value = '-(cw*ee*complex(0,1)*NN1x4*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x3*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2253 = Coupling(name = 'GC_2253',
                   value = '(cw*ee*NN1x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2254 = Coupling(name = 'GC_2254',
                   value = '(cw*ee*complex(0,1)*NN1x3*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN1x4*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2255 = Coupling(name = 'GC_2255',
                   value = '-(cw*ee*NN1x3*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x4*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2256 = Coupling(name = 'GC_2256',
                   value = '-(cw*ee*complex(0,1)*NN2x4*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x3*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2257 = Coupling(name = 'GC_2257',
                   value = '(cw*ee*NN2x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2258 = Coupling(name = 'GC_2258',
                   value = '(cw*ee*complex(0,1)*NN2x3*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN2x4*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2259 = Coupling(name = 'GC_2259',
                   value = '-(cw*ee*NN2x3*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x4*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2260 = Coupling(name = 'GC_2260',
                   value = '-(cw*ee*complex(0,1)*NN3x4*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x3*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2261 = Coupling(name = 'GC_2261',
                   value = '(cw*ee*NN3x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2262 = Coupling(name = 'GC_2262',
                   value = '(cw*ee*complex(0,1)*NN3x3*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN3x4*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2263 = Coupling(name = 'GC_2263',
                   value = '-(cw*ee*NN3x3*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x4*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2264 = Coupling(name = 'GC_2264',
                   value = '-(cw*ee*complex(0,1)*NN4x4*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x3*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2265 = Coupling(name = 'GC_2265',
                   value = '(cw*ee*NN4x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2266 = Coupling(name = 'GC_2266',
                   value = '(cw*ee*complex(0,1)*NN4x3*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN4x4*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2267 = Coupling(name = 'GC_2267',
                   value = '-(cw*ee*NN4x3*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x4*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2268 = Coupling(name = 'GC_2268',
                   value = '(cw*ee*complex(0,1)*NN1x1*NN1x4*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN1x4*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN1x4*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN1x3*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN1x3*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN1x3*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2269 = Coupling(name = 'GC_2269',
                   value = '-((cw*ee*complex(0,1)*NN1x1*NN1x3*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN1x2*NN1x3*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN1x3*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN1x4*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN1x4*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN1x4*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2270 = Coupling(name = 'GC_2270',
                   value = '(cw*ee*complex(0,1)*NN1x4*NN2x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN2x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN2x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN2x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN2x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN2x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x3*NN2x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN2x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN2x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN2x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN2x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN2x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2271 = Coupling(name = 'GC_2271',
                   value = '(cw*ee*complex(0,1)*NN2x1*NN2x4*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN2x4*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN2x4*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN2x3*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN2x3*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN2x3*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2272 = Coupling(name = 'GC_2272',
                   value = '-(cw*ee*complex(0,1)*NN1x3*NN2x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*NN2x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN2x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN2x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN2x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN2x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*NN2x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN2x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN2x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN2x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN2x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN2x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2273 = Coupling(name = 'GC_2273',
                   value = '-((cw*ee*complex(0,1)*NN2x1*NN2x3*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN2x2*NN2x3*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN2x3*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN2x4*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN2x4*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN2x4*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2274 = Coupling(name = 'GC_2274',
                   value = '(cw*ee*complex(0,1)*NN1x4*NN3x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN3x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN3x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN3x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN3x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN3x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x3*NN3x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN3x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN3x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN3x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN3x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN3x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2275 = Coupling(name = 'GC_2275',
                   value = '(cw*ee*complex(0,1)*NN2x4*NN3x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN3x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x4*NN3x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN3x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x4*NN3x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN3x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x3*NN3x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN3x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x3*NN3x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN3x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x3*NN3x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN3x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2276 = Coupling(name = 'GC_2276',
                   value = '(cw*ee*complex(0,1)*NN3x1*NN3x4*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN3x4*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN3x4*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*NN3x3*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN3x3*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN3x3*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2277 = Coupling(name = 'GC_2277',
                   value = '-(cw*ee*complex(0,1)*NN1x3*NN3x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*NN3x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN3x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN3x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN3x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN3x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*NN3x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN3x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN3x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN3x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN3x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN3x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2278 = Coupling(name = 'GC_2278',
                   value = '-(cw*ee*complex(0,1)*NN2x3*NN3x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*NN3x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x3*NN3x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN3x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x3*NN3x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN3x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x4*NN3x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN3x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x4*NN3x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN3x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x4*NN3x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN3x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2279 = Coupling(name = 'GC_2279',
                   value = '-((cw*ee*complex(0,1)*NN3x1*NN3x3*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN3x2*NN3x3*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN3x3*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*NN3x4*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN3x4*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN3x4*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2280 = Coupling(name = 'GC_2280',
                   value = '(cw*ee*complex(0,1)*NN1x4*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN4x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x3*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN4x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2281 = Coupling(name = 'GC_2281',
                   value = '(cw*ee*complex(0,1)*NN2x4*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x4*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x4*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN4x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x3*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x3*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x3*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN4x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2282 = Coupling(name = 'GC_2282',
                   value = '(cw*ee*complex(0,1)*NN3x4*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x4*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN4x4*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x4*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN4x4*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x3*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x3*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN4x3*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x3*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN4x3*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2283 = Coupling(name = 'GC_2283',
                   value = '(cw*ee*complex(0,1)*NN4x1*NN4x4*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*NN4x4*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*NN4x4*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*NN4x3*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*NN4x3*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*NN4x3*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2284 = Coupling(name = 'GC_2284',
                   value = '-(cw*ee*complex(0,1)*NN1x3*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x3*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x3*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN4x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x4*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x4*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x4*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*NN4x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2285 = Coupling(name = 'GC_2285',
                   value = '-(cw*ee*complex(0,1)*NN2x3*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x3*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x3*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN4x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x4*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x4*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x4*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*NN4x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2286 = Coupling(name = 'GC_2286',
                   value = '-(cw*ee*complex(0,1)*NN3x3*NN4x1*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x3*NN4x2*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN4x3*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x3*NN4x2*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN4x3*sw*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x4*NN4x1*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x4*NN4x2*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*NN4x4*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x4*NN4x2*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*NN4x4*sw*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2287 = Coupling(name = 'GC_2287',
                   value = '-((cw*ee*complex(0,1)*NN4x1*NN4x3*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN4x2*NN4x3*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*NN4x3*sw*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*NN4x4*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*NN4x4*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*NN4x4*sw*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2288 = Coupling(name = 'GC_2288',
                   value = '(complex(0,1)*NN1x4*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x4*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x3*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2289 = Coupling(name = 'GC_2289',
                   value = '(NN1x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x4*sw**2*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x3*sw**2*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2290 = Coupling(name = 'GC_2290',
                   value = '(complex(0,1)*NN1x3*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x4*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x4*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2291 = Coupling(name = 'GC_2291',
                   value = '(NN1x3*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN1x3*sw**2*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) + (NN1x4*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN1x4*sw**2*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2292 = Coupling(name = 'GC_2292',
                   value = '-((NN1x3*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (NN1x3*sw**2*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x4*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x4*sw**2*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2293 = Coupling(name = 'GC_2293',
                   value = '(complex(0,1)*NN2x4*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x4*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x3*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2294 = Coupling(name = 'GC_2294',
                   value = '(NN2x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x4*sw**2*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x3*sw**2*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2295 = Coupling(name = 'GC_2295',
                   value = '(complex(0,1)*NN2x3*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x4*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x4*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2296 = Coupling(name = 'GC_2296',
                   value = '(NN2x3*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN2x3*sw**2*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) + (NN2x4*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN2x4*sw**2*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2297 = Coupling(name = 'GC_2297',
                   value = '-((NN2x3*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (NN2x3*sw**2*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x4*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x4*sw**2*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2298 = Coupling(name = 'GC_2298',
                   value = '(complex(0,1)*NN3x4*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x4*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x3*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2299 = Coupling(name = 'GC_2299',
                   value = '(NN3x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x4*sw**2*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x3*sw**2*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2300 = Coupling(name = 'GC_2300',
                   value = '(complex(0,1)*NN3x3*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x4*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x4*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2301 = Coupling(name = 'GC_2301',
                   value = '(NN3x3*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN3x3*sw**2*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) + (NN3x4*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN3x4*sw**2*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2302 = Coupling(name = 'GC_2302',
                   value = '-((NN3x3*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (NN3x3*sw**2*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x4*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x4*sw**2*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2303 = Coupling(name = 'GC_2303',
                   value = '(complex(0,1)*NN4x4*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x4*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x3*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2304 = Coupling(name = 'GC_2304',
                   value = '(NN4x4*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x4*sw**2*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x3*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x3*sw**2*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2305 = Coupling(name = 'GC_2305',
                   value = '(complex(0,1)*NN4x3*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*sw**2*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x4*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x4*sw**2*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2306 = Coupling(name = 'GC_2306',
                   value = '(NN4x3*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN4x3*sw**2*cmath.cos(alp)*cmath.sqrt(0.6666666666666666))/(M32*MP*(-1 + sw)*(1 + sw)) + (NN4x4*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)) - (NN4x4*sw**2*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2307 = Coupling(name = 'GC_2307',
                   value = '-((NN4x3*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (NN4x3*sw**2*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x4*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x4*sw**2*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2308 = Coupling(name = 'GC_2308',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*sw**2) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_2309 = Coupling(name = 'GC_2309',
                   value = '-(ee**2*complex(0,1)*I109x44*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x44*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2310 = Coupling(name = 'GC_2310',
                   value = '-(ee**2*complex(0,1)*I109x55*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x55*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2311 = Coupling(name = 'GC_2311',
                   value = '(ee**2*complex(0,1)*I46x44*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x44*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2312 = Coupling(name = 'GC_2312',
                   value = '(ee**2*complex(0,1)*I46x55*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x55*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2313 = Coupling(name = 'GC_2313',
                   value = '(ee**2*complex(0,1)*I80x44*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2314 = Coupling(name = 'GC_2314',
                   value = '(ee**2*complex(0,1)*I80x55*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2315 = Coupling(name = 'GC_2315',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2316 = Coupling(name = 'GC_2316',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2317 = Coupling(name = 'GC_2317',
                   value = '(ee**2*complex(0,1)*I108x11*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I108x11*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2318 = Coupling(name = 'GC_2318',
                   value = '(ee**2*complex(0,1)*I108x22*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I108x22*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2319 = Coupling(name = 'GC_2319',
                   value = '-(ee**2*complex(0,1)*I45x11*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I45x11*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2320 = Coupling(name = 'GC_2320',
                   value = '-(ee**2*complex(0,1)*I45x22*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I45x22*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2321 = Coupling(name = 'GC_2321',
                   value = '-(ee**2*complex(0,1)*I79x11*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x11*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I79x11*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x11*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2322 = Coupling(name = 'GC_2322',
                   value = '-(ee**2*complex(0,1)*I79x22*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x22*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I79x22*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x22*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2323 = Coupling(name = 'GC_2323',
                   value = '-(ee**2*complex(0,1)*I45x33*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x33*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x33*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x33*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I61x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I56x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2324 = Coupling(name = 'GC_2324',
                   value = '-(ee**2*complex(0,1)*I45x36*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x36*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x36*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x36*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I61x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I56x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2325 = Coupling(name = 'GC_2325',
                   value = '-(ee**2*complex(0,1)*I45x63*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x63*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x63*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x63*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I61x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I56x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2326 = Coupling(name = 'GC_2326',
                   value = '-(ee**2*complex(0,1)*I45x66*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x66*vu*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x66*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x66*vd*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I61x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I61x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I56x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I56x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2327 = Coupling(name = 'GC_2327',
                   value = '-(ee**2*complex(0,1)*I79x33*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x33*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x33*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I88x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x33*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I85x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I85x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2328 = Coupling(name = 'GC_2328',
                   value = '-(ee**2*complex(0,1)*I79x36*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x36*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x36*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I88x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x36*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I85x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I85x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2329 = Coupling(name = 'GC_2329',
                   value = '-(ee**2*complex(0,1)*I79x63*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x63*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x63*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I88x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x63*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I85x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I85x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2330 = Coupling(name = 'GC_2330',
                   value = '-(ee**2*complex(0,1)*I79x66*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*vu*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x66*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*vd*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I88x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x66*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I88x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x66*sw**2*vd*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I85x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I85x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2331 = Coupling(name = 'GC_2331',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*sw**2) + (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*sw**2)',
                   order = {'QED':1})

GC_2332 = Coupling(name = 'GC_2332',
                   value = '(ee**2*complex(0,1)*I109x44*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x44*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2333 = Coupling(name = 'GC_2333',
                   value = '(ee**2*complex(0,1)*I109x55*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x55*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2334 = Coupling(name = 'GC_2334',
                   value = '-(ee**2*complex(0,1)*I46x44*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x44*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2335 = Coupling(name = 'GC_2335',
                   value = '-(ee**2*complex(0,1)*I46x55*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x55*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2336 = Coupling(name = 'GC_2336',
                   value = '-(ee**2*complex(0,1)*I80x44*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x44*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2337 = Coupling(name = 'GC_2337',
                   value = '-(ee**2*complex(0,1)*I80x55*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x55*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2338 = Coupling(name = 'GC_2338',
                   value = '(ee**2*complex(0,1)*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2339 = Coupling(name = 'GC_2339',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2340 = Coupling(name = 'GC_2340',
                   value = '-(ee**2*complex(0,1)*I108x11*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I108x11*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2341 = Coupling(name = 'GC_2341',
                   value = '-(ee**2*complex(0,1)*I108x22*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I108x22*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2342 = Coupling(name = 'GC_2342',
                   value = '(ee**2*complex(0,1)*I45x11*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I45x11*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2343 = Coupling(name = 'GC_2343',
                   value = '(ee**2*complex(0,1)*I45x22*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I45x22*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2344 = Coupling(name = 'GC_2344',
                   value = '(ee**2*complex(0,1)*I79x11*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x11*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I79x11*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x11*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2345 = Coupling(name = 'GC_2345',
                   value = '(ee**2*complex(0,1)*I79x22*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x22*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I79x22*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x22*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2346 = Coupling(name = 'GC_2346',
                   value = '-(ee**2*complex(0,1)*I108x33*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I109x33*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I131x33*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I131x33*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x33*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x33*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x33*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x33*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x33*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x33*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x33*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x33*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x33*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x33*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2347 = Coupling(name = 'GC_2347',
                   value = '-(ee**2*complex(0,1)*I108x36*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I109x36*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I131x36*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I131x36*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x36*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x36*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x36*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x36*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x36*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x36*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x36*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x36*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x36*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x36*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2348 = Coupling(name = 'GC_2348',
                   value = '-(ee**2*complex(0,1)*I108x63*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I109x63*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I131x63*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I131x63*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x63*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x63*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x63*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x63*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x63*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x63*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x63*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x63*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x63*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x63*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2349 = Coupling(name = 'GC_2349',
                   value = '-(ee**2*complex(0,1)*I108x66*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I109x66*vd*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I108x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I131x66*MUH*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I131x66*MUH*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x66*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x66*sw**2*complexconjugate(MUH)*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x66*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x66*vu*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x66*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x66*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x66*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x66*sw**2*vu*cmath.sin(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x66*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x66*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2350 = Coupling(name = 'GC_2350',
                   value = '-((ee*complex(0,1)*UU1x1*VV1x2*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU1x2*VV1x1*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2351 = Coupling(name = 'GC_2351',
                   value = '-((ee*complex(0,1)*UU2x1*VV1x2*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU2x2*VV1x1*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2352 = Coupling(name = 'GC_2352',
                   value = '-((ee*complex(0,1)*UU1x2*VV1x1*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU1x1*VV1x2*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2353 = Coupling(name = 'GC_2353',
                   value = '-((ee*complex(0,1)*UU2x2*VV1x1*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU2x1*VV1x2*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2354 = Coupling(name = 'GC_2354',
                   value = '-((ee*complex(0,1)*UU1x1*VV2x2*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU1x2*VV2x1*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2355 = Coupling(name = 'GC_2355',
                   value = '-((ee*complex(0,1)*UU2x1*VV2x2*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*UU2x2*VV2x1*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2356 = Coupling(name = 'GC_2356',
                   value = '-((ee*complex(0,1)*UU1x2*VV2x1*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU1x1*VV2x2*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2357 = Coupling(name = 'GC_2357',
                   value = '-((ee*complex(0,1)*UU2x2*VV2x1*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*UU2x1*VV2x2*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2358 = Coupling(name = 'GC_2358',
                   value = '(ee**2*complex(0,1)*I108x33*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x33*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x33*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x33*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x33*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x33*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x33*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x33*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x33*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x33*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I131x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I131x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2359 = Coupling(name = 'GC_2359',
                   value = '(ee**2*complex(0,1)*I108x36*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x36*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x36*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x36*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x36*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x36*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x36*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x36*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x36*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x36*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I131x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I131x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2360 = Coupling(name = 'GC_2360',
                   value = '(ee**2*complex(0,1)*I108x63*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x63*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x63*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x63*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x63*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x63*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x63*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x63*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x63*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x63*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I131x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I131x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2361 = Coupling(name = 'GC_2361',
                   value = '(ee**2*complex(0,1)*I108x66*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x66*vu*cmath.cos(alp))/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I135x66*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I136x66*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x66*vu*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I135x66*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I136x66*sw**2*vu*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I132x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I133x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I132x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I133x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee**2*complex(0,1)*I108x66*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I109x66*vd*cmath.sin(alp))/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I108x66*vd*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*I131x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I131x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I134x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I134x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2362 = Coupling(name = 'GC_2362',
                   value = '(ee**2*complex(0,1)*I45x33*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I46x33*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I56x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I56x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x33*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x33*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2363 = Coupling(name = 'GC_2363',
                   value = '(ee**2*complex(0,1)*I45x36*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I46x36*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I56x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I56x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x36*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x36*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2364 = Coupling(name = 'GC_2364',
                   value = '(ee**2*complex(0,1)*I45x63*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I46x63*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I56x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I56x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x63*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x63*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2365 = Coupling(name = 'GC_2365',
                   value = '(ee**2*complex(0,1)*I45x66*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I46x66*vd*cmath.cos(alp))/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I61x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I63x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I45x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I61x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I63x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I56x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I60x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I56x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I60x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I45x66*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I46x66*vu*cmath.sin(alp))/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I45x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I59x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I59x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I62x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I62x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2366 = Coupling(name = 'GC_2366',
                   value = '(ee**2*complex(0,1)*I79x33*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I80x33*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x33*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x33*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I88x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x33*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I85x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x33*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I85x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x33*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x33*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x33*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x33*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x33*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x33*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x33*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x33*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2367 = Coupling(name = 'GC_2367',
                   value = '(ee**2*complex(0,1)*I79x36*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I80x36*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x36*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x36*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I88x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x36*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I85x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x36*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I85x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x36*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x36*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x36*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x36*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x36*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x36*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x36*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x36*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2368 = Coupling(name = 'GC_2368',
                   value = '(ee**2*complex(0,1)*I79x63*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I80x63*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x63*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x63*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I88x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x63*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I85x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x63*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I85x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x63*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x63*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x63*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x63*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x63*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x63*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x63*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x63*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2369 = Coupling(name = 'GC_2369',
                   value = '(ee**2*complex(0,1)*I79x66*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I80x66*vd*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I88x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I92x66*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I79x66*vd*cmath.cos(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I88x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I92x66*sw**2*vd*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (complex(0,1)*I85x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I87x66*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I85x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I87x66*sw**2*cmath.cos(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee**2*complex(0,1)*I79x66*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I80x66*vu*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I79x66*vu*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I86x66*MUH*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I86x66*MUH*sw**2*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I90x66*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I90x66*sw**2*complexconjugate(MUH)*cmath.sin(alp))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2370 = Coupling(name = 'GC_2370',
                   value = '(cw*ee*complex(0,1)*NN1x1*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x4*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x3*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2371 = Coupling(name = 'GC_2371',
                   value = '(cw*ee*NN1x1*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x4*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN1x1*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x3*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2372 = Coupling(name = 'GC_2372',
                   value = '-(cw*ee*complex(0,1)*NN1x1*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x3*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN1x4*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN1x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2373 = Coupling(name = 'GC_2373',
                   value = '-(cw*ee*NN1x1*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x3*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN1x1*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN1x4*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN1x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2374 = Coupling(name = 'GC_2374',
                   value = '(cw*ee*complex(0,1)*NN2x1*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x4*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x3*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2375 = Coupling(name = 'GC_2375',
                   value = '(cw*ee*NN2x1*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x4*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN2x1*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x3*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2376 = Coupling(name = 'GC_2376',
                   value = '-(cw*ee*complex(0,1)*NN2x1*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x3*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN2x4*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN2x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2377 = Coupling(name = 'GC_2377',
                   value = '-(cw*ee*NN2x1*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x3*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN2x1*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN2x4*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN2x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2378 = Coupling(name = 'GC_2378',
                   value = '(cw*ee*complex(0,1)*NN3x1*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x4*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x3*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2379 = Coupling(name = 'GC_2379',
                   value = '(cw*ee*NN3x1*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x4*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN3x1*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x3*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2380 = Coupling(name = 'GC_2380',
                   value = '-(cw*ee*complex(0,1)*NN3x1*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x3*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN3x4*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN3x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2381 = Coupling(name = 'GC_2381',
                   value = '-(cw*ee*NN3x1*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x3*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN3x1*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN3x4*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN3x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2382 = Coupling(name = 'GC_2382',
                   value = '(cw*ee*complex(0,1)*NN4x1*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw*vd*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x4*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*vu*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x3*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2383 = Coupling(name = 'GC_2383',
                   value = '(cw*ee*NN4x1*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw*vd*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x4*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x4*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN4x1*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*vu*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x3*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x3*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2384 = Coupling(name = 'GC_2384',
                   value = '-(cw*ee*complex(0,1)*NN4x1*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*vu*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x3*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*vd*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*NN4x4*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*NN4x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2385 = Coupling(name = 'GC_2385',
                   value = '-(cw*ee*NN4x1*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*vu*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x3*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x3*sw**2*complexconjugate(MUH)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN4x1*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*vd*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (NN4x4*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (NN4x4*sw**2*complexconjugate(MUH)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2386 = Coupling(name = 'GC_2386',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x4)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x3)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2387 = Coupling(name = 'GC_2387',
                   value = '(cw*ee*complexconjugate(NN1x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN1x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2388 = Coupling(name = 'GC_2388',
                   value = '-((complex(0,1)*complexconjugate(NN1x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN1x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*complexconjugate(NN1x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*sw**2*complexconjugate(NN1x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2389 = Coupling(name = 'GC_2389',
                   value = '-(complexconjugate(NN1x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN1x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (complexconjugate(NN1x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN1x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2390 = Coupling(name = 'GC_2390',
                   value = '-(cw*ee*complex(0,1)*vd*complexconjugate(NN1x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*vd*complexconjugate(NN1x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*vd*complexconjugate(NN1x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN1x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN1x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vu*complexconjugate(NN1x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN1x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN1x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN1x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN1x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2391 = Coupling(name = 'GC_2391',
                   value = '-(cw*ee*vd*complexconjugate(NN1x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*vd*complexconjugate(NN1x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*vd*complexconjugate(NN1x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN1x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN1x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN1x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN1x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN1x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN1x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN1x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2392 = Coupling(name = 'GC_2392',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN1x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN1x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2393 = Coupling(name = 'GC_2393',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x3)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x4)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2394 = Coupling(name = 'GC_2394',
                   value = '-(cw*ee*complexconjugate(NN1x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN1x4)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2395 = Coupling(name = 'GC_2395',
                   value = '-((complex(0,1)*complexconjugate(NN1x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN1x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*complexconjugate(NN1x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*sw**2*complexconjugate(NN1x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2396 = Coupling(name = 'GC_2396',
                   value = '-((complexconjugate(NN1x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))) + (sw**2*complexconjugate(NN1x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2397 = Coupling(name = 'GC_2397',
                   value = '(complexconjugate(NN1x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN1x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2398 = Coupling(name = 'GC_2398',
                   value = '(cw*ee*complex(0,1)*vu*complexconjugate(NN1x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN1x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN1x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN1x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN1x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vd*complexconjugate(NN1x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vd*complexconjugate(NN1x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vd*complexconjugate(NN1x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*complexconjugate(NN1x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*sw**2*complexconjugate(NN1x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2399 = Coupling(name = 'GC_2399',
                   value = '(cw*ee*vu*complexconjugate(NN1x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN1x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN1x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN1x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN1x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vd*complexconjugate(NN1x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vd*complexconjugate(NN1x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vd*complexconjugate(NN1x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*complexconjugate(NN1x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*sw**2*complexconjugate(NN1x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2400 = Coupling(name = 'GC_2400',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN1x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN1x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2401 = Coupling(name = 'GC_2401',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x4)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x3)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2402 = Coupling(name = 'GC_2402',
                   value = '(cw*ee*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2403 = Coupling(name = 'GC_2403',
                   value = '-((complex(0,1)*complexconjugate(NN2x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN2x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*complexconjugate(NN2x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*sw**2*complexconjugate(NN2x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2404 = Coupling(name = 'GC_2404',
                   value = '-(complexconjugate(NN2x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (complexconjugate(NN2x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2405 = Coupling(name = 'GC_2405',
                   value = '-(cw*ee*complex(0,1)*vd*complexconjugate(NN2x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*vd*complexconjugate(NN2x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*vd*complexconjugate(NN2x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vu*complexconjugate(NN2x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN2x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN2x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2406 = Coupling(name = 'GC_2406',
                   value = '-(cw*ee*vd*complexconjugate(NN2x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*vd*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*vd*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN2x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN2x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN2x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN2x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN2x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2407 = Coupling(name = 'GC_2407',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN2x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN2x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2408 = Coupling(name = 'GC_2408',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN2x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN2x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2409 = Coupling(name = 'GC_2409',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x3)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x4)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2410 = Coupling(name = 'GC_2410',
                   value = '-(cw*ee*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2411 = Coupling(name = 'GC_2411',
                   value = '-((complex(0,1)*complexconjugate(NN2x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN2x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*complexconjugate(NN2x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*sw**2*complexconjugate(NN2x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2412 = Coupling(name = 'GC_2412',
                   value = '-((complexconjugate(NN2x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))) + (sw**2*complexconjugate(NN2x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2413 = Coupling(name = 'GC_2413',
                   value = '(complexconjugate(NN2x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN2x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2414 = Coupling(name = 'GC_2414',
                   value = '(cw*ee*complex(0,1)*vu*complexconjugate(NN2x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN2x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN2x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vd*complexconjugate(NN2x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vd*complexconjugate(NN2x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vd*complexconjugate(NN2x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*sw**2*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2415 = Coupling(name = 'GC_2415',
                   value = '(cw*ee*vu*complexconjugate(NN2x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN2x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN2x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vd*complexconjugate(NN2x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vd*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vd*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*complexconjugate(NN2x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*sw**2*complexconjugate(NN2x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2416 = Coupling(name = 'GC_2416',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN2x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN2x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2417 = Coupling(name = 'GC_2417',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN2x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN2x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2418 = Coupling(name = 'GC_2418',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN3x4)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x3)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2419 = Coupling(name = 'GC_2419',
                   value = '(cw*ee*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2420 = Coupling(name = 'GC_2420',
                   value = '-((complex(0,1)*complexconjugate(NN3x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN3x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*complexconjugate(NN3x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*sw**2*complexconjugate(NN3x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2421 = Coupling(name = 'GC_2421',
                   value = '-(complexconjugate(NN3x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (complexconjugate(NN3x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2422 = Coupling(name = 'GC_2422',
                   value = '-(cw*ee*complex(0,1)*vd*complexconjugate(NN3x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*vd*complexconjugate(NN3x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*vd*complexconjugate(NN3x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vu*complexconjugate(NN3x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN3x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN3x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2423 = Coupling(name = 'GC_2423',
                   value = '-(cw*ee*vd*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*vd*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*vd*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN3x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN3x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN3x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN3x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2424 = Coupling(name = 'GC_2424',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2425 = Coupling(name = 'GC_2425',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2426 = Coupling(name = 'GC_2426',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN3x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN3x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2427 = Coupling(name = 'GC_2427',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x3)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x4)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2428 = Coupling(name = 'GC_2428',
                   value = '-(cw*ee*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2429 = Coupling(name = 'GC_2429',
                   value = '-((complex(0,1)*complexconjugate(NN3x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN3x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*complexconjugate(NN3x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*sw**2*complexconjugate(NN3x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2430 = Coupling(name = 'GC_2430',
                   value = '-((complexconjugate(NN3x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))) + (sw**2*complexconjugate(NN3x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2431 = Coupling(name = 'GC_2431',
                   value = '(complexconjugate(NN3x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN3x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2432 = Coupling(name = 'GC_2432',
                   value = '(cw*ee*complex(0,1)*vu*complexconjugate(NN3x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN3x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN3x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vd*complexconjugate(NN3x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vd*complexconjugate(NN3x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vd*complexconjugate(NN3x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*sw**2*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2433 = Coupling(name = 'GC_2433',
                   value = '(cw*ee*vu*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN3x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN3x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vd*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vd*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vd*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*complexconjugate(NN3x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*sw**2*complexconjugate(NN3x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2434 = Coupling(name = 'GC_2434',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2435 = Coupling(name = 'GC_2435',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN3x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN3x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2436 = Coupling(name = 'GC_2436',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN3x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN3x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2437 = Coupling(name = 'GC_2437',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN4x4)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x3)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2438 = Coupling(name = 'GC_2438',
                   value = '(cw*ee*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2439 = Coupling(name = 'GC_2439',
                   value = '-((complex(0,1)*complexconjugate(NN4x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN4x4)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*complexconjugate(NN4x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*sw**2*complexconjugate(NN4x3)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2440 = Coupling(name = 'GC_2440',
                   value = '-(complexconjugate(NN4x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (sw**2*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (complexconjugate(NN4x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2441 = Coupling(name = 'GC_2441',
                   value = '-(cw*ee*complex(0,1)*vd*complexconjugate(NN4x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*vd*complexconjugate(NN4x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*vd*complexconjugate(NN4x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vu*complexconjugate(NN4x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN4x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN4x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2442 = Coupling(name = 'GC_2442',
                   value = '-(cw*ee*vd*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*vd*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*vd*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN4x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN4x4)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vu*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN4x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN4x3)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2443 = Coupling(name = 'GC_2443',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2444 = Coupling(name = 'GC_2444',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2445 = Coupling(name = 'GC_2445',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2446 = Coupling(name = 'GC_2446',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(NN4x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(NN4x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2447 = Coupling(name = 'GC_2447',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x3)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x4)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2448 = Coupling(name = 'GC_2448',
                   value = '-(cw*ee*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2449 = Coupling(name = 'GC_2449',
                   value = '-((complex(0,1)*complexconjugate(NN4x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw))) + (complex(0,1)*sw**2*complexconjugate(NN4x3)*cmath.cos(alp))/(MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*complexconjugate(NN4x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*sw**2*complexconjugate(NN4x4)*cmath.sin(alp))/(MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2450 = Coupling(name = 'GC_2450',
                   value = '-((complexconjugate(NN4x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))) + (sw**2*complexconjugate(NN4x4)*cmath.sqrt(0.6666666666666666)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2451 = Coupling(name = 'GC_2451',
                   value = '(complexconjugate(NN4x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (sw**2*complexconjugate(NN4x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2452 = Coupling(name = 'GC_2452',
                   value = '(cw*ee*complex(0,1)*vu*complexconjugate(NN4x1)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vu*complexconjugate(NN4x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vu*complexconjugate(NN4x2)*cmath.cos(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*sw**2*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*vd*complexconjugate(NN4x1)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*vd*complexconjugate(NN4x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*vd*complexconjugate(NN4x2)*cmath.sin(alp))/(4.*MP*(-1 + sw)*(1 + sw)) + (complex(0,1)*MUH*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (complex(0,1)*MUH*sw**2*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QGR':1})

GC_2453 = Coupling(name = 'GC_2453',
                   value = '(cw*ee*vu*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vu*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vu*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*complexconjugate(NN4x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*sw**2*complexconjugate(NN4x3)*cmath.cos(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*vd*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*vd*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*vd*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (MUH*complexconjugate(NN4x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (MUH*sw**2*complexconjugate(NN4x4)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2454 = Coupling(name = 'GC_2454',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2455 = Coupling(name = 'GC_2455',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2456 = Coupling(name = 'GC_2456',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(NN4x1)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.cos(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(NN4x1)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2457 = Coupling(name = 'GC_2457',
                   value = '-((cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(NN4x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.cos(alp))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.cos(alp))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(NN4x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.sin(alp))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.sin(alp))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2458 = Coupling(name = 'GC_2458',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x1)*complexconjugate(VV1x2)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU1x2)*complexconjugate(VV1x1)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2459 = Coupling(name = 'GC_2459',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x1)*complexconjugate(VV1x2)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU2x2)*complexconjugate(VV1x1)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2460 = Coupling(name = 'GC_2460',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x2)*complexconjugate(VV1x1)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU1x1)*complexconjugate(VV1x2)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2461 = Coupling(name = 'GC_2461',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x2)*complexconjugate(VV1x1)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU2x1)*complexconjugate(VV1x2)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2462 = Coupling(name = 'GC_2462',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x1)*complexconjugate(VV2x2)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU1x2)*complexconjugate(VV2x1)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2463 = Coupling(name = 'GC_2463',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x1)*complexconjugate(VV2x2)*cmath.cos(alp))/(sw*cmath.sqrt(2))) + (ee*complex(0,1)*complexconjugate(UU2x2)*complexconjugate(VV2x1)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2464 = Coupling(name = 'GC_2464',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x2)*complexconjugate(VV2x1)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU1x1)*complexconjugate(VV2x2)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2465 = Coupling(name = 'GC_2465',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x2)*complexconjugate(VV2x1)*cmath.cos(alp))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*complexconjugate(UU2x1)*complexconjugate(VV2x2)*cmath.sin(alp))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2466 = Coupling(name = 'GC_2466',
                   value = '-(cw*ee*complex(0,1)*NN1x1*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2467 = Coupling(name = 'GC_2467',
                   value = '-((cw*ee*NN1x1*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (ee*NN1x2*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2468 = Coupling(name = 'GC_2468',
                   value = '-(cw*ee*complex(0,1)*NN2x1*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2469 = Coupling(name = 'GC_2469',
                   value = '-((cw*ee*NN2x1*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (ee*NN2x2*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2470 = Coupling(name = 'GC_2470',
                   value = '-(cw*ee*complex(0,1)*NN3x1*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2471 = Coupling(name = 'GC_2471',
                   value = '-((cw*ee*NN3x1*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (ee*NN3x2*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2472 = Coupling(name = 'GC_2472',
                   value = '-(cw*ee*complex(0,1)*NN4x1*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2473 = Coupling(name = 'GC_2473',
                   value = '-((cw*ee*NN4x1*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))) + (ee*NN4x2*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2474 = Coupling(name = 'GC_2474',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2475 = Coupling(name = 'GC_2475',
                   value = '(cw*ee*complexconjugate(NN1x1)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN1x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN1x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2476 = Coupling(name = 'GC_2476',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2477 = Coupling(name = 'GC_2477',
                   value = '(cw*ee*complexconjugate(NN2x1)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN2x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN2x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2478 = Coupling(name = 'GC_2478',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2479 = Coupling(name = 'GC_2479',
                   value = '(cw*ee*complexconjugate(NN3x1)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN3x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN3x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2480 = Coupling(name = 'GC_2480',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.cos(alp)*cmath.sin(alp))/(2.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2481 = Coupling(name = 'GC_2481',
                   value = '(cw*ee*complexconjugate(NN4x1)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN4x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN4x2)*cmath.cos(alp)*cmath.sin(alp))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2482 = Coupling(name = 'GC_2482',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_2483 = Coupling(name = 'GC_2483',
                   value = '-(ee**2*complex(0,1)*cmath.cos(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(alp)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2484 = Coupling(name = 'GC_2484',
                   value = '(cw*ee*complex(0,1)*NN1x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2485 = Coupling(name = 'GC_2485',
                   value = '-(cw*ee*complex(0,1)*NN1x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2486 = Coupling(name = 'GC_2486',
                   value = '(cw*ee*NN1x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN1x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2487 = Coupling(name = 'GC_2487',
                   value = '-(cw*ee*NN1x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2488 = Coupling(name = 'GC_2488',
                   value = '(cw*ee*complex(0,1)*NN2x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2489 = Coupling(name = 'GC_2489',
                   value = '-(cw*ee*complex(0,1)*NN2x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2490 = Coupling(name = 'GC_2490',
                   value = '(cw*ee*NN2x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN2x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2491 = Coupling(name = 'GC_2491',
                   value = '-(cw*ee*NN2x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2492 = Coupling(name = 'GC_2492',
                   value = '(cw*ee*complex(0,1)*NN3x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2493 = Coupling(name = 'GC_2493',
                   value = '-(cw*ee*complex(0,1)*NN3x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2494 = Coupling(name = 'GC_2494',
                   value = '(cw*ee*NN3x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN3x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2495 = Coupling(name = 'GC_2495',
                   value = '-(cw*ee*NN3x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2496 = Coupling(name = 'GC_2496',
                   value = '(cw*ee*complex(0,1)*NN4x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2497 = Coupling(name = 'GC_2497',
                   value = '-(cw*ee*complex(0,1)*NN4x1*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2498 = Coupling(name = 'GC_2498',
                   value = '(cw*ee*NN4x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*NN4x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2499 = Coupling(name = 'GC_2499',
                   value = '-(cw*ee*NN4x1*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x1*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2500 = Coupling(name = 'GC_2500',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2501 = Coupling(name = 'GC_2501',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2502 = Coupling(name = 'GC_2502',
                   value = '(cw*ee*complexconjugate(NN1x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN1x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2503 = Coupling(name = 'GC_2503',
                   value = '-(cw*ee*complexconjugate(NN1x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN1x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN1x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN1x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2504 = Coupling(name = 'GC_2504',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2505 = Coupling(name = 'GC_2505',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2506 = Coupling(name = 'GC_2506',
                   value = '(cw*ee*complexconjugate(NN2x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN2x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2507 = Coupling(name = 'GC_2507',
                   value = '-(cw*ee*complexconjugate(NN2x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN2x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN2x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN2x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2508 = Coupling(name = 'GC_2508',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2509 = Coupling(name = 'GC_2509',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2510 = Coupling(name = 'GC_2510',
                   value = '(cw*ee*complexconjugate(NN3x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN3x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2511 = Coupling(name = 'GC_2511',
                   value = '-(cw*ee*complexconjugate(NN3x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN3x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN3x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN3x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2512 = Coupling(name = 'GC_2512',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2513 = Coupling(name = 'GC_2513',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2514 = Coupling(name = 'GC_2514',
                   value = '(cw*ee*complexconjugate(NN4x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN4x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2515 = Coupling(name = 'GC_2515',
                   value = '-(cw*ee*complexconjugate(NN4x1)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN4x2)*cmath.cos(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complexconjugate(NN4x1)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN4x2)*cmath.sin(alp)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2516 = Coupling(name = 'GC_2516',
                   value = '-(ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (5*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2517 = Coupling(name = 'GC_2517',
                   value = '(3*ee**2*complex(0,1)*vu*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vd*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2518 = Coupling(name = 'GC_2518',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (5*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2519 = Coupling(name = 'GC_2519',
                   value = '(3*ee**2*complex(0,1)*vd*cmath.cos(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vu*cmath.cos(alp)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(alp)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*ee**2*complex(0,1)*vu*cmath.sin(alp)**3)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2520 = Coupling(name = 'GC_2520',
                   value = 'complex(0,1)*I2x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_2521 = Coupling(name = 'GC_2521',
                   value = 'complex(0,1)*I30x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_2522 = Coupling(name = 'GC_2522',
                   value = 'complex(0,1)*I73x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_2523 = Coupling(name = 'GC_2523',
                   value = 'complex(0,1)*I75x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_2524 = Coupling(name = 'GC_2524',
                   value = '-((complex(0,1)*I10x33*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2525 = Coupling(name = 'GC_2525',
                   value = '(I12x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2526 = Coupling(name = 'GC_2526',
                   value = '(I12x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2527 = Coupling(name = 'GC_2527',
                   value = '(I14x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2528 = Coupling(name = 'GC_2528',
                   value = '(I14x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2529 = Coupling(name = 'GC_2529',
                   value = '(complex(0,1)*I15x33*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2530 = Coupling(name = 'GC_2530',
                   value = '(complex(0,1)*I15x36*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2531 = Coupling(name = 'GC_2531',
                   value = '(I17x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2532 = Coupling(name = 'GC_2532',
                   value = '(I17x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2533 = Coupling(name = 'GC_2533',
                   value = '(I18x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2534 = Coupling(name = 'GC_2534',
                   value = '(I18x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2535 = Coupling(name = 'GC_2535',
                   value = '-((complex(0,1)*I20x33*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2536 = Coupling(name = 'GC_2536',
                   value = '-((complex(0,1)*I20x36*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2537 = Coupling(name = 'GC_2537',
                   value = '-(I27x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2538 = Coupling(name = 'GC_2538',
                   value = '-(I27x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2539 = Coupling(name = 'GC_2539',
                   value = '-(I28x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2540 = Coupling(name = 'GC_2540',
                   value = '-(I28x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2541 = Coupling(name = 'GC_2541',
                   value = '(complex(0,1)*I33x33*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2542 = Coupling(name = 'GC_2542',
                   value = '(complex(0,1)*I33x36*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2543 = Coupling(name = 'GC_2543',
                   value = '-(I37x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2544 = Coupling(name = 'GC_2544',
                   value = '-(I37x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2545 = Coupling(name = 'GC_2545',
                   value = '-(I38x33*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2546 = Coupling(name = 'GC_2546',
                   value = '-(I38x36*cmath.sin(beta))/(2.*MP)',
                   order = {'QED':1,'QGR':1})

GC_2547 = Coupling(name = 'GC_2547',
                   value = '-((complex(0,1)*I42x33*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2548 = Coupling(name = 'GC_2548',
                   value = '-((complex(0,1)*I42x36*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2549 = Coupling(name = 'GC_2549',
                   value = '(complex(0,1)*I7x33*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2550 = Coupling(name = 'GC_2550',
                   value = '(complex(0,1)*I7x36*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2551 = Coupling(name = 'GC_2551',
                   value = '(complex(0,1)*I8x33*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2552 = Coupling(name = 'GC_2552',
                   value = '(complex(0,1)*I8x36*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2553 = Coupling(name = 'GC_2553',
                   value = '-((complex(0,1)*I9x33*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2554 = Coupling(name = 'GC_2554',
                   value = '-((I10x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2555 = Coupling(name = 'GC_2555',
                   value = '-((complex(0,1)*I12x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2556 = Coupling(name = 'GC_2556',
                   value = '-((complex(0,1)*I12x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2557 = Coupling(name = 'GC_2557',
                   value = '-((complex(0,1)*I14x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2558 = Coupling(name = 'GC_2558',
                   value = '-((complex(0,1)*I14x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2559 = Coupling(name = 'GC_2559',
                   value = '(I15x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2560 = Coupling(name = 'GC_2560',
                   value = '(I15x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2561 = Coupling(name = 'GC_2561',
                   value = '-((complex(0,1)*I17x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2562 = Coupling(name = 'GC_2562',
                   value = '-((complex(0,1)*I17x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2563 = Coupling(name = 'GC_2563',
                   value = '-((complex(0,1)*I18x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2564 = Coupling(name = 'GC_2564',
                   value = '-((complex(0,1)*I18x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6)))',
                   order = {'QED':1,'QGR':1})

GC_2565 = Coupling(name = 'GC_2565',
                   value = '-((I20x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2566 = Coupling(name = 'GC_2566',
                   value = '-((I20x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2567 = Coupling(name = 'GC_2567',
                   value = '(complex(0,1)*I27x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2568 = Coupling(name = 'GC_2568',
                   value = '(complex(0,1)*I27x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2569 = Coupling(name = 'GC_2569',
                   value = '(complex(0,1)*I28x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2570 = Coupling(name = 'GC_2570',
                   value = '(complex(0,1)*I28x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2571 = Coupling(name = 'GC_2571',
                   value = '(I33x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2572 = Coupling(name = 'GC_2572',
                   value = '(I33x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2573 = Coupling(name = 'GC_2573',
                   value = '(complex(0,1)*I37x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2574 = Coupling(name = 'GC_2574',
                   value = '(complex(0,1)*I37x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2575 = Coupling(name = 'GC_2575',
                   value = '(complex(0,1)*I38x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2576 = Coupling(name = 'GC_2576',
                   value = '(complex(0,1)*I38x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2577 = Coupling(name = 'GC_2577',
                   value = '-((I42x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2578 = Coupling(name = 'GC_2578',
                   value = '-((I42x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2579 = Coupling(name = 'GC_2579',
                   value = '(I7x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2580 = Coupling(name = 'GC_2580',
                   value = '(I7x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2581 = Coupling(name = 'GC_2581',
                   value = '(I8x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2582 = Coupling(name = 'GC_2582',
                   value = '(I8x36*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2583 = Coupling(name = 'GC_2583',
                   value = '-((I9x33*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2584 = Coupling(name = 'GC_2584',
                   value = '-(ee*complex(0,1)*NN1x3*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2585 = Coupling(name = 'GC_2585',
                   value = '(ee*NN1x3*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2586 = Coupling(name = 'GC_2586',
                   value = '-(ee*complex(0,1)*NN2x3*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2587 = Coupling(name = 'GC_2587',
                   value = '(ee*NN2x3*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2588 = Coupling(name = 'GC_2588',
                   value = '-(ee*complex(0,1)*NN3x3*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2589 = Coupling(name = 'GC_2589',
                   value = '(ee*NN3x3*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2590 = Coupling(name = 'GC_2590',
                   value = '-(ee*complex(0,1)*NN4x3*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2591 = Coupling(name = 'GC_2591',
                   value = '(ee*NN4x3*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2592 = Coupling(name = 'GC_2592',
                   value = '(complex(0,1)*UU1x2*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2593 = Coupling(name = 'GC_2593',
                   value = '-((complex(0,1)*UU1x2*cmath.sqrt(2)*cmath.sin(beta))/MP)',
                   order = {'QGR':1})

GC_2594 = Coupling(name = 'GC_2594',
                   value = '(ee*complex(0,1)*UU1x2*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2595 = Coupling(name = 'GC_2595',
                   value = '-((ee*complex(0,1)*UU1x2*cmath.sqrt(2)*cmath.sin(beta))/MP)',
                   order = {'QED':1,'QGR':1})

GC_2596 = Coupling(name = 'GC_2596',
                   value = '-((UU1x2*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_2597 = Coupling(name = 'GC_2597',
                   value = '-((ee*UU1x2*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2598 = Coupling(name = 'GC_2598',
                   value = '(ee*UU1x2*cmath.sin(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2599 = Coupling(name = 'GC_2599',
                   value = '(ee*complex(0,1)*UU1x2*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2600 = Coupling(name = 'GC_2600',
                   value = '-(cw*ee*complex(0,1)*UU1x2*cmath.sin(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2601 = Coupling(name = 'GC_2601',
                   value = '(cw*ee*complex(0,1)*sw*UU1x2*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2602 = Coupling(name = 'GC_2602',
                   value = '-((cw*ee*complex(0,1)*sw*UU1x2*cmath.sqrt(2)*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)))',
                   order = {'QED':1,'QGR':1})

GC_2603 = Coupling(name = 'GC_2603',
                   value = '(complex(0,1)*UU2x2*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2604 = Coupling(name = 'GC_2604',
                   value = '-((complex(0,1)*UU2x2*cmath.sqrt(2)*cmath.sin(beta))/MP)',
                   order = {'QGR':1})

GC_2605 = Coupling(name = 'GC_2605',
                   value = '(ee*complex(0,1)*UU2x2*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2606 = Coupling(name = 'GC_2606',
                   value = '-((ee*complex(0,1)*UU2x2*cmath.sqrt(2)*cmath.sin(beta))/MP)',
                   order = {'QED':1,'QGR':1})

GC_2607 = Coupling(name = 'GC_2607',
                   value = '-((UU2x2*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_2608 = Coupling(name = 'GC_2608',
                   value = '-((ee*UU2x2*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2609 = Coupling(name = 'GC_2609',
                   value = '(ee*UU2x2*cmath.sin(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2610 = Coupling(name = 'GC_2610',
                   value = '(ee*complex(0,1)*UU2x2*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2611 = Coupling(name = 'GC_2611',
                   value = '-(cw*ee*complex(0,1)*UU2x2*cmath.sin(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2612 = Coupling(name = 'GC_2612',
                   value = '(cw*ee*complex(0,1)*sw*UU2x2*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2613 = Coupling(name = 'GC_2613',
                   value = '-((cw*ee*complex(0,1)*sw*UU2x2*cmath.sqrt(2)*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)))',
                   order = {'QED':1,'QGR':1})

GC_2614 = Coupling(name = 'GC_2614',
                   value = '(yd3x3*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2615 = Coupling(name = 'GC_2615',
                   value = '(ye3x3*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2616 = Coupling(name = 'GC_2616',
                   value = '-(ee*complex(0,1)*complexconjugate(NN1x3)*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2617 = Coupling(name = 'GC_2617',
                   value = '(ee*complexconjugate(NN1x3)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2618 = Coupling(name = 'GC_2618',
                   value = '-(ee*complex(0,1)*complexconjugate(NN2x3)*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2619 = Coupling(name = 'GC_2619',
                   value = '(ee*complexconjugate(NN2x3)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2620 = Coupling(name = 'GC_2620',
                   value = '-(ee*complex(0,1)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2621 = Coupling(name = 'GC_2621',
                   value = '(ee*complexconjugate(NN3x3)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2622 = Coupling(name = 'GC_2622',
                   value = '-(ee*complex(0,1)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2623 = Coupling(name = 'GC_2623',
                   value = '(ee*complexconjugate(NN4x3)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2624 = Coupling(name = 'GC_2624',
                   value = '(complex(0,1)*complexconjugate(UU1x2)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2625 = Coupling(name = 'GC_2625',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x2)*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2626 = Coupling(name = 'GC_2626',
                   value = '-((complexconjugate(UU1x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_2627 = Coupling(name = 'GC_2627',
                   value = '(-2*ee*complexconjugate(UU1x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2628 = Coupling(name = 'GC_2628',
                   value = '(ee*complexconjugate(UU1x2)*cmath.sin(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2629 = Coupling(name = 'GC_2629',
                   value = '-((ee*complex(0,1)*complexconjugate(UU1x2)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2630 = Coupling(name = 'GC_2630',
                   value = '(complex(0,1)*complexconjugate(UU2x2)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2631 = Coupling(name = 'GC_2631',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x2)*cmath.sin(beta))/(MP*cmath.sqrt(2)))',
                   order = {'QED':1,'QGR':1})

GC_2632 = Coupling(name = 'GC_2632',
                   value = '-((complexconjugate(UU2x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)))',
                   order = {'QGR':1})

GC_2633 = Coupling(name = 'GC_2633',
                   value = '(-2*ee*complexconjugate(UU2x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2634 = Coupling(name = 'GC_2634',
                   value = '(ee*complexconjugate(UU2x2)*cmath.sin(beta))/(2.*MP*sw*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2635 = Coupling(name = 'GC_2635',
                   value = '-((ee*complex(0,1)*complexconjugate(UU2x2)*cmath.sin(beta))/(M32*MP*sw*cmath.sqrt(3)))',
                   order = {'QED':1,'QGR':1})

GC_2636 = Coupling(name = 'GC_2636',
                   value = '-((complexconjugate(yd3x3)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2637 = Coupling(name = 'GC_2637',
                   value = '-((complexconjugate(ye3x3)*cmath.sin(beta))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2638 = Coupling(name = 'GC_2638',
                   value = '-((I59x33*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I62x33*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I56x33*cmath.sin(beta))/cmath.sqrt(2) + (I60x33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2639 = Coupling(name = 'GC_2639',
                   value = '-((I59x36*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I62x36*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I56x36*cmath.sin(beta))/cmath.sqrt(2) + (I60x36*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2640 = Coupling(name = 'GC_2640',
                   value = '-((I59x63*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I62x63*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I56x63*cmath.sin(beta))/cmath.sqrt(2) + (I60x63*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2641 = Coupling(name = 'GC_2641',
                   value = '-((I59x66*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I62x66*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I56x66*cmath.sin(beta))/cmath.sqrt(2) + (I60x66*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2642 = Coupling(name = 'GC_2642',
                   value = '-((I86x33*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I90x33*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I85x33*cmath.sin(beta))/cmath.sqrt(2) + (I87x33*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2643 = Coupling(name = 'GC_2643',
                   value = '-((I86x36*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I90x36*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I85x36*cmath.sin(beta))/cmath.sqrt(2) + (I87x36*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2644 = Coupling(name = 'GC_2644',
                   value = '-((I86x63*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I90x63*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I85x63*cmath.sin(beta))/cmath.sqrt(2) + (I87x63*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2645 = Coupling(name = 'GC_2645',
                   value = '-((I86x66*MUH*cmath.cos(beta))/cmath.sqrt(2)) + (I90x66*complexconjugate(MUH)*cmath.cos(beta))/cmath.sqrt(2) - (I85x66*cmath.sin(beta))/cmath.sqrt(2) + (I87x66*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2646 = Coupling(name = 'GC_2646',
                   value = '(NN1x4*cmath.cos(beta))/MP + (NN1x3*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2647 = Coupling(name = 'GC_2647',
                   value = '-((complex(0,1)*NN1x4*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*NN1x3*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2648 = Coupling(name = 'GC_2648',
                   value = '(complex(0,1)*NN1x4*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN1x3*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2649 = Coupling(name = 'GC_2649',
                   value = '(NN2x4*cmath.cos(beta))/MP + (NN2x3*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2650 = Coupling(name = 'GC_2650',
                   value = '-((complex(0,1)*NN2x4*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*NN2x3*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2651 = Coupling(name = 'GC_2651',
                   value = '(complex(0,1)*NN2x4*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN2x3*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2652 = Coupling(name = 'GC_2652',
                   value = '(NN3x4*cmath.cos(beta))/MP + (NN3x3*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2653 = Coupling(name = 'GC_2653',
                   value = '-((complex(0,1)*NN3x4*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*NN3x3*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2654 = Coupling(name = 'GC_2654',
                   value = '(complex(0,1)*NN3x4*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN3x3*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2655 = Coupling(name = 'GC_2655',
                   value = '(NN4x4*cmath.cos(beta))/MP + (NN4x3*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2656 = Coupling(name = 'GC_2656',
                   value = '-((complex(0,1)*NN4x4*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*NN4x3*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2657 = Coupling(name = 'GC_2657',
                   value = '(complex(0,1)*NN4x4*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN4x3*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2658 = Coupling(name = 'GC_2658',
                   value = '(cw*ee*NN1x4*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*NN1x3*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2659 = Coupling(name = 'GC_2659',
                   value = '(cw*ee*complex(0,1)*NN1x4*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complex(0,1)*NN1x3*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2660 = Coupling(name = 'GC_2660',
                   value = '(cw*ee*NN2x4*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*NN2x3*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2661 = Coupling(name = 'GC_2661',
                   value = '(cw*ee*complex(0,1)*NN2x4*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complex(0,1)*NN2x3*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2662 = Coupling(name = 'GC_2662',
                   value = '(cw*ee*NN3x4*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*NN3x3*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2663 = Coupling(name = 'GC_2663',
                   value = '(cw*ee*complex(0,1)*NN3x4*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complex(0,1)*NN3x3*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2664 = Coupling(name = 'GC_2664',
                   value = '(cw*ee*NN4x4*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (cw*ee*NN4x3*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2665 = Coupling(name = 'GC_2665',
                   value = '(cw*ee*complex(0,1)*NN4x4*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complex(0,1)*NN4x3*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2666 = Coupling(name = 'GC_2666',
                   value = '-((cw*ee*NN1x1*NN1x4*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN1x2*NN1x4*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN1x2*NN1x4*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN1x1*NN1x3*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN1x2*NN1x3*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN1x2*NN1x3*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2667 = Coupling(name = 'GC_2667',
                   value = '-(cw*ee*NN1x4*NN2x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN1x1*NN2x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x4*NN2x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x2*NN2x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x4*NN2x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x2*NN2x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x3*NN2x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x1*NN2x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x3*NN2x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x2*NN2x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x3*NN2x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x2*NN2x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2668 = Coupling(name = 'GC_2668',
                   value = '-((cw*ee*NN2x1*NN2x4*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN2x2*NN2x4*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN2x2*NN2x4*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN2x1*NN2x3*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN2x2*NN2x3*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN2x2*NN2x3*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2669 = Coupling(name = 'GC_2669',
                   value = '-(cw*ee*NN1x4*NN3x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN1x1*NN3x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x4*NN3x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x2*NN3x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x4*NN3x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x2*NN3x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x3*NN3x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x1*NN3x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x3*NN3x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x2*NN3x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x3*NN3x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x2*NN3x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2670 = Coupling(name = 'GC_2670',
                   value = '-(cw*ee*NN2x4*NN3x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN2x1*NN3x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN2x4*NN3x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN2x2*NN3x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN2x4*NN3x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN2x2*NN3x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN2x3*NN3x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN2x1*NN3x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN2x3*NN3x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN2x2*NN3x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN2x3*NN3x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN2x2*NN3x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2671 = Coupling(name = 'GC_2671',
                   value = '-((cw*ee*NN3x1*NN3x4*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN3x2*NN3x4*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN3x2*NN3x4*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN3x1*NN3x3*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN3x2*NN3x3*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN3x2*NN3x3*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2672 = Coupling(name = 'GC_2672',
                   value = '-(cw*ee*NN1x4*NN4x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN1x1*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x4*NN4x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x2*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x4*NN4x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x2*NN4x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x3*NN4x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN1x1*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN1x3*NN4x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN1x2*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN1x3*NN4x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN1x2*NN4x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2673 = Coupling(name = 'GC_2673',
                   value = '-(cw*ee*NN2x4*NN4x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN2x1*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN2x4*NN4x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN2x2*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN2x4*NN4x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN2x2*NN4x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN2x3*NN4x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN2x1*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN2x3*NN4x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN2x2*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN2x3*NN4x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN2x2*NN4x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2674 = Coupling(name = 'GC_2674',
                   value = '-(cw*ee*NN3x4*NN4x1*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN3x1*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN3x4*NN4x2*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN3x2*NN4x4*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN3x4*NN4x2*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN3x2*NN4x4*sw*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN3x3*NN4x1*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN3x1*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*NN3x3*NN4x2*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN3x2*NN4x3*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN3x3*NN4x2*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*NN3x2*NN4x3*sw*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2675 = Coupling(name = 'GC_2675',
                   value = '-((cw*ee*NN4x1*NN4x4*cmath.cos(beta))/((-1 + sw)*(1 + sw))) + (ee*NN4x2*NN4x4*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*NN4x2*NN4x4*sw*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*NN4x1*NN4x3*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee*NN4x2*NN4x3*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*NN4x2*NN4x3*sw*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2676 = Coupling(name = 'GC_2676',
                   value = '(cw*ee*UU1x2*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*sw*UU1x2*cmath.sin(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2677 = Coupling(name = 'GC_2677',
                   value = '(ee*complex(0,1)*NN1x3*UU1x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x3*sw*UU1x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*UU1x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2678 = Coupling(name = 'GC_2678',
                   value = '(ee*complex(0,1)*NN2x3*UU1x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x3*sw*UU1x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*UU1x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2679 = Coupling(name = 'GC_2679',
                   value = '(ee*complex(0,1)*NN3x3*UU1x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x3*sw*UU1x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*UU1x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2680 = Coupling(name = 'GC_2680',
                   value = '(ee*complex(0,1)*NN4x3*UU1x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x3*sw*UU1x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*UU1x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*UU1x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2681 = Coupling(name = 'GC_2681',
                   value = '(cw*ee*UU2x2*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (cw*ee*sw*UU2x2*cmath.sin(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2682 = Coupling(name = 'GC_2682',
                   value = '(ee*complex(0,1)*NN1x3*UU2x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x3*sw*UU2x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN1x1*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN1x2*UU2x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN1x2*sw*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2683 = Coupling(name = 'GC_2683',
                   value = '(ee*complex(0,1)*NN2x3*UU2x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x3*sw*UU2x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN2x1*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN2x2*UU2x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN2x2*sw*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2684 = Coupling(name = 'GC_2684',
                   value = '(ee*complex(0,1)*NN3x3*UU2x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x3*sw*UU2x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN3x1*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN3x2*UU2x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN3x2*sw*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2685 = Coupling(name = 'GC_2685',
                   value = '(ee*complex(0,1)*NN4x3*UU2x1*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x3*sw*UU2x1*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN4x1*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN4x2*UU2x2*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN4x2*sw*UU2x2*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2686 = Coupling(name = 'GC_2686',
                   value = '-(ee**2*complex(0,1)*I101x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I101x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2687 = Coupling(name = 'GC_2687',
                   value = '-(ee**2*complex(0,1)*I101x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I101x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2688 = Coupling(name = 'GC_2688',
                   value = 'complex(0,1)*I102x33*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I101x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I103x33*cmath.sin(beta) + (complex(0,1)*I104x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I101x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2689 = Coupling(name = 'GC_2689',
                   value = 'complex(0,1)*I102x36*MUH*cmath.cos(beta) - (ee**2*complex(0,1)*I101x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I103x36*cmath.sin(beta) + (complex(0,1)*I104x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I101x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2690 = Coupling(name = 'GC_2690',
                   value = '-(ee**2*complex(0,1)*I110x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I110x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2691 = Coupling(name = 'GC_2691',
                   value = '-(ee**2*complex(0,1)*I110x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I110x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2692 = Coupling(name = 'GC_2692',
                   value = '-(ee**2*complex(0,1)*I121x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I121x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2693 = Coupling(name = 'GC_2693',
                   value = '-(ee**2*complex(0,1)*I121x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I121x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2694 = Coupling(name = 'GC_2694',
                   value = '-(ee**2*complex(0,1)*I95x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I95x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2695 = Coupling(name = 'GC_2695',
                   value = '-(ee**2*complex(0,1)*I95x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I95x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2696 = Coupling(name = 'GC_2696',
                   value = 'complex(0,1)*I98x33*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I95x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I96x33*cmath.sin(beta) + (complex(0,1)*I97x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I95x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2697 = Coupling(name = 'GC_2697',
                   value = 'complex(0,1)*I98x36*complexconjugate(MUH)*cmath.cos(beta) - (ee**2*complex(0,1)*I95x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I96x36*cmath.sin(beta) + (complex(0,1)*I97x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I95x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2698 = Coupling(name = 'GC_2698',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_2699 = Coupling(name = 'GC_2699',
                   value = '(cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2700 = Coupling(name = 'GC_2700',
                   value = '(ee*complex(0,1)*UU1x1*vu*cmath.cos(beta))/(4.*MP*sw) + (complex(0,1)*UU1x2*complexconjugate(MUH)*cmath.cos(beta))/(MP*cmath.sqrt(2)) + (ee*complex(0,1)*UU1x1*vd*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QGR':1})

GC_2701 = Coupling(name = 'GC_2701',
                   value = '(UU1x2*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)) + (ee*UU1x1*vu*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*UU1x1*vd*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2702 = Coupling(name = 'GC_2702',
                   value = '(ee*complex(0,1)*UU2x1*vu*cmath.cos(beta))/(4.*MP*sw) + (complex(0,1)*UU2x2*complexconjugate(MUH)*cmath.cos(beta))/(MP*cmath.sqrt(2)) + (ee*complex(0,1)*UU2x1*vd*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QGR':1})

GC_2703 = Coupling(name = 'GC_2703',
                   value = '(UU2x2*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)) + (ee*UU2x1*vu*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*UU2x1*vd*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2704 = Coupling(name = 'GC_2704',
                   value = 'complex(0,1)*I111x33*cmath.cos(beta) + complex(0,1)*I114x33*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I116x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I117x33*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I113x33*cmath.sin(beta) + complex(0,1)*I112x33*MUH*cmath.sin(beta) + (complex(0,1)*I115x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I116x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2705 = Coupling(name = 'GC_2705',
                   value = 'complex(0,1)*I111x36*cmath.cos(beta) + complex(0,1)*I114x36*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I116x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I117x36*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I113x36*cmath.sin(beta) + complex(0,1)*I112x36*MUH*cmath.sin(beta) + (complex(0,1)*I115x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I116x36*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2706 = Coupling(name = 'GC_2706',
                   value = 'complex(0,1)*I111x63*cmath.cos(beta) + complex(0,1)*I114x63*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I116x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I117x63*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x63*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I113x63*cmath.sin(beta) + complex(0,1)*I112x63*MUH*cmath.sin(beta) + (complex(0,1)*I115x63*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x63*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I116x63*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2707 = Coupling(name = 'GC_2707',
                   value = 'complex(0,1)*I111x66*cmath.cos(beta) + complex(0,1)*I114x66*complexconjugate(MUH)*cmath.cos(beta) + (complex(0,1)*I116x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I117x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I113x66*cmath.sin(beta) + complex(0,1)*I112x66*MUH*cmath.sin(beta) + (complex(0,1)*I115x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I110x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I116x66*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2708 = Coupling(name = 'GC_2708',
                   value = '(ee*UU1x1*VV1x2*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU1x2*VV1x1*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2709 = Coupling(name = 'GC_2709',
                   value = '(ee*UU2x1*VV1x2*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU2x2*VV1x1*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2710 = Coupling(name = 'GC_2710',
                   value = '(ee*UU1x1*VV2x2*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU1x2*VV2x1*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2711 = Coupling(name = 'GC_2711',
                   value = '(ee*UU2x1*VV2x2*cmath.cos(beta))/(sw*cmath.sqrt(2)) + (ee*UU2x2*VV2x1*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2712 = Coupling(name = 'GC_2712',
                   value = 'complex(0,1)*I124x33*cmath.cos(beta) + complex(0,1)*I122x33*MUH*cmath.cos(beta) + (complex(0,1)*I128x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x33*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x33*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I123x33*cmath.sin(beta) + complex(0,1)*I127x33*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I125x33*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x33*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I128x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2713 = Coupling(name = 'GC_2713',
                   value = 'complex(0,1)*I124x36*cmath.cos(beta) + complex(0,1)*I122x36*MUH*cmath.cos(beta) + (complex(0,1)*I128x36*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x36*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x36*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I123x36*cmath.sin(beta) + complex(0,1)*I127x36*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I125x36*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x36*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I128x36*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2714 = Coupling(name = 'GC_2714',
                   value = 'complex(0,1)*I124x63*cmath.cos(beta) + complex(0,1)*I122x63*MUH*cmath.cos(beta) + (complex(0,1)*I128x63*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x63*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x63*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I123x63*cmath.sin(beta) + complex(0,1)*I127x63*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I125x63*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x63*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I128x63*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2715 = Coupling(name = 'GC_2715',
                   value = 'complex(0,1)*I124x66*cmath.cos(beta) + complex(0,1)*I122x66*MUH*cmath.cos(beta) + (complex(0,1)*I128x66*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I126x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I123x66*cmath.sin(beta) + complex(0,1)*I127x66*complexconjugate(MUH)*cmath.sin(beta) + (complex(0,1)*I125x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I121x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I128x66*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2716 = Coupling(name = 'GC_2716',
                   value = '-((I132x33*cmath.cos(beta))/cmath.sqrt(2)) + (I133x33*cmath.cos(beta))/cmath.sqrt(2) - (I131x33*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I134x33*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2717 = Coupling(name = 'GC_2717',
                   value = '-((I132x36*cmath.cos(beta))/cmath.sqrt(2)) + (I133x36*cmath.cos(beta))/cmath.sqrt(2) - (I131x36*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I134x36*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2718 = Coupling(name = 'GC_2718',
                   value = '-((I132x63*cmath.cos(beta))/cmath.sqrt(2)) + (I133x63*cmath.cos(beta))/cmath.sqrt(2) - (I131x63*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I134x63*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2719 = Coupling(name = 'GC_2719',
                   value = '-((I132x66*cmath.cos(beta))/cmath.sqrt(2)) + (I133x66*cmath.cos(beta))/cmath.sqrt(2) - (I131x66*MUH*cmath.sin(beta))/cmath.sqrt(2) + (I134x66*complexconjugate(MUH)*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_2720 = Coupling(name = 'GC_2720',
                   value = '-(NN1x3*complexconjugate(MUH)*cmath.cos(beta))/(2.*MP) - (NN1x4*complexconjugate(MUH)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2721 = Coupling(name = 'GC_2721',
                   value = '(complex(0,1)*NN1x3*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN1x4*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2722 = Coupling(name = 'GC_2722',
                   value = '-(NN2x3*complexconjugate(MUH)*cmath.cos(beta))/(2.*MP) - (NN2x4*complexconjugate(MUH)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2723 = Coupling(name = 'GC_2723',
                   value = '(complex(0,1)*NN2x3*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN2x4*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2724 = Coupling(name = 'GC_2724',
                   value = '-(NN3x3*complexconjugate(MUH)*cmath.cos(beta))/(2.*MP) - (NN3x4*complexconjugate(MUH)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2725 = Coupling(name = 'GC_2725',
                   value = '(complex(0,1)*NN3x3*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN3x4*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2726 = Coupling(name = 'GC_2726',
                   value = '-(NN4x3*complexconjugate(MUH)*cmath.cos(beta))/(2.*MP) - (NN4x4*complexconjugate(MUH)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2727 = Coupling(name = 'GC_2727',
                   value = '(complex(0,1)*NN4x3*complexconjugate(MUH)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*NN4x4*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2728 = Coupling(name = 'GC_2728',
                   value = '-(ee*complex(0,1)*vu*VV1x1*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*vd*VV1x1*cmath.sin(beta))/(4.*MP*sw) - (complex(0,1)*VV1x2*complexconjugate(MUH)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2729 = Coupling(name = 'GC_2729',
                   value = '-(ee*vu*VV1x1*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (VV1x2*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)) - (ee*vd*VV1x1*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2730 = Coupling(name = 'GC_2730',
                   value = '-(ee*complex(0,1)*vu*VV2x1*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*vd*VV2x1*cmath.sin(beta))/(4.*MP*sw) - (complex(0,1)*VV2x2*complexconjugate(MUH)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2731 = Coupling(name = 'GC_2731',
                   value = '-(ee*vu*VV2x1*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (VV2x2*complexconjugate(MUH)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)) - (ee*vd*VV2x1*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2732 = Coupling(name = 'GC_2732',
                   value = '(complexconjugate(NN1x4)*cmath.cos(beta))/MP + (complexconjugate(NN1x3)*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2733 = Coupling(name = 'GC_2733',
                   value = '-((complex(0,1)*complexconjugate(NN1x4)*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*complexconjugate(NN1x3)*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2734 = Coupling(name = 'GC_2734',
                   value = '(complex(0,1)*complexconjugate(NN1x4)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*complexconjugate(NN1x3)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2735 = Coupling(name = 'GC_2735',
                   value = '-(cw*ee*complexconjugate(NN1x4)*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complexconjugate(NN1x3)*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2736 = Coupling(name = 'GC_2736',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN1x4)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complex(0,1)*complexconjugate(NN1x3)*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2737 = Coupling(name = 'GC_2737',
                   value = '(cw*ee*complexconjugate(NN1x1)*complexconjugate(NN1x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN1x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN1x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN1x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2738 = Coupling(name = 'GC_2738',
                   value = '-(MUH*complexconjugate(NN1x3)*cmath.cos(beta))/(2.*MP) - (MUH*complexconjugate(NN1x4)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2739 = Coupling(name = 'GC_2739',
                   value = '(complex(0,1)*MUH*complexconjugate(NN1x3)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*MUH*complexconjugate(NN1x4)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2740 = Coupling(name = 'GC_2740',
                   value = '(complexconjugate(NN2x4)*cmath.cos(beta))/MP + (complexconjugate(NN2x3)*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2741 = Coupling(name = 'GC_2741',
                   value = '-((complex(0,1)*complexconjugate(NN2x4)*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*complexconjugate(NN2x3)*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2742 = Coupling(name = 'GC_2742',
                   value = '(complex(0,1)*complexconjugate(NN2x4)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*complexconjugate(NN2x3)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2743 = Coupling(name = 'GC_2743',
                   value = '-(cw*ee*complexconjugate(NN2x4)*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complexconjugate(NN2x3)*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2744 = Coupling(name = 'GC_2744',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN2x4)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complex(0,1)*complexconjugate(NN2x3)*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2745 = Coupling(name = 'GC_2745',
                   value = '(cw*ee*complexconjugate(NN1x4)*complexconjugate(NN2x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x4)*complexconjugate(NN2x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN2x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN2x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x3)*complexconjugate(NN2x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x3)*complexconjugate(NN2x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN2x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN2x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2746 = Coupling(name = 'GC_2746',
                   value = '(cw*ee*complexconjugate(NN2x1)*complexconjugate(NN2x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN2x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN2x1)*complexconjugate(NN2x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN2x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2747 = Coupling(name = 'GC_2747',
                   value = '-(MUH*complexconjugate(NN2x3)*cmath.cos(beta))/(2.*MP) - (MUH*complexconjugate(NN2x4)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2748 = Coupling(name = 'GC_2748',
                   value = '(complex(0,1)*MUH*complexconjugate(NN2x3)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*MUH*complexconjugate(NN2x4)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2749 = Coupling(name = 'GC_2749',
                   value = '(complexconjugate(NN3x4)*cmath.cos(beta))/MP + (complexconjugate(NN3x3)*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2750 = Coupling(name = 'GC_2750',
                   value = '-((complex(0,1)*complexconjugate(NN3x4)*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*complexconjugate(NN3x3)*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2751 = Coupling(name = 'GC_2751',
                   value = '(complex(0,1)*complexconjugate(NN3x4)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*complexconjugate(NN3x3)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2752 = Coupling(name = 'GC_2752',
                   value = '-(cw*ee*complexconjugate(NN3x4)*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complexconjugate(NN3x3)*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2753 = Coupling(name = 'GC_2753',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complex(0,1)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2754 = Coupling(name = 'GC_2754',
                   value = '(cw*ee*complexconjugate(NN1x4)*complexconjugate(NN3x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x4)*complexconjugate(NN3x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x3)*complexconjugate(NN3x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x3)*complexconjugate(NN3x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2755 = Coupling(name = 'GC_2755',
                   value = '(cw*ee*complexconjugate(NN2x4)*complexconjugate(NN3x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN2x4)*complexconjugate(NN3x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN2x1)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN3x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN2x3)*complexconjugate(NN3x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN2x3)*complexconjugate(NN3x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN2x1)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN3x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2756 = Coupling(name = 'GC_2756',
                   value = '(cw*ee*complexconjugate(NN3x1)*complexconjugate(NN3x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN3x2)*complexconjugate(NN3x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN3x1)*complexconjugate(NN3x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN3x2)*complexconjugate(NN3x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2757 = Coupling(name = 'GC_2757',
                   value = '-(MUH*complexconjugate(NN3x3)*cmath.cos(beta))/(2.*MP) - (MUH*complexconjugate(NN3x4)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2758 = Coupling(name = 'GC_2758',
                   value = '(complex(0,1)*MUH*complexconjugate(NN3x3)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*MUH*complexconjugate(NN3x4)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2759 = Coupling(name = 'GC_2759',
                   value = '(complexconjugate(NN4x4)*cmath.cos(beta))/MP + (complexconjugate(NN4x3)*cmath.sin(beta))/MP',
                   order = {'QGR':1})

GC_2760 = Coupling(name = 'GC_2760',
                   value = '-((complex(0,1)*complexconjugate(NN4x4)*cmath.cos(beta)*cmath.sqrt(0.6666666666666666))/(M32*MP)) - (complex(0,1)*complexconjugate(NN4x3)*cmath.sqrt(0.6666666666666666)*cmath.sin(beta))/(M32*MP)',
                   order = {'QGR':1})

GC_2761 = Coupling(name = 'GC_2761',
                   value = '(complex(0,1)*complexconjugate(NN4x4)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*complexconjugate(NN4x3)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2762 = Coupling(name = 'GC_2762',
                   value = '-(cw*ee*complexconjugate(NN4x4)*cmath.cos(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complexconjugate(NN4x3)*cmath.sin(beta))/(4.*MP*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2763 = Coupling(name = 'GC_2763',
                   value = '-(cw*ee*complex(0,1)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (cw*ee*complex(0,1)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2764 = Coupling(name = 'GC_2764',
                   value = '(cw*ee*complexconjugate(NN1x4)*complexconjugate(NN4x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x3)*complexconjugate(NN4x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN1x1)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN1x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2765 = Coupling(name = 'GC_2765',
                   value = '(cw*ee*complexconjugate(NN2x4)*complexconjugate(NN4x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN2x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN2x1)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN2x3)*complexconjugate(NN4x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN2x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN2x1)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN2x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2766 = Coupling(name = 'GC_2766',
                   value = '(cw*ee*complexconjugate(NN3x4)*complexconjugate(NN4x1)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN3x4)*complexconjugate(NN4x2)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complexconjugate(NN3x1)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN3x2)*complexconjugate(NN4x4)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN3x3)*complexconjugate(NN4x1)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN3x3)*complexconjugate(NN4x2)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN3x1)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN3x2)*complexconjugate(NN4x3)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2767 = Coupling(name = 'GC_2767',
                   value = '(cw*ee*complexconjugate(NN4x1)*complexconjugate(NN4x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (ee*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*complexconjugate(NN4x2)*complexconjugate(NN4x4)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complexconjugate(NN4x1)*complexconjugate(NN4x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*complexconjugate(NN4x2)*complexconjugate(NN4x3)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2768 = Coupling(name = 'GC_2768',
                   value = '-(MUH*complexconjugate(NN4x3)*cmath.cos(beta))/(2.*MP) - (MUH*complexconjugate(NN4x4)*cmath.sin(beta))/(2.*MP)',
                   order = {'QGR':1})

GC_2769 = Coupling(name = 'GC_2769',
                   value = '(complex(0,1)*MUH*complexconjugate(NN4x3)*cmath.cos(beta))/(M32*MP*cmath.sqrt(6)) + (complex(0,1)*MUH*complexconjugate(NN4x4)*cmath.sin(beta))/(M32*MP*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2770 = Coupling(name = 'GC_2770',
                   value = '(ee*complex(0,1)*vu*complexconjugate(UU1x1)*cmath.cos(beta))/(4.*MP*sw) + (complex(0,1)*MUH*complexconjugate(UU1x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)) + (ee*complex(0,1)*vd*complexconjugate(UU1x1)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QGR':1})

GC_2771 = Coupling(name = 'GC_2771',
                   value = '(MUH*complexconjugate(UU1x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)) + (ee*vu*complexconjugate(UU1x1)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*vd*complexconjugate(UU1x1)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2772 = Coupling(name = 'GC_2772',
                   value = '(cw*ee*complex(0,1)*complexconjugate(UU1x2)*cmath.sin(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(UU1x2)*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2773 = Coupling(name = 'GC_2773',
                   value = '(cw*ee*complexconjugate(UU1x2)*cmath.sin(beta))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(UU1x2)*cmath.sin(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2774 = Coupling(name = 'GC_2774',
                   value = '(ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2775 = Coupling(name = 'GC_2775',
                   value = '(ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2776 = Coupling(name = 'GC_2776',
                   value = '(ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2777 = Coupling(name = 'GC_2777',
                   value = '(ee*complex(0,1)*complexconjugate(NN4x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x3)*complexconjugate(UU1x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(UU1x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2778 = Coupling(name = 'GC_2778',
                   value = '(ee*complex(0,1)*vu*complexconjugate(UU2x1)*cmath.cos(beta))/(4.*MP*sw) + (complex(0,1)*MUH*complexconjugate(UU2x2)*cmath.cos(beta))/(MP*cmath.sqrt(2)) + (ee*complex(0,1)*vd*complexconjugate(UU2x1)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QGR':1})

GC_2779 = Coupling(name = 'GC_2779',
                   value = '(MUH*complexconjugate(UU2x2)*cmath.cos(beta))/(M32*MP*cmath.sqrt(3)) + (ee*vu*complexconjugate(UU2x1)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*vd*complexconjugate(UU2x1)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2780 = Coupling(name = 'GC_2780',
                   value = '(cw*ee*complex(0,1)*complexconjugate(UU2x2)*cmath.sin(beta))/(2.*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (cw*ee*complex(0,1)*sw*complexconjugate(UU2x2)*cmath.sin(beta))/(MP*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1,'QGR':1})

GC_2781 = Coupling(name = 'GC_2781',
                   value = '(cw*ee*complexconjugate(UU2x2)*cmath.sin(beta))/(M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(3)) - (2*cw*ee*sw*complexconjugate(UU2x2)*cmath.sin(beta))/(M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(3))',
                   order = {'QED':1,'QGR':1})

GC_2782 = Coupling(name = 'GC_2782',
                   value = '(ee*complex(0,1)*complexconjugate(NN1x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN1x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2783 = Coupling(name = 'GC_2783',
                   value = '(ee*complex(0,1)*complexconjugate(NN2x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN2x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2784 = Coupling(name = 'GC_2784',
                   value = '(ee*complex(0,1)*complexconjugate(NN3x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN3x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2785 = Coupling(name = 'GC_2785',
                   value = '(ee*complex(0,1)*complexconjugate(NN4x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x3)*complexconjugate(UU2x1)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x1)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN4x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*complexconjugate(UU2x2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2786 = Coupling(name = 'GC_2786',
                   value = '-((ee*complexconjugate(UU1x1)*complexconjugate(VV1x2)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU1x2)*complexconjugate(VV1x1)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2787 = Coupling(name = 'GC_2787',
                   value = '-((ee*complexconjugate(UU2x1)*complexconjugate(VV1x2)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU2x2)*complexconjugate(VV1x1)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2788 = Coupling(name = 'GC_2788',
                   value = '-(ee*complex(0,1)*vu*complexconjugate(VV1x1)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*vd*complexconjugate(VV1x1)*cmath.sin(beta))/(4.*MP*sw) - (complex(0,1)*MUH*complexconjugate(VV1x2)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2789 = Coupling(name = 'GC_2789',
                   value = '-(ee*vu*complexconjugate(VV1x1)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (MUH*complexconjugate(VV1x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)) - (ee*vd*complexconjugate(VV1x1)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2790 = Coupling(name = 'GC_2790',
                   value = '-((ee*complexconjugate(UU1x1)*complexconjugate(VV2x2)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU1x2)*complexconjugate(VV2x1)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2791 = Coupling(name = 'GC_2791',
                   value = '-((ee*complexconjugate(UU2x1)*complexconjugate(VV2x2)*cmath.cos(beta))/(sw*cmath.sqrt(2))) - (ee*complexconjugate(UU2x2)*complexconjugate(VV2x1)*cmath.sin(beta))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_2792 = Coupling(name = 'GC_2792',
                   value = '-(ee*complex(0,1)*vu*complexconjugate(VV2x1)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*vd*complexconjugate(VV2x1)*cmath.sin(beta))/(4.*MP*sw) - (complex(0,1)*MUH*complexconjugate(VV2x2)*cmath.sin(beta))/(MP*cmath.sqrt(2))',
                   order = {'QGR':1})

GC_2793 = Coupling(name = 'GC_2793',
                   value = '-(ee*vu*complexconjugate(VV2x1)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (MUH*complexconjugate(VV2x2)*cmath.sin(beta))/(M32*MP*cmath.sqrt(3)) - (ee*vd*complexconjugate(VV2x1)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QGR':1})

GC_2794 = Coupling(name = 'GC_2794',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) + (ee*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_2795 = Coupling(name = 'GC_2795',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*sw) - (ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_2796 = Coupling(name = 'GC_2796',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2797 = Coupling(name = 'GC_2797',
                   value = '(cw*ee*cmath.cos(beta)*cmath.sin(alp))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*cmath.cos(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_2798 = Coupling(name = 'GC_2798',
                   value = '(ee*complex(0,1)*UU1x1*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) + (ee*complex(0,1)*UU1x1*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2799 = Coupling(name = 'GC_2799',
                   value = '(ee*UU1x1*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*UU1x1*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2800 = Coupling(name = 'GC_2800',
                   value = '(ee*complex(0,1)*UU2x1*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) + (ee*complex(0,1)*UU2x1*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2801 = Coupling(name = 'GC_2801',
                   value = '(ee*UU2x1*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*UU2x1*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2802 = Coupling(name = 'GC_2802',
                   value = '-(ee*complex(0,1)*VV1x1*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) - (ee*complex(0,1)*VV1x1*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2803 = Coupling(name = 'GC_2803',
                   value = '-(ee*VV1x1*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*VV1x1*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2804 = Coupling(name = 'GC_2804',
                   value = '-(ee*complex(0,1)*VV2x1*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) - (ee*complex(0,1)*VV2x1*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2805 = Coupling(name = 'GC_2805',
                   value = '-(ee*VV2x1*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*VV2x1*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2806 = Coupling(name = 'GC_2806',
                   value = '(ee*complex(0,1)*complexconjugate(UU1x1)*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) + (ee*complex(0,1)*complexconjugate(UU1x1)*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2807 = Coupling(name = 'GC_2807',
                   value = '(ee*complexconjugate(UU1x1)*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complexconjugate(UU1x1)*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2808 = Coupling(name = 'GC_2808',
                   value = '(ee*complex(0,1)*complexconjugate(UU2x1)*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) + (ee*complex(0,1)*complexconjugate(UU2x1)*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2809 = Coupling(name = 'GC_2809',
                   value = '(ee*complexconjugate(UU2x1)*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complexconjugate(UU2x1)*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2810 = Coupling(name = 'GC_2810',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x1)*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) - (ee*complex(0,1)*complexconjugate(VV1x1)*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2811 = Coupling(name = 'GC_2811',
                   value = '-(ee*complexconjugate(VV1x1)*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complexconjugate(VV1x1)*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2812 = Coupling(name = 'GC_2812',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x1)*cmath.cos(beta)*cmath.sin(alp))/(4.*MP*sw) - (ee*complex(0,1)*complexconjugate(VV2x1)*cmath.cos(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2813 = Coupling(name = 'GC_2813',
                   value = '-(ee*complexconjugate(VV2x1)*cmath.cos(beta)*cmath.sin(alp))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complexconjugate(VV2x1)*cmath.cos(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2814 = Coupling(name = 'GC_2814',
                   value = '-(ee*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) - (ee*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_2815 = Coupling(name = 'GC_2815',
                   value = '(ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*sw) + (ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_2816 = Coupling(name = 'GC_2816',
                   value = '(cw*ee**2*complex(0,1)*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*complex(0,1)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2817 = Coupling(name = 'GC_2817',
                   value = '(cw*ee*cmath.cos(alp)*cmath.cos(beta))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_2818 = Coupling(name = 'GC_2818',
                   value = '(ee*complex(0,1)*UU1x1*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*UU1x1*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2819 = Coupling(name = 'GC_2819',
                   value = '(ee*UU1x1*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*UU1x1*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2820 = Coupling(name = 'GC_2820',
                   value = '(ee*complex(0,1)*UU2x1*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*UU2x1*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2821 = Coupling(name = 'GC_2821',
                   value = '(ee*UU2x1*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*UU2x1*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2822 = Coupling(name = 'GC_2822',
                   value = '-(ee*complex(0,1)*VV1x1*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) + (ee*complex(0,1)*VV1x1*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2823 = Coupling(name = 'GC_2823',
                   value = '-(ee*VV1x1*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*VV1x1*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2824 = Coupling(name = 'GC_2824',
                   value = '-(ee*complex(0,1)*VV2x1*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) + (ee*complex(0,1)*VV2x1*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2825 = Coupling(name = 'GC_2825',
                   value = '-(ee*VV2x1*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*VV2x1*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2826 = Coupling(name = 'GC_2826',
                   value = '(ee*complex(0,1)*complexconjugate(UU1x1)*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*complexconjugate(UU1x1)*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2827 = Coupling(name = 'GC_2827',
                   value = '(ee*complexconjugate(UU1x1)*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complexconjugate(UU1x1)*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2828 = Coupling(name = 'GC_2828',
                   value = '(ee*complex(0,1)*complexconjugate(UU2x1)*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) - (ee*complex(0,1)*complexconjugate(UU2x1)*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2829 = Coupling(name = 'GC_2829',
                   value = '(ee*complexconjugate(UU2x1)*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complexconjugate(UU2x1)*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2830 = Coupling(name = 'GC_2830',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x1)*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) + (ee*complex(0,1)*complexconjugate(VV1x1)*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2831 = Coupling(name = 'GC_2831',
                   value = '-(ee*complexconjugate(VV1x1)*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complexconjugate(VV1x1)*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2832 = Coupling(name = 'GC_2832',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x1)*cmath.cos(alp)*cmath.cos(beta))/(4.*MP*sw) + (ee*complex(0,1)*complexconjugate(VV2x1)*cmath.sin(alp)*cmath.sin(beta))/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2833 = Coupling(name = 'GC_2833',
                   value = '-(ee*complexconjugate(VV2x1)*cmath.cos(alp)*cmath.cos(beta))/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complexconjugate(VV2x1)*cmath.sin(alp)*cmath.sin(beta))/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2834 = Coupling(name = 'GC_2834',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)**2) - ee*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':1})

GC_2835 = Coupling(name = 'GC_2835',
                   value = '2*ee**2*complex(0,1)*cmath.cos(beta)**2 + 2*ee**2*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':2})

GC_2836 = Coupling(name = 'GC_2836',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_2837 = Coupling(name = 'GC_2837',
                   value = '(ee*cmath.cos(beta)**2)/(2.*sw) + (ee*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':1})

GC_2838 = Coupling(name = 'GC_2838',
                   value = '-(ee**2*cmath.cos(beta)**2)/(2.*sw) - (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_2839 = Coupling(name = 'GC_2839',
                   value = '(ee**2*cmath.cos(beta)**2)/(2.*sw) + (ee**2*cmath.sin(beta)**2)/(2.*sw)',
                   order = {'QED':2})

GC_2840 = Coupling(name = 'GC_2840',
                   value = '-(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2841 = Coupling(name = 'GC_2841',
                   value = '(cw*ee**2*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2842 = Coupling(name = 'GC_2842',
                   value = '-(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':2})

GC_2843 = Coupling(name = 'GC_2843',
                   value = '(cw*ee*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_2844 = Coupling(name = 'GC_2844',
                   value = '-((cw*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2845 = Coupling(name = 'GC_2845',
                   value = '-(cw*ee*complex(0,1)*NN1x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2846 = Coupling(name = 'GC_2846',
                   value = '-(cw*ee*complex(0,1)*NN1x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN1x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN1x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN1x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN1x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN1x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2847 = Coupling(name = 'GC_2847',
                   value = '-(cw*ee*NN1x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2848 = Coupling(name = 'GC_2848',
                   value = '-(cw*ee*NN1x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN1x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN1x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN1x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2849 = Coupling(name = 'GC_2849',
                   value = '-(cw*ee*complex(0,1)*NN2x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2850 = Coupling(name = 'GC_2850',
                   value = '-(cw*ee*complex(0,1)*NN2x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN2x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN2x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN2x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN2x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN2x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2851 = Coupling(name = 'GC_2851',
                   value = '-(cw*ee*NN2x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2852 = Coupling(name = 'GC_2852',
                   value = '-(cw*ee*NN2x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN2x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN2x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN2x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2853 = Coupling(name = 'GC_2853',
                   value = '-(cw*ee*complex(0,1)*NN3x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2854 = Coupling(name = 'GC_2854',
                   value = '-(cw*ee*complex(0,1)*NN3x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN3x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN3x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN3x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN3x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN3x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2855 = Coupling(name = 'GC_2855',
                   value = '-(cw*ee*NN3x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2856 = Coupling(name = 'GC_2856',
                   value = '-(cw*ee*NN3x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN3x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN3x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN3x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2857 = Coupling(name = 'GC_2857',
                   value = '-(cw*ee*complex(0,1)*NN4x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2858 = Coupling(name = 'GC_2858',
                   value = '-(cw*ee*complex(0,1)*NN4x1*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN4x2*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN4x2*sw*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN4x1*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN4x2*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN4x2*sw*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2859 = Coupling(name = 'GC_2859',
                   value = '-(cw*ee*NN4x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2860 = Coupling(name = 'GC_2860',
                   value = '-(cw*ee*NN4x1*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*sw*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (cw*ee*NN4x1*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*NN4x2*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*NN4x2*sw*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2861 = Coupling(name = 'GC_2861',
                   value = '(2*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_2862 = Coupling(name = 'GC_2862',
                   value = '-(ee*UU1x1*cmath.cos(beta)**2)/(4.*MP*sw) + (ee*UU1x1*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2863 = Coupling(name = 'GC_2863',
                   value = '(ee*complex(0,1)*UU1x1*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complex(0,1)*UU1x1*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2864 = Coupling(name = 'GC_2864',
                   value = '-(ee*UU2x1*cmath.cos(beta)**2)/(4.*MP*sw) + (ee*UU2x1*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2865 = Coupling(name = 'GC_2865',
                   value = '(ee*complex(0,1)*UU2x1*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complex(0,1)*UU2x1*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2866 = Coupling(name = 'GC_2866',
                   value = '-(ee*VV1x1*cmath.cos(beta)**2)/(4.*MP*sw) + (ee*VV1x1*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2867 = Coupling(name = 'GC_2867',
                   value = '(ee*complex(0,1)*VV1x1*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complex(0,1)*VV1x1*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2868 = Coupling(name = 'GC_2868',
                   value = '-(ee*VV2x1*cmath.cos(beta)**2)/(4.*MP*sw) + (ee*VV2x1*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2869 = Coupling(name = 'GC_2869',
                   value = '(ee*complex(0,1)*VV2x1*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) - (ee*complex(0,1)*VV2x1*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2870 = Coupling(name = 'GC_2870',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2871 = Coupling(name = 'GC_2871',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN1x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2872 = Coupling(name = 'GC_2872',
                   value = '(cw*ee*complexconjugate(NN1x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN1x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2873 = Coupling(name = 'GC_2873',
                   value = '(cw*ee*complexconjugate(NN1x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN1x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN1x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN1x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2874 = Coupling(name = 'GC_2874',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2875 = Coupling(name = 'GC_2875',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN2x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2876 = Coupling(name = 'GC_2876',
                   value = '(cw*ee*complexconjugate(NN2x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN2x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2877 = Coupling(name = 'GC_2877',
                   value = '(cw*ee*complexconjugate(NN2x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN2x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN2x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN2x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2878 = Coupling(name = 'GC_2878',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2879 = Coupling(name = 'GC_2879',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN3x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2880 = Coupling(name = 'GC_2880',
                   value = '(cw*ee*complexconjugate(NN3x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN3x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2881 = Coupling(name = 'GC_2881',
                   value = '(cw*ee*complexconjugate(NN3x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN3x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN3x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN3x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2882 = Coupling(name = 'GC_2882',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2883 = Coupling(name = 'GC_2883',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN4x1)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(4.*MP*(-1 + sw)*(1 + sw))',
                   order = {'QED':1,'QGR':1})

GC_2884 = Coupling(name = 'GC_2884',
                   value = '(cw*ee*complexconjugate(NN4x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN4x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2885 = Coupling(name = 'GC_2885',
                   value = '(cw*ee*complexconjugate(NN4x1)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) + (ee*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) - (ee*sw*complexconjugate(NN4x2)*cmath.cos(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (cw*ee*complexconjugate(NN4x1)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6)) - (ee*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*sw*(1 + sw)*cmath.sqrt(6)) + (ee*sw*complexconjugate(NN4x2)*cmath.sin(beta)**2)/(2.*M32*MP*(-1 + sw)*(1 + sw)*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2886 = Coupling(name = 'GC_2886',
                   value = '(ee*complexconjugate(UU1x1)*cmath.cos(beta)**2)/(4.*MP*sw) - (ee*complexconjugate(UU1x1)*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2887 = Coupling(name = 'GC_2887',
                   value = '-(ee*complex(0,1)*complexconjugate(UU1x1)*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complex(0,1)*complexconjugate(UU1x1)*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2888 = Coupling(name = 'GC_2888',
                   value = '(ee*complexconjugate(UU2x1)*cmath.cos(beta)**2)/(4.*MP*sw) - (ee*complexconjugate(UU2x1)*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2889 = Coupling(name = 'GC_2889',
                   value = '-(ee*complex(0,1)*complexconjugate(UU2x1)*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complex(0,1)*complexconjugate(UU2x1)*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2890 = Coupling(name = 'GC_2890',
                   value = '(ee*complexconjugate(VV1x1)*cmath.cos(beta)**2)/(4.*MP*sw) - (ee*complexconjugate(VV1x1)*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2891 = Coupling(name = 'GC_2891',
                   value = '-(ee*complex(0,1)*complexconjugate(VV1x1)*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complex(0,1)*complexconjugate(VV1x1)*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2892 = Coupling(name = 'GC_2892',
                   value = '(ee*complexconjugate(VV2x1)*cmath.cos(beta)**2)/(4.*MP*sw) - (ee*complexconjugate(VV2x1)*cmath.sin(beta)**2)/(4.*MP*sw)',
                   order = {'QED':1,'QGR':1})

GC_2893 = Coupling(name = 'GC_2893',
                   value = '-(ee*complex(0,1)*complexconjugate(VV2x1)*cmath.cos(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6)) + (ee*complex(0,1)*complexconjugate(VV2x1)*cmath.sin(beta)**2)/(2.*M32*MP*sw*cmath.sqrt(6))',
                   order = {'QED':1,'QGR':1})

GC_2894 = Coupling(name = 'GC_2894',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2895 = Coupling(name = 'GC_2895',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2896 = Coupling(name = 'GC_2896',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_2897 = Coupling(name = 'GC_2897',
                   value = '-(ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(beta)**2*cmath.sin(alp))/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.cos(alp)*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(beta)*cmath.sin(alp)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*vd*cmath.cos(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*vu*cmath.sin(alp)*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

