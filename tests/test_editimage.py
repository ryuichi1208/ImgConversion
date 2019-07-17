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