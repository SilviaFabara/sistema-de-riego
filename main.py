def EncenderRiego():
    if Humedad > 350:
        basic.show_leds("""
            . # # # .
                        # # # # #
                        . . # . .
                        # . # . .
                        . # # . .
        """)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(3000)
        pins.servo_write_pin(AnalogPin.P2, 90)
        basic.pause(3000)
        pins.analog_write_pin(AnalogPin.P0, 0)
    basic.pause(5000)
def MedidaSensor():
    global Humedad
    Humedad = pins.analog_read_pin(AnalogPin.P1)
    serial.write_value("\"HumedadSuelo\"", Humedad)

def on_button_pressed_a():
    basic.show_number(Humedad)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
                # # # # #
                . . # . .
                # . # . .
                . # # . .
    """)
    pins.servo_write_pin(AnalogPin.P2, 0)
    basic.pause(3000)
    pins.servo_write_pin(AnalogPin.P2, 90)
    basic.pause(3000)
    pins.analog_write_pin(AnalogPin.P2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

Humedad = 0
Humedad = 350

def on_forever():
    MedidaSensor()
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    EncenderRiego()
basic.forever(on_forever)
