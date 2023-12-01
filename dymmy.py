from google.cloud import speech_v1p1beta1 as speech
import io

def speech_to_text():
    # Set up Google Cloud Speech client
    client = speech.SpeechClient()

    # Use the default microphone as the audio source
    with io.open("path/to/audio/file.wav", "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Perform speech recognition
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

if __name__ == "__main__":
    speech_to_text()
