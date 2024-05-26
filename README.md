# url-heartbeat

This is a simple container that will perform a GET call against a URL and log the response code. It is intended to be used with services that require a heartbeat such as Uptime Robot, etc.

## Getting Started

These instructions will cover usage information and for the docker container

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

```shell
docker run as6o/url-heartbeat -e URL=https://example.com -e PERIOD=60 -e TIMEOUT=5
```

#### Environment Variables

* `URL` - The URL that will be called via GET
* `PERIOD` - The period in seconds between calls
* `TIMEOUT` - The timeout in seconds for the call

#### Logging

Messages are sent to stdout and errors are sent to stderr.

## Find Us

* [GitHub](https://github.com/as6o/url_heartbeat)

## Authors

* **Aaron Siri** - *Initial work* - [as6o](https://github.com/as6o)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
