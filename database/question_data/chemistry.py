# 100 High-Quality Conceptual & Numerical Chemistry MCQs

CHEMISTRY_QUESTIONS = [
    # 1 - 10: Atomic Structure & Periodic Trends
    {
        "question_text": "What is the maximum number of electrons that can be accommodated in an atom with quantum numbers n = 3 and l = 1?",
        "option_a": "6",
        "option_b": "2",
        "option_c": "10",
        "option_d": "18",
        "correct_option": "A",
        "explanation": "n = 3 and l = 1 specifies the 3p subshell. The 3p subshell has 3 orbitals (m = -1, 0, +1), holding a maximum of 2 * 3 = 6 electrons.",
        "difficulty": "High"
    },
    {
        "question_text": "Which element has the highest first ionization enthalpy among the following?",
        "option_a": "Helium (He)",
        "option_b": "Neon (Ne)",
        "option_c": "Fluorine (F)",
        "option_d": "Argon (Ar)",
        "correct_option": "A",
        "explanation": "Helium has the smallest atomic size and a stable 1s^2 noble gas configuration, giving it the highest first ionization energy of all elements (2372 kJ/mol).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the wavelength of a photon emitted during a transition from n = 2 to n = 1 in a Hydrogen atom? (Rydberg constant R_H = 1.097 x 10^7 m^-1)",
        "option_a": "121.5 nm",
        "option_b": "91.2 nm",
        "option_c": "656.3 nm",
        "option_d": "486.1 nm",
        "correct_option": "A",
        "explanation": "1/lambda = R_H * (1/1^2 - 1/2^2) = R_H * (3/4) => lambda = 4 / (3 * 1.097 x 10^7) = 1.215 x 10^-7 m = 121.5 nm (Lyman-alpha line).",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following species is isoelectronic with CO (Carbon Monoxide)?",
        "option_a": "N2",
        "option_b": "O2",
        "option_c": "NO",
        "option_d": "CO2",
        "correct_option": "A",
        "explanation": "CO has 6 + 8 = 14 electrons. N2 also has 7 + 7 = 14 electrons, making CO and N2 isoelectronic.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the shape and hybridization of the central atom in SF6 (Sulfur Hexafluoride)?",
        "option_a": "Octahedral, sp3d2",
        "option_b": "Trigonal bipyramidal, sp3d",
        "option_c": "Square planar, sp3d2",
        "option_d": "Tetrahedral, sp3",
        "correct_option": "A",
        "explanation": "SF6 has 6 bonding pairs and 0 lone pairs on Sulfur (steric number 6), resulting in sp3d2 hybridization and an octahedral geometry.",
        "difficulty": "High"
    },
    {
        "question_text": "According to Molecular Orbital Theory, what is the bond order of the Oxygen molecule (O2)?",
        "option_a": "2.0",
        "option_b": "1.5",
        "option_c": "2.5",
        "option_d": "3.0",
        "correct_option": "A",
        "explanation": "O2 has 16 electrons: (sigma1s)^2 (sigma*1s)^2 (sigma2s)^2 (sigma*2s)^2 (sigma2pz)^2 (pi2px)^2 (pi2py)^2 (pi*2px)^1 (pi*2py)^1. Bond order = (10 - 6) / 2 = 2.0.",
        "difficulty": "High"
    },
    {
        "question_text": "Which compound exhibits the highest boiling point due to extensive intermolecular hydrogen bonding?",
        "option_a": "H2O",
        "option_b": "H2S",
        "option_c": "HF",
        "option_d": "NH3",
        "correct_option": "A",
        "explanation": "H2O forms a 3D hydrogen-bonded network (2 hydrogen donors and 2 lone pair acceptors per molecule), resulting in a higher boiling point (100 C) than HF or NH3.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the formal charge on the central Oxygen atom in Ozone (O3)?",
        "option_a": "+1",
        "option_b": "0",
        "option_c": "-1",
        "option_d": "+2",
        "correct_option": "A",
        "explanation": "Central oxygen in O3 has 6 valence electrons, 1 lone pair (2 non-bonding e-), and 3 bonds (6 bonding e-). Formal charge = 6 - 2 - (6/2) = +1.",
        "difficulty": "High"
    },
    {
        "question_text": "Which molecule has a non-zero net dipole moment?",
        "option_a": "NH3",
        "option_b": "BF3",
        "option_c": "CCl4",
        "option_d": "CO2",
        "correct_option": "A",
        "explanation": "NH3 has a trigonal pyramidal shape with a lone pair, giving a net dipole moment (1.47 D). BF3, CCl4, and CO2 are symmetrical with zero net dipole moment.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the correct order of increasing ionic radius among the isoelectronic species: N^3-, O^2-, F-, Na+?",
        "option_a": "Na+ < F- < O^2- < N^3-",
        "option_b": "N^3- < O^2- < F- < Na+",
        "option_c": "F- < Na+ < O^2- < N^3-",
        "option_d": "Na+ < N^3- < O^2- < F-",
        "correct_option": "A",
        "explanation": "For isoelectronic species, higher nuclear charge Z pulls electrons tighter, reducing ionic radius. Na+ (Z=11) < F- (Z=9) < O^2- (Z=8) < N^3- (Z=7).",
        "difficulty": "High"
    },

    # 11 - 20: Gas Laws, Thermodynamics & Equilibrium
    {
        "question_text": "Equal masses of H2 and O2 gases are mixed in an enclosed vessel at 27 degrees C. What is the partial pressure ratio of H2 to O2 in the vessel?",
        "option_a": "16 : 1",
        "option_b": "1 : 16",
        "option_c": "1 : 1",
        "option_d": "8 : 1",
        "correct_option": "A",
        "explanation": "Moles n = mass / Molar mass. n(H2) = m / 2, n(O2) = m / 32. Mole ratio n(H2)/n(O2) = (m/2) / (m/32) = 32 / 2 = 16 : 1. Partial pressure ratio equals mole ratio.",
        "difficulty": "High"
    },
    {
        "question_text": "For a reversible reaction A(g) + 2 B(g) <=> C(g) + D(g), delta H = -50 kJ/mol. Which condition favors maximum yield of C at equilibrium?",
        "option_a": "High pressure and low temperature",
        "option_b": "Low pressure and high temperature",
        "option_c": "High pressure and high temperature",
        "option_d": "Low pressure and low temperature",
        "correct_option": "A",
        "explanation": "By Le Chatelier's principle: Exothermic reaction (delta H < 0) is favored by low temperature. Reactants have 3 moles of gas, products have 2 moles; higher pressure shifts equilibrium toward fewer gas moles (forward).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the pH of a 1.0 x 10^-8 M HCl aqueous solution at 25 degrees C?",
        "option_a": "6.98",
        "option_b": "8.00",
        "option_c": "7.00",
        "option_d": "6.00",
        "correct_option": "A",
        "explanation": "Total [H+] = [H+]_acid + [H+]_water = 10^-8 + 10^-7 = 1.1 x 10^-7 M. pH = -log(1.1 x 10^-7) = 7 - log(1.1) = 7 - 0.041 = 6.96 to 6.98.",
        "difficulty": "High"
    },
    {
        "question_text": "Calculate the solubility of AgCl in pure water at 25 degrees C given Ksp(AgCl) = 1.0 x 10^-10.",
        "option_a": "1.0 x 10^-5 M",
        "option_b": "1.0 x 10^-10 M",
        "option_c": "2.0 x 10^-5 M",
        "option_d": "1.0 x 10^-4 M",
        "correct_option": "A",
        "explanation": "AgCl(s) <=> Ag+(aq) + Cl-(aq). Ksp = s * s = s^2 = 1.0 x 10^-10 => s = sqrt(1.0 x 10^-10) = 1.0 x 10^-5 M.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the Gibbs free energy change delta G degrees for a reaction with cell potential E degrees_cell = +1.10 V transferring n = 2 moles of electrons? (F = 96485 C/mol)",
        "option_a": "-212.3 kJ/mol",
        "option_b": "+212.3 kJ/mol",
        "option_c": "-106.1 kJ/mol",
        "option_d": "-424.6 kJ/mol",
        "correct_option": "A",
        "explanation": "delta G degrees = -n * F * E degrees = -2 * 96485 * 1.10 = -212,267 J/mol = -212.3 kJ/mol.",
        "difficulty": "High"
    },
    {
        "question_text": "A first-order reaction has a rate constant k = 6.93 x 10^-3 s^-1. What is the half-life t_1/2 of the reaction?",
        "option_a": "100 s",
        "option_b": "50 s",
        "option_c": "200 s",
        "option_d": "10 s",
        "correct_option": "A",
        "explanation": "t_1/2 = 0.693 / k = 0.693 / (6.93 x 10^-3) = 100 seconds.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the van 't Hoff factor (i) for a 0.1 M BaCl2 aqueous solution assuming complete dissociation?",
        "option_a": "3",
        "option_b": "2",
        "option_c": "1",
        "option_d": "4",
        "correct_option": "A",
        "explanation": "BaCl2 dissociates completely into 1 Ba^2+ and 2 Cl- ions, giving i = 1 + 2 = 3 ions per formula unit.",
        "difficulty": "High"
    },
    {
        "question_text": "In the van der Waals gas equation (P + a/V^2)(V - b) = RT, what do the constants 'a' and 'b' represent respectively?",
        "option_a": "Intermolecular attraction forces; Effective molecular volume",
        "option_b": "Effective molecular volume; Intermolecular attraction forces",
        "option_c": "Kinetic energy; Molecular mass",
        "option_d": "Gas pressure; Temperature coefficient",
        "correct_option": "A",
        "explanation": "'a' corrects for attractive forces between gas molecules; 'b' corrects for the finite excluded volume of the molecules.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the oxidation state of Chromium in Potassium Dichromate (K2Cr2O7)?",
        "option_a": "+6",
        "option_b": "+3",
        "option_c": "+7",
        "option_d": "+5",
        "correct_option": "A",
        "explanation": "2(+1) + 2(Cr) + 7(-2) = 0 => 2 + 2Cr - 14 = 0 => 2Cr = 12 => Cr = +6.",
        "difficulty": "High"
    },
    {
        "question_text": "Which buffer solution resists pH changes upon addition of small amounts of acid or base?",
        "option_a": "CH3COOH + CH3COONa",
        "option_b": "HCl + NaCl",
        "option_c": "NaOH + NaCl",
        "option_d": "HNO3 + KNO3",
        "correct_option": "A",
        "explanation": "An acidic buffer consists of a weak acid (CH3COOH) and its conjugate base salt (CH3COONa).",
        "difficulty": "High"
    },

    # 21 - 30: Electrochemistry & Kinetics
    {
        "question_text": "During the electrolysis of molten NaCl, what products are liberated at the cathode and anode respectively?",
        "option_a": "Sodium metal at cathode; Chlorine gas at anode",
        "option_b": "Chlorine gas at cathode; Sodium metal at anode",
        "option_c": "Hydrogen gas at cathode; Oxygen gas at anode",
        "option_d": "Sodium metal at cathode; Oxygen gas at anode",
        "correct_option": "A",
        "explanation": "At cathode (reduction): Na+ + e- -> Na(l). At anode (oxidation): 2 Cl- -> Cl2(g) + 2 e-.",
        "difficulty": "High"
    },
    {
        "question_text": "For a zero-order reaction A -> Products, if the initial concentration is doubled from [A]0 to 2[A]0, how does the half-life t_1/2 change?",
        "option_a": "Half-life doubles",
        "option_b": "Half-life remains unchanged",
        "option_c": "Half-life is halved",
        "option_d": "Half-life quadruples",
        "correct_option": "A",
        "explanation": "For a zero-order reaction, t_1/2 = [A]0 / (2k). Half-life is directly proportional to initial concentration [A]0.",
        "difficulty": "High"
    },
    {
        "question_text": "According to the Arrhenius equation k = A * exp(-Ea / RT), a plot of ln(k) versus 1/T yields a straight line with slope equal to:",
        "option_a": "-Ea / R",
        "option_b": "Ea / R",
        "option_c": "-Ea",
        "option_d": "A / R",
        "correct_option": "A",
        "explanation": "Taking natural log: ln(k) = ln(A) - (Ea / R) * (1/T). Comparing to y = c + m x gives slope m = -Ea / R.",
        "difficulty": "High"
    },
    {
        "question_text": "How many Coulombs of electricity are required to reduce 1 mole of Cr2O7^2- to Cr^3+ ions in acidic medium?",
        "option_a": "6 Faraday (578,910 C)",
        "option_b": "3 Faraday (289,455 C)",
        "option_c": "1 Faraday (96,485 C)",
        "option_d": "2 Faraday (192,970 C)",
        "correct_option": "A",
        "explanation": "Cr2O7^2- + 14 H+ + 6 e- -> 2 Cr^3+ + 7 H2O. 1 mole of Cr2O7^2- consumes 6 moles of electrons = 6 Faraday.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the order of reaction for radioactive decay processes?",
        "option_a": "First order",
        "option_b": "Zero order",
        "option_c": "Second order",
        "option_d": "Fractional order",
        "correct_option": "A",
        "explanation": "All nuclear radioactive decay reactions follow strict first-order kinetics rate = lambda * N.",
        "difficulty": "High"
    },
    {
        "question_text": "The molar conductivity of a weak electrolyte at infinite dilution (Lambda^0_m) can be calculated using:",
        "option_a": "Kohlrausch's Law of Independent Migration of Ions",
        "option_b": "Faraday's First Law",
        "option_c": "Ostwald's Dilution Law",
        "option_d": "Henry's Law",
        "correct_option": "A",
        "explanation": "Kohlrausch's law states that at infinite dilution, each ion makes a definite individual contribution to total molar conductivity.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following colligative properties is most suitable for determining the molar mass of macromolecules like proteins and polymers?",
        "option_a": "Osmotic pressure",
        "option_b": "Relative lowering of vapor pressure",
        "option_c": "Elevation of boiling point",
        "option_d": "Depression of freezing point",
        "correct_option": "A",
        "explanation": "Osmotic pressure measurements produce measurable values at room temperature even for very dilute solutions of high molar mass polymer samples.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the osmotic pressure pi of a 0.02 M glucose solution at 300 K? (R = 0.0821 L atm / mol K)",
        "option_a": "0.493 atm",
        "option_b": "0.246 atm",
        "option_c": "0.986 atm",
        "option_d": "1.230 atm",
        "correct_option": "A",
        "explanation": "pi = C * R * T = (0.02 mol/L) * (0.0821 L atm/mol K) * (300 K) = 0.4926 atm = 0.493 atm.",
        "difficulty": "High"
    },
    {
        "question_text": "In a reaction A + B -> Products, doubling [A] quadruples the rate, while doubling [B] leaves the rate unchanged. What is the overall order of the reaction?",
        "option_a": "2",
        "option_b": "1",
        "option_c": "3",
        "option_d": "0",
        "correct_option": "A",
        "explanation": "Rate = k [A]^x [B]^y. 4 = 2^x => x = 2. 1 = 2^y => y = 0. Overall order = 2 + 0 = 2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the standard cell emf E degrees_cell for the cell Zn(s) | Zn^2+(aq) || Cu^2+(aq) | Cu(s), given E degrees(Zn^2+/Zn) = -0.76 V and E degrees(Cu^2+/Cu) = +0.34 V?",
        "option_a": "+1.10 V",
        "option_b": "+0.42 V",
        "option_c": "-1.10 V",
        "option_d": "-0.42 V",
        "correct_option": "A",
        "explanation": "E degrees_cell = E degrees_cathode - E degrees_anode = +0.34 V - (-0.76 V) = +1.10 V.",
        "difficulty": "High"
    },

    # 31 - 40: Organic Chemistry Fundamentals & Reaction Mechanisms
    {
        "question_text": "Which carbocation is the most stable among the following?",
        "option_a": "(CH3)3C+ (tert-Butyl cation)",
        "option_b": "(CH3)2CH+ (Isopropyl cation)",
        "option_c": "CH3CH2+ (Ethyl cation)",
        "option_d": "CH3+ (Methyl cation)",
        "correct_option": "A",
        "explanation": "The tert-butyl cation is tertiary with 9 hyperconjugative alpha-hydrogens and 3 electron-donating methyl groups (+I effect), giving it maximum stability.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the IUPAC name of the compound CH3-CH(OH)-CH2-COOH?",
        "option_a": "3-hydroxybutanoic acid",
        "option_b": "2-hydroxybutanoic acid",
        "option_c": "3-hydroxybutyric acid",
        "option_d": "1-carboxypropan-2-ol",
        "correct_option": "A",
        "explanation": "Numbering starts at the -COOH carbon (C1). C3 holds the -OH group. IUPAC name is 3-hydroxybutanoic acid.",
        "difficulty": "High"
    },
    {
        "question_text": "Which mechanism dominates in the reaction of tert-butyl bromide with aqueous KOH to yield tert-butyl alcohol?",
        "option_a": "SN1 mechanism",
        "option_b": "SN2 mechanism",
        "option_c": "E2 mechanism",
        "option_d": "Electrophilic addition",
        "correct_option": "A",
        "explanation": "Tertiary alkyl halides undergo nucleophilic substitution primarily via the SN1 pathway through a stable tertiary carbocation intermediate.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following compounds fulfills Huckel's rule of aromaticity (4n + 2 pi electrons, planar conjugated)?",
        "option_a": "Benzene (C6H6)",
        "option_b": "Cyclooctatetraene (C8H8)",
        "option_c": "Cyclobutadiene (C4H4)",
        "option_d": "Cyclopentadienyl cation (C5H5+)",
        "correct_option": "A",
        "explanation": "Benzene is planar, fully conjugated, and contains 6 pi electrons (4n + 2 where n=1), making it aromatic.",
        "difficulty": "High"
    },
    {
        "question_text": "An alkene on ozonolysis (O3 followed by Zn/H2O) yields Propanone and Ethanal. What is the IUPAC name of the original alkene?",
        "option_a": "2-methylbut-2-ene",
        "option_b": "2-methylbut-1-ene",
        "option_c": "pent-2-ene",
        "option_d": "3-methylbut-1-ene",
        "correct_option": "A",
        "explanation": "Propanone (CH3-CO-CH3) + Ethanal (CH3-CHO) recombine at carbonyl carbons: (CH3)2C=CH-CH3 (2-methylbut-2-ene).",
        "difficulty": "High"
    },
    {
        "question_text": "Which reagent distinguishes an Aldehyde from a Ketone by forming a silver mirror on the tube walls?",
        "option_a": "Tollens' reagent [Ammoniacal AgNO3]",
        "option_b": "Fehling's solution B",
        "option_c": "Grignard reagent",
        "option_d": "Lucas reagent",
        "correct_option": "A",
        "explanation": "Tollens' reagent oxidizes aldehydes to carboxylate ions while reducing Ag+ to metallic silver (silver mirror test). Ketones do not react.",
        "difficulty": "High"
    },
    {
        "question_text": "What major product is obtained when Phenol is treated with Concentrated HNO3 in presence of Concentrated H2SO4?",
        "option_a": "2,4,6-trinitrophenol (Picric Acid)",
        "option_b": "o-nitrophenol only",
        "option_c": "p-nitrophenol only",
        "option_d": "Nitrobenzene",
        "correct_option": "A",
        "explanation": "Strong nitration of phenol with conc. HNO3/H2SO4 introduces nitro groups at both ortho and para positions, forming 2,4,6-trinitrophenol (Picric acid).",
        "difficulty": "High"
    },
    {
        "question_text": "Which alcohol reacts fastest with Lucas reagent (Conc. HCl + anhydrous ZnCl2) to give immediate turbidity at room temperature?",
        "option_a": "2-methylpropan-2-ol (tert-Butyl alcohol)",
        "option_b": "Propan-2-ol (Isopropyl alcohol)",
        "option_c": "Propan-1-ol (n-Propyl alcohol)",
        "option_d": "Ethanol",
        "correct_option": "A",
        "explanation": "Tertiary alcohols react immediately with Lucas reagent via fast SN1 formation of insoluble tertiary alkyl chloride turbidity.",
        "difficulty": "High"
    },
    {
        "question_text": "Which amine gives a foul-smelling isocyanide when heated with chloroform (CHCl3) and ethanolic KOH?",
        "option_a": "Aniline (Primary aromatic amine)",
        "option_b": "N-methylaniline (Secondary amine)",
        "option_c": "N,N-dimethylaniline (Tertiary amine)",
        "option_d": "Triethylamine",
        "correct_option": "A",
        "explanation": "The Carbylamine test (isocyanide test) is specific to primary aliphatic and aromatic amines (like Aniline).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the product formed when Benzene reacts with Acetyl Chloride (CH3COCl) in the presence of anhydrous AlCl3?",
        "option_a": "Acetophenone",
        "option_b": "Benzaldehyde",
        "option_c": "Toluene",
        "option_d": "Benzoic acid",
        "correct_option": "A",
        "explanation": "Friedel-Crafts acylation of benzene with CH3COCl/AlCl3 yields Acetophenone (C6H5COCH3).",
        "difficulty": "High"
    },

    # 41 - 50: Inorganic Chemistry & Coordination Compounds
    {
        "question_text": "What is the IUPAC name of the coordination compound [Co(NH3)5(Cl)]Cl2?",
        "option_a": "Pentaamminechloridocobalt(III) chloride",
        "option_b": "Pentamminedichlorocobalt(II)",
        "option_c": "Chloropentaamminecobalt(II) chloride",
        "option_d": "Pentaamminecobalt(III) trichloride",
        "correct_option": "A",
        "explanation": "Ligands in alphabetical order: pentaammine (5 NH3) chlorido (1 Cl^-), central metal cobalt(III), counter ion chloride.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the magnetic spin-only moment (in Bohr Magnetons, BM) of [Fe(CN)6]^3- ion? (Fe^3+ is low spin, d^5)",
        "option_a": "1.73 BM",
        "option_b": "5.92 BM",
        "option_c": "3.87 BM",
        "option_d": "4.90 BM",
        "correct_option": "A",
        "explanation": "CN- is a strong field ligand. Low spin d^5 has 1 unpaired electron (n=1). Spin-only moment mu = sqrt(n(n+2)) = sqrt(1*3) = sqrt(3) = 1.73 BM.",
        "difficulty": "High"
    },
    {
        "question_text": "Which geometry and isomerism does the complex [Pt(NH3)2Cl2] display?",
        "option_a": "Square planar, Geometric (cis and trans) isomerism",
        "option_b": "Tetrahedral, Optical isomerism",
        "option_c": "Octahedral, Facial-meridional isomerism",
        "option_d": "Square planar, Optical isomerism",
        "correct_option": "A",
        "explanation": "Pt(II) complexes are square planar (d^8) and [Pt(NH3)2Cl2] forms cis-platin and trans-platin geometric isomers.",
        "difficulty": "High"
    },
    {
        "question_text": "According to Crystal Field Theory, what is the crystal field stabilization energy (CFSE) for a high-spin d^6 octahedral complex?",
        "option_a": "-0.4 Delta_o",
        "option_b": "-2.4 Delta_o",
        "option_c": "-1.2 Delta_o",
        "option_d": "-0.6 Delta_o",
        "correct_option": "A",
        "explanation": "High spin d^6 in octahedral field: t2g^4 eg^2. CFSE = 4(-0.4 Delta_o) + 2(+0.6 Delta_o) = -1.6 + 1.2 = -0.4 Delta_o.",
        "difficulty": "High"
    },
    {
        "question_text": "Which gas is primarily responsible for global warming (Greenhouse Effect)?",
        "option_a": "Carbon dioxide (CO2)",
        "option_b": "Sulfur dioxide (SO2)",
        "option_c": "Nitrogen oxide (NO)",
        "option_d": "Carbon monoxide (CO)",
        "correct_option": "A",
        "explanation": "CO2 absorbs infrared radiation reradiated from Earth's surface, making it the major anthropogenic greenhouse gas.",
        "difficulty": "High"
    },
    {
        "question_text": "Ozone layer depletion in the stratosphere is primarily catalyzed by radicals produced from:",
        "option_a": "Chlorofluorocarbons (CFCs)",
        "option_b": "Carbon dioxide",
        "option_c": "Methane gas",
        "option_d": "Sulfur hexafluoride",
        "correct_option": "A",
        "explanation": "UV radiation breaks down CFCs to release Chlorine radicals (Cl*), which catalytically decompose ozone O3 into O2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the hybridization of Xenon in Xenon Tetrafluoride (XeF4)?",
        "option_a": "sp3d2",
        "option_b": "sp3d",
        "option_c": "sp3",
        "option_d": "dsp2",
        "correct_option": "A",
        "explanation": "XeF4 has 4 bonding pairs and 2 lone pairs on Xenon (steric number 6), giving sp3d2 hybridization and square planar geometry.",
        "difficulty": "High"
    },
    {
        "question_text": "Which oxide of Nitrogen is a neutral paramagnetic gas containing an odd number of valence electrons?",
        "option_a": "Nitric oxide (NO)",
        "option_b": "Nitrous oxide (N2O)",
        "option_c": "Dinitrogen tetroxide (N2O4)",
        "option_d": "Dinitrogen pentoxide (N2O5)",
        "correct_option": "A",
        "explanation": "NO has 5 + 6 = 11 valence electrons (odd electron molecule), making it paramagnetic and neutral.",
        "difficulty": "High"
    },
    {
        "question_text": "Which halide of Sodium has the highest lattice energy?",
        "option_a": "NaF",
        "option_b": "NaCl",
        "option_c": "NaBr",
        "option_d": "NaI",
        "correct_option": "A",
        "explanation": "Lattice energy is inversely proportional to ionic radius sum (r+ + r-). F- is the smallest halide ion, giving NaF the highest lattice energy.",
        "difficulty": "High"
    },
    {
        "question_text": "In the extraction of Iron in a blast furnace, what acts as the chief reducing agent of Hematite (Fe2O3) at higher temperatures?",
        "option_a": "Carbon monoxide (CO)",
        "option_b": "Carbon dioxide (CO2)",
        "option_c": "Limestone (CaCO3)",
        "option_d": "Silica (SiO2)",
        "correct_option": "A",
        "explanation": "CO produced by incomplete combustion of coke reduces Fe2O3 to molten metallic iron: Fe2O3 + 3 CO -> 2 Fe + 3 CO2.",
        "difficulty": "High"
    },

    # 51 - 60: Physical Chemistry & Stoichiometry
    {
        "question_text": "How many moles of O2 gas are required to completely react with 2 moles of C3H8 (Propane) during complete combustion?",
        "option_a": "10 moles",
        "option_b": "5 moles",
        "option_c": "6 moles",
        "option_d": "8 moles",
        "correct_option": "A",
        "explanation": "C3H8 + 5 O2 -> 3 CO2 + 4 H2O. 1 mole propane requires 5 moles O2. 2 moles propane require 2 * 5 = 10 moles O2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the molality of a solution containing 20 g of NaOH (molar mass = 40 g/mol) dissolved in 500 g of water?",
        "option_a": "1.0 m",
        "option_b": "0.5 m",
        "option_c": "2.0 m",
        "option_d": "0.1 m",
        "correct_option": "A",
        "explanation": "Moles NaOH = 20 / 40 = 0.5 mol. Solvent mass = 0.5 kg. Molality m = 0.5 mol / 0.5 kg = 1.0 m.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the normality of a 0.5 M H2SO4 aqueous solution for complete neutralization?",
        "option_a": "1.0 N",
        "option_b": "0.5 N",
        "option_c": "0.25 N",
        "option_d": "2.0 N",
        "correct_option": "A",
        "explanation": "H2SO4 is a dibasic acid (n-factor = 2). Normality N = Molarity x n-factor = 0.5 * 2 = 1.0 N.",
        "difficulty": "High"
    },
    {
        "question_text": "According to Graham's Law of Effusion, the rate of effusion of a gas is inversely proportional to:",
        "option_a": "Square root of its molar mass",
        "option_b": "Its molar mass",
        "option_c": "Square of its molar mass",
        "option_d": "Cube root of its molar mass",
        "correct_option": "A",
        "explanation": "Graham's law states rate r is proportional to 1 / sqrt(Molar Mass).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the oxidation state of Phosphorus in Hypophosphorous acid (H3PO2)?",
        "option_a": "+1",
        "option_b": "+3",
        "option_c": "+5",
        "option_d": "-3",
        "correct_option": "A",
        "explanation": "3(+1) + P + 2(-2) = 0 => 3 + P - 4 = 0 => P = +1.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following undergoes aldol condensation when treated with dilute NaOH?",
        "option_a": "Ethanal (CH3CHO)",
        "option_b": "Benzaldehyde (C6H5CHO)",
        "option_c": "Formaldehyde (HCHO)",
        "option_d": "2,2-dimethylpropanal",
        "correct_option": "A",
        "explanation": "Aldol condensation requires carbonyl compounds possessing at least one alpha-hydrogen (Ethanal has 3 alpha-H atoms).",
        "difficulty": "High"
    },
    {
        "question_text": "Which test distinguishes Primary, Secondary, and Tertiary amines using Benzenesulfonyl Chloride?",
        "option_a": "Hinsberg test",
        "option_b": "Biuret test",
        "option_c": "Victor Meyer test",
        "option_d": "Iodoform test",
        "correct_option": "A",
        "explanation": "Hinsberg reagent (Benzenesulfonyl chloride) forms alkali-soluble sulfonamides with primary amines, alkali-insoluble with secondary, and does not react with tertiary amines.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the major organic product formed when Chlorobenzene is treated with Sodium in dry ether (Fittig reaction)?",
        "option_a": "Biphenyl (Diphenyl)",
        "option_b": "Toluene",
        "option_c": "Benzene",
        "option_d": "Phenol",
        "correct_option": "A",
        "explanation": "Fittig reaction: 2 C6H5Cl + 2 Na -> C6H5-C6H5 (Biphenyl) + 2 NaCl.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the shape of the Water molecule (H2O) according to VSEPR theory?",
        "option_a": "Bent / V-shaped (angle approx 104.5 degrees)",
        "option_b": "Linear (180 degrees)",
        "option_c": "Trigonal planar",
        "option_d": "Tetrahedral",
        "correct_option": "A",
        "explanation": "H2O has 2 bonding pairs and 2 lone pairs on oxygen (sp3 hybridized), giving a bent/V-shaped geometry with 104.5 degree bond angle.",
        "difficulty": "High"
    },
    {
        "question_text": "Which halogen forms the strongest hydrogen bond in its hydride?",
        "option_a": "Fluorine (HF)",
        "option_b": "Chlorine (HCl)",
        "option_c": "Bromine (HBr)",
        "option_d": "Iodine (HI)",
        "correct_option": "A",
        "explanation": "Fluorine is the most electronegative element, resulting in the strongest hydrogen bonding in HF.",
        "difficulty": "High"
    },

    # 61 - 70: Organic Reactions & Mechanisms
    {
        "question_text": "What is the main product of the reaction between Propene and HBr in the presence of Organic Peroxides (Anti-Markovnikov addition)?",
        "option_a": "1-bromopropane",
        "option_b": "2-bromopropane",
        "option_c": "1,2-dibromopropane",
        "option_d": "2-propanol",
        "correct_option": "A",
        "explanation": "In presence of peroxides, HBr adds to unsymmetrical alkenes via free radical mechanism following Anti-Markovnikov rule, yielding 1-bromopropane.",
        "difficulty": "High"
    },
    {
        "question_text": "Which reaction converts an Amide to a Primary Amine containing one fewer carbon atom?",
        "option_a": "Hofmann bromamide degradation",
        "option_b": "Reimer-Tiemann reaction",
        "option_c": "Kolbe reaction",
        "option_d": "Cannizzaro reaction",
        "correct_option": "A",
        "explanation": "Hofmann bromamide degradation treats an amide with Br2/NaOH to yield a primary amine with one carbon atom reduced.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the product formed when Salicylic Acid is treated with Acetic Anhydride in presence of Conc. H2SO4?",
        "option_a": "Aspirin (Acetylsalicylic acid)",
        "option_b": "Methyl salicylate",
        "option_c": "Phenyl salicylate",
        "option_d": "Benzoic acid",
        "correct_option": "A",
        "explanation": "Acetylation of the phenolic -OH group of salicylic acid by acetic anhydride yields Acetylsalicylic acid (Aspirin).",
        "difficulty": "High"
    },
    {
        "question_text": "Which compound does NOT undergo Cannizzaro reaction when treated with 50% NaOH?",
        "option_a": "Acetaldehyde (CH3CHO)",
        "option_b": "Formaldehyde (HCHO)",
        "option_c": "Benzaldehyde (C6H5CHO)",
        "option_d": "Trimethylacetaldehyde",
        "correct_option": "A",
        "explanation": "Cannizzaro reaction occurs ONLY in aldehydes lacking alpha-hydrogens. Acetaldehyde has 3 alpha-hydrogens, so it undergoes Aldol condensation instead.",
        "difficulty": "High"
    },
    {
        "question_text": "What product is formed when Ethanol is heated with excess Concentrated H2SO4 at 443 K (170 C)?",
        "option_a": "Ethene (CH2=CH2)",
        "option_b": "Diethyl ether (CH3CH2OCH2CH3)",
        "option_c": "Ethanal",
        "option_d": "Ethyl hydrogen sulfate",
        "correct_option": "A",
        "explanation": "Dehydration of ethanol with conc. H2SO4 at 443 K produces Ethene via intramolecular elimination.",
        "difficulty": "High"
    },
    {
        "question_text": "Which functional group gives a positive Iodoform test (yellow precipitate of CHI3 upon treatment with I2 and NaOH)?",
        "option_a": "CH3-C=O (Methyl ketone) or CH3-CH(OH)- group",
        "option_b": "Carboxylic acid group (-COOH)",
        "option_c": "Primary amine group (-NH2)",
        "option_d": "Ester group (-COOR)",
        "correct_option": "A",
        "explanation": "Compounds containing a CH3-C=O or CH3-CH(OH)- unit form triiodomethane (iodoform CHI3) yellow precipitate.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the hybrid state of carbon in Graphite, Diamond, and Fullerene (C60) respectively?",
        "option_a": "sp2, sp3, sp2",
        "option_b": "sp3, sp2, sp2",
        "option_c": "sp2, sp2, sp3",
        "option_d": "sp3, sp3, sp2",
        "correct_option": "A",
        "explanation": "Graphite has sp2 planar sheets; Diamond has 3D sp2/sp3 network (sp3); Fullerene C60 has sp2 soccer-ball cage structure.",
        "difficulty": "High"
    },
    {
        "question_text": "Which gas is liberated when Sodium metal reacts with Ethanol?",
        "option_a": "Hydrogen gas (H2)",
        "option_b": "Oxygen gas (O2)",
        "option_c": "Methane gas (CH4)",
        "option_d": "Carbon dioxide (CO2)",
        "correct_option": "A",
        "explanation": "2 CH3CH2OH + 2 Na -> 2 CH3CH2ONa + H2(g). Hydrogen gas is evolved with effervescence.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the IUPAC name of Acrolein (CH2=CH-CHO)?",
        "option_a": "Prop-2-enal",
        "option_b": "Prop-1-enal",
        "option_c": "But-2-enal",
        "option_d": "Propanal",
        "correct_option": "A",
        "explanation": "CH2=CH-CHO has 3 carbons with aldehyde at C1 and double bond at C2: Prop-2-enal.",
        "difficulty": "High"
    },
    {
        "question_text": "Which reducing agent selectively reduces Carboxylic Acids and Esters to Primary Alcohols without affecting carbon-carbon double bonds?",
        "option_a": "Lithium Aluminium Hydride (LiAlH4)",
        "option_b": "Sodium Borohydride (NaBH4)",
        "option_c": "H2 / Ni catalyst",
        "option_d": "Zn / HCl",
        "correct_option": "A",
        "explanation": "LiAlH4 is a powerful reducing agent that converts -COOH and -COOR to -CH2OH without reducing isolated C=C double bonds.",
        "difficulty": "High"
    },

    # 71 - 80: Advanced Solutions & Electrochemistry
    {
        "question_text": "What is the cell notation for the Daniell cell?",
        "option_a": "Zn(s) | Zn^2+(aq) || Cu^2+(aq) | Cu(s)",
        "option_b": "Cu(s) | Cu^2+(aq) || Zn^2+(aq) | Zn(s)",
        "option_c": "Zn(s) | Cu^2+(aq) || Zn^2+(aq) | Cu(s)",
        "option_d": "Pt(s) | Zn^2+(aq) || Cu^2+(aq) | Pt(s)",
        "correct_option": "A",
        "explanation": "Daniell cell: Anode oxidation Zn -> Zn^2+ + 2e- (left), Cathode reduction Cu^2+ + 2e- -> Cu (right).",
        "difficulty": "High"
    },
    {
        "question_text": "According to Nernst equation, if the concentration of Zn^2+ in Daniell cell is increased while Cu^2+ concentration is kept constant, the cell potential E_cell will:",
        "option_a": "Decrease",
        "option_b": "Increase",
        "option_c": "Remain unchanged",
        "option_d": "Become zero instantly",
        "correct_option": "A",
        "explanation": "E_cell = E degrees - (RT/2F) ln([Zn^2+]/[Cu^2+]). Increasing [Zn^2+] increases the log term, reducing E_cell.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the mole fraction of solute in a 1.0 m aqueous solution?",
        "option_a": "0.0177",
        "option_b": "0.0354",
        "option_c": "0.1000",
        "option_d": "0.0500",
        "correct_option": "A",
        "explanation": "1.0 m means 1.0 mol solute per 1000 g water. Moles water = 1000 / 18 = 55.55 mol. Mole fraction = 1.0 / (1.0 + 55.55) = 1 / 56.55 = 0.0177.",
        "difficulty": "High"
    },
    {
        "question_text": "Which law states that at constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the liquid?",
        "option_a": "Henry's Law",
        "option_b": "Raoult's Law",
        "option_c": "Dalton's Law",
        "option_d": "Boyle's Law",
        "correct_option": "A",
        "explanation": "Henry's law: p = K_H * x, where p is gas partial pressure and x is mole fraction in solution.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following mixtures forms a maximum boiling azeotrope exhibiting negative deviation from Raoult's law?",
        "option_a": "Nitric acid (HNO3) + Water",
        "option_b": "Ethanol + Water",
        "option_c": "Acetone + Carbon disulfide",
        "option_d": "Benzene + Toluene",
        "correct_option": "A",
        "explanation": "HNO3 + H2O forms strong solute-solvent hydrogen bonds (negative deviation), forming a maximum boiling azeotrope at 68% HNO3 (boiling point 120.5 C).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the coordination number of Sodium ions (Na+) and Chloride ions (Cl-) in the NaCl crystal lattice?",
        "option_a": "6 : 6",
        "option_b": "8 : 8",
        "option_c": "4 : 4",
        "option_d": "12 : 12",
        "correct_option": "A",
        "explanation": "NaCl has a face-centered cubic (FCC) structure where each Na+ ion is surrounded octahedrally by 6 Cl- ions, and vice versa.",
        "difficulty": "High"
    },
    {
        "question_text": "What defect occurs when an ion leaves its normal lattice site and occupies an interstitial position in a crystal?",
        "option_a": "Frenkel defect",
        "option_b": "Schottky defect",
        "option_c": "Metal excess defect",
        "option_d": "Impurity defect",
        "correct_option": "A",
        "explanation": "Frenkel defect (dislocation defect) involves displacement of smaller cations into interstitial sites without altering overall density.",
        "difficulty": "High"
    },
    {
        "question_text": "Which catalyst is used in the Contact Process for the industrial manufacture of Sulfuric Acid (H2SO4)?",
        "option_a": "Vanadium pentoxide (V2O5)",
        "option_b": "Finely divided Iron (Fe)",
        "option_c": "Platinum-Rhodium gauze",
        "option_d": "Nickel (Ni)",
        "correct_option": "A",
        "explanation": "V2O5 catalyzes the oxidation of SO2 to SO3 at 450 C in the Contact Process.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the chemical formula of Philosopher's Wool?",
        "option_a": "ZnO",
        "option_b": "ZnSO4",
        "option_c": "Fe2O3",
        "option_d": "CaO",
        "correct_option": "A",
        "explanation": "Zinc oxide (ZnO) is historically known as Philosopher's wool when formed as fluffy white tufts by burning zinc in air.",
        "difficulty": "High"
    },
    {
        "question_text": "Which non-metal is stored under water due to its high reactivity and spontaneous combustion in air?",
        "option_a": "White Phosphorus (P4)",
        "option_b": "Red Phosphorus",
        "option_c": "Sulfur",
        "option_d": "Iodine",
        "correct_option": "A",
        "explanation": "White phosphorus has a low ignition temperature (35 C) and spontaneously catches fire in air, so it is kept under water.",
        "difficulty": "High"
    },

    # 81 - 90: Organic Synthesis & Spectroscopy/Biomolecules
    {
        "question_text": "Which carbohydrate is known as invert sugar?",
        "option_a": "Equimolar mixture of Glucose and Fructose obtained by hydrolysis of Sucrose",
        "option_b": "Pure Glucose",
        "option_c": "Pure Maltose",
        "option_d": "Lactose",
        "correct_option": "A",
        "explanation": "Hydrolysis of dextrorotatory sucrose (+66.5 deg) yields a laevorotatory mixture (-39.7 deg) of glucose and fructose, called invert sugar.",
        "difficulty": "High"
    },
    {
        "question_text": "Which vitamin deficiency causes the disease Scurvy?",
        "option_a": "Vitamin C (Ascorbic acid)",
        "option_b": "Vitamin B1 (Thiamine)",
        "option_c": "Vitamin A (Retinol)",
        "option_d": "Vitamin D (Calciferol)",
        "correct_option": "A",
        "explanation": "Vitamin C (Ascorbic acid) deficiency leads to scurvy characterized by bleeding gums and delayed wound healing.",
        "difficulty": "High"
    },
    {
        "question_text": "Which nitrogenous base is present in RNA but absent in DNA?",
        "option_a": "Uracil",
        "option_b": "Thymine",
        "option_c": "Adenine",
        "option_d": "Guanine",
        "correct_option": "A",
        "explanation": "RNA contains Uracil instead of Thymine (which is present in DNA).",
        "difficulty": "High"
    },
    {
        "question_text": "Which polymer is a addition polymer formed by polymerization of Chloroprene (2-chlorobuta-1,3-diene)?",
        "option_a": "Neoprene (Synthetic rubber)",
        "option_b": "Buna-N",
        "option_c": "Teflon",
        "option_d": "Nylon-6,6",
        "correct_option": "A",
        "explanation": "Free radical polymerization of chloroprene yields Neoprene (synthetic rubber).",
        "difficulty": "High"
    },
    {
        "question_text": "What are the monomeric units of Nylon-6,6?",
        "option_a": "Hexamethylenediamine and Adipic acid",
        "option_b": "Caprolactam",
        "option_c": "Terephthalic acid and Ethylene glycol",
        "option_d": "Styrene and 1,3-Butadiene",
        "correct_option": "A",
        "explanation": "Nylon-6,6 is a condensation polyamide produced from Hexamethylenediamine and Adipic acid.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following is a broad-spectrum antibiotic?",
        "option_a": "Chloramphenicol",
        "option_b": "Penicillin G",
        "option_c": "Aspirin",
        "option_d": "Paracetamol",
        "correct_option": "A",
        "explanation": "Chloramphenicol is effective against a wide range of Gram-positive and Gram-negative bacteria (broad-spectrum).",
        "difficulty": "High"
    },
    {
        "question_text": "Which synthetic detergent belongs to the category of cationic detergents?",
        "option_a": "Cetyltrimethylammonium bromide",
        "option_b": "Sodium lauryl sulfate",
        "option_c": "Sodium dodecylbenzenesulfonate",
        "option_d": "Pentaerythrityl monostearate",
        "correct_option": "A",
        "explanation": "Cetyltrimethylammonium bromide is a quaternary ammonium salt with a long hydrocarbon chain in the cation.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the IUPAC name of Glycerol?",
        "option_a": "Propane-1,2,3-triol",
        "option_b": "Propane-1,2-diol",
        "option_c": "Ethane-1,2-diol",
        "option_d": "Butane-1,2,3-triol",
        "correct_option": "A",
        "explanation": "Glycerol has 3 carbon atoms with hydroxyl groups on each carbon: Propane-1,2,3-triol.",
        "difficulty": "High"
    },
    {
        "question_text": "Which functional group is formed in the Victor Meyer test for primary alcohols yielding a blood-red color?",
        "option_a": "Nitrolic acid salt",
        "option_b": "Pseudonitrol",
        "option_c": "Carbylamine",
        "option_d": "Azo dye",
        "correct_option": "A",
        "explanation": "Primary alcohols produce nitrolic acid which dissolves in NaOH to give a characteristic blood-red solution.",
        "difficulty": "High"
    },
    {
        "question_text": "Which reagent converts an Alkynes into Cis-Alkene selectively?",
        "option_a": "Lindlar's catalyst (H2 / Pd / CaCO3 poisoned with quinoline)",
        "option_b": "Sodium in liquid Ammonia (Birch reduction)",
        "option_c": "Concentrated H2SO4",
        "option_d": "LiAlH4",
        "correct_option": "A",
        "explanation": "Partial hydrogenation of alkynes over Lindlar's catalyst yields cis-alkenes, whereas Birch reduction (Na/NH3) yields trans-alkenes.",
        "difficulty": "High"
    },

    # 91 - 100: Comprehensive Review & Advanced Inorganic/Organic Synthesis
    {
        "question_text": "What is the oxidation state of Iron in Potassium Ferrocynide [K4Fe(CN)6]?",
        "option_a": "+2",
        "option_b": "+3",
        "option_c": "+6",
        "option_d": "0",
        "correct_option": "A",
        "explanation": "4(+1) + Fe + 6(-1) = 0 => 4 + Fe - 6 = 0 => Fe = +2.",
        "difficulty": "High"
    },
    {
        "question_text": "Which catalyst is used in the Haber process for the industrial synthesis of Ammonia?",
        "option_a": "Iron catalyst with Molybdenum promoter",
        "option_b": "Vanadium pentoxide",
        "option_c": "Nickel catalyst",
        "option_d": "Copper chromite",
        "correct_option": "A",
        "explanation": "The Haber process N2 + 3 H2 <=> 2 NH3 uses finely divided Iron catalyst boosted by Molybdenum/Al2O3 promoter.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the coordination number of the central atom in [EDTA]^4- complexes?",
        "option_a": "6 (Hexadentate ligand)",
        "option_b": "4 (Tetradentate ligand)",
        "option_c": "2 (Bidentate ligand)",
        "option_d": "8 (Octadentate ligand)",
        "correct_option": "A",
        "explanation": "EDTA^4- (Ethylenediaminetetraacetate) has 2 Nitrogen and 4 Oxygen donor atoms, making it a hexadentate chelating ligand.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following compounds exhibits optical activity (chiral molecule)?",
        "option_a": "2-chlorobutane",
        "option_b": "1-chlorobutane",
        "option_c": "2-chloropropane",
        "option_d": "2-methylpropan-2-ol",
        "correct_option": "A",
        "explanation": "C2 in 2-chlorobutane is bonded to 4 different groups (-H, -Cl, -CH3, -CH2CH3), making it a chiral center.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the product of Wurtz reaction of Methyl iodide (CH3I) with Sodium in dry ether?",
        "option_a": "Ethane (CH3-CH3)",
        "option_b": "Methane (CH4)",
        "option_c": "Propane (C3H8)",
        "option_d": "Ethene (C2H4)",
        "correct_option": "A",
        "explanation": "2 CH3I + 2 Na -> CH3-CH3 (Ethane) + 2 NaI.",
        "difficulty": "High"
    },
    {
        "question_text": "Which test is used to detect presence of peptide bonds in proteins?",
        "option_a": "Biuret test",
        "option_b": "Barfoed test",
        "option_c": "Seliwanoff test",
        "option_d": "Molisch test",
        "correct_option": "A",
        "explanation": "Biuret reagent (alkaline CuSO4) reacts with peptide bonds (-CO-NH-) to form a violet/purple complex.",
        "difficulty": "High"
    },
    {
        "question_text": "Which of the following noble gases forms maximum stable chemical compounds?",
        "option_a": "Xenon (Xe)",
        "option_b": "Helium (He)",
        "option_c": "Neon (Ne)",
        "option_d": "Argon (Ar)",
        "correct_option": "A",
        "explanation": "Xenon has a lower ionization enthalpy among noble gases, enabling it to form stable fluorides and oxides (XeF2, XeF4, XeO3).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the bond order of CN- ion according to Molecular Orbital Theory?",
        "option_a": "3.0",
        "option_b": "2.5",
        "option_c": "2.0",
        "option_d": "1.5",
        "correct_option": "A",
        "explanation": "CN- has 6 + 7 + 1 = 14 electrons (isoelectronic with N2). Bond order = (10 - 4) / 2 = 3.0.",
        "difficulty": "High"
    },
    {
        "question_text": "Which law states that energy can neither be created nor destroyed, only transformed?",
        "option_a": "First Law of Thermodynamics",
        "option_b": "Second Law of Thermodynamics",
        "option_c": "Third Law of Thermodynamics",
        "option_d": "Zeroth Law of Thermodynamics",
        "correct_option": "A",
        "explanation": "The First Law of Thermodynamics is the Law of Conservation of Energy (delta U = Q - W).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the pH of a 0.01 M NaOH aqueous solution at 25 degrees C?",
        "option_a": "12.0",
        "option_b": "2.0",
        "option_c": "7.0",
        "option_d": "14.0",
        "correct_option": "A",
        "explanation": "[OH-] = 0.01 = 10^-2 M. pOH = -log(10^-2) = 2.0. pH = 14 - pOH = 14 - 2 = 12.0.",
        "difficulty": "High"
    }
]
