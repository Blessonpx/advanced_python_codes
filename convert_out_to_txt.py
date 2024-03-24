## THis is for converting output of cprofile to a txt file 
import pstats

stats = pstats.Stats('prof.out')
stats.strip_dirs()
stats.sort_stats('cumulative')
with open('prof.txt', 'w') as f:
    # Redirect the output to a file
    stats.stream = f
    stats.print_stats()
