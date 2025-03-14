```json
{
  "repo_name": "mm-tools",
  "repo_description": "A collection of molecular modeling tools and plugins for various tasks such as structure manipulation, molecular dynamics, and data processing.",
  "tools": [
    {
      "name": "remove_terminal_residue_name_prefixes",
      "description": "A plugin to remove terminal residue name prefixes from PDB files.",
      "key_features": ["Removes prefixes from residue names in PDB files"],
      "usage_example": "remove_terminal_residue_name_prefixes --input_pdb_path input.pdb --output_pdb_path output.pdb"
    },
    {
      "name": "scatter_plot",
      "description": "Generates scatter plots from given data arrays.",
      "key_features": ["Creates scatter plots", "Supports multiple Y-axis data"],
      "usage_example": "scatter_plot --xs [1.0, 2.0, 3.0] --ys [4.0, 5.0, 6.0] --output_png_path plot.png"
    },
    {
      "name": "wget_xlsx",
      "description": "Downloads an XLSX file from a given URL.",
      "key_features": ["Downloads XLSX files"],
      "usage_example": "wget_xlsx --url http://example.com/file.xlsx --output_xlsx_path file.xlsx"
    },
    {
      "name": "gmx_trjconv_str",
      "description": "A wrapper for the GROMACS trjconv module to convert structure file formats and extract atom selections.",
      "key_features": ["Converts GROMACS structure files", "Extracts atom selections"],
      "usage_example": "gmx_trjconv_str --input_crd_path input.xtc --output_str_path output.pdb"
    },
    {
      "name": "sanitize_ligand",
      "description": "Handles molecules with RDKit errors gracefully.",
      "key_features": ["Sanitizes ligands", "Handles RDKit errors"],
      "usage_example": "sanitize_ligand --pattern '*.mol' --indir input_dir --outdir output_dir"
    },
    {
      "name": "fix_amides",
      "description": "Fixes amide groups in residues of PDB files.",
      "key_features": ["Fixes amide groups"],
      "usage_example": "fix_amides --input_pdb_path input.pdb --output_pdb_path output.pdb"
    },
    {
      "name": "check_linear_fit",
      "description": "Checks the linear fit of data points.",
      "key_features": ["Evaluates linear fit", "Supports tolerance and slope constraints"],
      "usage_example": "check_linear_fit --xs [1.0, 2.0, 3.0] --ys [4.0, 5.0, 6.0] --tol_quad 0.1"
    },
    {
      "name": "combine_structure",
      "description": "Combines two XYZ structures into a single PDB file using RDKit.",
      "key_features": ["Combines structures", "Outputs PDB format"],
      "usage_example": "combine_structure --input_structure1 file1.xyz --input_structure2 file2.xyz --output_structure_path combined.pdb"
    },
    {
      "name": "mm_python_template",
      "description": "A template for creating new molecular modeling tools with Python.",
      "key_features": ["Provides setup scripts", "Includes Docker and testing setup"],
      "usage_example": "Follow the setup instructions to create a new tool."
    },
    {
      "name": "pdb2gmx",
      "description": "A wrapper for the GROMACS pdb2gmx module to generate topology files.",
      "key_features": ["Generates topology files", "Supports multiple force fields"],
      "usage_example": "pdb2gmx --input_pdb_path input.pdb --output_crd_path output.gro"
    },
    {
      "name": "box",
      "description": "Sets the center and size of a box around residues or a pocket in a PDB file.",
      "key_features": ["Defines box dimensions", "Outputs annotated PDB"],
      "usage_example": "box --input_pdb_path input.pdb --output_pdb_path output.pdb"
    },
    {
      "name": "str_check_add_hydrogens",
      "description": "Adds hydrogens to a 3D structure using a structure checking tool.",
      "key_features": ["Adds hydrogens", "Supports PDB and PDBQT formats"],
      "usage_example": "str_check_add_hydrogens --input_structure_path input.pdb --output_structure_path output.pdb"
    },
    {
      "name": "gmx_rms_nofit",
      "description": "Performs RMSd analysis on GROMACS trajectories without fitting.",
      "key_features": ["RMSd analysis", "Supports multiple trajectory formats"],
      "usage_example": "gmx_rms_nofit --input_structure_path input.tpr --input_traj_path trajectory.xtc --output_xvg_path rmsd.xvg"
    },
    {
      "name": "convert_mol2",
      "description": "A wrapper for Open Babel to convert molecular formats to MOL2.",
      "key_features": ["Converts to MOL2 format", "Supports various input formats"],
      "usage_example": "convert_mol2 --input_path input.sdf --output_mol2_path output.mol2"
    },
    {
      "name": "extract_protein_openmm",
      "description": "Extracts protein from a PDB file using OpenMM.",
      "key_features": ["Extracts protein structures"],
      "usage_example": "extract_protein_openmm --input_pdb_path input.pdb --output_pdb_path protein.pdb"
    },
    {
      "name": "gmx_editconf",
      "description": "A wrapper for the GROMACS editconf module to modify structure files.",
      "key_features": ["Modifies structure files", "Supports box type and dimensions"],
      "usage_example": "gmx_editconf --input_crd_path input.gro --output_crd_path output.gro"
    },
    {
      "name": "genion",
      "description": "A wrapper for the GROMACS genion module to add ions to a system.",
      "key_features": ["Adds ions", "Supports topology updates"],
      "usage_example": "genion --input_tpr_path input.tpr --output_crd_path output.gro"
    },
    {
      "name": "config_tag_mdp",
      "description": "Generates a JSON-encoded string of MDP configuration arguments.",
      "key_features": ["Generates MDP config string"],
      "usage_example": "config_tag_mdp --nsteps 5000 --dt 0.002 --ref-t 300"
    },
    {
      "name": "mdrun",
      "description": "A wrapper for the GROMACS mdrun module to perform molecular dynamics simulations.",
      "key_features": ["Runs MD simulations", "Supports various output formats"],
      "usage_example": "mdrun --input_tpr_path input.tpr --output_crd_path output.gro"
    },
    {
      "name": "grompp",
      "description": "A wrapper for the GROMACS grompp module to preprocess input files for MD simulations.",
      "key_features": ["Preprocesses input files", "Generates TPR files"],
      "usage_example": "grompp --input_crd_path input.gro --output_tpr_path output.tpr"
    },
    {
      "name": "acpype",
      "description": "A wrapper for Acpype to generate topologies for GROMACS.",
      "key_features": ["Generates GROMACS topologies", "Supports multiple input formats"],
      "usage_example": "acpype --input_path input.mol2 --output_gro_path output.gro"
    },
    {
      "name": "sander_mdrun",
      "description": "A wrapper for the AmberTools sander module to run molecular dynamics simulations.",
      "key_features": ["Runs MD simulations with Amber", "Supports various output formats"],
      "usage_example": "sander_mdrun --input_top_path input.top --output_log_path output.log"
    },
    {
      "name": "process_mdout",
      "description": "A wrapper for the AmberTools process_mdout module to process MD output files.",
      "key_features": ["Processes MD output", "Generates data files"],
      "usage_example": "process_mdout --input_log_path input.log --output_dat_path output.dat"
    },
    {
      "name": "filter_array",
      "description": "Filters an array based on a boolean array.",
      "key_features": ["Filters arrays"],
      "usage_example": "filter_array --input_array [1, 2, 3] --input_bool_array [True, False, True]"
    },
    {
      "name": "random_subset_rows",
      "description": "Returns subset indices for an array using random sampling.",
      "key_features": ["Random sampling", "Generates subset indices"],
      "usage_example": "random_subset_rows --input_file data.csv --num_of_samples 10"
    },
    {
      "name": "array_indices",
      "description": "Returns a subset of an array based on input indices.",
      "key_features": ["Subsets arrays"],
      "usage_example": "array_indices --input_indices [0, 2] --input_array [1, 2, 3]"
    },
    {
      "name": "pdb4amber_run",
      "description": "A wrapper for the AmberTools pdb4amber module to prepare PDB files.",
      "key_features": ["Prepares PDB files for Amber"],
      "usage_example": "pdb4amber_run --input_pdb_path input.pdb --output_pdb_path output.pdb"
    },
    {
      "name": "solvate",
      "description": "A wrapper for the GROMACS solvate module to solvate a system.",
      "key_features": ["Solvates systems", "Updates topology"],
      "usage_example": "solvate --input_solute_crd_path input.gro --output_crd_path output.gro"
    },
    {
      "name": "generate_conformers_sdf",
      "description": "Uses Open Babel to generate and minimize conformers of small molecules.",
      "key_features": ["Generates conformers", "Minimizes structures"],
      "usage_example": "generate_conformers_sdf --input_path input.smi --output_sdf_path output.sdf"
    },
    {
      "name": "download_gdb9_database",
      "description": "Downloads MolGAN models and datasets.",
      "key_features": ["Downloads datasets"],
      "usage_example": "download_gdb9_database --output_sdf_path data.sdf"
    },
    {
      "name": "pdbbind_generate_conformers",
      "description": "Downloads the PDBbind refined database and generates conformers from SMILES.",
      "key_features": ["Downloads PDBbind", "Generates conformers"],
      "usage_example": "pdbbind_generate_conformers --input_excel_path data.xlsx --output_sdf_path conformers.sdf"
    },
    {
      "name": "pdb_tool",
      "description": "Downloads PDB files.",
      "key_features": ["Downloads PDB files"],
      "usage_example": "pdb_tool --config pdb_config.json --output_pdb_path output.pdb"
    },
    {
      "name": "zip_top",
      "description": "Zips GROMACS topology files.",
      "key_features": ["Zips topology files"],
      "usage_example": "zip_top --input_top_path topology.top --output_top_zip_path topology.zip"
    },
    {
      "name": "append_ligand",
      "description": "Inserts a ligand ITP file into a topology.",
      "key_features": ["Appends ligands to topology"],
      "usage_example": "append_ligand --input_top_zip_path topology.zip --input_itp_path ligand.itp"
    },
    {
      "name": "extract_ligand_protein",
      "description": "Extracts ligands and protein from a PDB file using OpenMM.",
      "key_features": ["Extracts ligands and proteins"],
      "usage_example": "extract_ligand_protein --input_pdb_path input.pdb --output_pdb_path protein.pdb"
    },
    {
      "name": "duplicate",
      "description": "Duplicates a PDBQT file n times.",
      "key_features": ["Duplicates PDBQT files"],
      "usage_example": "duplicate --input_pdbqt_singleton_path ligand.pdbqt --input_pdbqt_array_path array.pdbqt"
    },
    {
      "name": "fix_side_chain",
      "description": "Models missing atoms in amino acid side chains of a PDB.",
      "key_features": ["Fixes side chains"],
      "usage_example": "fix_side_chain --input_pdb_path input.pdb --output_pdb_path output.pdb"
    },
    {
      "name": "rename_residues_mol",
      "description": "Renames residues in a MOL2 file.",
      "key_features": ["Renames residues"],
      "usage_example": "rename_residues_mol --input_mol2_path input.mol2 --output_mol2_path output.mol2"
    },
    {
      "name": "extract_model",
      "description": "Extracts a model from a 3D structure.",
      "key_features": ["Extracts models"],
      "usage_example": "extract_model --input_structure_path input.pdb --output_structure_path output.pdb"
    },
    {
      "name": "extract_model_pdbqt",
      "description": "Extracts a model from a PDBQT file with several models.",
      "key_features": ["Extracts models from PDBQT"],
      "usage_example": "extract_model_pdbqt --input_pdbqt_path input.pdbqt --output_pdbqt_path output.pdbqt"
    },
    {
      "name": "convert_pdbqt",
      "description": "A wrapper for Open Babel to convert molecular formats to PDB.",
      "key_features": ["Converts to PDB format"],
      "usage_example": "convert_pdbqt --input_path input.sdf --output_pdb_path output.pdb"
    },
    {
      "name": "pdb_fixer",
      "description": "Fixes structural issues in proteins.",
      "key_features": ["Fixes protein structures"],
      "usage_example": "pdb_fixer --input_pdb_path input.pdb --output_pdb_path fixed.pdb"
    },
    {
      "name": "pose_cluster_filter",
      "description": "Clusters poses in protein and selects the most confident pose for each cluster.",
      "key_features": ["Clusters poses", "Filters poses"],
      "usage_example": "pose_cluster_filter --centroid_cutoff 1.0 --predicted_poses poses.pdbqt"
    },
    {
      "name": "autodock_vina_run",
      "description": "A wrapper for the AutoDock Vina software for molecular docking.",
      "key_features": ["Performs molecular docking"],
      "usage_example": "autodock_vina_run --input_ligand_pdbqt_path ligand.pdbqt --input_receptor_pdbqt_path receptor.pdbqt"
    },
    {
      "name": "config_tag_box",
      "description": "Generates a JSON-encoded string for box configuration.",
      "key_features": ["Generates box config string"],
      "usage_example": "config_tag_box --offset 1.0"
    },
    {
      "name": "gmx_energy",
      "description": "Extracts energy components from a GROMACS energy file.",
      "key_features": ["Extracts energy components"],
      "usage_example": "gmx_energy --input_energy_path energy.edr --output_xvg_path energy.xvg"
    },
    {
      "name": "editconf",
      "description": "A wrapper for the GROMACS editconf module to modify structure files.",
      "key_features": ["Modifies structure files"],
      "usage_example": "editconf --input_crd_path input.gro --output_crd_path output.gro"
    },
    {
      "name": "convert_xyz",
      "description": "A wrapper for Open Babel to convert molecular formats to XYZ.",
      "key_features": ["Converts to XYZ format"],
      "usage_example": "convert_xyz --input_path input.pdb --output_xyz_path output.xyz"
    },
    {
      "name": "config_tag_pdb2gmx",
      "description": "Generates a JSON-encoded string for pdb2gmx configuration.",
      "key_features": ["Generates pdb2gmx config string"],
      "usage_example": "config_tag_pdb2gmx --water_type spc --forcefield amber99"
    }
  ],
  "unified_readme": "# mm-tools\n\nA collection of molecular modeling tools and plugins for various tasks such as structure manipulation, molecular dynamics, and data processing.\n\n## Tools Overview\n\n### remove_terminal_residue_name_prefixes\n- **Description**: A plugin to remove terminal residue name prefixes from PDB files.\n- **Key Features**: Removes prefixes from residue names in PDB files\n- **Usage Example**: `remove_terminal_residue_name_prefixes --input_pdb_path input.pdb --output_pdb_path output.pdb`\n\n### scatter_plot\n- **Description**: Generates scatter plots from given data arrays.\n- **Key Features**: Creates scatter plots, Supports multiple Y-axis data\n- **Usage Example**: `scatter_plot --xs [1.0, 2.0, 3.0] --ys [4.0, 5.0, 6.0] --output_png_path plot.png`\n\n### wget_xlsx\n- **Description**: Downloads an XLSX file from a given URL.\n- **Key Features**: Downloads XLSX files\n- **Usage Example**: `wget_xlsx --url http://example.com/file.xlsx --output_xlsx_path file.xlsx`\n\n### gmx_trjconv_str\n- **Description**: A wrapper for the GROMACS trjconv module to convert structure file formats and extract atom selections.\n- **Key Features**: Converts GROMACS structure files, Extracts atom selections\n- **Usage Example**: `gmx_trjconv_str --input_crd_path input.xtc --output_str_path output.pdb`\n\n### sanitize_ligand\n- **Description**: Handles molecules with RDKit errors gracefully.\n- **Key Features**: Sanitizes ligands, Handles RDKit errors\n- **Usage Example**: `sanitize_ligand --pattern '*.mol' --indir input_dir --outdir output_dir`\n\n### fix_amides\n- **Description**: Fixes amide groups in residues of PDB files.\n- **Key Features**: Fixes amide groups\n- **Usage Example**: `fix_amides --input_pdb_path input.pdb --output_pdb_path output.pdb`\n\n### check_linear_fit\n- **Description**: Checks the linear fit of data points.\n- **Key Features**: Evaluates linear fit, Supports tolerance and slope constraints\n- **Usage Example**: `check_linear_fit --xs [1.0, 2.0, 3.0] --ys [4.0, 5.0, 6.0] --tol_quad 0.1`\n\n### combine_structure\n- **Description**: Combines two XYZ structures into a single PDB file using RDKit.\n- **Key Features**: Combines structures, Outputs PDB format\n- **Usage Example**: `combine_structure --input_structure1 file1.xyz --input_structure2 file2.xyz --output_structure_path combined.pdb`\n\n### mm_python_template\n- **Description**: A template for creating new molecular modeling tools with Python.\n- **Key Features**: Provides setup scripts, Includes Docker and testing setup\n- **Usage Example**: Follow the setup instructions to create a new tool.\n\n### pdb2gmx\n- **Description**: A wrapper for the GROMACS pdb2gmx module to generate topology files.\n- **Key Features**: Generates topology files, Supports multiple force fields\n- **Usage Example**: `pdb2gmx --input_pdb_path input.pdb --output_crd_path output.gro`\n\n### box\n- **Description**: Sets the center and size of a box around residues or a pocket in a PDB file.\n- **Key Features**: Defines box dimensions, Outputs annotated PDB\n- **Usage Example**: `box --input_pdb_path input.pdb --output_pdb_path output.pdb`\n\n### str_check_add_hydrogens\n- **Description**: Adds hydrogens to a 3D structure using a structure checking tool.\n- **Key Features**: Adds hydrogens, Supports PDB and PDBQT formats\n- **Usage Example**: `str_check_add_hydrogens --input_structure_path input.pdb --output_structure_path output.pdb`\n\n### gmx_rms_nofit\n- **Description**: Performs RMSd analysis on GROMACS trajectories without fitting.\n- **Key Features**: RMSd analysis, Supports multiple trajectory formats\n- **Usage Example**: `gmx_rms_nofit --input_structure_path input.tpr --input_traj_path trajectory.xtc --output_xvg_path rmsd.xvg`\n\n### convert_mol2\n- **Description**: A wrapper for Open Babel to convert molecular formats to MOL2.\n- **Key Features**: Converts to MOL2 format, Supports various input formats\n- **Usage Example**: `convert_mol2 --input_path input.sdf --output_mol2_path output.mol2`\n\n### extract_protein_openmm\n- **Description**: Extracts protein from a PDB file using OpenMM.\n- **Key Features**: Extracts protein structures\n- **Usage Example**: `extract_protein_openmm --input_pdb_path input.pdb --output_pdb_path protein.pdb`\n\n### gmx_editconf\n- **Description**: A wrapper for the GROMACS editconf module to modify structure files.\n- **Key Features**: Modifies structure files, Supports box type and dimensions\n- **Usage Example**: `gmx_editconf --input_crd_path input.gro --output_crd_path output.gro`\n\n### genion\n- **Description**: A wrapper for the GROMACS genion module to add ions to a system.\n- **Key Features**: Adds ions, Supports topology updates\n- **Usage Example**: `genion --input_tpr_path input.tpr --output_crd_path output.gro`\n\n### config_tag_mdp\n- **Description**: Generates a JSON-encoded string of MDP configuration arguments.\n- **Key Features**: Generates MDP config string\n- **Usage Example**: `config_tag_mdp --nsteps 5000 --dt 0.002 --ref-t 300`\n\n### mdrun\n- **Description**: A wrapper for the GROMACS mdrun module to perform molecular dynamics simulations.\n- **Key Features**: Runs MD simulations, Supports various output formats\n- **Usage Example**: `mdrun --input_tpr_path input.tpr --output_crd_path output.gro`\n\n### grompp\n- **Description**: A wrapper for the GROMACS grompp module to preprocess input files for MD simulations.\n- **Key Features**: Preprocesses input files, Generates TPR files\n- **Usage Example**: `grompp --input_crd_path input.gro --output_tpr_path output.tpr`\n\n### acpype\n- **Description**: A wrapper for Acpype to generate topologies for GROMACS.\n- **Key Features**: Generates GROMACS topologies, Supports multiple input formats\n- **Usage Example**: `acpype --input_path input.mol2 --output_gro_path output.gro`\n\n### sander_mdrun\n- **Description**: A wrapper for the AmberTools sander module to run molecular dynamics simulations.\n- **Key Features**: Runs MD simulations with Amber, Supports various output formats\n- **Usage Example**: `sander_mdrun --input_top_path input.top --output_log_path output.log`\n\n### process_mdout\n- **Description**: A wrapper for the AmberTools process_mdout module to process MD output files.\n- **Key Features**: Processes MD output, Generates data files\n- **Usage Example**: `process_mdout --input_log_path input.log --output_dat_path output.dat`\n\n### filter_array\n- **Description**: Filters an array based on a boolean array.\n- **Key Features**: Filters arrays\n- **Usage Example**: `filter_array --input_array [1, 2, 3] --input_bool_array [True, False, True]`\n\n### random_subset_rows\n- **Description**: Returns subset indices for an array using random sampling.\n- **Key Features**: Random sampling, Generates subset indices\n- **Usage Example**: `random_subset_rows --input_file data.csv --num_of_samples 10`\n\n### array_indices\n- **Description**: Returns a subset of an array based on input indices.\n- **Key Features**: Subsets arrays\n- **Usage Example**: `array_indices --input_indices [0, 2] --input_array [1, 2, 3]`\n\n### pdb4amber_run\n- **Description**: A wrapper for the AmberTools pdb4amber module to prepare PDB files.\n- **Key Features**: Prepares PDB files for Amber\n- **Usage Example**: `pdb4amber_run --input_pdb_path input.pdb --output_pdb_path output.pdb`\n\n### solvate\n- **Description**: A wrapper for the GROMACS solvate module to solvate a system.\n- **Key Features**: Solvates systems, Updates topology\n- **Usage Example**: `solvate --input_solute_crd_path input.gro --output_crd_path output.gro`\n\n### generate_conformers_sdf\n- **Description**: Uses Open Babel to generate and minimize conformers of small molecules.\n- **Key Features**: Generates conformers, Minimizes structures\n- **Usage Example**: `generate_conformers_sdf --input_path input.smi --output_sdf_path output.sdf`\n\n### download_gdb9_database\n- **Description**: Downloads MolGAN models and datasets.\n- **Key Features**: Downloads datasets\n- **Usage Example**: `download_gdb9_database --output_sdf_path data.sdf`\n\n### pdbbind_generate_conformers\n- **Description**: Downloads the PDBbind refined database and generates conformers from SMILES.\n- **Key Features**: Downloads PDBbind, Generates conformers\n- **Usage Example**: `pdbbind_generate_conformers --input_excel_path data.xlsx --output_sdf_path conformers.sdf`\n\n### pdb_tool\n- **Description**: Downloads PDB files.\n- **Key Features**: Downloads PDB files\n- **Usage Example**: `pdb_tool --config pdb_config.json --output_pdb_path output.pdb`\n\n### zip_top\n- **Description**: Zips GROMACS topology files.\n- **Key Features**: Zips topology files\n- **Usage Example**: `zip_top --input_top_path topology.top --output_top_zip_path topology.zip`\n\n### append_ligand\n- **Description**: Inserts a ligand ITP file into a topology.\n- **Key Features**: Appends ligands to topology\n- **Usage Example**: `append_ligand --input_top_zip_path topology.zip --input_itp_path ligand.itp`\n\n### extract_ligand_protein\n- **Description**: Extracts ligands and protein from a PDB file using OpenMM.\n- **Key Features**: Extracts ligands and proteins\n- **Usage Example**: `extract_ligand_protein --input_pdb_path input.pdb --output_pdb_path protein.pdb`\n\n### duplicate\n- **Description**: Duplicates a PDBQT file n times.\n- **Key Features**: Duplicates PDBQT files\n- **Usage Example**: `duplicate --input_pdbqt_singleton_path ligand.pdbqt --input_pdbqt_array_path array.pdbqt`\n\n### fix_side_chain\n- **Description**: Models missing atoms in amino acid side chains of a PDB.\n- **Key Features**: Fixes side chains\n- **Usage Example**: `fix_side_chain --input_pdb_path input.pdb --output_pdb_path output.pdb`\n\n### rename_residues_mol\n- **Description**: Renames residues in a MOL2 file.\n- **Key Features**: Renames residues\n- **Usage Example**: `rename_residues_mol --input_mol2_path input.mol2 --output_mol2_path output.mol2`\n\n### extract_model\n- **Description**: Extracts a model from a 3D structure.\n- **Key Features**: Extracts models\n- **Usage Example**: `extract_model --input_structure_path input.pdb --output_structure_path output.pdb`\n\n### extract_model_pdbqt\n- **Description**: Extracts a model from a PDBQT file with several models.\n- **Key Features**: Extracts models from PDBQT\n- **Usage Example**: `extract_model_pdbqt --input_pdbqt_path input.pdbqt --output_pdbqt_path output.pdbqt`\n\n### convert_pdbqt\n- **Description**: A wrapper for Open Babel to convert molecular formats to PDB.\n- **Key Features**: Converts to PDB format\n- **Usage Example**: `convert_pdbqt --input_path input.sdf --output_pdb_path output.pdb`\n\n### pdb_fixer\n- **Description**: Fixes structural issues in proteins.\n- **Key Features**: Fixes protein structures\n- **Usage Example**: `pdb_fixer --input_pdb_path input.pdb --output_pdb_path fixed.pdb`\n\n### pose_cluster_filter\n- **Description**: Clusters poses in protein and selects the most confident pose for each cluster.\n- **Key Features**: Clusters poses, Filters poses\n- **Usage Example**: `pose_cluster_filter --centroid_cutoff 1.0 --predicted_poses poses.pdbqt`\n\n### autodock_vina_run\n- **Description**: A wrapper for the AutoDock Vina software for molecular docking.\n- **Key Features**: Performs molecular docking\n- **Usage Example**: `autodock_vina_run --input_ligand_pdbqt_path ligand.pdbqt --input_receptor_pdbqt_path receptor.pdbqt`\n\n### config_tag_box\n- **Description**: Generates a JSON-encoded string for box configuration.\n- **Key Features**: Generates box config string\n- **Usage Example**: `config_tag_box --offset 1.0`\n\n### gmx_energy\n- **Description**: Extracts energy components from a GROMACS energy file.\n- **Key Features**: Extracts energy components\n- **Usage Example**: `gmx_energy --input_energy_path energy.edr --output_xvg_path energy.xvg`\n\n### editconf\n- **Description**: A wrapper for the GROMACS editconf module to modify structure files.\n- **Key Features**: Modifies structure files\n- **Usage Example**: `editconf --input_crd_path input.gro --output_crd_path output.gro`\n\n### convert_xyz\n- **Description**: A wrapper for Open Babel to convert molecular formats to XYZ.\n- **Key Features**: Converts to XYZ format\n- **Usage Example**: `convert_xyz --input_path input.pdb --output_xyz_path output.xyz`\n\n### config_tag_pdb2gmx\n- **Description**: Generates a JSON-encoded string for pdb2gmx configuration.\n- **Key Features**: Generates pdb2gmx config string\n- **Usage Example**: `config_tag_pdb2gmx --water_type spc --forcefield amber99`\n"
}
```