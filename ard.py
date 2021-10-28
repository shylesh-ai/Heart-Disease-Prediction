import serial
import time
def heart_control():
    try:
        ser=serial.Serial('com8',9600)
        time.sleep(2)
        while True:
            try:
                ser_bytes=ser.readline()
                decoded_bytes=ser_bytes.decode("utf-8")
                print(decoded_bytes)
            except:
                print("Keyboard Interrupt")
                break
    except serial.SerialException:
        return "There's no arduino board"

heart_control()
