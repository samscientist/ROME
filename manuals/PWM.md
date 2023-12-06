
## Using PWM in Jetson Orin Nano with PCA9685






### Hardware connection of PCA9685



How to connect PCA9685 by I2C [^1.1] [^1.2] [^1.3]


```bash
sudo i2cdetect -r -y 7
```


*Output*
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --  
```




### Setting to using PCA9685

#### Install Anaconda


```bash
conda activate <environment name>

conda install pip # Need to check if this command is really needed
```
> *Currently, conda environment is useless. When executing Python file, prompts that no `Jetson` module is found. So, currently, working on the original environment.*

#### Install Python Package
```bash
sudo apt install python3-pip
sudo pip install adafruit-circuitpython-lis3dh
sudo pip install adafruit-circuitpython-motor
```

#### Import Modules
```python
import board
import busio
```
Error could occur by the Python code above even with proper package installation. Mainly caused from not available to find the modules. In this case, seek if the Python interpreter(or virtual environment) you're using is the one that the package is installed.



## Reference
- [^1.1]: [Jetson Orin Nano Pinmap and how to detect I2C](https://jetsonhacks.com/nvidia-jetson-orin-nano-gpio-header-pinout)
- [⭐ How to use PCA9685](https://cdn-learn.adafruit.com/downloads/pdf/micropython-hardware-pca9685-dc-motor-and-stepper-driver.pdf#page=8)
    - ['Adafruit_CircuitPython_Bundle' Repo](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)


[^1.2]: [How to connect the pins](https://learn.adafruit.com/16-channel-pwm-servo-driver/hooking-it-up)
[^1.3]: [What voltage to supply to PCA9685 - '3.3V or 5V both works'](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf#page=39)
[^4]: [When `conda activate` is not working](https://github.com/conda/conda/issues/7980#issuecomment-441358406)
[]: [Why some files in Linux doesn't have extension(like `python3.9`)](https://askubuntu.com/a/1188034)


#### Tips

**Where the Python interpreter being used is located**
```python
import sys
print(sys.executable)

# Output Example: '/usr/bin/python3.8'
## The `Python3.8` is the full name of the executable.
```
**Where the Python packages are installed**

*Need to find the certain difference between the two below*

- `~/.local/lib/<Python version>/site-packages`

- `/usr/lib/<Python version>`
