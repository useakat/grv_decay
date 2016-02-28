ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP6()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_965 = (MDL_CW*MDL_NN3X2)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_NN3X1*MDL_SW)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_NN3X2*MDL_SW__EXP__2)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_NN3X1
     $ *MDL_SW__EXP__3)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_967 = (MDL_CW*MDL_NN4X2)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_NN4X1*MDL_SW)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_NN4X2*MDL_SW__EXP__2)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_NN4X1
     $ *MDL_SW__EXP__3)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_969 = -MDL_UU1X1/(2.000000D+00*MDL_MP)
      GC_1006 = -MDL_UU2X1/(2.000000D+00*MDL_MP)
      GC_1103 = MDL_VV1X1/(2.000000D+00*MDL_MP)
      GC_1140 = MDL_VV2X1/(2.000000D+00*MDL_MP)
      GC_1194 = (MDL_CW*MDL_CONJG__NN1X1)/(2.000000D+00*MDL_MP)
     $ +(MDL_SW*MDL_CONJG__NN1X2)/(2.000000D+00*MDL_MP)
      GC_1219 = (MDL_SW*MDL_CONJG__NN1X1)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_SW__EXP__3
     $ *MDL_CONJG__NN1X1)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_CONJG__NN1X2)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_CW*MDL_SW__EXP__2*MDL_CONJG__NN1X2)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_1275 = (MDL_CW*MDL_CONJG__NN2X1)/(2.000000D+00*MDL_MP)
     $ +(MDL_SW*MDL_CONJG__NN2X2)/(2.000000D+00*MDL_MP)
      GC_1300 = (MDL_SW*MDL_CONJG__NN2X1)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_SW__EXP__3
     $ *MDL_CONJG__NN2X1)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_CONJG__NN2X2)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_CW*MDL_SW__EXP__2*MDL_CONJG__NN2X2)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_1356 = (MDL_CW*MDL_CONJG__NN3X1)/(2.000000D+00*MDL_MP)
     $ +(MDL_SW*MDL_CONJG__NN3X2)/(2.000000D+00*MDL_MP)
      GC_1381 = (MDL_SW*MDL_CONJG__NN3X1)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_SW__EXP__3
     $ *MDL_CONJG__NN3X1)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_CONJG__NN3X2)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_CW*MDL_SW__EXP__2*MDL_CONJG__NN3X2)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_1437 = (MDL_CW*MDL_CONJG__NN4X1)/(2.000000D+00*MDL_MP)
     $ +(MDL_SW*MDL_CONJG__NN4X2)/(2.000000D+00*MDL_MP)
      GC_1462 = (MDL_SW*MDL_CONJG__NN4X1)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_SW__EXP__3
     $ *MDL_CONJG__NN4X1)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_CONJG__NN4X2)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_CW*MDL_SW__EXP__2*MDL_CONJG__NN4X2)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_1505 = -((MDL_COMPLEXI*MDL_CONJG__RD1X1)/(MDL_MP*MDL_SQRT__2))
      GC_1518 = -((MDL_COMPLEXI*MDL_CONJG__RD2X2)/(MDL_MP*MDL_SQRT__2))
      GC_1531 = -((MDL_COMPLEXI*MDL_CONJG__RD3X3)/(MDL_MP*MDL_SQRT__2))
      GC_1544 = (MDL_COMPLEXI*MDL_CONJG__RD3X6)/(MDL_MP*MDL_SQRT__2)
      GC_1557 = (MDL_COMPLEXI*MDL_CONJG__RD4X4)/(MDL_MP*MDL_SQRT__2)
      GC_1570 = (MDL_COMPLEXI*MDL_CONJG__RD5X5)/(MDL_MP*MDL_SQRT__2)
      GC_1583 = -((MDL_COMPLEXI*MDL_CONJG__RD6X3)/(MDL_MP*MDL_SQRT__2))
      GC_1596 = (MDL_COMPLEXI*MDL_CONJG__RD6X6)/(MDL_MP*MDL_SQRT__2)
      GC_1608 = -((MDL_COMPLEXI*MDL_CONJG__RL1X1)/(MDL_MP*MDL_SQRT__2))
      GC_1618 = -((MDL_COMPLEXI*MDL_CONJG__RL2X2)/(MDL_MP*MDL_SQRT__2))
      GC_1628 = -((MDL_COMPLEXI*MDL_CONJG__RL3X3)/(MDL_MP*MDL_SQRT__2))
      END
