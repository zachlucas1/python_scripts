from names import given_name, family_name, full_name
import pytest

#this file tests functions and makes sure they output correctly from the names.py file

def test_full_name(): #returns a string that essentially flips the names "last name, first"
    assert full_name("Sally", "Brown") == "Brown; Sally"
    assert full_name("Penelope", "Smith-Jones") == "Smith-Jones; Penelope"
    assert full_name("George", "Washington") == "Washington; George"
    assert full_name("J", "Ng") == "Ng; J" 
    assert full_name("", "") == "; "
    

def test_family_name(): #this just returns the last name
    assert family_name("Brown; Sally") == "Brown"
    assert family_name("Smith-Jones; Penelope") == "Smith-Jones"
    assert family_name("Washington; George") == "Washington"
    assert family_name("Ng; J") == "Ng"
    assert family_name("; ") == ""


def test_given_name(): #this just returns the first name
    assert given_name("Brown; Sally") == "Sally"
    assert given_name("Smith-Jones; Penelope") == "Penelope"
    assert given_name("Washington; George") == "George"
    assert given_name("Ng; J") == "J"
    assert given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "07TeamActivityTestingandFixingFunctions.py"])