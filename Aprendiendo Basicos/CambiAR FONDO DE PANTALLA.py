import ctypes
import os
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'leeder.jpg', 3) 
#'C:\\Users\\Public\\Pictures\\abc.jpg'