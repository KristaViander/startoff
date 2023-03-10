import questions

# Test if conversion to integer works as expected
 

def test_ask_user_integer(monkeypatch): # argumenttina monkeypatch-moduli (venv - pytest)
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful')

# Test an error confition when user adds a unit to a number
def test_askuser_integer2(monkeypatch):
    user_input = '100 v'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_integer(False) == (0, 'Error', 1, "invalid literal for int() with base 10: '100 v'")

def test_askuser_float(monkeypatch):
    user_input = '1.5'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_float(False) == (1.5, 'OK', 0, 'Conversion successful')

def test_askuser_float2(monkeypatch):
    user_input = '1.5v'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_float(False) == (0, 'Error', 1, "could noot convert string to float '1.5v'")

def test_askuser_float3(monkeypatch):
    user_input = '74,6'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_float(False) == (0, 'Error', 1, "could not convert string to float: '74,6'")

def test_askuser_boolean(monkeypatch):
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Haluatko jatkaa')
    assert question.ask_user_boolean('Y', 'N', False) == (True, 'OK', 0, 'Conversion successful')

def test_askuser_boolean2(monkeypatch):
    user_input = 'n'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Haluatko jatkaa')
    assert question.ask_user_boolean('Y', 'N', False) == (False, 'OK', 0, 'Conversion successful')

def test_askuser_boolean3(monkeypatch):
    user_input = 'v'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # Korvataan järjestelmän input() muuttujalla
    question = questions.Question('Haluatko jatkaa')
    assert question.ask_user_boolean('Y', 'N', False) == ('N/A', 'Error', 1, 'unable to convert to boolean')