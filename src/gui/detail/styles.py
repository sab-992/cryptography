def get_button_hover_effect(hex_color: str) -> str:
    ALPHA_VALUE = 30
    HEX_BASE = 16

    def lighter(hex_color: str) -> str:
        if hex_color == "transparent":
            return f"rgba(255, 255, 255, {ALPHA_VALUE})"
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[0:2], HEX_BASE), int(hex_color[2:4], HEX_BASE), int(hex_color[4:6], HEX_BASE)
        r, g, b = min(r + ALPHA_VALUE, 255), min(g + ALPHA_VALUE, 255), min(b + ALPHA_VALUE, 255)
        return f"#{r:02X}{g:02X}{b:02X}"

    def darker(hex_color: str) -> str:
        if hex_color == "transparent":
            return f"rgba(0, 0, 0, {ALPHA_VALUE * 2})"
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[0:2], HEX_BASE), int(hex_color[2:4], HEX_BASE), int(hex_color[4:6], HEX_BASE)
        r, g, b = max(r - ALPHA_VALUE, 0), max(g - ALPHA_VALUE, 0), max(b - ALPHA_VALUE, 0)
        return f"#{r:02X}{g:02X}{b:02X}"

    return f"""\nQPushButton:hover {{ background: { lighter(hex_color) }; }}\nQPushButton:pressed {{ background: { darker(hex_color) }; }}"""