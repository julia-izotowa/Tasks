"""
Check if given chord is minor or major.

Rules:

Basic minor/major chord have three elements.

Chord is minor when interval between first and second element equals 3 and between second and third -> 4.

Chord is major when interval between first and second element equals 4 and between second and third -> 3.

In minor/major chord interval between first and third element equals... 7.
"""


def minor_or_major(chord):
    notes = ['C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', ['F#', 'Gb'], 'G', ['G#', 'Ab'], 'A', ['A#', 'Bb'], 'B']
    positions = []
    for chord_note in chord.split(" "):
        if chord_note in notes:
            note_index = notes.index(chord_note)
            if len(positions) > 0 and note_index < positions[-1]:
                note_index += 12
            positions.append(note_index)
        else:
            for note in notes:
                if chord_note in note:
                    note_index = notes.index(note)
                    if len(positions) > 0 and note_index < positions[-1]:
                        note_index += 12
                    positions.append(note_index)
                    break

    if len(positions) == 3 and abs(positions[0] - positions[1]) == 3 and abs(positions[1] - positions[2]) == 4:
        return 'Minor'
    elif len(positions) == 3 and abs(positions[0] - positions[1]) == 4 and abs(positions[1] - positions[2]) == 3:
        return 'Major'
    else:
        return 'Not a chord'


if __name__ == "__main__":
    assert minor_or_major('F A C') == "Major"
    assert minor_or_major('C Eb G') == "Minor"
    assert minor_or_major('C D E') == "Not a chord"
    assert minor_or_major('C D') == "Not a chord"
    assert minor_or_major('F# A# C#') == "Major"
