# test_script.py
import shivakher as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is()) > 1

# Run the test
if __name__ == "__main__":
    test_hi_my_name_is()
    print("All tests passed!")

