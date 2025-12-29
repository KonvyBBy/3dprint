#!/usr/bin/env python3
"""
Generate a 3D printable keychain with 'Austin' text - Final Version.

This version creates a clean, printable keychain design optimized for FDM/resin printing.
"""

import trimesh


def create_austin_keychain_final():
    """Create a professional keychain design."""
    
    # Parameters
    length = 50  # mm
    width = 20   # mm
    height = 3   # mm
    hole_diameter = 5  # mm
    hole_radius = hole_diameter / 2
    
    # Create the main rectangular base
    base = trimesh.creation.box(extents=[length, width, height])
    base.apply_translation([length/2, width/2, height/2])
    
    print("✓ Created rectangular base (50mm x 20mm x 3mm)")
    
    # Create keyring hole positioned 5mm from right edge, centered vertically
    hole_x = length - 5
    hole_y = width / 2
    hole_z = height / 2
    
    hole = trimesh.creation.cylinder(
        radius=hole_radius,
        height=height + 1,  # Slightly taller to ensure clean subtraction
        sections=32
    )
    hole.apply_translation([hole_x, hole_y, hole_z])
    
    # Subtract hole from base
    base_with_hole = base.difference(hole, engine='manifold')
    print("✓ Created and subtracted keyring hole (5mm diameter)")
    
    # Create embossed "AUSTIN" text using geometric primitives
    # Text will be raised 1mm above the surface
    text_height = 8  # Height of letters
    text_depth = 1   # How much the text protrudes
    stroke_width = 1.2  # Width of letter strokes
    
    # Position text on the left side of keychain
    text_start_x = 4
    text_start_y = width / 2
    text_start_z = height  # Top surface
    
    text_blocks = []
    x_pos = text_start_x
    letter_spacing = 5.5
    
    # Helper function to create a block
    def add_block(x, y_offset, w, h, d=text_depth):
        block = trimesh.creation.box(extents=[w, h, d])
        block.apply_translation([x + w/2, text_start_y + y_offset, text_start_z + d/2])
        return block
    
    # Letter A (x_pos)
    text_blocks.append(add_block(x_pos, 0, stroke_width, text_height))  # Left vertical
    text_blocks.append(add_block(x_pos + 3, 0, stroke_width, text_height))  # Right vertical
    text_blocks.append(add_block(x_pos, text_height/2 - stroke_width/2, 4.2, stroke_width))  # Top horizontal
    text_blocks.append(add_block(x_pos, text_height/4 - stroke_width/2, 4.2, stroke_width))  # Middle crossbar
    x_pos += letter_spacing
    
    # Letter U
    text_blocks.append(add_block(x_pos, 0, stroke_width, text_height))  # Left vertical
    text_blocks.append(add_block(x_pos + 3, 0, stroke_width, text_height))  # Right vertical
    text_blocks.append(add_block(x_pos, -text_height/2 + stroke_width/2, 4.2, stroke_width))  # Bottom bar
    x_pos += letter_spacing
    
    # Letter S (simplified)
    text_blocks.append(add_block(x_pos, text_height/2 - stroke_width/2, 3.5, stroke_width))  # Top bar
    text_blocks.append(add_block(x_pos, 0, 3.5, stroke_width))  # Middle bar
    text_blocks.append(add_block(x_pos, -text_height/2 + stroke_width/2, 3.5, stroke_width))  # Bottom bar
    text_blocks.append(add_block(x_pos, text_height/4 - stroke_width/4, stroke_width, text_height/4 + stroke_width))  # Top-left vertical connecting to top and middle bars
    text_blocks.append(add_block(x_pos + 2.8, -text_height/4 + stroke_width/4, stroke_width, text_height/4 + stroke_width))  # Bottom-right vertical connecting to middle and bottom bars
    x_pos += letter_spacing
    
    # Letter T
    text_blocks.append(add_block(x_pos + 1.5, 0, stroke_width, text_height))  # Vertical center
    text_blocks.append(add_block(x_pos, text_height/2 - stroke_width/2, 4, stroke_width))  # Top bar
    x_pos += letter_spacing
    
    # Letter I
    text_blocks.append(add_block(x_pos + 1.5, 0, stroke_width, text_height))  # Vertical
    x_pos += letter_spacing
    
    # Letter N
    text_blocks.append(add_block(x_pos, 0, stroke_width, text_height))  # Left vertical
    text_blocks.append(add_block(x_pos + 3, 0, stroke_width, text_height))  # Right vertical
    # Diagonal approximated with multiple small blocks
    text_blocks.append(add_block(x_pos + 0.7, text_height/3, stroke_width, text_height/3.5))  # Upper diagonal segment
    text_blocks.append(add_block(x_pos + 1.5, 0, stroke_width, text_height/3.5))  # Middle diagonal segment
    text_blocks.append(add_block(x_pos + 2.3, -text_height/3, stroke_width, text_height/3.5))  # Lower diagonal segment
    
    print(f"✓ Created 'AUSTIN' text with {len(text_blocks)} components")
    
    # Union all text blocks with the base
    all_parts = [base_with_hole] + text_blocks
    final_mesh = trimesh.util.concatenate(all_parts)
    
    # Attempt to merge and clean up the mesh
    try:
        # Merge vertices that are very close
        final_mesh.merge_vertices()
        # Fix normals
        trimesh.repair.fix_normals(final_mesh)
        print("✓ Optimized mesh geometry")
    except Exception as e:
        print(f"! Mesh optimization skipped: {e}")
    
    print("✓ Combined all components into final design")
    
    return final_mesh


def main():
    """Generate and save the keychain."""
    print("=" * 50)
    print("Generating Austin Keychain")
    print("=" * 50)
    print()
    
    keychain = create_austin_keychain_final()
    
    # Export to STL
    output_file = "austin_keychain.stl"
    keychain.export(output_file, file_type='stl')
    
    # Display statistics
    print()
    print("=" * 50)
    print("KEYCHAIN SPECIFICATIONS")
    print("=" * 50)
    print(f"Output File:        {output_file}")
    print(f"Dimensions:         50mm x 20mm x 3mm (plus 1mm text)")
    print(f"Text:               AUSTIN (embossed)")
    print(f"Keyring Hole:       5mm diameter, 5mm from right edge")
    print(f"Triangles:          {len(keychain.faces)}")
    print(f"Vertices:           {len(keychain.vertices)}")
    print(f"Volume:             {keychain.volume:.2f} mm³")
    print(f"Surface Area:       {keychain.area:.2f} mm²")
    print(f"Bounding Box:       {keychain.extents}")
    print()
    print("=" * 50)
    print("✓ STL file generated successfully!")
    print("✓ Ready for 3D printing (FDM or resin)")
    print("=" * 50)
    
    # Additional printing recommendations
    print()
    print("PRINTING RECOMMENDATIONS:")
    print("- Layer height: 0.1-0.2mm for FDM")
    print("- Supports: Not required")
    print("- Orientation: Flat on build plate")
    print("- Material: PLA, PETG, ABS, or resin")
    print("- Estimated print time: 15-30 minutes (depending on printer)")


if __name__ == "__main__":
    main()
