from pydub import AudioSegment
import os
import uuid

def mix_audio(voice_segments, fx_paths):
    base = AudioSegment.silent(duration=0)
    for seg in voice_segments:
        base += seg

    for fx_path in fx_paths:
        fx = AudioSegment.from_file(fx_path)
        base = base.overlay(fx)

    output_path = f"outputs/teasers/teaser_{uuid.uuid4().hex}.mp3"
    base.export(output_path, format="mp3")
    return output_path
