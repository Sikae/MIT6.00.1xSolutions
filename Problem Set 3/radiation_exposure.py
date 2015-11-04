__author__ = 'm'

"""
This program finds the amount of radiation a person is exposed to during some period of time.
"""


def f(x):
    import math
    return 10 * math.e ** (math.log(0.5) / 5.27 * x)


def compute_rectangular_area(height, width):
    return height * width


def radiation_exposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    """
    steps = int((stop - start) / step)
    radiation = 0

    for i in range(steps):
        radiation += compute_rectangular_area(f(start + i * step), step)

    return radiation


def print_radiation_exposure(radiation):
    print("The radiation exposure is " + str(radiation))


def main():
    print_radiation_exposure(radiation_exposure(0, 5, 1))
    print_radiation_exposure(radiation_exposure(5, 11, 1))
    print_radiation_exposure(radiation_exposure(0, 11, 1))
    print_radiation_exposure(radiation_exposure(40, 100, 1.5))

if __name__ == "__main__":
    main()
