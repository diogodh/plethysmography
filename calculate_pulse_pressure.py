def calc_pulsepressure_var(high_max, low_max, high_min, low_min):
	big_pulsepressure = high_max - high_min
	low_pulsepressure = low_max - low_min
	avg_pulsepressure = (big_pulsepressure + low_pulsepressure) / 2

	ppv = ((big_pulsepressure - low_pulsepressure) / avg_pulsepressure)

	print(f"Pulse pressure is {ppv:.2f}")
	return ppv