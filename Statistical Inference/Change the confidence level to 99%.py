modified_level = 0.99
modified_interval = st.t.interval(confidence_level, degrees_of_freedom,
sample_mean, sample_standard_error)
print('Modified CL of above one : ',modified_interval)
