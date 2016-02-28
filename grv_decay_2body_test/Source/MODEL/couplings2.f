ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP2()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1086 = (MDL_COMPLEXI*MDL_I40X36*MDL_VU)/(2.000000D+00*MDL_MP)
      GC_1095 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN1X3*MDL_VD)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN1X4*MDL_VU)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1097 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN2X3*MDL_VD)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN2X4*MDL_VU)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1099 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN3X3*MDL_VD)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN3X4*MDL_VU)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1101 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN4X3*MDL_VD)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN4X4*MDL_VU)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1128 = (MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_VV1X2)/(2.000000D
     $ +00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_1165 = (MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_VV2X2)/(2.000000D
     $ +00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_1257 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__NN1X3)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__NN1X4
     $ )/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1338 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__NN2X3)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__NN2X4
     $ )/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1419 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__NN3X3)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__NN3X4
     $ )/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1500 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__NN4X3)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__NN4X4
     $ )/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))
      GC_1837 = (MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__UU1X2)
     $ /(2.000000D+00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_1884 = (MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__UU2X2)
     $ /(2.000000D+00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_1935 = -(MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__VV1X2)
     $ /(2.000000D+00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_1980 = -(MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__VV2X2)
     $ /(2.000000D+00*MDL_MP*MDL_SW*MDL_SQRT__2)
      GC_2370 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN1X1*MDL_VD*MDL_COS__A
     $ LP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN1X2*MDL_VD*MDL_COS__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN1X2*MDL_SW*MDL_VD
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN1X4*MDL_CONJG__MUH
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN1X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI
     $ *MDL_NN1X1*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEX
     $ I*MDL_NN1X2*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE
     $ *MDL_COMPLEXI*MDL_NN1X2*MDL_SW*MDL_VU*MDL_SIN__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_NN1X3*MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_NN1X3*MDL_SW__EXP__2*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_2372 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN1X1*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN1X2*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN1X2
     $ *MDL_SW*MDL_VU*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN1X3
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN1X3
     $ *MDL_SW__EXP__2*MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN1X1*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN1X2*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN1X2*MDL_SW*MDL_VD
     $ *MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN1X4*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN1X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_2374 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN2X1*MDL_VD*MDL_COS__A
     $ LP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN2X2*MDL_VD*MDL_COS__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN2X2*MDL_SW*MDL_VD
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN2X4*MDL_CONJG__MUH
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN2X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI
     $ *MDL_NN2X1*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEX
     $ I*MDL_NN2X2*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE
     $ *MDL_COMPLEXI*MDL_NN2X2*MDL_SW*MDL_VU*MDL_SIN__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_NN2X3*MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_NN2X3*MDL_SW__EXP__2*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_2376 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN2X1*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN2X2*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN2X2
     $ *MDL_SW*MDL_VU*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN2X3
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN2X3
     $ *MDL_SW__EXP__2*MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN2X1*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN2X2*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN2X2*MDL_SW*MDL_VD
     $ *MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN2X4*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN2X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_2378 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN3X1*MDL_VD*MDL_COS__A
     $ LP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN3X2*MDL_VD*MDL_COS__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN3X2*MDL_SW*MDL_VD
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN3X4*MDL_CONJG__MUH
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN3X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI
     $ *MDL_NN3X1*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEX
     $ I*MDL_NN3X2*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE
     $ *MDL_COMPLEXI*MDL_NN3X2*MDL_SW*MDL_VU*MDL_SIN__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_NN3X3*MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_NN3X3*MDL_SW__EXP__2*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_2380 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN3X1*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN3X2*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN3X2
     $ *MDL_SW*MDL_VU*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN3X3
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN3X3
     $ *MDL_SW__EXP__2*MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN3X1*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN3X2*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN3X2*MDL_SW*MDL_VD
     $ *MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN3X4*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN3X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_2382 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN4X1*MDL_VD*MDL_COS__A
     $ LP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN4X2*MDL_VD*MDL_COS__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN4X2*MDL_SW*MDL_VD
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN4X4*MDL_CONJG__MUH
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN4X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_CW*MDL_EE*MDL_COMPLEXI
     $ *MDL_NN4X1*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEX
     $ I*MDL_NN4X2*MDL_VU*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE
     $ *MDL_COMPLEXI*MDL_NN4X2*MDL_SW*MDL_VU*MDL_SIN__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_NN4X3*MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_NN4X3*MDL_SW__EXP__2*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_2384 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN4X1*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN4X2*MDL_VU
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN4X2
     $ *MDL_SW*MDL_VU*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN4X3
     $ *MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN4X3
     $ *MDL_SW__EXP__2*MDL_CONJG__MUH*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_NN4X1*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_NN4X2*MDL_VD*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*MDL_SW*(1.000000D
     $ +00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_NN4X2*MDL_SW*MDL_VD
     $ *MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_COMPLEXI*MDL_NN4X4*MDL_CONJG__MUH
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_COMPLEXI*MDL_NN4X4*MDL_SW__EXP__2
     $ *MDL_CONJG__MUH*MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D
     $ +00+MDL_SW)*(1.000000D+00+MDL_SW))
      GC_2390 = -(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__NN1X1
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI*MDL_VD*MDL_CONJG__N
     $ N1X2*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI
     $ *MDL_SW*MDL_VD*MDL_CONJG__NN1X2*MDL_COS__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_MUH*MDL_CONJG__NN1X4*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_MUH*MDL_SW__EXP__2*MDL_CONJG__NN1X4
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU
     $ *MDL_CONJG__NN1X1*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEX
     $ I*MDL_VU*MDL_CONJG__NN1X2*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))+(MDL_EE
     $ *MDL_COMPLEXI*MDL_SW*MDL_VU*MDL_CONJG__NN1X2*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_COMPLEXI*MDL_MUH*MDL_CONJG__NN1X3*MDL_SIN__ALP)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_COMPLEXI*MDL_MUH*MDL_SW__EXP__2*MDL_CONJG__NN1X3
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      GC_2398 = (MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__NN1X1
     $ *MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEXI*MDL_VU*MDL_CONJG__N
     $ N1X2*MDL_COS__ALP)/(4.000000D+00*MDL_MP*(-1.000000D+00
     $ +MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))+(MDL_EE*MDL_COMPLEXI
     $ *MDL_SW*MDL_VU*MDL_CONJG__NN1X2*MDL_COS__ALP)/(4.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ -(MDL_COMPLEXI*MDL_MUH*MDL_CONJG__NN1X3*MDL_COS__ALP)/(2.000000D
     $ +00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))
     $ +(MDL_COMPLEXI*MDL_MUH*MDL_SW__EXP__2*MDL_CONJG__NN1X3
     $ *MDL_COS__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))+(MDL_CW*MDL_EE*MDL_COMPLEXI*MDL_VD
     $ *MDL_CONJG__NN1X1*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*(1.000000D+00+MDL_SW))-(MDL_EE*MDL_COMPLEX
     $ I*MDL_VD*MDL_CONJG__NN1X2*MDL_SIN__ALP)/(4.000000D+00*MDL_MP*(
     $ -1.000000D+00+MDL_SW)*MDL_SW*(1.000000D+00+MDL_SW))+(MDL_EE
     $ *MDL_COMPLEXI*MDL_SW*MDL_VD*MDL_CONJG__NN1X2*MDL_SIN__ALP)
     $ /(4.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))+(MDL_COMPLEXI*MDL_MUH*MDL_CONJG__NN1X4*MDL_SIN__ALP)
     $ /(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)*(1.000000D+00
     $ +MDL_SW))-(MDL_COMPLEXI*MDL_MUH*MDL_SW__EXP__2*MDL_CONJG__NN1X4
     $ *MDL_SIN__ALP)/(2.000000D+00*MDL_MP*(-1.000000D+00+MDL_SW)
     $ *(1.000000D+00+MDL_SW))
      END
