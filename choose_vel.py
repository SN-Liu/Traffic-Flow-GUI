import random

def vel_distribution(vel,velocity_level,traffic_segment_list):
    
    vel = sorted(vel)

    vel_e = vel[0:velocity_level[4]]
    vel_d = vel[velocity_level[4]:velocity_level[4]+velocity_level[3]]
    vel_c = vel[velocity_level[4]+velocity_level[3]:velocity_level[4]+velocity_level[3]+velocity_level[2]]
    vel_b = vel[velocity_level[4]+velocity_level[3]+velocity_level[2]:velocity_level[4]+velocity_level[3]+velocity_level[2]+velocity_level[1]]
    vel_a = vel[-velocity_level[0]:]
    
    
    for i in range(len(traffic_segment_list)):
        #car
        if traffic_segment_list[i]['class'] == 'car' and traffic_segment_list[i]['character'] == 'Aggressive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_a)
            vel_a.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'car' and traffic_segment_list[i]['character'] == 'Normal':
            traffic_segment_list[i]['velocity'] = random.choice(vel_b)
            vel_b.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'car' and traffic_segment_list[i]['character'] == 'Defensive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_c)
            vel_c.remove(traffic_segment_list[i]['velocity'])
        #van
        elif traffic_segment_list[i]['class'] == 'van' and traffic_segment_list[i]['character'] == 'Aggressive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_b)
            vel_b.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'van' and traffic_segment_list[i]['character'] == 'Normal':
            traffic_segment_list[i]['velocity'] = random.choice(vel_c)
            vel_c.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'van' and traffic_segment_list[i]['character'] == 'Defensive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_d)
            vel_d.remove(traffic_segment_list[i]['velocity'])
        #truck
        elif traffic_segment_list[i]['class'] == 'truck' and traffic_segment_list[i]['character'] == 'Aggressive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_c)
            vel_c.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'truck' and traffic_segment_list[i]['character'] == 'Normal':
            traffic_segment_list[i]['velocity'] = random.choice(vel_d)
            vel_d.remove(traffic_segment_list[i]['velocity'])
        elif traffic_segment_list[i]['class'] == 'truck' and traffic_segment_list[i]['character'] == 'Defensive':
            traffic_segment_list[i]['velocity'] = random.choice(vel_e)
            vel_e.remove(traffic_segment_list[i]['velocity'])

    return traffic_segment_list


