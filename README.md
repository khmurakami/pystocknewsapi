## pystocknewsapi

This is an Unofficial Wrapper for Pystocknewsapi

## Requirements

Also listed in requirements.txt:

-   requests

## Install

#### Install Locally

This has been tested with Python 2.7, 3.3, 3.4, 3.5, 3.6 and 3.6-dev

```shell
$ git clone https://github.com/khmurakami/pystocknewsapi
$ cd pystocknewsapi
$ python setup.py install
```

#### Install inside a Virtualenv

```shell
$ pip install virtualenv
$ python -m virutalenv env
$ source env/bin/activate
$ git clone https://github.com/khmurakami/pystocknewsapi
$ cd pystocknewsapi
$ python setup.py install
```

## Using the Python Wrapper

Descriptions of files can be found inside pystocktwits.py

## Samples

Code samples can be found in example_code/python_scripts
JSON sample outputs can be found in example_code/example_json_files

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python tests/pystocknewsapi_test.py
```

## Using Curl Requests to Test

These curl requests are from the Stocktwits API site and are not mine. They can be found here: <https://api.stocktwits.com/developers/docs>

```shell
$ cd example_curl_requests
$ ./streams_user_curl.sh
```

## TODO

- Figure out how the callback part works in the functions when making the web call.
- Create Flask App for the redirect uri

## Links/Credits

- Git Ignore Used in this Repo: https://github.com/github/gitignore/blob/master/Python.gitignore
