from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="suriname-hr-payroll",
    version="1.0.0",
    description="Suriname-compliant HR/Payroll module for ERPNext",
    author="Mark Nvesec",
    author_email="marknvesec@example.com",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)