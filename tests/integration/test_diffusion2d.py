"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    solver.initialize_domain(w=15.0, h=15.0, dx=0.5, dy=0.5)

    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

    assert solver.D == 4.0, f"Expected D should be 4.0, but got {solver.D}"

    dx2, dy2 = solver.dx ** 2, solver.dy ** 2
    calculated_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))

    assert solver.dt == calculated_dt, f"Expected dt is {calculated_dt}, got {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    
    solver.initialize_domain(w=10.0, h=10.0, dx=0.5, dy=0.5)

    
    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

    
    u = solver.set_initial_condition()

    nx, ny = solver.nx, solver.ny
    T_cold, T_hot = solver.T_cold, solver.T_hot
    r, cx, cy = 2.0, 5.0, 5.0

    expected_u = T_cold * np.ones((nx, ny))


    for i in range(nx):
        for j in range(ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r ** 2:
                expected_u[i, j] = T_hot

    np.testing.assert_array_equal(u, expected_u, err_msg="Initial condition array does not match")

