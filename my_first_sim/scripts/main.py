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
        laser_window = 1.5
        critical_distance = 0.5

        while True:
            range_list = my_bot.get_rangelist()

            left_sensors, middle_sensors, right_sensors = get_sensors_data(range_list)

            # values could be maximum 1.5
            ld_avg = get_avg(left_sensors)
            rd_avg = get_avg(right_sensors)
            md_avg = get_avg(middle_sensors)

            objects_near_to_bot = [x < allowed_distance for x in [ld_avg, md_avg, rd_avg]]

            total_left = left_sensors[0]
            middle = middle_sensors[1]
            total_right = right_sensors[len(right_sensors)-1]

            #print(ld_avg, md_avg, rd_avg)

            general_value = (0 - (ld_avg - rd_avg))

            if ld_avg <= laser_window or md_avg <= laser_window or rd_avg <= laser_window:
                my_bot.slow_down().wait()

            if md_avg < allowed_distance:

                # there is a trap, try to find a way out
                if total_left < critical_distance and total_right < critical_distance and middle < critical_distance:
                    my_bot.last_n_steps = -4
                    my_bot.turn_sharp().wait()

                print('something in my sight, turning somewhere')
                w = general_value * 6
                my_bot.last_n_steps = w
                turning_value = (0.1, w)
            else:
                print('correcting my way')
                my_bot.last_n_steps = general_value
                turning_value = (0.5, general_value)

            ls = my_bot.last_n_steps
            tmp = None
            i = 0
            for item in ls:
                if tmp != item:
                    tmp = item
                    i = 0
                else:
                    i += 1

            if i > 5:
                print('speeding up')
                my_bot.last_n_steps = turning_value[1]
                turning_value = (1.5, turning_value[1])

            print(ls)

            my_bot.move(*turning_value)

            simu.sleep(0.2)
