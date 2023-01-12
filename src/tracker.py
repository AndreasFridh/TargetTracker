import numpy as np

# positions of the microphones in 3D space
microphone_positions = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]])

# time delay of arrival of the sound trigger at each microphone
tdoa = np.array([0.1, 0.2, 0.3])

# sound speed in meters per second
sound_speed = 343

# calculate the difference in distance for each pair of microphones
differences = np.array([microphone_positions[i+1] - microphone_positions[i] for i in range(len(microphone_positions)-1)])

# calculate the time delay of arrival for each pair of microphones
differences *= sound_speed / tdoa

# calculate the position of the sound source using the law of cosines
A = np.linalg.norm(differences[0])
B = np.linalg.norm(differences[1])
C = np.linalg.norm(differences[2])
alpha = np.arccos((B**2 + C**2 - A**2) / (2 * B * C))
beta = np.arccos((A**2 + C**2 - B**2) / (2 * A * C))

# sound source position
sound_source_position = microphone_positions[2] + differences[2] / C * np.cos(beta)

print("Sound source position:", sound_source_position)
