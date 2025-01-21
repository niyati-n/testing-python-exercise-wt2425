# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
======================================================================== test session starts =========================================================================
platform darwin -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425
collected 3 items                                                                                                                                                    

tests/unit/test_diffusion2d_functions_copy.py F..                                                                                                              [100%]

============================================================================== FAILURES ==============================================================================
_______________________________________________________________________ test_initialize_domain _______________________________________________________________________

    def test_initialize_domain():
            """
            Check function SolveDiffusion2D.initialize_domain
            """
            solver = SolveDiffusion2D()
            w, h, dx, dy = 15.0, 20.0, 0.2, 0.5
            calculated_nx, calculated_ny = int(w / dx), int(h / dy)
    
            solver.initialize_domain(w, h, dx, dy)
    
>           assert solver.nx == calculated_nx, f"Returned nx is incorrect: is {solver.nx}, should be {calculated_nx}"
E           AssertionError: Returned nx is incorrect: is 100, should be 75
E           assert 100 == 75
E            +  where 100 = <diffusion2d.SolveDiffusion2D object at 0x1058acbc0>.nx

tests/unit/test_diffusion2d_functions_copy.py:19: AssertionError
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions_copy.py::test_initialize_domain - AssertionError: Returned nx is incorrect: is 100, should be 75
==================================================================== 1 failed, 2 passed in 0.28s =====================================================================

======================================================================== test session starts =========================================================================
platform darwin -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425
collected 3 items                                                                                                                                                    

tests/unit/test_diffusion2d_functions_copy.py .F.                                                                                                              [100%]

============================================================================== FAILURES ==============================================================================
________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________

    def test_initialize_physical_parameters():
            """
            Checks function SolveDiffusion2D.initialize_domain
            """
            solver = SolveDiffusion2D()
            d, dx, dy = 5.0, 0.1, 0.2
    
            # Computing a stable time step
            dx2, dy2 = dx * dx, dy * dy
            dt_calculated = dx2 * dy2 / (2 * d * (dx2 + dy2))
    
            # Manually set dx,dy values
            solver.dx = dx
            solver.dy = dy
    
            solver.initialize_physical_parameters(d)
            #Assertion
>           assert solver.dt == dt_calculated, f"Expected dt = {dt_calculated}, but got {solver.dt}"
E           AssertionError: Expected dt = 0.0008000000000000001, but got 0.0020000000000000005
E           assert 0.0020000000000000005 == 0.0008000000000000001
E            +  where 0.0020000000000000005 = <diffusion2d.SolveDiffusion2D object at 0x1059c3650>.dt

tests/unit/test_diffusion2d_functions_copy.py:42: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------
dt = 0.0020000000000000005
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions_copy.py::test_initialize_physical_parameters - AssertionError: Expected dt = 0.0008000000000000001, but got 0.0020000000000000005
==================================================================== 1 failed, 2 passed in 0.29s =====================================================================

======================================================================== test session starts =========================================================================
platform darwin -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425
collected 3 items                                                                                                                                                    

tests/unit/test_diffusion2d_functions_copy.py ..F                                                                                                              [100%]

============================================================================== FAILURES ==============================================================================
_____________________________________________________________________ test_set_initial_condition _____________________________________________________________________

    def test_set_initial_condition():
            """
            Checks function SolveDiffusion2D.get_initial_function
            """
            solver = SolveDiffusion2D()
            dx, dy, nx, ny = 2.0, 3.0, 15, 20
            T_hot, T_cold = 700, 300
    
            solver.nx = nx
            solver.ny = ny
            solver.dx = dx
            solver.dy = dy
            solver.T_hot = T_hot
            solver.T_cold = T_cold
    
            calculate_u = T_cold * np.ones((nx, ny))
            r, cx, cy = 2, 5, 5
            r2 = r ** 2
            for i in range(nx):
                for j in range(ny):
                    p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                    if p2 < r2:
                        calculate_u[i, j] = T_hot
    
            u = solver.set_initial_condition()
