Selenium setup
==============

1. Install pip and selenium

        sudo apt-get install python-pip

2. Install selenium python bindings

        sudo pip install selenium

3. Test it

    Create a file named test.py

        #!/usr/bin/env python

        from selenium import webdriver

        driver = webdriver.Firefox()
        driver.get('http://www.ubuntu.com/')
        print driver.title
        driver.quit()

    and run it

        python test.py


For more info, see: http://python.dzone.com/articles/python-getting-started
