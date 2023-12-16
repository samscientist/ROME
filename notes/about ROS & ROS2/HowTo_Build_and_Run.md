# How to Build Packages and Run it (ROS & ROS2)
> There are distinct differences between ROS and ROS2.<br/>
> But the main workflow in building packages is quite similar to each other as the diagram shown below.

$$
\begin{CD}
    \text{Place packages' source in ``src/" directory} \\
    @VVV \\
    \text{Build}\\
    @V\text{Source setup script}VV \\
    \begin{CD}
        \text{Ready to launch} @>launch>> \text{Run}
    \end{CD}
\end{CD}
$$

## ROS

### Before Build

```
< workspace_folder >/
│
└── src/
    ├── < package_1 name >/
    │   │
    │   ...
    ├── < package_2 name >/
    │   │
    │   ...
    │
    ...
    └── < package_n name >/
        │
        ...
```

### Build

- **Build Command:** `catkin_make`<br/>
  └── *// must be executed while the Shell's working directory is set to the ROS workspace folder*
- **New Directories**
  - `build/` :
  - `devel/` :
  - `log/` : 

```
< workspace_folder >/
├── build/
├── devel/
│   ├── setup.ps1
│   ├── setup.sh
|   ├── setup.zsh
│   ...
├── log/
└── src/
    │
    ...*same as before the build*

```

### Run

**Source setup script**
```bash
source ./devel/setup.bash
```

**Launch**
```bash
roslaunch <package name> <launch file>
```

## ROS2

### Before Build

```
< workspace_folder >/
│
└── src/
    ├── < package_1 name >/
    │   │
    │   ...
    ├── < package_2 name >/
    │   │
    │   ...
    │
    ...
    └── < package_n name >/
        │
        ...
```

```
workspace_folder/
│
└── src/
    ├── cpp_package_1/
    │   ├── CMakeLists.txt
    │   ├── include/cpp_package_1/
    │   ├── package.xml
    │   └── src/
    │
    ├── py_package_1/
    │   ├── package.xml
    │   ├── resource/py_package_1
    │   ├── setup.cfg
    │   ├── setup.py
    │   └── py_package_1/
    ...
```


### Build
- **Build Command:** `colcon build`<br/>
  └── *// must be executed while the Shell's working directory is set to the ROS workspace folder*
- **New Directories**
  - `build/` : 
  - `install/` : 
  - `log/` : 


```
< workspace_folder >/
├── build/
├── install/
│   ├── setup.ps1
│   ├── setup.sh
|   ├── setup.zsh
│   ...
├── log/
└── src/
    │
    ...*same as before the build*

```

### Run

**Source setup script**
```bash
source ./install/setup.bash
```

**Launch**
```bash
ros2 launch <package name> <launch file>
```

## Examples