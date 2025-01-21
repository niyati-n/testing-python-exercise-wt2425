"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w, h, dx, dy = 15.0, 20.0, 0.2, 0.5
        calculated_nx, calculated_ny = int(w / dx), int(h / dy)

        self.solver.initialize_domain(w, h, dx, dy)

        self.assertEqual(self.solver.nx, calculated_nx, f"Expected nx = {calculated_nx}, but got {self.solver.nx}")
        self.assertEqual(self.solver.ny, calculated_ny, f"Expected ny = {calculated_ny}, but got {self.solver.ny}")




    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        d, dx, dy = 5.0, 0.1, 0.2

        # Computing a stable time step
        dx2, dy2 = dx * dx, dy * dy
        dt_calculated = dx2 * dy2 / (2 * d * (dx2 + dy2))

        # Manually set dx,dy values
        self.solver.dx = dx
        self.solver.dy = dy

        self.solver.initialize_physical_parameters(d)
        #Assertion
        self.assertAlmostEqual(self.solver.dt, dt_calculated, delta=1e-9, msg=f"Expected dt = {dt_calculated}, but got {self.solver.dt}")



    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        dx, dy, nx, ny = 2.0, 3.0, 15, 20
        T_hot, T_cold = 700, 300

        self.solver.nx = nx
        self.solver.ny = ny
        self.solver.dx = dx
        self.solver.dy = dy
        self.solver.T_hot = T_hot
        self.solver.T_cold = T_cold

        calculate_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r2:
                    calculate_u[i, j] = T_hot
        
        u = self.solver.set_initial_condition()
        np.testing.assert_array_equal(u, calculate_u, err_msg="The condition specified initially is not correct.")

