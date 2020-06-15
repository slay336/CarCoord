# -*- coding: utf-8 -*-


class CoordException(Exception):
    pass


class VehicleCoord:
    name: str = "Vehicle"
    axis_x = 0.0
    axis_z = 0.0

    def __init__(self, x, z):
        self.axis_x = x
        self.axis_z = z

    def __setattr__(self, key, value):
        if key in ("axis_x", "axis_z") and (value < 0 or value > 15360):
            raise CoordException("Todo esta malo")
        else:
            self.__dict__[key] = value

    def __str__(self):
        return f"{self.name}: x={self.axis_x}, z={self.axis_z}"


class Rover(VehicleCoord):
    name = "Rover"


class BMW(VehicleCoord):
    pass


class BMWWhite(BMW):
    name = "BMWWhite"


class BMWRed(BMW):
    name = "BMWRed"


class BMWBlack(BMW):
    name = "BMWBlack"


class BMWBlue(BMW):
    name = "BMWBlue"


event_mapping = {"VehicleLandRoverDefender": Rover,
                 "VehicleCrSk_BMW_525i_E34": BMWWhite,
                 "VehicleCrSk_BMW_525i_E34_Red": BMWRed,
                 "VehicleCrSk_BMW_525i_E34_Black": BMWBlack,
                 "VehicleCrSk_BMW_525i_E34_Beater": BMWBlue}