>           np.testing.assert_array_equal(u, calculate_u, err_msg="The condition specified initially is not correct.")

tests/unit/test_diffusion2d_functions_copy.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (array([[700., 700., 700., 700., 700., 700., 700., 700., 700., 700., 700.,
        700., 700., 700., 700., 700., 700.,... 300., 300., 300., 300., 300., 300., 300., 300., 300.,
        300., 300., 300., 300., 300., 300., 300., 300., 300.]]))
kwargs = {'err_msg': 'The condition specified initially is not correct.'}, old_name = 'y', new_name = 'desired'

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        for old_name, new_name in zip(old_names, new_names):
            if old_name in kwargs:
                if dep_version:
                    end_version = dep_version.split('.')
                    end_version[1] = str(int(end_version[1]) + 2)
                    end_version = '.'.join(end_version)
                    msg = (f"Use of keyword argument `{old_name}` is "
                           f"deprecated and replaced by `{new_name}`. "
                           f"Support for `{old_name}` will be removed "
                           f"in NumPy {end_version}.")
                    warnings.warn(msg, DeprecationWarning, stacklevel=2)
                if new_name in kwargs:
                    msg = (f"{fun.__name__}() got multiple values for "
                           f"argument now known as `{new_name}`")
                    raise TypeError(msg)
                kwargs[new_name] = kwargs.pop(old_name)
>       return fun(*args, **kwargs)
E       AssertionError: 
E       Arrays are not equal
E       The condition specified initially is not correct.
E       Mismatched elements: 298 / 300 (99.3%)
E       Max absolute difference among violations: 400.
E       Max relative difference among violations: 1.33333333
E        ACTUAL: array([[700., 700., 700., 700., 700., 700., 700., 700., 700., 700., 700.,
E               700., 700., 700., 700., 700., 700., 700., 700., 700.],
E              [700., 700., 700., 700., 700., 700., 700., 700., 700., 700., 700.,...
E        DESIRED: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
E               300., 300., 300., 300., 300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...

path/to/venv/lib/python3.12/site-packages/numpy/_utils/__init__.py:85: AssertionError
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions_copy.py::test_set_initial_condition - AssertionError: 
==================================================================== 1 failed, 2 passed in 0.31s =====================================================================


### unittest log

python3 -m unittest tests/unit/test_diffusion2d_functions.py
Fdt = 0.0008000000000000001
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 23, in test_initialize_domain
    self.assertEqual(self.solver.nx, calculated_nx, f"Expected nx = {calculated_nx}, but got {self.solver.nx}")
AssertionError: 100 != 75 : Expected nx = 75, but got 100

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=1)

F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 45, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, dt_calculated, delta=1e-9, msg=f"Expected dt = {dt_calculated}, but got {self.solver.dt}")
AssertionError: 0.0005000000000000001 != 0.0008000000000000001 within 1e-09 delta (0.00030000000000000003 difference) : Expected dt = 0.0008000000000000001, but got 0.0005000000000000001

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)

