from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "J58", "9135262387"),
    Smartphone("Siemens", "A52", "9335695845"),
    Smartphone("Nokia", "B568", "9139856587"),
    Smartphone("Xiaomi", "15 ultra", "9239562458"),
    Smartphone("Honor", "600 PRO", "9337258456")
]

for smartphone in catalog:
    print(f"{smartphone.stamp} - {smartphone.model}. {smartphone.number}")