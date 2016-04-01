ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP10()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_2768 = -(MDL_MUH*MDL_CONJG__NN4X3*MDL_COS__BETA)/(2.000000D
     $ +00*MDL_MP)-(MDL_MUH*MDL_CONJG__NN4X4*MDL_SIN__BETA)/(2.000000D
     $ +00*MDL_MP)
      END
