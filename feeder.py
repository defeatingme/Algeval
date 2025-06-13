import serial
import serial.tools.list_ports
import time

class Feeder(object):
    def __init__(self):
        super().__init__()
        self.arduino = None
        self.feeding = False

        self.initialize()

    def initialize(self):
        ports = serial.tools.list_ports.comports()

        port1 = None  # Initialize it first

        for port in ports:
            print(port)
            if "USB-SERIAL CH340" in port.description:
                port1 = str(port.device)
                break

        if port1 is None:
            print("Arduino not found.")
            return

        print(f"Connecting to Arduino on {port1}")
        self.arduino = serial.Serial(port=port1, baudrate=9600, timeout=1)
        time.sleep(2)


    def send_command(self, cmd):
        if cmd == 'mode1' or cmd =='mode2':
            self.feeding = True
        else:
            self.feeding = False
        
        if self.arduino is None:
            print("Feeder not connected")
            return
            
        self.arduino.write((cmd + "\n").encode())
        time.sleep(0.5)
        while self.arduino.in_waiting:
            print("Feeder:", self.arduino.readline().decode().strip())
    
    
    def close(self):
        #Close port connection
        if self.arduino is None:
            print("No serial connection to close.")
            return

        try:
            if self.arduino.is_open:
                self.arduino.close()
                print("Serial connection closed.")
            else:
                print("Serial port was already closed.")
        except Exception as e:
            print(f"Error while closing serial port: {e}")
        finally:
            self.arduino = None
