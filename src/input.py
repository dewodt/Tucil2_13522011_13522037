from point import Point


class Input:
    type: int  # 1 for brute force, 2 for divide and conquer
    order: int  # Order of Bezier Curve
    control_points: list[Point]  # Array of control points
    steps: int  # Steps for brute force / DNC

    def __init__(self):
        # Type of algorithm
        print("Choose algorithm:")
        print("1. Brute Force")
        print("2. Divide and Conquer")
        type = int(input("Enter number of algorithm: "))
        # Validation: Type must be 1 or 2
        while type != 1 and type != 2:
            print("Type of algorithm must be 1 or 2")
            type = int(input("Enter number of algorithm: "))

        # Order of bezier curve
        order = int(input("Enter order of Bezier Curve (n): "))
        # Validation: Minimal order = 2
        while order < 1:
            print(
                "Order of Bezier Curve must be greater than or equal than 2 (Linear Bezier Curve)"
            )
            order = int(input("Enter order of Bezier Curve (n): "))

        # Array of control points
        control_points: list[Point] = []
        for i in range(order + 1):
            print("Input coordinate (x, y) of control point P_", i)
            x, y = list(map(int, input().split()))
            point = Point(x, y)
            control_points.append(point)

        # Steps
        steps = int(input("Enter number of steps/iteration for brute force / DNC: "))
        # Validation: Minimal steps = 1
        while steps < 1:
            print("Number of steps/iteration must be greater than 0")
            steps = int(
                input("Enter number of steps/iteration for brute force / DNC: ")
            )

        # Set the input data
        self.type = type
        self.order = order
        self.control_points = control_points
        self.steps = steps

    def get_type(self) -> int:
        return self.type

    def get_order(self) -> int:
        return self.order

    def get_control_points(self) -> list[Point]:
        return self.control_points

    def get_steps(self) -> int:
        return self.steps

    def is_brute_force(self) -> bool:
        return self.type == 1
