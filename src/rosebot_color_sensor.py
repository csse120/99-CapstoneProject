"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the ColorSensor class, for the robot's downward-facing
sensor that repeated shines right, green and blue light and measures the
intensity of the reflections.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Fall term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_low_level
import time


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    """
    Methods for the downward-facing ColorSensor on the robot, including:
      get_reading    print_detected_color     wait_until_color
    """

    def __init__(self, port):
        """ Constructs the underlying low-level ColorSensor. """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.low_level_color_sensor = rosebot_low_level.ColorSensor()
        self.color_names = self.low_level_color_sensor.COLORS

    def get_reading(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is an integer between
        0 and 7, where the meanings of the integers are:
          - 0: No color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self.low_level_color_sensor.get_color()

    def get_color_name(self):
        """
        Returns the detected color, as a string ('Black', 'Red', etc.)
        :rtype:  str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self.color_names[self.get_reading()]

    def wait_for_color(self, color):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the given color (as an string) to be detected.
        The string can be in any case (lower, upper or mixed), e.g. BLaCk.
          :type color: str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        while True:
            if self.get_color_name().lower() == color.lower():
                break
            time.sleep(0.05)


