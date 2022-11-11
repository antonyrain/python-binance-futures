# python-binance-futures
Demo: https://youtu.be/GwwDXQXv2aY

How to run the program:

-- Unzip or copy files to specific folder.

-- To start the program, we have to open the command line.

-- To change directory use the command ‘cd’ like this ‘cd /home/user/python_projects’’ and navigate to your project folder.

-- To create a virtual environment use the commands:

py -m venv env

Tutorial: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

-- To activate a virtual environment use the command:

.\env\Scripts\activate

-- You’re in your virtual environment and you can install packages:

py -m pip install -r requirements.txt

!!! Probably you will get an ERROR: Failed building wheel for twisted-iocpsupport.

??? If this error appears, download and install Twisted (an event-driven networking engine): twisted_iocpsupport‑1.0.2‑[python version and your windows system] from page:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

-- Copy file to the program folder and use the command:

pip install twisted_iocpsupport‑1.0.2‑[python version and your windows system]

-- Try to install all dependencies again:

py -m pip install -r requirements.txt

-- Go to the Binance Account and open the API management page.

-- Create the API Keys and insert them to the file credentials.py of the program.

-- To run the program use the command:

py main.py
