import librosa
import numpy as np
def extract_pitch_yin(filepath, sr=22050, frame_length=2048, hop_length=256):
    y, sr = librosa.load(filepath, sr=sr)
    f0 = librosa.yin(
        y,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7'),
        sr=sr,
        frame_length=frame_length,
        hop_length=hop_length
    )
    return f0

def hz_to_note_name(frequencies):
    notes = []
    for f in frequencies:
        if np.isnan(f):
            notes.append(None)
        else:
            midi = librosa.hz_to_midi(f)
            name = librosa.midi_to_note(midi)
            notes.append(name)
    return notes


