from audio_tools import record_to_file
import os, sys, shutil

def set_character():
    while True:
        print("Enter character you are recording.")
        c_input = input()
        if len(c_input) > 1:
            print("Please input a single character only.")
        else:
            return c_input
            break

def dir_builder(c_input):
    path = "../data/" + c_input + "/"
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
    os.mkdir( path);
    print("Path is created")

def input_loop(c_input):
    for x in range(10):
        path = "../data/" + c_input + "/" + c_input + "_" + str(x) + ".wav"
        print("Please speak a word into the microphone")
        record_to_file(path)
        print("done - result written to " + path)

if __name__ == '__main__':
    input_character = set_character()
    dir_builder(input_character)
    input_loop(input_character)
