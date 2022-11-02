import pytest

a=101

@pytest.mark.smoke
#@pytest.mark.skipif(a>100,reason="we are skipping")
def test_testcasethree():
    print('smoke tc')
    assert a != 101  


@pytest.mark.sanity
#@pytest.mark.skip("we are skipping")
def test_testcasethree1():
    print('sanity tc')
    
    

