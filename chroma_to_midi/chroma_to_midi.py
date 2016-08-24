"""
create a chromagram from an audio file and then render that chromagram to MIDI
""" 

import madmom
import numpy as np
import scipy
import pretty_midi

from sys import argv
from os.path import exists

# Run the script from the command line
script, path_to_audio, path_to_midi, tempo_var = argv

# Create the chromagram
dcp = madmom.audio.chroma.DeepChromaProcessor()
chroma = dcp(path_to_audio)

# Function to threshhold the chroma array to only the top 3 strongest pitch classes. 
def threshhold_chroma(chromagram):
	# Create an array of zeros the same size/dimension as the chromagram
    chromagram_out = scipy.zeros_like(chromagram)  
    # Loop through the chroma_vector the size of the zeros array and sort for the strongest pitch centers
    for i, chroma_vector in enumerate(chromagram):
        chromagram_out[i, chroma_vector.argsort()[::-1][:3]] = [10, 9, 8]
   
    return chromagram_out

# Call the threshholding function
chroma_out = threshhold_chroma(chroma)

# Function to create our MIDI file based on the above sorted chroma array
def chroma_to_midi(chromagram):

    chroma_midi = pretty_midi.PrettyMIDI(midi_file=None, resolution=220, initial_tempo=int(tempo_var))
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)
    
    start=0.0
    end=0.0
    make_a_chord = 0
    vi = 0
    last_vector = []

    # Loop through the chroma vectors of the array by their vector_index
    for vector_index, chroma_vector in enumerate(chromagram):
    	# Everytime we loop through, increase the point in the MIDI file that we are writing by the framesize of the original chromagram
        end+=0.1
        # If it's the first note of the song, or the tonal centers' balance have changed, increase the vector index counter and tell the script we want to make a new chord
        if vi == 0 or not np.array_equal(chroma_vector,last_vector):
            make_a_chord = 1
            vi+=1 
        # If the tonal centers have not changed, don't 
        else:
            make_a_chord = 0
            vi+=1 

        if make_a_chord == 1:
        	# Loop through the current vector of chroma_notes by their chroma_note_index
            for chroma_note_index, chroma_note in enumerate(last_vector):
            	# If it's the strongest chroma center, make a 127 velocity note and append to the pretty_midi object
                if chroma_note == 10:
                    note = pretty_midi.Note(velocity=127, pitch=(chroma_note_index+60), start=start, end=end)
                    piano.notes.append(note)
                # If it's the second strongest chroma center, make a 64 velocity note and append to the pretty_midi object       
                elif chroma_note == 9:
                    note = pretty_midi.Note(velocity=64, pitch=(chroma_note_index+60), start=start, end=end)
                    piano.notes.append(note)   
                # If it's the third strongest chroma center, make a 1 velocity note and append to the pretty_midi object           
                elif chroma_note == 8:
                    note = pretty_midi.Note(velocity=1, pitch=(chroma_note_index+60), start=start, end=end)
                    piano.notes.append(note)   
                else:
                    pass
            # Set the start of the next time we write a note to the end time
            start=end                
        else:
            pass
        # Set the last_vector, so that the next time we loop through we have a state to compare to and decide whether or not we need to write a new MIDI chord
        last_vector = chroma_vector
    # Add the MIDI we just made to the piano instrument   
    chroma_midi.instruments.append(piano)
    # Write the MIDI file to a filename we specified above
    chroma_midi.write(path_to_midi)
    return chroma_midi

# Run the function    
chroma_to_midi(chroma_out)