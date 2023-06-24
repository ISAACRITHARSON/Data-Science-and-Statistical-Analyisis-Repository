confidence_level = 0.95
sample_mean = s2_mean
degrees_of_freedom = sample2.size - 1
sample_standard_error = st.sem(sample2)
confidence_interval = st.t.interval(confidence_level, degrees_of_freedom,
sample_mean, sample_standard_error)
print('Confidence Interval : ',confidence_interval)
