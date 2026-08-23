from client import B2bFoodDistributorCatalogOrderEntryOsClient

def main():
    client = B2bFoodDistributorCatalogOrderEntryOsClient()
    res = client.digitize_restaurant_invoice_order('RST_BROOKLYN_DINER', '4 crates Haas Avocados, 2 wheels Parmigiano')
    print('Digital Order: ' + res['digital_order_id'] + ' | Total: $' + str(res['total_order_usd']))
    print('Delivery: Next morning cutoff met ' + str(res['order_cutoff_met_for_next_morning']))
    for item in res['parsed_line_items']:
        print('  - ' + item['name'] + ' x' + str(item['qty_crates']) + ' ($' + str(item['subtotal_usd']) + ')')

if __name__ == '__main__':
    main()
