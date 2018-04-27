import snowboydecoder_arecord
import snowboydecoder
import sys
import signal
import wave

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) != 3:
    print("Error: need to specify model name")
    print("Usage: python demo.py wave_file your.model")
    sys.exit(-1)

wave_file = sys.argv[1]
model_file = sys.argv[2]

f = wave.open(wave_file)
data = f.readframes(f.getnframes())
sensitivity = 0.5
detection = snowboydecoder_arecord.HotwordDetector(model_file, sensitivity=sensitivity)

ans = detection.detector.RunDetection(data)
#ans = detection.start(detected_callback=snowboydecoder.play_audio_file,
#                      interrupt_check=interrupt_callback,
#                      sleep_time=0.03)


if ans == 1:
    print('Hotword Detected!')
    snowboydecoder_arecord.play_audio_file()
else:
    print('Hotword Not Detected!')
#detection.terminate()

# capture SIGINT signal, e.g., Ctrl+C
#signal.signal(signal.SIGINT, signal_handler)

#detector = snowboydecoder_arecord.HotwordDetector(model, sensitivity=0.5)
#print('Listening... Press Ctrl+C to exit')

# main loop
#detector.start(detected_callback=snowboydecoder_arecord.play_audio_file,
               #interrupt_check=interrupt_callback,
               #sleep_time=0.03)

#detector.terminate()
