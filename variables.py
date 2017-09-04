# Here come the variables



# manila_pop = 1788573
# manila_area = 16.56
# manila_pop_density = manila_pop / manila_area
# print(manila_area)
# print(manila_pop_density)
#
#
# manila_pop += 1675 # increase the value of manila_pop by 1675
# print(manila_pop)
# manila_pop -= 250 # decrease the value of manila_pop by 250
# print(manila_pop)
# manila_pop *= 0.9 # decimate manila_pop
# print(manila_area)
# manila_area /=  2 # approximate the female population of Manila
# print(manila_area)
# print(manila_pop)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)