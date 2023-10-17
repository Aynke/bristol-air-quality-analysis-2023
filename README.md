#  Bristol-Air-quality-analysis

A brief description of your project.

## Table of Contents
- [Project Title](#project-title)
- [Description](#description)
- [Demo](#demo)
- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description

# Air Quality Monitoring for Nitrogen Dioxide (NO2)

This project is focused on monitoring the air quality in Bristol, United Kingdom with a specific emphasis on Nitrogen Dioxide (NO2). Airborne pollutants like Nitrogen Monoxide (NO), Nitrogen Dioxide (NO2), and particulate matter significantly impact overall air quality. We specifically measure NO2 in micrograms per cubic meter (㎍/m3), with a microgram being one-millionth of a gram. For context, a concentration of 1 ㎍/m3 indicates that one cubic meter of air contains one microgram of NO2.

The UK Government, in its Air Quality Strategy, has established two key air quality objectives for NO2:

1. **Hourly Objective**: This is the concentration of NO2 in the air, averaged over a period of one hour.

2. **Annual Objective**: This is the concentration of NO2 in the air, averaged over a year.

In the context of this project, we provide a color-coded table that illustrates the levels and corresponding color encoding for Objective 1, the mean hourly ratio. This information is critical for understanding and maintaining air quality standards in the UK.

By monitoring and presenting this data, we aim to contribute to the protection of public health and promote awareness of air quality in the region.The following table shows the colour encoding and the levels for Objective 1 above, the mean hourly ratio, adopted in the UK.

![image](https://github.com/Aynke/bristol-air-quality-analysis-2023/assets/105416349/74427f6e-69eb-4f31-a2cd-cf3b8f9f831a)


## Demo


**Input Data**

The provided ZIP file contains data spanning from 2004 to February 7, 2023, collected from 19 monitoring stations in and around Bristol.

Please follow these steps to access and work with the data:

1. **Download and Save the Data**:
   - Download the data file named "air-quality-data-2003-2022.zip" (21 Mb).

2. **Unzip the Data**:
   - Extract the contents of the ZIP file, which will yield a CSV file named "air-quality-data-2003-2022.csv" (258 Mb).

Below, you can find the first 8 lines of the file, providing a glimpse of the data:


*Note the following:*

- There are 19 monitoring stations, each identified by a unique code:
  - 188 => 'AURN Bristol Centre'
  - 203 => 'Brislington Depot'
  - 206 => 'Rupert Street'
  - 209 => 'IKEA M32'
  - 213 => 'Old Market'
  - 215 => 'Parson Street School'
  - 228 => 'Temple Meads Station'
  - 270 => 'Wells Road'
  - 271 => 'Trailer Portway P&R'
  - 375 => 'Newfoundland Road Police Station'
  - 395 => "Shiner's Garage"
  - 452 => 'AURN St Pauls'
  - 447 => 'Bath Road'
  - 459 => 'Cheltenham Road \ Station Road'
  - 463 => 'Fishponds Road'
  - 481 => 'CREATE Centre Roof'
  - 500 => 'Temple Way'
  - 501 => 'Colston Avenue'
  - 672 => 'Marlborough Street'

- Each line represents a reading from a specific detector, with detectors taking readings once every hour. The data file contains headers in the first row, followed by a substantial 1.52 million+ rows (lines), each containing 23 data items (columns).

The schema for the data is outlined below:
![image](https://github.com/Aynke/bristol-air-quality-analysis-2023/assets/105416349/748322b6-d5db-4a81-aee6-bb200745d664)


## Tools
- Python
- SQL
- Tableau
- etc

## Features

Data Processing:

Process and convert substantial real-world data (258mb+) through Python scripts, including modeling, cropping, cleansing, and normalization.
Gain hands-on experience in data processing by writing Python scripts to create cleansed CSV and normalized SQL data.
Relational Database Integration:

Design and implement a MySQL relational database.
Utilize a Python script to import cleansed data into the appropriate tables while ensuring data integrity constraints are maintained.
Efficient Data Extraction:

Construct and implement SQL queries to extract data using a variety of filters and constraints, enabling precise data retrieval.
NoSQL Integration:

Forward engineer data to a NoSQL database of your choice, such as MongoDB, BaseX, CouchBase, ArangoDB, or others.

## Installation

Provide instructions on how to install and set up your project on a user's machine. Include any dependencies that need to be installed and how to install them.

# Contributing to the Repository

## Forking the Repository
To start contributing to this project, the first step is to fork the repository. Forking creates your own copy of the repository, allowing you to make changes without affecting the main project. You can later submit your changes for review and integration. If you're new to forking, you can follow [this tutorial](tutorial-link) for detailed guidance.

## Cloning the Repository to Your Local Machine
Once you've forked the repository, you should clone it to your local machine. This step is essential for working on the project. Here's how to do it:

1. Copy the link of your forked repository.
2. Open the folder on your local machine where you want to work.
3. Open your preferred code editor (e.g., VSCode).
4. Launch your terminal.
5. Run the following command to clone the repository:

   ```bash
   git clone [Link to your forked repository]
   ```

   The link should resemble this format: `https://github.com/YourUsername/YourRepository`.

## Configuring the Upstream
As multiple developers contribute to the project, it's crucial to keep your local copy up-to-date with the original repository. To achieve this, configure your local copy to connect to the original repository:

1. Open your terminal in the project folder on your local machine.
2. Run the following command to add the upstream repository as a remote:

   ```bash
   git remote add upstream [Link to the original repository]
   ```

   This ensures you can easily update your local copy with the latest changes from the main repository.

## Making and Committing Changes
Now that your local copy is set up, you can start making changes that address your designated issues. Follow these steps for making and committing your changes:

1. Add your changes using `git add .` or any method that suits your workflow (e.g., GitHub Desktop or VSCode source control).
2. Provide a concise commit message, like this:

   ```bash
   git commit -m "Adds a signup button to the sign-up page"
   ```

3. Push your changes to your online repository:

   ```bash
   git push origin
   ```

   This action updates your online copy, preparing it for the next step.

## Opening Pull Requests
Once your online copy is updated, it's time to inform the Pull Request (PR) Lead handling the original repository that your contributions are ready for review and integration. To do this, open a Pull Request:

1. Navigate to your GitHub account and access your repository.
2. Look for the option to open a pull request.
3. Change the base repository branch to `develop`.
4. Explain the purpose and impact of your changes.
5. Click the "Open Pull Request" button and patiently await feedback and integration.

## Keeping Your Local Copy Updated
To stay up-to-date and prevent conflicts, it's essential to update your local copy before making changes. Whenever you intend to work on the project, run the following command:

1. In the project directory on your local machine, open the terminal.
2. Execute the following command to fetch and merge changes from the original repository:

   ```bash
   git pull upstream develop
   ```

   This command checks for changes in the original repository and applies them to your local copy, ensuring your work is based on the latest project version.

