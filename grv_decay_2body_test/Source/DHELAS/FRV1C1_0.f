C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2
C     ,1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FRV1C1_0(R2, F1, V3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 V3(*)
      COMPLEX*16 R2(*)
      COMPLEX*16 F1(*)
      COMPLEX*16 TMP26
      COMPLEX*16 VERTEX
      COMPLEX*16 TMP27
      COMPLEX*16 COUP
      TMP26 = (F1(3)*-1D0*(R2(7)*V3(4)+R2(11)*V3(5)+R2(15)*V3(6)
     $ -R2(3)*V3(3))-F1(4)*(R2(8)*V3(4)+R2(12)*V3(5)+R2(16)*V3(6)
     $ -R2(4)*V3(3)))
      TMP27 = (F1(3)*(V3(3)*(R2(3)+R2(8)+R2(15)-CI*(R2(12)))+(V3(4)*
     $ -1D0*(R2(4)+R2(7)+CI*(R2(11))-R2(16))+(V3(5)*(-CI*(R2(16))
     $ +CI*(R2(4)+R2(7))-R2(11))-V3(6)*(R2(3)+R2(8)+R2(15)-CI
     $ *(R2(12))))))+F1(4)*(V3(3)*(R2(4)+R2(7)+CI*(R2(11))-R2(16))
     $ +(V3(4)*-1D0*(R2(3)+R2(8)+R2(15)-CI*(R2(12)))+(V3(5)*-1D0
     $ *(R2(12)+CI*(R2(3)+R2(8)+R2(15)))+V3(6)*(R2(4)+R2(7)+CI
     $ *(R2(11))-R2(16))))))
      VERTEX = COUP*(-CI*(TMP27)+2D0 * CI*(TMP26))
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (Gamma(2,2,-2)*Gamma(3,-2,-1)*ProjM(-1,1) - 2*Metric(2,3)*ProjM(2
C     ,1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FRV1_2_3_4C1_0(R2, F1, V3, COUP1, COUP2, COUP3, COUP4
     $ ,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 V3(*)
      COMPLEX*16 R2(*)
      COMPLEX*16 F1(*)
      COMPLEX*16 COUP1
      COMPLEX*16 COUP2
      COMPLEX*16 COUP3
      COMPLEX*16 VERTEX
      COMPLEX*16 TMP
      COMPLEX*16 COUP4
      CALL FRV1C1_0(R2,F1,V3,COUP1,VERTEX)
      CALL FRV2C1_0(R2,F1,V3,COUP2,TMP)
      VERTEX = VERTEX + TMP
      CALL FRV3C1_0(R2,F1,V3,COUP3,TMP)
      VERTEX = VERTEX + TMP
      CALL FRV4C1_0(R2,F1,V3,COUP4,TMP)
      VERTEX = VERTEX + TMP
      END

