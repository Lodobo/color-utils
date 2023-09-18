import yaml

class Base16:
    def __init__(self, path: str):
        self.scheme = self.parse_yaml(path)
        
        self.name=   self.scheme["scheme"]
        self.base00= self.scheme["base00"]
        self.base01= self.scheme["base01"]
        self.base02= self.scheme["base02"]
        self.base03= self.scheme["base03"]
        self.base04= self.scheme["base04"]
        self.base05= self.scheme["base05"]
        self.base06= self.scheme["base06"]
        self.base07= self.scheme["base07"]
        self.base08= self.scheme["base08"]
        self.base09= self.scheme["base09"]
        self.base0A= self.scheme["base0A"]
        self.base0B= self.scheme["base0B"]
        self.base0C= self.scheme["base0C"]
        self.base0D= self.scheme["base0D"]
        self.base0E= self.scheme["base0E"]
        self.base0F= self.scheme["base0F"]

    def parse_yaml(self, file: str) -> dict:
        with open(file, 'r') as file:
            scheme: dict = yaml.safe_load(file)
            return scheme

    def print_eight_bit(self):
        print("To do")

    def print_rgb(self):
        print("To do")

    def print_hex(self):
        print("To do")
        
    def print(self):
        print(
            f"scheme \t {self.name}\n"
            f"base00 \t {self.base00} \t rgb {hex_to_rgb(self.base00)} \t u8 ({hex_to_u8(self.base00)})\n"
            f"base01 \t {self.base01} \t rgb {hex_to_rgb(self.base01)} \t u8 ({hex_to_u8(self.base01)})\n"
            f"base02 \t {self.base02} \t rgb {hex_to_rgb(self.base02)} \t u8 ({hex_to_u8(self.base02)})\n"
            f"base03 \t {self.base03} \t rgb {hex_to_rgb(self.base03)} \t u8 ({hex_to_u8(self.base03)})\n"
            f"base04 \t {self.base04} \t rgb {hex_to_rgb(self.base04)} \t u8 ({hex_to_u8(self.base04)})\n"
            f"base05 \t {self.base05} \t rgb {hex_to_rgb(self.base05)} \t u8 ({hex_to_u8(self.base05)})\n"
            f"base06 \t {self.base06} \t rgb {hex_to_rgb(self.base06)} \t u8 ({hex_to_u8(self.base06)})\n"
            f"base07 \t {self.base07} \t rgb {hex_to_rgb(self.base07)} \t u8 ({hex_to_u8(self.base07)})\n"
            f"base08 \t {self.base08} \t rgb {hex_to_rgb(self.base08)} \t u8 ({hex_to_u8(self.base08)})\n"
            f"base09 \t {self.base09} \t rgb {hex_to_rgb(self.base09)} \t u8 ({hex_to_u8(self.base09)})\n"
            f"base0A \t {self.base0A} \t rgb {hex_to_rgb(self.base0A)} \t u8 ({hex_to_u8(self.base0A)})\n"
            f"base0B \t {self.base0B} \t rgb {hex_to_rgb(self.base0B)} \t u8 ({hex_to_u8(self.base0B)})\n"
            f"base0C \t {self.base0C} \t rgb {hex_to_rgb(self.base0C)} \t u8 ({hex_to_u8(self.base0C)})\n"
            f"base0D \t {self.base0D} \t rgb {hex_to_rgb(self.base0D)} \t u8 ({hex_to_u8(self.base0D)})\n"
            f"base0E \t {self.base0E} \t rgb {hex_to_rgb(self.base0E)} \t u8 ({hex_to_u8(self.base0E)})\n"
            f"base0F \t {self.base0F} \t rgb {hex_to_rgb(self.base0F)} \t u8 ({hex_to_u8(self.base0F)})\n"
        )

# Function to convert a hexadecimal color to an 8-bit u8 color
def hex_to_u8(hex_color: str) -> int:
    decimal_color = int(hex_color, 16)
    u8_color = decimal_color % 256
    return u8_color

# Function to convert a hexadecimal color to RGB values
def hex_to_rgb(hex_color: str) -> (int, int, int):
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    return (red, green, blue)