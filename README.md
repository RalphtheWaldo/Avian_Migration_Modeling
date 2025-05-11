# Avian Migration Modeling

This project models bird migration patterns using data from **eBird** (a citizen science platform) and various **environmental variables**. The aim is to uncover trends in species distribution and migration patterns, with potential applications in ecology, conservation, and environmental science.

## Table of Contents

- [Overview](#overview)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Future Features](#future-features)

## Overview

The **Avian Migration Modeling** project uses statistical modeling and data science techniques to analyze bird migration patterns. The main goal is to integrate eBird data with environmental variables and sighting data to identify factors influencing bird movement and migration.

## Installation Instructions

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone git@github.com:RalphtheWaldo/avian_migration_modeling.git

## Usage

After installing the dependencies, you can run the main script to start analyzing bird sighting patterns.

apppropriate data can be stored in the 'Data' folder. The folder path should be updated in the variable ebird_path in app.py.

Run the main app script:
python main.py

Check data sources:
The project integrates data from eBird and environmental datasets. You can access the raw data in the /data directory.

## Contributing

Contributions to this project are welcome! If you have suggestions, bug fixes, or enhancements, please feel free to:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Features

Add weather data for specific locations to provide probabilities on common or rare species
Add Distance travelded per outing
Add full data for comparision against individual observations to caclulate probabiities
Add functionality to read Data directory so individual variables dont have to be set upon download