# Downloading installation script
# TODO: Bring always the latest version. Currently, the URL points to specific version(which was the latest when this script was written).
wget -P ~/Downloads/ https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-aarch64.sh
bash ~/Downloads/Anaconda3-2023.09-0-Linux-aarch64.sh

# Add PATH environment variable
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc

# Sourcing Anaconda commands as default Bash configuration
echo 'source ~/anaconda3/etc/profile.d/conda.sh' >> ~/.bashrc
# without the command above, `conda activate` will not run.

# Source Bash configuration
source ~/.bashrc