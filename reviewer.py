# Simple AI-assisted code reviewer

def review_code(code_text):
    suggestions = []

    code = code_text.strip()

    # Short code check
    if len(code) < 10:
        return "The code is too short to review. Try pasting a function or a few lines."

    # Missing comments
    if "#" not in code:
        suggestions.append("Consider adding comments to explain your logic.")

    # Long lines
    long_lines = [line for line in code.split("\n") if len(line) > 80]
    if long_lines:
        suggestions.append(f"{len(long_lines)} line(s) are quite long. Breaking them up may help readability.")

    # Unused import check
    imported_modules = []
    lines = code.split("\n")
    
    for line in lines:
        line_strip = line.strip()
        if line_strip.startswith("import "):
            parts = line_strip.split()
            if len(parts) > 1:
                imported_modules.append(parts[1])
    
    # Check usage outside import lines
    for module in imported_modules:
        used_elsewhere = False
        for line in lines:
            if not line.strip().startswith("import") and module in line:
                used_elsewhere = True
                break
        if not used_elsewhere:
            suggestions.append(f"The module '{module}' might be unused.")


    # Indentation check
    for line in code.split("\n"):
        if line.startswith("    ") and "\t" in line:
            suggestions.append("Mixed tabs and spaces detected. Consider using consistent indentation.")

    # If no suggestions
    if not suggestions:
        return "The code looks clean. No major issues spotted."

    # Build output
    final_output = "Here are some suggestions:\n\n"
    for s in suggestions:
        final_output += "- " + s + "\n"

    return final_output
