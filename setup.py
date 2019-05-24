import setuptools

setuptools.setup(
    name="stock-forcasting",
    version="0.0.3",
    author="Kalani Murakami",
    author_email="kalanimurakami1218@gmail.com",
    description="Helper to get the Stock data I want to forecase",
    packages=['stock_forcasting', 'analytics'],
    install_requires=["requests"],
    license="MIT",
    url="https://github.com/khmurakami/stock-forcasting"
)
