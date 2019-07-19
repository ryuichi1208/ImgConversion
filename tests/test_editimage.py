import pytest
import sys
sys.path.append('.')
from editimage import *

@pytest.mark.parametrize(
    "_int, _str", [
        (100, "100"),
        (100.0, "100.0"),
        (1024.2224, "1024.2"),
        (-200, "-200"),
        (-30.55, "-30.6"),
    ]
)
def test_roundstr(_int, _str):
    assert roundstr(_int) == _str

@pytest.mark.parametrize(
    "_in, _out", [
        (-100.01, "-100.01 B"),
        (-1, "-1 B"),
        (0, "0 B"),
        (1023, "1023 B"),
        (1024, "1.0 KB"),
        (1048575, "1024.0 KB"),
        (1048576, "1.0 MB"),
        (1073741823, "1024.0 MB"),
        (1073741824, "1.0 GB"),
        (1099511627775, "1024.0 GB"),
        (1099511627776, "1.0 TB")
    ]
)
def test_filesize(_in, _out):
    assert filesize(_in) == _out

@pytest.mark.parametrize(
    "_src_ext, _dst_ext, result", [
        ("jpg", "jpg", 0),
        ("png", "png", 0),
        ("jpg", "png", 1),
        ("png", "jpg", 1)
    ]
)
def test_compare_ext(_src_ext, _dst_ext, result):
    assert compare_ext(_src_ext, _dst_ext) == result

