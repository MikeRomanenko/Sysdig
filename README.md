# Sysdig

Run test
======
Before running make sure `chromedriver` (or a browser of your choice) is in your PATH or you can specify it in `driver` variable.
You can run it from an IDE of your choice or via terminal:
    
    # Navigate to the project location
    # Make sure your virtual environment is activated
    # run pytest command
    $ pytest

The test can be enhanced with some features such as WebDriver Wait or can be split into multiple tests related 
to each feature/test case or functionality depending on your framework.

Possible defects:
1) Login page doesn't contain 'login' in the title page.
2) Login page a bit 'slow'. Requires some performance testing for a better user experience.
