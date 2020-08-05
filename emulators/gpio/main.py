'''
Created on 6 Aug 2020

@author: IBeRyUS
'''
from gpio_emulator import gpioEmulator

if __name__ == "__main__":        
    # Create the server, binding to localhost on port 9999
    print("This is main")
    gpio = gpioEmulator()
    
    print("Server Closing...")
