**ThemeShift**
    A Python script that switches themes and wallpapers based on whether you're indoors or outdoors.


**ThemeShift – Automatic Theme and Wallpaper Changer for Windows**
    ThemeShift is a Python script that dynamically switches between light and dark themes on your Windows PC based on your environment (indoors or outdoors). It also automatically changes your desktop wallpaper to match      the theme, creating a seamless and adaptive user experience for different lighting conditions.

##Key Features:
  Automatic Theme Switching: Switches between dark mode and light mode based on your current environment — indoors or outdoors.
  Wallpaper Customization: Changes your desktop wallpaper along with the theme to maintain a consistent aesthetic that suits the lighting.
  Taskbar Accent Color Adjustment: Automatically adjusts the taskbar accent color to match your selected theme, providing a consistent and polished look.
  User-Friendly Interface: Simple command-line interface (CLI) where you just tell the script whether you're indoors or outdoors, and it handles the rest.

##How It Works:
  Indoors: The script switches your system to dark mode and sets a dark wallpaper, ideal for low-light or night-time use.
  Outdoors: The script switches your system to light mode and sets a light wallpaper, optimizing visibility in bright outdoor environments.

##Why Use ThemeShift?
  Optimized Visual Comfort: Automatically adjust the theme and wallpaper based on the lighting around you, helping to reduce eye strain.
  Effortless Transitions: Say goodbye to manual theme switching and wallpaper changes. Let ThemeShift do all the work for you.
  Easy to Customize: You can easily change the wallpaper paths or adjust the taskbar accent colors to suit your personal preferences.


##Requirements:
  Python 3.x
  ctypes and winreg libraries (both are included in the standard Python library for Windows)


##How to Use:
  Clone or download this repository.
  Open a terminal (Command Prompt or PowerShell).
  Run the script using the following command:
  bash
  Copy code
  python themeshift.py
  The script will ask if you're indoors or outdoors. Based on your input, it will automatically switch the theme and change the wallpaper accordingly.


##Customization:
  Update the file paths for your dark and light wallpapers in the script.
  Modify the RGB color values in the script to change the taskbar accent color for each theme.
