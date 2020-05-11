# Module that converts security.evtx to xml
import Evtx.Evtx as evt
# Module that parses xml
import xml.etree.ElementTree as ET


def main():
    # Path to security.evtx that will be parsed
    path = "<path to security.evtx>"

    # Path to .xml file that saves parsed info
    output_file = open("<path to output.xml>", "w")

    with evt.Evtx(path) as open_log:
        # Convert each security.evtx record to xml record
        for record in open_log.records():
            xml_record = record.xml()

            # Parse XML record
            tree = ET.fromstring(xml_record)

            # Iterate over all tree
            tags = tree.iter()
            for elem in tags:

                # Find needed EvenID number
                if "EventID" in elem.tag and "<EventID number ex. - 5379>" in elem.text:

                    # Write needed XML record to output file
                    output_file.write(xml_record)


if __name__ == "__main__":
    main()
