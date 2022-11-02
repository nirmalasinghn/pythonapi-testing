import pytest

a=101

@pytest.mark.smoke
#@pytest.mark.skipif(a>100,reason="we are skipping")
def test_testcasefour():
    print('smoke tc')
    


@pytest.mark.sanity
#@pytest.mark.skip("we are skipping")
def test_testcasefour1():
    print('sanity tc')
    
    

