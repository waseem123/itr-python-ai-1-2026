# class Vehicle:
#     def run(self):
#         print('Vehicle runs')
        
class Car:
    def run(self):
        print('Car runs on Road')
        
class Train:
    def run(self):
        print('Train runs on the Railway Track')
        
class AeroPlane:
    def run(self):
        print('Aeroplane runs on the Runway and flies in the Air')
        
        
c = Car()
t = Train()
a = AeroPlane()

vehicles = [c,t,a]

for i in vehicles:
    i.run()