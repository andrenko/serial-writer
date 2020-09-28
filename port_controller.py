import os
import serial

SERIAL_PORT = os.environ.get('SERIAL_PORT')


class Serial:
    ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=0)
    print(f'Serial port {ser.name} was opened')

    def read(self, bytes_size=1, readline=False):
        if bytes_size:
            return self.ser.read(bytes_size).decode()
        elif readline:
            return self.ser.readline().decode()

    def write(self, string):
        self.ser.write(string.encode())

    def in_waiting(self):
        return self.ser.in_waiting
