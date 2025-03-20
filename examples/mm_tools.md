# MM Tools Repository

Welcome to the MM Tools repository, a comprehensive collection of molecular modeling tools designed to facilitate various tasks in computational chemistry and molecular dynamics. This repository includes plugins and utilities for structure manipulation, data analysis, molecular dynamics simulations, and more.

## Tools Overview

### Structure Manipulation
- **remove-terminal-residue-name-prefixes-plugin**: Remove terminal residue name prefixes from PDB files.
- **sanitize-ligand-plugin**: Handle molecules with RDKit errors gracefully.
- **fix-amides-plugin**: Fix amide groups in residues within PDB files.
- **combine-structure-plugin**: Combine two XYZ structures into a single PDB file using RDKit.
- **pdb2gmx-plugin**: Wrapper for the GROMACS pdb2gmx module to convert PDB files.
- **box-plugin**: Set the center and size of a box around residues or pockets in PDB files.
- **str-check-add-hydrogens-plugin**: Add hydrogens to 3D structures using the Structure Checking tool.
- **extract-protein-openmm-plugin**: Extract protein structures from PDB files using OpenMM.
- **gmx-editconf-plugin**: Edit GROMACS structure files using the editconf module.
- **genion-plugin**: Add ions to GROMACS structures using the genion module.
- **solvate-plugin**: Solvate GROMACS structures using the solvate module.
- **pdbfixer-plugin**: Fix structural issues in protein PDB files.

### Data Analysis
- **scatter_plot_plugin**: Generate scatter plots from data arrays.
- **check-linear-fit-tool**: Check linear fit for given data arrays.
- **filter-array-tool**: Filter arrays based on a boolean array input.
- **random-subset-rows-tool**: Select random subset indices from arrays using a seed.
- **array-indices-plugin**: Return a subset from an array based on input indices.

### Molecular Dynamics
- **gmx-trjconv-str-plugin**: Convert and extract atom selections from GROMACS structure files.
- **gmx-rms-nofit-plugin**: Perform RMSd analysis on GROMACS trajectories without fitting.
- **mdrun-tool**: Run molecular dynamics simulations using the GROMACS mdrun module.
- **grompp-tool**: Prepare GROMACS run files using the grompp module.
- **sander-mdrun-tool**: Run MD simulations using the AmberTools sander module.
- **process-mdout-tool**: Process AMBER MD output files to extract data.
- **acpype-tool**: Generate topologies for GROMACS using Acpype.

### Docking
- **autodock-vina-run-tool**: Run docking simulations using AutoDock Vina.
- **pose-cluster-filter-tool**: Cluster poses in proteins and select the most confident pose for each cluster.

### Pre-Processing
- **generate-conformers-sdf-tool**: Generate conformers for small molecules using Open Babel.
- **download-gdb9-database-tool**: Download MolGAN models and datasets.
- **pdbbind-generate-conformers-tool**: Download PDBbind database and generate conformers from SMILES.
- **pdb-tool**: Download PDB files from specified configurations.
- **zip-top-tool**: Zip GROMACS topology files for easier handling.
- **append-ligand-tool**: Insert ligand ITP files into GROMACS topologies.
- **extract-ligand-protein-tool**: Extract ligands and proteins from PDB files using OpenMM.
- **duplicate-tool**: Duplicate PDBQT files based on array length.
- **fix-side-chain-tool**: Model missing atoms in amino acid side chains of PDB files.
- **rename-residues-mol-tool**: Rename residues in MOL2 files.
- **extract-model-tool**: Extract models from 3D structures using the Structure Checking tool.
- **extract-model-pdbqt-tool**: Extract models from PDBQT files with multiple models.

### Format Conversion
- **convert-mol2-plugin**: Convert various file formats to MOL2 using Open Babel.
- **convert-pdbqt-tool**: Convert various file formats to PDB using Open Babel.
- **convert-xyz-plugin**: Convert various file formats to XYZ using Open Babel.

### Configuration
- **config-tag-mdp-tool**: Generate JSON-encoded configuration strings for molecular dynamics parameters.
- **config-tag-box-plugin**: Generate JSON-encoded configuration strings for box parameters.
- **config-tag-pdb2gmx-plugin**: Generate JSON-encoded configuration strings for pdb2gmx parameters.

### Development
- **mm-python-template**: Template for creating new Python-based molecular modeling tools.

## Installation and Usage
Each tool in the repository comes with its own set of installation and usage instructions. Please refer to the README file of each tool for detailed information on how to install and use it.

## Contributing
We welcome contributions to the MM Tools repository. If you have a new tool or improvement to existing tools, please follow the contribution guidelines outlined in the repository.

## License
This repository is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any questions or issues, please contact the repository maintainers or open an issue on GitHub.

---

Thank you for using MM Tools! We hope these tools enhance your molecular modeling workflows.