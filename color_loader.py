def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        blue_channel = int(255 * (num_colors - i) / num_colors)
        red_channel = int(255 * i / num_colors)
        green_channel = 255 - max(blue_channel, red_channel)
        
        # Create the RGB color
        color = (red_channel, green_channel, blue_channel)
        colors.append(color)
    
    return colors


colors = generate_colors(100)