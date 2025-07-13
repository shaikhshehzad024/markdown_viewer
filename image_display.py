"""Image display functionality for terminal markdown viewer."""

import os
from .constants import RESETCOLOR, CYAN, YELLOW, RED


def display_image_info(alt_text, image_path, max_width=80):
    """Display image information when image cannot be rendered."""
    if not os.path.exists(image_path):
        return f"{RED}[Image not found: {alt_text}] ({image_path}){RESETCOLOR}"
    
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            width, height = img.size
            format_info = img.format or "Unknown"
            file_size = os.path.getsize(image_path)
            
            # Format file size
            if file_size < 1024:
                size_str = f"{file_size} bytes"
            elif file_size < 1024 * 1024:
                size_str = f"{file_size / 1024:.1f} KB"
            else:
                size_str = f"{file_size / (1024 * 1024):.1f} MB"
            
            info = f"{CYAN}[{alt_text}]{RESETCOLOR} {YELLOW}({width}x{height} {format_info}, {size_str}){RESETCOLOR}"
            return info
    except Exception as e:
        return f"{RED}[Image error: {alt_text}] ({image_path}) - {str(e)}{RESETCOLOR}"


def image_to_ascii_blocks(image_path, max_width=80, max_height=24):
    """Convert image to ASCII block characters for terminal display."""
    try:
        from PIL import Image
        
        if not os.path.exists(image_path):
            return None
            
        with Image.open(image_path) as img:
            # Convert to grayscale for ASCII conversion
            img = img.convert('L')
            
            # Calculate dimensions maintaining aspect ratio
            orig_width, orig_height = img.size
            aspect_ratio = orig_width / orig_height
            
            # Adjust for character aspect ratio (characters are taller than wide)
            char_aspect = 0.5  # Typical character height/width ratio
            
            if orig_width > max_width:
                new_width = max_width
                new_height = int(max_width / aspect_ratio * char_aspect)
            else:
                new_width = orig_width
                new_height = int(orig_height * char_aspect)
                
            if new_height > max_height:
                new_height = max_height
                new_width = int(max_height * aspect_ratio / char_aspect)
            
            # Resize image
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to ASCII using block characters
            ascii_chars = [' ', '░', '▒', '▓', '█']
            
            result = []
            for y in range(new_height):
                line = ""
                for x in range(new_width):
                    pixel = img.getpixel((x, y))
                    # Map pixel value (0-255) to ASCII character index
                    char_index = min(int(pixel / 255 * (len(ascii_chars) - 1)), len(ascii_chars) - 1)
                    line += ascii_chars[char_index]
                result.append(line)
            
            return '\n'.join(result)
            
    except Exception as e:
        return None


def display_image(alt_text, image_path, max_width=80, max_height=24):
    """Display image in terminal or show image information."""
    # Try to display as ASCII art first
    ascii_art = image_to_ascii_blocks(image_path, max_width, max_height)
    
    if ascii_art:
        # Display the ASCII art with a header
        header = f"{CYAN}[{alt_text}]{RESETCOLOR}"
        return f"{header}\n{ascii_art}"
    else:
        # Fall back to showing image information
        return display_image_info(alt_text, image_path, max_width)