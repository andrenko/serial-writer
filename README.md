# Welcome to serial-writer app!

##### Execute the following steps in order to start the app:
- Clone the repo and install requirements
- Configure serial port address in .flaskenv or by executing "export SERIAL_PORT=your_serial_port"
- Start app with "flask run"
 
##### Once app is running, you can start tests:
- Configure environment variable for pytest runner: api_env=localhost_env.ini
- Start tests (tests/tests_read_write) with pytest runner