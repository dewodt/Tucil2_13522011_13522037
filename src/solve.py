import time
from math import comb

from input import Input
from point import Point


class Solve:
    duration: int  # Calculation duration
    solution: list[Point]  # Array of result points

    def __init__(self):
        self.duration = 0
        self.solution = []

    def solve_brute_force(self, input: Input):
        # Start time
        timeStart = time.time()

        # Initialize
        order = input.get_order()
        steps = input.get_steps()
        control_points = input.get_control_points()
        solution: list[Point] = []

        # Iterate 0 <= t <= 1 in steps
        for t in [i / steps for i in range(steps)]:
            # Use formula to calculate brute force
            x, y = 0, 0

            # Calculate B(t) = sum from 0 to n nCi * (1-t)^(n-i) * t^i * P_i
            for i in range(order):
                coefficient = comb(order, i) * ((1 - t) ** (order - i)) * (t**i)
                x += coefficient * control_points[i].x
                y += coefficient * control_points[i].y

            # Create new point
            bt = Point(x, y)

            # Append to solution
            solution.append(bt)

        # End time
        timeEnd = time.time()

        # Set the solution
        self.duration = timeEnd - timeStart
        self.solution = solution

    def get_duration(self) -> int:
        return self.duration

    def get_solution(self) -> list[Point]:
        return self.solution

    def print_solution(self):
        # Print duration
        print("Calculation duration:", self.duration, "seconds")

        # Print points
        print("Result:")
        for i in range(len(self.solution)):
            t = i / len(self.solution)
            print(f"B({t}) = ({self.solution[i].x}, {self.solution[i].y})")
