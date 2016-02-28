C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjP(-1,1) - 2*Metric(2,3)*ProjP(2
C     ,1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FRV3C1_0(R2, F1, V3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 V3(*)
      COMPLEX*16 R2(*)
      COMPLEX*16 TMP23
      COMPLEX*16 F1(*)
      COMPLEX*16 VERTEX
      COMPLEX*16 TMP24
      COMPLEX*16 COUP
      TMP24 = (F1(5)*(V3(3)*(R2(5)+CI*(R2(14))-R2(10)-R2(17))
     $ +(V3(4)*(R2(6)+R2(18)-CI*(R2(13))-R2(9))+(V3(5)*-1D0*(R2(13)
     $ -CI*(R2(9))+CI*(R2(6)+R2(18)))+V3(6)*(R2(5)+CI*(R2(14))-R2(10)
     $ -R2(17)))))+F1(6)*(V3(3)*(R2(6)+R2(18)-CI*(R2(13))-R2(9))
     $ +(V3(4)*(R2(5)+CI*(R2(14))-R2(10)-R2(17))+(V3(5)*-1D0*(R2(14)
     $ -CI*(R2(5))+CI*(R2(10)+R2(17)))+V3(6)*(R2(9)+CI*(R2(13))-R2(6)
     $ -R2(18))))))
      TMP23 = (F1(5)*-1D0*(R2(9)*V3(4)+R2(13)*V3(5)+R2(17)*V3(6)
     $ -R2(5)*V3(3))-F1(6)*(R2(10)*V3(4)+R2(14)*V3(5)+R2(18)*V3(6)
     $ -R2(6)*V3(3)))
      VERTEX = COUP*(-CI*(TMP24)+2D0 * CI*(TMP23))
      END


