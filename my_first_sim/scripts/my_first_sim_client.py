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

from scripts.mybot import MyBot


def get_sensors_data(range_list):
    middle_sensor_idx = int(len(range_list) / 2)

    middle_sensors = range_list[middle_sensor_idx - 1: middle_sensor_idx + 2]
    left_sensors = range_list[1:middle_sensor_idx - 1]
    right_sensors = range_list[middle_sensor_idx + 2:len(range_list) - 1]

    return left_sensors, middle_sensors, right_sensors


if __name__ == '__main__':

    with Morse() as simu:

        my_bot = MyBot(simu)
        allowed_distance = 1
        critical_distance = 0.6

        # my_bot.turn_right().wait().go_foward()

        while True:
            range_list = my_bot.get_rangelist()

            left_sensors, middle_sensors, right_sensors = get_sensors_data(range_list)

            ld_avg = sum(left_sensors) / len(left_sensors)
            rd_avg = sum(right_sensors) / len(right_sensors)
            md_avg = sum(middle_sensors) / len(middle_sensors)

            are_objects_on_left = ld_avg < 2
            are_objects_on_right = rd_avg < 2
            are_objects_on_mid = md_avg < 2

            # something is near to me, slow down
            if all([are_objects_on_left, are_objects_on_mid, are_objects_on_right]):
                my_bot.slow_down()

            l, m, r = middle_sensors

            if critical_distance < ld_avg < allowed_distance:
                my_bot.turn_right()
            elif critical_distance < rd_avg < allowed_distance:
                my_bot.turn_left()
            elif md_avg < critical_distance and ld_avg < critical_distance and rd_avg < critical_distance:
                my_bot.stop().turn_sharp()
            else:
                my_bot.go_forward()

            simu.sleep(0.2)