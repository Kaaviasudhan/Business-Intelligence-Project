# Business-Intelligence-Project
Steam Spy API Data Analysis: A Python project leveraging Steam Spy API to retrieve and analyze data on video games, implementing OLAP operations such as slicing and dicing to gain insights into game attributes.

# Steam Spy API Data Analysis

This Python project utilizes the Steam Spy API to retrieve and analyze data on video games available on the Steam platform. It implements OLAP (Online Analytical Processing) operations such as slicing and dicing to gain insights into various game attributes.

## Features

- Retrieve data from the Steam Spy API.
- Perform OLAP operations including slicing and dicing.
- Analyze game attributes such as positive and negative reviews, average playtime, developers, and publishers.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Python scripts to perform data retrieval and analysis.

## File Structure

- `steam_spy_api.py`: Python script to interact with the Steam Spy API and retrieve data.
- `README.md`: Documentation file providing information about the project.

## Requirements

- Python 3.x
- Requests library
- Kibana *
- Elasticsearch *

Note: (*)
Cloud Deployment:
For cloud deployment of the project, leverage Elastic's cloud services available at Elastic Cloud. [Visit Elastic's cloud services](https://www.elastic.co/cloud/)

Local Deployment:
For local deployment of this project, ensure to download and install Kibana and Elasticsearch. You can download Kibana from here and Elasticsearch from here. <br>The project utilizes version 8.12.x; however, feel free to proceed with an upgraded version if available.
  * For kibana Download Visit this website: [Kibana Download](https://www.elastic.co/downloads/elasticsearch)
  * For Elasticsearch Download Visit this website: [Elasticsearch Download](https://www.elastic.co/downloads/elasticsearch)

## Work Flow
Workflow Steps for Cloud Deployment:

- 1. Access the Elasticsearch cloud website.
- 2. Open Kibana.
- 3. Execute the Python script, ensuring correct entry of Elasticsearch endpoint, username, and password.
- 4. Navigate to Kibana, proceed to Stock Management, then Index Management, and view the Indices, including source size.
- 5. Analyze and manipulate the data to prepare the dashboard.

## Disclaimer
This project is for educational purposes only. It is not intended for commercial use. All data retrieved from the Steam Spy API is for analysis and learning purposes.


[video_About this_project](https://github.com/Kaaviasudhan/Business-Intelligence-Project/assets/75906178/70c3b3c9-6b92-43cb-a3a8-84fcc4207d88)

** Output:
![my-deployment-f6c6a7 kb us-central1 gcp cloud es io_9243_app_dashboards (2)](https://github.com/Kaaviasudhan/Business-Intelligence-Project/assets/75906178/47bf584f-2130-4e30-8408-8a7c69c08826)




