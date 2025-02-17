#include <iostream>
#include <string>
#include <vector>

// Base class representing any particle in the Standard Model
class Particle {
protected:
    std::string name;
    double mass;    // Mass in MeV/c^2 (for illustration)
    double charge;  // In units of the elementary charge
    double spin;    // In units of ℏ (0.5 for fermions, integers for bosons)
public:
    Particle(const std::string& name, double mass, double charge, double spin)
        : name(name), mass(mass), charge(charge), spin(spin) {}

    virtual ~Particle() {}

    virtual void printInfo() const {
        std::cout << "Particle: " << name
                  << ", Mass: " << mass << " MeV/c^2"
                  << ", Charge: " << charge
                  << ", Spin: " << spin << std::endl;
    }
};

// Fermions are particles that follow Fermi-Dirac statistics (spin = half-integer)
class Fermion : public Particle {
public:
    Fermion(const std::string& name, double mass, double charge, double spin)
        : Particle(name, mass, charge, spin) {}
};

// Bosons are force carriers (spin = integer)
class Boson : public Particle {
public:
    Boson(const std::string& name, double mass, double charge, double spin)
        : Particle(name, mass, charge, spin) {}
};

// Leptons (e.g., electrons, neutrinos)
class Lepton : public Fermion {
public:
    Lepton(const std::string& name, double mass, double charge, double spin)
        : Fermion(name, mass, charge, spin) {}
};

// Quarks, which come in different flavors (up, down, charm, strange, top, bottom)
class Quark : public Fermion {
private:
    std::string flavor;
public:
    Quark(const std::string& name, double mass, double charge, double spin, const std::string& flavor)
        : Fermion(name, mass, charge, spin), flavor(flavor) {}

    std::string getFlavor() const { return flavor; }

    void printInfo() const override {
        std::cout << "Quark: " << name
                  << " (Flavor: " << flavor << ")"
                  << ", Mass: " << mass << " MeV/c^2"
                  << ", Charge: " << charge
                  << ", Spin: " << spin << std::endl;
    }
};

// Gauge bosons (e.g., photon, gluon, W and Z bosons)
class GaugeBoson : public Boson {
public:
    GaugeBoson(const std::string& name, double mass, double charge, double spin)
        : Boson(name, mass, charge, spin) {}

    void printInfo() const override {
        std::cout << "Gauge Boson: " << name
                  << ", Mass: " << mass << " MeV/c^2"
                  << ", Charge: " << charge
                  << ", Spin: " << spin << std::endl;
    }
};

// The Higgs boson is a special boson responsible for giving mass
class HiggsBoson : public Boson {
public:
    HiggsBoson(const std::string& name, double mass, double charge, double spin)
        : Boson(name, mass, charge, spin) {}

    void printInfo() const override {
        std::cout << "Higgs Boson: " << name
                  << ", Mass: " << mass << " MeV/c^2"
                  << ", Charge: " << charge
                  << ", Spin: " << spin << std::endl;
    }
};

// Hadrons are composite particles made of quarks (e.g., protons and neutrons)
class Hadron : public Particle {
private:
    std::vector<Quark*> constituents;  // Quarks that make up the hadron
public:
    Hadron(const std::string& name, double mass, double charge, double spin)
        : Particle(name, mass, charge, spin) {}

    // Add a quark constituent to the hadron
    void addConstituent(Quark* q) {
        constituents.push_back(q);
    }

    // Print info including constituent quarks
    void printInfo() const override {
        std::cout << "Hadron: " << name
                  << ", Mass: " << mass << " MeV/c^2"
                  << ", Charge: " << charge
                  << ", Spin: " << spin << std::endl;
        if (!constituents.empty()) {
            std::cout << "Constituent quarks:" << std::endl;
            for (const auto& q : constituents) {
                std::cout << "  ";
                q->printInfo();
            }
        }
    }
};

// Atom: A simplified model of an atom, with a nucleus and electrons.
// The nucleus is represented as a Hadron, and electrons as Leptons.
class Atom : public Particle {
private:
    Hadron nucleus;
    std::vector<Lepton> electrons;
public:
    Atom(const std::string& name, const Hadron& nucleus, const std::vector<Lepton>& electrons)
        : Particle(name, 0, 0, 0), nucleus(nucleus), electrons(electrons)
    {
        // Calculate the atom's mass and charge by summing the nucleus and electron contributions.
        mass = nucleus.mass;
        charge = nucleus.charge;
        for (const auto& electron : electrons) {
            mass += electron.mass;
            charge += electron.charge;
        }
        // Spin is a complex combination; here we simply use the nucleus's spin as a placeholder.
        spin = nucleus.spin;
    }

