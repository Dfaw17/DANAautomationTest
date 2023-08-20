# Mini Tools for automation mobile testing

this tools to help test mobile automation with python

link video : https://www.youtube.com/watch?v=NYPSpJOi0YQ&ab_channel=DaffaFawwazMaulana

## Install all library
*location : root*
```python
pip install -r requirements.txt
```

## Run
*location : root*
```python
pytest -v -n 3                = Run with 3 parallel device
```

## Explanation
*location : root*
```python
helper/actions.py               = file to save action of appium
helper/general_function.py      = file to save reusable function that we can use
helper/shared_step.py           = file to save shared step that we can use at test file
pom/*                           = folder to save our selector component mobile
test/*                          = folder to make test automation
```