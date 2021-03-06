# XferNgine

## OverView
XferNgine is a multi-tailed web service that enables conversion of data from one type to another.
Due to the intervention of multiple languages in a multilayered architecture, some older languages can’t work with newer data types right away. 

XferNgine breaks this barrier by providing APIs that are capable of transferring one form of newer data, say JSON; to older forms of data, say XML;. 

This enables parsing the data as native to the language as possible thus reducing the application’s complexity.
    
* The inclusion of XferNgine into your application might ensure the following factors:
    * Support by other programming languages
    * Reading / writing performance
    * Compactness (file size)
## Goals

* Type conversion of data without modifying the structure of the original incoming data.
* Support for as many data storage types as possible for scaling to multiple languages.
* Support for larger and multiple payloads per request.(experimental feature ahead, may result in a loss).
## Specifications
   As of posing this solution, the design plan has the following accepted type conversions/ data transfers
From  | To
---------- | -------------
JSON       | XML Document
XML Document| JSON
Protobuf| XML
XML| Protobuf
ProtoBuf| JSON
JSON| Protobuf
CSV| JSON
JSON| CSV
MessagePack| JSON
MessagePack| XML
YAML| JSON
JSON| YAML
YAML| XML
XML| YAML
JSON| MessagePack
XML| MessagePack
