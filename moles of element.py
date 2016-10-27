

H  	 =	Hydrogen	  =	1.008	
He	 =	Helium	  =	4.002	
Li	 =	Lithium	  =		6.94
Be	 =	Beryllium	  =	9.012	
B	 =	Boron	  =		10.81
C	 =	Carbon	  =		12.01
N	 =	Nitrogen	  =	14	
O	 =	Oxygen	  =		15.99
F	 =	Fluorine	  =	18.99	
Ne	 =	Neon	  =		20.17
Na	 =	Sodium	  =		22.98
Mg	 =	Magnesium	  =	24.3	
Al	 =	Aluminium	  =	26.98	
Si	 =	Silicon	  =		28.08
P	 =	Phosphorus	  =	30.97	
S	 =	Sulfur	  =		32.06
Cl	 =	Chlorine	  =	35.45	
Ar	 =	Argon	  =		39.94
K	 =	Potassium	  =	39.09	
Ca	 =	Calcium	  =		40.07
Sc	 =	Scandium	  =	44.95	
Ti	 =	Titanium	  =	47.86	
V	 =	Vanadium	  =	50.94	
Cr	 =	Chromium	  =	51.99	
Mn	 =	Manganese	  =	54.93	
Fe	 =	Iron	  =		55.84
Co	 =	Cobalt	  =		58.93
Ni	 =	Nickel	  =		58.69
Cu	 =	Copper	  =		63.54
Zn	 =	Zinc	  =		65.38
Ga	 =	Gallium	  =		69.72
Ge	 =	Germanium	  =	72.63	
As	 =	Arsenic	  =		74.92
Se	 =	Selenium	  =	78.97	
Br	 =	Bromine	  =		79.9
Kr	 =	Krypton	  =		83.79
Rb	 =	Rubidium	  =	85.46	
Sr	 =	Strontium	  =	87.62	
Y	 =	Yttrium	  =		88.9
Zr	 =	Zirconium	  =	91.22	
Nb	 =	Niobium	  =		92.9
Mo	 =	Molybdenum	  =	95.95	
Tc	 =	Technetium	  =	97	
Ru	 =	Ruthenium	  =	101.07	
Rh	 =	Rhodium	  =		102.9
Pd	 =	Palladium	  =	106.42	
Ag	 =	Silver	  =		107.86
Cd	 =	Cadmium	  =		112.41
In	 =	Indium	  =		114.81
Sn	 =	Tin	  =		118.71
Sb	 =	Antimony	  =	121.76	
Te	 =	Tellurium	  =	127.6	
I	 =	Iodine	  =		126.9
Xe	 =	Xenon	  =		131.29
Cs	 =	Caesium	  =		132.9
Ba	 =	Barium	  =		137.32
La	 =	Lanthanum	  =	138.9	
Ce	 =	Cerium	  =		140.11
Pr	 =	Praseodymium   = 140.90	  	
Nd	 =	Neodymium	  =	144.24	
Pm	 =	Promethium	  =	145	
Sm	 =	Samarium	  =	150.36	
Eu	 =	Europium	  =	151.96	
Gd	 =	Gadolinium	  =	157.25	
Tb	 =	Terbium	  =		158.92
Dy	 =	Dysprosium	  =	162.5	
Ho	 =	Holmium	  =		164.93
Er	 =	Erbium	  =		167.25
Tm	 =	Thulium	  =		168.93
Yb	 =	Ytterbium	  =	173.04	
Lu	 =	Lutetium	  =	174.96	
Hf	 =	Hafnium	  =		178.49
Ta	 =	Tantalum	  =	180.94	
W	 =	Tungsten	  =	183.84	
Re	 =	Rhenium	  =		186.2
Os	 =	Osmium	  =		190.23
Ir	 =	Iridium	  =		192.21
Pt	 =	Platinum	  =	195.08	
Au	 =	Gold	  =		196.96
Hg	 =	Mercury	  =		200.59
Tl	 =	Thallium	  =	204.38	
Pb	 =	Lead	  =		207.2
Bi	 =	Bismuth	  =		208.98
Po	 =	Polonium	  =	209	
At	 =	Astatine	  =	210	
Rn	 =	Radon	  =		222
Fr	 =	Francium	  =	223	
Ra	 =	Radium	  =		226
Ac	 =	Actinium	  =	227	
Th	 =	Thorium	  =		232.03
Pa	 =	Protactinium	  =	231.03	
U	 =	Uranium	  =		238.02
Np	 =	Neptunium	  =	237	
Pu	 =	Plutonium	  =	244	
Am	 =	Americium	  =	243	
Cm	 =	Curium	  =		247
Bk	 =	Berkelium	  =	247	
Cf	 =	Californium	  =	251	
Es	 =	Einsteinium	  =	252	
Fm	 =	Fermium	  =		257
Md	 =	Mendelevium	  =	258	
No	 =	Nobelium	  =	259	


print("""Enter the name or symbol of the element 
 
       Ex: Helium,Fr  """)


b=input()
 
print('Enter the given weight of the element')

a=float(input())





moles = a/b

atoms=moles*6.022*10**23

print('the element is of')
print moles,'moles '

print 'the number of atoms are',atoms
