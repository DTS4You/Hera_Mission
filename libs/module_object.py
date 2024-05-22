####################################################################
### Objects                                                      ###
####################################################################

class LED_OBJ:

    def __init__(self, num_pix = 0):
        
        self.num_pix = num_pix      # Number of LED Pixel
        self.pos = 0                # Position
        self.dir = False            # False = Left | True = Right
        self.anim = False           # Animation State
    
    def get_num_pix(self):
        return self.num_pix



# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("Object -> Setup")
    led_obj = LED_OBJ(20)
    print("Decode -> Test")
    print(led_obj.get_num_pix())
    print("-----------------------------------")


# ==============================================================================

# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":
    main()

    # Normal sollte das Programm hier nie ankommen !
    print("End of Programm !!!")

# ##############################################################################
