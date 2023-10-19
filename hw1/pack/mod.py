def theme(current_theme: str) -> str:
    if current_theme == "light":
        return "dark"
    else:
        return "light"


def generate_qr_theme(current_theme):
    if current_theme == "dark":
        return "#f2bf2b", "#252525"
    else:
        return "grey", "white"


text_about = """QR Code Generator App"

Create personalized QR codes effortlessly!
This intuitive application lets you swiftly generate QR codes from links.
Experience a sleek interface designed using customtkinter, an advanced UI library. 
Just input your link, click 'Generate QR code', and voilà! 
The generated QR code is ready to use. 
Explore the dynamic blend of aesthetics and functionality.

Features:

Generate QR codes from links
Stylish and user-friendly design
Powered by customtkinter and qrcode
Unleash the power of QR codes with ease. 
Elevate your link sharing experience today!"""