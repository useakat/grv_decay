C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2,
C     1)
C     
      SUBROUTINE FRV1_0(F1, R2, V3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 R2(*)
      COMPLEX*16 F1(*)
      COMPLEX*16 TMP26
      COMPLEX*16 V3(*)
      COMPLEX*16 VERTEX
      COMPLEX*16 TMP25
      TMP25 = (F1(3)*(V3(3)*-1D0*(R2(8)+R2(15)+CI*(R2(12))-R2(3))
     $ +(V3(4)*(R2(4)+R2(16)+CI*(R2(11))-R2(7))+(V3(5)*(-CI*(R2(7))
     $ +CI*(R2(4)+R2(16))-R2(11))-V3(6)*(R2(8)+R2(15)+CI*(R2(12))
     $ -R2(3)))))+F1(4)*(V3(3)*(R2(4)+R2(16)+CI*(R2(11))-R2(7))
     $ +(V3(4)*-1D0*(R2(8)+R2(15)+CI*(R2(12))-R2(3))+(V3(5)*(
     $ -CI*(R2(3))+CI*(R2(8)+R2(15))-R2(12))-V3(6)*(R2(4)+R2(16)
     $ +CI*(R2(11))-R2(7))))))
      TMP26 = (F1(3)*-1D0*(R2(7)*V3(4)+R2(11)*V3(5)+R2(15)*V3(6)
     $ -R2(3)*V3(3))-F1(4)*(R2(8)*V3(4)+R2(12)*V3(5)+R2(16)*V3(6)
     $ -R2(4)*V3(3)))
      VERTEX = COUP*(-CI*(TMP25)+2D0 * CI*(TMP26))
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2,
C     1)
C     
      SUBROUTINE FRV1_2_3_4_0(F1, R2, V3, COUP1, COUP2, COUP3, COUP4
     $ ,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 R2(*)
      COMPLEX*16 F1(*)
      COMPLEX*16 COUP1
      COMPLEX*16 COUP2
      COMPLEX*16 TMP
      COMPLEX*16 V3(*)
      COMPLEX*16 VERTEX
      COMPLEX*16 COUP3
      COMPLEX*16 COUP4
      CALL FRV1_0(F1,R2,V3,COUP1,VERTEX)
      CALL FRV2_0(F1,R2,V3,COUP2,TMP)
      VERTEX = VERTEX + TMP
      CALL FRV3_0(F1,R2,V3,COUP3,TMP)
      VERTEX = VERTEX + TMP
      CALL FRV4_0(F1,R2,V3,COUP4,TMP)
      VERTEX = VERTEX + TMP
      END


