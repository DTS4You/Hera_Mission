# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True
    inc_i2c             = True


class Global_WS2812:

    numpix_1            = 30            # Anz. LEDs im 1. Stripe -> Einschlagbahn
    numpix_2            = 256           # Anz. LEDs im 2. Stripe -> Umlaufbahn alt innen
    numpix_3            = 256           # Anz. LEDs im 3. Stripe -> Umlaufbahn alt aussen
    numpix_4            = 256           # Anz. LEDs im 4. Stripe -> Umlaufbahn neu innen
    numpix_5            = 256           # Anz. LEDs im 5. Stripe -> Umlaufbahn neu aussen
    numpix_6            = 8             # Anz. LEDs im 4. Stripe -> Splitter-Strahl

    seg_01_strip        = 0             #  1. Seg -> Stripe      # Einschlagbahn
    seg_01_start        = 0             #  1. Seg -> Start
    seg_01_count        = 30            #  1. Seg -> Anzahl

    seg_02_strip        = 1             #  2. Seg -> Stripe      # Umlaufbahn alt innen
    seg_02_start        = 0             #  2. Seg -> Start
    seg_02_count        = 256           #  2. Seg -> Anzahl

    seg_03_strip        = 2             #  3. Seg -> Stripe      # Umlaufbahn alt aussen
    seg_03_start        = 0             #  3. Seg -> Start
    seg_03_count        = 256           #  3. Seg -> Anzahl
    
    seg_04_strip        = 3             #  4. Seg -> Stripe      # Umlaufbahn neu innen
    seg_04_start        = 0             #  4. Seg -> Start
    seg_04_count        = 256           #  4. Seg -> Anzahl

    seg_05_strip        = 4             #  5. Seg -> Stripe      # Umlaufbahn neu aussen
    seg_05_start        = 0             #  5. Seg -> Start
    seg_05_count        = 256           #  5. Seg -> Anzahl
    
    seg_06_strip        = 5             #  6. Seg -> Stripe      # Splitter-Strahl
    seg_06_start        = 0             #  6. Seg -> Start
    seg_06_count        = 8             #  6. Seg -> Anzahl
    

# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  5)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 30, 30, 30)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
