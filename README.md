# kytos-challenge
Kytos parser to OpenFlow messages.

## Usage
  This is a python script and you can call it from command line:

  ``$ python openflow_parser.py <message-file.dat>``

  For the moment the script supports only HELLO messages.
  You can run our example message passing the 'oftp_hello.dat' file as argument.

  **OUTPUT**
  The output message cotains the following information:

  - Protocol Version: Version of the protocol used to communicate in the network.
  - Message Type: Message type (Hello, Error, Reply, etc).
  - Size: N (bytes) The size of the message including the header.
  - xid: The id from where the message came.
  - Is valid: A True or False value calculated as a checksum for the message size and its content.
  - Body: The body of the message, if it has one. Some types of messages does not contain a body.


## License

  This repository and all its files are under GPL.v3 License.
  Check LICENSE file for more details

## Contrib

  You can contribute with this repository by opening issues or
  sending a PR :)
