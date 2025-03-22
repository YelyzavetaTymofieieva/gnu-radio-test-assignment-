from scipy.io import wavfile

def get_sample_rate(file_path):
    sample_rate, _ = wavfile.read(file_path)
    return sample_rate

# Example
print(get_sample_rate("file1.wav"))