    void printInfo() const override {
        std::cout << "Atom: " << name
                  << ", Total Mass: " << mass << " MeV/c^2"
                  << ", Total Charge: " << charge << std::endl;
        std::cout << "Nucleus Info:" << std::endl;
        nucleus.printInfo();
        if (!electrons.empty()) {
            std::cout << "Electrons:" << std::endl;
            for (const auto& electron : electrons) {
                std::cout << "  ";
                electron.printInfo();
            }
        }
    }
};

// Molecule: A composite object made up of one or more atoms.
class Molecule : public Particle {
private:
    std::vector<Atom> atoms;
public:
    Molecule(const std::string& name, const std::vector<Atom>& atoms)
        : Particle(name, 0, 0, 0), atoms(atoms)
    {
        // Aggregate the mass and charge of all atoms to define the molecule.
        for (const auto& atom : atoms) {
            mass += atom.mass;
            charge += atom.charge;
        }
        // For simplicity, we set spin to zero (real molecular spin combinations are more complex).
        spin = 0;
    }

    void printInfo() const override {
        std::cout << "Molecule: " << name
                  << ", Total Mass: " << mass << " MeV/c^2"
                  << ", Total Charge: " << charge << std::endl;
        std::cout << "Constituent Atoms:" << std::endl;
        for (const auto& atom : atoms) {
            std::cout << "  ";
            atom.printInfo();
        }
    }
};

int main() {
    // Create some quarks (illustrative masses)
    Quark up("Up Quark", 2.3, +2.0/3, 0.5, "up");
    Quark down("Down Quark", 4.8, -1.0/3, 0.5, "down");

    // Create a proton as a hadron: Proton = 2 up quarks + 1 down quark.
    Hadron protonHadron("Proton", 938.3, +1, 0.5);
    protonHadron.addConstituent(&up);
    protonHadron.addConstituent(&up);
    protonHadron.addConstituent(&down);

    // Create a neutron as a hadron: Neutron = 1 up quark + 2 down quarks.
    Hadron neutronHadron("Neutron", 939.6, 0, 0.5);
    neutronHadron.addConstituent(&up);
    neutronHadron.addConstituent(&down);
    neutronHadron.addConstituent(&down);

    // Create a lepton: Electron
    Lepton electron("Electron", 0.511, -1, 0.5);

    // Create atoms.
    // For Hydrogen, the nucleus is simply a proton.
    Atom hydrogen("Hydrogen", protonHadron, std::vector<Lepton>{electron});

    // For Oxygen, we will simulate a simple nucleus by combining protons and neutrons.
    // (In reality, an oxygen nucleus is made up of 8 protons and 8 neutrons.
    // Here we use approximate aggregate values for illustration.)
    Hadron oxygenNucleus("Oxygen Nucleus", 15000, +8, 0.5);
    // Oxygen atom with 8 electrons (again, values are illustrative).
    Atom oxygen("Oxygen", oxygenNucleus, std::vector<Lepton>{electron, electron, electron, electron,
                                                                electron, electron, electron, electron});

    // Create a water molecule (H2O): 2 Hydrogen atoms and 1 Oxygen atom.
    Molecule water("Water", std::vector<Atom>{hydrogen, hydrogen, oxygen});

    // Display information about the particles
    std::cout << "=== Standard Model Particles and Composite Systems ===" << std::endl << std::endl;
    
    std::cout << "Proton (Hadron):" << std::endl;
    protonHadron.printInfo();
    std::cout << std::endl;
    
    std::cout << "Electron (Lepton):" << std::endl;
    electron.printInfo();
    std::cout << std::endl;
    
    std::cout << "Hydrogen Atom:" << std::endl;
    hydrogen.printInfo();
    std::cout << std::endl;
    
    std::cout << "Oxygen Atom:" << std::endl;
    oxygen.printInfo();
    std::cout << std::endl;
    
    std::cout << "Water Molecule:" << std::endl;
    water.printInfo();
    std::cout << std::endl;
    
    return 0;
}
