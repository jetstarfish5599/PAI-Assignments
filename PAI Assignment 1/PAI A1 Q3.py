#Q3 LahoreLogistics SIM

#package info
class Package:
    def __init__(self, packageId, weightinKg):
        self.packageId = packageId
        self.weightinKg = weightinKg


#drone info
class Drone:
    def __init__(self, droneId, maxLoadinKg):
        self.droneId = droneId
        self.maxLoadinKg = maxLoadinKg
        self._status = 'idle'       #private attr
        self.currentPackage = None

    #get status from drone class
    def getstatus(self):
        return self._status

    #set status only if valid
    def setstatus(self, newStatus):
        if newStatus in ['idle', 'delivering', 'charging']:
            self._status = newStatus
        else:
            print(f"invalid status '{newStatus}' for drone {self.droneId}")

    #assign package only if idle, within load
    def assignpackage(self, packageObj):
        if self._status == 'idle' and packageObj.weightinKg <= self.maxLoadinKg:
            self.currentPackage = packageObj
            self._status = 'delivering'
            print(f"drone {self.droneId} delivering package {packageObj.packageId}")
        else:
            print(f"drone {self.droneId} cannot take package {packageObj.packageId}")


#fleet manager
class FleetManager:
    def __init__(self):
        self.drones = []
        self.pendingPackages = []

    #add drone
    def adddrone(self, drone):
        self.drones.append(drone)

    #add package
    def addpackage(self, package):
        self.pendingPackages.append(package)

    #assign jobs to idle drones
    def dispatchjobs(self):
        for drone in self.drones:
            if drone.getstatus() == 'idle' and self.pendingPackages:
                pkg = self.pendingPackages.pop(0)
                drone.assignpackage(pkg)

    #update states after one tick
    def simulationtick(self):
        for drone in self.drones:
            if drone.getstatus() == 'delivering':
                drone.setstatus('charging')
                print(f"drone {drone.droneId} is now charging")
            elif drone.getstatus() == 'charging':
                drone.setstatus('idle')
                print(f"drone {drone.droneId} is idle")


#main
manager = FleetManager()
#add drones
d1 = Drone('D1', 5)
d2 = Drone('D2', 10)
manager.adddrone(d1)
manager.adddrone(d2)
#add packages
p1 = Package('P1', 4)
p2 = Package('P2', 8)
p3 = Package('P3', 12)
manager.addpackage(p1)
manager.addpackage(p2)
manager.addpackage(p3)

#run sim
print("\ndispatching jobs")
manager.dispatchjobs()

print("\nsimulation tick 1")
manager.simulationtick()

print("\nsimulation tick 2")
manager.simulationtick()
