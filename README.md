# XferNgine

# OVERVIEW
XferNgine is a multi-tailed web service that enables conversion of data from one type to another.
Due to the intervention of multiple languages in a multilayered architecture, some older languages can’t work with newer data types right away. 

XferNgine breaks this barrier by providing APIs that are capable of transferring one form of newer data, say JSON; to older forms of data, say XML;. 

This enables parsing the data as native to the language as possible thus reducing the application’s complexity.
    
    The inclusion of XferNgine into your application might ensure the following factors:
        ● Support by other programming languages
        ● Reading / writing performance
        ● Compactness (file size)
# GOALS

    1. Type conversion of data without modifying the structure of the original incoming data.
    2. Support for as many data storage types as possible for scaling to multiple languages.
    3. Support for larger and multiple payloads per request.(experimental feature ahead, may result in data loss).
# SPECIFICATIONS
   As of proposing this solution, the design plan has the following accepted type conversions/ data transfers
4. JSON to XML Document
5. XML Document to JSON
6. Protobuf to XML
7. XML to Protobuf
8. ProtoBuf to JSON
9. JSON to Protobuf
10. CSV to JSON
11. JSON to CSV
12. MessagePack to JSON
13. MessagePack to XML
14. YAML to JSON
15. JSON to YAML
16. YAML to XML
17. XML to YAML
18. JSON to MessagePack
19. XML to MessagePack
