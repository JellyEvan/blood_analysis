import pytest
import chol_analysis


def test_HDL_analysis():
    """Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    input = 100
    answer = HDL_analysis(input)
    expected = 'Normal'
    assert answer == expected








'''
@pytest.mark.parametrize("input, ouput", [
    (100, 'Normal'),
    (50, 'Borderline low'),
    (20, 'Low'),
])
def test_HDL_analysis2(input, ouput):
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(input)
    expected = ouput
    assert answer == expected


@pytest.mark.parametrize("input, output, expected", [
    (100, 'Normal', True),
    (50, 'Borderline low', True),
    (20, 'Low', True),
])
def test_HDL_analysis3(input, output, expected):
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer == expected
    """
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(input) == output
    assert answer == expected
'''
