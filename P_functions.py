import pyaudio
import matplotlib.pyplot as plt
import numpy as np
from peakutils.peak import indexes
import json

def record_note(RECORD_SECONDS):
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 32000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    print("Recording . . . ")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # Record Data in frames as byte list
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()  # Close
    stream.close()
    p.terminate()

    print("Done")
    decoded = np.fromstring(np.asarray(frames), np.int16)

    return decoded

def data_transform(segment):
    print("Transforming data")
    Data = 1 / len(segment) * np.absolute(np.fft.fft(segment)) ** 2  # PSD of data
    # Data = Data[0:6000:2]  # Truncate to important frequencies
    Data = Data[0:6000]
    Data_norm = Data / np.amax(Data)
    print("Done")
    print('')
    return Data

def plot_data(data,peaks):
    print("Plotting data")

    value = []
    for i in peaks:
        value.append(data[i])

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(data)  # Make Plot
    ax1.plot(peaks,value, 'ro')
    plt.show()
    print('')

def detect_note():  #Used to detect if a note is being played, should run constantly
    print("Detecting note")



def find_peaks(Data):
    print("Finding the peaks")
    freq = indexes(Data, thres=0.05, min_dist=10)
    print('Peaks are: %s' % (freq))
    print('')
    return freq

def determine_fundamental_freq(freq):
    print("Determining fundamental frequency")
    # if len(freq) > 1:
    #     temp = []
    #     for i in range(len(freq)-1):
    #         temp.append(freq[i+1]-freq[i])
    #
    #     #take median
    #     f = int(np.median(temp))
    #     print(temp)
    #     print("The median frequency is: %s Hz" % (f))
    #     print('')
    #     return f
    # else:
    #     return freq[0]

    #Experimantal
    res = []
    for i in freq:
        temp = []
        for j in freq:
            temp.append(j%i)
        res.append(int(np.mean(temp)))
        temp = []
    f = freq[res.index(min(res))]
    print("The fundamental frequency is: %s Hz" % (f))
    print('')
    return f


def played_note(f):
    print("Finding the played note")


    with open('data.txt') as json_file: #Load notes file using json
        notes = json.load(json_file)

    for i in notes: #Convert key to int
        notes[int(i)]= notes.pop(i)




    fclosest = min(notes, key=lambda x: abs(x - f))

    note = notes[fclosest]
    diff = abs(fclosest-f)
    print("The played note was %s (%s) with a difference of %s Hz" %(note,fclosest,diff))
    print('')
    return note


def load_note(load_note):
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Note is being loaded")
    path = 'Test/'

    t1 = np.load(path + load_note)
    print("Note %s is loaded" %(load_note))
    print('')
    return t1