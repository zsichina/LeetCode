from typing import Callable
from threading import Lock


class TrafficLight:
    def __init__(self):
        self.sn_green = Lock()
        self.ew_green = Lock()
        self.dir = 1
        self.ew_green.acquire()

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        
        if self.dir == 1 and roadId == 2:
            self.ew_green.release()
            self.sn_green.acquire()
            turnGreen()
        elif self.dir == 2 and roadId == 1:
            self.ew_green.acquire()
            self.sn_green.release()
            turnGreen()

        crossCar()
        self.dir = roadId
