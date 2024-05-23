####################################################################
### Objects                                                      ###
####################################################################

class LED_OBJ:

    def __init__(self, num_pix = 0, dir = False):
        
        self.num_pix = num_pix      # Number of LED Pixel
        self.pos = 0                # Position
        self.dir = dir              # False = Left | True = Right
        self.anim = False           # Animation State
        self.color_off = 0          # Color-Table "OFF"
        self.color_on = 0           # Color-Table "ON"
        self.color_anim = 0         # Color-Table "ANIM"
    
    def get_num_pix(self):
        return self.num_pix
    
    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos
    
    def anim_step(self):
        if self.dir == True:
            print("Step Right")
        else:
            print("Step Left")


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("Object -> Setup")
    led_obj = LED_OBJ(50)
    print("Decode -> Test")
    print("Get -> num_pix = ", led_obj.get_num_pix())
    led_obj.set_pos(20)
    print("Get -> pos = ", led_obj.get_pos())
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
