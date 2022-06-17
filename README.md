
<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  
<h3 align="center">PDGA Tournament Updater</h3>

  <p align="center">
    Sends Text Updates of a PDGA Tournament results at 5:00pm Thursday,Friday,Saturday and Sunday. If you don't know what the PDGA is it is the Pro Disc Golf Association
    <br />
    <a href="https://github.com/wgallagher44/PDGA-Tournament-Updater"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wgallagher44/PDGA-Tournament-Updater">View Demo</a>
    ·
    <a href="https://github.com/wgallagher44/PDGA-Tournament-Updater/issues">Report Bug</a>
    ·
    <a href="https://github.com/wgallagher44/PDGA-Tournament-Updater/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

PDGA Tournament Updater is built with python. It Utilizes two python libraries BeautifulSoup which is a python library for web scrapping I used this to get the result data from the tournament. The other library I used for this project is the schedule and time library this allows me to let a function run a specific time. Another part of this project I used was the use of the Twilio Api which allows me to send text messages to a phone number. The last part is a way to have this python running all the time. I created a server with Replit but they would only allow me to have the server active for an hour to get around this I used uptime robot which pings the server every 5 minutes which lets the server constantly run.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Twilio](https://www.twilio.com/)
* [BeautifulSoup](https://vuejs.org/)
* [Schedule](https://schedule.readthedocs.io/en/stable/)
* [Replit](https://replit.com/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [uptimerobot](https://uptimerobot.com/)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To be able to test out this project yourself your going have to do the following steps

### Prerequisites

First install Python on your machine if your on linux you can do the command below

* Python 

  ```sh
  sudo apt install python@latest-version
  ```

### Installation

1. Create a Twilio Account [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio)
2. Clone the repo

   ```sh
   git clone https://github.com/wgallagher44/PDGA-Tournament-Updater.git
   ```

3. Install Pip 

   ```sh
   For Windows
   pip install package_name
   Linux
   sudo apt install python3-pip
   ```

4. Install necessary Libraries For the project

   ```sh
   pip install schedule
   pip install beautifulsoup4
   pip install flask
   ```
5. Add twilio information and phone number
  ```py
  account_sid = 'your twilio sid'
  auth_token = 'your auth token'
  from_ = 'twilio phone number'
  to = 'Phone number your trying to send to'
  ```
6. The last step is run it [replit](https://replit.com/) and copy link from the run into [uptimerobot](https://uptimerobot.com/)
<p align="right">(<a href="#top">back to top</a>)</p>

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

See the [open issues](https://github.com/wgallagher44/PDGA-Tournament-Updater/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* willgallagher0702@gmail.com

## Project Link

 [https://github.com/wgallagher44/PDGA-Tournament-Updater](https://github.com/wgallagher44/PDGA-Tournament-Updater)

<p align="right">(<a href="#top">back to top</a>)</p>
