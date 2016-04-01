C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     P(-1,3)*Gamma(-1,-3,-2)*Gamma(1,2,-3)*ProjP(-2,1)
C     
      SUBROUTINE RFS4_0(R1, F2, S3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 R1(*)
      COMPLEX*16 S3(*)
      REAL*8 P3(0:3)
      COMPLEX*16 F2(*)
      COMPLEX*16 TMP32
      COMPLEX*16 VERTEX
      COMPLEX*16 COUP
      P3(0) = DBLE(S3(1))
      P3(1) = DBLE(S3(2))
      P3(2) = DIMAG(S3(2))
      P3(3) = DIMAG(S3(1))
      TMP32 = (F2(5)*(P3(0)*(R1(5)+R1(10)+R1(17)-CI*(R1(14)))
     $ +(P3(1)*-1D0*(R1(6)+R1(9)+R1(18)-CI*(R1(13)))+(P3(2)*(
     $ -CI*(R1(9))+CI*(R1(6)+R1(18))-R1(13))-P3(3)*(R1(5)+R1(17)
     $ +CI*(R1(14))-R1(10)))))+F2(6)*(P3(0)*(R1(6)+R1(9)+CI*(R1(13))
     $ -R1(18))+(P3(1)*-1D0*(R1(5)+R1(10)+CI*(R1(14))-R1(17))
     $ +(P3(2)*(-CI*(R1(5))+CI*(R1(10)+R1(17))-R1(14))-P3(3)*(R1(9)
     $ +R1(18)+CI*(R1(13))-R1(6))))))
      VERTEX = COUP*-CI * TMP32*S3(3)
      END


