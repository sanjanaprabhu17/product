from product import product_details

def test_product_details():
    expected_output = (
        "Product Name: Lenovo Laptop\n"
        "Product ID: P1001\n"
        "Price: 48000\n"
        "Quantity: 10\n"
    )
    assert product_details("Lenovo Laptop", "P1001", 48000, 10) == expected_output
