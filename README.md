[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">HITL LlamaIndex Django</h3>

  <p align="center">
    Human In The Loop (HITL) implementation with LlamaIndex using Django Channels websockets.
    <br />
    <a href="https://github.com/SAGAR-TAMANG/hitl-llama_index-django/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SAGAR-TAMANG/hitl-llama_index-django/issues">Report Bug</a>
    ·
    <a href="https://github.com/SAGAR-TAMANG/hitl-llama_index-django/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A ChatGPT-like interface implementing Human-In-The-Loop (HITL) functionality using LlamaIndex and Django Channels. This project enables real-time interaction through websockets while leveraging LlamaIndex's HITL capabilities for enhanced AI responses.

### Built With

* Django
* Django Channels
* LlamaIndex
* Websockets
* HTML/CSS/JavaScript
* Bootstrap 5.3

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get started with the project locally, follow these steps:

### Prerequisites

* Python 3.8+
* pip
* virtualenv

### Installation

1. Clone the repo
```sh
git clone https://github.com/SAGAR-TAMANG/hitl-llama_index-django.git
```

2. Create and activate virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```sh
pip install -r requirements.txt
```

4. Run migrations
```sh
python manage.py migrate
```

5. Start the development server
```sh
python manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Basic Django Channels setup
- [x] LlamaIndex integration
- [x] HITL implementation
- [ ] User authentication
- [ ] Multiple chat sessions
- [ ] Response history

See the [open issues](https://github.com/SAGAR-TAMANG/hitl-llama_index-django/issues) for proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open-source community thrive. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Sagar Tamang - [LinkedIn](https://www.linkedin.com/in/sagar-tmg/) - cs22bcagn033@kazirangauniversity.in

Project Link: [https://github.com/SAGAR-TAMANG/hitl-llama_index-django](https://github.com/SAGAR-TAMANG/hitl-llama_index-django)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/SAGAR-TAMANG/hitl-llama_index-django.svg?style=for-the-badge
[contributors-url]: https://github.com/SAGAR-TAMANG/hitl-llama_index-django/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SAGAR-TAMANG/hitl-llama_index-django.svg?style=for-the-badge
[forks-url]: https://github.com/SAGAR-TAMANG/hitl-llama_index-django/network/members
[stars-shield]: https://img.shields.io/github/stars/SAGAR-TAMANG/hitl-llama_index-django.svg?style=for-the-badge
[stars-url]: https://github.com/SAGAR-TAMANG/hitl-llama_index-django/stargazers
[issues-shield]: https://img.shields.io/github/issues/SAGAR-TAMANG/hitl-llama_index-django.svg?style=for-the-badge
[issues-url]: https://github.com/SAGAR-TAMANG/hitl-llama_index-django/issues
[license-shield]: https://img.shields.io/github/license/SAGAR-TAMANG/hitl-llama_index-django.svg?style=for-the-badge
[license-url]: https://github.com/SAGAR-TAMANG/hitl-llama_index-django/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sagar-tmg/