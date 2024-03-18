import time
from input import Input
from solve import Solve
from draw import Draw


# Main Program
def main():
    # Create input
    input = Input()

    # Create GUI window
    draw = Draw(input.all_positive)

    if input.is_brute_force():
        for i in range(len(input.control_points)):
            input.control_points[i].scale(input.scale)

        # Start time
        timeStart = time.time()

        # Solve the curve
        result = Solve()

        # Print solution
        result.print_solution(input.scale)

        # Draw in GUI
        Draw.drawControlPoints(input.control_points)
        result.solve_brute_force_optimized(input)
        Draw.drawBruteForceCurve(result.solution)
        Draw.t.hideturtle()

        # End time
        timeEnd = time.time()
        duration = timeEnd - timeStart
        print("Calculation duration:", duration, "seconds")

    else:
        for i in range(len(input.control_points)):
            input.control_points[i].scale(input.scale)

        # Start time
        timeStart = time.time()

        # Solve the curve
        result = Solve()

        # Draw in GUI
        Draw.drawControlPoints(input.control_points)
        result.solve_dnc(input)
        Draw.drawDNCCurve(result.solution)
        Draw.t.hideturtle()

        # Print the Solution
        result.print_solution(input.scale)

        # End time
        timeEnd = time.time()
        duration = timeEnd - timeStart
        print("Calculation duration:", duration, "seconds")

    draw.t.screen.mainloop()

# Run main program
main()