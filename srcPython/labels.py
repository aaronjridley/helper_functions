#!/usr/bin/env python

import datetime

# -------------------------------------------------------------------
# Make a label that shows the whole time range
# -------------------------------------------------------------------

def get_label_time_range(times):
    startTime = times[0]
    endTime = times[-1]    
    label = startTime.strftime('%b %d, %Y %H:%M UT') + ' - ' + \
        endTime.strftime('%b %d, %Y %H:%M UT (Hours)')
    return label
