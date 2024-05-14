# YD-RP2040 Board
# User Button (GPIO24)
# User LED    (GPIO25)

from machine import Pin, Timer # type: ignore
 
led = Pin(25, Pin.OUT)
Counter = 0
Fun_Num = 0
 
def fun(tim):
    global Counter
    Counter = Counter + 1
    print(Counter)
    led.value(Counter%2)
 

def main():

    tim = Timer(-1)
    tim.init(period=1000, mode=Timer.PERIODIC, callback=fun)

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":
    
    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
