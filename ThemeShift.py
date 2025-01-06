import ctypes
import winreg as reg
import os

# Constants for changing wallpaper
SPI_SETDESKWALLPAPER = 20

# Paths to your wallpapers
dark_wallpaper = r"C:\path\to\your\dark-wallpaper.jpg"
light_wallpaper = r"C:\path\to\your\light-wallpaper.jpg"

def set_accent_color(r, g, b):
    """
    Set the accent color in Windows by modifying the registry.
    Color is given as RGB values (0-255).
    """
    # Convert RGB to Hex
    color_hex = (r << 16) + (g << 8) + b  # RGB to Hex
    
    registry_path = r"Software\Microsoft\Windows\DWM"
    
    try:
        # Open the registry key for DWM (Desktop Window Manager)
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE)
        
        # Set the AccentColor key with the new color value
        reg.SetValueEx(key, "AccentColor", 0, reg.REG_DWORD, color_hex)
        reg.CloseKey(key)
        
        print(f"Accent color changed to RGB({r}, {g}, {b})")
        
    except Exception as e:
        print(f"Error setting accent color: {e}")

def switch_theme(mode="dark"):
    """
    Switch between Dark and Light theme by modifying the Windows registry.
    """
    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    
    # Open the registry key for Personalize
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE)

    if mode == "dark":
        # Set the theme to dark mode
        reg.SetValueEx(key, "AppsUseLightTheme", 0, reg.REG_DWORD, 0)
        reg.SetValueEx(key, "SystemUsesLightTheme", 0, reg.REG_DWORD, 0)
        print("Switched to Dark Mode")
        # Set dark taskbar accent color (black)
        set_accent_color(0, 0, 0)
    elif mode == "light":
        # Set the theme to light mode
        reg.SetValueEx(key, "AppsUseLightTheme", 0, reg.REG_DWORD, 1)
        reg.SetValueEx(key, "SystemUsesLightTheme", 0, reg.REG_DWORD, 1)
        print("Switched to Light Mode")
        # Set light taskbar accent color (white)
        set_accent_color(255, 255, 255)

    # Close the registry key
    reg.CloseKey(key)

def change_wallpaper(image_path):
    """
    Change the wallpaper to the given image path using Windows API.
    """
    if os.path.exists(image_path):
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        print(f"Wallpaper changed to {image_path}")
    else:
        print(f"Error: The wallpaper path '{image_path}' does not exist.")

def main():
    # Ask the user if they are indoors or outdoors
    user_input = input("Are you outdoors or indoors? (type 'outdoors' or 'indoors'): ").strip().lower()

    if user_input == "indoors":
        # If indoors, switch to dark theme and dark wallpaper
        print("You are indoors.")
        switch_theme("dark")
        change_wallpaper(dark_wallpaper)
    elif user_input == "outdoors":
        # If outdoors, switch to light theme and light wallpaper
        print("You are outdoors.")
        switch_theme("light")
        change_wallpaper(light_wallpaper)
    else:
        print("Invalid input! Please type 'indoors' or 'outdoors'.")

if __name__ == "__main__":
    main()
