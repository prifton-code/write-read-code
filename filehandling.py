def main():
    print("File Reader and Modifier")
    
    # Get filename from user
    filename = input("Enter the filename to read: ")
    
    try:
        # Read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"Successfully read '{filename}'")
        
        # Modify content (add line numbers and make uppercase)
        lines = content.split('\n')
        modified_lines = []
        
        for i, line in enumerate(lines, 1):
            modified_line = f"{i}: {line.upper()}"
            modified_lines.append(modified_line)
        
        modified_content = '\n'.join(modified_lines)
        
        # Create output filename
        output_filename = filename.replace('.', '_modified.')
        if '_modified' not in output_filename:
            output_filename += '_modified'
        
        # Write to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified file saved as: {output_filename}")
        
        # Show preview
        preview = input("Show preview? (y/n): ").lower()
        if preview == 'y':
            print("\nFirst 5 lines of modified file:")
            for line in modified_lines[:5]:
                print(line)
            if len(modified_lines) > 5:
                print("...")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Cannot read '{filename}'. Check permissions.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
