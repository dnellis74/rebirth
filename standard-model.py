class Particle:
    def __init__(self, name, mass, charge, spin):
        """
        Base class for any particle.
        :param name: Name of the particle.
        :param mass: Mass in MeV/c^2 (illustrative).
        :param charge: Charge (in elementary charge units).
        :param spin: Spin (in units of ℏ).
        """
        self.name = name
        self.mass = mass
        self.charge = charge
        self.spin = spin

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}{self.name}: Mass = {self.mass} MeV/c^2, Charge = {self.charge}, Spin = {self.spin}")

# New Energy class to deabstract energy.
class Energy:
    def __init__(self, value, energy_type):
        """
        Represents a quantized amount of energy.
        :param value: Energy value in MeV.
        :param energy_type: Type of energy (e.g., 'photon', 'thermal').
        """
        self.value = value
        self.energy_type = energy_type

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Energy: {self.value} MeV, Type: {self.energy_type}")

# Photon to represent emitted light.
class Photon(Particle):
    def __init__(self):
        # Photons are massless, uncharged, and have spin 1.
        super().__init__("Photon", mass=0.0, charge=0.0, spin=1)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}{self.name}: Mass = {self.mass} MeV/c^2, Charge = {self.charge}, Spin = {self.spin}")

# Quark: Fundamental constituent of hadrons.
class Quark(Particle):
    def __init__(self, name, mass, charge, spin, flavor):
        super().__init__(name, mass, charge, spin)
        self.flavor = flavor

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Quark: {self.name} (Flavor: {self.flavor}), Mass = {self.mass} MeV/c^2, Charge = {self.charge}, Spin = {self.spin}")

# Gluon: Carrier of the strong force between quarks.
class Gluon(Particle):
    def __init__(self):
        # Gluons are massless and uncharged.
        super().__init__("Gluon", mass=0.0, charge=0.0, spin=1)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}{self.name}: Mass = {self.mass} MeV/c^2, Charge = {self.charge}, Spin = {self.spin}")

# Hadron: A composite particle made of quarks and gluons.
class Hadron(Particle):
    def __init__(self, name, mass, charge, spin):
        super().__init__(name, mass, charge, spin)
        self.quarks = []   # List to hold quark constituents.
        self.gluons = []   # List to hold gluon mediators.

    def add_quark(self, quark):
        self.quarks.append(quark)

    def add_gluon(self, gluon):
        self.gluons.append(gluon)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}{self.name}: Total Mass = {self.mass} MeV/c^2, Total Charge = {self.charge}, Spin = {self.spin}")
        if self.quarks:
            print(f"{ind}  Constituent quarks:")
            for q in self.quarks:
                q.print_info(indent + 4)
        if self.gluons:
            print(f"{ind}  Mediating gluons:")
            for g in self.gluons:
                g.print_info(indent + 4)

    def simulate_qcd_interaction(self):
        """
        Simulate a simplified view of quark-gluon interactions.
        """
        print(f"    [QCD] {self.name}: Quarks and gluons are interacting...")
        for q in self.quarks:
            print(f"      [QCD] {q.name} (flavor: {q.flavor}) exchanges a gluon.")
        for _ in self.gluons:
            print("      [QCD] A gluon is exchanged between quarks.")

# Nucleus: Composed of nucleons (protons and neutrons).
class Nucleus(Particle):
    def __init__(self, name, nucleons):
        """
        :param nucleons: List of Hadron instances representing protons and neutrons.
        """
        self.nucleons = nucleons
        total_mass = sum(n.mass for n in nucleons)
        total_charge = sum(n.charge for n in nucleons)
        # For simplicity, assume overall nuclear spin is 0.
        super().__init__(name, total_mass, total_charge, spin=0)

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Nucleus: {self.name} -> Mass = {self.mass} MeV/c^2, Charge = {self.charge}")
        print(f"{ind} Nucleons:")
        for n in self.nucleons:
            n.print_info(indent + 2)

    def simulate_nuclear_qcd(self):
        """
        Simulate QCD interactions for each nucleon in the nucleus.
        """
        print("  Simulating QCD interactions within the nucleus:")
        for nucleon in self.nucleons:
            nucleon.simulate_qcd_interaction()

