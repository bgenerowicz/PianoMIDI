import P_functions as p_f

#Variables
RECORD_SECONDS = 2
load_note = 'G4.npy'
#Record segment
# segment = p_f.record_note(RECORD_SECONDS)



# Data = p_f.data_transform(segment)


Data = p_f.load_note(load_note)

peaks = p_f.find_peaks(Data)

f = p_f.determine_fundamental_freq(peaks)

played_note = p_f.played_note(f)


p_f.plot_data(Data,peaks)