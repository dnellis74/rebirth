class Particle:
    def __init__(self, name, mass, charge, spin):
        """
        Base class for any particle in the Standard Model.
        :param name: Name of the particle.
        :param mass: Mass (in MeV/c^2 for illustration).
        :param charge: Charge (in units of elementary charge).
        :param spin: Spin (in units of ℏ).
        """
        self.name = name
        self.mass = mass
        self.charge = charge
        self.spin = spin

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Particle: {self.name}, Mass: {self.mass} MeV/c^2, Charge: {self.charge}, Spin: {self.spin}")


# Fermions (matter particles with half-integer spin)
class Fermion(Particle):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)


# Bosons (force carriers with integer spin)
class Boson(Particle):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)


# Leptons (e.g., electrons, neutrinos)
class Lepton(Fermion):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)


# Quarks, with an additional attribute for flavor.
class Quark(Fermion):
    def __init__(self, name, mass, charge, spin, flavor):
        super().__init__(name, mass, charge, spin)
        self.flavor = flavor

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Quark: {self.name} (Flavor: {self.flavor}), Mass: {self.mass} MeV/c^2, Charge: {self.charge}, Spin: {self.spin}")


# Gauge Bosons (e.g., photon, gluon, W and Z bosons)
class GaugeBoson(Boson):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Gauge Boson: {self.name}, Mass: {self.mass} MeV/c^2, Charge: {self.charge}, Spin: {self.spin}")


# The Higgs boson
class HiggsBoson(Boson):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Higgs Boson: {self.name}, Mass: {self.mass} MeV/c^2, Charge: {self.charge}, Spin: {self.spin}")


# Hadrons are composite particles made up of quarks (e.g., protons and neutrons)
class Hadron(Particle):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)
        self.constituents = []  # List to hold quark constituents

    def add_constituent(self, quark):
        self.constituents.append(quark)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Hadron: {self.name}, Mass: {self.mass} MeV/c^2, Charge: {self.charge}, Spin: {self.spin}")
        if self.constituents:
            print(f"{ind}Constituent quarks:")
            for q in self.constituents:
                q.print_info(indent + 2)


# Atom: A simplified model with a nucleus (Hadron) and electrons (Leptons)
class Atom(Particle):
    def __init__(self, name, nucleus, electrons):
        """
        :param nucleus: An instance of Hadron representing the nucleus.
        :param electrons: A list of Lepton instances representing electrons.
        """
        # We'll compute total mass and charge by combining the nucleus and electrons.
        total_mass = nucleus.mass + sum(e.mass for e in electrons)
        total_charge = nucleus.charge + sum(e.charge for e in electrons)
        # For simplicity, we'll take the nucleus spin as the atom's spin.
        super().__init__(name, total_mass, total_charge, nucleus.spin)
        self.nucleus = nucleus
        self.electrons = electrons

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Atom: {self.name}, Total Mass: {self.mass} MeV/c^2, Total Charge: {self.charge}")
        print(f"{ind}Nucleus:")
        self.nucleus.print_info(indent + 2)
        if self.electrons:
            print(f"{ind}Electrons:")
            for e in self.electrons:
                e.print_info(indent + 2)


# Molecule: A composite object made up of one or more atoms.
class Molecule(Particle):
    def __init__(self, name, atoms):
        """
        :param atoms: A list of Atom instances.
        """
        total_mass = sum(atom.mass for atom in atoms)
        total_charge = sum(atom.charge for atom in atoms)
        # We'll set a default spin value (real molecules may have complex spin coupling).
        super().__init__(name, total_mass, total_charge, 0)
        self.atoms = atoms

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Molecule: {self.name}, Total Mass: {self.mass} MeV/c^2, Total Charge: {self.charge}")
        print(f"{ind}Constituent Atoms:")
        for atom in self.atoms:
            atom.print_info(indent + 2)


# Example usage
if __name__ == '__main__':
    # Create some quarks (illustrative masses)
    up = Quark("Up Quark", 2.3, +2.0/3, 0.5, "up")
    down = Quark("Down Quark", 4.8, -1.0/3, 0.5, "down")

    # Create a proton as a hadron: Proton = 2 up quarks + 1 down quark.
    proton_hadron = Hadron("Proton", 938.3, +1, 0.5)
    proton_hadron.add_constituent(up)
    proton_hadron.add_constituent(up)
    proton_hadron.add_constituent(down)

    # Create a neutron as a hadron: Neutron = 1 up quark + 2 down quarks.
    neutron_hadron = Hadron("Neutron", 939.6, 0, 0.5)
    neutron_hadron.add_constituent(up)
    neutron_hadron.add_constituent(down)
    neutron_hadron.add_constituent(down)

    # Create an electron (a lepton)
    electron = Lepton("Electron", 0.511, -1, 0.5)

    # Create atoms.
    # For Hydrogen, the nucleus is a proton.
    hydrogen = Atom("Hydrogen", proton_hadron, [electron])

    # For Oxygen, we simulate a nucleus (in reality, oxygen has 8 protons and 8 neutrons).
    # Here, we use an illustrative aggregate nucleus.
    oxygen_nucleus = Hadron("Oxygen Nucleus", 15000, +8, 0.5)
    oxygen = Atom("Oxygen", oxygen_nucleus, [electron] * 8)

    # Create a water molecule (H2O): 2 Hydrogen atoms and 1 Oxygen atom.
    water = Molecule("Water", [hydrogen, hydrogen, oxygen])

    # Create some gauge bosons and the Higgs boson.
    photon = GaugeBoson("Photon", 0.0, 0.0, 1)
    gluon = GaugeBoson("Gluon", 0.0, 0.0, 1)
    higgs = HiggsBoson("Higgs Boson", 125000, 0.0, 0.0)  # 125 GeV in MeV

    # Display information about our objects
    print("=== Standard Model Particles and Composite Systems ===\n")
    print("Proton (Hadron):")
    proton_hadron.print_info(indent=2)
    print("\nElectron (Lepton):")
    electron.print_info(indent=2)
    print("\nHydrogen Atom:")
    hydrogen.print_info(indent=2)
    print("\nOxygen Atom:")
    oxygen.print_info(indent=2)
    print("\nWater Molecule:")
    water.print_info(indent=2)
    print("\nPhoton (Gauge Boson):")
    photon.print_info(indent=2)
    print("\nGluon (Gauge Boson):")
    gluon.print_info(indent=2)
    print("\nHiggs Boson:")
    higgs.print_info(indent=2)
