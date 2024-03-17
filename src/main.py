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
        result = Solve()
        Draw.drawControlPoints(input.control_points)
        result.solve_brute_force_optimized(input)
        Draw.drawBruteForceCurve(result.solution)
        Draw.t.hideturtle()
        result.print_solution()

    else:
        for i in range(len(input.control_points)):
            input.control_points[i].scale(input.scale)
        # print(input.scale)
        result = Solve()
        Draw.drawControlPoints(input.control_points)
        result.solve_dnc(input)
        Draw.drawDNCCurve(result.solution)
        Draw.t.hideturtle()
        result.print_solution()

    draw.t.screen.mainloop()

# Run main program
main()
