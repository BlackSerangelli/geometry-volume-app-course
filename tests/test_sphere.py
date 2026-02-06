import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid sphere radius.
    """
    radius = 2.0
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == expected

def test_volume_sphere_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    The sphere module raises ValueError for negative radius.
    """
    radius = -2.0
    with pytest.raises(ValueError, match="Radius must be non-negative"):
        volume_sphere(radius)

def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 1.1
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
