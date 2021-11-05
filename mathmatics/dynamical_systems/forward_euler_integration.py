import numpy as np
import matplotlib.pyplot as plt


def integrate_exponential(a, x0, dt, T):
    """Compute solution of the differential equation dx/dt=a*x with
    initial condition x0 for a duration T. Use time step dt for numerical
    solution.

    Args:
    a (scalar): parameter of dx/dt (dx/dt=a*x)
    x0 (scalar): initial condition (x at time 0)
    dt (scalar): timestep of the simulation
    T (scalar): total duration of the simulation

    ! xdot = dx/dt

    Returns:
    ndarray, ndarray: `x` for all simulation steps and the time `t` at each step
    """
    # Initialize variables
    t = np.arange(0, T, dt)
    x = np.zeros_like(t, dtype=complex)
    x[0] = x0
    for k in range(1, len(t)):
        xdot = a * x[k - 1]
        x[k] = x[k - 1] + xdot * dt
    return x, t
def main():
    figure, plots = plt.subplots(2,2)

    # Choose parameters
    a = -0.5  # parameter in f(x)
    T = 10  # total Time duration
    dt = 0.001  # timestep of our simulation
    x0 = 1.  # initial condition of x at time 0

    # Use Euler's method
    x, t = integrate_exponential(a, x0, dt, T)

    # Visualize
    plots[0, 0].plot(t, x.real)
    plots[0, 0].set_title("a < 0, dt = 0.001")

    a = 0.5
    x, t = integrate_exponential(a, x0, dt, T)
    plots[1, 0].plot(t, x.real)
    plots[1, 0].set_title("a > 0, dt = 0.001")

    a = 0
    x, t = integrate_exponential(a, x0, dt, T)
    plots[0, 1].plot(t, x.real)
    plots[0, 1].set_title("a = 0, dt = 0.001")

    dt = 0.1
    a = 0.1
    x, t = integrate_exponential(a, x0, dt, T)
    plots[1, 1].plot(t, x.real)
    plots[1, 1].set_title("a > 0, dt = 0.1")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
