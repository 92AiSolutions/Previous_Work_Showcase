from app.controllers.emotion_parser import parse_emotions
from app.controllers.voice_generator import synthesize_voice
from app.controllers.audio_mixer import mix_audio
from pydub import AudioSegment

def generate_teaser(script_text):
    parsed_lines = parse_emotions(script_text)[:3]  # Limit to teaser preview
    voice_segments = []

    for line in parsed_lines:
        audio_bytes = synthesize_voice(line["text"], voice_id="TxGEqnHWrfWFTfGW9XjX")  # static for now
        seg = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
        voice_segments.append(seg)

    return mix_audio(voice_segments, fx_paths=[])
