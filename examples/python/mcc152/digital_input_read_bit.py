#!/usr/bin/env python
"""
    MCC 152 Methods Demonstrated:
        mcc152.dio_reset
        mcc152.dio_input_read_bit
        mcc152.info

    Purpose:
        Read individual digital inputs until terminated by the user.

    Description:
        This example demonstrates using the digital I/O as inputs and reading
        them individually.
"""
from __future__ import print_function
from sys import version_info
from daqhats_utils import select_hat_device
from daqhats import mcc152, HatIDs, HatError, DIOConfigItem


def main():
    """
    This function is executed automatically when the module is run directly.
    """

    print("MCC 152 digital input read example.")
    print("Reads the inputs individually and displays their state.")
    print("   Methods demonstrated:")
    print("      mcc152.dio_reset")
    print("      mcc152.dio_input_read_bit")
    print("      mcc152.info")
    print()

    # Get an instance of the selected hat device object.
    address = select_hat_device(HatIDs.MCC_152)

    print("\nUsing address {}.\n".format(address))

    hat = mcc152(address)

    # Reset the DIO to defaults (all channels input, pull-up resistors
    # enabled).
    hat.dio_reset()

    num_channels = hat.info().NUM_DIO_CHANNELS

    run_loop = True
    error = False
    # Loop until the user terminates or we get a library error.
    while run_loop and not error:
        # Read and display the individual channels.
        for channel in range(num_channels):
            try:
                value = hat.dio_input_read_bit(channel)
            except (HatError, ValueError):
                error = True
                break
            else:
                print("DIO{0}: {1}\t".format(channel, value), end="")
        
        if error:
            print("\nError reading the input.")
        else:
            # Wait for the user to enter a response
            message = "\nEnter Q to exit, anything else to read again: "
            if version_info.major > 2:
                response = input(message)
            else:
                response = raw_input(message)

            if response == "q" or response == "Q":
                # Exit the loop
                run_loop = False

if __name__ == '__main__':
    # This will only be run when the module is called directly.
    main()
