ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP5()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_274 = (MDL_COMPLEXI*MDL_RN2X2*MDL_SQRT__2)/MDL_MP
      GC_276 = -((MDL_COMPLEXI*MDL_RN3X3)/(MDL_MP*MDL_SQRT__2))
      GC_277 = (MDL_COMPLEXI*MDL_RN3X3*MDL_SQRT__2)/MDL_MP
      GC_280 = -((MDL_COMPLEXI*MDL_RU1X1)/(MDL_MP*MDL_SQRT__2))
      GC_281 = (MDL_COMPLEXI*MDL_RU1X1*MDL_SQRT__2)/MDL_MP
      GC_289 = -((MDL_COMPLEXI*MDL_RU2X2)/(MDL_MP*MDL_SQRT__2))
      GC_290 = (MDL_COMPLEXI*MDL_RU2X2*MDL_SQRT__2)/MDL_MP
      GC_298 = -((MDL_COMPLEXI*MDL_RU3X3)/(MDL_MP*MDL_SQRT__2))
      GC_299 = (MDL_COMPLEXI*MDL_RU3X3*MDL_SQRT__2)/MDL_MP
      GC_307 = (MDL_COMPLEXI*MDL_RU3X6)/(MDL_MP*MDL_SQRT__2)
      GC_308 = -((MDL_COMPLEXI*MDL_RU3X6*MDL_SQRT__2)/MDL_MP)
      GC_316 = (MDL_COMPLEXI*MDL_RU4X4)/(MDL_MP*MDL_SQRT__2)
      GC_317 = -((MDL_COMPLEXI*MDL_RU4X4*MDL_SQRT__2)/MDL_MP)
      GC_325 = (MDL_COMPLEXI*MDL_RU5X5)/(MDL_MP*MDL_SQRT__2)
      GC_326 = -((MDL_COMPLEXI*MDL_RU5X5*MDL_SQRT__2)/MDL_MP)
      GC_334 = -((MDL_COMPLEXI*MDL_RU6X3)/(MDL_MP*MDL_SQRT__2))
      GC_335 = (MDL_COMPLEXI*MDL_RU6X3*MDL_SQRT__2)/MDL_MP
      GC_343 = (MDL_COMPLEXI*MDL_RU6X6)/(MDL_MP*MDL_SQRT__2)
      GC_344 = -((MDL_COMPLEXI*MDL_RU6X6*MDL_SQRT__2)/MDL_MP)
      GC_695 = -(MDL_CW*MDL_NN1X1)/(2.000000D+00*MDL_MP)-(MDL_NN1X2
     $ *MDL_SW)/(2.000000D+00*MDL_MP)
      GC_697 = -(MDL_CW*MDL_NN2X1)/(2.000000D+00*MDL_MP)-(MDL_NN2X2
     $ *MDL_SW)/(2.000000D+00*MDL_MP)
      GC_699 = -(MDL_CW*MDL_NN3X1)/(2.000000D+00*MDL_MP)-(MDL_NN3X2
     $ *MDL_SW)/(2.000000D+00*MDL_MP)
      GC_701 = -(MDL_CW*MDL_NN4X1)/(2.000000D+00*MDL_MP)-(MDL_NN4X2
     $ *MDL_SW)/(2.000000D+00*MDL_MP)
      GC_961 = (MDL_CW*MDL_NN1X2)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_NN1X1*MDL_SW)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_NN1X2*MDL_SW__EXP__2)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_NN1X1
     $ *MDL_SW__EXP__3)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_963 = (MDL_CW*MDL_NN2X2)/(2.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_NN2X1*MDL_SW)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_NN2X2*MDL_SW__EXP__2)/(2.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_NN2X1
     $ *MDL_SW__EXP__3)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      END
