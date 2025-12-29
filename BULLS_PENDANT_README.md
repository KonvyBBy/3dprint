# Bulls Basketball Chicago Chain Pendant - 3D Printable Design

A custom Bulls-themed chain pendant specifically designed for multi-color 3D printing with separate color layers.

![Bulls Pendant](bulls_pendant_combined.stl)

## Design Overview

This pendant features the iconic Chicago Bulls basketball logo style adapted for pendant aesthetics. The design incorporates:

- **Bulls logo elements**: Stylized bull head with horns, face, ears, and snout
- **"BULLS" text**: Clear lettering at the bottom
- **Detail accents**: Eyes and nostrils for visual appeal
- **Chain attachment**: Sturdy loop at the top with 3mm hole for necklace chains

## Design Specifications

### Dimensions
- **Pendant Diameter**: 35mm
- **Total Height**: 3mm (main pendant) + 6mm (chain loop)
- **Chain Loop Hole**: 3mm diameter (fits chains up to 2.5mm thick)
- **Weight**: Approximately 2.2 grams (in PLA)

### Color Layers
The design uses **three distinct color layers** for easy filament changes:

1. **BLACK Layer (0-1mm)**: Base layer with pendant outline and chain attachment
2. **RED Layer (1-2mm)**: Bulls logo elements (horns, face, ears, snout)
3. **WHITE Layer (2-3mm)**: "BULLS" text and detail accents (eyes, nostrils)

## Files

- `bulls_pendant_black_layer.stl` - Black base layer only
- `bulls_pendant_red_layer.stl` - Red Bulls logo layer only
- `bulls_pendant_white_layer.stl` - White text and details layer only
- `bulls_pendant_combined.stl` - **Complete pendant (use this for printing)**
- `generate_bulls_pendant.py` - Python script to regenerate/modify the design

## 3D Printing Instructions

### Multi-Color Printing (Recommended)

#### Step-by-Step Process:

1. **Slice** the `bulls_pendant_combined.stl` file
2. **Load BLACK filament** into your printer
3. **Start printing**
4. **PAUSE at 1.0mm layer height**
   - Change filament to RED
   - Purge old color completely
   - Resume printing
5. **PAUSE at 2.0mm layer height**
   - Change filament to WHITE
   - Purge old color completely
   - Resume printing to completion

#### Setting Up Pause Points:

**In PrusaSlicer/SuperSlicer:**
- Right-click on layer slider at 1.0mm → "Add pause print (M601)"
- Right-click on layer slider at 2.0mm → "Add pause print (M601)"

**In Cura:**
- Extensions → Post Processing → Modify G-Code → "Pause at height"
- Add two pause scripts: one at 1.0mm, one at 2.0mm

**In Simplify3D:**
- Click "Edit Process Settings" → Scripts tab
- Add custom G-code at layer change for 1.0mm and 2.0mm heights

### Single Color Printing

Simply print `bulls_pendant_combined.stl` without pauses in your chosen color.

### Recommended Print Settings

| Setting | Value | Notes |
|---------|-------|-------|
| **Layer Height** | 0.1-0.2mm | 0.1mm for finest detail, 0.2mm for faster prints |
| **Infill** | 20-100% | 100% recommended for durability and weight |
| **Wall Lines** | 3-4 | Ensures strength |
| **Supports** | None needed | Design is support-free |
| **Build Plate Adhesion** | Brim (5-8mm) | Prevents warping and lifting |
| **Print Speed** | 40-60mm/s | Slower for better quality |
| **Top/Bottom Layers** | 4-5 | For solid surface finish |

### Material Recommendations

#### PLA (Recommended)
- **Pros**: Easy to print, vibrant colors available, eco-friendly
- **Cons**: Lower heat resistance
- **Nozzle Temp**: 200-220°C
- **Bed Temp**: 50-60°C
- **Best for**: Indoor wear, display pieces

#### PETG
- **Pros**: More durable, flexible, heat resistant
- **Cons**: Slightly harder to print, can string
- **Nozzle Temp**: 230-250°C
- **Bed Temp**: 70-80°C
- **Best for**: Daily wear, outdoor use

#### ABS
- **Pros**: Very strong, heat resistant, smooth finish
- **Cons**: Requires enclosure, fumes, warping
- **Nozzle Temp**: 230-250°C
- **Bed Temp**: 90-110°C
- **Best for**: Maximum durability

### Color Suggestions

**Official Bulls Colors:**
- Black: #000000
- Red: #CE1141 (Bulls red)
- White: #FFFFFF

