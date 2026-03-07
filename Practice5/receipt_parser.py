import re
import json
def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    item_pattern = re.compile(r'\d+\.\n(.*?)\n[\d, ]+ x [\d, ]+\n([\d, ]+)', re.DOTALL)
    total_pattern = re.compile(r'ИТОГО:\n([\d, ]+)')
    date_pattern = re.compile(r'(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})')
    payment_pattern = re.compile(r'(Банковская карта|Наличные):')
    items = []
    product_matches = item_pattern.findall(content)
    for name, price in product_matches:
        items.append({
            "product_name": name.replace('\n', ' ').strip(),
            "price": price.replace(' ', '').replace(',', '.')
        })
    total_match = total_pattern.search(content)
    date_match = date_pattern.search(content)
    payment_match = payment_pattern.search(content)
    receipt_data = {
        "merchant": "EUROPHARMA",
        "date_time": date_match.group(1) if date_match else None,
        "payment_method": payment_match.group(1) if payment_match else None,
        "items": items,
        "total_calculated": sum(float(i['price']) for i in items),
        "total_on_receipt": total_match.group(1).replace(' ', '').replace(',', '.') if total_match else None
    }
    return receipt_data

if __name__ == "__main__":
    data = parse_receipt('raw.txt')
    print(json.dumps(data, indent=4, ensure_ascii=False))