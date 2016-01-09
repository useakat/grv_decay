C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     -(Epsilon(1,3,-1,-2)*P(-1,3)*Gamma(-2,2,-3)*ProjM(-3,1)) +
C      complex(0,1)*P(-1,3)*Gamma(-1,2,-2)*Metric(1,3)*ProjM(-2,1) -
C      complex(0,1)*P(1,3)*Gamma(3,2,-1)*ProjM(-1,1) + Epsilon(1,3,-1,-
C     2)*P(-1,3)*Gamma(-2,2,-3)*ProjP(-3,1) + complex(0,1)*P(-1,3)*Gamm
C     a(-1,2,-2)*Metric(1,3)*ProjP(-2,1) - complex(0,1)*P(1,3)*Gamma(3,
C     2,-1)*ProjP(-1,1)
C     
      SUBROUTINE RFV4_0(R1, F2, V3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 R1(*)
      COMPLEX*16 V3(*)
      COMPLEX*16 TMP37
      COMPLEX*16 TMP36
      REAL*8 P3(0:3)
      COMPLEX*16 F2(*)
      COMPLEX*16 TMP32
      COMPLEX*16 VERTEX
      COMPLEX*16 TMP34
      COMPLEX*16 COUP
      COMPLEX*16 TMP35
      COMPLEX*16 TMP33
      P3(0) = DBLE(V3(1))
      P3(1) = DBLE(V3(2))
      P3(2) = DIMAG(V3(2))
      P3(3) = DIMAG(V3(1))
      TMP33 = (F2(5)*(V3(3)*(R1(3)*(P3(0)+P3(3))+R1(4)*(P3(1)
     $ -CI*(P3(2))))+(V3(4)*(R1(7)*-1D0*(P3(0)+P3(3))+R1(8)*(
     $ +CI*(P3(2))-P3(1)))+(V3(5)*(R1(12)*(+CI*(P3(2))-P3(1))
     $ -R1(11)*(P3(0)+P3(3)))+V3(6)*(R1(15)*-1D0*(P3(0)+P3(3))
     $ +R1(16)*(+CI*(P3(2))-P3(1))))))+F2(6)*(V3(3)*(R1(3)*(P3(1)
     $ +CI*(P3(2)))+R1(4)*(P3(0)-P3(3)))+(V3(4)*(R1(7)*-1D0*(P3(1)
     $ +CI*(P3(2)))+R1(8)*(P3(3)-P3(0)))+(V3(5)*(R1(12)*(P3(3)-P3(0))
     $ -R1(11)*(P3(1)+CI*(P3(2))))+V3(6)*(R1(15)*-1D0*(P3(1)+CI
     $ *(P3(2)))+R1(16)*(P3(3)-P3(0)))))))
      TMP32 = (F2(5)*(P3(0)*(R1(16)*(V3(5)+CI*(V3(4)))+(V3(6)*
     $ -1D0*(R1(12)+CI*(R1(8)))+(V3(4)*R1(11)-V3(5)*R1(7))))+(P3(1)
     $ *(R1(11)*-1D0*(V3(3)+V3(6))+(V3(5)*(R1(3)+R1(15))+(-CI*(V3(3)
     $ *R1(16))+CI*(V3(6)*R1(4)))))+(P3(2)*(R1(7)*(V3(3)+V3(6))
     $ +(V3(4)*-1D0*(R1(3)+R1(15))+(V3(6)*R1(4)-V3(3)*R1(16))))
     $ +P3(3)*(R1(4)*-1D0*(V3(5)+CI*(V3(4)))+(V3(3)*(R1(12)+CI
     $ *(R1(8)))+(V3(4)*R1(11)-V3(5)*R1(7)))))))+F2(6)*(P3(0)*(R1(15)
     $ *(V3(5)-CI*(V3(4)))+(V3(6)*(+CI*(R1(7))-R1(11))+(V3(5)*R1(8)
     $ -V3(4)*R1(12))))+(P3(1)*(R1(12)*(V3(3)-V3(6))+(V3(5)*(R1(16)
     $ -R1(4))+(-CI*(V3(6)*R1(3))+CI*(V3(3)*R1(15)))))+(P3(2)*(R1(8)
     $ *(V3(6)-V3(3))+(V3(4)*(R1(4)-R1(16))+(V3(6)*R1(3)-V3(3)
     $ *R1(15))))+P3(3)*(R1(3)*(+CI*(V3(4))-V3(5))+(V3(3)*(R1(11)
     $ -CI*(R1(7)))+(V3(4)*R1(12)-V3(5)*R1(8))))))))
      TMP37 = (F2(3)*(P3(0)*(R1(5)*(V3(3)-V3(6))+R1(6)*(+CI*(V3(5))
     $ -V3(4)))+(P3(1)*(R1(9)*(V3(6)-V3(3))+R1(10)*(V3(4)-CI*(V3(5))))
     $ +(P3(2)*(R1(13)*(V3(6)-V3(3))+R1(14)*(V3(4)-CI*(V3(5))))
     $ +P3(3)*(R1(17)*(V3(6)-V3(3))+R1(18)*(V3(4)-CI*(V3(5)))))))
     $ +F2(4)*(P3(0)*(R1(5)*-1D0*(V3(4)+CI*(V3(5)))+R1(6)*(V3(3)
     $ +V3(6)))+(P3(1)*(R1(9)*(V3(4)+CI*(V3(5)))-R1(10)*(V3(3)+V3(6)))
     $ +(P3(2)*(R1(13)*(V3(4)+CI*(V3(5)))-R1(14)*(V3(3)+V3(6)))
     $ +P3(3)*(R1(17)*(V3(4)+CI*(V3(5)))-R1(18)*(V3(3)+V3(6)))))))
      TMP36 = (F2(3)*(V3(3)*(R1(5)*(P3(0)-P3(3))+R1(6)*(+CI*(P3(2))
     $ -P3(1)))+(V3(4)*(R1(9)*(P3(3)-P3(0))+R1(10)*(P3(1)-CI*(P3(2))))
     $ +(V3(5)*(R1(13)*(P3(3)-P3(0))+R1(14)*(P3(1)-CI*(P3(2))))
     $ +V3(6)*(R1(17)*(P3(3)-P3(0))+R1(18)*(P3(1)-CI*(P3(2)))))))
     $ +F2(4)*(V3(3)*(R1(5)*-1D0*(P3(1)+CI*(P3(2)))+R1(6)*(P3(0)
     $ +P3(3)))+(V3(4)*(R1(9)*(P3(1)+CI*(P3(2)))-R1(10)*(P3(0)+P3(3)))
     $ +(V3(5)*(R1(13)*(P3(1)+CI*(P3(2)))-R1(14)*(P3(0)+P3(3)))
     $ +V3(6)*(R1(17)*(P3(1)+CI*(P3(2)))-R1(18)*(P3(0)+P3(3)))))))
      TMP35 = (F2(3)*(P3(0)*(R1(18)*-1D0*(V3(5)+CI*(V3(4)))+(V3(6)
     $ *(R1(14)+CI*(R1(10)))+(V3(5)*R1(9)-V3(4)*R1(13))))+(P3(1)
     $ *(R1(13)*(V3(3)-V3(6))+(V3(5)*(R1(17)-R1(5))+(-CI*(V3(6)*R1(6))
     $ +CI*(V3(3)*R1(18)))))+(P3(2)*(R1(9)*(V3(6)-V3(3))+(V3(4)*(R1(5)
     $ -R1(17))+(V3(3)*R1(18)-V3(6)*R1(6))))+P3(3)*(R1(6)*(V3(5)
     $ +CI*(V3(4)))+(V3(3)*-1D0*(R1(14)+CI*(R1(10)))+(V3(4)*R1(13)
     $ -V3(5)*R1(9)))))))+F2(4)*(P3(0)*(R1(17)*(+CI*(V3(4))-V3(5))
     $ +(V3(6)*(R1(13)-CI*(R1(9)))+(V3(4)*R1(14)-V3(5)*R1(10))))
     $ +(P3(1)*(R1(14)*-1D0*(V3(3)+V3(6))+(V3(5)*(R1(6)+R1(18))
     $ +(-CI*(V3(3)*R1(17))+CI*(V3(6)*R1(5)))))+(P3(2)*(R1(10)*(V3(3)
     $ +V3(6))+(V3(4)*-1D0*(R1(6)+R1(18))+(V3(3)*R1(17)-V3(6)*R1(5))))
     $ +P3(3)*(R1(5)*(V3(5)-CI*(V3(4)))+(V3(3)*(+CI*(R1(9))-R1(13))
     $ +(V3(4)*R1(14)-V3(5)*R1(10))))))))
      TMP34 = (F2(5)*(P3(0)*(R1(3)*(V3(3)+V3(6))+R1(4)*(V3(4)
     $ -CI*(V3(5))))+(P3(1)*(R1(7)*-1D0*(V3(3)+V3(6))+R1(8)*(
     $ +CI*(V3(5))-V3(4)))+(P3(2)*(R1(12)*(+CI*(V3(5))-V3(4))
     $ -R1(11)*(V3(3)+V3(6)))+P3(3)*(R1(15)*-1D0*(V3(3)+V3(6))
     $ +R1(16)*(+CI*(V3(5))-V3(4))))))+F2(6)*(P3(0)*(R1(3)*(V3(4)
     $ +CI*(V3(5)))+R1(4)*(V3(3)-V3(6)))+(P3(1)*(R1(7)*-1D0*(V3(4)
     $ +CI*(V3(5)))+R1(8)*(V3(6)-V3(3)))+(P3(2)*(R1(12)*(V3(6)-V3(3))
     $ -R1(11)*(V3(4)+CI*(V3(5))))+P3(3)*(R1(15)*-1D0*(V3(4)+CI
     $ *(V3(5)))+R1(16)*(V3(6)-V3(3)))))))
      VERTEX = COUP*(TMP33+TMP36-CI*(TMP35)+CI*(TMP32)-TMP34-TMP37)
      END


