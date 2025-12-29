# Austin Keychain - 3D Printable Design

A customized 3D printable keychain featuring the text "Austin" in a clean, modern design.

## Design Specifications

- **Dimensions:** 50mm × 20mm × 3mm (base thickness)
- **Text:** "AUSTIN" embossed 1mm above the surface
- **Keyring Hole:** 5mm diameter, positioned 5mm from the right edge
- **Style:** Modern, geometric text design
- **Format:** STL (binary)

## Files

- `austin_keychain.stl` - Ready-to-print STL file
- `generate_keychain_final.py` - Python script to generate the STL file
- `README.md` - This documentation file

## 3D Printing Guidelines

### Recommended Settings

- **Layer Height:** 0.1-0.2mm for FDM printers
- **Infill:** 20-50% (100% for maximum durability)
- **Supports:** Not required
- **Build Plate Adhesion:** Brim or raft recommended for better adhesion
- **Print Orientation:** Lay flat on the build plate with text facing up

### Material Compatibility

This design works well with:
- **PLA** - Easy to print, good for most uses
- **PETG** - More durable, better for outdoor use
- **ABS** - Strong and heat-resistant
- **Resin** - Excellent detail and smooth finish

### Estimated Print Time

- **FDM Printers:** 15-30 minutes (depending on printer speed and quality settings)
- **Resin Printers:** 20-40 minutes

## Technical Details

- **Triangles:** 360
- **Vertices:** 206
- **Volume:** ~3,065 mm³
- **Surface Area:** ~2,923 mm²

## Regenerating the STL

If you want to modify or regenerate the design:

```bash
python3 generate_keychain_final.py
```

### Requirements

```bash
pip install trimesh manifold3d
```

## Design Features

1. **Rectangular Base:** Clean 50mm × 20mm rectangular shape, 3mm thick for durability
2. **Embossed Text:** "AUSTIN" text raised 1mm above the surface for excellent visibility
3. **Functional Hole:** 5mm diameter hole perfectly sized for standard keyring attachments
4. **Print-Friendly:** No overhangs, no supports needed, optimized for FDM and resin printing

## License

This design is provided as-is for personal and educational use.

## Modification Tips

To customize the keychain:
- Edit `generate_keychain_final.py` to change dimensions, text, or hole size
- The text can be modified by changing the letter generation code
- Adjust `text_depth` parameter to make text more or less prominent
- Change `length`, `width`, or `height` for different base dimensions

## Quality Assurance

✅ Mesh validated and optimized
✅ Suitable for FDM printers
✅ Suitable for resin printers
✅ No supports required
✅ Manifold geometry for clean boolean operations
✅ Tested dimensions within standard keychain sizes

---

**Created:** 2025
**Format:** STL Binary
**Software:** Python + Trimesh
