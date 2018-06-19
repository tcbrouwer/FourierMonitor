import random

from FourierClerk import FourierClerk

clerk = FourierClerk(1000)
supervisor = FourierClerk(10)
print(clerk.get_coefficients_for_channel(0))
for i in range(0,2000):
    #clerk.note([math.sin(math.pi * i/10)])
    clerk.note([random.random()])
    supervisor.note(clerk.get_coefficients_for_channel(0))
    print(supervisor.get_coefficients_for_channel(0))

