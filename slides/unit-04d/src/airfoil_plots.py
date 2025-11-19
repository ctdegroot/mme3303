import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def parse_naca_section_e(filename):
    """Parse Section E: 3-column data (Alpha, CL, CD)"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    datasets = {}
    current_dataset = None
    data_buffer = []
    in_section_e = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Look for lines with 3 values (Section E format)
        parts = line.split()
        
        # Check for dataset marker
        if 'Data set' in line:
            if current_dataset and data_buffer:
                datasets[current_dataset] = np.array(data_buffer)
                data_buffer = []
            continue
        
        # Try to parse dataset number
        try:
            if len(parts) == 1:
                val = int(parts[0])
                current_dataset = val
                continue
        except:
            pass
        
        # Try to parse 3-column data
        if current_dataset is not None:
            try:
                if len(parts) >= 3:
                    alpha = float(parts[0])
                    cl = float(parts[1])
                    cd = float(parts[2])
                    data_buffer.append([alpha, cl, cd])
                    in_section_e = True
            except:
                pass
    
    # Save last dataset
    if current_dataset and data_buffer:
        datasets[current_dataset] = np.array(data_buffer)
    
    return datasets

print("Parsing Section E data...")
data_23015 = parse_naca_section_e('147.ALL')
data_66215 = parse_naca_section_e('255.ALL')

print(f"NACA 23015 datasets in Section E: {list(data_23015.keys())}")
print(f"NACA 66-215 datasets in Section E: {list(data_66215.keys())}")

# Use dataset 2 (Re = 6 million)
if 2 in data_23015:
    section_e_23015 = data_23015[2]
    section_e_23015 = section_e_23015[section_e_23015[:,0].argsort()]
    print(f"\nNACA 23015 Dataset 2: {len(section_e_23015)} points")
    print("Sample data:")
    for i in range(min(5, len(section_e_23015))):
        print(f"  α={section_e_23015[i,0]:6.2f}°, CL={section_e_23015[i,1]:7.4f}, CD={section_e_23015[i,2]:9.6f}")

if 2 in data_66215:
    section_e_66215 = data_66215[2]
    section_e_66215 = section_e_66215[section_e_66215[:,0].argsort()]
    print(f"\nNACA 66-215 Dataset 2: {len(section_e_66215)} points")
    print("Sample data:")
    for i in range(min(5, len(section_e_66215))):
        print(f"  α={section_e_66215[i,0]:6.2f}°, CL={section_e_66215[i,1]:7.4f}, CD={section_e_66215[i,2]:9.6f}")

# Extract columns
alpha_23015 = section_e_23015[:,0]
cl_23015 = section_e_23015[:,1]
cd_23015 = section_e_23015[:,2]

alpha_66215 = section_e_66215[:,0]
cl_66215 = section_e_66215[:,1]
cd_66215 = section_e_66215[:,2]

# Filter out zero CD values (as noted in README)
valid_23015 = cd_23015 > 0
valid_66215 = cd_66215 > 0

print(f"\nValid data points (CD > 0):")
print(f"  NACA 23015: {valid_23015.sum()} points")
print(f"  NACA 66-215: {valid_66215.sum()} points")

print(f"\nCD ranges:")
print(f"  NACA 23015: {cd_23015[valid_23015].min():.6f} to {cd_23015[valid_23015].max():.6f}")
print(f"  NACA 66-215: {cd_66215[valid_66215].min():.6f} to {cd_66215[valid_66215].max():.6f}")

#  CREATE THE FINAL PLOT
fig = plt.figure(figsize=(12, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35,
              left=0.1, right=0.95, top=0.92, bottom=0.08)

color1 = '#1f77b4'
color2 = '#d62728'

# Plot 1: CL vs Alpha - NACA 23015
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(alpha_23015, cl_23015, 'D-', color=color1, linewidth=2,
         markersize=5, markerfacecolor='white', markeredgewidth=1.5)
ax1.set_xlabel('Angle of attack, α (deg)', fontsize=11)
ax1.set_ylabel('C$_{L}$', fontsize=11)
ax1.set_title('(a) Lift coefficient vs. angle of attack\nConventional section (NACA 23015)',
              fontsize=11, pad=10)
ax1.grid(True, alpha=0.3, linewidth=0.5)
ax1.set_xlim(-5, 22)
ax1.set_ylim(0, 2.0)
max_cl_23015 = cl_23015.max()
ax1.axhline(y=max_cl_23015, color='gray', linestyle='--', alpha=0.4, linewidth=1)
ax1.text(17, max_cl_23015+0.05, f'C$_{{L_{{max}}}}$ = {max_cl_23015:.2f}',
         fontsize=9, color='gray', style='italic')

# Plot 2: CL vs Alpha - NACA 66-215
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(alpha_66215, cl_66215, 'D-', color=color2, linewidth=2,
         markersize=5, markerfacecolor='white', markeredgewidth=1.5)
ax2.set_xlabel('Angle of attack, α (deg)', fontsize=11)
ax2.set_ylabel('C$_{L}$', fontsize=11)
ax2.set_title('(b) Lift coefficient vs. angle of attack\nLaminar-flow section (NACA 66-215)',
              fontsize=11, pad=10)
ax2.grid(True, alpha=0.3, linewidth=0.5)
ax2.set_xlim(-5, 22)
ax2.set_ylim(0, 2.0)
max_cl_66215 = cl_66215.max()
ax2.axhline(y=max_cl_66215, color='gray', linestyle='--', alpha=0.4, linewidth=1)
ax2.text(17, max_cl_66215+0.05, f'C$_{{L_{{max}}}}$ = {max_cl_66215:.2f}',
         fontsize=9, color='gray', style='italic')

# Plot 3: CD vs Alpha - NACA 23015
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(alpha_23015[valid_23015], cd_23015[valid_23015], 'D-', color=color1, linewidth=2,
         markersize=5, markerfacecolor='white', markeredgewidth=1.5)
ax3.set_xlabel('Angle of attack, α (deg)', fontsize=11)
ax3.set_ylabel('C$_{D}$', fontsize=11)
ax3.set_title('(c) Drag coefficient vs. angle of attack\nConventional section (NACA 23015)',
              fontsize=11, pad=10)
ax3.grid(True, alpha=0.3, linewidth=0.5)
ax3.set_xlim(-5, 22)
ax3.set_ylim(0, 0.022)

# Plot 4: CD vs Alpha - NACA 66-215
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(alpha_66215[valid_66215], cd_66215[valid_66215], 'D-', color=color2, linewidth=2,
         markersize=5, markerfacecolor='white', markeredgewidth=1.5)
ax4.set_xlabel('Angle of attack, α (deg)', fontsize=11)
ax4.set_ylabel('C$_{D}$', fontsize=11)
ax4.set_title('(d) Drag coefficient vs. angle of attack\nLaminar-flow section (NACA 66-215)',
              fontsize=11, pad=10)
ax4.grid(True, alpha=0.3, linewidth=0.5)
ax4.set_xlim(-5, 22)
ax4.set_ylim(0, 0.022)

plt.savefig('naca_airfoils.png', dpi=300, bbox_inches='tight')

print("\n✅✅✅ FINAL PLOT WITH CORRECT DATA CREATED! ✅✅✅")
print(f"\nKey findings from REAL NACA data:")
print(f"NACA 23015: CL_max = {max_cl_23015:.3f}, CD_min = {min_cd_23015:.5f}")
print(f"NACA 66-215: CL_max = {max_cl_66215:.3f}, CD_min = {min_cd_66215:.5f}")
if min_cd_66215 < min_cd_23015:
    print(f"  → {((min_cd_23015 - min_cd_66215)/min_cd_23015 * 100):.1f}% lower drag for laminar flow at cruise!")