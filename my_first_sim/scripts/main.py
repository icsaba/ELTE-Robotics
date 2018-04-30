#! /usr/bin/env python3
"""
Test client for the <my_first_sim> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

from pprint import pprint
from pymorse import Morse

import sys, os

package_path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, package_path + '/../')

pprint(sys.path)

from scripts.mybot import MyBot


def get_sensors_data(range_list):
    middle_sensor_idx = int(len(range_list) / 2)

    middle_sensors = range_list[middle_sensor_idx - 1: middle_sensor_idx + 2]
    left_sensors = range_list[1:middle_sensor_idx - 1]
    right_sensors = range_list[middle_sensor_idx + 2:len(range_list) - 1]

    return left_sensors, middle_sensors, right_sensors


def get_avg(data):
    return sum(data) / len(data)


if __name__ == '__main__':

    with Morse() as simu:

        my_bot = MyBot(simu)
        allowed_distance = 1
        critical_distance = 0.6

        # my_bot.turn_right().wait().go_foward()

        while True:
            range_list = my_bot.get_rangelist()

            left_sensors, middle_sensors, right_sensors = get_sensors_data(range_list)

            ld_avg = get_avg(left_sensors)
            rd_avg = get_avg(right_sensors)
            md_avg = get_avg(middle_sensors)

            objects_near_to_bot = [x < allowed_distance for x in [ld_avg, md_avg, rd_avg]]

            l, m, r = middle_sensors

            # something is near to me, slow down
            # if all(objects_near_to_bot):
            #    my_bot.slow_down()

            turning_value = (0 - (ld_avg - rd_avg)) * 2

            if turning_value:
                my_bot.turning( turning_value)

            if md_avg > critical_distance:
                my_bot.go_forward()
            else:
                my_bot.stop().turn_sharp().wait()

            simu.sleep(0.2)
