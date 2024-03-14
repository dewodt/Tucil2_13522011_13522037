from input import Input
from solve import Solve


# Main Program
def main():
    # Create input
    input = Input()

    if input.is_brute_force():
        result = Solve()
        result.solve_brute_force(input)
        result.print_solution()
    else:
        result = Solve()
        result.solve_dnc(input)
        result.print_solution()


# Run main program
main()
