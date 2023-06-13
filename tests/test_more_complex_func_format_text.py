import pytest
from DCI_lesson4_pytesting import more_complex_function as main

badString= "pyLint, a i  .. widely uSed tool that checks for .errors. in Python code and encourages good Python coding patterns, Is integrated into Visual Studio for Python projects. Run PyLint. In Visual Studio, right-click a Python project in Solution Explorer and select Python and then "
goodString= "PyLint, a widely uSed tool that checks for. errors. in Python code and encourages good Python coding patterns, Is integrated into Visual Studio for Python projects. Run PyLint. In Visual Studio, right-click a Python project in Solution Explorer and select Python and then"

# unit test 
# @pytest.mark.skip(reason="Reason for skipping the test")
def test_grammar(testString= goodString):
        # option A
        assert "  " not in testString , "no double space"
        assert ".."not in testString , "no double fullstop"
        assert " ."not in testString , "no space before full stop"
        assert not testString[0].islower() , "capital letter starts sentence"
        assert " i "not in testString , " 'I' is capitalised"


# unit test on imported functions   
def test_format_text(testString= badString):
    assert main.format_text(testString)