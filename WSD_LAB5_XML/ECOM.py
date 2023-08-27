from lxml import etree

# Load XML and XSL files

xml = etree.parse("WSD_LAB5_XML\ECOM.xml")
xsl = etree.parse("WSD_LAB5_XML\ECOM.xsl")
xsd = etree.parse("WSD_LAB5_XML\ECOM.xsd") 


# Apply XSL transformation
transform = etree.XSLT(xsl)
html = transform(xml)
print(html)

# Save transformed HTML to a file
with open('"WSD_LAB5_XML\ECOM.html', 'wb') as output_file:
    output_file.write(etree.tostring(html, pretty_print=True))

# Load XSD schema
schema = etree.XMLSchema(xsd)


# Validate transformed HTML against XSD schema
validation_result = schema.validate(xml)

if validation_result:
    print("Validation successful!")
else:
    print("Validation errors:")
    print("Validation Result :",validation_result)
    print(schema.error_log)