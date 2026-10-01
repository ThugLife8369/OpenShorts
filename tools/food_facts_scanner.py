import httpx

class OpenFoodFactsRetriever:
    """Fetches real ingredient and additive data to build highly factual, viral hooks."""
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org/api/v2/product/"

    async def scan_product(self, barcode: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}{barcode}.json")
            if response.status_code == 200:
                data = response.json().get("product", {})
                return {
                    "product_name": data.get("product_name", "Unknown"),
                    "ingredients_text": data.get("ingredients_text", "No data"),
                    "additives": data.get("additives_tags", []),
                    "nutriscore": data.get("nutriscore_grade", "unknown"),
                    "nova_group": data.get("nova_group", "unknown") # UPF indicator
                }
            return {"error": "Product not found or API unreachable"}
