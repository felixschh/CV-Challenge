# Self Driving Car Lane Detection

[![OS](https://img.shields.io/badge/OS-Windows|macOS-yellow.svg?longCache=true&style=flat-square)](https://www.microsoft.com/de-de/windows/windows-11-45434254328)
[![openCV 4.5.5](https://img.shields.io/badge/openCV-4.5.5-red.svg?longCache=true&style=flat-square)](https://docs.opencv.org/4.5.5/d4/db1/tutorial_documentation.html)
[![NumPy 1.22.3](https://img.shields.io/badge/NumPy-1.22.3-green.svg?longCache=true&style=flat-square)](https://numpy.org/doc/stable/)
[![Matplotlib 3.5.1](https://img.shields.io/badge/Matplotlib-3.5.1-blue.svg?longCache=true&style=flat-square)](https://matplotlib.org/stable/)

Our Project is about lane-recognition as one part of autonomous driving. We used some example pictures and videos for this.
First we greyscaled the original image, then we used the `Canny-method` for edge detection and applied mask and cropped the region with the lanes to detect.
After that we used HoughLines to the render points of the lines and used those ponits to create lines as a mask on the original image.

### 📦 *Installation*

Install the required libraries into the the environment. Using the line below we can install the libraries.
You check the versions from the `requirements.txt`


```bash
pip install -r requirements.txt
```
### 🚀 *How to use*

Initially we have to import the libraries
```python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
```

The Original Image
![c2503606-d5c4-45af-81d7-a4cf89254236](https://user-images.githubusercontent.com/71933145/164476465-4c77232c-a209-48e2-95b8-b1998af88605.png)
Grayscale image
![d795852e-f969-43b9-8898-b1e2f000f9e0](https://user-images.githubusercontent.com/71933145/164474630-db003b5c-44a1-4e1b-8211-983865427fbc.png)
After Canny Kernel
![0667ef48-0d08-40be-a3e5-f96f2fcab647](https://user-images.githubusercontent.com/71933145/164474807-89e4fdcd-ba41-4fc6-b2eb-82c183459b41.png)
![8a2e8e70-1a49-4ef7-bde0-11ac743f705e](https://user-images.githubusercontent.com/71933145/164474985-4ef6c9d7-adc7-44c8-bb85-c4f8efe9e883.png)
![7b886a99-d789-4ea7-8cbb-c13f796ee976](https://user-images.githubusercontent.com/71933145/164476219-7f290229-0ab5-4bae-bc3c-2f196a6493d1.png)
