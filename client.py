class B2bFoodDistributorCatalogOrderEntryOsClient:
    def digitize_restaurant_invoice_order(self, restaurant_id='RST_MANHATTAN_BISTRO', voice_or_text_order='Need 4 crates Haas Avocados and 2 wheels Parmigiano Reggiano'):
        line_items = [
            {'sku': 'PRD_AVO_HAAS_48CT', 'name': 'Haas Avocados 48ct', 'qty_crates': 4, 'unit_price_usd': 58.0, 'subtotal_usd': 232.0},
            {'sku': 'PRD_CHEESE_PARM_24M', 'name': 'Parmigiano Reggiano 24-Month Wheel', 'qty_crates': 2, 'unit_price_usd': 420.0, 'subtotal_usd': 840.0}
        ]
        return {
            'digital_order_id': 'pep_ord_90124',
            'restaurant_id': restaurant_id,
            'parsed_line_items': line_items,
            'total_order_usd': 1072.0,
            'order_cutoff_met_for_next_morning': True,
            'automated_erp_sync_status': 'SYNCED_TO_DISTRIBUTOR_INVENTORY'
        }
