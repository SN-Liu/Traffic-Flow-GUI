import random

def asymmode(traffic_segment_list):
    for i in range(len(traffic_segment_list)):
        if traffic_segment_list[i]['class'] == 'truck':
            traffic_segment_list[i]['asymmode'] = 'RHTraffic'
            if traffic_segment_list[i]['character'] == 'Aggressive':
                traffic_segment_list[i]['asymmode_para'] = 0.4
            elif traffic_segment_list[i]['character'] == 'Normal':
                traffic_segment_list[i]['asymmode_para'] = 0.6
            elif traffic_segment_list[i]['character'] == 'Defensive':
                traffic_segment_list[i]['asymmode_para'] = 0.8
        else:
            traffic_segment_list[i]['asymmode'] = random.choice(['LHTraffic','SymTraffic'])
            if traffic_segment_list[i]['character'] == 'Aggressive':
                traffic_segment_list[i]['asymmode_para'] = 0.8
            elif traffic_segment_list[i]['character'] == 'Normal':
                traffic_segment_list[i]['asymmode_para'] = 0.5
            elif traffic_segment_list[i]['character'] == 'Defensive':
                traffic_segment_list[i]['asymmode_para'] = 0.3
    
    return traffic_segment_list