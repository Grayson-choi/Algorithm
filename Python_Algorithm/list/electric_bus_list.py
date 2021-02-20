"""
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
"""

import math

T = int(input())

for test_case in range(1, T + 1):
    max_range, station_num, battery_station_num = list(map(int, input().split()))
    # print(max_range, station_num, battery_station_num)
    battery_stations = list(map(int, input().split()))
    # print(battery_stations)
    battery_stations_list = []
    for i in range(station_num):
        if i in battery_stations:
            battery_stations_list.append(1)
        else:
            battery_stations_list.append(0)
    # print(battery_stations_list)
    stations = list(range(station_num))
    charge_count = 0

    curr = 0
    battery = max_range
    index = 0
    close_battery_station = battery_stations[0]
    positive = True
    # 못 가는 경우 찾기
    for i in range(1, battery_station_num):
        if battery_stations[i] - battery_stations[i - 1] > max_range:
            positive = False

    if not positive:
        print("#{} {}".format(test_case, charge_count))
        continue

    while curr + battery < station_num:

        if curr + battery in battery_stations: # 최대 거리를 이동할 수 있다면 이동하고 충전
            close_battery_station = curr + battery
            battery_stations = battery_stations[battery_stations.index(close_battery_station):]
            curr = close_battery_station
            battery = max_range
            charge_count += 1
        elif battery == 0:
            curr = close_battery_station
            battery = max_range
            charge_count += 1
            battery_stations = list(filter(lambda item: item >= curr, battery_stations))
            close_battery_station = battery_stations[0]
        elif curr > close_battery_station:
            battery_stations = list(filter(lambda item: item >= curr, battery_stations))
            close_battery_station = battery_stations[0]

        curr += 1
        battery -= 1

    print("#{} {}".format(test_case, charge_count))