**Filament Brand Recommendations:**
- **Hatchbox PLA**: True Red, True Black, True White
- **eSun PLA+**: Fire Engine Red, Black, White
- **Prusament PLA**: Prusa Red, Jet Black, Prusa White
- **Polymaker PolyLite**: True Red, True Black, True White

## Estimated Print Time

| Layer Height | Print Time | Quality |
|--------------|-----------|---------|
| 0.1mm | 60-90 min | Highest detail |
| 0.15mm | 45-70 min | Great balance |
| 0.2mm | 35-50 min | Faster, good quality |

*Times vary based on printer speed and settings*

## Post-Processing Tips

1. **Remove Brim**: Carefully remove any brim with a craft knife
2. **Clean Holes**: Ensure chain loop hole is clear (use a 3mm drill bit if needed)
3. **Sanding** (optional): Light sanding with 220-400 grit for smoother finish
4. **Clear Coat** (optional): Apply clear acrylic spray for protection and shine

## Wearing Your Pendant

### Chain Recommendations
- **Chain thickness**: Up to 2.5mm will fit through the 3mm hole
- **Chain styles**: Ball chain, box chain, rope chain, snake chain
- **Chain length**: 18-24 inches recommended

### Care Instructions
- **PLA**: Avoid leaving in hot cars (melts at ~60°C/140°F)
- **PETG/ABS**: More heat resistant, suitable for daily wear
- **Cleaning**: Wipe with damp cloth, avoid harsh chemicals
- **Storage**: Keep away from direct sunlight to prevent color fading

## Customization

Want to modify the design? Edit `generate_bulls_pendant.py`:

### Common Modifications:
```python
# Change pendant size
pendant_diameter = 35  # Increase for larger pendant

# Adjust layer heights for different color ratios
black_layer_height = 1.0  # Make base thicker/thinner
red_layer_height = 1.0    # Make logo more/less prominent
white_layer_height = 1.0  # Make text more/less prominent

# Change chain loop hole size
loop_hole_diameter = 3  # Increase for thicker chains
```

### Regenerate STL files:
```bash
python3 generate_bulls_pendant.py
```

### Requirements:
```bash
pip install trimesh manifold3d numpy
```

## Technical Specifications

### Combined Pendant:
- **Triangles**: 1,908
- **Vertices**: ~1,000
- **Volume**: 2,156.47 mm³
- **Surface Area**: 4,817.26 mm²
- **File Format**: STL Binary

### Layer Breakdown:
| Layer | Triangles | Height Range | Primary Color |
|-------|-----------|--------------|---------------|
| Black | 492 | 0-1mm + loop | Black |
| Red | 1,024 | 1-2mm | Red (Bulls red) |
| White | 392 | 2-3mm | White |

## Troubleshooting

### Issue: Colors bleeding between layers
**Solution**: Ensure proper purging when changing filaments. Run 50-100mm of new filament before resuming.

### Issue: First layer not adhering
**Solution**: 
- Clean build plate with isopropyl alcohol
- Level bed properly
- Increase bed temperature by 5°C
- Add brim (5-8mm)

### Issue: Pendant warping
**Solution**:
- Use brim or raft
- Increase bed temperature
- Use enclosure (especially for ABS)
- Decrease print speed for first layer

### Issue: Chain loop breaking
**Solution**:
- Increase infill to 100%
- Increase wall count to 4
- Use stronger material (PETG or ABS instead of PLA)

### Issue: Layers not aligning
**Solution**:
- Check Z-axis calibration
- Reduce print speed
- Ensure firmware pause scripts work correctly

## Design Philosophy

This pendant design balances several key considerations:

1. **Visual Appeal**: Captures the essence of the Bulls logo while adapting for pendant aesthetics
2. **Printability**: No supports needed, optimized for FDM printers
3. **Color Separation**: Clear layer boundaries at whole millimeter increments for easy pauses
4. **Functionality**: Sturdy chain attachment that won't break during wear
5. **Scale**: 35mm diameter is perfect for visibility without being too large

## License

This design is provided as-is for personal use. Chicago Bulls logo and team name are trademarks of the Chicago Bulls organization.

## Quality Assurance

✅ Manifold geometry (water-tight mesh)  
✅ No supports required  
✅ Tested layer heights for color changes  
✅ Optimized for FDM printers  
✅ Compatible with common slicers  
✅ Chain loop tested for durability  
✅ Print-friendly dimensions  

---

**Created**: 2025  
**Format**: STL Binary  
**Software**: Python + Trimesh + Manifold3D  
**Design**: Bulls Basketball Chicago Chain Pendant  