# Atom: Composed of a nucleus and electrons.
class Atom(Particle):
    def __init__(self, name, nucleus, electrons):
        """
        :param nucleus: A Nucleus instance.
        :param electrons: List of Particle instances representing electrons.
        """
        total_mass = nucleus.mass + sum(e.mass for e in electrons)
        total_charge = nucleus.charge + sum(e.charge for e in electrons)
        # For simplicity, use the nucleus's spin.
        super().__init__(name, total_mass, total_charge, spin=nucleus.spin)
        self.nucleus = nucleus
        self.electrons = electrons
        self.electron_excited = False  # Flag to indicate excitation state

    def print_info(self, indent=0):
        ind = " " * indent
        print(f"{ind}Atom: {self.name} -> Mass = {self.mass} MeV/c^2, Charge = {self.charge}")
        print(f"{ind} Nucleus:")
        self.nucleus.print_info(indent + 2)
        if self.electrons:
            print(f"{ind} Electrons:")
            for e in self.electrons:
                e.print_info(indent + 2)

    def absorb_energy(self, energy_obj):
        """
        Simulate the absorption of energy by the atom.
        The energy object can be from a photon or another source.
        This energy both excites an electron and triggers QCD interactions.
        :param energy_obj: An Energy instance.
        """
        print(f"\n[Sodium Atom] Absorbing energy:")
        energy_obj.print_info(indent=2)
        # Excite an electron (we mark the first electron as excited)
        self.electron_excited = True
        print("  An electron is excited to a higher orbital.")
        # Simulate nuclear response (QCD interactions within each nucleon)
        self.nucleus.simulate_nuclear_qcd()

    def emit_photon(self):
        """
        Simulate the de-excitation of an electron with photon emission.
        """
        if self.electron_excited:
            print("\n[Sodium Atom] Electron de-excitation:")
            print("  The excited electron transitions back to a lower energy state, emitting a photon.")
            photon = Photon()
            photon.print_info(indent=4)
            self.electron_excited = False
        else:
            print("  No excited electron is present to emit a photon.")

# Helper functions to create nucleons with internal structure.
def create_proton():
    """
    Creates a proton (mass ≈ 938.3 MeV, charge +1) as a hadron composed of:
      - 2 up quarks and 1 down quark
      - A couple of gluons for strong force mediation.
    """
    proton = Hadron("Proton", mass=938.3, charge=+1, spin=0.5)
    proton.add_quark(Quark("Up Quark", 2.3, +2.0/3, 0.5, "up"))
    proton.add_quark(Quark("Up Quark", 2.3, +2.0/3, 0.5, "up"))
    proton.add_quark(Quark("Down Quark", 4.8, -1.0/3, 0.5, "down"))
    proton.add_gluon(Gluon())
    proton.add_gluon(Gluon())
    return proton

def create_neutron():
    """
    Creates a neutron (mass ≈ 939.6 MeV, charge 0) as a hadron composed of:
      - 1 up quark and 2 down quarks
      - A couple of gluons.
    """
    neutron = Hadron("Neutron", mass=939.6, charge=0, spin=0.5)
    neutron.add_quark(Quark("Up Quark", 2.3, +2.0/3, 0.5, "up"))
    neutron.add_quark(Quark("Down Quark", 4.8, -1.0/3, 0.5, "down"))
    neutron.add_quark(Quark("Down Quark", 4.8, -1.0/3, 0.5, "down"))
    neutron.add_gluon(Gluon())
    neutron.add_gluon(Gluon())
    return neutron

# Main simulation for a Sodium Atom (Sodium-23) that absorbs energy and emits light.
if __name__ == '__main__':
    # Sodium-23 has 11 protons and 12 neutrons.
    nucleons = []
    for _ in range(11):
        nucleons.append(create_proton())
    for _ in range(12):
        nucleons.append(create_neutron())

    sodium_nucleus = Nucleus("Sodium-23 Nucleus", nucleons)

    # A neutral sodium atom has 11 electrons.
    electrons = [Particle("Electron", mass=0.511, charge=-1, spin=0.5) for _ in range(11)]

    sodium_atom = Atom("Sodium Atom", nucleus=sodium_nucleus, electrons=electrons)

    # Display detailed information about the sodium atom.
    print("=== Sodium Atom Simulation with Quarks, Gluons, and Light Emission ===\n")
    sodium_atom.print_info(indent=2)

    # Create an Energy object representing, for example, a photon providing 3.0 MeV of energy.
    incident_energy = Energy(3.0, "photon")

    # Simulate the atom absorbing the energy.
    sodium_atom.absorb_energy(incident_energy)

    # Later, the excited electron de-excites and emits a photon.
    sodium_atom.emit_photon()