dt = 0.0008000000000000001
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 73, in test_set_initial_condition
    np.testing.assert_array_equal(u, calculate_u, err_msg="The condition specified initially is not correct.")
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/path/to/venv/lib/python3.12/site-packages/numpy/_utils/__init__.py", line 85, in wrapper
    return fun(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/path/to/venv/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1021, in assert_array_equal
    assert_array_compare(operator.__eq__, actual, desired, err_msg=err_msg,
  File "/Users/niyati./Desktop/Winter 24/SSE/python-test/testing-python-exercise-wt2425/path/to/venv/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 885, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Arrays are not equal
The condition specified initially is not correct.
Mismatched elements: 2 / 300 (0.667%)
Max absolute difference among violations: 400.
Max relative difference among violations: 0.57142857
 ACTUAL: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
        300., 300., 300., 300., 300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...
 DESIRED: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
        300., 300., 300., 300., 300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...

----------------------------------------------------------------------
Ran 3 tests in 0.008s

FAILED (failures=1)

### intergrationtest log

tests/integration/test_diffusion2d.py ..                                                                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py F..                                                                                                                   [100%]

============================================================================== FAILURES ==============================================================================
_______________________________________________________________ TestDiffusion2D.test_initialize_domain _______________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w, h, dx, dy = 15.0, 20.0, 0.2, 0.5
        calculated_nx, calculated_ny = int(w / dx), int(h / dy)
    
        self.solver.initialize_domain(w, h, dx, dy)
    
>       self.assertEqual(self.solver.nx, calculated_nx, f"Expected nx = {calculated_nx}, but got {self.solver.nx}")
E       AssertionError: 100 != 75 : Expected nx = 75, but got 100

tests/unit/test_diffusion2d_functions.py:23: AssertionError
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 100 != 75 : Expected nx = 75, but got 100
==================================================================== 1 failed, 4 passed in 0.29s =====================================================================

tests/integration/test_diffusion2d.py ..                                                                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py .F.                                                                                                                   [100%]

============================================================================== FAILURES ==============================================================================
________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters _________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

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
>       self.assertAlmostEqual(self.solver.dt, dt_calculated, delta=1e-9, msg=f"Expected dt = {dt_calculated}, but got {self.solver.dt}")
E       AssertionError: 0.0032000000000000006 != 0.0008000000000000001 within 1e-09 delta (0.0024000000000000002 difference) : Expected dt = 0.0008000000000000001, but got 0.0032000000000000006

tests/unit/test_diffusion2d_functions.py:45: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------
dt = 0.0032000000000000006
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.0032000000000000006 != 0.0008000000000000001 within 1e-09 delta (0.0024000000000000002 difference) : Expected dt = 0.0008000000000000001, but g...
==================================================================== 1 failed, 4 passed in 0.29s =====================================================================

tests/integration/test_diffusion2d.py ..                                                                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py ..F                                                                                                                   [100%]

============================================================================== FAILURES ==============================================================================
_____________________________________________________________ TestDiffusion2D.test_set_initial_condition _____________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

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
>       np.testing.assert_array_equal(u, calculate_u, err_msg="The condition specified initially is not correct.")

tests/unit/test_diffusion2d_functions.py:73: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
        300., 300., 300., 300.],
       [30... 300., 300., 300., 300., 300., 300., 300., 300., 300.,
        300., 300., 300., 300., 300., 300., 300., 300., 300.]]))
kwargs = {'err_msg': 'The condition specified initially is not correct.'}, old_name = 'y', new_name = 'desired'

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        for old_name, new_name in zip(old_names, new_names):
            if old_name in kwargs:
                if dep_version:
                    end_version = dep_version.split('.')
                    end_version[1] = str(int(end_version[1]) + 2)
                    end_version = '.'.join(end_version)
                    msg = (f"Use of keyword argument `{old_name}` is "
                           f"deprecated and replaced by `{new_name}`. "
                           f"Support for `{old_name}` will be removed "
                           f"in NumPy {end_version}.")
                    warnings.warn(msg, DeprecationWarning, stacklevel=2)
                if new_name in kwargs:
                    msg = (f"{fun.__name__}() got multiple values for "
                           f"argument now known as `{new_name}`")
                    raise TypeError(msg)
                kwargs[new_name] = kwargs.pop(old_name)
>       return fun(*args, **kwargs)
E       AssertionError: 
E       Arrays are not equal
E       The condition specified initially is not correct.
E       (shapes (15, 15), (15, 20) mismatch)
E        ACTUAL: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
E               300., 300., 300., 300.],
E              [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...
E        DESIRED: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
E               300., 300., 300., 300., 300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...

path/to/venv/lib/python3.12/site-packages/numpy/_utils/__init__.py:85: AssertionError
====================================================================== short test summary info =======================================================================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: 
==================================================================== 1 failed, 4 passed in 0.30s =====================================================================


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
