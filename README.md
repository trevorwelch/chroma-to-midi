# Chroma to MIDI
### A simple module to create a chromagram from an audio file and then render that chromagram to MIDI

A hack started at CCRMA Summer MIR 2016: compute a chromagram, then sort the resulting array by its the 3 strongest values (tonal centers, more or less) and then write a MIDI file with "chroma-chords" at velocities 127, 64, and 1 respectively.

So, the MIDI file generated is a 3 note chord starting from C3 (aka middle c), with the 127 velocity note representing the strongest chroma, 64 the second strongest, 1 the third strongest. The chord duration is continuous as long as the chroma strength stays the same, and only makes a new chord if the chroma strength changes. 

It works a little better if you input the tempo, which you can find by listening and tapping it out [here](http://www.all8.com/tools/bpm.htm) or automatically estimate it in Python using [Librosa](http://musicinformationretrieval.com/tempo_estimation.html) or with Madmom [Madmom](http://madmom.readthedocs.io/en/latest/modules/features/tempo.html) (among other packages).

Uses Madmom's DeepChromaProcessor to create the Chromagram and then C Raffel's pretty_midi to print the MIDI file. 

Example usage for creating a chromagram and then generating a MIDI file, from the root directory of the repo:

```
$ cd chroma_to_midi
$ python chroma_to_midi.py <path_to_audio> <path_to_midi> <tempo>
```

An example of the output is included in the repo, `kanaya_base_salt.mid`, which is a chroma-to-MIDI representation of the song ['Salt' by Kanaya Base](https://dl.dropboxusercontent.com/u/53977633/kanaya_base_salt_c_90bpm.mp3) (right click, save target as to download) from Lady Boy Records (Reykjavik, IS), used with permission ;) 

### Dependencies: 
- [Madmom](https://github.com/CPJKU/madmom) 
- [pretty_midi](https://github.com/craffel/pretty-midi)   
- Numpy, Scipy

### Thanks for the help:
Steve Tjoa, Jeff Scott, James Jannicelli