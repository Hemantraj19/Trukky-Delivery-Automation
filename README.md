# Trukky Door-to-Door Goods Delivery Automation

This script automates the process of booking a door-to-door goods delivery service on the Trukky platform using Selenium and Chrome WebDriver.

## Prerequisites

- Python installed on your machine
- Selenium library installed (`pip install selenium`)
- Chrome WebDriver installed and its path added to system environment variables

## Usage

1. Clone the repository or download the script file.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the script using `python trukky_delivery_automation.py`.

## Script Explanation

- The script uses Selenium with Chrome WebDriver to automate the steps of booking a delivery service on Trukky.
- It fills in pickup and drop locations, selects service type, adds materials, chooses the delivery date, and completes the booking process.
- The script pauses at various steps to allow time for elements to load using `time.sleep()`.

## Instructions

1. Ensure you have a stable internet connection.
2. Review the script and update it if there are any changes in the Trukky website structure.
3. Provide the required information like pickup and drop locations, phone number, and OTP during script execution.

## Important Note

- This script is provided as-is and may require adjustments if there are changes to the Trukky website structure.
