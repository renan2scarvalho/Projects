def parse_gpx(track, elevation, dtime, track_length,
            lon_list, lat_list, elev_list, time_list):
    
    """
    Function to parse the gpx file
    """

    for s in range(track_length):
        
        lon,lat = track[s].attributes['lon'].value, track[s].attributes['lat'].value
        elev = elevation[s].firstChild.nodeValue
        lon_list.append(float(lon))
        lat_list.append(float(lat))
        elev_list.append(float(elev))
        
        dt = dtime[s].firstChild.nodeValue
        time_split = dt.split('T')
        hms_split = time_split[1].split(':')
        time_hour = int(hms_split[0])
        time_min = int(hms_split[1])
        time_sec = int(hms_split[2].split('Z')[0])
        total_second = time_hour*3600 + time_min*60 + time_sec
        time_list.append(total_second)
