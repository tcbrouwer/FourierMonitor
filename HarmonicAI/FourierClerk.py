import cmath


class Channel:

    def __init__(self, n):
        self.observations = [0] * n
        self.coefficients = dict.fromkeys(range(0, n-1), 0 * cmath.sqrt(-1))


class FourierClerk:

    def __init__(self, num_observations, num_channels=1):
        self.num_observations = num_observations
        self.num_channels = num_channels
        self.channels = [Channel(num_observations) for i in range(num_channels)]
        self.state = num_observations

    def note(self, observation):
        for index, channel in enumerate(self.channels, start=0):
            self._note(observation[index], channel)
        self._increase_state()

    def _note(self, single_observation, channel):
        channel.observations.insert(0, single_observation)
        removed_observation = channel.observations.pop()
        for key, value in channel.coefficients.items():
            cat = (2 * cmath.pi * (key - self.state)) / self.num_observations  # ??
            weight = cmath.exp(-cmath.sqrt(-1) * cat)
            new_value = value + (channel.observations[0] - removed_observation) * weight
            channel.coefficients[key] = new_value

    def get_coefficients_for_channel(self, channel_index):
        return self.channels[channel_index].coefficients

    def _increase_state(self):
        self.state = (self.state + 1) % self.num_observations
