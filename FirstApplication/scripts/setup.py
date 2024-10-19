from screeninfo import get_monitors

class Setup:
    def __init__(self):
        pass
    
    @staticmethod
    def get_monitor_size():
        monitor_list = get_monitors()
        
        for m in monitor_list:
            active_m = str(m)
            print(active_m)
            
            if active_m.__contains__("is_primary=True"):
                screen_width_string = active_m[active_m.index("width="):active_m.index(", height=")]
                screen_height_string = active_m[active_m.index("height="):active_m.index(", width_mm=")]  
                screen_width = int(screen_width_string[screen_width_string.index("=") + 1:len(screen_width_string)])
                screen_height = int(screen_height_string[screen_height_string.index("=") + 1:len(screen_height_string)])
        
        return screen_width, screen_height