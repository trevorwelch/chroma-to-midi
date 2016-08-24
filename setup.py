from setuptools import setup

setup(
    name='chroma_to_midi',
    version='0.1',
    description='Functions and classes for handling MIDI data conveniently.',
    author='Trevor Welch',
    author_email='trevor.welch@gmail.com',
    url='https://github.com/trevorwelch/chroma-to-midi',
    packages=['chroma_to_midi'],
    package_data={'': ['']},
    long_description="""\
    Takes a chromagram, compute the 3 strongest values, then writes a MIDI file
    with velocities 127, 60, and 10 respectively for every chord in the song.
    """,
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python 2.7",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
    keywords='audio music midi mir',
    license='MIT',
    install_requires=[
        'numpy >= 1.7.0',
        'midi',
        'madmom',
        'pretty_midi',
        'scipy'
    ],
)
