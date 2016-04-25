ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1 = -(MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_2 = (2.000000D+00*MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_695 = -(MDL_CW*MDL_NN1X1)/(2.000000D+00*MDL_MP)-(MDL_NN1X2
     $ *MDL_SW)/(2.000000D+00*MDL_MP)
      GC_1194 = (MDL_CW*MDL_CONJG__NN1X1)/(2.000000D+00*MDL_MP)
     $ +(MDL_SW*MDL_CONJG__NN1X2)/(2.000000D+00*MDL_MP)
      END
