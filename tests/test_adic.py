import pytest
import adic
def test_non_prime(n):
    with pytest.raises(TypeError):
        adic.adic.p_adic(n)
