#!/usr/bin/env python
from setuptools import find_packages, setup

# from pip.req import parse_requirements

setup(
    name="phalp",
    version="0.1.3",
    description="PHALP: A Python package for People Tracking in 3D",
    url="https://github.com/hansen1416/PHALP",
    author="Jathushan Rajasegaran",
    author_email="jathushan@berkeley.edu",
    license="MIT License",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "opencv-python",
        "joblib",
        "scikit-learn",
        "pyrender",
        "dill",
        "rich",
        "einops",
        "scenedetect[opencv]",
        "hydra-core",
        "timm",
        "av",
        "smplx==0.1.28",
        "numpy",
        "detectron2 @ git+https://github.com/hansen1416/detectron2.git@a59f05630a8f205756064244bf5beb8661f96180",
        "pytube @ git+https://github.com/pytube/pytube.git",
        "pyopengl @ git+https://github.com/mmatl/pyopengl.git",
        "chumpy @ git+https://github.com/mattloper/chumpy",  # smplx dependency
        "neural-renderer-pytorch @ git+https://github.com/shubham-goel/NMR.git",
    ],
    extras_require={
        "all": [
            "hmr2 @ git+https://github.com/hansen1416/4D-Humans.git",
        ],
        "blur": ["facenet_pytorch"],
    },
    dependency_links=[],
)
