from audio_tools import record_to_file, calibrate
import os, sys, shutil

# Sets character for recording
def set_character():
    while True:
        print("Enter character you are recording.")
        c_input = input()
        if len(c_input) > 1:
            print("Please input a single character only.")
        else:
            return c_input
            break

# Checks if directory already exists and builds a new one if it does not.
def dir_builder(c_input):
    path = "../data/" + c_input + "/"
    if os.path.exists(path):
        print("Path exists")
    else:
        os.mkdir( path);
    print("Path is created")

# Loops through 10 to create 10 training instances.
def input_loop(c_input):
    for x in range(10):
        path = "../data/" + c_input + "/" + c_input + "_" + str(x) + ".wav"
        print("Please speak a word into the microphone")
        record_to_file(path)
        print("done - result written to " + path)

if __name__ == '__main__':
    print("Please remain silent for 5 seconds for calibration.")
    print("Calibrated for " + str(calibrate()) +" silence value.")
    input_character = set_character()
    dir_builder(input_character)
    input_loop(input_character)
